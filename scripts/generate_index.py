"""
從 Medium RSS 取得最新文章，自動生成首頁 index.md。
用法: python scripts/generate_index.py
"""

import json
import re
import urllib.request
import xml.etree.ElementTree as ET
from html import unescape

MEDIUM_RSS = "https://medium.com/feed/@dwsamurai84_dev"
APP_API = "https://sync-artist-app.zeabur.app/api/apps"
MAX_ARTICLES = 10
MAX_APPS = 3


def fetch_medium_articles():
    req = urllib.request.Request(MEDIUM_RSS, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as resp:
        tree = ET.parse(resp)
    root = tree.getroot()

    ns = {"content": "http://purl.org/rss/1.0/modules/content/"}
    articles = []
    for item in root.findall(".//item"):
        title = unescape(item.findtext("title", "")).strip()
        link = item.findtext("link", "")
        pub_date = item.findtext("pubDate", "")
        date_short = format_date(pub_date)

        encoded = item.findtext("content:encoded", "", ns)
        thumbnail = extract_first_image(encoded)
        summary = extract_summary(encoded)

        if title and link:
            articles.append({
                "title": title,
                "link": link,
                "date": date_short,
                "summary": summary,
                "thumbnail": thumbnail,
            })
    return articles[:MAX_ARTICLES]


def extract_first_image(html):
    match = re.search(r'<img[^>]+src="([^"]+)"', html)
    if match:
        url = match.group(1)
        url = re.sub(r'/max/\d+/', '/max/400/', url)
        return url
    return ""


def extract_summary(html, max_len=120):
    text = re.sub(r'<[^>]+>', '', html)
    text = unescape(text).strip()
    text = re.sub(r'\s+', ' ', text)
    if len(text) > max_len:
        return text[:max_len] + "..."
    return text


def format_date(pub_date):
    parts = pub_date.split()
    if len(parts) >= 4:
        months = {
            "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
            "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
            "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12",
        }
        day = parts[1].zfill(2)
        month = months.get(parts[2], "01")
        year = parts[3]
        return f"{year}/{month}/{day}"
    return ""


def fetch_top_apps():
    req = urllib.request.Request(APP_API, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read())
    apps = data["data"]
    apps.sort(
        key=lambda x: int(m.group(1)) if (m := re.search(r"/id(\d+)", x.get("trackViewUrl", ""))) else 0,
        reverse=True,
    )
    return apps[:MAX_APPS]


def generate_markdown(articles, apps):
    md = """---
title: 首頁
description: iOS 工程師 — 專精於 Swift 開發
hide:
  - navigation
  - toc
---

<div class="hero-section">
<img src="https://github.com/dwhao84.png" alt="Dawei" class="hero-avatar">
<div class="hero-text">
<h1 class="hero-title"><strong>Hi, I'm Dawei</strong></h1>

iOS 工程師，擅長 Swift・UIKit・SwiftUI。<br>目前任職於租車公司，負責內部 App 開發與維護。<br>同時獨立開發並上架多款 App 至 App Store。

<div style="margin-top:1rem;">
<a href="about/" class="btn-outline">關於我</a> <a href="projects/" class="btn-outline">專案</a>
</div>
</div>
</div>

---

## 最新文章

<div class="article-grid">
"""
    for a in articles:
        title = a["title"]
        link = a["link"]
        date = a["date"]
        summary = a["summary"]
        thumb = a["thumbnail"]

        md += f'<a href="{link}" class="article-card" target="_blank">\n'
        if thumb:
            md += f'<img src="{thumb}" class="article-card-thumb" alt="">\n'
        md += f'<div class="article-card-body">\n'
        md += f'<div class="article-card-text">\n'
        md += f'<h3>{title}</h3>\n'
        md += f'<p>{summary}</p>\n'
        md += f'</div>\n'
        md += f'<div class="article-card-meta">\n'
        md += f'<span class="article-card-date">{date}</span>\n'
        md += f'<span class="article-card-readmore">閱讀全文 →</span>\n'
        md += f'</div>\n'
        md += f'</div>\n'
        md += f'</a>\n\n'

    md += f'</div>\n\n'
    md += f'<a href="https://medium.com/@dwsamurai84_dev" class="btn-outline" target="_blank">更多文章</a>\n'

    md += """
---

## 個人專案

"""
    md += '<div class="app-grid">\n\n'
    for app in apps:
        name = app["trackName"]
        icon_url = app.get("artworkUrl512", "")
        store_url = app.get("trackViewUrl", "")
        desc = app.get("description", "").strip().split("\n")[0]
        if len(desc) > 80:
            desc = desc[:80] + "..."

        md += f'<a href="{store_url}" class="app-card" target="_blank">\n'
        md += f'<img src="{icon_url}" alt="{name}" class="app-card-icon">\n'
        md += f'<div class="app-card-body">\n'
        md += f'<div class="app-card-text">\n'
        md += f'<h3>{name}</h3>\n'
        md += f'<p>{desc}</p>\n'
        md += f'</div>\n'
        md += f'<span class="article-card-readmore">App Store →</span>\n'
        md += f'</div>\n'
        md += f'</a>\n\n'

    md += '</div>\n\n'
    md += '<a href="projects/" class="btn-outline">查看全部專案</a>\n'

    md += """
---

## 聯絡方式

- **Email**: [dwsamurai84@gmail.com](mailto:dwsamurai84@gmail.com)
- **GitHub**: [dwhao84](https://github.com/dwhao84)
- **Medium**: [@dwsamurai84_dev](https://medium.com/@dwsamurai84_dev)
"""
    return md


def main():
    articles = fetch_medium_articles()
    apps = fetch_top_apps()
    md = generate_markdown(articles, apps)
    output_path = "docs/index.md"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"已生成 {output_path}，共 {len(articles)} 篇文章、{len(apps)} 個精選 App")


if __name__ == "__main__":
    main()
