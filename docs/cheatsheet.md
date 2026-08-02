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
│   └── assets/
└── site/                  Generated. Never edited, never uploaded.
```

## The publishing checklist

- [ ] `requirements.txt` exists, with pinned versions
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
