# 5. Configure the site

Everything about your site that is not content lives in `mkdocs.yml`. It sits
next to the `docs` folder and it is a plain text file you edit by hand.

## Three rules of YAML

`mkdocs.yml` is written in YAML. YAML is picky about exactly three things, and
every configuration error you will ever hit comes from one of them.

1. **Indentation is meaning.** Two spaces per level. Being nested one level
    deeper changes what a line belongs to.
2. **Spaces only, never tabs.** A tab character causes an error that does not
    say "tab". Set your editor to insert spaces when you press ++tab++.
3. **A space after every colon.** `site_name: My docs` works,
    `site_name:My docs` does not.

!!! tip "When in doubt, copy"
    Copy a working example and change the values inside it. That avoids almost
    every YAML problem.

## The settings worth knowing

### site_name

```yaml
site_name: My documentation
```

Shown in the header and in the browser tab. The only setting MkDocs requires.

### site_url

```yaml
site_url: https://your-username.github.io/my-docs/
```

The final public address. It matters more than it looks: search, sitemaps and
some theme features build absolute links from it. Fill it in as soon as you
know your address, in [step 8](publish.md). Keep the trailing slash.

### site_description

```yaml
site_description: How to install and use the project, for new team members.
```

One sentence. It is what search engines and chat apps show underneath your
link.

### nav

```yaml
nav:
  - Home: index.md
  - Installation: install.md
  - Reference:
      - Commands: reference/commands.md
```

The menu, in your order, with your labels. Covered in detail in
[step 4](writing-pages.md#take-control-of-the-menu).

### theme

```yaml
theme:
  name: material
```

Which look to use. `mkdocs` and `readthedocs` are built in. `material` is the
one this tutorial uses, and it is the one you installed. All of
[step 6](theme.md) is about what goes under this key.

### repo_url

```yaml
repo_url: https://github.com/your-username/my-docs
repo_name: your-username/my-docs
edit_uri: edit/main/docs/
```

Adds a link to your GitHub project in the top right corner. With `edit_uri`
set, every page also gets an "edit this page" pencil that takes readers
straight to the file on GitHub. It is the cheapest way to get corrections from
your readers.

### plugins

```yaml
plugins:
  - search
```

Programs that take part in the build and add features. If you leave this out
entirely, MkDocs uses `search` on its own, which is why your site has a search
box without you asking for one. Writing the list yourself replaces that
default, so `search` has to stay on it. Covered in [step 9](plugins.md).

### markdown_extensions

```yaml
markdown_extensions:
  - admonition
  - attr_list
  - tables
  - toc:
      permalink: true
```

Extra Markdown features, switched on one by one. `admonition` gives you the
coloured boxes, `tables` gives you tables, `toc: permalink: true` puts a small
anchor link next to every heading so people can link to a section.

## A complete file to copy

This is a good starting point for a real project. Change the names and delete
what you do not need.

```yaml title="mkdocs.yml"
site_name: My documentation
site_description: What this project is and how to use it.
site_url: https://your-username.github.io/my-docs/

repo_url: https://github.com/your-username/my-docs
repo_name: your-username/my-docs
edit_uri: edit/main/docs/

theme:
  name: material
  language: en
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: teal
      toggle:
        icon: material/weather-night
        name: Switch to dark mode
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: teal
      toggle:
        icon: material/weather-sunny
        name: Switch to light mode
  features:
    - navigation.top
    - content.code.copy
    - search.suggest

markdown_extensions:
  - admonition
  - attr_list
  - def_list
  - footnotes
  - md_in_html
  - tables
  - toc:
      permalink: true
  - pymdownx.details
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.inlinehilite
  - pymdownx.keys
  - pymdownx.superfences
  - pymdownx.tabbed:
      alternate_style: true
  - pymdownx.tilde

nav:
  - Home: index.md
  - Installation: install.md
```

!!! note "Where did these extension names come from"
    They ship with the Material theme you already installed, so there is
    nothing else to download. `pymdownx.superfences` powers the tabs and nested
    code blocks, `pymdownx.keys` renders keyboard keys like ++ctrl+c++, and
    `pymdownx.details` is what makes foldable boxes fold.

## Check your file before you get stuck

If MkDocs complains about the configuration, the error names the line number.
Go to that line, then look at the line above it too: in YAML, a broken
indentation is usually reported one line later than the actual mistake.

```bash
mkdocs build --strict
```

`--strict` turns every warning into an error, including broken internal links.
Running it once before publishing saves you from putting a site online with
dead links in it.

---

Next: [make it look good](theme.md).
