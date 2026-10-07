from __future__ import annotations

import os
import zipfile

import pytest

from md_to_docx.converter import ConversionError, ConvertOptions, OnExists, convert_md_to_docx
from md_to_docx.resources import bundled_reference_doc

FIXTURES = os.path.join(os.path.dirname(__file__), "fixtures")


def test_convert_basic_markdown(tmp_path):
    src = os.path.join(FIXTURES, "sample.md")
    out = tmp_path / "out.docx"
    result = convert_md_to_docx(
        src,
        ConvertOptions(output_file=str(out), on_exists=OnExists.REPLACE),
    )
    assert result == str(out)
    assert out.is_file()
    assert zipfile.is_zipfile(out)


def test_convert_embeds_relative_image(tmp_path):
    src = os.path.join(FIXTURES, "with_image.md")
    out = tmp_path / "with_image.docx"
    convert_md_to_docx(
        src,
        ConvertOptions(output_file=str(out), on_exists=OnExists.REPLACE),
    )
    with zipfile.ZipFile(out) as zf:
        media = [n for n in zf.namelist() if n.startswith("word/media/")]
        assert media, "expected embedded image under word/media/"


def test_missing_input_raises():
    with pytest.raises(ConversionError, match="does not exist"):
        convert_md_to_docx("/nonexistent/file.md", ConvertOptions(on_exists=OnExists.REPLACE))


def test_skip_existing(tmp_path):
    src = os.path.join(FIXTURES, "sample.md")
    out = tmp_path / "sample.docx"
    out.write_bytes(b"existing")
    with pytest.raises(ConversionError, match="Skipped"):
        convert_md_to_docx(
            src,
            ConvertOptions(output_file=str(out), on_exists=OnExists.SKIP),
        )


def test_convert_with_gfm(tmp_path):
    src = os.path.join(FIXTURES, "gfm_sample.md")
    out = tmp_path / "gfm.docx"
    convert_md_to_docx(
        src,
        ConvertOptions(output_file=str(out), on_exists=OnExists.REPLACE, from_format="gfm"),
    )
    assert out.is_file()


def test_convert_with_toc(tmp_path):
    src = os.path.join(FIXTURES, "sample.md")
    out = tmp_path / "toc.docx"
    convert_md_to_docx(
        src,
        ConvertOptions(output_file=str(out), on_exists=OnExists.REPLACE, toc=True, toc_depth=2),
    )
    with zipfile.ZipFile(out) as zf:
        doc_xml = zf.read("word/document.xml").decode("utf-8")
        assert "TOC" in doc_xml or "fldChar" in doc_xml


def test_bundled_reference_doc_exists():
    assert bundled_reference_doc().is_file()


def test_convert_with_bundled_reference(tmp_path):
    src = os.path.join(FIXTURES, "sample.md")
    out = tmp_path / "styled.docx"
    convert_md_to_docx(
        src,
        ConvertOptions(
            output_file=str(out),
            on_exists=OnExists.REPLACE,
            reference_doc=str(bundled_reference_doc()),
        ),
    )
    assert out.is_file()


def test_output_dir_created(tmp_path):
    src = os.path.join(FIXTURES, "sample.md")
    out_dir = tmp_path / "docs"
    result = convert_md_to_docx(
        src,
        ConvertOptions(output_dir=str(out_dir), on_exists=OnExists.REPLACE),
    )
    assert result == str(out_dir / "sample.docx")
    assert (out_dir / "sample.docx").is_file()
