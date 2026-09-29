#!/usr/bin/env python3
"""
fix_site.py - one-shot fix for the Kavosh site after moving to kavoshspace.ir

Run it from the repo's root folder (next to index.html):

    python fix_site.py --dry-run     # only report, change nothing
    python fix_site.py               # apply

(On Windows, if "python" is not found, use:  py fix_site.py)

What it does (exact text replacement, line endings and everything else untouched):
  1. https://kavosh-space.github.io  ->  https://kavoshspace.ir   (canonical, og:url, og:image, JSON-LD, ...)
  2. Nav links to offerings.html  ->  workshops.html   (only if workshops.html exists)
  3. Old flat nav (no "About" dropdown, e.g. in sky-map.html) -> the current site nav
It skips .git / .github and never touches the GitHub repo link.
It is safe to run twice.
"""
import os
import re
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

DRY = "--dry-run" in sys.argv
ROOT = os.path.dirname(os.path.abspath(__file__))
SELF = os.path.basename(__file__)

OLD_HOST = b"https://kavosh-space.github.io"
NEW_HOST = b"https://kavoshspace.ir"
TEXT_EXT = (".html", ".xml", ".txt", ".py", ".js", ".json", ".css", ".md")
SKIP_DIRS = {".git", ".github", "node_modules"}

NAV_TEMPLATE = """<nav class="nav-links" id="navLinks">
    <a href="index.html">\u062e\u0627\u0646\u0647</a>
    <a href="news.html">\u0627\u062e\u0628\u0627\u0631</a>
    <a href="tools.html"{tools_active}>\u0627\u0628\u0632\u0627\u0631 \u0631\u0635\u062f</a>
    <a href="tours.html">\u06af\u0634\u062a \u0631\u0635\u062f\u06cc</a>

    <div class="nav-dropdown" id="navAboutDropdown">
      <button class="nav-dropdown-toggle" aria-expanded="false">\u062f\u0631\u0628\u0627\u0631\u0647 \u0645\u0627</button>
      <div class="nav-dropdown-menu">
        <a href="about.html">\u062f\u0631\u0628\u0627\u0631\u0647 \u06a9\u0627\u0648\u0634</a>
        <a href="team.html">\u0627\u0639\u0636\u0627</a>
        <a href="workshops.html">\u06a9\u0627\u0631\u06af\u0627\u0647\u200c\u0647\u0627</a>
      </div>
    </div>

    <a href="contact.html">\u062a\u0645\u0627\u0633 \u0628\u0627 \u0645\u0627</a>

    <button class="nv-toggle" id="nvToggle" aria-pressed="false">
      <span class="nv-dot"></span>
      <span id="nvLabel">\u062d\u0627\u0644\u062a \u0631\u0635\u062f</span>
    </button>
  </nav>"""
NAV_ACTIVE_FOR = {"sky-map.html": "tools.html"}      # page -> which nav item is highlighted
NAV_RE = re.compile(rb'<nav class="nav-links" id="navLinks">.*?</nav>', re.S)

has_workshops = os.path.exists(os.path.join(ROOT, "workshops.html"))
report = {"host": [], "offerings": [], "nav": []}
leftovers = []

for folder, dirs, files in os.walk(ROOT):
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
    for name in files:
        if name == SELF or not name.lower().endswith(TEXT_EXT):
            continue
        path = os.path.join(folder, name)
        rel = os.path.relpath(path, ROOT)
        with open(path, "rb") as f:
            data = orig = f.read()
        is_html = name.lower().endswith(".html")

        # 1) domain
        n = data.count(OLD_HOST)
        if n:
            data = data.replace(OLD_HOST, NEW_HOST)
            report["host"].append((rel, n))

        # 2) offerings.html -> workshops.html (links only)
        if is_html and has_workshops:
            n = data.count(b'href="offerings.html"') + data.count(b'href="../offerings.html"')
            if n:
                data = data.replace(b'href="offerings.html"', b'href="workshops.html"')
                data = data.replace(b'href="../offerings.html"', b'href="../workshops.html"')
                report["offerings"].append((rel, n))

        # 3) stale flat nav (root-level pages only; news/ pages are rebuilt by build_news.py)
        if is_html and os.path.dirname(rel) == "":
            m = NAV_RE.search(data)
            if m and b"nav-dropdown" not in m.group(0):
                active = ' class="active"' if NAV_ACTIVE_FOR.get(name) == "tools.html" else ""
                block = NAV_TEMPLATE.format(tools_active=active)
                if b"\r\n" in data:
                    block = block.replace("\n", "\r\n")
                data = data[:m.start()] + block.encode("utf-8") + data[m.end():]
                report["nav"].append(rel)

        if data != orig and not DRY:
            with open(path, "wb") as f:
                f.write(data)

        for i, line in enumerate(data.split(b"\n"), 1):
            if b"kavosh-space.github.io" in line and b"github.com/kavosh-space/kavosh-space.github.io" not in line:
                leftovers.append((rel, i, line.strip()[:110].decode("utf-8", "replace")))

print(("DRY RUN - nothing was written\n" if DRY else "") + "=== summary ===")
print(f"1) domain switched:      {sum(n for _, n in report['host'])} replacements in {len(report['host'])} files")
print(f"2) offerings -> workshops: {sum(n for _, n in report['offerings'])} links in {len(report['offerings'])} files"
      + ("" if has_workshops else "   (skipped: workshops.html not found)"))
print(f"3) old nav replaced in:  {', '.join(report['nav']) or 'no file needed it'}")

if report["offerings"]:
    print("\nFiles whose offerings.html link was changed:", ", ".join(r for r, _ in report["offerings"]))
if os.path.exists(os.path.join(ROOT, "offerings.html")):
    print("\nNOTE: offerings.html still exists in the repo but nothing links to it anymore.")
    print("      If it is the old version of workshops.html, delete it (or keep it and tell me).")
if leftovers:
    print("\nStill mentions the old host in another form - check by hand:")
    for r, i, l in leftovers:
        print(f"  {r}:{i}: {l}")
else:
    print("\nNo other mentions of the old host left.")
