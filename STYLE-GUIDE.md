# Kitchen AO 網頁及文章設計規範

> 新頁面、Blog、Landing page 一律跟從。最後更新：2026-11-04

## 標題（H2）
- **不用左邊金色直線**（border-left）。
- 改用**標題上方的金色短線**：寬 46px、高 4px、圓角 3px、顏色 #C8A24A，標題 padding-top 16px。

```css
h2{position:relative;padding:16px 0 0;border:0;}
h2:before{content:"";position:absolute;left:0;top:0;width:46px;height:4px;border-radius:3px;background:#C8A24A;}
```

## 提示框、引言、卡片
- **不用左邊金色直線**（border-left 色條）的 AI 風格設計，任何提示框、引言、備註、卡片都不用。
- 可用：黑底置中區塊（EDM 風格）、米色卡＋圓形 icon、虛線優惠券框＋頂部標籤、頂部金色短線。

## 文案
- 書面語、香港用詞；不用「——」；不用廣東話口語字（揀、唔、嘅、咗、睇、嚟、今個、定）。

## 產品推介
- 只推介有售及有圖片的產品；停售或沒有圖片的不放。
- 場景頁：先推介套餐或餐盒，再推介單點，最後提及歡迎度身訂製；適合的場景加素食套餐。
- 產品卡圖片統一填滿正方形（object-fit:cover，置中裁切），單點卡不顯示份量（例如 4 磅）。（2026-11-04 起取代舊的「不裁切」規則）

## 已選定風格（18404 公司到會，2026-11-04）
- 方案 C「Monochrome Bands 黑白分段」：全幅黑色開場段 → 白色段大圓形相片 tab（已選加金色外圈）→ 米白段內容。
- 字體沿用網站原有字體，不用襯線字。顏色只用黑 #141414、白、米白 #F7F5F0、金 #C8A24A。
- 不用動畫（hover 輕微放大除外）。

## 設計參考網站（建議 template、section 時優先參考）
| 網站 | 用途 | 可借用重點 |
|---|---|---|
| [Wolfgang Puck Catering](https://wolfgangpuckcatering.com/) | 整頁版型 | 全幅大相 Hero、大標題、服務 tab 切換大圖＋故事文字 |
| [Pret Catering](https://www.pret.com/en-US/catering) | 整頁版型、賣點 | 3 個 icon 賣點、餐單／指南下載卡、方形相片分類格 |
| [agnès b. CAFÉ & FLEURISTE](https://cafefleuriste.agnesb.com.hk/) | 簡約風格 | 大量留白、英文小標（Explore／Discover）、幼線分隔、直身相片格 |
| [Nourish by Eileen](https://nourishbyeileen.framer.website/)（[Services](https://nourishbyeileen.framer.website/services)） | 內容排版 | 左大圖右文字、Signature dishes 相片 slider、承諾清單、全幅相片 CTA 橫幅 |
| [Chanterelle Catering](https://www.chanterellecateringcompany.com/)（[Corporate lunch](https://www.chanterellecateringcompany.com/corporate-lunch-catering)、[Team meeting](https://www.chanterellecateringcompany.com/team-meeting-catering)、[Office breakfast](https://www.chanterellecateringcompany.com/office-breakfast-catering)） | 文案筆法、選單 | 每個活動一句簡介、3 張賣點卡、重點列（送貨／人數／起價）、By occasion ＋ Where we deliver 兩欄 |
| [Jai Ambey Caterers](https://jaiambaycaterers.com/) | Section 及 icon | 服務 icon 卡、活動相片分類 tab（不跟動畫） |
| [Curfew Coffee](https://www.curfew.coffee/) | 宣言橫幅 | 深色相片底、左邊大字宣言、下面一句說明 |
| [Four Seasons Sydney](https://www.fourseasons.com/sydney/) | 高級感段落（Hero 賣點、特色體驗） | 大圖加細圖疊放、金色英文小標、幼線分隔、幼身標題、文字底線連結、1 / N 輪播計數。每次提出設計方案都要提醒有此參考 |

使用方法：建議新設計時，先說明參考哪個網站的哪個部分，再按本規範（黑金白、無左邊直線、書面語）調整。

## 可重用元件
- **相片宣言橫幅（ao-mission）**：全幅深色相片底，左邊大標題（網站原有字體、粗 900、部分金色），英文口號可做第一行大字（例如 We Serve, We WOW.），下面一句說明，可選按鈕。程式見 18404 `build_corp.py` 的 `mission()`，其他頁面沿用時只換文字及相片。
- **左文右圖大標題段（ao-onsite2）**：兩行大標題（第一行部分金色）＋說明＋✓ 清單＋一黑一白框圓角掣，右邊單張相貼邊填滿。
