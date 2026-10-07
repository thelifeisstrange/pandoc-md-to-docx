# Markdown to Word (.docx)

**Turn Markdown files into Microsoft Word documents—images, links, tables, and code included.**

- **Source & issues:** [github.com/thelifeisstrange/md-to-docx](https://github.com/thelifeisstrange/md-to-docx)
- **Install from PyPI:** `pip install "pandoc-md-to-docx[binary]"` — run the tool as **`md-to-docx`**

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

`md-to-docx` converts `.md` files to `.docx` using [Pandoc](https://pandoc.org/). It wraps Pandoc with sensible defaults for everyday use:

| You get | How |
|--------|-----|
| **One command per file or many** | Pass paths on the command line, or pick files in a terminal menu (macOS/Linux) |
| **Sensible defaults** | Output name matches the input (`report.md` → `report.docx`) |
| **Safe overwrites** | Prompts in the terminal, or `--force` / `--skip-existing` for scripts |
| **GitHub READMEs** | `--from gfm` for GitHub-flavored Markdown |
| **Word that looks intentional** | Built-in style template (`--reference-doc bundled`) and optional table of contents |

Ideal for **documentation, notes, specs, and READMEs** you need to share as Word.

---

## Why use this instead of copy-paste or Pandoc alone?

- **Copy-paste from VS Code or GitHub** often breaks tables, code blocks, and images. This produces a real `.docx` with embedded assets.
- **Raw `pandoc` commands** are easy to forget (`--resource-path`, reference doc, TOC flags). This tool sets the important defaults—especially **where to look for images**.
- **Batch and automation** — convert many files, set an output folder, and use exit codes in scripts.

---

## Images and links

### Local images

```markdown
![Architecture diagram](./images/architecture.png)
```

For each input file, paths are resolved from **that file’s directory**, not from where you run the command. Keep images beside the `.md` file (e.g. `docs/guide.md` and `docs/images/...`).

### Remote images and links

```markdown
![Logo](https://example.com/logo.png)
[Project site](https://example.com)
```

HTTPS images are fetched when Pandoc can reach them. Markdown links become clickable links in Word.

For edge cases and limits, see [Limitations](https://github.com/thelifeisstrange/md-to-docx/blob/main/docs/LIMITATIONS.md) on GitHub.

---

## Installation

```bash
pip install "pandoc-md-to-docx[binary]"
```

| Extra | Purpose |
|-------|---------|
| `[binary]` | Bundled Pandoc (recommended) |
| (none) | You must install [Pandoc](https://pandoc.org/installing.html) yourself |

**Requirements:** Python 3.9+

---

## Usage examples

```bash
md-to-docx notes.md
md-to-docx notes.md -o ~/Desktop/report.docx --force
md-to-docx README.md --from gfm --reference-doc bundled --force
md-to-docx ch1.md ch2.md -d ./word-output --skip-existing
md-to-docx spec.md --toc --toc-depth 3 --reference-doc bundled --force
```

### Interactive mode (macOS / Linux)

```bash
md-to-docx       # .md files in current directory
md-to-docx -r    # include subdirectories
```

Use ↑/↓, **Space** to select, **Enter** to convert, **Esc** to cancel. On Windows, pass file paths on the command line instead.

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

## Help and feedback

- **Bug reports & feature requests:** [GitHub Issues](https://github.com/thelifeisstrange/md-to-docx/issues)
- **Release history:** [CHANGELOG](https://github.com/thelifeisstrange/md-to-docx/blob/main/CHANGELOG.md)

## License

MIT — see [LICENSE](https://github.com/thelifeisstrange/md-to-docx/blob/main/LICENSE).
