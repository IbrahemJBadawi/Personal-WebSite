# Personal Portfolio — TechMood Design Brief

Updated: 2026-11-24

## Purpose
A professional, Arabic-first (RTL) portfolio for a Management Information Systems specialist and the founder of TechMood Technology. It should communicate the person's professional profile and role in digital products through accurate evidence, selected work, clear design decisions, and accessible navigation. It is not an agency sales landing page.

## Sources reviewed (design inspiration, not implementation dependencies)
- Figma, *Portfolio Website Examples*: https://www.figma.com/resource-library/portfolio-website-examples/
  - Useful principle: explain individual role, context, process, and outcomes; keep contact obvious.
- Framer, *Casebook*: https://www.framer.com/marketplace/templates/casebook/
  - Useful principle: editorial case studies, filtering, mobile layout, and legible content.
- Framer, *FolioBase*: https://www.framer.com/marketplace/templates/foliobase/
  - Useful principle: quiet layouts that let the work lead.
- v0, *Blog & Portfolio Templates*: https://v0.app/templates/blog-and-portfolio
  - Useful principle: reusable sections and responsive layout hierarchy.
- 21st.dev, *Portfolio Projects Showcase*: https://21st.dev/@wrapcoders/components/portfolio-projects-showcase
  - Useful principle: feature one selected project; derive custom cards for a static, dependency-free website.
- 21st.dev, *Featured Project Hero*: https://dev.21st.dev/@ibrandify/components/featured-project-hero
  - Useful principle: a clear case-study introduction and challenge/approach framing.
- W3C, *Reflow*: https://www.w3.org/WAI/WCAG22/Understanding/reflow
  - Useful requirement: readable at 320 CSS px without unnecessary horizontal scrolling.

## Reusable original design prompt
> Improve a bilingual Arabic-English personal portfolio for a Management Information Systems specialist. Preserve an RTL-first experience and a TechMood blue identity (#2454E5, #1742CE, #20BDEF) with IBM Plex Sans Arabic and Manrope. Lead with a concise professional introduction, portrait, and accessible links to selected work and the academic CV. Build a bento-style projects gallery that features TechMood Technology and presents independent initiatives accurately, with useful filters and a live result count. Add a three-stage method panel (requirements → solution structure → iteration) grounded in actual work and editorial case studies explaining problem and approach. Keep whitespace generous, content readable, and animation restrained; support reduced-motion preferences. No invented awards, customer metrics, university acceptance, product features, testimonials, or degree-issuance claims. The site must remain fast, mobile-first, keyboard accessible and bilingual without a heavy framework.

## Components implemented
- Visual hierarchy through a flagship project card, supporting project cards, and consistent action icons
- Responsive 12-column desktop bento layout, balanced filtered results, and single-column phone layout
- Three-step work-method panel with Arabic/English content
- Case studies with project marks and existing problem/approach narratives
- Live project count and accessible filter labels in both languages
- Preserved TechMood blue identity, WhatsApp/Telegram communities, and existing CV link

## Constraints
- Do not copy proprietary website templates or source code.
- Do not invent business impact metrics or testimonials.
- Preserve link targets and personal branding.
- Keep project maturity descriptions truthful.
- Changes to academic degree wording must reflect actual academic records.
- Retain keyboard focus indicators, readable contrast, and reduced-motion styling.

## QA checklist
- [ ] Browse desktop and narrow-phone layouts in both Arabic and English
- [ ] Test each project filter and result count
- [ ] Test section navigation, menu, and article dialog with keyboard
- [ ] Confirm social, community, project, and CV links
- [ ] Check image loading, text wrapping, and no overflow at 320 CSS px
- [ ] Confirm deployment uses intended commit and production aliases
