# Theme customization reference

Guide to customizing the appearance and behavior of your MkDocs Material portfolio site.

## Overview

MkDocs Material provides extensive customization options without requiring custom CSS. This guide covers theme configuration, colors, fonts, features, and advanced customization.

## Basic theme configuration

### Color schemes

Material supports light and dark color schemes with customizable primary and accent colors.

#### Light and dark mode

Enable automatic theme switching:

```yaml
theme:
  name: material
  palette:
    # Light mode
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    
    # Dark mode
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
```

This enables a toggle button for users to switch between light and dark modes.

#### Single color scheme

Use only light or dark mode:

```yaml
theme:
  name: material
  palette:
    scheme: default  # or 'slate' for dark
    primary: indigo
    accent: indigo
```

### Primary and accent colors

Choose from Material Design colors:

**Available primary colors**:
- `red`, `pink`, `purple`, `deep purple`
- `indigo`, `blue`, `light blue`, `cyan`
- `teal`, `green`, `light green`, `lime`
- `yellow`, `amber`, `orange`, `deep orange`
- `brown`, `grey`, `blue grey`
- `black`, `white`

**Example configurations**:

Professional blue:
```yaml
primary: blue
accent: light blue
```

Modern purple:
```yaml
primary: deep purple
accent: purple
```

Vibrant green:
```yaml
primary: teal
accent: green
```

Tech-focused:
```yaml
primary: indigo
accent: cyan
```

### Fonts

Customize text and code fonts:

```yaml
theme:
  name: material
  font:
    text: Roboto
    code: Roboto Mono
```

**Popular font combinations**:

Clean and modern:
```yaml
font:
  text: Inter
  code: Fira Code
```

Professional:
```yaml
font:
  text: Open Sans
  code: Source Code Pro
```

Technical:
```yaml
font:
  text: Ubuntu
  code: Ubuntu Mono
```

Disable web fonts (use system fonts):
```yaml
theme:
  font: false
```

## Logo and favicon

### Add custom logo

Place logo file in `docs/images/`:

```yaml
theme:
  name: material
  logo: images/logo.png
```

Or use Material Design icon:

```yaml
theme:
  icon:
    logo: material/book-open-page-variant
```

### Add favicon

```yaml
theme:
  favicon: images/favicon.png
```

Recommended sizes:
- Logo: 128x128 or 256x256 PNG with transparency
- Favicon: 32x32 or 16x16 PNG or ICO format

## Navigation features

### Enable navigation features

```yaml
theme:
  name: material
  features:
    # Top-level tabs
    - navigation.tabs
    - navigation.tabs.sticky
    
    # Sections in sidebar
    - navigation.sections
    
    # Expand all sections
    - navigation.expand
    
    # Back to top button
    - navigation.top
    
    # Navigation path (breadcrumbs)
    - navigation.path
    
    # Instant loading (SPA-like)
    - navigation.instant
    
    # Track anchor links
    - navigation.tracking
```

### Navigation feature descriptions

**navigation.tabs**:
- Renders top-level sections as tabs
- Good for sites with multiple major sections
- Tabs appear in header below site name

**navigation.tabs.sticky**:
- Keeps tabs visible when scrolling
- Use with `navigation.tabs`

**navigation.sections**:
- Renders sections in sidebar
- Groups pages under section headings
- Better organization for larger sites

**navigation.expand**:
- Expands all collapsible sections by default
- Shows full navigation tree
- Can make sidebar long for large sites

**navigation.top**:
- Adds "Back to top" button
- Appears when scrolling down
- Improves navigation on long pages

**navigation.path**:
- Shows current location path
- Breadcrumb-style navigation
- Helps users understand site structure

**navigation.instant**:
- Enables single-page application behavior
- Faster page transitions
- No full page reloads

**navigation.tracking**:
- Updates URL with current section
- Enables deep linking to sections
- Better for sharing specific sections

### Recommended combinations

**Simple portfolio (3-5 pages)**:
```yaml
features:
  - navigation.top
  - navigation.tracking
```

