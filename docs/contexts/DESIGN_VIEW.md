# DESIGN VIEW - SLICE_GPT_LAB SITE

## Purpose

Define the design decisions for the documentation site in `docs/index.html`.

This view is the source of truth for the visual and interaction direction of the local course site.

---

## Product Intent

The site is a minimal study reader for Slice GPT Lab.

It should feel close to a clean word processor document, but warmer, more playful, and easier to navigate.

The experience must help students move through the course without feeling like they are inside a heavy web application.

---

## Audience

| Audience | Need |
|---|---|
| Student / developer | Read the full course in order |
| Young learner | Understand AI steps with friendly visual cues |
| Teacher / facilitator | Present the learning path as one coherent page |

---

## Design Principles

- Minimal first.
- Document-like layout.
- One main reading surface.
- Soft playful details instead of decorative clutter.
- Clear internal navigation.
- No dependency on markdown loading at runtime.
- No public links to source markdown files from the site.
- No complex frontend framework.
- Prefer readable content over animation.

---

## Technology Choices

| Concern | Decision | Reason |
|---|---|---|
| Structure | HTML5 | Static, inspectable, beginner-friendly |
| Styling | Tailwind CSS via CDN | Fast iteration without build tooling |
| Interaction | Vanilla JavaScript | Keeps the site simple and educational |
| Icons | Lucide via CDN | Consistent lightweight icon language |
| Runtime | Static local file / static server | Matches local educational project |

---

## Visual System

### Layout

- Sticky top header.
- Left course navigation on desktop.
- Central document page as the main reading surface.
- Single-page internal anchor navigation.
- Print-friendly layout.

### Tone

- Minimal.
- Warm.
- Study-oriented.
- Lightly playful.

### Palette

| Token | Color | Use |
|---|---|---|
| `ink` | `#202124` | Main text and dark buttons |
| `page` | `#fffdf8` | Reading surface |
| `shell` | `#f4f0e8` | Outer background |
| `line` | `#e4ded2` | Borders and separators |
| `soft` | `#746d63` | Secondary text |
| `coral` | `#f06a7a` | Primary accent |
| `honey` | `#f8c75e` | Highlight accent |
| `mint` | `#6fcfac` | Learning/progress accent |
| `sky` | `#6caef8` | Technical accent |
| `grape` | `#9b83f6` | Concept accent |

### Components

- Header with course identity.
- Progress bar.
- Searchable course map.
- Central paper-like reading container.
- Icon chips.
- Lesson sections.
- Code blocks.
- Flow cards.
- Focus mode.
- Print button.

---

## Interaction Rules

- Course navigation uses internal anchors only.
- The active lesson is highlighted while scrolling.
- The filter narrows visible course map entries.
- Focus mode hides the sidebar and centers reading.
- Print removes navigation and keeps the document content.
- JavaScript enhances navigation but should not hide core content.

---

## Content Rules

- Public site content should be in English.
- The site should not expose markdown-source links as primary navigation.
- The markdown files may remain in the repository as source documentation, but the HTML site should be self-contained.
- The site summarizes the complete learning path:
  - Course guide
  - Introduction
  - How LLMs work
  - Context model
  - Tokenization
  - Embeddings
  - Self-attention
  - Transformer blocks
  - Forward pass
  - Loss and backpropagation
  - Training loop
  - Checkpoint and weights
  - Inference
  - API layer
  - Limitations
  - File-by-file lessons
  - Young builders guide

---

## Accessibility

- Use semantic sections and headings.
- Keep text contrast readable.
- Use buttons for actions.
- Keep navigation labels explicit.
- Preserve print mode.
- Avoid motion-heavy interactions.

---

## Non-Goals

- No SPA framework.
- No build pipeline.
- No markdown runtime renderer.
- No marketing landing-page layout.
- No decorative hero artwork.
- No external analytics.

---

## Readiness Gate

- Design direction is explicit: yes.
- Runtime choices are defined: yes.
- Navigation behavior is defined: yes.
- Visual tokens are defined: yes.
- Content language rule is defined: yes.
- Blockers: none.
