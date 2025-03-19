# Construction Tools Theme System

This directory contains the universal theme system for the Construction Tools application. The theme provides consistent styling and behavior across all pages of the application.

## Files

- `theme.css` - The main CSS file containing color variables, typography, and component styles
- `theme.js` - JavaScript utilities for working with the theme
- `navigation.css` - Styles for the navigation component
- `navigation.js` - JavaScript for the navigation component

## How to Use

### 1. Include the Theme Files

Add the following to the `<head>` section of your HTML:

```html
<link rel="stylesheet" href="/styles/theme.css">
<link rel="stylesheet" href="/styles/navigation.css">
<script src="/styles/theme.js" defer></script>
<script src="/styles/navigation.js" defer></script>
```

### 2. Use CSS Variables

The theme defines CSS variables that you can use in your styles:

```css
.my-element {
  background-color: var(--primary-100);
  color: var(--primary-700);
  padding: var(--spacing-4);
  border-radius: var(--radius-md);
}
```

### 3. Use Predefined Classes

The theme includes predefined classes for common elements:

```html
<button class="btn btn-primary">Primary Button</button>
<button class="btn btn-secondary">Secondary Button</button>
<button class="btn btn-outline">Outline Button</button>

<div class="card">
  <!-- Card content -->
</div>

<div class="alert alert-success">
  Success message
</div>
```

### 4. Add Navigation

Include the navigation component in your HTML:

```html
<nav class="main-nav">
    <div class="nav-container">
        <a href="/" class="nav-logo">
            <i class="fas fa-hard-hat" style="color: var(--secondary-500);"></i>
            Construction Tools
        </a>
        <div class="nav-links">
            <a href="/" class="nav-link">Home</a>
            <a href="/calculators" class="nav-link">Calculators</a>
            <a href="/aggregates" class="nav-link">Aggregates</a>
            <a href="/employees" class="nav-link">Employees</a>
        </div>
        <button class="mobile-nav-toggle" aria-expanded="false" aria-label="Toggle navigation">
            <i class="fas fa-bars"></i>
        </button>
    </div>
</nav>
```

### 5. Add Breadcrumbs

Include the breadcrumbs component in your HTML:

```html
<div class="breadcrumbs mb-6">
    <!-- Breadcrumbs will be generated automatically by navigation.js -->
</div>
```

## Color Palette

The theme includes the following color palettes:

### Primary Colors (Steel Blue)
- Professional, industrial blue tones for main actions and UI elements
- Range from `--primary-50` (lightest) to `--primary-950` (darkest)
- Main accent color is `--primary-600` (#1a6fd4)

### Secondary Colors (Construction Yellow/Orange)
- Vibrant yellow/orange tones that evoke construction equipment
- Range from `--secondary-50` (lightest) to `--secondary-950` (darkest)
- Main secondary color is `--secondary-500` (#f59e0b)

### Accent Colors (Concrete Gray)
- Warm gray tones reminiscent of concrete and building materials
- Range from `--accent-50` (lightest) to `--accent-950` (darkest)
- Main accent color is `--accent-500` (#918b83)

### Neutral Colors (Warm Gray)
- Slightly warm gray tones for text, backgrounds, and borders
- Range from `--neutral-50` (lightest) to `--neutral-950` (darkest)
- These colors provide a softer alternative to pure grays

### Status Colors
- Success: `--success-50`, `--success-500`, `--success-700`
- Warning: `--warning-50`, `--warning-500`, `--warning-700`
- Error: `--error-50`, `--error-500`, `--error-700`

## JavaScript Utilities

The `theme.js` file provides several utility functions:

- `ConstructionTheme.formatNumber(number, decimals)` - Format a number with specified decimal places
- `ConstructionTheme.getCssVariable(variableName)` - Get the value of a CSS variable
- `ConstructionTheme.setCssVariable(variableName, value)` - Set the value of a CSS variable
- `ConstructionTheme.enhanceHeroSections()` - Add subtle enhancements to hero sections
- `ConstructionTheme.initializeHoverEffects()` - Initialize hover effects for interactive elements

## Responsive Design

The theme is fully responsive and includes media queries for different screen sizes. The navigation automatically adapts to mobile devices. 