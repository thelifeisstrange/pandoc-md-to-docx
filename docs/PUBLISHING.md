# Publishing releases

## Prerequisites

- PyPI account and [API token](https://pypi.org/manage/account/token/) (scope: entire account or project `md-to-docx`).
- GitHub repository secret **`PYPI_API_TOKEN`** for automated publishes (optional).

## Manual publish (TestPyPI first)

```bash
pip install build twine
python -m build
twine upload --repository testpypi dist/*
pip install --index-url https://test.pypi.org/simple/ "md-to-docx[binary]"
md-to-docx --version
```

When satisfied:

```bash
twine upload dist/*
```

## Tag a release

```bash
git tag -a v0.2.0 -m "v0.2.0"
git push origin v0.2.0
```

Update `CHANGELOG.md` and bump `version` in `pyproject.toml` and `src/md_to_docx/__init__.py` before tagging the next version.

## GitHub Actions

- **CI** (`.github/workflows/ci.yml`) runs on every push and pull request.
- **Publish** (`.github/workflows/publish.yml`) runs when a GitHub **Release** is published; uploads wheels/sdist to PyPI using `PYPI_API_TOKEN`.

To create a release from the CLI:

```bash
gh release create v0.2.0 --title "v0.2.0" --notes-file CHANGELOG.md
```
