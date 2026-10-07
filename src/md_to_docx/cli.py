from __future__ import annotations

import argparse
import glob
import os
import sys
from collections.abc import Iterable
from typing import Optional

from md_to_docx import __version__
from md_to_docx.converter import (
    DEFAULT_FROM_FORMAT,
    SUPPORTED_FROM_FORMATS,
    ConversionError,
    ConvertOptions,
    OnExists,
    convert_md_to_docx,
)
from md_to_docx.interactive import select_files_interactive
from md_to_docx.resources import bundled_reference_doc


def _resolve_reference_doc(path: Optional[str]) -> Optional[str]:
    if path is None:
        return None
    if path in ("bundled", "default"):
        return str(bundled_reference_doc())
    return path


def _collect_markdown_files(pattern: str, recursive: bool) -> list[str]:
    if recursive:
        root = pattern if os.path.isdir(pattern) else "."
        found: list[str] = []
        for dirpath, _, filenames in os.walk(root):
            for name in filenames:
                if name.lower().endswith(".md"):
                    found.append(os.path.join(dirpath, name))
        return sorted(found)

    if any(ch in pattern for ch in "*?[]"):
        return sorted(glob.glob(pattern))

    if os.path.isdir(pattern):
        return sorted(glob.glob(os.path.join(pattern, "*.md")))

    return sorted(glob.glob("*.md"))


def _on_exists_from_args(args: argparse.Namespace) -> OnExists:
    if args.force:
        return OnExists.REPLACE
    if args.skip_existing:
        return OnExists.SKIP
    if args.rename_on_exists:
        return OnExists.RENAME
    return OnExists.PROMPT


def _convert_many(paths: Iterable[str], options: ConvertOptions) -> int:
    exit_code = 0
    for path in paths:
        try:
            out = convert_md_to_docx(path, options)
            print(f"Conversion successful: '{path}' -> '{out}'")
        except ConversionError as e:
            msg = str(e)
            if msg.startswith("Skipped"):
                print(msg)
            else:
                print(f"Error: {msg}", file=sys.stderr)
                exit_code = 1
    return exit_code


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convert Markdown files to Word documents (.docx) using Pandoc.",
    )
    parser.add_argument(
        "input",
        nargs="*",
        help="Input .md file(s), directory, or glob. Opens interactive picker if omitted.",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Output .docx path (single input file only).",
    )
    parser.add_argument(
        "-d",
        "--output-dir",
        help="Directory for generated .docx files (batch mode).",
    )
    parser.add_argument(
        "-f",
        "--force",
        action="store_true",
        help="Replace existing output files without prompting.",
    )
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help="Skip conversion when the output file already exists.",
    )
    parser.add_argument(
        "--rename-on-exists",
        action="store_true",
        help="Write to 'name (1).docx' when output already exists (non-interactive friendly).",
    )
    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help="With no inputs, scan current directory recursively for .md files (interactive).",
    )
    parser.add_argument(
        "--from",
        dest="from_format",
        default=DEFAULT_FROM_FORMAT,
        choices=sorted(SUPPORTED_FROM_FORMATS),
        help=(
            f"Pandoc input format (default: {DEFAULT_FROM_FORMAT}). "
            "Use gfm for GitHub-flavored Markdown."
        ),
    )
    parser.add_argument(
        "--reference-doc",
        metavar="PATH",
        help=(
            "Pandoc reference .docx for Word styles. "
            "Use 'bundled' for the package default template."
        ),
    )
    parser.add_argument(
        "--toc",
        action="store_true",
        help="Include a table of contents in the output document.",
    )
    parser.add_argument(
        "--toc-depth",
        type=int,
        metavar="N",
        help="Heading depth for --toc (default: Pandoc default).",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    return parser


def main(argv: Optional[list[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    on_exists = _on_exists_from_args(args)
    if sum([args.force, args.skip_existing, args.rename_on_exists]) > 1:
        print(
            "Error: use only one of --force, --skip-existing, or --rename-on-exists.",
            file=sys.stderr,
        )
        return 2

    reference_doc = _resolve_reference_doc(args.reference_doc)
    base_options = ConvertOptions(
        output_dir=args.output_dir,
        on_exists=on_exists,
        from_format=args.from_format,
        reference_doc=reference_doc,
        toc=args.toc,
        toc_depth=args.toc_depth,
    )

    if not args.input:
        md_files = _collect_markdown_files(".", recursive=args.recursive)
        if not md_files:
            print("No Markdown (.md) files found.", file=sys.stderr)
            return 1
        selected = select_files_interactive(md_files)
        if not selected:
            print("Conversion cancelled.")
            return 0
        return _convert_many(selected, base_options)

    if len(args.input) == 1:
        options = ConvertOptions(
            output_file=args.output,
            output_dir=args.output_dir,
            on_exists=on_exists,
            from_format=args.from_format,
            reference_doc=reference_doc,
            toc=args.toc,
            toc_depth=args.toc_depth,
        )
        return _convert_many([args.input[0]], options)

    if args.output:
        print(
            "Warning: --output is ignored when multiple input files are provided.",
            file=sys.stderr,
        )
    return _convert_many(args.input, base_options)


if __name__ == "__main__":
    sys.exit(main())
