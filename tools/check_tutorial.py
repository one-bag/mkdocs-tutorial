#!/usr/bin/env python3
"""Check that everything the tutorial teaches works for the reader.

The failure mode this catches: a page shows the reader some Markdown and the
result it produces, but that feature needs configuration the reader has not
been given yet. The page looks right on this site, which has the finished
configuration, and produces raw text on theirs. A reader with no experience
cannot tell that apart from a mistake of their own, so it stops them dead.

Three checks, all done by rendering rather than by reading:

1. Every ```markdown block, rendered with the extensions the reader has at
   that point in the tutorial, must produce what this site shows.
2. Every "you write | you get" table row, same rule.
3. Everything taught anywhere must also work with the complete mkdocs.yml
   offered in step 5, because that is the configuration readers copy.

Run it with:  python3 tools/check_tutorial.py
"""

import re
import sys
from pathlib import Path

import markdown
import yaml

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
CONFIG = ROOT / "mkdocs.yml"

# Python-Markdown extensions MkDocs always enables, whatever the config says.
BUILTINS = ["toc", "tables", "fenced_code"]

# What the reader's own mkdocs.yml contains by the time they reach each page.
# Pages not listed here are read after step 5, so they get the full set.
READER_TIMELINE = {
    "index.md": BUILTINS,
    "what-is-mkdocs.md": BUILTINS,
    "install.md": BUILTINS,
    "first-site.md": BUILTINS,
    # Step 4 opens by telling the reader to add these three.
    "writing-pages.md": BUILTINS + [
        "admonition", "pymdownx.details", "pymdownx.tilde",
    ],
    # The shortcut page hands over a complete mkdocs.yml of its own.
    "quick-start.md": BUILTINS + [
        "admonition", "attr_list", "pymdownx.details", "pymdownx.superfences",
    ],
}

# Fenced blocks that are file contents, not Markdown meant to be rendered.
SKIP_PREFIXES = ("site_name:", "nav:", "plugins:", "theme:", "extra_css:")

# Markers that mean the reader sees raw syntax instead of a result.
LEFTOVERS = [
    (r"^\s*!!!\s", "admonition (!!!) shown as plain text"),
    (r"^\s*\?\?\?\s", "foldable box (???) shown as plain text"),
    (r"^\s*===\s+\"", "tabs (===) shown as plain text"),
    (r"~~[^~]+~~", "strikethrough (~~) shown as plain text"),
    (r"\+\+[a-z+]+\+\+", "keyboard keys (++) shown as plain text"),
]


class QuietLoader(yaml.SafeLoader):
    """YAML loader that tolerates the !!python/name: tags MkDocs allows."""


QuietLoader.add_multi_constructor(
    "tag:yaml.org,2002:python/name:", lambda *a: None)
QuietLoader.add_multi_constructor("!!python/name:", lambda *a: None)


def extension_names(items):
    return [i if isinstance(i, str) else next(iter(i)) for i in (items or [])]


def site_extensions():
    cfg = yaml.load(CONFIG.read_text(), Loader=QuietLoader)
    return extension_names(cfg.get("markdown_extensions"))


def step5_extensions():
    """The extensions in the complete file step 5 tells readers to copy."""
    text = (DOCS / "configuration.md").read_text()
    parts = text.split("## A complete file to copy", 1)
    if len(parts) != 2:
        raise SystemExit("check_tutorial: step 5 no longer has a section "
                         "called 'A complete file to copy'. Update this script.")
    block = re.search(r"```yaml[^\n]*\n(.*?)```", parts[1], re.S)
    if not block:
        raise SystemExit("check_tutorial: no mkdocs.yml block found in step 5.")
    cfg = yaml.load(block.group(1), Loader=QuietLoader)
    return BUILTINS + extension_names(cfg.get("markdown_extensions"))


def taught_snippets(text):
    """Yield (line, snippet, kind) for everything a page teaches."""
    # 1. ```markdown fences: "type this".
    for m in re.finditer(r"^(\s*)```+markdown\s*\n(.*?)^\1```+\s*$",
                         text, re.S | re.M):
        indent, body = m.group(1), m.group(2)
        if indent:
            body = "\n".join(line[len(indent):] if line.startswith(indent)
                             else line for line in body.split("\n"))
        if body.lstrip().startswith(SKIP_PREFIXES):
            continue
        yield text[:m.start()].count("\n") + 1, body, "block"

    # 2. Tables whose left column is the syntax and right column the result.
    for m in re.finditer(r"^\|\s*(?:``\s*)?`([^`]+)`(?:\s*``)?\s*\|", text, re.M):
        yield text[:m.start()].count("\n") + 1, m.group(1), "table row"


