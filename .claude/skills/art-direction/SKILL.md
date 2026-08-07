---
name: art-direction
description: Dirección de arte y sistema visual de este portafolio (editorial, analógico-digital, tipografía expresiva, color emocional, collage, motion, accesibilidad). Úsalo SIEMPRE que diseñes, rediseñes, estilices, revises o extiendas cualquier parte visual del sitio — hero, proyectos, skills/stack, about, archive, certificaciones, contacto, componentes, tokens CSS, animaciones o layout responsive. También al portar secciones del sitio legacy a Astro.
---

# Personal Portfolio Art Direction

## 0. Mission

This portfolio is not a generic developer landing page.

It is a personal digital space: part portfolio, part archive, part editorial object,
part visual diary, and part software showcase.

The visitor should first feel:

> "This person has a point of view."

and only then:

> "This person builds software."

The interface must communicate personality without sacrificing clarity, accessibility,
performance, or the ability to understand the owner's work.

The site should feel authored, not templated.

---

# 1. Core creative idea

## A stable system containing changing emotional states

The site has a consistent structural foundation:

- navigation
- spacing
- typography roles
- interaction logic
- page rhythm
- responsive behavior
- accessibility
- content hierarchy

Inside that foundation, each section or project may have a different emotional tone.

The portfolio should be able to move between:

- clean and chaotic
- quiet and saturated
- analog and digital
- polished and imperfect
- editorial and playful
- nostalgic and contemporary

without losing identity.

Do not force every page to look identical.

Do not let every page look unrelated.

---

# 2. Reference translation

The visual references come from music, fashion, editorial design, photography,
early-digital interfaces, collage, and expressive animation.

The goal is NOT to copy any artist, album, brand, website, logo, cover, or campaign.

Extract the underlying principles.

## Tyler / CMIYGL — worldbuilding

Take inspiration from the idea of building a complete visual universe using:

- documents
- IDs
- stamps
- tickets
- labels
- travel ephemera
- printed matter
- photography
- objects
- personal artifacts
- codes and serial numbers
- handwritten marks

Use this principle to turn the owner's real life and work into a coherent world.

Examples of portfolio-native objects:

- project tickets
- build receipts
- issue numbers
- commit references
- terminal fragments
- certificates
- screenshots
- project labels
- timestamps
- archive IDs
- technical notes
- city/location metadata
- handwritten annotations

Do not reproduce CMIYGL assets or branding.

## Frank Ocean — emotion through color

Color is not merely brand decoration.

Color can represent:

- mood
- memory
- intensity
- project personality
- section atmosphere

The site does not need one permanent corporate accent color.

Use a neutral base, then allow deliberate emotional colors to appear where they have
meaning.

A project may be blue because it should feel calm and introspective.

Another may be orange because it should feel warm, energetic, or nostalgic.

Another may be red because it needs urgency or visual force.

Choose color because of the desired feeling, not because a palette generator suggested it.

## Golf Wang — personality + object presentation

Take inspiration from:

- confident color
- clean white space
- strong product-like presentation
- objects given room to exist
- straightforward navigation
- playful but controlled visual identity

Do not turn the portfolio into an ecommerce site.

Use the principle of presenting important items as if they deserve attention.

Projects, technologies, artifacts, and photographs should not be compressed into
identical cards by default.

## Brent Faiyaz / ICON — digital nostalgia and typography

Use as a secondary language:

- early-2000s digital references
- desktop/file-browser metaphors
- interface chrome
- soft-tech typography
- slightly futuristic or Y2K letterforms
- system-like labels
- monospaced metadata
- compact UI details

This language should be contextual.

Good places:

- Archive
- Experiments
- Certifications
- Miscellaneous work
- Project files
- Media
- Technical notes

Do not place the entire website inside a fake operating system window.

## Spider-Verse-like energy — composition and motion

Use only as an energy reference.

Extract:

- extreme scale changes
- panel divisions
- layered frames
- diagonal tension
- motion
- unexpected crops
- bursts of saturation
- visual rhythm

Do not imitate characters, comic assets, or franchise-specific graphics.

Use this energy for occasional high-impact moments.

---

# 3. Design ratio

Default visual balance:

- 70% editorial clarity
- 20% analog/digital collage
- 10% controlled chaos

This ratio is a guideline, not a literal calculation.

If the screen feels chaotic, remove elements before adding more.

If the screen feels generic, add one meaningful personal or editorial gesture.

---

# 4. Personality test

Before approving a design, ask:

