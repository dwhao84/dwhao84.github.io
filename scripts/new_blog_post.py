#!/usr/bin/env python3
"""
Create a new blog post from templates/blog-post.md.

Usage:
    python3 scripts/new_blog_post.py "Article Title"
    python3 scripts/new_blog_post.py "Article Title" --slug custom-slug
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_PATH = ROOT / "templates" / "blog-post.md"
POSTS_DIR = ROOT / "docs" / "blog" / "posts"
MKDOCS_PATH = ROOT / "mkdocs.yml"


def slugify(title: str) -> str:
    slug = title.lower().strip()
    slug = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", slug)
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug or "new-post"


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a new blog post.")
    parser.add_argument("title", help="Post title")
    parser.add_argument("--slug", help="URL/file slug, e.g. swift6-notes")
    args = parser.parse_args()

    today = dt.date.today().isoformat()
    slug = slugify(args.slug or args.title)
    post_path = POSTS_DIR / f"{today}-{slug}.md"

    if post_path.exists():
        raise SystemExit(f"Post already exists: {post_path.relative_to(ROOT)}")

    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    content = template.replace("YYYY-MM-DD", today, 1)
    content = content.replace("# 文章標題", f"# {args.title}", 1)

    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    post_path.write_text(content, encoding="utf-8")

    relative_post = post_path.relative_to(ROOT)
    nav_path = post_path.relative_to(ROOT / "docs").as_posix()
    add_post_to_nav(args.title, nav_path)

    print(f"Created: {relative_post}")
    print(f"Updated: {MKDOCS_PATH.relative_to(ROOT)}")
    print("Next: edit the post, run `.venv/bin/mkdocs build --strict`, then commit and push.")


def add_post_to_nav(title: str, nav_path: str) -> None:
    lines = MKDOCS_PATH.read_text(encoding="utf-8").splitlines()
    nav_entry = f"      - {title}: {nav_path}"

    if nav_entry in lines:
        return

    try:
        blog_index = lines.index("  - Blog:")
    except ValueError as exc:
        raise SystemExit("Could not find `  - Blog:` in mkdocs.yml") from exc

    insert_at = blog_index + 1
    while insert_at < len(lines):
        line = lines[insert_at]
        if line.startswith("  - ") and not line.startswith("      - "):
            break
        insert_at += 1

    lines.insert(insert_at, nav_entry)
    MKDOCS_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
