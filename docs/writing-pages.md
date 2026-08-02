# 4. Write your pages

Your content is written in Markdown. It is plain text with a handful of
symbols, and you can learn the useful half in five minutes.

## Markdown in five minutes

Keep `mkdocs serve` running while you read this and try things in
`docs/index.md`. Seeing the result appear is the fastest way to learn.

### Headings

```markdown
# Page title
## A section
### A subsection
```

Use exactly one `#` heading per page, at the top. It becomes the page title,
and everything below it turns into the table of contents on the right.

### Emphasis

| You write | You get |
| --- | --- |
| `**important**` | **important** |
| `*a bit of stress*` | *a bit of stress* |
| `` `some_command` `` | `some_command` |
| `~~no longer true~~` | ~~no longer true~~ |

Strikethrough is the one exception in that table: it only works once
`pymdownx.tilde` is listed under `markdown_extensions` in `mkdocs.yml`. It is
already in the example configuration you will copy in
[step 5](configuration.md#a-complete-file-to-copy).

### Lists

```markdown
- First thing
- Second thing
    - A detail, indented by four spaces
- Third thing

1. Do this
2. Then this
3. Finally this
```

- First thing
- Second thing
    - A detail, indented by four spaces
- Third thing

!!! warning "Blank lines matter"
    Markdown needs an empty line before a list, before a heading and before a
    code block. If a list refuses to render as a list, a missing blank line is
    almost always the reason.

### Links

```markdown
[Text people click](https://example.org)
[Another page of my site](install.md)
[A section of another page](install.md#step-6-install-mkdocs)
```

Links between your own pages use the file name, ending in `.md`. MkDocs
rewrites them into proper web addresses when it builds. This also means MkDocs
can warn you when a link points at a page that does not exist.

### Images

Put the file in `docs/assets/` and refer to it like this:

```markdown
![Description of the image](assets/screenshot.png)
```

The text in square brackets is what screen readers announce and what shows if
the image fails to load. Write something meaningful there.

### Code

For a word or a command inside a sentence, wrap it in single backticks:
`` `mkdocs serve` ``.

For several lines, use three backticks and name the language:

````markdown
```python
def greet(name):
    print(f"Hello {name}")
```
````

```python
def greet(name):
    print(f"Hello {name}")
```

The language name is what gives you the colours. Use `bash` for terminal
commands, `yaml` for settings files, `text` when it is nothing in particular.

### Tables

```markdown
| Option | Meaning | Default |
| --- | --- | --- |
| `--strict` | Fail on warnings | off |
| `--clean`  | Empty the site folder first | on |
```

| Option | Meaning | Default |
| --- | --- | --- |
| `--strict` | Fail on warnings | off |
| `--clean`  | Empty the site folder first | on |

The columns do not need to line up in your text file. Only the pipes matter.

### Coloured boxes

These are called admonitions, and they are the fastest way to make a page look
organised.

!!! warning "Switch these two on first"
    Unlike everything above, coloured boxes are not part of plain Markdown. Try
    one right now and the page will show your text exactly as you typed it,
    `!!!` and all.

    Open `mkdocs.yml`, add these three lines at the bottom, and save:

    ```yaml title="mkdocs.yml"
    markdown_extensions:
      - admonition
      - pymdownx.details
    ```

    [Step 5](configuration.md) explains what that section is. The boxes work
    straight away, and they get their colours once you switch to the Material
    theme in [step 6](theme.md).

```markdown
!!! note "Optional title"
    Indent the content by four spaces.

!!! tip
    Without a title, the box is labelled by its type.

!!! warning "Read this before continuing"
    Use it when something can go wrong.
```

!!! note "Optional title"
    Indent the content by four spaces.

!!! tip
    Without a title, the box is labelled by its type.

!!! warning "Read this before continuing"
    Use it when something can go wrong.

The available types are `note`, `abstract`, `info`, `tip`, `success`,
`question`, `warning`, `failure`, `danger`, `bug`, `example` and `quote`.

Swap the first `!!!` for `???` and the box becomes foldable, closed by default.
Useful for long error messages that most readers can skip.

```markdown
??? question "Can I fold a box?"
    Yes, exactly like this one.
```

??? question "Can I fold a box?"
    Yes, exactly like this one.

## Add a second page

Create a new file called `docs/install.md` and write something in it:

```markdown title="docs/install.md"
# Installation

Download the program and run it. That is the whole procedure.
```

Save it, and look at your browser. The page is already in the menu, because by
default MkDocs lists every file it finds in `docs`.

## Take control of the menu

Automatic ordering is alphabetical, which is rarely what you want. Add a `nav`
section to `mkdocs.yml` and you decide both the order and the titles:

```yaml title="mkdocs.yml"
site_name: My documentation

nav:
  - Home: index.md
  - Getting started: install.md
```

The part before the colon is the label shown in the menu. The part after it is
the file. They are independent, which is why `install.md` can appear as
"Getting started".

!!! warning "Only list files that exist"
    Add a line for a file you have not created yet and MkDocs prints
    `A reference to 'usage.md' is included in the 'nav' configuration, which is
    not found in the documentation files`. The site still builds, so it is a
    warning rather than a disaster, but it will keep nagging you until the file
    exists or the line goes.

!!! warning "Once you write `nav`, it is the only source of truth"
    A page missing from `nav` still gets built, but no link points to it, so
    nobody will find it. Whenever you add a file, add its line to `nav`.

## Group pages into sections

For a larger site, put related pages in a folder and nest them in the menu:

```text
docs/
├── index.md
├── guide/
│   ├── install.md
│   └── usage.md
└── reference/
    └── commands.md
```

```yaml title="mkdocs.yml"
nav:
  - Home: index.md
  - User guide:
      - Installation: guide/install.md
      - Usage: guide/usage.md
  - Reference:
      - Commands: reference/commands.md
```

The indentation is what creates the nesting, so keep it consistent. Four spaces
under a menu label, six for the entries below it, as in the example above.

## Checklist for this step

- [x] You can write headings, lists, links and code blocks.
- [x] You added a second page and it appeared on the site.
- [x] You wrote a `nav` section and the menu follows your order.

---

Next: [configure the site](configuration.md).
