# Contributing

Thank you for helping improve **md-to-docx**. User-facing docs live in [README.md](README.md) and [docs/LIMITATIONS.md](docs/LIMITATIONS.md).

## Development setup

```bash
git clone https://github.com/thelifeisstrange/pandoc-md-to-docx.git
cd pandoc-md-to-docx
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -e ".[dev]"
pre-commit install         # optional
```

## Checks

```bash
ruff check src tests && ruff format --check src tests
pytest
```

## CI

GitHub Actions runs lint, then Linux and Windows tests (Python 3.12). If a run fails with **internal server error** or **job was not acquired**, re-run from the Actions tab—that is usually GitHub infrastructure, not your code.

## Maintainers

Release and PyPI steps are kept locally in **`docs/private/`** (gitignored), not in the public repo.
