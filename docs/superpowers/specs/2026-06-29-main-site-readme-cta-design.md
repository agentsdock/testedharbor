# Main Site README and CTA Optimization Design

Date: 2026-06-29

## Goal

Optimize the public GitHub README for `https://testedharbor.com` and fix CTA/button default-state readability only on the original TestedHarbor main site pages.

## Scope

### In Scope

- Create or update `README.md` in English.
- Use the README to explain and promote `https://testedharbor.com` as an independent product review and buying guide site.
- Link to core main-site category and review pages.
- Include affiliate disclosure and static-site/Cloudflare Pages context.
- Fix CTA/button default-state color readability in original main-site pages only:
  - `index.html`
  - `categories/**`
  - `reviews/**`
  - `about/**`
  - `contact/**`
  - `privacy/**`
  - `disclaimer/**`
  - shared main-site assets such as `css/style.css` and `js/main.js` if needed.

### Out of Scope

- Do not modify affiliate landing page directories:
  - `levoit/**`
  - `seesii/**`
  - `syokami/**`
- Do not rewrite review/article copy.
- Do not change affiliate URLs.
- Do not change main navigation structure.
- Do not add schema, `llms.txt`, or broader SEO architecture in this step.
- Do not deploy manually; pushing to GitHub may trigger the already-configured Cloudflare Pages pipeline.

## README Strategy

The README should function as a concise public entity description for GitHub, search engines, and AI systems.

It should include:

- Site name and canonical URL: `https://testedharbor.com`.
- A one-paragraph explanation of TestedHarbor.
- Core category links.
- Featured review links.
- A short review philosophy.
- Important pages such as About, Contact, Privacy, Disclaimer, and Sitemap.
- Affiliate disclosure.
- Repository and static hosting context.

The README should not be a developer-heavy implementation note. It should primarily describe the website and its public value.

## Main-Site CTA Readability Strategy

The requested color fix applies only to original TestedHarbor pages, not the imported affiliate landing pages.

Fix rules:

- Inspect existing main-site CTA/button/link styles.
- Prefer changing shared `css/style.css` rather than editing every HTML page.
- Ensure default-state CTA text is readable without hover.
- Use high-contrast colors consistent with the TestedHarbor theme.
- Preserve hover behavior where it already works.
- Do not alter text content, URLs, layout, or page structure unless required for button readability.

## Verification Plan

After implementation:

1. Confirm `README.md` exists and contains `https://testedharbor.com`.
2. Confirm no files under `levoit/`, `seesii/`, or `syokami/` changed.
3. Serve the site locally and confirm representative original main-site pages return HTTP 200:
   - `/`
   - `/categories/home.html`
   - `/categories/kitchen.html`
   - `/categories/tech.html`
   - `/categories/office/index.html`
   - `/categories/deals/index.html`
   - `/reviews/best-air-purifiers.html`
   - `/reviews/best-office-chairs.html`
   - `/about/index.html`
   - `/contact/index.html`
4. Use browser/computed-style checks on representative main-site CTA/button elements to confirm foreground and background colors are not effectively identical in default state.
5. Confirm original brand checks still pass:
   - No `LabTestedPicks` in actual site files outside docs/CLAUDE.
   - No `labtestedpicks.com` in actual site files outside docs/CLAUDE.
6. Commit changes and push to GitHub `origin/main` after verification.

## Follow-Up Work

After this step, broader SEO improvements can be handled separately, including schema markup, `llms.txt`, sitemap/robots improvements, and page-level SEO enhancements.
