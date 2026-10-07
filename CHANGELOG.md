# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2025-10-06

### Added

- Installable package (`md-to-docx` CLI, `src/md_to_docx/` layout).
- `--force`, `--skip-existing`, `--rename-on-exists` for non-interactive runs.
- `--output-dir`, `--reference-doc`, `--toc`, `--toc-depth`.
- `--from` input format (including `gfm` for GitHub-flavored Markdown).
- Bundled Pandoc reference template (`--reference-doc bundled`).
- Image resolution via Pandoc `--resource-path` (relative to each `.md` file).
- Pytest suite and GitHub Actions CI (Linux and Windows).
- MIT `LICENSE`.

### Changed

- Replaced monolithic `md_to_docx.py` with `convert.py` and `python -m md_to_docx`.
- Dependencies managed in `pyproject.toml` (removed root `requirements.txt`).

### Removed

- Sample markdown/docx fixtures from the repository root (use `tests/fixtures/`).

## [0.1.0] - 2025-07-12

### Added

- Initial single-script converter with interactive curses file picker.

[0.2.0]: https://github.com/thelifeisstrange/md-to-docx/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/thelifeisstrange/md-to-docx/releases/tag/v0.1.0
