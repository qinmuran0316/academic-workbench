#!/usr/bin/env python3
"""Read DXF with optional ezdxf; report geometry without modifying the file.

Exit 0: parsed/audited; 1: invalid or required units mismatch; 2: dependency missing.
This is a parser audit, not AutoCAD validation or engineering certification.
"""
import argparse
from collections import Counter
import json
import math
from pathlib import Path
import sys


def ensure_finite(value):
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError('nonfinite numerical geometry or metadata')
    if isinstance(value, dict):
        for item in value.values():
            ensure_finite(item)
    elif isinstance(value, (tuple, list)):
        for item in value:
            ensure_finite(item)


def inspect(path, require_mm=False):
    try:
        import ezdxf
        from ezdxf import bbox, units
    except ImportError:
        return {'valid': False, 'status': 'dependency_missing', 'dependency': 'ezdxf',
                'suggested_command': 'python -m pip install ezdxf',
                'native_application_checked': False}, 2
    try:
        doc = ezdxf.readfile(path)
        space = doc.modelspace()
        code = int(doc.units)
        report = {'valid': True, 'file': str(path), 'dxf_version': doc.dxfversion,
                  'units': {'code': code, 'name': units.unit_name(code)},
                  'entity_counts': dict(Counter(e.dxftype() for e in space)),
                  'layers': [layer.dxf.name for layer in doc.layers],
                  'circles': [], 'polylines': [], 'dimensions': [],
                  'native_application_checked': False, 'issues': []}
        for entity in space:
            kind = entity.dxftype()
            if kind == 'CIRCLE':
                report['circles'].append({'center': list(entity.dxf.center),
                                          'radius': float(entity.dxf.radius), 'layer': entity.dxf.layer})
            elif kind == 'LWPOLYLINE':
                report['polylines'].append({'closed': bool(entity.closed),
                                           'points': [list(p) for p in entity.get_points('xyb')],
                                           'layer': entity.dxf.layer})
            elif kind == 'DIMENSION':
                try:
                    measurement = entity.get_measurement()
                    if hasattr(measurement, '__iter__'):
                        measurement = list(measurement)
                except (ValueError, TypeError, AttributeError):
                    measurement = None
                report['dimensions'].append({'type': entity.dimtype,
                                             'measurement': measurement,
                                             'text_override': entity.dxf.get('text', ''),
                                             'layer': entity.dxf.layer})
        ensure_finite(report)
        try:
            ext = bbox.extents(space, fast=False)
            report['bounds'] = {'min': list(ext.extmin), 'max': list(ext.extmax)} if ext.has_data else None
        except (ValueError, TypeError, AttributeError) as exc:
            report['bounds'] = None
            report['issues'].append(f'bounds unavailable: {exc}')
        auditor = doc.audit()
        report['audit'] = {'errors': len(auditor.errors), 'fixes': len(auditor.fixes)}
        if auditor.errors or auditor.fixes:
            report['issues'].append('parser audit found errors or in-memory repairs; original file was not rewritten')
        if require_mm and code != 4:
            report['issues'].append('millimeter units required ($INSUNITS=4)')
        report['valid'] = not report['issues']
        ensure_finite(report)
        return report, 0 if report['valid'] else 1
    except Exception as exc:
        return {'valid': False, 'status': 'parse_failed', 'error': str(exc),
                'native_application_checked': False}, 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('file', type=Path)
    parser.add_argument('--require-mm', action='store_true')
    args = parser.parse_args()
    result, code = inspect(args.file, args.require_mm)
    print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))
    return code


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    sys.exit(main())
