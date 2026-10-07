from __future__ import annotations

import os
import subprocess
import sys

FIXTURES = os.path.join(os.path.dirname(__file__), "fixtures")


def test_cli_single_file(tmp_path):
    out = tmp_path / "cli_out.docx"
    proc = subprocess.run(
        [
            sys.executable,
            "-m",
            "md_to_docx",
            os.path.join(FIXTURES, "sample.md"),
            "-o",
            str(out),
            "--force",
        ],
        cwd=os.path.dirname(os.path.dirname(__file__)),
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, proc.stderr
    assert out.is_file()


def test_cli_skip_existing(tmp_path):
    out = tmp_path / "skip.docx"
    src = os.path.join(FIXTURES, "sample.md")
    root = os.path.dirname(os.path.dirname(__file__))
    base_cmd = [sys.executable, "-m", "md_to_docx", src, "-o", str(out), "--force"]
    first = subprocess.run(base_cmd, cwd=root, capture_output=True, text=True)
    assert first.returncode == 0, first.stderr
    second = subprocess.run(
        [sys.executable, "-m", "md_to_docx", src, "-o", str(out), "--skip-existing"],
        cwd=root,
        capture_output=True,
        text=True,
    )
    assert second.returncode == 0, second.stderr
    assert "Skipped" in second.stdout


def test_cli_toc_flag(tmp_path):
    out = tmp_path / "cli_toc.docx"
    proc = subprocess.run(
        [
            sys.executable,
            "-m",
            "md_to_docx",
            os.path.join(FIXTURES, "sample.md"),
            "-o",
            str(out),
            "--force",
            "--toc",
        ],
        cwd=os.path.dirname(os.path.dirname(__file__)),
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, proc.stderr
    assert out.is_file()


def test_cli_version():
    proc = subprocess.run(
        [sys.executable, "-m", "md_to_docx", "--version"],
        cwd=os.path.dirname(os.path.dirname(__file__)),
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0
    assert "0.2.2" in proc.stdout
