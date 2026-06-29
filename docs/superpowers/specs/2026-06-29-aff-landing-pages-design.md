# Affiliate Landing Pages Integration Design

Date: 2026-06-29

## Goal

Integrate the three static affiliate landing page directories from:

`/Users/hongc/codebuddy/github/review-site/static/aff`

into the TestedHarbor static site as top-level brand directories.

## Source Directories

```text
/Users/hongc/codebuddy/github/review-site/static/aff/levoit
/Users/hongc/codebuddy/github/review-site/static/aff/seesii
/Users/hongc/codebuddy/github/review-site/static/aff/syokami
```

## Target Paths

Use top-level brand paths, not an `/aff/` prefix:

```text
/levoit/
/seesii/
/syokami/
```

Representative target URLs:

```text
/levoit/vital200s-air-purifier.html
/levoit/lvac-200.html
/levoit/levoit-de-store.html
/seesii/
/syokami/steak-knives-affiliate.html
```

## Integration Rules

- Copy the three directories into the site root.
- Keep the landing pages static.
- Do not introduce a framework.
- Do not add the pages to the TestedHarbor main navigation.
- Do not rewrite the landing page copy.
- Do not change affiliate links.
- Do not restyle the pages globally or force them into the TestedHarbor theme.
- Only change CSS needed to make default-state CTA text readable.

## CTA Readability Fix

Some landing pages have “Check price” / “Check Price” CTA buttons whose default state is not readable until hover.

Fix the default state only as much as needed:

- Ensure default button text has sufficient contrast against its background.
- Prefer CSS-only changes.
- Preserve hover behavior unless it conflicts with default readability.
- Do not alter button URLs or product copy.
- Scope changes to the imported landing page directories:
  - `/levoit/**`
  - `/seesii/**`
  - `/syokami/**`

## Verification Plan

After implementation:

1. Serve the site locally with `python3 -m http.server`.
2. Confirm these pages return HTTP 200:
   - `/levoit/vital200s-air-purifier.html`
   - `/levoit/lvac-200.html`
   - `/levoit/levoit-de-store.html`
   - `/seesii/`
   - `/syokami/steak-knives-affiliate.html`
3. Confirm local resources used by those pages do not 404.
4. Open representative pages in a browser and confirm CTA text is readable before hover.
5. Confirm existing TestedHarbor pages still return HTTP 200:
   - `/`
   - `/categories/home.html`
   - `/reviews/best-air-purifiers.html`
6. Do not deploy or publicly publish.

## Out of Scope

- No `/aff/` path.
- No new aggregation page.
- No main navigation changes.
- No production deployment.
