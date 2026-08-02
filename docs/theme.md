# 6. Make it look good

You already installed Material for MkDocs back in
[step 2](install.md#step-6-install-mkdocs). Now switch it on and tune it. Every
change in this page goes inside `mkdocs.yml`, under `theme`.

## Switch the theme on

```yaml title="mkdocs.yml"
theme:
  name: material
```

Save, look at your browser. Different site, same content, no work.

## Choose your colours

```yaml title="mkdocs.yml"
theme:
  name: material
  palette:
    primary: indigo
    accent: pink
```

`primary` colours the header and the links. `accent` colours things you hover
over. Available names: `red`, `pink`, `purple`, `deep purple`, `indigo`,
`blue`, `light blue`, `cyan`, `teal`, `green`, `light green`, `lime`, `yellow`,
`amber`, `orange`, `deep orange`, `brown`, `grey`, `blue grey`, `black` and
`white`.

## Add a dark mode switch

Instead of one palette, give the theme two, and it puts a toggle in the header.

```yaml title="mkdocs.yml"
theme:
  name: material
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: teal
      accent: teal
      toggle:
        icon: material/weather-night
        name: Switch to dark mode
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: teal
      accent: teal
      toggle:
        icon: material/weather-sunny
        name: Switch to light mode
```

`scheme: default` is the light one, `scheme: slate` is the dark one. The
`media` lines mean visitors get whichever matches their system setting, and the
toggle lets them override it. Try the switch in the header of this page.

## Turn on the useful features

```yaml title="mkdocs.yml"
theme:
  name: material
  features:
    - navigation.instant
    - navigation.top
    - navigation.footer
    - content.code.copy
    - content.action.edit
    - search.suggest
    - search.highlight
    - toc.follow
```

| Feature | What it gives you |
| --- | --- |
| `navigation.instant` | Pages load without a full refresh, so the site feels instant |
| `navigation.top` | A "back to top" button appears when scrolling up |
| `navigation.footer` | Previous and next links at the bottom of every page |
| `content.code.copy` | A copy button on every code block |
| `content.action.edit` | The edit pencil, if you set `edit_uri` |
| `search.suggest` | The search box completes what you are typing |
| `search.highlight` | Your search words are highlighted on the page you open |
| `toc.follow` | The table of contents follows you as you scroll |

Two more worth knowing once your site grows past a dozen pages:
`navigation.tabs` puts your top level sections across the header, and
`navigation.sections` shows sections as groups in the sidebar instead of
folding menus.

## Add a logo and a favicon

Put your image files in `docs/assets/` and point at them:

```yaml title="mkdocs.yml"
theme:
  name: material
  logo: assets/logo.png
  favicon: assets/favicon.png
```

The logo goes in the header next to the site name. The favicon is the small
icon in the browser tab. A square PNG of about 512 by 512 pixels works for
both.

No logo? Use an icon from the built in set instead:

```yaml title="mkdocs.yml"
theme:
  name: material
  icon:
    logo: material/book-open-page-variant
```

You can browse the names at
[the Material icon search](https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/).

## Add links in the footer

```yaml title="mkdocs.yml"
extra:
  social:
    - icon: fontawesome/brands/github
      link: https://github.com/your-username
      name: My projects on GitHub
    - icon: fontawesome/brands/mastodon
      link: https://mastodon.social/@your-account
```

Note that `extra` is at the left margin, not indented under `theme`.

## Change something the theme does not offer

For anything else, add your own CSS. Create `docs/stylesheets/extra.css`:

```css title="docs/stylesheets/extra.css"
:root {
  --md-primary-fg-color: #005f73;
}

.md-typeset h1 {
  font-weight: 700;
}
```

And register it:

```yaml title="mkdocs.yml"
extra_css:
  - stylesheets/extra.css
```

That variable trick lets you set an exact brand colour rather than picking from
the named list.

!!! tip "Change one thing at a time"
    With `mkdocs serve` running, edit, save, look. If something breaks you know
    exactly which line did it. Changing five settings and then debugging is
    much harder.

---

Next: [put it on GitHub](github-basics.md).
