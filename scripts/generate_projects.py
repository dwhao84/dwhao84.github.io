"""
從 API 取得 App Store 上架的 App 資料，自動生成 projects.md。
用法: python scripts/generate_projects.py
"""

import re
from app_data import ROOT, atomic_write, load_apps, preserve_existing

HEADER = """---
title: 專案
description: 我的 iOS App 作品集 — 資料自動同步自 App Store
---

# 專案

"""


def fetch_apps():
    return load_apps()


def format_price(price):
    if price == 0:
        return "免費"
    return f"NT$ {int(price)}"


def truncate_description(desc, max_chars=150):
    first_line = desc.strip().split("\n")[0].strip()
    if len(first_line) > max_chars:
        return first_line[:max_chars] + "..."
    return first_line


def generate_markdown(apps):
    def extract_app_id(app):
        match = re.search(r'/id(\d+)', app.get("trackViewUrl", ""))
        return int(match.group(1)) if match else 0

    apps.sort(key=extract_app_id, reverse=True)

    md = HEADER
    md += '<div class="project-grid">\n\n'
    for app in apps:
        name = app["trackName"]
        desc = truncate_description(app.get("description", ""))
        icon_url = app.get("artworkUrl512", "")
        store_url = app.get("trackViewUrl", "")
        price = format_price(app.get("price", 0))

        md += f'<a href="{store_url}" class="project-card" target="_blank">\n'
        md += f'<img src="{icon_url}" alt="{name}" class="project-card-icon">\n'
        md += f'<div class="project-card-body">\n'
        md += f'<div class="project-card-text">\n'
        md += f'<h3>{name}</h3>\n'
        md += f'<p>{desc}</p>\n'
        md += f'</div>\n'
        md += f'<div class="project-card-meta">\n'
        md += f'<span class="project-card-price">{price}</span>\n'
        md += f'<span class="article-card-readmore">App Store →</span>\n'
        md += f'</div>\n'
        md += f'</div>\n'
        md += f'</a>\n\n'

    md += '</div>\n\n'
    return md


def main():
    output_path = ROOT / "docs/projects.md"
    apps = fetch_apps()
    if apps is None:
        preserve_existing(output_path, "project-card")
        return
    md = generate_markdown(apps)
    atomic_write(output_path, md)
    print(f"已生成 {output_path}，共 {len(apps)} 個 App")


if __name__ == "__main__":
    main()
