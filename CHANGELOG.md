# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.4] - 2025-10-08

### Changed

- GitHub repository URL updated to [thelifeisstrange/pandoc-md-to-docx](https://github.com/thelifeisstrange/pandoc-md-to-docx) in README and PyPI project metadata.

## [0.2.3] - 2025-10-08

### Changed

- README trimmed for PyPI/end users (no CI maintainer notes or publishing docs).
- Contributor/CI notes moved to `CONTRIBUTING.md`.

### Fixed

- CLI import on Windows without curses (lazy import of interactive mode).

## [0.2.2] - 2025-10-08

### Changed

- README rewritten for clarity (features, images/links, GitHub/PyPI links, PyPI-friendly URLs).
- PyPI metadata: longer summary, Documentation and Issues project URLs.
- Public docs only under `docs/` (`LIMITATIONS.md`); maintainer publishing notes moved to gitignored `docs/private/`.

## [0.2.1] - 2025-10-06

### Changed

- PyPI distribution renamed to **`pandoc-md-to-docx`** (`md-to-docx` on PyPI is another project). The CLI command is still **`md-to-docx`**.

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

[0.2.0]: https://github.com/thelifeisstrange/pandoc-md-to-docx/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/thelifeisstrange/pandoc-md-to-docx/releases/tag/v0.1.0
