from __future__ import annotations

import os
import sys
from dataclasses import dataclass
from enum import Enum
from typing import Optional

import pypandoc


class OnExists(str, Enum):
    PROMPT = "prompt"
    REPLACE = "replace"
    SKIP = "skip"
    RENAME = "rename"


class ConversionError(Exception):
    """Raised when conversion cannot be completed."""


DEFAULT_FROM_FORMAT = "markdown"

SUPPORTED_FROM_FORMATS = frozenset(
    {
        "markdown",
        "gfm",
        "commonmark",
        "commonmark_x",
        "markdown_strict",
    }
)


@dataclass
class ConvertOptions:
    output_file: Optional[str] = None
    output_dir: Optional[str] = None
    on_exists: OnExists = OnExists.PROMPT
    from_format: str = DEFAULT_FROM_FORMAT
    reference_doc: Optional[str] = None
    toc: bool = False
    toc_depth: Optional[int] = None
    extra_pandoc_args: Optional[list[str]] = None


def _resolve_output_path(input_file: str, options: ConvertOptions) -> str:
    if options.output_file is not None:
        return options.output_file

    base_name, _ = os.path.splitext(os.path.basename(input_file))
    if options.output_dir:
        os.makedirs(options.output_dir, exist_ok=True)
        return os.path.join(options.output_dir, f"{base_name}.docx")

    stem, _ = os.path.splitext(input_file)
    return f"{stem}.docx"


def _pick_output_if_exists(output_file: str, on_exists: OnExists) -> Optional[str]:
    if not os.path.exists(output_file):
        return output_file

    if on_exists == OnExists.REPLACE:
        return output_file

    if on_exists == OnExists.SKIP:
        return None

    if on_exists == OnExists.RENAME:
        base_name, ext = os.path.splitext(output_file)
        counter = 1
        while os.path.exists(f"{base_name} ({counter}){ext}"):
            counter += 1
        return f"{base_name} ({counter}){ext}"

    if on_exists != OnExists.PROMPT:
        raise ConversionError(f"Unknown on_exists policy: {on_exists}")

    if not sys.stdin.isatty():
        raise ConversionError(
            f"Output file '{output_file}' already exists. "
            "Use --force, --skip-existing, or --rename-on-exists in non-interactive mode."
        )

    print(f"Warning: The file '{output_file}' already exists.")
    while True:
        choice = input(
            "Do you want to (r)eplace it, (c)reate new, or (s)kip? [r/c/s]: "
        ).strip().lower()
        if choice == "r":
            return output_file
        if choice == "c":
            return _pick_output_if_exists(output_file, OnExists.RENAME)
        if choice == "s":
            return None
        print("Invalid choice. Please enter 'r', 'c', or 's'.")


def _pandoc_extra_args(input_file: str, options: ConvertOptions) -> list[str]:
    args: list[str] = []
    input_dir = os.path.dirname(os.path.abspath(input_file)) or "."
    args.extend(["--resource-path", input_dir])

    if options.reference_doc:
        if not os.path.isfile(options.reference_doc):
            raise ConversionError(f"Reference document not found: '{options.reference_doc}'")
        args.extend(["--reference-doc", os.path.abspath(options.reference_doc)])

    if options.toc:
        args.append("--toc")
        if options.toc_depth is not None:
            args.extend(["--toc-depth", str(options.toc_depth)])

    if options.extra_pandoc_args:
        args.extend(options.extra_pandoc_args)

    return args


def convert_md_to_docx(input_file: str, options: Optional[ConvertOptions] = None) -> str:
    """
    Convert a Markdown file to DOCX.

    Returns the path to the written DOCX file.

    Raises ConversionError on failure or when skipped due to existing output.
    """
    options = options or ConvertOptions()

    if not os.path.isfile(input_file):
        raise ConversionError(f"Input file '{input_file}' does not exist.")

    output_file = _resolve_output_path(input_file, options)
    output_file = _pick_output_if_exists(output_file, options.on_exists)
    if output_file is None:
        raise ConversionError(f"Skipped '{input_file}' (output already exists).")

    if options.from_format not in SUPPORTED_FROM_FORMATS:
        raise ConversionError(
            f"Unsupported input format '{options.from_format}'. "
            f"Choose from: {', '.join(sorted(SUPPORTED_FROM_FORMATS))}."
        )

    extra_args = _pandoc_extra_args(input_file, options)

    try:
        pypandoc.convert_file(
            input_file,
            "docx",
            format=options.from_format,
            outputfile=output_file,
            extra_args=extra_args,
        )
    except OSError as e:
        raise ConversionError(
            f"Conversion failed: {e}. "
            "Install Pandoc on your system or pip install 'pandoc-md-to-docx[binary]'."
        ) from e
    except RuntimeError as e:
        raise ConversionError(f"Conversion failed: {e}") from e

    return output_file
