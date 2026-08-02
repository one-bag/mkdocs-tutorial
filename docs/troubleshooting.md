# Troubleshooting

Find your error message below. They are grouped by where the problem happens.

## On your computer

??? failure "`mkdocs: command not found` or `'mkdocs' is not recognized`"
    The terminal cannot find the program. In order of likelihood:

    1. The virtual environment is not active. Your prompt should start with
       `(.venv)`. If it does not, run `source .venv/bin/activate` on macOS or
       Linux, `.venv\Scripts\Activate.ps1` on Windows.
    2. You are in the wrong folder. `cd` back into your project.
    3. It never installed. Run `pip install mkdocs-material` again and read the
       last lines of the output.

??? failure "`python: command not found`"
    On macOS and Linux the command is `python3`, not `python`.

    On Windows this usually means the **Add python.exe to PATH** box was not
    ticked during installation. Run the installer again, choose **Modify**, and
    enable it. Then close and reopen PowerShell.

??? failure "`Config file 'mkdocs.yml' does not exist`"
    You are running the command from the wrong folder. `mkdocs serve` has to be
    run from the folder that contains `mkdocs.yml`. Check with `ls` on macOS or
    Linux, `dir` on Windows.

??? failure "`[Errno 48] Address already in use`"
    Another `mkdocs serve` is still running, probably in a terminal window you
    forgot. Either press ++ctrl+c++ there, or use a different port:

    ```bash
    mkdocs serve -a localhost:8001
    ```

??? failure "`Error: mapping values are not allowed in this context`"
    A YAML problem in `mkdocs.yml`. The error gives a line number. The usual
    causes:

    - A tab character instead of spaces.
    - A missing space after a colon: `site_name:My docs` should be
      `site_name: My docs`.
    - A value containing a colon and not quoted:
      `site_description: "MkDocs: a guide"` needs those quotes.

    Look at the line above the reported one as well. Indentation errors get
    reported one line late.

## In the built site

??? failure "A page exists but is not in the menu"
    Once `mkdocs.yml` has a `nav` section, only pages listed there appear.
    Add a line for the new file.

??? failure "`Doc file contains a link ... but the target is not found`"
    A link points at a file that does not exist. Check the spelling, the
    folder, and that the target ends in `.md`. Link to `install.md`, not to
    `install` and not to `install.html`.

??? failure "The table of contents on the right is empty"
    A page needs headings for MkDocs to build one. Add `##` sections.

??? failure "My table renders as one long line of pipes"
    Tables need a blank line before them, and the separator row, `| --- |`,
    right under the header row.

??? failure "My list is not a list"
    A blank line is missing before the first item. Markdown requires an empty
    line between a paragraph and a list.

## On GitHub

??? failure "The Actions run fails at `mkdocs build --strict`"
    The build works locally but not on GitHub, which almost always means a
    broken internal link or a page missing from `nav`. Reproduce it on your
    machine with the same flag:

    ```bash
    mkdocs build --strict
    ```

    Fix what it reports, then push again.

??? failure "The Actions run fails with `Error: Resource not accessible by integration`"
    The workflow does not have permission to publish. The `permissions` block
    must be present exactly as shown in [step 8](publish.md#step-2-add-the-recipe):

    ```yaml
    permissions:
      contents: read
      pages: write
      id-token: write
    ```

    If it is there and the error persists, check
    **Settings > Actions > General > Workflow permissions** and make sure
    Actions are allowed to run.

??? failure "The Actions run fails at `pip install -r requirements.txt`"
    Either the file is missing from the repository, or it has a version that
    does not exist. Confirm the file is really on GitHub, and compare the
    version numbers against `pip show mkdocs mkdocs-material` on your machine.

??? failure "Green tick, but the address shows 404"
    **Settings > Pages > Source** is not set to **GitHub Actions**. This is the
    single most common cause. Change it, then rerun the workflow from the
    Actions tab.

    Also give it a couple of minutes on the very first deployment, and check
    the address carefully: it is
    `https://username.github.io/repository-name/`, with the repository name and
    the trailing slash.

??? failure "The site loads but has no styling"
    The browser is asking for the CSS at the wrong address. Set `site_url` in
    `mkdocs.yml` to your real Pages address, including the repository name and
    the trailing slash, then push again.

??? failure "The repository has thousands of files in it"
    The `site` folder was committed. Add a `.gitignore` containing `site/`,
    then:

    ```bash
    git rm -r --cached site
    git commit -m "Stop tracking the generated site folder"
    git push
    ```

??? failure "My changes are on GitHub but the website is old"
    Check the Actions tab. If there is no new run, the workflow file is not on
    the `main` branch or is not at `.github/workflows/deploy.yml`. If the run is
    green, your browser is showing a cached copy: reload with ++ctrl+shift+r++,
    or ++cmd+shift+r++ on macOS.

## Still stuck

1. Read the last five lines of the error. The answer is usually in there, in
   plain English, with a file name and a line number.
2. Undo your last change and confirm that things work again. That tells you
   which change caused it.
3. Search the exact error message. Someone has hit it before.
4. The official documentation is genuinely good:
   [MkDocs](https://www.mkdocs.org/) and
   [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).
