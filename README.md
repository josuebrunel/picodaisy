# Pico-Daisy UI

A single, self-contained CSS file that gives [PicoCSS v2](https://picocss.com/) a [DaisyUI](https://daisyui.com/)-inspired
violet look. Link one file — nothing else to install, no CDN dependency, no build step.

[Live demo](https://josuebrunel.github.io/picodaisy/)

![PicoCSS v2](https://img.shields.io/badge/built_on-PicoCSS_v2.0.6-333333?style=for-the-badge)
![Self-contained](https://img.shields.io/badge/dependencies-none-570df8?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)

## Installation

```html
<!-- CDN -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/josuebrunel/picodaisy@latest/pico-daisy.css">
```

or download `pico-daisy.css` and link it locally:

```html
<link rel="stylesheet" href="pico-daisy.css">
```

That's it — `pico-daisy.css` vendors PicoCSS itself, so this is the only stylesheet you need.

## Philosophy

Pico-Daisy stays as close to PicoCSS's own "classless" spirit as possible:

- **Plain semantic HTML is themed automatically.** `<button>`, `<article>`, `<details>`, `<progress>`, `<mark>`,
  `<kbd>`, `<dialog>`, form inputs — all pick up the violet theme with zero classes, because Pico-Daisy only
  redefines PicoCSS's own CSS custom properties (`--pico-*`).
- **PicoCSS's native variants aren't reinvented.** Secondary/outline/contrast buttons, `data-tooltip` tooltips,
  `<details>` accordions and `aria-busy="true"` loading states are already built into Pico — Pico-Daisy doesn't
  ship a parallel class system for any of them. Check the [PicoCSS docs](https://picocss.com/docs) for those.
- **A small set of opt-in classes** covers what plain HTML genuinely can't express: badges, alerts, avatars,
  stats, and a few layout/visual utilities. That's the entire custom class list — see [Components](#components)
  below.

## Themes

7 color variants, each with full dark mode support (`data-theme="dark"` or `prefers-color-scheme: dark`):

| Theme | Primary | File |
| --- | --- | --- |
| **Violet** (default) | `#6366f1` | `pico-daisy.css` |
| **Blue** | `#2563eb` | `pico-daisy.blue.css` |
| **Red** | `#e11d48` | `pico-daisy.red.css` |
| **Green** | `#22c55e` | `pico-daisy.green.css` |
| **Teal** | `#14b8a6` | `pico-daisy.teal.css` |
| **Light Grey** | `#6b7280` | `pico-daisy.light-grey.css` |
| **Dark Grey** | `#475569` | `pico-daisy.dark-grey.css` |

Use a variant file **instead of** `pico-daisy.css` — it imports the base theme and only overrides the color scale:

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/josuebrunel/picodaisy@latest/pico-daisy.blue.css">
```

## Custom properties

Reskinning the whole theme means overriding four tokens (see any `pico-daisy.*.css` file for a working example):

```css
:root {
    --primary-400: #3b82f6; /* light shade — soft badges, dark-mode accents */
    --primary-500: #2563eb; /* base — buttons, links, focus rings */
    --primary-600: #1d4ed8; /* hover/active */
    --primary-700: #1e40af; /* deep — soft-badge text */
}
```

Everything else — surfaces, borders, shadows, semantic success/warning/error/info colors, radii — lives in
`pico-daisy.css` under `:root` and its `[data-theme="dark"]` block, all as regular CSS custom properties you can
override the same way.

## Components

### Native PicoCSS (zero extra classes)

```html
<button>Primary</button>
<button class="secondary">Secondary</button>
<button class="outline">Outline</button>
<button class="contrast">Contrast</button>
<button aria-busy="true">Loading…</button>

<article>
    <header>Card title</header>
    <p>Any &lt;article&gt; is a themed card, including header/footer sectioning.</p>
    <footer><button>Action</button></footer>
</article>

<details>
    <summary>Accordion item</summary>
    <p>Content revealed on click, with an animated chevron.</p>
</details>

<span data-tooltip="Hello!">Hover me</span>

<dialog id="my-modal">
    <article>
        <header>
            <a href="#close" aria-label="Close" class="close" rel="prev"></a>
            Title
        </header>
        <p>Modal content.</p>
        <footer>
            <button class="secondary">Cancel</button>
            <button>Confirm</button>
        </footer>
    </article>
</dialog>
```

### Pico-Daisy additions

**Button extras** — `.btn-ghost` (the one variant Pico doesn't ship), plus `.btn-sm` / `.btn-lg` sizes:

```html
<button class="btn-ghost">Ghost</button>
<button class="btn-sm">Small</button>
<button class="btn-lg">Large</button>
```

**Badges**:

```html
<span class="badge badge-primary">Primary</span>
<span class="badge badge-success">Success</span>
<span class="badge badge-warning">Warning</span>
<span class="badge badge-error">Error</span>
<span class="badge badge-info">Info</span>
<span class="badge badge-soft-primary">Soft primary</span>
```

**Alerts**:

```html
<div role="alert" class="alert-info">Informational message</div>
<div role="alert" class="alert-success">Success message</div>
<div role="alert" class="alert-warning">Warning message</div>
<div role="alert" class="alert-error">Error message</div>
```

**Avatars**:

```html
<div class="avatar"><img src="user.jpg" alt=""></div>
<div class="avatar avatar-lg"><img src="user.jpg" alt=""></div>

<div class="avatar-group">
    <div class="avatar"><img src="user1.jpg" alt=""></div>
    <div class="avatar"><img src="user2.jpg" alt=""></div>
</div>
```

**Floating labels**:

```html
<div class="input-floating">
    <input type="email" id="email" placeholder=" " required>
    <label for="email">Email address</label>
</div>
```

**Cards for non-`<article>` elements** and **hover lift**:

```html
<div class="card card-hover">Card content on a &lt;div&gt;</div>
```

**Stats**:

```html
<div class="stats">
    <div class="stat">
        <div class="stat-value">1,204</div>
        <div class="stat-label">Daily users</div>
    </div>
</div>
```

**Layout & visual utilities**:

```html
<!-- Sticky, translucent nav -->
<nav class="glass sticky-top">…</nav>

<!-- Full-bleed hero section -->
<section class="hero bg-mesh">
    <h1><span class="text-gradient">Gradient</span> heading</h1>
</section>

<!-- Labeled divider -->
<div class="divider">OR</div>
```

## License

MIT — see [LICENSE](LICENSE). PicoCSS is vendored inside `pico-daisy.css` under its own MIT license.
