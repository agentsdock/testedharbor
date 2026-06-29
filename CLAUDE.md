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
