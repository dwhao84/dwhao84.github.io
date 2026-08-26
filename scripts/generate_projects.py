"""
從 API 取得 App Store 上架的 App 資料，自動生成 projects.md。
用法: python scripts/generate_projects.py
"""

import json
import re
import urllib.error
import urllib.request

API_URL = "https://developer-category-api.dawei84.com/api/dawei"
API_URL_FALLBACK = (
    "https://app-store-developer-catalog-api.dwsamurai84.workers.dev/api/dawei"
)

HEADER = """---
title: 專案
description: 我的 iOS App 作品集 — 資料自動同步自 App Store
---

# 專案

"""


def fetch_apps():
    try:
        data = fetch_app_data(API_URL)
    except urllib.error.HTTPError as error:
        if error.code != 403:
            raise
        data = fetch_app_data(API_URL_FALLBACK)
    return data["data"]


def fetch_app_data(url):
    req = urllib.request.Request(
        url,
        headers={"Accept": "application/json", "User-Agent": "Mozilla/5.0"},
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


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
    apps = fetch_apps()
    md = generate_markdown(apps)
    output_path = "docs/projects.md"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"已生成 {output_path}，共 {len(apps)} 個 App")


if __name__ == "__main__":
    main()
