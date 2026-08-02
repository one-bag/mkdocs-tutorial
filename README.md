# MkDocs Tutorial

A friendly, step by step guide to building and publishing a documentation
website with MkDocs, written for people who have never used GitHub.

**Read it here: <https://one-bag.github.io/mkdocs-tutorial/>**

This repository is both the tutorial and a working example of what it teaches.
Everything the guide describes is used here, so you can open any file and see
the real thing.

**In a hurry?**
[Publish without installing anything](https://one-bag.github.io/mkdocs-tutorial/quick-start/)
gets a real site online in about fifteen minutes using nothing but a web
browser. No Python, no terminal.

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
10. Customising the theme with your own CSS, starting from no CSS at all
11. Publishing Jupyter notebooks as pages, with their outputs and charts

Plus a browser-only shortcut for people who would rather not install anything,
a troubleshooting page with the errors people actually hit, and a one page
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
├── requirements.txt               Pinned versions of MkDocs, the theme and the plugins
├── tools/check_tutorial.py        Checks the tutorial against a reader's own setup
└── docs/                          The tutorial itself, one Markdown file per page
```

## The check that keeps it honest

The way a tutorial like this fails is not by being too complicated. It fails by
showing a result the reader cannot reproduce, because the page needs
configuration they have not been given yet. It looks right here, where the
configuration is finished, and produces raw symbols on their screen. Someone
new cannot tell that apart from a mistake of their own, so it stops them.

`tools/check_tutorial.py` looks for exactly that, by rendering rather than by
reading. For every snippet the tutorial teaches, it renders it twice: once with
this site's configuration, and once with the configuration the reader actually
has at that point in the tutorial. Any difference is a promise the reader
cannot keep. It also checks that everything still works with the complete
`mkdocs.yml` handed out in step 5, that the Python version the tutorial asks
for is high enough for every package it later tells you to install, and that no
notebook contains a `.md` link, which MkDocs does not rewrite inside notebooks
and would publish broken.

```bash
python3 tools/check_tutorial.py
```

It runs on every push, before the site is built.

## Contributing

Corrections and clearer explanations are welcome. Open an issue, or click the
pencil icon on any page of the site to edit it directly on GitHub.

## License

Released under the [MIT License](LICENSE).
