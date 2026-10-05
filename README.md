# Markdown to Docx Converter

Convert Markdown (`.md`) files to Microsoft Word (`.docx`) using [Pandoc](https://pandoc.org/), with an optional interactive file picker and batch CLI.

## Features

- **CLI and interactive UI** — convert paths directly or pick files with the terminal menu
- **Batch conversion** — multiple inputs; optional `--output-dir`
- **Asset paths** — resolves images relative to each Markdown file (`--resource-path`)
- **Automation-friendly** — `--force`, `--skip-existing`, `--rename-on-exists`, exit codes
- **Optional styling** — `--reference-doc`, `--toc`, `--toc-depth`
- **Local venv** — `./convert.py` re-execs into `venv/bin/python` when present

## Requirements

- Python 3.9+
- Pandoc (system install) **or** `pypandoc_binary` via optional extra

## Installation

From a clone of this repository:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -e ".[dev]"
```

For end users (without cloning), after publishing to PyPI:

```bash
pip install "md-to-docx[binary]"
```

## Usage

### Command line

```bash
md-to-docx notes.md
md-to-docx notes.md -o report.docx --force
md-to-docx chapter1.md chapter2.md -d ./output --skip-existing
md-to-docx long-doc.md --toc --toc-depth 3 --reference-doc template.docx
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
pytest
```

## License

MIT — see [LICENSE](LICENSE).
