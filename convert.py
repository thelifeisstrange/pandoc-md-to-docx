#!/usr/bin/env python3
"""Run the converter from a clone (auto-uses ./venv when present). Prefer `md-to-docx` after pip install."""
import os
import sys

_venv_python = os.path.join(os.path.dirname(os.path.abspath(__file__)), "venv", "bin", "python")
if os.path.exists(_venv_python) and sys.executable != _venv_python:
    os.execl(_venv_python, _venv_python, *sys.argv)

_root = os.path.dirname(os.path.abspath(__file__))
_src = os.path.join(_root, "src")
if _src not in sys.path:
    sys.path.insert(0, _src)

from md_to_docx.cli import main

if __name__ == "__main__":
    sys.exit(main())
