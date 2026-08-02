# MkDocs Tutorial

A friendly, step by step guide to building and publishing a documentation
website with MkDocs, written for people who have never used GitHub.

**Read it here: <https://one-bag.github.io/mkdocs-tutorial/>**

This repository is both the tutorial and a working example of what it teaches.
Everything the guide describes is used here, so you can open any file and see
the real thing.

## What the tutorial covers

1. What MkDocs is, and the vocabulary you need
2. Installing Python and MkDocs, on Windows, macOS and Linux
3. Creating a site and previewing it live in the browser
4. Writing pages in Markdown and building the navigation menu
5. Configuring the site through `mkdocs.yml`
6. The Material theme: colours, dark mode, logo, search
7. GitHub accounts, repositories and commits, from zero
8. Publishing for free with GitHub Pages and GitHub Actions
9. Adding plugins, and pinning them so the published build keeps working

Plus a troubleshooting page with the errors people actually hit, and a one page
cheat sheet.

## Run this site on your own computer

```bash
git clone https://github.com/one-bag/mkdocs-tutorial.git
cd mkdocs-tutorial
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Then open <http://127.0.0.1:8000>.

On Windows, use `python` instead of `python3` and `.venv\Scripts\Activate.ps1`
instead of the `source` line.

## What is in here

```text
.
├── .github/workflows/deploy.yml   Builds and publishes the site on every push
├── mkdocs.yml                     Site configuration
├── requirements.txt               Pinned versions of MkDocs and the theme
└── docs/                          The tutorial itself, one Markdown file per page
```

## Contributing

Corrections and clearer explanations are welcome. Open an issue, or click the
pencil icon on any page of the site to edit it directly on GitHub.

## License

Released under the [MIT License](LICENSE).
