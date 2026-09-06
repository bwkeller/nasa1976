# NASA 1976 — Sphinx theme

Documentation theme after NHB 1430.2, the NASA Graphics Standards Manual of
January 1976. Companion to the PowerPoint template and the aquarel matplotlib
themes: same palette, same Futura stack, same flush-left grid.

## Install

```bash
pip install .
```

Then in `conf.py`:

```python
html_theme = "nasa1976"
```

The package registers itself through the `sphinx.html_themes` entry point, so
no `html_theme_path` is needed. To use the checkout directly without installing,
point `html_theme_path` at the repository root (the directory that contains the
`nasa1976/` package folder):

```python
import os
html_theme_path = [os.path.abspath("path/to/nasa1976-repo")]
html_theme = "nasa1976"
```

## Options

```python
html_theme_options = {
    "program_label": "Graphics Standards",   # small caps line above the title
    "document_number": "NHB 1430.2",         # footer, left
    "revision": "January 1976",              # footer, beside the number
    "accent_color": "#e4002b",               # links, rules, warning labels
    "color_scheme": "auto",                  # "auto", "light", or "dark"
}
```

`html_short_title` sets the masthead title; `release` prints beside it.

## What it does

**Structure.** A two-column grid: a narrow margin column holding the contents
and search, and a body column capped at 44rem. That is the manual's page —
heading in the left margin, text to the right of it. The margin column sticks
on scroll and collapses behind a Contents button below 820px, using a CSS
checkbox rather than JavaScript.

**Colour.** Black on white, warm gray for secondary labels, and NASA Red held
back as a genuine accent. Red appears on links, the current nav item, and
`warning` / `danger` / `error` / `caution` admonition labels. `note`, `tip`,
`important` and `seealso` get a black label bar instead — the manual's point
that red loses its force when it is used for everything.

**Rules, not boxes.** `h1` and `h2` carry hairline rules underneath, tables
rule top, bottom and under the header row with no vertical lines, and nothing
has rounded corners. Admonitions are hairline frames with a solid label bar.

**Dark mode** via `prefers-color-scheme`, inverting to white on black, matching
the deck's closing plate and the `nasa-1976-inverted` aquarel theme. Pygments
switches to `native` automatically. Set `color_scheme` to `"light"` or `"dark"`
to fix the scheme regardless of the reader's system preference.

## Type

Futura first, falling through `Futura PT`, `Century Gothic`, `URW Gothic`,
`Avenir Next`, `Trebuchet MS`, then the system sans. Since Futura is not a web
font here, readers without it get the nearest geometric sans installed. If you
want an exact match everywhere, self-host a licensed Futura and add:

```python
html_css_files = ["fonts.css"]   # containing your @font-face rules
```

Body text is set at 16.5px rather than the more usual 16px, because Futura's
small x-height reads smaller than its point size suggests — a caution the
manual itself gives on page 5.4.

## Notes

The theme inherits from `basic`, so `globaltoc.html` and `searchbox.html` are
the default sidebars. Override with `html_sidebars` as normal.

No logotype or seal artwork is included. The manual requires both to be
reproduced photographically from official artwork rather than redrawn, so
supply your own via `html_logo` if you have the right to use one.
# nasa1976
