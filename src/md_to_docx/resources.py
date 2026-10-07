from __future__ import annotations

from functools import lru_cache
from pathlib import Path


@lru_cache(maxsize=1)
def bundled_reference_doc() -> Path:
    """Path to the Pandoc default reference.docx shipped with this package."""
    path = Path(__file__).resolve().parent / "templates" / "reference.docx"
    if not path.is_file():
        raise FileNotFoundError(f"Bundled reference template not found: {path}")
    return path