**Standard portfolio (5-10 pages)**:
```yaml
features:
  - navigation.tabs
  - navigation.tabs.sticky
  - navigation.top
  - navigation.instant
```

**Large portfolio (10+ pages)**:
```yaml
features:
  - navigation.tabs
  - navigation.tabs.sticky
  - navigation.sections
  - navigation.top
  - navigation.instant
  - navigation.path
```

## Search customization

### Basic search

Enable with default settings:

```yaml
plugins:
  - search
```

### Advanced search configuration

```yaml
plugins:
  - search:
      lang: en
      separator: '[\s\-\.]+'
      pipeline:
        - stemmer
        - stopWordFilter
        - trimmer
```

### Search features

Enable search enhancements:

```yaml
theme:
  features:
    - search.highlight
    - search.share
    - search.suggest
```

**search.highlight**: Highlights search terms in results  
**search.share**: Adds share button to search  
**search.suggest**: Shows search suggestions as you type

## Table of contents

### Configure TOC behavior

```yaml
theme:
  features:
    - toc.follow
    - toc.integrate
```

**toc.follow**: Sidebar scrolls to active section  
**toc.integrate**: Integrates TOC into navigation sidebar

### TOC depth in Markdown extensions

```yaml
markdown_extensions:
  - toc:
      permalink: true
      permalink_title: Anchor link to this section
      toc_depth: 3
```

Controls how many heading levels appear in TOC.

## Social links

Add social media links to footer:

```yaml
extra:
  social:
    - icon: fontawesome/brands/github
      link: https://github.com/yourusername
      name: GitHub
    
    - icon: fontawesome/brands/linkedin
      link: https://linkedin.com/in/yourprofile
      name: LinkedIn
    
    - icon: fontawesome/brands/twitter
      link: https://twitter.com/yourhandle
      name: Twitter
    
    - icon: fontawesome/solid/envelope
      link: mailto:your.email@example.com
      name: Email
```

**Popular social icons**:
- GitHub: `fontawesome/brands/github`
- LinkedIn: `fontawesome/brands/linkedin`
- Twitter: `fontawesome/brands/twitter`
- Email: `fontawesome/solid/envelope`
- Website: `fontawesome/solid/globe`
- Medium: `fontawesome/brands/medium`

