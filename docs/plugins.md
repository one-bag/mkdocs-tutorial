# 9. Add plugins

A theme changes how your site looks. A plugin changes what happens while the
site is being built.

Plugins can add a "last updated" date to every page, shrink the files so the
site loads faster, keep old addresses working after you rename a page, or build
reference documentation out of your source code. You install one, add a line to
`mkdocs.yml`, and it works from then on.

!!! tip "This site uses one"
    Scroll to the bottom of any page here and you will see when it was last
    changed. That comes from a plugin, configured exactly as described below.

## You are already using one

MkDocs has one plugin switched on out of the box: `search`, the plugin that
builds the search index behind the search box.

You have never had to write it down, because when `mkdocs.yml` says nothing
about plugins, MkDocs assumes this:

```yaml title="mkdocs.yml"
plugins:
  - search
```

That detail matters more than it looks, which brings us to the one rule worth
remembering.

## The rule that catches everyone

!!! danger "Writing a `plugins` list replaces the default, it does not add to it"
    The moment you add a `plugins` section, `search` is no longer included
    automatically. If you forget to list it, your search box disappears without
    any error message. The site builds happily and looks fine, and the search
    is simply gone.

So this is wrong, even though it looks reasonable:

```yaml title="mkdocs.yml"
plugins:
  - glightbox      # the search box is now gone
```

And this is right:

```yaml title="mkdocs.yml"
plugins:
  - search
  - glightbox
```

Whenever you touch the `plugins` section, check that `search` is still the
first line.

## Adding a plugin, step by step

Four steps, always the same.

### Step 1: install it

```bash
pip install mkdocs-glightbox
```

!!! warning "The package name and the plugin name are usually different"
    You install `mkdocs-glightbox` but you write `glightbox` in `mkdocs.yml`.
    The pip package almost always starts with `mkdocs-`, and the name that goes
    in the configuration almost never does. The plugin's own page tells you
    both. Using the wrong one is the most common plugin error there is.

### Step 2: add it to `mkdocs.yml`

```yaml title="mkdocs.yml"
plugins:
  - search
  - glightbox
```

### Step 3: check it locally

```bash
mkdocs serve
```

If the plugin is missing or misspelled, MkDocs says so immediately and names
the plugin it could not find.

### Step 4: add it to `requirements.txt`

```text title="requirements.txt"
mkdocs==1.6.1
mkdocs-material==9.7.7
mkdocs-glightbox==0.5.2
```

This step is the one people forget. Your computer has the plugin installed;
the machine GitHub uses does not. If it is not in `requirements.txt`, the
build works for you and fails for GitHub, with an error saying the plugin is
not installed.

Then commit and push as usual, and the live site picks it up in about a minute.

## Giving a plugin options

Some plugins take settings. Put a colon after the name and indent the options
underneath, two spaces further in:

```yaml title="mkdocs.yml"
plugins:
  - search
  - glightbox:
      touchNavigation: true
      zoomable: true
```

Note the colon after `glightbox`, which is not there when the plugin takes no
options. Forgetting it is a common YAML error.

## The worked example: last updated dates

This is the plugin running on this site. It reads your git history and prints
the date each page was last changed.

**Install it**

```bash
pip install mkdocs-git-revision-date-localized-plugin
```

**Configure it**

```yaml title="mkdocs.yml"
plugins:
  - search
  - git-revision-date-localized:
      enable_creation_date: false
      type: date
      fallback_to_build_date: true
```

`type: date` prints a plain date. Use `type: timeago` for "3 days ago" instead.
`fallback_to_build_date: true` keeps the build working for files that have not
been committed yet, which saves you an error while you are still writing.

**Pin it**

```text title="requirements.txt"
mkdocs-git-revision-date-localized-plugin==1.5.3
```

**Give GitHub the full history**

This plugin needs one extra thing, and it is worth understanding because
several plugins share the problem. To save time, GitHub normally downloads only
the most recent commit of your repository. This plugin reads the whole history,
so with only one commit available every page would show the same date.

Tell the checkout step to bring everything:

```yaml title=".github/workflows/deploy.yml"
      - name: Get the files
        uses: actions/checkout@v7
        with:
          fetch-depth: 0
```

`fetch-depth: 0` means "no limit". Without it the plugin still works, it just
reports the wrong dates.

## Plugins that come with the theme

Material for MkDocs ships several plugins of its own. There is nothing to
install: list them and they work.

| Plugin | What it does |
| --- | --- |
| `tags` | Add tags to pages and get an index of them |
| `blog` | Turn a folder into a blog with dates and archives |
| `offline` | Build a site that works from a USB stick, with no web server |
| `privacy` | Download external fonts and images so visitors are not tracked |

```yaml title="mkdocs.yml"
plugins:
  - search
  - tags
```

!!! note "Two of them need extra software"
    The `social` plugin, which generates preview images for social media, and
    `optimize`, which compresses images, both rely on libraries that are
    installed outside pip. They are worth knowing about, but leave them until
    everything else is comfortable.

## Plugins worth knowing about

| Write this in `mkdocs.yml` | Install this with pip | What you get |
| --- | --- | --- |
| `search` | nothing, built in | The search box |
| `git-revision-date-localized` | `mkdocs-git-revision-date-localized-plugin` | Last updated dates |
| `glightbox` | `mkdocs-glightbox` | Click an image to enlarge it |
| `minify` | `mkdocs-minify-plugin` | Smaller, faster pages |
| `redirects` | `mkdocs-redirects` | Old addresses keep working after you rename a page |
| `awesome-pages` | `mkdocs-awesome-pages-plugin` | Build the menu from the folder structure, without writing `nav` |
| `mkdocstrings` | `mkdocstrings[python]` | Reference pages generated from Python docstrings |

Start with one. Every plugin is another thing that can break a build, so add
them when you actually want what they do.

## Where to find more

* The [MkDocs plugin catalog](https://github.com/mkdocs/catalog), a maintained
  list of everything available.
* The [Material for MkDocs plugin reference](https://squidfunk.github.io/mkdocs-material/plugins/),
  for the ones that come with the theme.

Each plugin's page lists its options. There is no single place documenting all
of them, because each is a separate project.

## When something breaks

??? failure "`The 'xxx' plugin is not installed`"
    Either it really is not installed, or you used the pip package name where
    the plugin name belongs. You install `mkdocs-glightbox` and you write
    `glightbox`. Check the plugin's page for the exact spelling of both.

??? failure "The search box has disappeared"
    You wrote a `plugins` section and left `search` out of it. Add it back as
    the first entry.

??? failure "It works on my computer but the Actions run fails"
    The plugin is missing from `requirements.txt`. Add it, with the version
    from `pip show <package-name>`, then push again.

??? failure "Every page says it was last updated today"
    The `fetch-depth: 0` line is missing from the checkout step in
    `.github/workflows/deploy.yml`. GitHub only downloaded the latest commit,
    so that is the only date the plugin can see.

??? failure "`Config value 'plugins': Plugin 'xxx' option 'yyy': unrecognised`"
    That option does not exist for that plugin, or it is indented wrongly.
    Options go two spaces further in than the plugin name, and the plugin name
    needs a colon after it when it has options.

---

That is the last step. Keep the [Cheat sheet](cheatsheet.md) nearby, and use
[Troubleshooting](troubleshooting.md) when something misbehaves.
