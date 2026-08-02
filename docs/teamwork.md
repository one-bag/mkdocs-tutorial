# 12. Work with other people

Everything so far assumed one person, changing a page and publishing it
straight away. That works well, and it keeps working for a long time.

It stops working the day someone else joins, or the day you want a second pair
of eyes before something goes live. This page covers both, and it is the last
piece of GitHub you need.

## The idea in one picture

```text
main        ────●────────────────────●──────  the published site
                 \                  /
your branch       ●───●───●────────●          your work, invisible to visitors
                  add   fix        pull request:
                  page  typo       checked, reviewed, merged
```

A **branch** is a parallel copy of the files where you can change anything
without touching the live site. A **pull request** is the moment you say "I
think this is ready", and it is where the checks run and other people comment.
Merging it puts your work on `main`, which publishes it.

Nothing about your site changes until you merge. That is the whole point.

## Why bother, if it is just you

Three reasons, and the first one alone is usually enough:

* **A half finished page never goes live.** Right now, every commit publishes.
  On a branch you can leave something unfinished overnight.
* **The build is checked before it counts.** A pull request runs the same build
  as a publish, so a broken link or an invalid `mkdocs.yml` is caught while it
  is still easy to fix.
* **You can change your mind.** Deleting a branch costs nothing and leaves no
  trace.

## Make the checks run on pull requests

Out of the box the workflow from [step 8](publish.md) only runs when something
reaches `main`, which is too late to be useful. Add a second trigger, and stop
the publishing half from running on pull requests:

```yaml title=".github/workflows/deploy.yml"
on:
  push:
    branches:
      - main
  pull_request:          # (1) build and check proposed changes too
    branches:
      - main
  workflow_dispatch:

jobs:
  build:
    # ... unchanged ...

  deploy:
    needs: build
    if: github.event_name != 'pull_request'   # (2) only main gets published
    # ... unchanged ...
```

1. Every pull request aimed at `main` now gets built exactly as a publish would
   be.
2. Without this line, a pull request would try to publish itself, which is both
   wrong and impossible for anyone outside the project.

This site's own workflow does precisely that, and you can
[read it](https://github.com/one-bag/mkdocs-tutorial/blob/main/.github/workflows/deploy.yml).

## The flow, in the browser

No terminal needed. GitHub makes a branch for you at the moment you commit.

1. Open the file you want to change and click the pencil icon.
2. Make your changes.
3. Click **Commit changes**, and in the dialog choose
   **Create a new branch for this commit and start a pull request**.
4. Give the branch a short name, such as `fix-install-typo`.
5. Click **Propose changes**, then **Create pull request**.

The pull request page opens. Within a minute or two a line appears at the
bottom saying whether the checks passed. Green means the site still builds.

6. When you are happy, click **Merge pull request**, then **Confirm merge**.
7. Click **Delete branch**. The work is on `main`, so the branch has done its
   job.

Merging counts as a push to `main`, so the site publishes itself as usual.

## The flow, with git

```bash
git switch -c fix-install-typo    # create a branch and move onto it
# ... edit files ...
git add .
git commit -m "Fix the typo in the install page"
git push -u origin fix-install-typo
```

The push prints a link that opens the pull request page. Or use the GitHub CLI:

```bash
gh pr create --fill
gh pr checks --watch
gh pr merge --squash --delete-branch
```

Back on your machine afterwards:

```bash
git switch main
git pull
```

That last step matters. Your computer does not know about the merge until you
ask, and starting the next branch from an old `main` is how conflicts happen.

| Command | What it does |
| --- | --- |
| `git switch -c name` | Make a branch and move onto it |
| `git switch main` | Go back to the main line |
| `git branch` | List your branches, marking the one you are on |
| `git pull` | Bring down what has been merged since |
| `git branch -d name` | Delete a branch you have finished with |

## Reviewing someone else's work

On the pull request, the **Files changed** tab shows every line added in green
and removed in red. Hover over a line number and click the blue **+** to
comment on that exact line.

Useful things to check in a documentation change, roughly in order:

- [ ] Did the checks pass? If not, nothing else matters yet.
- [ ] Does a new page appear in `nav`? A page missing from it is invisible.
- [ ] Do the instructions work at the point they appear, with only what the
      reader has been given so far?
- [ ] Are new links pointing at pages that exist?
- [ ] Do new images have a description in the square brackets?

The reviewer does not have to be a writer. Someone following the steps and
saying where they got lost is worth more than someone polishing the grammar.

## Insisting on the checks

Once more than one person can merge, it is worth making the checks compulsory
rather than advisory. In **Settings > Branches**, add a branch protection rule
for `main` and tick **Require status checks to pass before merging**, then
choose the build check.

From then on the **Merge** button stays disabled until the site is known to
build. It is the same guarantee as before, except nobody has to remember it.

## When two people change the same lines

GitHub says the branch has conflicts and offers **Resolve conflicts**. It shows
the file with both versions marked:

```text
<<<<<<< your-branch
The text you wrote.
=======
The text they wrote.
>>>>>>> main
```

Delete the markers and the version you do not want, leaving the text you do,
then click **Mark as resolved** and **Commit merge**.

Conflicts feel alarming and are almost always trivial in documentation: two
people improved the same paragraph. Nothing is lost, and both versions are
sitting right there in front of you.

!!! tip "How to have fewer of them"
    Short branches. A branch that lives for an afternoon rarely conflicts; one
    that lives for a month usually does. Merge early, and start each new branch
    from a fresh `git pull`.

---

Next: [writing a tutorial of your own](writing-a-tutorial.md), if what you are
publishing is one.
