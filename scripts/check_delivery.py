#!/usr/bin/env python3
"""Check delivery structure, signatures and recorded evidence; never execute commands.

Exit 0: structure complete. Exit 1: invalid artifact/manifest or failed required check.
Exit 2: valid structure but required verification not run. This does NOT certify
academic correctness, native application compatibility, or the truth of test logs.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path, PureWindowsPath
import re
import sys
import xml.etree.ElementTree as ET
import zipfile


def reject_constant(value):
    raise ValueError(f'Nonfinite JSON number: {value}')


def finite_float(value):
    number = float(value)
    if not math.isfinite(number):
        raise ValueError(f'Nonfinite JSON number: {value}')
    return number


def inside(root, value):
    if not isinstance(value, str) or not value.strip():
        raise ValueError('path must be a nonempty relative string')
    portable = value.replace('\\', '/')
    if PureWindowsPath(value).drive or portable.startswith('/') or ':' in portable or '\x00' in portable:
        raise ValueError('absolute paths, drive-relative paths and alternate streams are not allowed')
    target = (root / portable).resolve()
    if not target.is_relative_to(root):
        raise ValueError('path escapes delivery root')
    return target


def inspect_format(path):
    suffix = path.suffix.lower()
    if suffix in ('.docx', '.xlsx', '.pptx'):
        part = {'.docx': 'word/document.xml', '.xlsx': 'xl/workbook.xml',
                '.pptx': 'ppt/presentation.xml'}[suffix]
        with zipfile.ZipFile(path) as archive:
            if archive.testzip() is not None:
                raise ValueError('damaged OpenXML ZIP member')
            types = ET.fromstring(archive.read('[Content_Types].xml'))
            if types.tag != '{http://schemas.openxmlformats.org/package/2006/content-types}Types':
                raise ValueError('invalid OpenXML content-types root')
            document = ET.fromstring(archive.read(part))
            part_roots = {
                '.docx': ('wordprocessingml', 'document'),
                '.xlsx': ('spreadsheetml', 'workbook'),
                '.pptx': ('presentationml', 'presentation'),
            }
            domain, tag = part_roots[suffix]
            accepted = {f'{{http://schemas.openxmlformats.org/{domain}/2006/main}}{tag}',
                        f'{{http://purl.oclc.org/ooxml/{domain}/main}}{tag}'}
            if document.tag not in accepted:
                raise ValueError('invalid OpenXML document root or namespace')
        return 'openxml_member_roots_only'
    if suffix == '.pdf':
        with path.open('rb') as stream:
            if not stream.read(8).startswith(b'%PDF-'):
                raise ValueError('not a PDF header')
            stream.seek(max(0, path.stat().st_size - 2048))
            if b'%%EOF' not in stream.read():
                raise ValueError('PDF EOF marker missing')
        return 'pdf_header_and_eof_only'
    if suffix == '.dwg':
        with path.open('rb') as stream:
            if not re.fullmatch(rb'AC10\d\d', stream.read(6)):
                raise ValueError('not a recognized DWG header')
        return 'dwg_header_only_native_check_required'
    if suffix == '.svg':
        root_tag = ET.parse(path).getroot().tag
        if root_tag.rsplit('}', 1)[-1] != 'svg':
            raise ValueError('XML root is not SVG')
        return 'svg_xml_structure'
    if suffix == '.dxf':
        with path.open('rb') as stream:
            prefix = stream.read(4096)
        if prefix.startswith(b'AutoCAD Binary DXF\r\n\x1a\x00'):
            return 'binary_dxf_header_only'
        text = path.read_text(encoding='utf-8-sig', errors='replace')
        pairs = [item.strip() for item in text.splitlines()]
        if 'SECTION' not in pairs or 'ENTITIES' not in pairs or not pairs or pairs[-1] != 'EOF':
            raise ValueError('DXF section/ENTITIES/EOF structure missing')
        return 'ascii_dxf_tokens_only_use_inspect_dxf_for_geometry'
    if suffix == '.json':
        json.loads(path.read_text(encoding='utf-8-sig'), parse_constant=reject_constant,
                   parse_float=finite_float)
        return 'json_parse'
    return 'nonempty_file_only'


def validate(manifest_path, root):
    result = {'valid': False, 'complete': False, 'validation_scope': 'structure_and_recorded_evidence',
              'errors': [], 'warnings': [], 'artifacts': [], 'checks': []}
    errors, warnings = result['errors'], result['warnings']
    try:
        payload = json.loads(manifest_path.read_text(encoding='utf-8-sig'), parse_constant=reject_constant,
                             parse_float=finite_float)
        if not isinstance(payload, dict) or type(payload.get('schema_version')) is not int or payload['schema_version'] != 1:
            raise ValueError('schema_version must be integer 1')
        task = payload.get('task')
        if not isinstance(task, dict) or not isinstance(task.get('id'), str) or not task['id'].strip():
            raise ValueError('task.id must be nonempty')
        if type(task.get('synthetic')) is not bool:
            raise ValueError('task.synthetic must be boolean')
        for field in ('deliverables', 'checks', 'limitations'):
            if not isinstance(payload.get(field), list):
                raise ValueError(f'{field} must be an array')
        if not payload['deliverables']:
            raise ValueError('at least one deliverable is required')
    except (OSError, ValueError, TypeError, KeyError) as exc:
        errors.append(f'manifest: {exc}')
        return result, 1
    seen = set()
    for item in payload['deliverables']:
        label = item.get('path', '<missing>') if isinstance(item, dict) else '<invalid>'
        try:
            if not isinstance(item, dict):
                raise ValueError('deliverable must be an object')
            if type(item.get('required', True)) is not bool:
                raise ValueError('required must be boolean')
            target = inside(root, item.get('path'))
            key = str(target).casefold() if sys.platform == 'win32' else str(target)
            if key in seen:
                raise ValueError('duplicate deliverable path')
            seen.add(key)
            if not target.is_file():
                if item.get('required', True):
                    raise ValueError('required file does not exist')
                warnings.append(f'{label}: optional file missing')
                continue
            size = target.stat().st_size
            if size == 0:
                raise ValueError('file is empty')
            with target.open('rb') as stream:
                hasher = hashlib.sha256()
                for block in iter(lambda: stream.read(1024 * 1024), b''):
                    hasher.update(block)
                digest = hasher.hexdigest()
            if 'sha256' in item and (not isinstance(item['sha256'], str) or digest != item['sha256'].lower()):
                raise ValueError('SHA-256 mismatch')
            probe = inspect_format(target)
            result['artifacts'].append({'path': label, 'bytes': size, 'sha256': digest, 'format_check': probe})
            if 'only' in probe:
                warnings.append(f'{label}: {probe}; deeper or native validation is separate')
        except (OSError, ValueError, TypeError, KeyError, zipfile.BadZipFile, ET.ParseError, RuntimeError) as exc:
            errors.append(f'{label}: {exc}')
    pending = False
    check_ids = set()
    for check in payload['checks']:
        label = check.get('id', '<missing>') if isinstance(check, dict) else '<invalid>'
        try:
            if not isinstance(check, dict) or not isinstance(label, str) or not label.strip() or label == '<missing>':
                raise ValueError('check.id must be nonempty')
            if label in check_ids:
                raise ValueError('duplicate check id')
            check_ids.add(label)
            status = check.get('status')
            if status not in ('passed', 'failed', 'not_run', 'not_applicable'):
                raise ValueError('unknown check status')
            if type(check.get('required', True)) is not bool:
                raise ValueError('required must be boolean')
            if status in ('passed', 'failed'):
                evidence = inside(root, check.get('evidence'))
                if not evidence.is_file() or evidence.stat().st_size == 0:
                    raise ValueError('executed check requires nonempty evidence file')
            if status == 'failed' and check.get('required', True):
                errors.append(f'{label}: required check failed')
            if status == 'not_run':
                warnings.append(f'{label}: not run')
                pending = pending or check.get('required', True)
            if status == 'not_applicable':
                reason = check.get('reason')
                if not isinstance(reason, str) or not reason.strip():
                    raise ValueError('not_applicable requires a nonempty reason')
            result['checks'].append({'id': label, 'status': status})
        except (OSError, ValueError, TypeError) as exc:
            errors.append(f'{label}: {exc}')
    result['limitations'] = payload['limitations']
    result['valid'] = not errors
    result['complete'] = not errors and not pending
    return result, 1 if errors else (2 if pending else 0)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manifest', type=Path)
    parser.add_argument('--root', type=Path, help='Delivery root, defaults to manifest parent')
    args = parser.parse_args()
    root = (args.root or args.manifest.parent).resolve()
    report, code = validate(args.manifest.resolve(), root)
    print(json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False))
    return code


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    sys.exit(main())
