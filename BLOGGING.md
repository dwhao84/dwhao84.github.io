# Blog Writing Workflow

這個專案的文章放在 `docs/blog/posts/`。

## 建立新文章

使用腳本建立文章：

```bash
python3 scripts/new_blog_post.py "文章標題"
```

也可以指定 slug：

```bash
python3 scripts/new_blog_post.py "Swift 6 LocalizedStringKey 筆記" --slug swift6-localized-string-key
```

腳本會：

- 從 `templates/blog-post.md` 複製文章格式
- 自動填入今天日期
- 建立 `docs/blog/posts/YYYY-MM-DD-slug.md`
- 自動把文章加到 `mkdocs.yml` 的 Blog 導覽列

## 文章格式

每篇文章需要保留 front matter：

```yaml
---
date: 2026-06-04
authors:
  - dawei
tags:
  - Swift
  - iOS
---
```

`<!-- more -->` 以上的內容會作為摘要使用，建議放在第一段後面。

## 發布流程

1. 建立文章。
2. 編輯文章內容。
3. 本地檢查：

```bash
.venv/bin/mkdocs build --strict
```

4. Commit 並 push 到 `main` 後，GitHub Actions 會自動部署。
