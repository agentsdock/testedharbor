# TestedHarbor Clone Design

Date: 2026-06-29

## Goal

Create a full static clone of `https://lp-449e12fe-ff76-44c6-904d-ee768af77a2f.pages.dev/` in this directory.

The only intentional content change is:

```text
LabTestedPicks -> TestedHarbor
```

Everything else should remain as close to the source site as possible: page structure, copy, layout, styles, images, links, metadata, and file paths.

## Scope

Clone all same-origin, publicly reachable pages and static resources from the source site, including but not limited to:

- `index.html`
- `categories/*`
- `reviews/*`
- `about/`
- `contact/`
- `privacy/`
- `disclaimer/`
- `sitemap.xml`
- CSS, JavaScript, images, icons, fonts, and other page resources

Do not clone external websites. External links should remain links unless they are page assets required to render the source site.

## Approach

Use a static mirror approach rather than rebuilding the site in a framework.

1. Discover same-origin URLs from the homepage, sitemap, and crawled internal links.
2. Download each reachable HTML page and referenced static asset.
3. Preserve the original directory structure and relative link behavior.
4. Replace all occurrences of `LabTestedPicks` with `TestedHarbor` across downloaded text files.
5. Serve the result locally as static files for verification.

This approach minimizes interpretation and reduces the chance of changing behavior, layout, or content beyond the requested brand replacement.

## Project Rules

Before implementation, create a project `CLAUDE.md` that records these constraints:

- Static clone only; do not introduce a framework unless explicitly requested.
- Only intentional brand change is `LabTestedPicks` to `TestedHarbor`.
- Preserve source structure and content.
- No deployment or public publishing without explicit approval.
- Run local verification after changes.

## File Structure

Expected output structure:

```text
/
├── CLAUDE.md
├── index.html
├── categories/
├── reviews/
├── about/
├── contact/
├── privacy/
├── disclaimer/
├── assets/ or source-equivalent asset directories
├── sitemap.xml
└── docs/superpowers/specs/
```

The exact asset directory names should follow the source site where practical.

## Brand Replacement Rules

Replace `LabTestedPicks` with `TestedHarbor` in:

- Visible page text
- Header and footer logo text
- HTML `<title>` values
- Meta tags and Open Graph/Twitter metadata
- Structured data JSON-LD
- Copyright text
- Sitemap or XML content if present

Do not change:

- Article titles, product names, category names, or review copy
- Layout, colors, spacing, or CSS classes
- Navigation structure
- Internal URL paths, except where needed to make the static local mirror work
- External affiliate or source links

## Verification Plan

After implementation, verify with these checks:

1. Start a local static server from the project root.
2. Open the local homepage in a browser.
3. Confirm homepage renders with the `TestedHarbor` brand.
4. Click representative navigation links for categories, reviews, company pages, and sitemap.
5. Check browser network output for obvious missing local resources.
6. Search text files to confirm no `LabTestedPicks` remains.
7. Confirm the source domain is not required for core page rendering.

## Out of Scope

- No redesign.
- No copywriting changes.
- No SEO optimization beyond preserving source metadata with brand replacement.
- No new tracking scripts.
- No production deployment.
- No git commit, because the current directory is not a git repository.
