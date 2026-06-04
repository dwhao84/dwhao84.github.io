# Dawei Hao — iOS Developer Portfolio & Blog

Personal website built with **MkDocs + Material for MkDocs**. Features a tech blog synced from Medium, and a project showcase auto-generated from the App Store API.

**Live site**: [blog.dawei84.com](https://blog.dawei84.com)

## Tech Stack

- **MkDocs** + **Material for MkDocs** — static site generator
- **Python scripts** — auto-generate homepage (Medium RSS) & projects page (App Store API)
- **GitHub Actions** — CI/CD, auto build & deploy to GitHub Pages
- **giscus** — comment system powered by GitHub Discussions

## Project Structure

```
mkdocs.yml                  # MkDocs configuration
docs/
  index.md                  # Homepage (auto-generated)
  about.md                  # About me
  projects.md               # App Store projects (auto-generated)
  experience.md             # Work experience
  contact.md                # Contact
  blog/
    posts/                  # Blog posts (Markdown)
    images/                 # Blog photos and screenshots
    .authors.yml            # Author info
  stylesheets/
    custom.css              # Custom styling
templates/
  blog-post.md              # Blog post template
overrides/
  partials/
    footer.html             # Custom footer
    comments.html           # giscus integration
scripts/
  new_blog_post.py          # Create a new blog post from template
  generate_index.py         # Fetch Medium RSS + App API -> index.md
  generate_projects.py      # Fetch App API -> projects.md
```

## Local Development

```bash
# Create virtual environment & install
python3 -m venv .venv
source .venv/bin/activate
pip install mkdocs-material

# Generate dynamic pages
python scripts/generate_index.py
python scripts/generate_projects.py

# Start dev server
mkdocs serve
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Writing a New Blog Post

Use the helper script:

```bash
python3 scripts/new_blog_post.py "Article Title"
```

Or specify a slug:

```bash
python3 scripts/new_blog_post.py "Swift 6 LocalizedStringKey Notes" --slug swift6-localized-string-key
```

The script creates a post in `docs/blog/posts/` and adds it to the Blog nav in `mkdocs.yml`.

Post format:

```markdown
---
date: 2026-06-04
authors:
  - dawei
tags:
  - Swift
---

# Post Title

Summary text...

<!-- more -->

Full content...
```

More details are in [BLOGGING.md](BLOGGING.md).

## Adding Photos to Blog Posts

Put blog photos or screenshots in:

```text
docs/blog/images/
```

Then reference them from a post in `docs/blog/posts/`:

```markdown
![Screenshot description](../images/example.jpg)
```

For a centered image with caption and responsive width:

```html
<figure>
  <img src="../images/example.jpg" alt="Screenshot description" style="max-width:720px;width:100%;border-radius:12px;">
  <figcaption>Screenshot description</figcaption>
</figure>
```

Image guidelines:

- Use lowercase English filenames with hyphens, e.g. `swiftui-layout-debug.jpg`
- Use `.jpg` or `.webp` for photos, `.png` for screenshots
- Keep each image under 1 MB when possible

## Deployment

Push to `main` branch triggers GitHub Actions:

1. `generate_index.py` — fetches latest Medium articles + top 3 apps
2. `generate_projects.py` — fetches all apps from App Store API
3. `mkdocs gh-deploy --force` — builds & deploys to `gh-pages` branch

## Contact

- **GitHub**: [@dwhao84](https://github.com/dwhao84)
- **Medium**: [@dwsamurai84_dev](https://medium.com/@dwsamurai84_dev)
- **Email**: dwsamurai84@gmail.com