1. Could this exact screen belong to 1,000 other developer portfolios?
2. Does it contain a decision that feels authored?
3. Does it reveal something about the owner beyond job title?
4. Is the visual idea connected to the content?
5. Is the unusual element helping the story?
6. Is the design still usable without animation?
7. Does the mobile version retain personality?
8. Is the page memorable after closing the tab?

If the answer to #1 is "yes", the design needs more identity.

If the unusual visual element has no reason to exist, remove it.

---

# 5. Base visual system

## Foundation

Prefer:

- warm off-white
- ivory
- paper white
- deep black
- charcoal
- dark olive
- muted gray

Possible base tokens:

```css
--paper: #F3F0E7;
--paper-clean: #FAF9F5;
--ink: #11110F;
--ink-soft: #2A2924;
--muted: #77736A;
--line: rgba(17, 17, 15, 0.18);
```

These are starting points, not mandatory exact values.

Avoid pure #FFFFFF everywhere unless the composition benefits from clinical white.

Avoid making the entire site dark mode by default simply because it is a developer portfolio.

---

# 6. Emotional color system

Do not define one universal accent and apply it everywhere.

Create contextual palettes.

Possible emotional associations:

| Color family | Possible feeling |
|---|---|
| Blue | calm, introspection, digital, distance |
| Red | energy, urgency, focus, heat |
| Yellow | play, confidence, optimism |
| Green | growth, nature, systems, experimentation |
| Pink | personality, nostalgia, intimacy |
| Orange | warmth, memory, movement |
| Purple | dreamlike, surreal, nighttime |

These meanings are flexible.

A project's color should come from the project's personality.

## Rule

A section may temporarily dominate the screen with a strong color.

The full site should still return to a neutral visual baseline.

Avoid permanent rainbow interfaces.

Avoid generic purple-to-blue startup gradients.

---

# 7. Typography system

Typography must carry a large percentage of the visual identity.

Use a role-based system.

## Display

For:

- name
- hero statement
- project titles
- section openers
- issue numbers
- oversized editorial words

Characteristics:

- strong silhouette
- confident
- high personality
- may be grotesk, bold sans, condensed, wide, or soft-tech/Y2K

Suggested direction, not mandatory fonts:

- bold grotesk
- neo-grotesk
- geometric display
- extended/condensed display
- soft futuristic sans

## Body

For:

- descriptions
- case studies
- biography
- project context

Characteristics:

- neutral
- readable
- not overly stylized
- comfortable at long lengths

## Metadata / system

For:

- dates
- file names
- coordinates
- project IDs
- labels
- versions
- stacks
- timestamps

Prefer:

- mono
- narrow sans
- system-like type

## Handwriting

Use sparingly.

For:

- arrows
- short notes
- signatures
- emotional comments
- labels
- annotations

Never use handwriting for long body text.

If the owner has real handwriting available, prefer a scanned or traced personal mark
over a generic handwritten font.

---

# 8. Type scale

Use contrast in scale aggressively.

Example:

```css
--text-xs: clamp(.7rem, .65rem + .15vw, .8rem);
--text-sm: clamp(.85rem, .8rem + .2vw, 1rem);
--text-md: clamp(1rem, .95rem + .3vw, 1.2rem);
--text-lg: clamp(1.3rem, 1.1rem + .8vw, 2rem);
--text-xl: clamp(2rem, 1.4rem + 2.5vw, 4rem);
--text-display: clamp(4rem, 10vw, 10rem);
```

A huge title next to tiny metadata is encouraged.

Do not solve hierarchy only with font-weight.

Use:

- size
- position
- whitespace
- width
- capitalization
- contrast

---

# 9. Layout philosophy

The grid is a tool, not a prison.

Use:

- strong alignment
- large margins
- intentional whitespace
- asymmetry
- overlap
- full-bleed media
- large typographic blocks
- occasional off-grid objects

Most screens should begin from a clean grid.

Then break the grid once, intentionally.

Do not randomly rotate or overlap every element.

---

# 10. Spacing

Recommended spacing scale:

```text
4
8
12
16
24
32
48
64
96
128
160
```

Major section spacing:

Desktop:
- 96–160px typical

Mobile:
- 56–96px typical

Do not make every section the same height.

Allow some sections to feel dense and others quiet.

---

# 11. Hero direction

Do NOT default to:

- circular portrait
- "Hi, I'm..."
- generic subtitle
- two gradient buttons
- animated blobs
- skill badges
- centered everything

Preferred hero language:

- oversized name
- editorial crop
- strong photo
- minimal metadata
- one personal annotation
- one visual object or stamp
- clear path to work

Example information architecture:

