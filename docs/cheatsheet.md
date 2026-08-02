# Cheat sheet

Everything on one page, for when you just need to remember the command.

## Starting a session

=== "Windows"

    ```powershell
    cd $HOME\my-docs
    .venv\Scripts\Activate.ps1
    mkdocs serve
    ```

=== "macOS / Linux"

    ```bash
    cd ~/my-docs
    source .venv/bin/activate
    mkdocs serve
    ```

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000) and start writing.
Stop with ++ctrl+c++.

## MkDocs commands

| Command | What it does |
| --- | --- |
| `mkdocs new .` | Create a project in the current folder |
| `mkdocs serve` | Live preview on port 8000 |
| `mkdocs serve -a localhost:8001` | Same, on another port |
| `mkdocs build` | Write the finished site into `site/` |
| `mkdocs build --strict` | Build, and fail on any warning |
| `mkdocs --version` | Check the installed version |

## Git commands

| Command | What it does |
| --- | --- |
| `git status` | What has changed since the last commit |
| `git add .` | Mark everything as ready to save |
| `git commit -m "message"` | Save it with that message |
| `git push` | Upload commits to GitHub |
| `git pull` | Download changes from GitHub |
| `git log --oneline` | The history, one line per commit |

The everyday sequence is three lines:

```bash
git add .
git commit -m "Describe what changed"
git push
```

Working on a branch instead, so nothing goes live until it is checked
([step 12](teamwork.md)):

```bash
git switch -c my-change      # start a branch
git add . && git commit -m "Describe what changed"
git push -u origin my-change # the output links to the pull request
git switch main && git pull  # after it is merged
```

## Markdown

| You write | You get |
| --- | --- |
| `# Title` | A page title |
| `## Section` | A section heading |
| `**bold**` | **bold** |
| `*italic*` | *italic* |
| `` `code` `` | `code` |
| `[text](https://example.org)` | A link |
| `[text](other-page.md)` | A link to another page of your site |
| `![description](assets/image.png)` | An image |
| `- item` | A bullet list |
| `1. item` | A numbered list |
| `> quoted text` | A quotation |
| `---` | A horizontal line |

Fenced code, with the language named for colours:

````markdown
```python
print("hello")
```
````

A table:

```markdown
| Column | Column |
| --- | --- |
| Cell | Cell |
```

A coloured box:

```markdown
!!! warning "Title"
    Content, indented by four spaces.
```

Types available: `note`, `abstract`, `info`, `tip`, `success`, `question`,
`warning`, `failure`, `danger`, `bug`, `example`, `quote`. Start it with `???`
instead of `!!!` to make it foldable.

## Adding a plugin

Four steps, in this order:

```bash
pip install mkdocs-glightbox           # 1. install it
```

```yaml title="mkdocs.yml"
plugins:                               # 2. switch it on
  - search                             #    keep this line or search breaks
  - glightbox
```

```bash
mkdocs serve                           # 3. check it locally
```

```text title="requirements.txt"
mkdocs-glightbox==0.5.2                # 4. pin it, or GitHub cannot build
```

The pip package name and the name you write in `mkdocs.yml` are usually
different. Details in [step 9](plugins.md).

## Adding your own CSS

```text title="where the file goes"
docs/stylesheets/extra.css
```

```yaml title="mkdocs.yml"
extra_css:
  - stylesheets/extra.css       # path starts inside docs/
```

```css title="docs/stylesheets/extra.css"
[data-md-color-primary] {       /* your brand colour, both modes */
  --md-primary-fg-color: #00695c;
  --md-accent-fg-color:  #00897b;
}

[data-md-color-scheme="slate"][data-md-color-primary] {
  --md-typeset-a-color: #4db6ac;   /* dark mode only */
}

.md-typeset h2 {                /* .md-typeset for anything in the page body */
  border-bottom: 0.05rem solid var(--md-default-fg-color--lightest);
}
```

Right click anything and choose **Inspect** to find its class name. Details in
[step 10](custom-css.md).

## Publishing a Jupyter notebook

```bash
pip install mkdocs-jupyter
```

```yaml title="mkdocs.yml"
plugins:
  - search
  - mkdocs-jupyter:
      include: ["*.ipynb"]     # leave the Markdown pages alone
      execute: false           # use the outputs saved in the notebook
      include_source: true     # publish the .ipynb too, link to it yourself

nav:
  - Analysis: analysis.ipynb   # the file lives in docs/, like any page
```

Run the notebook and save it before committing: with `execute: false` the page
shows the outputs stored in the file. Details in [step 11](notebooks.md).

## A minimal `mkdocs.yml`

```yaml title="mkdocs.yml"
site_name: My documentation
site_url: https://your-username.github.io/my-docs/

theme:
  name: material
  palette:
    primary: teal
  features:
    - content.code.copy
    - navigation.top

markdown_extensions:
  - admonition
  - attr_list
  - tables
  - toc:
      permalink: true
  - pymdownx.details
  - pymdownx.superfences

nav:
  - Home: index.md
  - Installation: install.md
```

## Project layout

```text
my-docs/
├── .github/
│   └── workflows/
│       └── deploy.yml     Instructions for GitHub
├── .gitignore             What git should ignore
├── mkdocs.yml             Your settings
├── requirements.txt       Which versions to install
├── docs/                  Your content, all of it
│   ├── index.md
│   ├── analysis.ipynb     Notebooks go here too
│   ├── assets/            Images, logo, favicon
│   └── stylesheets/
│       └── extra.css      Your own CSS, if you add any
└── site/                  Generated. Never edited, never uploaded.
```

## The publishing checklist

- [ ] `requirements.txt` exists, with pinned versions of MkDocs, the theme and
      every plugin you use
- [ ] `.github/workflows/deploy.yml` exists
- [ ] `.gitignore` contains `site/`
- [ ] **Settings > Pages > Source** is set to **GitHub Actions**
- [ ] `mkdocs build --strict` passes on your machine
- [ ] `site_url` in `mkdocs.yml` matches the real address
- [ ] The Actions tab shows a green tick

## Where to look next

* [MkDocs documentation](https://www.mkdocs.org/)
* [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
* [Markdown guide](https://www.markdownguide.org/basic-syntax/)
* [GitHub Pages documentation](https://docs.github.com/en/pages)
