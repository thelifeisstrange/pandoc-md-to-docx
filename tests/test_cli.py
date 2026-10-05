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


def test_cli_version():
    proc = subprocess.run(
        [sys.executable, "-m", "md_to_docx", "--version"],
        cwd=os.path.dirname(os.path.dirname(__file__)),
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0
    assert "0.2.0" in proc.stdout
