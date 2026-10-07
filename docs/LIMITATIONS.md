# Conversion limitations

This tool is a thin wrapper around [Pandoc](https://pandoc.org/). Word output quality and supported syntax depend on your Pandoc version and the input format you choose (`--from`).

## Markdown dialect

- Default input is Pandoc **`markdown`** (Pandoc’s extended Markdown).
- Use **`--from gfm`** for GitHub-flavored Markdown (tables, task lists, strikethrough where Pandoc supports them).
- Features that work on GitHub but not in Word (e.g. some HTML blocks, custom containers) may be dropped or simplified.

## Images and files

- Local images use paths relative to the **markdown file’s directory** (via `--resource-path`).
- Remote `https://` images are embedded only if Pandoc can download them at conversion time.
- Missing files usually produce warnings in Pandoc stderr; the CLI may still exit 0 with partial output.

## Word-specific behavior

- **`--reference-doc`** / **`--reference-doc bundled`** controls styles (headings, body text, code). It does not preserve arbitrary CSS from HTML-heavy markdown.
- **`--toc`** adds a Word table of contents field; users may need to **Update Table** in Word after opening.
- Complex layout (multi-column, floating figures, precise pagination) is not a goal of this converter.

## Math and code

- **LaTeX math** (`$...$`, `$$...$$`) depends on Pandoc’s math → Word path; display may differ from PDF/LaTeX exports.
- **Syntax highlighting** in code fences becomes styled runs in Word, not an editable “code block” object like in some editors.

## Interactive mode

- The curses picker requires a **TTY** and may not work in all terminals on Windows; prefer CLI arguments in scripts and CI.

## Pandoc installation

- Without system Pandoc, install the optional binary extra: `pip install "md-to-docx[binary]"`.
- CI and tests assume Pandoc is available (via `pypandoc_binary` in dev dependencies).
