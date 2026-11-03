# Kitchen AO 網頁及文章設計規範

> 新頁面、Blog、Landing page 一律跟從。最後更新：2026-11-03

## 標題（H2）
- **不用左邊金色直線**（border-left）。
- 改用**標題上方的金色短線**：寬 46px、高 4px、圓角 3px、顏色 #C8A24A，標題 padding-top 16px。

```css
h2{position:relative;padding:16px 0 0;border:0;}
h2:before{content:"";position:absolute;left:0;top:0;width:46px;height:4px;border-radius:3px;background:#C8A24A;}
```

## 文案
- 書面語、香港用詞；不用「——」；不用廣東話口語字（揀、唔、嘅、咗、睇、嚟、今個、定）。

## 產品推介
- 只推介有售及有圖片的產品；停售或沒有圖片的不放。
- 場景頁：先推介套餐或餐盒，再推介單點，最後提及歡迎度身訂製；適合的場景加素食套餐。
- 產品卡圖片不裁切（object-fit:contain，底色補位），單點卡不顯示份量（例如 4 磅）。
