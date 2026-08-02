# 10. Customise with CSS

The theme settings in [step 6](theme.md) cover most of what people want. CSS is
for the rest: an exact brand colour, a heading that needs more room, something
you would rather hide.

This page assumes you have never written CSS. You will not need much of it.

!!! tip "This site is styled this way"
    The green in the header is not one of the theme's named colours, and the
    thin line under each section heading is not a theme feature. Both come from
    a stylesheet of about twenty lines, shown in full further down.

## First, check you actually need CSS

Settings in `mkdocs.yml` survive theme updates and cannot break the layout. CSS
can do both. So try the settings first.

| What you want | Where it belongs |
| --- | --- |
| One of the theme's twenty named colours | `mkdocs.yml`, see [step 6](theme.md#choose-your-colours) |
| A dark mode switch | `mkdocs.yml` |
| A logo or favicon | `mkdocs.yml` |
| A different font | `mkdocs.yml`, under `theme.font` |
| **An exact colour, from a brand guide** | **CSS** |
| **Wider or narrower content** | **CSS** |
| **Hiding something the theme always shows** | **CSS** |
| **Anything the theme has no setting for** | **CSS** |

## Setting it up

Two steps, done once.

**Create the file.** Inside `docs`, make a folder called `stylesheets` and a
file inside it called `extra.css`:

```text
my-docs/
├── mkdocs.yml
└── docs/
    ├── index.md
    └── stylesheets/
        └── extra.css
```

**Register it** in `mkdocs.yml`:

```yaml title="mkdocs.yml"
extra_css:
  - stylesheets/extra.css
```

The path starts from inside the `docs` folder, so it is
`stylesheets/extra.css` and not `docs/stylesheets/extra.css`. Getting this
wrong is the most common reason a stylesheet appears to do nothing.

With `mkdocs serve` running, every save of the CSS file refreshes the browser,
same as with your Markdown.

## CSS in sixty seconds

A CSS file is a list of rules. Every rule has the same shape:

```css
.md-header {
  background-color: darkgreen;
}
```

* `.md-header` is the **selector**: which parts of the page to change. A name
  starting with a dot is a class, which is how nearly everything on a Material
  site is labelled.
* `background-color` is the **property**: what aspect to change.
* `darkgreen` is the **value**.
* The semicolon ends each line, the braces group them.

Anything between `/*` and `*/` is a comment, ignored by the browser.

## Prefer variables over selectors

Material defines its colours as **variables**, names starting with `--md-`.
Change a variable once and every part of the site that uses it follows: the
header, the links, the buttons, the search bar.

That is much safer than styling each piece by hand, and it survives theme
updates better.

| Variable | What it colours |
| --- | --- |
| `--md-primary-fg-color` | The header and the main accents |
| `--md-primary-fg-color--dark` | A darker shade, used for hover states |
| `--md-accent-fg-color` | Whatever you are hovering over |
| `--md-typeset-a-color` | Links inside your content |
| `--md-default-bg-color` | The page background |
| `--md-default-fg-color` | The body text |
| `--md-code-bg-color` | The background of code blocks |

## The exact brand colour

Here is the first half of the stylesheet this site uses:

```css title="docs/stylesheets/extra.css"
[data-md-color-primary] {
  --md-primary-fg-color:        #00695c;
  --md-primary-fg-color--light: #4a9d92;
  --md-primary-fg-color--dark:  #004d40;
  --md-accent-fg-color:         #00897b;
}
```

`#00695c` is a hexadecimal colour code. Any colour picker will give you one for
your own brand colour.

??? question "Why `[data-md-color-primary]` and not `:root`?"
    Most CSS tutorials tell you to put variables in a `:root` block, and for a
    plain website that is right. It does not work here.

    Material writes its own colour variables onto the `<body>` tag of every
    page. A `:root` block sets them on the tag above it, `<html>`, and the
    value closest to the element wins. So a `:root` block gets silently
    overruled and nothing changes.

    `[data-md-color-primary]` selects that same `<body>` tag, so both rules
    apply to the same place. Your stylesheet is loaded after the theme's, and
    when two rules are equally specific, the last one wins.

    If that felt like a lot of detail: the practical version is **write your
    variables in a `[data-md-color-primary]` block** and it will work.

If you set the colour this way, remove `primary` and `accent` from the
`palette` section of `mkdocs.yml`. Leaving both in place means two things are
deciding the same colour, and you will not be able to tell which one is
winning.

## Light and dark are two separate problems

A colour that reads well on white can be unreadable on a dark background. Check
both modes every time, using the switch in the header.

