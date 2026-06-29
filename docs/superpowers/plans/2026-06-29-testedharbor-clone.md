# TestedHarbor Clone Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a full static clone of the source site with every `LabTestedPicks` occurrence changed to `TestedHarbor` and no other intentional content, style, or structure changes.

**Architecture:** Use a static mirroring workflow: create project rules, crawl/download all same-origin public pages and assets, then perform a single brand-name replacement across downloaded text files. Keep the source site's directory structure and serve it locally for browser verification.

**Tech Stack:** Static HTML/CSS/JS/assets, Python 3 standard library for local server and verification scripts, shell utilities available on macOS. No frontend framework.

---

## File Structure

- Create: `CLAUDE.md` — project-specific rules for this static clone.
- Create/Modify: `index.html` — mirrored homepage with brand replacement.
- Create/Modify: `categories/**` — mirrored category pages and nested indexes.
- Create/Modify: `reviews/**` — mirrored review pages.
- Create/Modify: `about/**`, `contact/**`, `privacy/**`, `disclaimer/**` — mirrored company/legal pages.
- Create/Modify: `sitemap.xml` — mirrored sitemap if available.
- Create/Modify: source-equivalent asset paths such as `assets/**`, image paths, CSS paths, JS paths, font paths — downloaded assets required for local rendering.
- Keep: `docs/superpowers/specs/2026-06-29-testedharbor-clone-design.md` — approved design.
- Keep: `docs/superpowers/plans/2026-06-29-testedharbor-clone.md` — this implementation plan.

The exact mirrored paths are determined by the source site. Do not rename source paths unless required to make local relative links work.

---

### Task 1: Add Project Rules

**Files:**
- Create: `CLAUDE.md`

- [ ] **Step 1: Create project `CLAUDE.md`**

Write this exact file at `/Users/hongc/codebuddy/github/testedharbor/CLAUDE.md`:

```markdown
# TestedHarbor Project Rules

## Project Type

This project is a static mirror of:

`https://lp-449e12fe-ff76-44c6-904d-ee768af77a2f.pages.dev/`

## Primary Constraint

The only intentional content change is:

```text
LabTestedPicks -> TestedHarbor
```

Do not rewrite copy, redesign layouts, rename categories, change article titles, or introduce new functionality.

## Implementation Rules

- Keep the site static: HTML, CSS, JavaScript, images, fonts, and other assets.
- Do not introduce Next.js, Vite, Astro, React, Vue, or another framework unless the user explicitly asks.
- Preserve the source site's directory structure and relative links where practical.
- Clone all same-origin, publicly reachable pages and required static assets.
- Do not clone external websites.
- External links should remain external links unless they are static assets required to render the site.
- Do not deploy or publicly publish without explicit user approval.

## Verification Rules

After changes, run local verification:

