# README and Affiliate CTA Optimization Design

Date: 2026-06-29

## Goal

First implement the focused optimization package:

1. Add an SEO-oriented GitHub `README.md` that promotes `https://testedharbor.com` and explains the site entity clearly.
2. Fix unreadable default-state affiliate CTA buttons in the imported landing pages.

Broader site SEO work such as homepage/schema/content restructuring is intentionally deferred until after this package is complete.

## Scope

### In Scope

- Create `README.md` in English.
- Include the canonical domain: `https://testedharbor.com`.
- Link to key category, review, and affiliate landing pages.
- Explain TestedHarbor as an independent product review and buying guide site.
- Include affiliate disclosure.
- Mention Cloudflare Pages/static-site implementation only as supporting context.
- Update CTA button colors in:
  - `levoit/**/*.html`
  - `seesii/**/*.html`
  - `syokami/**/*.html`
- Ensure CTA text is readable before hover.
- Commit and push to GitHub after verification.

### Out of Scope

- No main site redesign.
- No navigation changes.
- No affiliate URL changes.
- No rewrite of landing page product copy.
- No schema implementation in this step.
- No `llms.txt` or sitewide SEO architecture work in this step.

## README Strategy

The README should work as a public entity description for GitHub, search engines, and AI systems.

It should cover:

- What TestedHarbor is.
- What categories it covers.
- Featured product review pages.
- Affiliate landing pages.
- Review philosophy.
- Important legal/contact pages.
- The canonical domain and GitHub repository.
- Affiliate disclosure.

The README should be concise, link-rich, and written for humans first while remaining extractable by AI systems.

## CTA Color Strategy

The current issue is that some “Check price” / Amazon CTA buttons can be hard to read in the default state because foreground and background colors are too similar or because the readable style only appears on hover.

Fix rules:

- Scope CSS changes only to imported affiliate directories.
- Make default CTA states high-contrast.
- Preserve existing visual identity per brand where possible:
  - Levoit: teal/orange CTAs with white text.
  - Seesii: green or amber CTAs with high-contrast text.
  - Syokami: gold CTAs with dark text.
- Do not alter CTA URLs.
- Do not alter product claims or page copy.
- Keep hover styles secondary; default state must already be readable.

## Verification Plan

After implementation:

1. Confirm `README.md` exists and includes `https://testedharbor.com`.
2. Serve the site locally and confirm these pages return HTTP 200:
   - `/`
   - `/levoit/vital200s-air-purifier.html`
   - `/levoit/lvac-200.html`
   - `/levoit/levoit-de-store.html`
   - `/seesii/`
   - `/syokami/steak-knives-affiliate.html`
3. Check imported page local resources for missing references.
4. Use browser/computed style checks on representative CTA buttons to confirm foreground and background are not the same and default state is readable.
5. Confirm no affiliate links were changed unexpectedly.
6. Commit changes.
7. Push to GitHub `origin/main` using the existing HTTPS token credential path.

## Follow-Up Work

After this is complete, handle broader SEO work separately, including possible schema markup, `llms.txt`, improved robots/sitemap strategy, and page-level SEO improvements.