Find more icons: [FontAwesome icon search](https://fontawesome.com/search)

## Footer customization

### Copyright notice

```yaml
copyright: Copyright &copy; 2024 Your Name
```

Or with link:

```yaml
copyright: >
  Copyright &copy; 2024 <a href="https://yoursite.com">Your Name</a>
```

### Add footer links

Create `overrides/partials/footer.html`:

```html
{% extends "base.html" %}

{% block footer %}
<footer>
  <div class="md-footer-meta md-typeset">
    <div class="md-footer-meta__inner md-grid">
      <div class="md-footer-copyright">
        {{ config.copyright }}
        <br>
        <a href="/privacy">Privacy Policy</a> · 
        <a href="/terms">Terms</a>
      </div>
    </div>
  </div>
</footer>
{% endblock %}
```

Enable custom overrides:

```yaml
theme:
  name: material
  custom_dir: overrides
```

## Custom CSS

### Add custom styles

Create `docs/stylesheets/extra.css`:

```css
/* Custom color for links */
.md-typeset a {
  color: #2196F3;
}

/* Custom heading style */
.md-typeset h1 {
  font-weight: 700;
  color: #1a237e;
}

/* Custom code block style */
.md-typeset pre {
  border-radius: 8px;
}

/* Custom button style */
.md-button {
  border-radius: 20px;
}
```

Enable in `mkdocs.yml`:

```yaml
extra_css:
  - stylesheets/extra.css
```

### Common customizations

**Adjust content width**:
```css
.md-grid {
  max-width: 1200px;  /* Default is 1220px */
}
```

**Change heading colors**:
```css
.md-typeset h1 { color: #1565C0; }
.md-typeset h2 { color: #1976D2; }
.md-typeset h3 { color: #1E88E5; }
```

**Custom code block background**:
```css
.md-typeset pre {
  background-color: #1e1e1e;
}

.md-typeset code {
  background-color: #f5f5f5;
}
```

**Adjust font sizes**:
```css
.md-typeset {
  font-size: 0.9rem;  /* Slightly smaller */
}

.md-typeset h1 {
  font-size: 2rem;
}
```

## Homepage customization

### Hero section

Create custom homepage with hero:

```markdown
---
template: home.html
title: Home
---

# Your Name
## Technical Writer

I create clear, accurate documentation for developer tools and APIs.

[View Projects](projects/index.md){ .md-button .md-button--primary }
[Contact Me](contact.md){ .md-button }
```

Style hero in `extra.css`:

```css
/* Hero section */
.md-typeset h1 {
  font-size: 3rem;
  margin-bottom: 0.5rem;
}

.md-typeset h2 {
  font-size: 1.5rem;
  font-weight: 400;
  color: #666;
}

/* Hero buttons */
.md-button {
  margin-right: 1rem;
  margin-top: 1rem;
}
```

### Hide TOC on homepage

In homepage frontmatter:

```markdown
---
hide:
  - toc
---
```

Or hide navigation:

```markdown
---
hide:
  - navigation
  - toc
---
```

## Code block enhancements

### Enable syntax highlighting

```yaml
markdown_extensions:
  - pymdownx.highlight:
      anchor_linenums: true
      line_spans: __span
      pygments_lang_class: true
  - pymdownx.inlinehilite
  - pymdownx.snippets
  - pymdownx.superfences
```

### Code block features

**Line numbers**:
````markdown
```python linenums="1"
def hello():
    print("Hello, world!")
```
````

**Highlight specific lines**:
````markdown
```python hl_lines="2 3"
def hello():
    print("Line 2 is highlighted")
    print("Line 3 is highlighted")
```
````

**Code block title**:
````markdown
```python title="example.py"
def hello():
    print("Hello, world!")
```
````

## Admonition styles

### Configure admonitions

```yaml
markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
```

### Available admonition types

```markdown
!!! note
    Blue info box

!!! abstract
    Light blue summary box

!!! info
    Cyan information box

!!! tip
    Green helpful tip box

!!! success
    Green success box

!!! question
    Light green question box

!!! warning
    Orange warning box

!!! failure
    Red failure box

!!! danger
    Red critical warning box

!!! bug
    Red bug alert box

!!! example
    Purple example box

!!! quote
    Gray quotation box
```

### Collapsible admonitions

```markdown
??? note "Click to expand"
    This content is collapsed by default.

???+ tip "Expanded by default"
    This content is expanded by default but can be collapsed.
```

## Content tabs

### Enable content tabs

```yaml
markdown_extensions:
  - pymdownx.tabbed:
      alternate_style: true
  - pymdownx.superfences
```

### Usage

```markdown
=== "Python"
    ```python
    print("Hello, world!")
    ```

=== "JavaScript"
    ```javascript
    console.log("Hello, world!");
    ```

=== "Ruby"
    ```ruby
    puts "Hello, world!"
    ```
```

Useful for showing code examples in multiple languages.

## Advanced customization

### Custom templates

Create custom templates in `overrides/`:

```
overrides/
├── main.html
├── home.html
└── partials/
    ├── header.html
    └── footer.html
```

Enable:

```yaml
theme:
  name: material
  custom_dir: overrides
```

### Add custom HTML

Create `overrides/main.html`:

```html
{% extends "base.html" %}

{% block announce %}
  <div class="announcement">
    📢 New portfolio samples added! Check out the latest projects.
  </div>
{% endblock %}
```

### Custom JavaScript

Add custom scripts in `docs/javascripts/extra.js`:

```javascript
// Add analytics or custom behavior
document.addEventListener('DOMContentLoaded', function() {
  console.log('Custom JavaScript loaded');
});
```

Enable in `mkdocs.yml`:

```yaml
extra_javascript:
  - javascripts/extra.js
```

## Mobile optimization

Material is responsive by default, but you can enhance mobile experience.

### Mobile-specific CSS

```css
@media screen and (max-width: 76.1875em) {
  /* Tablet and mobile styles */
  .md-typeset {
    font-size: 0.85rem;
  }
}

@media screen and (max-width: 44.9375em) {
  /* Mobile only styles */
  .md-typeset h1 {
    font-size: 1.6rem;
  }
}
```

### Test mobile layout

```bash
# Serve and test on mobile
mkdocs serve

# View on mobile device (use your computer's IP)
# Or use browser dev tools mobile emulation
```

## Complete example configuration

Putting it all together:

```yaml
site_name: Your Name - Technical Writer
site_description: Technical writing portfolio showcasing API docs and developer guides
site_author: Your Name
site_url: https://yourusername.github.io/portfolio/

theme:
  name: material
  custom_dir: overrides
  logo: images/logo.png
  favicon: images/favicon.png
  
  palette:
    # Light mode
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: indigo
      accent: cyan
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    
    # Dark mode
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: indigo
      accent: cyan
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
  
  font:
    text: Inter
    code: Fira Code
  
  features:
    - navigation.tabs
    - navigation.tabs.sticky
    - navigation.sections
    - navigation.top
    - navigation.instant
    - navigation.tracking
    - search.highlight
    - search.share
    - search.suggest
    - toc.follow

nav:
  - Home: index.md
  - About: about.md
  - Projects:
      - Overview: projects/index.md
      - API Documentation: projects/api-docs.md
      - CLI Reference: projects/cli-reference.md
  - Samples:
      - Overview: samples/index.md
      - Getting Started: samples/getting-started.md
  - Contact: contact.md

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.inlinehilite
  - pymdownx.tabbed:
      alternate_style: true
  - toc:
      permalink: true

plugins:
  - search:
      lang: en

extra:
  social:
    - icon: fontawesome/brands/github
      link: https://github.com/yourusername
    - icon: fontawesome/brands/linkedin
      link: https://linkedin.com/in/yourprofile
    - icon: fontawesome/solid/envelope
      link: mailto:your.email@example.com

extra_css:
  - stylesheets/extra.css

extra_javascript:
  - javascripts/extra.js

copyright: Copyright &copy; 2024 Your Name
```

## Testing customizations

### Preview changes

```bash
mkdocs serve
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) to see changes live.

### Check different viewports

Use browser dev tools to test:
- Desktop (1920x1080)
- Tablet (768x1024)
- Mobile (375x667)

### Validate configuration

```bash
mkdocs build --strict
```

This catches configuration errors before deployment.

## Common customization mistakes

### Mistake 1: Too many colors

Problem: Using too many different colors

Solution: Stick to primary and accent colors, let Material handle the rest

### Mistake 2: Unreadable contrast

Problem: Poor color contrast makes text hard to read

Solution: Use Material's built-in colors or test contrast ratios

### Mistake 3: Overriding too much

Problem: Heavy customization breaks Material theme features

Solution: Use built-in options first, custom CSS sparingly

### Mistake 4: Not testing mobile

Problem: Customizations look good on desktop, broken on mobile

Solution: Always test responsive behavior

### Mistake 5: Forgetting accessibility

Problem: Custom colors or fonts hurt accessibility

Solution: Maintain contrast ratios, use readable fonts

## Resources

- [Material for MkDocs documentation](https://squidfunk.github.io/mkdocs-material/)
- [Material Design color system](https://material.io/design/color/)
- [Google Fonts](https://fonts.google.com/)
- [FontAwesome icons](https://fontawesome.com/search)
- [WebAIM contrast checker](https://webaim.org/resources/contrastchecker/)

## Related documentation

- [Tutorial Step 1: Setup environment](../tutorial/step-1-setup.md)
- [Site structure reference](site-structure.md)
- [Troubleshooting guide](../troubleshooting.md)