1. Serve the project with `python3 -m http.server` from the project root.
2. Open the local site in a browser.
3. Check representative pages from homepage navigation, review pages, category pages, legal/company pages, and sitemap.
4. Confirm no `LabTestedPicks` string remains in text files.
5. Check browser console/network output for obvious missing local resources.
```

- [ ] **Step 2: Verify the rules file exists**

Run:

```bash
test -f /Users/hongc/codebuddy/github/testedharbor/CLAUDE.md && printf 'CLAUDE.md exists\n'
```

Expected output:

```text
CLAUDE.md exists
```

---

### Task 2: Mirror Source Site

**Files:**
- Create/Modify: `index.html`
- Create/Modify: `categories/**`
- Create/Modify: `reviews/**`
- Create/Modify: `about/**`
- Create/Modify: `contact/**`
- Create/Modify: `privacy/**`
- Create/Modify: `disclaimer/**`
- Create/Modify: `sitemap.xml`
- Create/Modify: all required source-equivalent static asset files

- [ ] **Step 1: Run a same-origin static mirror command**

From `/Users/hongc/codebuddy/github/testedharbor`, run:

```bash
cd /Users/hongc/codebuddy/github/testedharbor && \
wget \
  --mirror \
  --page-requisites \
  --convert-links \
  --adjust-extension \
  --no-parent \
  --span-hosts \
  --domains lp-449e12fe-ff76-44c6-904d-ee768af77a2f.pages.dev \
  --reject-regex='^(?!https://lp-449e12fe-ff76-44c6-904d-ee768af77a2f\.pages\.dev/)' \
  https://lp-449e12fe-ff76-44c6-904d-ee768af77a2f.pages.dev/
```

Expected: `wget` downloads HTML pages and page requisites into a directory named `lp-449e12fe-ff76-44c6-904d-ee768af77a2f.pages.dev/`.

If `wget` is not installed, install nothing globally. Use this Python fallback instead:

```bash
cd /Users/hongc/codebuddy/github/testedharbor && \
python3 - <<'PY'
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse, urldefrag
from urllib.request import Request, urlopen

ROOT = 'https://lp-449e12fe-ff76-44c6-904d-ee768af77a2f.pages.dev/'
HOST = urlparse(ROOT).netloc
OUT = Path('lp-449e12fe-ff76-44c6-904d-ee768af77a2f.pages.dev')
TEXT_EXTS = {'.html', '.htm', '.css', '.js', '.xml', '.txt', '.json', '.svg'}

class LinkParser(HTMLParser):
    def __init__(self, base):
        super().__init__()
        self.base = base
        self.links = set()
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ('href', 'src'):
            if key in attrs:
                self.add(attrs[key])
        if 'srcset' in attrs:
            for part in attrs['srcset'].split(','):
                self.add(part.strip().split(' ')[0])
    def add(self, value):
        if not value or value.startswith(('mailto:', 'tel:', 'javascript:', '#')):
            return
        url, _ = urldefrag(urljoin(self.base, value))
        if urlparse(url).netloc == HOST:
            self.links.add(url)

def out_path(url, content_type=''):
    parsed = urlparse(url)
    path = parsed.path
    if path.endswith('/') or not Path(path).suffix:
        path = path.rstrip('/') + '/index.html'
    return OUT / path.lstrip('/')

def fetch(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0 static mirror'})
    with urlopen(req, timeout=30) as res:
        return res.read(), res.headers.get('content-type', '')

queue = [ROOT, urljoin(ROOT, 'sitemap.xml')]
seen = set()
while queue:
    url = queue.pop(0)
    if url in seen:
        continue
    seen.add(url)
    try:
        body, ctype = fetch(url)
    except Exception as exc:
        print(f'SKIP {url}: {exc}')
        continue
    path = out_path(url, ctype)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(body)
    print(f'WROTE {path}')
    lower = path.suffix.lower()
    if 'text/html' in ctype or lower in {'.html', '.htm'}:
        try:
            text = body.decode('utf-8', errors='ignore')
        except Exception:
            continue
        parser = LinkParser(url)
        parser.feed(text)
        for link in sorted(parser.links):
            if link not in seen and link not in queue:
                queue.append(link)
    elif lower == '.xml':
        text = body.decode('utf-8', errors='ignore')
        for chunk in text.split('<loc>')[1:]:
            link = chunk.split('</loc>', 1)[0].strip()
            if urlparse(link).netloc == HOST and link not in seen and link not in queue:
                queue.append(link)
PY
```

Expected: The fallback prints `WROTE ...` lines for downloaded pages/assets.

- [ ] **Step 2: Move mirrored files to project root**

After the mirror exists, run:

```bash
cd /Users/hongc/codebuddy/github/testedharbor && \
python3 - <<'PY'
from pathlib import Path
import shutil

src = Path('lp-449e12fe-ff76-44c6-904d-ee768af77a2f.pages.dev')
if not src.is_dir():
    raise SystemExit('mirror directory missing')
for child in src.iterdir():
    dest = Path(child.name)
    if dest.exists():
        if dest.is_dir() and child.is_dir():
            for nested in child.rglob('*'):
                rel = nested.relative_to(child)
                target = dest / rel
                if nested.is_dir():
                    target.mkdir(parents=True, exist_ok=True)
                else:
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(nested, target)
        else:
            if dest.is_dir():
                shutil.rmtree(dest)
            else:
                dest.unlink()
            shutil.move(str(child), str(dest))
    else:
        shutil.move(str(child), str(dest))
shutil.rmtree(src)
print('mirror moved to project root')
PY
```

Expected output:

```text
mirror moved to project root
```

- [ ] **Step 3: Verify expected top-level files exist**

Run:

```bash
cd /Users/hongc/codebuddy/github/testedharbor && \
python3 - <<'PY'
from pathlib import Path
expected_any = [
    Path('index.html'),
    Path('categories'),
    Path('reviews'),
    Path('about'),
    Path('contact'),
    Path('privacy'),
    Path('disclaimer'),
    Path('sitemap.xml'),
]
for path in expected_any:
    print(f'{path}: {path.exists()}')
missing_core = [str(p) for p in [Path('index.html')] if not p.exists()]
if missing_core:
    raise SystemExit('missing core files: ' + ', '.join(missing_core))
PY
```

Expected: `index.html: True`. Other paths should be `True` if present on the source site.

---

### Task 3: Replace Brand Name Only

**Files:**
- Modify: downloaded text files under project root
- Do not modify: binary image/font/archive files

- [ ] **Step 1: Replace `LabTestedPicks` in text files**

Run:

```bash
cd /Users/hongc/codebuddy/github/testedharbor && \
python3 - <<'PY'
from pathlib import Path

SKIP_DIRS = {'.git', 'docs/superpowers/plans', 'docs/superpowers/specs'}
TEXT_SUFFIXES = {'.html', '.htm', '.css', '.js', '.json', '.xml', '.txt', '.svg', '.webmanifest'}
changed = []
for path in Path('.').rglob('*'):
    if not path.is_file():
        continue
    parts = set(path.parts)
    if '.git' in parts:
        continue
    rel = path.as_posix()
    if rel.startswith('docs/superpowers/plans/') or rel.startswith('docs/superpowers/specs/'):
        continue
    if path.suffix.lower() not in TEXT_SUFFIXES:
        continue
    data = path.read_bytes()
    try:
        text = data.decode('utf-8')
    except UnicodeDecodeError:
        continue
    new = text.replace('LabTestedPicks', 'TestedHarbor')
    if new != text:
        path.write_text(new, encoding='utf-8')
        changed.append(rel)
for rel in changed:
    print(rel)
print(f'changed_files={len(changed)}')
PY
```

Expected: The command prints changed file paths and `changed_files=` with a number greater than zero.

- [ ] **Step 2: Verify no source brand remains outside docs**

Run:

```bash
cd /Users/hongc/codebuddy/github/testedharbor && \
python3 - <<'PY'
from pathlib import Path
TEXT_SUFFIXES = {'.html', '.htm', '.css', '.js', '.json', '.xml', '.txt', '.svg', '.webmanifest'}
hits = []
for path in Path('.').rglob('*'):
    if not path.is_file():
        continue
    rel = path.as_posix()
    if rel.startswith('docs/superpowers/') or '.git/' in rel:
        continue
    if path.suffix.lower() not in TEXT_SUFFIXES:
        continue
    try:
        text = path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        continue
    if 'LabTestedPicks' in text:
        hits.append(rel)
if hits:
    print('\n'.join(hits))
    raise SystemExit('LabTestedPicks remains')
print('No LabTestedPicks remains outside docs')
PY
```

Expected output:

```text
No LabTestedPicks remains outside docs
```

- [ ] **Step 3: Verify replacement appears in homepage**

Run:

```bash
cd /Users/hongc/codebuddy/github/testedharbor && \
python3 - <<'PY'
from pathlib import Path
text = Path('index.html').read_text(encoding='utf-8', errors='ignore')
if 'TestedHarbor' not in text:
    raise SystemExit('TestedHarbor missing from index.html')
print('TestedHarbor present in index.html')
PY
```

Expected output:

```text
TestedHarbor present in index.html
```

---

### Task 4: Verify Local Static Site

**Files:**
- Read-only verification of generated static files

- [ ] **Step 1: Start local server**

Run from `/Users/hongc/codebuddy/github/testedharbor`:

```bash
cd /Users/hongc/codebuddy/github/testedharbor && python3 -m http.server 4173
```

Expected output includes:

```text
Serving HTTP on :: port 4173
```

Leave this server running while performing browser checks.

- [ ] **Step 2: Open homepage in browser**

Navigate to:

```text
http://localhost:4173/
```

Expected browser title contains:

```text
TestedHarbor
```

Expected page header/footer brand text:

```text
TestedHarbor
```

- [ ] **Step 3: Check representative internal pages**

Open these URLs if the corresponding files exist:

```text
http://localhost:4173/categories/home.html
http://localhost:4173/categories/kitchen.html
http://localhost:4173/categories/tech.html
http://localhost:4173/categories/office/index.html
http://localhost:4173/categories/deals/index.html
http://localhost:4173/reviews/best-air-purifiers.html
http://localhost:4173/reviews/best-office-chairs.html
http://localhost:4173/about/index.html
http://localhost:4173/contact/index.html
http://localhost:4173/privacy/index.html
http://localhost:4173/disclaimer/index.html
http://localhost:4173/sitemap.xml
```

Expected: Existing pages return HTTP 200 and render or display XML. Missing URLs should be investigated against the mirrored file tree before deciding whether they are unavailable on the source site.

- [ ] **Step 4: Check browser console and network**

Using browser developer tools, inspect the homepage and at least one review page.

Expected:

- No obvious missing CSS or image assets that break the page layout.
- No core page rendering dependency on `https://lp-449e12fe-ff76-44c6-904d-ee768af77a2f.pages.dev/`.
- Any remaining external URLs are normal outbound links or third-party resources, not required internal pages.

- [ ] **Step 5: Stop local server**

Stop the `python3 -m http.server 4173` process with `Ctrl+C` in its terminal.

Expected output includes server shutdown or the terminal returns to the prompt.

---

### Task 5: Final Requirements Checklist

**Files:**
- Read-only verification of all project files

- [ ] **Step 1: Confirm project rule file exists**

Run:

```bash
cd /Users/hongc/codebuddy/github/testedharbor && test -f CLAUDE.md && printf 'CLAUDE.md exists\n'
```

Expected output:

```text
CLAUDE.md exists
```

- [ ] **Step 2: Confirm homepage exists**

Run:

```bash
cd /Users/hongc/codebuddy/github/testedharbor && test -f index.html && printf 'index.html exists\n'
```

Expected output:

```text
index.html exists
```

- [ ] **Step 3: Confirm no source brand remains outside docs**

Run:

```bash
cd /Users/hongc/codebuddy/github/testedharbor && \
python3 - <<'PY'
from pathlib import Path
TEXT_SUFFIXES = {'.html', '.htm', '.css', '.js', '.json', '.xml', '.txt', '.svg', '.webmanifest'}
hits = []
for path in Path('.').rglob('*'):
    if not path.is_file():
        continue
    rel = path.as_posix()
    if rel.startswith('docs/superpowers/') or '.git/' in rel:
        continue
    if path.suffix.lower() not in TEXT_SUFFIXES:
        continue
    try:
        text = path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        continue
    if 'LabTestedPicks' in text:
        hits.append(rel)
if hits:
    print('\n'.join(hits))
    raise SystemExit('LabTestedPicks remains')
print('No LabTestedPicks remains outside docs')
PY
```

Expected output:

```text
No LabTestedPicks remains outside docs
```

- [ ] **Step 4: Confirm no deployment happened**

Run:

```bash
cd /Users/hongc/codebuddy/github/testedharbor && printf 'No deployment command is part of this plan.\n'
```

Expected output:

```text
No deployment command is part of this plan.
```

- [ ] **Step 5: Record final status honestly**

Report exactly:

- Whether the mirror command completed.
- Which representative pages were checked locally.
- Whether `LabTestedPicks` remains outside docs.
- Whether any local resource errors remain.
- That no deployment/public publishing was performed.

Do not claim completion unless the verification commands and browser checks have been run in the current implementation session.

---

## Self-Review Notes

- Spec coverage: The plan covers project rules, full same-origin static mirroring, brand-only replacement, local serving, representative navigation checks, source-brand search, and no deployment.
- Placeholder scan: No forbidden placeholder markers or unspecified implementation steps are present.
- Consistency: Paths, commands, and verification scripts consistently use `/Users/hongc/codebuddy/github/testedharbor` and the approved source URL.
- Git note: The current directory is not a git repository, so this plan does not include commit steps.
