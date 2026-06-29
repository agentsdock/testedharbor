# Main Site README and CTA Optimization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add an SEO-oriented README for TestedHarbor and fix default-state CTA/button readability on the original main-site pages only.

**Architecture:** Keep this as a static-site content and CSS update. Add `README.md` at the repository root, then inspect and adjust shared main-site CSS or original main-site HTML only; explicitly verify no files under `levoit/`, `seesii/`, or `syokami/` changed.

**Tech Stack:** Static HTML/CSS/JS, Markdown, Python 3 standard library for verification, Playwright/browser checks if available, git.

---

## File Structure

- Create: `/Users/hongc/codebuddy/github/testedharbor/README.md` — public GitHub README describing and promoting `https://testedharbor.com`.
- Modify if needed: `/Users/hongc/codebuddy/github/testedharbor/css/style.css` — preferred place for shared main-site CTA color fixes.
- Modify only if CSS alone is insufficient: original main-site HTML under `/Users/hongc/codebuddy/github/testedharbor/index.html`, `categories/**`, `reviews/**`, `about/**`, `contact/**`, `privacy/**`, `disclaimer/**`.
- Do not modify: `/Users/hongc/codebuddy/github/testedharbor/levoit/**`, `/Users/hongc/codebuddy/github/testedharbor/seesii/**`, `/Users/hongc/codebuddy/github/testedharbor/syokami/**`.

---

### Task 1: Add SEO-Oriented README

**Files:**
- Create: `/Users/hongc/codebuddy/github/testedharbor/README.md`

- [ ] **Step 1: Create README.md**

Create an English README that explains TestedHarbor as an independent product review and buying guide site. It must include `https://testedharbor.com`, main category links, featured review links, affiliate landing page links, review philosophy, important pages, technical notes, and affiliate disclosure.

- [ ] **Step 2: Verify README content**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
p = Path('README.md')
s = p.read_text(encoding='utf-8')
checks = {
    'exists': p.exists(),
    'has_domain': 'https://testedharbor.com' in s,
    'has_categories': 'Main Buying Guide Categories' in s,
    'has_reviews': 'Featured Product Reviews' in s,
    'has_disclosure': 'affiliate commissions' in s,
}
for k, v in checks.items():
    print(f'{k}: {v}')
if not all(checks.values()):
    raise SystemExit(1)
PY
```

Expected output:

```text
exists: True
has_domain: True
has_categories: True
has_reviews: True
has_disclosure: True
```

---

### Task 2: Inspect and Fix Main-Site CTA Readability

**Files:**
- Modify if needed: `/Users/hongc/codebuddy/github/testedharbor/css/style.css`
- Do not modify: `/Users/hongc/codebuddy/github/testedharbor/levoit/**`
- Do not modify: `/Users/hongc/codebuddy/github/testedharbor/seesii/**`
- Do not modify: `/Users/hongc/codebuddy/github/testedharbor/syokami/**`

- [ ] **Step 1: Capture affiliate directory baseline**

Run:

```bash
git diff --quiet -- levoit seesii syokami && printf 'affiliate_dirs_clean_before\n'
```

Expected output:

```text
affiliate_dirs_clean_before
```

- [ ] **Step 2: Apply high-contrast default button colors in shared CSS**

Append a scoped CSS override block to `css/style.css` if not already present:

```css
/* Main-site CTA readability overrides */
.btn,
.button,
.cta,
.cta-button,
.card-cta,
.hero-cta,
.newsletter button,
button[type="submit"] {
  color: #ffffff;
  background: #0f766e;
  border-color: #0f766e;
}

.btn:hover,
.button:hover,
.cta:hover,
.cta-button:hover,
.card-cta:hover,
.hero-cta:hover,
.newsletter button:hover,
button[type="submit"]:hover {
  color: #ffffff;
  background: #115e59;
  border-color: #115e59;
}
```

- [ ] **Step 3: Verify affiliate directories remain unchanged**

Run:

```bash
git diff --quiet -- levoit seesii syokami && printf 'affiliate_dirs_unchanged\n'
```

Expected output:

```text
affiliate_dirs_unchanged
```

---

### Task 3: Verify Main Site and CTA Styles

**Files:**
- Read-only verification of `README.md`, `css/style.css`, and representative main-site pages.

- [ ] **Step 1: Verify local HTTP routes**

Run a local Python HTTP server from the repo root and confirm these routes return HTTP 200:

```text
/
/categories/home.html
/categories/kitchen.html
/categories/tech.html
/categories/office/index.html
/categories/deals/index.html
/reviews/best-air-purifiers.html
/reviews/best-office-chairs.html
/about/index.html
/contact/index.html
```

- [ ] **Step 2: Verify CTA computed styles with browser if available**

Use browser automation to inspect visible buttons/CTA links on `/` and at least one review page. Expected: CTA/button elements have readable default foreground/background pairs, such as white text on teal background.

- [ ] **Step 3: Verify brand residue checks still pass**

Run a text scan over site files excluding `docs/` and `CLAUDE.md`. Expected: no `LabTestedPicks`, `LabTested`, `labtestedpicks.com`, or `rss.xml.html` hits.

---

### Task 4: Commit and Push

**Files:**
- Commit: `/Users/hongc/codebuddy/github/testedharbor/README.md`
- Commit if changed: `/Users/hongc/codebuddy/github/testedharbor/css/style.css`
- Commit: `/Users/hongc/codebuddy/github/testedharbor/docs/superpowers/plans/2026-06-29-main-site-readme-cta.md`

- [ ] **Step 1: Review changed files**

Run:

```bash
git status --short
```

Expected: only `README.md`, `css/style.css` if needed, and the plan file are changed or untracked. No `levoit/`, `seesii/`, or `syokami/` changes appear.

- [ ] **Step 2: Commit changes**

Run:

```bash
git add README.md docs/superpowers/plans/2026-06-29-main-site-readme-cta.md css/style.css
git commit -m "docs: add README and improve main site CTA contrast"
```

Expected: commit succeeds.

- [ ] **Step 3: Push to GitHub**

Run:

```bash
git -c http.proxy= -c https.proxy= -c http.version=HTTP/1.1 -c http.postBuffer=157286400 push origin master:main
```

Expected: push succeeds to `https://github.com/agentsdock/testedharbor`.

- [ ] **Step 4: Verify clean status**

Run:

```bash
git status --short --branch
```

Expected output:

```text
## master...origin/main
```

---

## Self-Review Notes

- Spec coverage: The plan adds README, scopes CTA color fixes to original main-site files, explicitly excludes affiliate directories, verifies local pages and brand residue, commits, and pushes.
- Placeholder scan: No forbidden placeholder markers or vague implementation steps remain.
- Consistency: All paths use `/Users/hongc/codebuddy/github/testedharbor`; affiliate directories are excluded from changes.
