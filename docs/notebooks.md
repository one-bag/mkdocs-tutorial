# 11. Add Jupyter notebooks

If your work lives in Jupyter notebooks, you do not have to export them to PDF,
paste screenshots into a page, or ask people to download a `.ipynb` and open it
themselves. A notebook can be a page of your site, with its code, its printed
output and its charts all in place.

!!! tip "There is a real one on this site"
    Have a look at the [Example notebook](example-notebook.ipynb). It is a
    genuine `.ipynb` file sitting in the `docs` folder, rendered by the setup
    described on this page.

## What it looks like

The plugin turns each part of the notebook into part of the page:

| In the notebook | On the page |
| --- | --- |
| A Markdown cell | Ordinary page text, headings included |
| A code cell | A code block, highlighted, with a copy button |
| A printed result | The text below the code, as you saw it |
| A table, for example a DataFrame | A real HTML table |
| A chart or any image | An image, stored inside the notebook file |

Nothing is lost and nothing has to be maintained twice.

## Setting it up

### Step 1: install the plugin

```bash
pip install mkdocs-jupyter
```

### Step 2: switch it on

```yaml title="mkdocs.yml"
plugins:
  - search
  - mkdocs-jupyter:
      include: ["*.ipynb"]
      execute: false
      include_source: true
```

