# Affiliate Landing Pages Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add the existing Levoit, Seesii, and Syokami affiliate landing page directories as top-level static paths and fix unreadable default CTA button states.

**Architecture:** Copy the three source directories from `/Users/hongc/codebuddy/github/review-site/static/aff` into the TestedHarbor root as independent static landing page directories. Keep the main TestedHarbor clone unchanged, scope CTA readability changes to the imported directories, and verify both new landing pages and representative existing pages locally.

**Tech Stack:** Static HTML/CSS/assets, Python 3 standard library for verification, shell file operations, git.

---

## File Structure

- Create: `/Users/hongc/codebuddy/github/testedharbor/levoit/**` — copied Levoit affiliate landing pages.
- Create: `/Users/hongc/codebuddy/github/testedharbor/seesii/**` — copied Seesii affiliate landing page and assets.
- Create: `/Users/hongc/codebuddy/github/testedharbor/syokami/**` — copied Syokami affiliate landing pages.
- Modify: imported HTML/CSS files under `/Users/hongc/codebuddy/github/testedharbor/levoit/**`, `/Users/hongc/codebuddy/github/testedharbor/seesii/**`, `/Users/hongc/codebuddy/github/testedharbor/syokami/**` only if needed for default-state CTA readability.
- Keep unchanged: existing TestedHarbor pages such as `/Users/hongc/codebuddy/github/testedharbor/index.html`, `/Users/hongc/codebuddy/github/testedharbor/categories/**`, `/Users/hongc/codebuddy/github/testedharbor/reviews/**`.

---

### Task 1: Copy Affiliate Directories

**Files:**
- Create: `/Users/hongc/codebuddy/github/testedharbor/levoit/**`
- Create: `/Users/hongc/codebuddy/github/testedharbor/seesii/**`
- Create: `/Users/hongc/codebuddy/github/testedharbor/syokami/**`

- [ ] **Step 1: Verify source directories exist**

Run:

```bash
\
for d in levoit seesii syokami; do
  test -d "/Users/hongc/codebuddy/github/review-site/static/aff/$d" && printf 'source_exists %s\n' "$d"
done
```

Expected output:

```text
source_exists levoit
source_exists seesii
source_exists syokami
```

- [ ] **Step 2: Copy directories into the site root**

Run:

```bash
cd /Users/hongc/codebuddy/github/testedharbor && \
python3 - <<'PY'
from pathlib import Path
import shutil

root = Path('/Users/hongc/codebuddy/github/testedharbor')
src_root = Path('/Users/hongc/codebuddy/github/review-site/static/aff')
for name in ['levoit', 'seesii', 'syokami']:
    src = src_root / name
    dst = root / name
    if dst.exists():
        raise SystemExit(f'target already exists: {dst}')
    shutil.copytree(src, dst)
    print(f'copied {src} -> {dst}')
PY
```

Expected output includes:

```text
copied /Users/hongc/codebuddy/github/review-site/static/aff/levoit -> /Users/hongc/codebuddy/github/testedharbor/levoit
copied /Users/hongc/codebuddy/github/review-site/static/aff/seesii -> /Users/hongc/codebuddy/github/testedharbor/seesii
copied /Users/hongc/codebuddy/github/review-site/static/aff/syokami -> /Users/hongc/codebuddy/github/testedharbor/syokami
```

- [ ] **Step 3: Verify key copied pages exist**

Run:

```bash
cd /Users/hongc/codebuddy/github/testedharbor && \
for p in \
  levoit/vital200s-air-purifier.html \
  levoit/lvac-200.html \
  levoit/levoit-de-store.html \
  seesii/index.html \
  syokami/steak-knives-affiliate.html; do
  test -f "$p" && printf 'page_exists %s\n' "$p"
done
```

Expected output:

```text
page_exists levoit/vital200s-air-purifier.html
page_exists levoit/lvac-200.html
page_exists levoit/levoit-de-store.html
page_exists seesii/index.html
page_exists syokami/steak-knives-affiliate.html
```

---

### Task 2: Fix CTA Default Readability

**Files:**
- Modify: `/Users/hongc/codebuddy/github/testedharbor/levoit/*.html`
- Modify: `/Users/hongc/codebuddy/github/testedharbor/seesii/*.html`
- Modify: `/Users/hongc/codebuddy/github/testedharbor/syokami/*.html`

- [ ] **Step 1: Locate CTA styles and text**

Run:

```bash
cd /Users/hongc/codebuddy/github/testedharbor && \
python3 - <<'PY'
from pathlib import Path
for base in ['levoit', 'seesii', 'syokami']:
    for path in sorted(Path(base).rglob('*.html')):
        text = path.read_text(encoding='utf-8', errors='ignore')
        lowered = text.lower()
        if 'check price' in lowered or 'check current price' in lowered or 'amazon' in lowered:
            print(path)
            for line_no, line in enumerate(text.splitlines(), 1):
                l = line.lower()
                if 'check price' in l or 'check current price' in l or 'btn' in l or 'cta' in l:
                    print(f'{line_no}: {line[:180]}')
            print('---')
PY
```

Expected: The command prints the relevant landing pages and CTA/style lines to inspect.

- [ ] **Step 2: Apply scoped CSS readability fixes**

Run this script to adjust only default CTA/button colors inside imported pages:

```bash
cd /Users/hongc/codebuddy/github/testedharbor && \
python3 - <<'PY'
from pathlib import Path

replacements = {
    'levoit': [
        ('.nav-cta {\n      background: var(--teal);\n      color: #fff;', '.nav-cta {\n      background: #007d6f;\n      color: #ffffff;'),
        ('.btn-primary {\n      background: var(--teal);\n      color: #fff;', '.btn-primary {\n      background: #007d6f;\n      color: #ffffff;'),
        ('.btn {\n      display: inline-block;', '.btn {\n      display: inline-block;'),
    ],
    'seesii': [
        ('background: var(--brand);\n      color: #fff;', 'background: #174724;\n      color: #ffffff;'),
        ('background: var(--accent);\n      color: #20231f;', 'background: #f0a800;\n      color: #111111;'),
    ],
    'syokami': [
        ('background: var(--gold);\n      color: #111;', 'background: #e8c96a;\n      color: #111111;'),
        ('background: var(--gold); color: #111;', 'background: #e8c96a; color: #111111;'),
    ],
}

changed = []
for directory, pairs in replacements.items():
    for path in sorted(Path(directory).rglob('*.html')):
        text = path.read_text(encoding='utf-8')
        new = text
        for old, repl in pairs:
            new = new.replace(old, repl)
        if new != text:
            path.write_text(new, encoding='utf-8')
            changed.append(path.as_posix())
for path in changed:
    print(path)
print(f'changed_files={len(changed)}')
if not changed:
    raise SystemExit('no CTA style files changed')
PY
```

Expected: `changed_files=` is greater than 0.

- [ ] **Step 3: Verify CTA text exists and obvious bad contrast patterns are absent**

Run:

```bash
cd /Users/hongc/codebuddy/github/testedharbor && \
python3 - <<'PY'
from pathlib import Path
cta_pages = []
bad_patterns = []
for base in ['levoit', 'seesii', 'syokami']:
    for path in sorted(Path(base).rglob('*.html')):
        text = path.read_text(encoding='utf-8', errors='ignore')
        lower = text.lower()
        if 'check price' in lower or 'check current price' in lower:
            cta_pages.append(path.as_posix())
        if 'color: transparent' in lower:
            bad_patterns.append((path.as_posix(), 'color transparent'))
        if 'background: #fff;\n      color: #fff' in lower or 'background: #ffffff;\n      color: #ffffff' in lower:
            bad_patterns.append((path.as_posix(), 'white on white'))
for p in cta_pages:
    print(f'cta_page {p}')
print(f'cta_pages={len(cta_pages)}')
print(f'bad_patterns={len(bad_patterns)}')
if bad_patterns:
    for p, reason in bad_patterns:
        print(f'{reason}: {p}')
    raise SystemExit(1)
if not cta_pages:
    raise SystemExit('no CTA pages found')
PY
```

Expected output includes `bad_patterns=0`.

---

### Task 3: Verify Local Routing and Existing Site

**Files:**
- Read-only verification of copied and existing static pages.

- [ ] **Step 1: Run HTTP verification for new and existing pages**

Run:

```bash
cd /Users/hongc/codebuddy/github/testedharbor && \
python3 - <<'PY'
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.request import urlopen
from urllib.parse import urlparse
from html.parser import HTMLParser
import os, socket, threading, time

root = Path('/Users/hongc/codebuddy/github/testedharbor')
os.chdir(root)

class Quiet(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass

sock = socket.socket()
sock.bind(('127.0.0.1', 0))
port = sock.getsockname()[1]
sock.close()
server = ThreadingHTTPServer(('127.0.0.1', port), Quiet)
thread = threading.Thread(target=server.serve_forever, daemon=True)
thread.start()
time.sleep(0.2)

paths = [
    '/levoit/vital200s-air-purifier.html',
    '/levoit/lvac-200.html',
    '/levoit/levoit-de-store.html',
    '/seesii/',
    '/syokami/steak-knives-affiliate.html',
    '/',
    '/categories/home.html',
    '/reviews/best-air-purifiers.html',
]

try:
    for path in paths:
        with urlopen(f'http://127.0.0.1:{port}{path}', timeout=5) as res:
            body = res.read(2000)
            print(f'{path} {res.status} {res.headers.get("content-type", "")}')
            if res.status != 200:
                raise SystemExit(1)
finally:
    server.shutdown()
    server.server_close()
PY
```

