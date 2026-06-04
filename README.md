# Dawei Hao — iOS Developer Portfolio & Blog

Personal website built with **MkDocs + Material for MkDocs**. Features a tech blog synced from Medium, and a project showcase auto-generated from the App Store API.

**Live site**: [dwhao84.github.io](https://dwhao84.github.io)

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
    .authors.yml            # Author info
  stylesheets/
    custom.css              # Custom styling
overrides/
  partials/
    footer.html             # Custom footer
    comments.html           # giscus integration
scripts/
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

Create a new `.md` file in `docs/blog/posts/`:

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

## Deployment

Push to `main` branch triggers GitHub Actions:

1. `generate_index.py` — fetches latest Medium articles + top 3 apps
2. `generate_projects.py` — fetches all apps from App Store API
3. `mkdocs gh-deploy --force` — builds & deploys to `gh-pages` branch

## Contact

- **GitHub**: [@dwhao84](https://github.com/dwhao84)
- **Medium**: [@dwsamurai84_dev](https://medium.com/@dwsamurai84_dev)
- **Email**: dwsamurai84@gmail.com
