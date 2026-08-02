# Writing a tutorial of your own

Everything up to here was about the tool. This page is about the writing, and
about the handful of MkDocs settings that matter specifically when what you are
publishing is a tutorial rather than reference documentation.

It is written from the mistakes made in this one. Every example below is a real
bug that shipped on this site and had to be fixed.

## The rule everything else follows from

**Someone new cannot tell your mistake from their own.**

An experienced reader who sees `!!! note` printed as plain text on their page
thinks "ah, I need the extension" and carries on. A beginner seeing exactly the
same thing has one hypothesis available, which is that they typed it wrong. They
have no way to check. They stop.

So the way a tutorial fails is not by being too complicated. It fails by being
**untrue**, in a way so small that you cannot see it any more.

Look at the pattern in the bugs this site shipped:

| What the page promised | What the reader got |
| --- | --- |
| `~~struck out~~` renders as struck out | The tildes, printed | 
| Coloured boxes from `!!! note` | The exclamation marks, printed |
| `:root { --md-primary-fg-color: ... }` changes the colour | Nothing at all |
| `include_source: true` gives a download link | No link anywhere |
| "Python 3.9 or newer" is enough | A plugin in step 9 refusing to install |
| A link to another page from inside a notebook | A 404 |

Not one of those is a complexity problem. All six are the same problem: the text
described something the reader's machine was not going to do.

## Order by the reader's clock, not by topic

"Markdown syntax goes in the Markdown chapter" is a sensible table of contents
and it is how this tutorial got its worst bug. Coloured boxes were taught in
step 4; the configuration that makes them work arrived in step 5.

A tutorial is not organised by subject. It is organised along a timeline of one
machine's state. At every point, the only things you may demonstrate are the
things that already work.

When something genuinely has to come early, give the reader what it needs then
and there, and defer only the explanation:

```markdown
Open `mkdocs.yml`, add these three lines, and save. Step 5 explains
what that section is.
```

Three lines they do not understand yet, but that work, beat a forward reference
to a page they have not read.

## Show what success looks like

The question a beginner is actually asking is not "how does this work?". It is
**"am I still all right?"**. Answer it often.

* A screenshot captioned "this is what you should see now".
* The exact output of a command, so they can compare character by character.
* A short checklist at the end of a page.

Without those, someone who went wrong at step 3 finds out at step 8, with no
idea which of the five things in between was the one.

## Name the failure where it can happen

Not in a troubleshooting appendix. Right next to the step, before they hit it:

```markdown
!!! danger "The most common mistake"
    If Source is left on Deploy from a branch, the workflow runs, says it
    succeeded, and your address still shows a 404.
```

A named failure is another checkpoint. It converts "I am stuck and I do not know
why" into "I am at the known problem, and the fix is right here".

Keep the long ones folded so the page stays scannable for everyone else:

```markdown
??? failure "`mkdocs: command not found`"
    Three things to check, in this order...
```

## Explain exactly as much as buys a diagnosis

Not the theory. Not nothing either. The amount that makes the *next* error
interpretable.

"The theme writes those variables on the `<body>` tag, so a `:root` block is
overruled" is worth a paragraph, because the reader will now recognise the whole
family of problems where a rule looks right and does nothing.

## Short is not the same as simple

The temptation is to cut. Removing one caveat from this site's plugin page,
about `fetch-depth: 0`, would make it shorter and would leave every reader's
"last updated" dates wrong.

Someone with no experience will happily read three hundred words that keep them
moving, and will quit at thirty that leave them stuck. Simple means no gaps
between what you wrote and what happens. It does not mean brief.

## Make the site the example

The strongest structural defence is that the thing you are teaching is also the
thing you are publishing. Then a claim that stops being true tends to break
visibly, in your own face, instead of quietly on a stranger's laptop.

Where that is not possible, keep a folder with a worked example that you rebuild
before every release.

## The MkDocs settings that matter for a tutorial

Most of the theme is a matter of taste. These are not.

```yaml title="mkdocs.yml"
theme:
  name: material
  features:
    - navigation.footer      # previous and next links: the reader is on a path
    - content.code.copy      # nobody should retype a command
    - content.action.edit    # readers report your mistakes by fixing them
    - toc.follow

markdown_extensions:
  - admonition               # named failures and checkpoints
  - pymdownx.details         # long error messages, folded away
  - pymdownx.keys            # ++ctrl+c++ looks like a key, not like text
  - pymdownx.superfences
  - pymdownx.tabbed:         # Windows / macOS / Linux without three pages
      alternate_style: true

validation:
  omitted_files: warn
  absolute_links: warn
  unrecognized_links: warn
  anchors: warn              # a dead link mid-tutorial is a dead end
```

And four habits around them:

**Number your pages in `nav`.** `1.`, `2.`, `3.` in the labels. It tells the
reader there is an order and where they are in it, which no sidebar does on its
own.

```yaml title="mkdocs.yml"
nav:
  - Start here: index.md
  - 1. Install the tools: install.md
  - 2. Build your first site: first-site.md
```

**Use tabs for the differences between systems**, not separate pages. A reader
on Windows should never have to work out which of three pages is theirs.

**Put the file name on every code block** with `title="..."`, so nobody has to
guess where the contents go.

**Build with `--strict`.** In a tutorial a broken internal link is not a
cosmetic flaw, it is the reader's path disappearing under them.

## Test it by running it, not by reading it

Rereading your own tutorial proves nothing. You read it with the knowledge that
makes it work: you look at `!!! note` and you see a box.

**Follow it yourself in an empty folder.** Once, all the way through, doing
exactly and only what the page says. That is how the coloured-box bug on this
site was found, after the page had been reviewed several times without anyone
noticing.

**Then automate the part that can be automated.** This repository carries
[`tools/check_tutorial.py`](https://github.com/one-bag/mkdocs-tutorial/blob/main/tools/check_tutorial.py),
which renders every snippet the tutorial teaches twice: once with the finished
configuration this site has, and once with the configuration the reader actually
has at that point. Any difference is a promise the reader cannot keep. It runs
in CI, before the site is built, so the class of bug cannot come back.

The idea transfers even if the code does not. Ask of every tutorial you write:
what would have to be true on the reader's machine for this paragraph to be
honest, and is it true *yet*?

!!! tip "The one habit worth keeping"
    Before publishing a page, reread it as someone who will believe every word,
    has no way to check any of it, and will blame themselves when it does not
    work. Everything else on this page follows from taking that person
    seriously.
