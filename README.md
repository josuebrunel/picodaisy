
# Pico-Daisy UI

A drop-in CSS theme that gives [PicoCSS v2](https://picocss.com/) the look and feel of [DaisyUI](https://daisyui.com/), with custom component styles and a modern design system.
It's [live](https://josuebrunel.github.io/picodaisy/)

![Pico-Daisy UI Demo](https://img.shields.io/badge/style-DaisyUI_violet-570df8?style=for-the-badge&logo=css3&logoColor=white)
![PicoCSS v2](https://img.shields.io/badge/built_on-PicoCSS_v2-333333?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)
![Github Pages](https://img.shields.io/badge/github%20pages-121013?style=for-the-badge&logo=github&logoColor=white)

## ✨ Features

- **DaisyUI-inspired design** with the violet color scheme
- **Dark mode support** using CSS custom properties
- **Custom components**: Stats, Alerts, Chat bubbles, Cards, Badges, Charts
- **Modern typography** using Tailwind's default font stack
- **Responsive design** that works on all screen sizes
- **No JavaScript required** - pure CSS enhancements
- **Easy integration** with existing PicoCSS projects

## 📦 Installation

### Option 1: CDN (Recommended)
```html
<!-- PicoCSS v2 -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css">

<!-- Pico-Daisy UI (Add AFTER PicoCSS) -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/yourusername/pico-daisy/pico-daisy.css">
```

### Option 2: Local file

1. Download pico-daisy.css

2. Include it in your HTML:

```html
<link rel="stylesheet" href="css/pico.min.css">
<link rel="stylesheet" href="css/pico-daisy.css">
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

### Hero Section

```html
<section class="daisy-hero">
    <div class="daisy-hero-content">
        <h1>Welcome to Pico-Daisy</h1>
        <p class="lead">A beautiful combination of PicoCSS and DaisyUI</p>
        <button>Get Started</button>
    </div>
</section>
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
    
    <button type="submit" class="primary">Submit</button>
</form>
```
