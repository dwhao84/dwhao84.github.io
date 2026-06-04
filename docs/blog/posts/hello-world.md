---
date: 2026-06-04
authors:
  - dawei
tags:
  - Swift
  - 學習筆記
---

# 我的技術部落格開張了

歡迎來到我的技術部落格！這裡會記錄我在 iOS 開發學習過程中的筆記和心得。

<!-- more -->

## 為什麼要寫部落格？

寫部落格對我來說有幾個好處：

1. **整理思緒** — 把學到的東西寫下來，可以幫助自己更深入地理解
2. **建立知識庫** — 以後遇到類似問題可以回來查閱
3. **分享與交流** — 希望我的筆記也能幫助到其他學習者

## 會寫什麼內容？

主要會涵蓋：

- Swift 語法與最佳實踐
- UIKit 開發技巧
- Core Data 使用心得
- API 串接經驗
- 開發中遇到的問題與解決方案

## 範例：Swift 的 Optional 用法

```swift
// Optional Binding
var name: String? = "DaWei"

if let unwrappedName = name {
    print("Hello, \(unwrappedName)!")
}

// Guard Let
func greet(name: String?) {
    guard let name = name else {
        print("No name provided")
        return
    }
    print("Hello, \(name)!")
}
```

!!! tip "小提示"
    使用 `guard let` 可以讓程式碼更清楚，特別是在函式開頭做參數驗證的時候。

期待在這裡和大家分享更多學習心得！
