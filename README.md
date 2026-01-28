
# Pico-Daisy UI

A drop-in CSS theme that gives [PicoCSS v2](https://picocss.com/) the look and feel of [DaisyUI](https://daisyui.com/), with custom component styles and a modern design system.
It's [live](https://josuebrunel.github.io/picodaisy/)

![Pico-Daisy UI Demo](https://img.shields.io/badge/style-DaisyUI_violet-570df8?style=for-the-badge&logo=css3&logoColor=white)
![PicoCSS v2](https://img.shields.io/badge/built_on-PicoCSS_v2-333333?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)
![Github Pages](https://img.shields.io/badge/github%20pages-121013?style=for-the-badge&logo=github&logoColor=white)

## Installation

### Option 1: CDN (Recommended)
```html
<!-- Pico-Daisy UI (Includes PicoCSS v2) -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/josuebrunel/picodaisy@latest/pico-daisy.css">
```

### Option 2: Local file

1. Download pico-daisy.css

2. Include it in your HTML:

```html
<link rel="stylesheet" href="css/pico-daisy.css">
```

## Features

- **DaisyUI-inspired design** with the violet color scheme
- **Dark mode support** using CSS custom properties
- **Extensive component library**: Steps, Toast, Tooltips, Avatars, and more
- **Custom components**: Stats, Alerts, Chat bubbles, Cards, Badges, Charts
- **Modern typography** using Tailwind's default font stack
- **Responsive design** that works on all screen sizes
- **No JavaScript required** - pure CSS enhancements
- **Easy integration** with existing PicoCSS projects

## Themes

Pico-Daisy UI comes with 7 color variants:

- **Default (Violet)**: The classic DaisyUI look.
- **Blue**: A professional blue theme.
- **Red**: A bold and energetic theme.
- **Green**: A fresh nature-inspired theme.
- **Teal**: A clean, calming theme.
- **Light Grey**: A minimal, monochrome theme.
- **Dark Grey**: A sleek, dark monochrome theme.

To use a variant, simply include the corresponding CSS file:

```html
<!-- Blue Theme -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/josuebrunel/picodaisy@latest/pico-daisy.blue.css">

<!-- Red Theme -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/josuebrunel/picodaisy@latest/pico-daisy.red.css">

<!-- Green Theme -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/josuebrunel/picodaisy@latest/pico-daisy.green.css">

<!-- Teal Theme -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/josuebrunel/picodaisy@latest/pico-daisy.teal.css">

<!-- Light Grey Theme -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/josuebrunel/picodaisy@latest/pico-daisy.light-grey.css">

<!-- Dark Grey Theme -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/josuebrunel/picodaisy@latest/pico-daisy.dark-grey.css">
```

## Custom Properties
The theme uses CSS custom properties for easy customization:

```css
:root {
    --pico-primary: #570df8;          /* DaisyUI violet */
    --pico-primary-hover: #460ac6;
    --pico-background-color: #ffffff;  /* Light mode */
    --pico-card-background-color: #ffffff;
    --pico-color: #1f2937;             /* Gray-800 */
    --pico-border-radius: 0.75rem;     /* DaisyUI's rounded corners */
    --pico-font-family: ui-sans-serif, system-ui, ...; /* Tailwind's font stack */
}
```

## Components

### Navigation bar

```html
<nav class="daisy-nav">
    <ul>
        <li><strong>Your Brand</strong></li>
    </ul>
    <ul>
        <li><a href="#">Home</a></li>
        <li><a href="#">About</a></li>
    </ul>
</nav>
```

### Menu / Side Navigation

```html
<ul class="daisy-menu">
  <li>
    <span class="daisy-menu-title">Main Menu</span>
    <ul>
      <li><a class="active">Dashboard</a></li>
      <li><a>Profile</a></li>
    </ul>
  </li>
  <li>
    <details>
      <summary>Settings</summary>
      <ul>
        <li><a>Account</a></li>
        <li><a>Security</a></li>
      </ul>
    </details>
  </li>
</ul>
```

### Hero Section

Standard Hero:
```html
<section class="daisy-hero">
    <div class="daisy-hero-content">
        <h1>Welcome to Pico-Daisy</h1>
        <p class="lead">A beautiful combination of PicoCSS and DaisyUI</p>
        <button>Get Started</button>
    </div>
</section>
```

Hero with Overlay:
```html
<div class="daisy-hero daisy-hero-overlay" style="background-image: url('image.jpg');">
  <div class="daisy-hero-content text-center text-neutral-content">
    <div>
      <h1>Hero with Overlay</h1>
      <p>Use an overlay to make text readable on busy background images.</p>
      <button class="primary">Get Started</button>
    </div>
  </div>
</div>
```

### Steps

```html
<ul class="daisy-steps">
  <li class="daisy-step daisy-step-primary">Register</li>
  <li class="daisy-step daisy-step-primary">Choose plan</li>
  <li class="daisy-step">Purchase</li>
  <li class="daisy-step">Receive Product</li>
</ul>
```

### Toast

```html
<div class="daisy-toast daisy-toast-end">
  <div class="daisy-alert alert-success">
    <span>Message sent successfully.</span>
  </div>
</div>
```

### Tooltip

```html
<div class="daisy-tooltip" data-tip="hello">
  <button>Hover me</button>
</div>
```

### Avatar

```html
<div class="daisy-avatar">
  <div class="w-24 rounded-full">
    <img src="https://i.pravatar.cc/150?img=32" />
  </div>
</div>
```

### Join (Input Group)

```html
<div class="daisy-join">
  <input class="daisy-join-item" placeholder="Email"/>
  <button class="daisy-join-item primary">Subscribe</button>
</div>
```

### Loading

```html
<span class="daisy-loading daisy-loading-spinner daisy-loading-lg"></span>
```

### Divider

```html
<div class="flex w-full flex-col border-opacity-50">
  <div class="card bg-base-300 rounded-box grid h-20 place-items-center">content</div>
  <div class="daisy-divider">OR</div>
  <div class="card bg-base-300 rounded-box grid h-20 place-items-center">content</div>
</div>
```

### Stats 

```html
<div class="daisy-stats">
    <div class="daisy-stat">
        <div class="daisy-stat-value">1,234</div>
        <div class="daisy-stat-title">Daily Users</div>
    </div>
    <div class="daisy-stat">
        <div class="daisy-stat-value">89%</div>
        <div class="daisy-stat-title">Satisfaction</div>
    </div>
</div>
```

### Alerts

```html
<div class="daisy-alert alert-info">
    <span>ℹ</span>
    <div>This is an informational alert</div>
</div>

<div class="daisy-alert alert-success">
    <span>✓</span>
    <div>Success! Operation completed</div>
</div>

<div class="daisy-alert alert-warning">
    <span>⚠</span>
    <div>Warning: Please check configuration</div>
</div>

<div class="daisy-alert alert-error">
    <span>✗</span>
    <div>Error: Something went wrong</div>
</div>
```

### Chat Bubbles

```html
<div class="daisy-chat">
    <div class="chat-message chat-start">
        <div class="chat-bubble">
            Hello! How can I help you?
        </div>
    </div>
    <div class="chat-message chat-end">
        <div class="chat-bubble">
            I need assistance with my order
        </div>
    </div>
</div>
```

### Cards

```html
<article class="daisy-card">
    <header>
        <h3>Card Title</h3>
        <span class="badge badge-primary">New</span>
    </header>
    <p>Card content with hover effect and shadow</p>
    <footer>
        <button>Learn More</button>
    </footer>
</article>
```

### Badges

```html
<!-- Solid Badges -->
<span class="badge">Default</span>
<span class="badge badge-primary">Primary</span>
<span class="badge badge-secondary">Secondary</span>
<span class="badge badge-accent">Accent</span>
<span class="badge badge-ghost">Ghost</span>

<!-- Outline Badges -->
<span class="badge badge-outline">Default Outline</span>
<span class="badge badge-primary badge-outline">Primary Outline</span>
<span class="badge badge-secondary badge-outline">Secondary Outline</span>
```

### Chart Wrappers

```html
<div class="daisy-chart-wrapper">
    <div class="daisy-chart-header">
        <div>
            <h3 class="daisy-chart-title">Monthly Revenue</h3>
            <p class="daisy-chart-subtitle">Last 6 months performance</p>
        </div>
        <div class="daisy-chart-toolbar">
            <button class="chart-toolbar-btn active">1M</button>
            <button class="chart-toolbar-btn">3M</button>
        </div>
    </div>
    
    <!-- Your chart library goes here -->
    <canvas id="myChart"></canvas>
    
    <div class="daisy-chart-legend">
        <div class="legend-item">
            <span class="legend-color primary"></span>
            <span>Product Sales</span>
        </div>
        <div class="legend-item">
            <span class="legend-color secondary"></span>
            <span>Services</span>
        </div>
    </div>
    
    <div class="daisy-chart-footer">
        <span class="chart-updated">Updated 2 hours ago</span>
        <a href="#" class="chart-source">View raw data</a>
    </div>
</div>
```

### Form Elements

```html
<form>
    <label for="email">
        Email
        <input type="email" id="email" placeholder="your@email.com">
    </label>
    
    <label for="password">
        Password
        <input type="password" id="password">
    </label>

    <label>
        <input name="terms" type="checkbox" role="switch" checked />
        I agree to the terms
    </label>
    
    <button type="submit" class="primary">Submit</button>
</form>
```
