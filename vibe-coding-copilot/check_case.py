"""Case-sensitivity link audit. Windows/NTFS is case-insensitive so href="X.HTML"
resolving to "x.html" works locally but silently 404s on GitHub Pages (Linux, case-sensitive).
This script flags any href/src whose case doesn't exactly match the real file on disk."""
import re
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
PATTERN = re.compile(r'(?:href|src)="([^"#][^"]*)"')

issues = []
checked = 0

for lang in ("fr", "nl", "en"):
    d = os.path.join(ROOT, lang)
    for fn in os.listdir(d):
        if not fn.endswith(".html"):
            continue
        path = os.path.join(d, fn)
        with open(path, encoding="utf-8") as f:
            content = f.read()
        for m in PATTERN.finditer(content):
            href = m.group(1)
            checked += 1
            if href.startswith(("http://", "https://", "mailto:")):
                continue
            file_part = href.split("#")[0]
            if not file_part:
                continue
            target = os.path.normpath(os.path.join(d, file_part))
            if os.path.isfile(target):
                real_dir = os.path.dirname(target)
                base = os.path.basename(target)
                real_name = None
                for f2 in os.listdir(real_dir):
                    if f2.lower() == base.lower():
                        real_name = f2
                        break
                if real_name and real_name != base:
                    issues.append(f'{lang}/{fn}: href="{href}" -> case mismatch, actual file is "{real_name}"')

print(f"Checked {checked} local paths across fr/nl/en")
print(f"Case mismatches found: {len(issues)}")
for i in issues[:40]:
    print(" -", i)
