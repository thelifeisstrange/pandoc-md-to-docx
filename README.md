# Markdown to Docx Converter

[![CI](https://github.com/thelifeisstrange/md-to-docx/actions/workflows/ci.yml/badge.svg)](https://github.com/thelifeisstrange/md-to-docx/actions/workflows/ci.yml)
[![PyPI version](https://img.shields.io/pypi/v/md-to-docx)](https://pypi.org/project/md-to-docx/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Convert Markdown (`.md`) files to Microsoft Word (`.docx`) using [Pandoc](https://pandoc.org/), with an optional interactive file picker and batch CLI.

## Features

- **CLI and interactive UI** — convert paths directly or pick files with the terminal menu
- **Batch conversion** — multiple inputs; optional `--output-dir`
- **Asset paths** — resolves images relative to each Markdown file
- **Automation-friendly** — `--force`, `--skip-existing`, `--rename-on-exists`, exit codes
- **GitHub Markdown** — `--from gfm` for GitHub-flavored input
- **Word styling** — `--reference-doc`, bundled template (`--reference-doc bundled`), `--toc`
- **Local venv** — `./convert.py` re-execs into `venv/bin/python` when present

See [docs/LIMITATIONS.md](docs/LIMITATIONS.md) for Pandoc/Word caveats.

## Requirements

- Python 3.9+
- Pandoc (system install) **or** `pypandoc_binary` via optional extra

## Installation

From PyPI:

```bash
pip install "md-to-docx[binary]"
```

From a clone:

```bash
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -e ".[dev]"
pre-commit install         # optional
```

## Usage

### Command line

```bash
md-to-docx notes.md
md-to-docx notes.md -o report.docx --force
md-to-docx README.md --from gfm --reference-doc bundled
md-to-docx chapter1.md chapter2.md -d ./output --skip-existing
md-to-docx long-doc.md --toc --toc-depth 3 --reference-doc my-template.docx
```

### Interactive mode

```bash
md-to-docx
md-to-docx -r   # include .md files in subdirectories
```

Use **Space** to multi-select, **Enter** to convert, **Esc** to cancel.

### From a clone (without activating venv)

```bash
./convert.py input.md --force
python -m md_to_docx input.md --force
```

## Development

```bash
pip install -e ".[dev]"
ruff check src tests && ruff format --check src tests
pytest
```

CI runs lint, then Linux and Windows tests (Python 3.12). If GitHub reports a runner
**internal server error** or **job was not acquired**, re-run the workflow from the
Actions tab or use **Run workflow** (`workflow_dispatch`); that is usually infrastructure,
not a failing test.

Release process: [docs/PUBLISHING.md](docs/PUBLISHING.md). History: [CHANGELOG.md](CHANGELOG.md).

## License

MIT — see [LICENSE](LICENSE).