To change something in dark mode only, add the scheme to the selector. This is
the second half of the stylesheet this site uses:

```css title="docs/stylesheets/extra.css"
[data-md-color-scheme="slate"][data-md-color-primary] {
  --md-accent-fg-color:  #4db6ac;
  --md-typeset-a-color:  #4db6ac;
}
```

`slate` is the theme's internal name for dark mode. That rule makes links a
lighter green, because the darker green from the light theme almost disappears
against the dark background.

!!! warning "Two attributes, not one"
    The theme's own dark mode rules use two attributes together, and a rule
    with only one of them loses no matter where it sits in the file. If a dark
    mode override seems to be ignored, this is usually why.

## Styling the content itself

For anything inside the page body rather than the chrome around it, start the
selector with `.md-typeset`. The theme's own content rules all do, and without
it yours will lose.

This is the last rule this site uses. It puts a thin line under every `##`
heading, which helps on long pages:

```css title="docs/stylesheets/extra.css"
.md-typeset h2 {
  border-bottom: 0.05rem solid var(--md-default-fg-color--lightest);
  padding-bottom: 0.2rem;
}
```

`var(--md-default-fg-color--lightest)` reuses one of the theme's own colours,
so the line stays right in both light and dark mode. Hard coding `#eeeeee`
there would look wrong the moment someone switched to dark.

A few more that people commonly want. These are not used on this site, so treat
them as a starting point:

```css
/* Wider content on large screens. The default is 61rem. */
.md-grid {
  max-width: 70rem;
}

/* Make tables span the full width instead of shrinking to their content. */
.md-typeset table:not([class]) {
  display: table;
  width: 100%;
}

/* Slightly larger body text. */
.md-typeset {
  font-size: 0.85rem;
}

/* Stop a very long code block from taking over the whole page. */
.md-typeset pre > code {
  max-height: 25rem;
}
```

## Finding the name of the thing you want to change

You do not have to guess or memorise class names. Every browser will tell you.

1. Right click the thing you want to change and choose **Inspect**.
2. A panel opens with the page structure, and the element you clicked is
   highlighted. Look for its `class`, for example `md-header__title`.
3. In the panel next to it you can see, and edit, the styles already applied.
   Change a value there and the page updates immediately.
4. Once it looks right, copy the property into your `extra.css` with the class
   name as the selector.

Editing in the browser changes nothing permanently. It disappears on reload,
which makes it the safest place to experiment.

## Keep it short

Every rule you add is another thing that can break when the theme is updated,
because you are reaching into someone else's design. Twenty lines of CSS you
understand will serve you better than two hundred copied from the internet.

If a rule stops working after an update, delete it and start again. Nothing
else in your site depends on it.

## When your CSS does nothing

??? failure "The stylesheet has no effect at all"
    In order:

    1. Is `extra_css` in `mkdocs.yml`, spelled exactly that way?
    2. Is the path relative to `docs`? It should be `stylesheets/extra.css`,
       not `docs/stylesheets/extra.css`.
    3. Is the file really where you think it is? A file saved as
       `extra.css.txt`, which some editors do quietly, will never load.

    `mkdocs serve` watches `mkdocs.yml` as well as your pages, so you do not
    need to restart it after adding the `extra_css` line. If the terminal shows
    no rebuild at all when you save, the file is not where MkDocs is looking.

??? failure "One rule is ignored while the others work"
    The theme has a more specific rule for that element. Two fixes, in order of
    preference: add `.md-typeset` to the front of your selector, or match the
    shape of the theme's own rule as described above.

    As a last resort, `color: red !important;` overrules everything. It works,
    and it makes the next problem harder to debug, so use it sparingly.

??? failure "It works locally but not on the published site"
    Two possibilities. Your browser is showing a cached copy: reload with
    ++ctrl+shift+r++, or ++cmd+shift+r++ on macOS. Or the file was never
    committed: run `git status` and check that
    `docs/stylesheets/extra.css` is not sitting there untracked.

??? failure "I edited the CSS in the site folder and it keeps disappearing"
    Everything in `site` is regenerated on each build. Your stylesheet belongs
    in `docs/stylesheets/`, and MkDocs copies it across.

## One more file you can add

The same mechanism exists for JavaScript, if you ever need behaviour rather
than appearance:

```yaml title="mkdocs.yml"
extra_javascript:
  - javascripts/extra.js
```

You will rarely want it. Almost everything people reach for JavaScript to do,
Material already has a setting or a plugin for.

---

Next, and last: [add Jupyter notebooks](notebooks.md), if you have any.
