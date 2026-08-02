# 2. Install the tools

You need two things: Python, and MkDocs itself. This page walks through both,
with a check after each step so you always know where you stand.

## Step 1: open a terminal

=== "Windows"

    Press ++windows++, type `powershell`, and open **Windows PowerShell**.

=== "macOS"

    Press ++cmd+space++, type `terminal`, and press ++enter++.

=== "Linux"

    Press ++ctrl+alt+t++, or look for **Terminal** in your applications menu.

A window opens with a blinking cursor. That is where every command in this
tutorial goes. Type the command, press ++enter++, wait for it to finish.

!!! tip "Nothing here can break your computer"
    Every command in this tutorial either installs a program, prints
    information, or creates files inside a folder you choose. None of them
    delete anything.

## Step 2: check whether you already have Python

=== "Windows"

    ```powershell
    python --version
    ```

=== "macOS / Linux"

    ```bash
    python3 --version
    ```

If you see something like `Python 3.12.2`, you are set. Skip to step 4.

If you see an error, or a version starting with `2.`, install Python first.

## Step 3: install Python (only if step 2 failed)

=== "Windows"

    1. Go to [python.org/downloads](https://www.python.org/downloads/).
    2. Click the big yellow **Download Python** button.
    3. Run the file you downloaded.
    4. **Important:** tick the box that says **Add python.exe to PATH** at the
       bottom of the first screen, before clicking Install Now.
    5. When it finishes, close PowerShell, open it again, and run
       `python --version` to confirm.

    Forgetting the PATH checkbox is the single most common problem on Windows.
    If you forgot it, run the installer again, choose **Modify**, and enable it.

=== "macOS"

    1. Go to [python.org/downloads](https://www.python.org/downloads/).
    2. Click **Download Python**, open the `.pkg` file and follow the installer.
    3. Close Terminal, open it again, and run `python3 --version` to confirm.

    If you use Homebrew, `brew install python` works just as well.

=== "Linux"

    Most distributions already include Python. If not:

    ```bash
    # Debian, Ubuntu, Mint
    sudo apt update && sudo apt install python3 python3-pip python3-venv

    # Fedora
    sudo dnf install python3 python3-pip
    ```

## Step 4: create a folder for your project

Pick where your documentation will live and move into it. Here we use a folder
called `my-docs` inside your home directory.

=== "Windows"

    ```powershell
    cd $HOME
    mkdir my-docs
    cd my-docs
    ```

=== "macOS / Linux"

    ```bash
    cd ~
    mkdir my-docs
    cd my-docs
    ```

`cd` means "change directory", `mkdir` means "make directory". The terminal is
now working inside that folder, and everything you create lands there.

## Step 5: create a virtual environment

A virtual environment is a private box for this project's tools. It keeps
MkDocs out of the rest of your system, so nothing you install here can break
anything else on your computer.

=== "Windows"

    ```powershell
    python -m venv .venv
    .venv\Scripts\Activate.ps1
    ```

    If PowerShell refuses with a message about execution policies, run this once
    and then try again:

    ```powershell
    Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
    ```

=== "macOS / Linux"

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

Your prompt now starts with `(.venv)`. That is how you know the box is open.

!!! warning "You have to do this every time"
    The `(.venv)` marker disappears when you close the terminal. Next time you
    work on your docs, move into the folder and run the activate line again.
    That is the whole ritual, and it takes two seconds.

## Step 6: install MkDocs

```bash
pip install mkdocs-material
```

One package, two results: `mkdocs-material` is the theme, and installing it
pulls in MkDocs itself automatically. You do not need a separate command.

The download takes a few seconds. A wall of text scrolling past is normal.

## Step 7: check that it worked

```bash
mkdocs --version
```

You should see something like:

```text
mkdocs, version 1.6.1 from ... (Python 3.12)
```

If you do, you are done here.

??? failure "It says `mkdocs: command not found` or `'mkdocs' is not recognized`"
    Three things to check, in this order:

    1. Is `(.venv)` at the start of your prompt? If not, activate the virtual
       environment again (step 5).
    2. Are you in the `my-docs` folder? Run `cd ~/my-docs` on macOS or Linux,
       `cd $HOME\my-docs` on Windows.
    3. Did `pip install mkdocs-material` actually finish, or did it end in a
       red error? Scroll up and read the last few lines.

    More cases are collected on the [Troubleshooting](troubleshooting.md) page.

---

Next: [build your first site](first-site.md).