def python_version_problems():
    """The version the tutorial asks for must cover everything it installs.

    Catches the case where the core steps work on an old Python and an optional
    plugin taught later refuses to install on it.
    """
    import importlib.metadata as meta

    claimed = re.search(r"Python (\d+)\.(\d+) or newer",
                        (DOCS / "index.md").read_text())
    if not claimed:
        return ["index.md no longer states a Python version; update this script."]
    want = (int(claimed.group(1)), int(claimed.group(2)))

    packages = set(re.findall(r"pip install ([a-z0-9][a-z0-9._-]+)",
                              "\n".join(p.read_text() for p in DOCS.glob("*.md"))))
    packages |= {line.split("==")[0].strip()
                 for line in (ROOT / "requirements.txt").read_text().splitlines()
                 if line.strip() and not line.startswith("#")}

    problems = []
    for name in sorted(packages):
        try:
            spec = meta.metadata(name).get("Requires-Python") or ""
        except meta.PackageNotFoundError:
            continue          # not installed here, cannot check offline
        floor = re.search(r">=\s*(\d+)\.(\d+)", spec)
        if not floor:
            continue
        needs = (int(floor.group(1)), int(floor.group(2)))
        if needs > want:
            problems.append(
                f"{name} needs Python {needs[0]}.{needs[1]}+, but the tutorial "
                f"asks for {want[0]}.{want[1]}+")
    return problems


def profile(html):
    """Structural fingerprint of rendered HTML: tags plus telling classes."""
    tags = set(re.findall(r"<([a-z][a-z0-9]*)", html))
    classes = set()
    for value in re.findall(r'class="([^"]+)"', html):
        classes.update(value.split())
    keep = {"admonition", "tabbed", "task", "highlight", "keys"}
    return tags | {c for c in classes if c.split("-")[0] in keep}


def compare(snippet, shown_exts, reader_exts):
    """Return why the reader does not get what is shown, or None if they do."""
    try:
        as_shown = markdown.markdown(snippet, extensions=shown_exts)
        as_reader = markdown.markdown(snippet, extensions=reader_exts)
    except Exception as exc:
        return f"render failed: {exc}"
    if as_shown == as_reader:
        return None
    reasons = [label for pattern, label in LEFTOVERS
               if re.search(pattern, as_reader, re.M)
               and not re.search(pattern, as_shown, re.M)]
    missing = profile(as_shown) - profile(as_reader)
    if missing:
        reasons.append("reader is missing " + ", ".join(sorted(missing)))
    return "; ".join(reasons) if reasons else None


def main():
    site = site_extensions()
    step5 = step5_extensions()
    timeline_problems, step5_problems = [], []
    checked = 0

    for page in sorted(DOCS.glob("*.md")):
        reader = READER_TIMELINE.get(page.name, site)
        for line, snippet, kind in taught_snippets(page.read_text()):
            checked += 1
            where = f"docs/{page.name}:{line} ({kind})"
            reason = compare(snippet, site, reader)
            if reason:
                timeline_problems.append((where, reason))
            reason = compare(snippet, site, step5)
            if reason:
                step5_problems.append((where, reason))

    version_problems = python_version_problems()

    print(f"Checked {checked} taught snippets by rendering them, and the "
          "stated Python version\nagainst every package the tutorial installs.\n")

    ok = True
    if version_problems:
        ok = False
        print(f"{len(version_problems)} problem(s) with the Python version "
              "the tutorial asks for:")
        for problem in version_problems:
            print(f"  {problem}")
        print()
    if timeline_problems:
        ok = False
        print(f"{len(timeline_problems)} snippet(s) the reader cannot "
              "reproduce at that point in the tutorial:")
        for where, reason in timeline_problems:
            print(f"  {where}\n      {reason}")
        print()
    if step5_problems:
        ok = False
        print(f"{len(step5_problems)} snippet(s) that still fail with the "
              "complete mkdocs.yml from step 5:")
        for where, reason in step5_problems:
            print(f"  {where}\n      {reason}")
        print()

    if ok:
        print("OK: everything the tutorial teaches works with the "
              "configuration the reader\n    has when they meet it, and with "
              "the complete file step 5 hands them.")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
