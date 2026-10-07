# Markdown to Word (.docx)

**Turn Markdown files into Microsoft Word documents—images, links, tables, and code included.**

- **GitHub:** [thelifeisstrange/md-to-docx](https://github.com/thelifeisstrange/md-to-docx)
- **PyPI:** [pandoc-md-to-docx](https://pypi.org/project/pandoc-md-to-docx/) (install name; the command is still `md-to-docx`)

[![CI](https://github.com/thelifeisstrange/md-to-docx/actions/workflows/ci.yml/badge.svg)](https://github.com/thelifeisstrange/md-to-docx/actions/workflows/ci.yml)
[![PyPI version](https://img.shields.io/pypi/v/pandoc-md-to-docx)](https://pypi.org/project/pandoc-md-to-docx/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/thelifeisstrange/md-to-docx/blob/main/LICENSE)

---

## Quick start

```bash
pip install "pandoc-md-to-docx[binary]"
md-to-docx your-notes.md --force
```

This creates **`your-notes.docx`** next to your Markdown file. The `[binary]` extra bundles Pandoc so you do not need a separate Pandoc install.

---

## What this tool does

`md-to-docx` converts `.md` files to `.docx` using the industry-standard [Pandoc](https://pandoc.org/) engine. It adds a friendly command-line interface on top:

| You get | How |
|--------|-----|
| **One command per file or many** | Pass paths on the command line, or pick files in a simple terminal menu |
| **Sensible defaults** | Output name matches the input (`report.md` → `report.docx`) |
| **Safe overwrites** | Prompts in the terminal, or `--force` / `--skip-existing` for scripts |
| **GitHub READMEs** | `--from gfm` for GitHub-flavored Markdown |
| **Word that looks intentional** | Built-in style template (`--reference-doc bundled`) and optional table of contents |

It is aimed at **documentation, notes, specs, and READMEs** you need to share as Word—not at replacing a full document designer.

---

## Why use this instead of copy-paste or Pandoc alone?

- **Copy-paste from VS Code or GitHub** often breaks tables, code blocks, and images. This produces a real `.docx` with embedded assets.
- **Raw `pandoc` commands** are easy to forget (`--resource-path`, reference doc, TOC flags). This tool sets the important defaults for you—especially **where to look for images**.
- **Batch and automation** — convert many files, set an output folder, and use exit codes in CI or shell scripts.
- **Optional interactive picker** — no need to type paths when you are working in a folder full of `.md` files.

---

## Images and links (how they are handled)

### Local images

Markdown like this:

```markdown
![Architecture diagram](./images/architecture.png)
```

**How we handle it:** For each input file, Pandoc’s `--resource-path` is set to **that file’s directory**. Relative paths such as `./images/...` or `images/...` are resolved from the folder where the `.md` lives—not from where you run the command.

**Tip:** Keep images in a folder next to the Markdown (for example `docs/guide.md` and `docs/images/...`).

### Remote images and URLs

```markdown
![Logo](https://example.com/logo.png)
[Project site](https://example.com)
```

**How we handle it:** Pandoc embeds or links according to its normal rules. HTTPS images are fetched at convert time when Pandoc can reach them. Standard markdown links become clickable links in Word.

### When something is missing

If a **local** image path does not exist, Pandoc may omit the image or warn on stderr. Check your paths relative to the `.md` file. More detail: [Limitations](https://github.com/thelifeisstrange/md-to-docx/blob/main/docs/LIMITATIONS.md).

---

## Features

- **CLI** — convert one or many files; custom output path (`-o`) or output directory (`-d`)
- **Interactive UI** — run `md-to-docx` with no arguments; navigate with arrow keys, Space to select, Enter to convert
- **Recursive scan** — `md-to-docx -r` finds `.md` files in subfolders (interactive mode)
- **Input formats** — `--from markdown` (default), `--from gfm`, CommonMark variants
- **Word styling** — `--reference-doc bundled` (included template) or your own `.docx` template
- **Table of contents** — `--toc` and optional `--toc-depth`
- **Automation** — `--force`, `--skip-existing`, `--rename-on-exists`; meaningful exit codes
- **Cross-platform** — tested on Linux and Windows in CI

---

## Installation

### From PyPI (recommended)

```bash
pip install "pandoc-md-to-docx[binary]"
```

| Extra | Purpose |
|-------|---------|
| `[binary]` | Includes `pypandoc_binary` (Pandoc bundled—easiest for most users) |
| (none) | Uses `pypandoc` only—you must install [Pandoc](https://pandoc.org/installing.html) yourself |

### From GitHub

```bash
git clone https://github.com/thelifeisstrange/md-to-docx.git
cd md-to-docx
python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -e ".[dev]"
```

---

## Usage examples

```bash
# Basic: creates notes.docx beside notes.md
md-to-docx notes.md

# Custom output location, overwrite without asking
md-to-docx notes.md -o ~/Desktop/report.docx --force

# GitHub-style README + bundled Word styles
md-to-docx README.md --from gfm --reference-doc bundled --force

# Many files into one folder
md-to-docx ch1.md ch2.md ch3.md -d ./word-output --skip-existing

# Long document with table of contents
md-to-docx spec.md --toc --toc-depth 3 --reference-doc bundled --force
```

### Interactive mode

```bash
md-to-docx       # .md files in current directory
md-to-docx -r    # include subdirectories
```

**Controls:** ↑/↓ move, **Space** toggle selection, **Enter** convert, **Esc** cancel.

### Clone-only shortcut

If you cloned the repo and use the bundled `venv`:

```bash
./convert.py myfile.md --force
python -m md_to_docx myfile.md --force
```

---

## Command reference

| Option | Description |
|--------|-------------|
| `-o`, `--output` | Output `.docx` path (single input only) |
| `-d`, `--output-dir` | Directory for output files (batch) |
| `-f`, `--force` | Overwrite existing output without prompting |
| `--skip-existing` | Skip if output already exists |
| `--rename-on-exists` | Write `name (1).docx`, etc. |
| `--from` | Input format: `markdown`, `gfm`, `commonmark`, … |
| `--reference-doc` | Path to style template, or `bundled` |
| `--toc` | Add a table of contents |
| `--toc-depth N` | Heading levels included in TOC |
| `-r`, `--recursive` | Scan subfolders (interactive mode only) |
| `--version` | Print version and exit |

---

## Requirements

- **Python 3.9+**
- **Pandoc** — via `pip install "pandoc-md-to-docx[binary]"` or a system install

---

## Documentation

| Public (in git) | Purpose |
|-----------------|--------|
| [README.md](https://github.com/thelifeisstrange/md-to-docx/blob/main/README.md) | Install, usage, images & links |
| [docs/LIMITATIONS.md](https://github.com/thelifeisstrange/md-to-docx/blob/main/docs/LIMITATIONS.md) | Pandoc / Word caveats |
| [CHANGELOG.md](https://github.com/thelifeisstrange/md-to-docx/blob/main/CHANGELOG.md) | Release history |

Maintainer-only files (PyPI tokens, `.env`, release checklists) stay **local** under `docs/private/` and are not committed.

## Development

Contributions and issues: **[github.com/thelifeisstrange/md-to-docx](https://github.com/thelifeisstrange/md-to-docx)**

```bash
pip install -e ".[dev]"
ruff check src tests && ruff format --check src tests
pytest
```

Release notes: [CHANGELOG.md](https://github.com/thelifeisstrange/md-to-docx/blob/main/CHANGELOG.md)

---

## License

MIT — see [LICENSE](https://github.com/thelifeisstrange/md-to-docx/blob/main/LICENSE).
