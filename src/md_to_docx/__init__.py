"""Markdown to Word (.docx) conversion."""

__version__ = "0.2.0"

from md_to_docx.converter import ConversionError, convert_md_to_docx

__all__ = ["__version__", "ConversionError", "convert_md_to_docx"]
