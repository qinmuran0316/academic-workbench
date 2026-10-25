#!/usr/bin/env python3
"""Read-only local capability inventory; never probes the network or installs tools."""
import importlib.util
import json
import platform
import shutil
import sys


def collect():
    executables = ['python', 'python3', 'java', 'javac', 'mvn', 'gradle', 'node',
                   'pandoc', 'libreoffice', 'soffice', 'pdftoppm', 'mutool',
                   'inkscape', 'dot', 'xelatex', 'latexmk', 'tectonic', 'typst',
                   'octave', 'blender', 'ODAFileConverter']
    modules = ['ezdxf', 'numpy', 'sympy', 'matplotlib', 'docx', 'openpyxl',
               'pptx', 'reportlab', 'pypdf', 'fitz', 'PIL']
    packages = {}
    for name in modules:
        try:
            packages[name] = importlib.util.find_spec(name) is not None
        except (ImportError, ValueError, AttributeError):
            packages[name] = False
    return {'python': {'version': platform.python_version(), 'executable': sys.executable},
            'system': platform.system(),
            'executables': {name: shutil.which(name) for name in executables},
            'packages': packages, 'network': 'not_probed',
            'desktop_app_validation': 'not_performed',
            'note': 'Presence is not a successful execution test. Host chat/file/browser tools must be checked separately.'}


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    print(json.dumps(collect(), ensure_ascii=False, indent=2))