This is one of the rare plugins where the name you write matches the package
you install. And as always, `search` has to stay on the list or the search box
disappears. That rule is explained in [step 9](plugins.md#the-rule-that-catches-everyone).

!!! warning "Set `include` yourself"
    Left alone, this plugin also claims `*.md` and `*.py` files. Your Markdown
    pages will still build, but they are then handled by the plugin rather than
    by MkDocs, and some theme features stop behaving. Writing
    `include: ["*.ipynb"]` keeps each tool to its own job.

    Leave `*.py` in the list only if you write scripts in the percent format,
    where `# %%` separates the cells. Those get rendered like notebooks too.

### Step 3: put the notebook in `docs`

```text
my-docs/
├── mkdocs.yml
└── docs/
    ├── index.md
    └── analysis.ipynb
```

It is an ordinary file in an ordinary folder. Copy it in, or work on it right
there.

### Step 4: add it to the menu

```yaml title="mkdocs.yml"
nav:
  - Home: index.md
  - Analysis: analysis.ipynb
```

Exactly like a Markdown page, with the real file extension.

### Step 5: pin it

```text title="requirements.txt"
mkdocs-jupyter==0.26.3
```

Otherwise the site builds on your computer and fails on GitHub, which is
covered in [step 9](plugins.md#step-4-add-it-to-requirementstxt).

## The one decision that matters: execute or not

The plugin can either use the outputs already saved in your notebook, or run
every notebook again each time the site is built.

| | `execute: false`, the default | `execute: true` |
| --- | --- | --- |
| Where the outputs come from | The saved notebook | A fresh run at build time |
| Build speed | Instant | As slow as your slowest notebook |
| What GitHub needs | Nothing extra | Every library your notebooks import, plus any data files they read |
| A cell that raises an error | Nothing happens, the saved output stands | Can fail the whole build |
| Result if you forget to save | The page shows the old outputs | Always current |

**Start with `execute: false`.** Run your notebooks yourself, check the output
is what you meant, save, and commit. The published page then shows exactly what
you saw. It is also the only option that works when a notebook needs data,
credentials or hardware that GitHub does not have.

Switch to `execute: true` only when a notebook is fully self contained and you
want it re-run as a check. If you do, remember that every import inside it now
belongs in `requirements.txt`, and consider `allow_errors: false` so a broken
cell stops the build instead of publishing quietly.

You can also run most of them and skip the awkward ones:

```yaml title="mkdocs.yml"
plugins:
  - search
  - mkdocs-jupyter:
      include: ["*.ipynb"]
      execute: true
      execute_ignore:
        - "notebooks/needs-the-database.ipynb"
```

## The options you are likely to want

| Option | Default | What it does |
| --- | --- | --- |
| `include` | `["*.py", "*.ipynb", "*.md"]` | Which files the plugin handles. Set it to `["*.ipynb"]`. |
| `ignore` | empty | Files to skip entirely |
| `execute` | `false` | Run the notebooks at build time |
| `execute_ignore` | empty | Notebooks to leave alone when `execute` is on |
| `allow_errors` | `true` | With `execute`, whether a failing cell is tolerated |
| `include_source` | `false` | Copy the original `.ipynb` into the built site, so it can be downloaded |
| `ignore_h1_titles` | `false` | Use the `nav` label as the title instead of the notebook's first heading |
| `no_input` | `false` | Show only the outputs, hiding all the code |
| `kernel_name` | automatic | Force a particular kernel when executing |
| `toc_depth` | `6` | How deep the table of contents goes |

`no_input: true` is worth remembering. It turns a notebook into a clean report
of results with no code in sight, which is often what a non technical reader
wants.

!!! warning "`include_source` does not add a button"
    It is easy to misread. The option copies the `.ipynb` into the built site
    next to its page, and stops there. No download link appears anywhere: if
    you want one, you write it yourself.

    The copied file sits at the page address followed by the file name, so for
    the example on this site that is
    [example-notebook.ipynb](https://one-bag.github.io/mkdocs-tutorial/example-notebook/example-notebook.ipynb).
    Add a Markdown cell at the top of your notebook with a link of that shape
    and readers get their download.

    Without the option the file is not published at all, and any link to it is
    a dead end.

## Links written inside a notebook

This one is easy to get wrong and nothing warns you about it.

On a normal Markdown page you link to another page by its file name, and MkDocs
turns it into a real address for you:

```markdown
[the install page](install.md)
```

Inside a notebook that does not happen. The notebook is rendered by the plugin,
not by MkDocs, so the link is published exactly as you typed it and leads
nowhere. Write the address the reader's browser will actually need:

```markdown
[the install page](../install/)
```

The `../` is there because each page sits in its own folder. From
`/example-notebook/`, going up one level and into `install` gives
`/install/`.

!!! warning "`mkdocs build --strict` does not catch this"
    Link checking only covers the pages MkDocs renders itself. A broken link
    in a notebook builds green and 404s for your readers. Click the links in
    your notebooks once, on the published site, and you will never think about
    it again.

## Titles

By default the first `#` heading inside the notebook becomes the page title,
and the `nav` label is only used for the menu entry. If you would rather the
`nav` label won, set `ignore_h1_titles: true`.

Either way, give each notebook one `#` heading at the top, exactly as you would
for a Markdown page.

## Before you commit a notebook

??? warning "Check what is in the outputs"
    Outputs are saved inside the file and published as they are. A stray
    `print(df)` can put personal data on a public website, an error traceback
    can reveal the full paths of your home directory, and an API key printed
    once stays in the file. Look at the notebook before pushing it.

??? warning "Watch the file size"
    Every chart is stored inside the `.ipynb` as an encoded image. A notebook
    with fifty plots can reach several megabytes, and git keeps every version
    of it forever. Delete the outputs you do not need before saving.

??? info "Notebooks make ugly diffs"
    A `.ipynb` is a JSON file, so `git diff` on one is close to unreadable. It
    works, it is just unpleasant. If it becomes a problem, look at `nbstripout`
    to drop outputs automatically, or `jupytext` to keep a plain text twin of
    each notebook. Neither is necessary to get started.

## Charts and dark mode

Charts do not follow your site's dark mode. They are images, generated when the
cell ran, and they keep whatever background they had at that moment.

A chart saved with a transparent background looks fine on a white page and
becomes unreadable when a visitor switches to dark mode: dark axis labels on a
dark page. Give your figures an explicit background instead:

```python
fig, ax = plt.subplots(figsize=(7, 3.5), facecolor="white")
ax.set_facecolor("white")
```

The chart then reads as a white card on the dark page, which is not elegant but
is legible. That is what the [example notebook](example-notebook.ipynb) does,
and you can check it by switching this site to dark mode.

## When it does not work

??? failure "The notebook is not in the menu and its address gives a 404"
    Add it to `nav`, with the `.ipynb` extension, exactly like a Markdown page.

??? failure "My Markdown pages started rendering oddly"
    The plugin took them over. Add `include: ["*.ipynb"]` to its configuration.

??? failure "The build fails only when `execute` is on"
    The build machine is missing something the notebook needs. Read the error:
    `ModuleNotFoundError` means a library is missing from `requirements.txt`,
    `FileNotFoundError` means the notebook reads a data file that is not in the
    repository. Either fix the cause or add that notebook to `execute_ignore`.

??? failure "The code shows but the charts and tables do not"
    The notebook was saved with its outputs cleared, so there is nothing to
    display. Run it again, save, and commit. Some editors and some `nbstripout`
    setups clear outputs on save, which is exactly the wrong behaviour here.

??? failure "`Alternative text is missing on 1 image(s)`"
    This comes from the tool that converts the notebook, not from MkDocs, and
    it means a chart has no text description for screen readers. It is printed
    on every build and it does not stop one, not even with `--strict`. There is
    no way to silence it from inside the notebook. Ignore it, and where the
    chart carries information that the surrounding text does not, describe it
    in a Markdown cell underneath.

??? failure "`has no git logs, using current timestamp`"
    Only relevant if you also use the "last updated" plugin from
    [step 9](plugins.md#the-worked-example-last-updated-dates). The notebook has
    not been committed yet, so there is no history to read a date from. With
    `--strict` this stops the build. Commit the notebook and it goes away.

??? failure "A `.cache` folder appeared in my project"
    That is this plugin storing rendered notebooks so later builds are faster.
    It is harmless and it does not belong in git. Add `.cache/` to your
    `.gitignore`.

---

That is the end of the tutorial. The [Cheat sheet](cheatsheet.md) has the
commands and [Troubleshooting](troubleshooting.md) has the errors.
