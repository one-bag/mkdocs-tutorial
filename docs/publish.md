# 8. Publish it online

One more step and your documentation has a public address that anyone can open.

GitHub Pages is free hosting for static websites. You give it your files,
it gives you an address like `https://your-username.github.io/my-docs/`. No
server to rent, no payment details.

Better still, GitHub can run MkDocs for you. You push your Markdown, GitHub
builds the site and publishes it, every single time, without you doing
anything.

## Step 1: pin the versions

Create a file called `requirements.txt` next to `mkdocs.yml`:

```text title="requirements.txt"
mkdocs==1.6.1
mkdocs-material==9.7.7
```

This tells GitHub exactly which versions to install, so your site keeps
building the same way in a year's time.

Check the versions you have locally with `pip show mkdocs mkdocs-material`, and
use those numbers.

## Step 2: add the recipe

GitHub looks for instructions in a folder called `.github/workflows`. Create
that folder, and inside it a file called `deploy.yml`.

!!! note "The dot at the start"
    Folders whose name starts with a dot are hidden in most file managers. In
    the terminal, `mkdir -p .github/workflows` creates both at once. On GitHub
    itself, typing `.github/workflows/deploy.yml` as the file name when
    creating a new file creates the folders automatically.

```yaml title=".github/workflows/deploy.yml"
name: Publish documentation

on:
  push:
    branches:
      - main
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
          cache: pip
      - run: pip install -r requirements.txt
      - run: mkdocs build --strict
      - uses: actions/configure-pages@v5
      - uses: actions/upload-pages-artifact@v3
        with:
          path: site

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - id: deployment
        uses: actions/deploy-pages@v4
```

Copy it exactly. YAML cares about indentation, and this file is the one place
in the tutorial where you should not improvise.

??? info "What each part of that file says"
    | Part | Meaning |
    | --- | --- |
    | `on: push: branches: [main]` | Run this whenever something reaches the main branch |
    | `workflow_dispatch` | Also allow running it by hand from the Actions tab |
    | `permissions` | Allow this job to publish to Pages, nothing more |
    | `concurrency` | If two pushes overlap, do not let them fight |
    | `runs-on: ubuntu-latest` | Use a fresh Linux machine that GitHub provides |
    | `actions/checkout` | Download your repository onto that machine |
    | `actions/setup-python` | Install Python on it |
    | `pip install -r requirements.txt` | Install MkDocs and the theme |
    | `mkdocs build --strict` | Build the site, and stop if anything is wrong |
    | `upload-pages-artifact` | Hand the finished `site` folder to GitHub Pages |
    | `deploy-pages` | Put it online |

## Step 3: switch Pages on

This is done once, in the browser.

1. Open your repository on GitHub.
2. Click **Settings**, in the row of tabs at the top.
3. In the left sidebar, click **Pages**.
4. Under **Build and deployment**, open the **Source** dropdown and choose
   **GitHub Actions**.

There is no save button. The choice applies immediately.

!!! danger "The most common mistake"
    If **Source** is left on **Deploy from a branch**, the workflow runs, says
    it succeeded, and your address still shows a 404. The setting has to say
    **GitHub Actions**.

## Step 4: push and watch

Send the two new files to GitHub, exactly as in
[step 7](github-basics.md#two-ways-to-upload-your-files): drag them into the
browser, or use git:

```bash
git add .
git commit -m "Publish the site with GitHub Pages"
git push
```

Now click the **Actions** tab of your repository. A run appears with a yellow
dot, meaning it is working. It takes about a minute.

* **Green tick:** done. Your site is live.
* **Red cross:** click the run, then the failed step, and read the last lines
  of the log. It names the file and the problem. The
  [Troubleshooting](troubleshooting.md) page covers the usual causes.

## Step 5: open your website

Back in **Settings > Pages**, your address is shown at the top of the page:

```text
https://your-username.github.io/my-docs/
```

Open it. That link works for anyone, anywhere.

Add it to `mkdocs.yml` now, so that search and social previews use the real
address:

```yaml title="mkdocs.yml"
site_url: https://your-username.github.io/my-docs/
```

While you are there, put the link in your repository description too: on the
repository home page, click the gear next to **About** and paste it into
**Website**.

## Updating the site from now on

This is the whole routine, forever:

1. Edit or add a Markdown file in `docs`.
2. Preview locally with `mkdocs serve` if you want to check it.
3. Commit and push, or edit the file directly on GitHub and click
   **Commit changes**.
4. Wait about a minute. The site updates itself.

You never run `mkdocs build` for the public site, and you never touch the
`site` folder. GitHub does that part.

## Optional: your own domain

If you own a domain such as `docs.example.org`:

1. At your domain provider, add a `CNAME` record pointing
   `docs` at `your-username.github.io`.
2. In **Settings > Pages**, type `docs.example.org` into **Custom domain** and
   save.
3. Wait for the check to pass, then tick **Enforce HTTPS**.
4. Update `site_url` in `mkdocs.yml` to the new address.

## You are done

You now have a documentation website that is written in plain text, versioned,
searchable, readable on a phone, published for free and updated by saving a
file.

Keep the [Cheat sheet](cheatsheet.md) open for the commands, and come back to
[Troubleshooting](troubleshooting.md) when something misbehaves.
