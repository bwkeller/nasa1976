"""NASA 1976 — a Sphinx theme after NHB 1430.2."""

from pathlib import Path

__version__ = "1.1.0"


def get_path() -> str:
    """Return the directory holding the theme, for ``html_theme_path``."""
    return str(Path(__file__).parent.parent.resolve())


def setup(app):
    app.add_html_theme("nasa1976", str(Path(__file__).parent.resolve()))
    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