Expected: Every listed path prints status `200`.

- [ ] **Step 2: Verify local resources referenced by imported pages exist**

Run:

```bash
cd /Users/hongc/codebuddy/github/testedharbor && \
python3 - <<'PY'
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse

class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ('href', 'src'):
            if key in attrs:
                self.refs.append(attrs[key])
        if 'srcset' in attrs:
            self.refs.extend(part.strip().split(' ')[0] for part in attrs['srcset'].split(','))

missing = []
checked = 0
for base in ['levoit', 'seesii', 'syokami']:
    for path in sorted(Path(base).rglob('*.html')):
        parser = Parser()
        parser.feed(path.read_text(encoding='utf-8', errors='ignore'))
        for ref in parser.refs:
            if not ref or ref.startswith(('#', 'mailto:', 'tel:', 'javascript:')):
                continue
            parsed = urlparse(ref)
            if parsed.scheme or parsed.netloc:
                continue
            if not parsed.path:
                continue
            checked += 1
            target = Path(parsed.path.lstrip('/')) if parsed.path.startswith('/') else path.parent / parsed.path
            if parsed.path.endswith('/'):
                target = target / 'index.html'
            if not target.exists():
                missing.append(f'{path} -> {ref} -> {target}')
print(f'imported_local_refs_checked={checked}')
print(f'imported_missing_local_refs={len(missing)}')
if missing:
    print('\n'.join(missing[:50]))
    raise SystemExit(1)
PY
```

Expected output:

```text
imported_missing_local_refs=0
```

- [ ] **Step 3: Verify main site brand checks still pass**

Run:

```bash
cd /Users/hongc/codebuddy/github/testedharbor && \
python3 - <<'PY'
from pathlib import Path
suffixes={'.html','.htm','.css','.js','.json','.xml','.txt','.svg','.webmanifest'}
terms=['LabTestedPicks','LabTested','labtestedpicks.com','images.unsplash.com','rss.xml.html']
hits={t:[] for t in terms}
for p in sorted(Path('.').rglob('*')):
    if not p.is_file() or p.suffix.lower() not in suffixes:
        continue
    rel=p.as_posix()
    if rel.startswith('docs/') or rel == 'CLAUDE.md':
        continue
    text=p.read_text(encoding='utf-8', errors='ignore')
    for t in terms:
        if t in text:
            hits[t].append(rel)
for t, paths in hits.items():
    print(f'hits_{t}={len(paths)}')
    if paths:
        print('\n'.join(paths[:20]))
        raise SystemExit(1)
print('brand_checks_pass')
PY
```

Expected output includes:

```text
brand_checks_pass
```

---

### Task 4: Commit Affiliate Landing Pages

**Files:**
- Commit all files created or modified by Tasks 1-3.

- [ ] **Step 1: Review git status**

Run:

```bash
cd /Users/hongc/codebuddy/github/testedharbor && git status --short
```

Expected: new `levoit/`, `seesii/`, `syokami/`, and the plan file appear. No unrelated modified files appear.

- [ ] **Step 2: Commit changes**

Run:

```bash
cd /Users/hongc/codebuddy/github/testedharbor && \
git add docs/superpowers/plans/2026-06-29-aff-landing-pages.md levoit seesii syokami && \
git commit -m "feat: add affiliate landing pages"
```

Expected: commit succeeds.

- [ ] **Step 3: Verify clean status**

Run:

```bash
cd /Users/hongc/codebuddy/github/testedharbor && git status --short --branch
```

Expected output:

```text
## master
```

---

## Self-Review Notes

- Spec coverage: The plan copies the three selected source directories to top-level paths, avoids `/aff/`, scopes CTA readability fixes to imported pages, verifies new routes and existing pages, and avoids deployment.
- Placeholder scan: No forbidden placeholder markers or vague implementation steps remain.
- Consistency: All commands use `/Users/hongc/codebuddy/github/testedharbor` as target and `/Users/hongc/codebuddy/github/review-site/static/aff` as source.