```text
LUIS
EDUARDO
BARRÓN

DEVELOPER / SYSTEMS / INTERNET
MAZATLÁN, MX
2026 — PRESENT

[VIEW WORK]
```

Possible secondary objects:

```text
PORTFOLIO — ISSUE 001
BUILD 2026.08
AVAILABLE / SELECTED WORK
ARCHIVE ID: LEB-001
```

Do not make all of these visible at once.

Choose what serves the composition.

---

# 12. Navigation

Navigation should be simple enough to survive visual experimentation around it.

Preferred:

- text links
- compact labels
- minimal chrome
- subtle active state

Possible sections:

```text
INDEX
WORK
ABOUT
ARCHIVE
CONTACT
```

or:

```text
WORK
ABOUT
STACK
ARCHIVE
CONTACT
```

Do not create a dashboard navbar.

Do not overuse pill-shaped navigation.

Sticky is allowed if it remains lightweight.

---

# 13. Projects

Projects are the main professional proof.

Each project should feel like a feature story, not a database row.

Avoid identical card grids by default.

Possible compositions:

- large image + small metadata
- full-width project poster
- split screen
- editorial spread
- project index with strong typography
- image sequence
- archive file entry
- horizontal strip
- numbered chapter

Each project may have:

```text
01
PROJECT NAME
ROLE
YEAR
STACK
STATUS
SHORT DESCRIPTION
```

Prioritize:

- real screenshots
- real interface states
- real development artifacts
- project-specific visual language

Do not decorate weak content with excessive effects.

---

# 14. Project case studies

A case study should answer:

- What was it?
- What problem existed?
- What did the owner build?
- What was the owner's role?
- What decisions mattered?
- What technologies were used?
- What changed?
- What was learned?

Visual content can include:

- screenshots
- flows
- diagrams
- commit snippets
- architecture fragments
- before/after
- mobile screens
- API examples
- deployment notes

Do not make a case study read like a corporate annual report.

Keep it personal, technical, and concise.

---

# 15. Skills / stack

Never default to 30 colored technology pills.

Possible treatment:

```text
WHAT I USE

FRONTEND
Angular
Ionic
Astro
TypeScript

BACKEND
NestJS
Node.js

DATA
MySQL
PostgreSQL

TOOLS
Git
Docker
Linux
```

Alternative:

Present technologies as an editorial catalog.

Each item may receive:

- index number
- category
- experience context
- small icon
- tiny annotation

Icons are secondary.

Names and context matter more.

---

# 16. About section

About should feel personal but not like a social-media biography.

Use a mix of:

- portrait
- short biography
- personal objects
- document-like metadata
- handwriting
- city
- timeline fragments
- interests
- work philosophy

Possible visual concept:

A custom "license", "archive record", "passport", or "identity document" created for the
portfolio.

Example concept:

```text
PERSONAL ARCHIVE RECORD

NAME ............ LUIS EDUARDO
FIELD ........... SOFTWARE / SYSTEMS
BASE ............ MAZATLÁN, MX
STATUS .......... BUILDING
ISSUED .......... 2026
```

This must be an original design.

Do not reproduce an existing artist's exact prop or document.

---

# 17. Archive

Archive is the ideal place for stronger early-digital/Y2K interface language.

Possible content:

- experiments
- certifications
- school work
- prototypes
- screenshots
- photos
- abandoned ideas
- small utilities
- design tests
- miscellaneous builds

Possible visual metaphor:

- file browser
- old desktop window
- media library
- directory
- catalog
- index

Keep actual navigation usable.

Retro UI must not reduce accessibility.

---

# 18. Certifications / education

Avoid generic certificate cards.

Treat them as documents in an archive.

Possible format:

```text
ARCHIVE / EDUCATION

2026
Linux Essentials
Cisco Networking Academy
PDF / CERTIFICATE

2025
...
```

Optionally show a scanned/document preview.

---

# 19. Contact

Contact should feel like the closing page of a publication.

Keep it strong and simple.

Examples:

```text
LET'S MAKE
SOMETHING WORTH
REMEMBERING.
```

or a more understated ending:

```text
END OF ISSUE 001

EMAIL
GITHUB
LINKEDIN
```

Avoid giant contact forms unless necessary.

---

# 20. Photography

Photography is a major design material.

Prefer:

- real photos
- flash photography
- grain
- imperfect framing
- natural moments
- editorial crops
- scanned texture
- low-light images
- personal objects

Do not over-process every photo with the same filter.

Possible treatments:

- monochrome
- warm grain
- overexposure
- halftone
- photocopy
- duotone
- color wash
- cutout

