# Build a documentation website with MkDocs

This tutorial teaches you how to turn a folder of plain text files into a real
documentation website, published on the internet for free.

You do not need to be a programmer. You do not need to know GitHub. Every step
is spelled out, including which buttons to click.

!!! tip "This website is the example"
    The site you are reading right now was built with MkDocs by following these
    exact steps. When you finish, you will have one just like it.

## What you will end up with

* A folder on your computer with your documentation written in Markdown, a
  simple text format.
* A live website with a search box, a navigation menu, a dark mode switch and a
  layout that works on phones.
* A public address such as `https://your-username.github.io/my-docs/`.
* A way to update it later: change a file, save it, and the website updates
  itself in about a minute.

## What you need before starting

| You need | Why | Cost |
| --- | --- | --- |
| A computer with Windows, macOS or Linux | To write and preview the site | Free |
| Python 3.9 or newer | MkDocs is a Python program | Free |
| A text editor | To write your pages. [Step 2](install.md#step-8-get-a-text-editor) recommends one | Free |
| A GitHub account | To store the files and host the website | Free |
| An afternoon | Realistically, 2 to 4 hours if all of this is new | Free |

That is all. No web design, no servers, no credit card.

## How long it takes

The whole tutorial is around 13,000 words, so an hour of reading before you
touch anything. Doing it as you go, from a standing start:

| Part | What you get out of it | Roughly |
| --- | --- | --- |
| Steps 1 to 3 | MkDocs installed, a site running on your own screen | 45 to 60 minutes |
| Steps 4 to 6 | Your own pages, your own menu, a theme that looks good | 45 minutes |
| Steps 7 and 8 | The site on GitHub and live on the internet | 45 to 60 minutes |
| Steps 9 to 11 | Optional extras, dip in when you want one | as long as you like |

!!! tip "In a hurry, or stuck on the terminal?"
    There is a shortcut. [Publish without installing anything](quick-start.md)
    gets a real site online in about fifteen minutes using nothing but your
    web browser, and you can come back and do it properly afterwards.

## How the tutorial is organised

Read the pages in order. Each one builds on the previous one.

<div class="grid cards" markdown>

* :material-help-circle: **[1. What is MkDocs](what-is-mkdocs.md)**
  The idea in two minutes, plus the words you will keep seeing.

* :material-download: **[2. Install the tools](install.md)**
  Python and MkDocs on your computer, checked step by step.

* :material-rocket-launch: **[3. Build your first site](first-site.md)**
  One command creates it, another shows it in your browser.

* :material-file-document-edit: **[4. Write your pages](writing-pages.md)**
  Markdown basics, adding pages, building the menu.

* :material-cog: **[5. Configure the site](configuration.md)**
  The `mkdocs.yml` file explained line by line.

* :material-palette: **[6. Make it look good](theme.md)**
  Colours, logo, dark mode and the useful extras.

* :material-github: **[7. Put it on GitHub](github-basics.md)**
  Accounts, repositories and commits, with no prior knowledge assumed.

* :material-web: **[8. Publish it online](publish.md)**
  Turn on GitHub Pages and get your public address.

* :material-puzzle: **[9. Add plugins](plugins.md)**
  Extra features, added one line at a time.

* :material-palette-swatch: **[10. Customise with CSS](custom-css.md)**
  Your exact colours, and the last bits the theme does not cover.

* :material-notebook: **[11. Add Jupyter notebooks](notebooks.md)**
  Publish `.ipynb` files as pages, outputs and charts included.

</div>

Steps 1 to 8 take you from nothing to a published site. Steps 9 to 11 are
optional extras. Two reference pages are there for later:
[Troubleshooting](troubleshooting.md) for when something breaks, and the
[Cheat sheet](cheatsheet.md) for when you just need to remember a command.

## How to read the code boxes

Boxes like this one contain commands you type into a terminal. Type or paste
one line, press ++enter++, then move to the next line.

```bash
mkdocs --version
```

Hover over a box and a copy button appears on the right, so you never have to
retype anything.

Boxes with a file name on top show the contents of a file. Create the file with
that exact name and paste the contents inside.

```yaml title="mkdocs.yml"
site_name: My documentation
```

!!! note "About the terminal"
    A terminal is a window where you type commands instead of clicking. It is
    called **Command Prompt** or **PowerShell** on Windows, **Terminal** on
    macOS and Linux. The [install page](install.md) shows you how to open it.

Ready? Start with [What is MkDocs](what-is-mkdocs.md).
