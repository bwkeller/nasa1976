# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

`sphinx-nasa1976` is a Sphinx HTML theme styled after NHB 1430.2, the 1976 NASA Graphics Standards Manual. It is a pure-Python package with no runtime code beyond theme registration; the work is in one Jinja template and one CSS template. There is no test suite, linter config, or example docs project in the repo.

## Commands

```bash
# Install editable into the current environment (pyproject is at repo root)
pip install -e .

# Build sdist/wheel
python -m build

# Verify a change: build any Sphinx project that sets html_theme = "nasa1976"
sphinx-build -b html <docs-src> <out-dir>
```

Note: the README's `pip install ./nasa1976_sphinx` refers to an old folder name. From this repo, `pip install .` is correct.

## How the theme is wired

Three registration paths exist and must stay consistent:

1. **Entry point** in `pyproject.toml`: `[project.entry-points."sphinx.html_themes"] nasa1976 = "nasa1976"`. Sphinx imports the package and calls `setup(app)`, which does `app.add_html_theme("nasa1976", <package dir>)`. This is why users need no `html_theme_path`.
2. **`get_path()`** in `nasa1976/__init__.py` returns the *parent* of the package (repo root) for manual `html_theme_path` use, since Sphinx looks for a subdirectory named after the theme.
3. **`package-data`** in `pyproject.toml` must list every non-.py file shipped (`theme.toml`, `*.html`, `static/*`). Adding a new template or static file requires no change unless it lands outside those globs.

`__version__` in `__init__.py` and `version` in `pyproject.toml` are both `1.0.0` and must be bumped together.

## Theme structure

- **`nasa1976/theme.toml`** — inherits `basic`; declares the stylesheet, default sidebars (`globaltoc.html`, `searchbox.html`), Pygments styles (`tango` light / `native` dark), and the `[options]` block. Every key under `[options]` becomes a `theme_<key>` Jinja variable available in both `layout.html` and the CSS template.
- **`nasa1976/layout.html`** — extends `basic/layout.html`. Blanks `relbar1`/`relbar2`, replaces `header`, `content`, and `footer`. Layout is a two-column CSS grid (`.nasa-margin` sidebar + `.nasa-body`). The mobile nav toggle is a pure-CSS checkbox (`#nasa-nav-toggle`), so there is deliberately no JavaScript.
- **`nasa1976/static/nasa1976.css_t`** — the `_t` suffix makes Sphinx render it as a Jinja template at build time. `{{ theme_accent_color }}` feeds `--nasa-red`, and `theme_color_scheme` decides how the dark token block is emitted: behind a `prefers-color-scheme: dark` media query (`auto`), unconditionally (`dark`), or not at all (`light`). `layout.html` mirrors the same option in the `color-scheme` meta tag and, when the scheme is fixed, overrides the `css` block so only the matching Pygments stylesheet (`pygments.css` or `pygments_dark.css`) is linked, without Sphinx's media query. Everything else is driven by CSS custom properties defined in `:root`.

### Design constraints to preserve

The CSS encodes rules from the manual that should not be casually broken:

- Two colours plus warm gray. Red (`--nasa-red`) is restricted to links, current nav item, focus rings, and `warning`/`danger`/`error`/`caution`/`attention` admonition labels. `note`/`tip`/`important`/`hint`/`seealso` get a black bar instead.
- Rules, not boxes: no `border-radius` anywhere, tables have horizontal rules only, headings carry hairline underlines.
- Flush left, ragged right. Body text is `16.5px` to compensate for Futura's small x-height.
- Font stack starts with Futura and falls through geometric sans alternatives; no web font is bundled.

## Known gap

`theme.toml` declares a `show_masthead_band` option, but neither `layout.html` nor the CSS reads it. It is currently a no-op.