Use treatments according to the emotional context.

---

# 21. Collage rules

Collage must feel composed, not accidental.

Allowed materials:

- photography
- screenshots
- paper
- receipts
- tickets
- labels
- text fragments
- diagrams
- stamps
- stars
- tape
- scribbles
- scanned objects
- UI fragments
- newspaper-like text
- code fragments

Rules:

1. Start with hierarchy.
2. Choose one focal object.
3. Add supporting elements.
4. Keep one clear reading path.
5. Preserve breathing room.
6. Do not use every collage technique at once.
7. Let some edges remain clean.

---

# 22. Texture

Texture should simulate physical media without destroying legibility.

Allowed:

- grain
- paper
- scan noise
- halftone
- photocopy
- slight ink bleed
- compression artifacts
- subtle dust

Avoid:

- heavy texture behind body text
- texture on every component
- fake grunge overlays with no purpose

---

# 23. Borders, radius, and shadows

Prefer:

- straight edges
- subtle borders
- low-radius components
- occasional hard outline

Typical radius:

```text
0
4
8
12
```

Use 16px+ only when a component clearly benefits.

Avoid making everything a rounded card.

Avoid floating SaaS shadows.

If a shadow is used, consider:

- hard editorial offset shadow
- tiny natural elevation
- contextual physical-object shadow

---

# 24. Buttons and links

Buttons should not look like generic startup CTAs.

Prefer:

- text links
- underlines
- arrows
- compact boxed actions
- hard-edged controls
- context-specific retro UI controls

Hover ideas:

- underline grows
- arrow shifts
- text inverts
- background snaps to emotional color
- small label appears

Do not animate buttons excessively.

---

# 25. Motion

Motion should feel designed.

Preferred:

- reveal
- slide
- clip
- crop
- subtle scale
- image parallax
- panel transition
- text mask
- horizontal movement
- layered entry

Microinteraction:
150–250ms

Interface transition:
250–450ms

Editorial reveal:
450–900ms

Preferred easing:

```css
cubic-bezier(0.16, 1, 0.3, 1)
```

Do not animate every element on scroll.

One strong animation is better than ten weak ones.

Always support:

```css
@media (prefers-reduced-motion: reduce)
```

---

# 26. Scroll behavior

Scroll can be cinematic but must remain understandable.

Allowed:

- sticky project media
- horizontal project sequence
- changing background color
- section color transitions
- image reveal
- large type movement
- controlled parallax

Avoid:

- scroll hijacking
- excessive smooth-scroll delay
- interactions that make users fight the page
- mandatory animations before content becomes readable

---

# 27. Responsive design

Mobile is not a simplified afterthought.

The mobile version must preserve:

- strong typography
- emotional color
- photography
- hierarchy
- personality
- intentional asymmetry

On mobile:

- collapse complex overlap
- reduce decorative objects
- keep one dominant gesture per screen
- remove hover-only concepts
- increase tap targets
- preserve project images
- avoid horizontal overflow unless the interaction is explicitly horizontal

Never simply stack every desktop column and call it done.

---

# 28. Accessibility

Experimental design still needs discipline.

Always:

- semantic HTML
- meaningful headings
- keyboard navigation
- visible focus
- alt text
- adequate contrast
- accessible link names
- minimum touch target sizes
- readable body text
- reduced-motion support

Decorative images should not create noise for screen readers.

Important information must never exist only through color.

---

# 29. Performance

The page should feel like an art-directed site, not a heavy art project.

Prefer:

- AVIF/WebP
- responsive images
- lazy loading
- SVG
- CSS effects
- native browser APIs
- lightweight animation
- selective JavaScript

Do not import a large animation library for a simple fade.

Do not ship multi-megabyte textures when a tiny optimized asset works.

---

# 30. Content authenticity

Do not generate fake personality.

Avoid empty statements like:

- "I turn ideas into digital experiences"
- "Passionate developer"
- "Crafting innovative solutions"
- "Where creativity meets code"

Prefer specific language.

Good copy sounds like something the owner would actually say.

Use:

- real interests
- real projects
- real constraints
- real tools
- real observations
- real humor when appropriate

---

# 31. Anti-generic rules

Never default to:

- purple/blue gradient hero
- floating glowing orb
- particle background
- glassmorphism
- Bento-grid-everything
- 3D floating tech logos
- circular headshot with gradient ring
- gradient CTA buttons
- "Hi, I'm X"
- giant list of skill pills
- four identical project cards
- dashboard UI
- startup landing page
- fake testimonials
- excessive rounded rectangles
- random neon
- generic AI copy

