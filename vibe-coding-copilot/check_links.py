"""Static internal link checker for the generated site.
Scans every generated .html file (root + fr/nl/en) for <a href="..."> targets,
resolves relative links against the file's own directory, and reports:
  - links pointing to files that don't exist
  - anchor links (#id) whose target id doesn't exist anywhere in the target file
Ignores external links (http/https/mailto) and javascript:/tel: links.
"""
import re
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
HREF_RE = re.compile(r'href="([^"]+)"')
ID_RE = re.compile(r'id="([^"]+)"')

html_files = []
for lang in ("", "fr", "nl", "en"):
    d = os.path.join(ROOT, lang) if lang else ROOT
    if not os.path.isdir(d):
        continue
    for fn in os.listdir(d):
        if fn.endswith(".html"):
            html_files.append(os.path.join(d, fn))

errors = []
checked = 0

id_cache = {}


def rel(p):
    return os.path.relpath(p, ROOT)

def get_ids(path):
    if path in id_cache:
        return id_cache[path]
    if not os.path.isfile(path):
        id_cache[path] = set()
        return id_cache[path]
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    ids = set(ID_RE.findall(content))
    id_cache[path] = ids
    return ids

for path in html_files:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    base_dir = os.path.dirname(path)
    for href in HREF_RE.findall(content):
        checked += 1
        if href.startswith(("http://", "https://", "mailto:", "javascript:", "tel:")):
            continue
        if href.startswith("#"):
            ids = get_ids(path)
            frag = href[1:]
            if frag and frag not in ids:
                errors.append(f"{rel(path)}: broken same-page anchor '{href}'")
            continue
        # split off fragment
        if "#" in href:
            file_part, frag = href.split("#", 1)
        else:
            file_part, frag = href, None
        if file_part == "":
            target_path = path
        else:
            target_path = os.path.normpath(os.path.join(base_dir, file_part))
        if not os.path.isfile(target_path):
            errors.append(f"{rel(path)}: missing target file for href='{href}' -> {rel(target_path)}")
            continue
        if frag:
            ids = get_ids(target_path)
            if frag not in ids:
                errors.append(f"{rel(path)}: anchor '#{frag}' not found in {rel(target_path)} (href='{href}')")

if errors:
    print(f"Checked {checked} href attributes across {len(html_files)} files.")
    print(f"FOUND {len(errors)} problem(s):\n")
    for e in errors:
        print(" -", e)
    sys.exit(1)
else:
    print(f"Checked {checked} href attributes across {len(html_files)} files. All internal links resolve correctly.")