A component may use one of these patterns only if there is a specific conceptual reason.

---

# 32. Anti-copy rules

References are inspiration, not assets.

Do not:

- recreate an album cover
- recreate Golf Wang's exact website
- recreate a CMIYGL passport
- copy a Brent Faiyaz logo
- reproduce Spider-Verse art
- imitate a living designer's work one-to-one
- use artist logos as portfolio identity

Instead:

1. identify the principle
2. translate it into personal content
3. redesign it using original assets
4. make it belong to the portfolio's world

---

# 33. UI component rule

Before creating a new component, inspect existing:

- typography
- spacing
- colors
- borders
- interactions
- responsive behavior
- image treatment

New components must inherit the system.

Do not create isolated mini-design systems inside individual sections.

---

# 34. Editing existing sections

When asked:

> "Improve this section."

Do not automatically redesign everything.

Follow:

1. identify the purpose
2. preserve useful content
3. remove generic styling
4. improve hierarchy
5. improve composition
6. improve typography
7. improve spacing
8. introduce one meaningful visual idea
9. verify mobile
10. verify accessibility

Do not change unrelated sections without reason.

---

# 35. Implementation decision hierarchy

When choosing between design options, prioritize:

1. personality
2. clarity
3. content
4. typography
5. composition
6. responsiveness
7. accessibility
8. motion
9. decorative detail

Decoration is last.

---

# 36. Recommended page architecture

Suggested structure:

```text
/
  Hero / Cover
  Selected Work
  Short About
  Stack
  Archive Preview
  Contact / Closing Page

/work
  Project Index

/work/[project]
  Project Case Study

/about
  Personal editorial profile
  Personal archive/document concept

/archive
  Experiments
  Certifications
  Misc
  Media

/contact
  Minimal contact page
```

This architecture may be adapted to the existing project.

Do not create pages solely to imitate another website.

---

# 37. Suggested design tokens

Example only:

```css
:root {
  --paper: #F3F0E7;
  --paper-clean: #FAF9F5;
  --ink: #11110F;
  --ink-soft: #2A2924;
  --muted: #77736A;
  --line: rgba(17, 17, 15, 0.18);

  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-3: 0.75rem;
  --space-4: 1rem;
  --space-6: 1.5rem;
  --space-8: 2rem;
  --space-12: 3rem;
  --space-16: 4rem;
  --space-24: 6rem;
  --space-32: 8rem;

  --radius-xs: 2px;
  --radius-sm: 6px;
  --radius-md: 10px;

  --ease-editorial: cubic-bezier(0.16, 1, 0.3, 1);
}
```

Project-specific emotional colors should live outside the global identity:

```css
[data-project="example"] {
  --project-bg: ...;
  --project-fg: ...;
  --project-accent: ...;
}
```

---

# 38. Visual review checklist

Before finishing any visual task, verify:

## Identity

- Does it feel authored?
- Is there one strong visual idea?
- Is it connected to the content?
- Does it avoid generic developer-portfolio tropes?

## Hierarchy

- Is the first thing obvious?
- Can the section be understood in five seconds?
- Are title, metadata, image, and body clearly differentiated?

## Composition

- Is whitespace intentional?
- Is overlap controlled?
- Is asymmetry helping?
- Is there unnecessary decoration?

## Color

- Does color have a purpose?
- Is the emotional tone intentional?
- Is contrast accessible?
- Are too many accents competing?

## Typography

- Is display type doing meaningful work?
- Is body copy readable?
- Is metadata visually secondary?
- Is handwriting used sparingly?

## Media

- Are images high enough quality?
- Are crops intentional?
- Are treatments consistent with the mood?
- Are screenshots presented as content rather than filler?

## Motion

- Does motion improve the experience?
- Does the page work without motion?
- Is reduced motion respected?

## Mobile

- Does mobile retain personality?
- Is there overflow?
- Are tap targets usable?
- Are decorative layers simplified intelligently?

## Performance

- Are large assets optimized?
- Is unnecessary JavaScript avoided?
- Are fonts and images loaded intentionally?

---

# 39. Final creative rule

The portfolio must not look like a developer trying to prove that they know design trends.

It should look like a person with tastes, memories, references, technical ability,
and a personal visual language who happens to express all of that through a website.

When forced to choose between:

- a fashionable effect
- a personal idea

choose the personal idea.

When forced to choose between:

- more decoration
- stronger composition

choose stronger composition.

When forced to choose between:

- copying a reference
- translating why the reference works

translate the principle.

The final site should feel like a digital extension of the owner.
