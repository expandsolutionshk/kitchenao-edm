# Kitchen AO 項目筆記（備份：2026-11-11）

> 用途：新 session 開始時先讀此檔，了解工作規則、檔案位置及未完成事項。
> 設計規範另見 `STYLE-GUIDE.md`。

## 1. 工作規則（必須遵守）

- 回覆用廣東話，簡潔。網頁／文章文案用書面語＋香港用詞。
- 不用「——」；網頁文案不用口語字（揀、唔、嘅、咗、睇、嚟、今個、定）。
- 不可記錄任何客戶資料。
- 下載檔案要先問（每次）。不連結未發佈的 blog。不畫／不複製任何 logo。交付物不提競爭對手名稱。
- **每次更新檔案都要給連結及資料夾路徑。**
- 每次提出 design option，都要提醒：參考網站包括 **Four Seasons Sydney**（https://www.fourseasons.com/sydney/）。
- 相片：不用帶其他品牌 logo 的人物相；Pexels 免費圖可作場景；不推薦已停售或無圖的產品。
- 設計：不用左邊金色直線；H2 上方金色短線（46×4px #C8A24A）；產品卡用正方形 cover 裁切。

## 2. 技術規則（WordPress / Lafka / WPBakery）

- GitHub Pages：`https://expandsolutionshk.github.io/kitchenao-edm/`，用戶以 GitHub Desktop push。
- WP 頁面用 WPBakery **Raw HTML**；首頁 Raw HTML 可用 `<script>` 及 `onclick`。
- **WAF**：擋 `$_POST`；分類描述擋 `<script>`、`<style>`、`onclick`；WPCode **HTML Snippet** 含 `<script>` 會被擋 → 用 **JavaScript Snippet** 或 PHP enqueue。
- **附加 CSS 不可出現 `<`**（連註解都不可），否則之後內容被截走；註解只用 ASCII。
- 中英雙語：`<span class="ao-zh" data-no-translation>` / `<span class="ao-en" data-no-translation>`，CSS 按 `html[lang^="en"]` 隱藏，JS 用 `document.currentScript.parentNode` 移除另一語言。
- 全闊 section：`width:100vw;margin-left:calc(50% - 50vw)` ＋ `body:has(.x){overflow-x:hidden}`；排除 row padding 要用 `body.home .vc_row.wpb_row:not(.vc_inner):has(.x)`。
- Chrome MCP：視窗隱藏（innerWidth 0），只能讀 DOM／代碼，不能量版面；輸出含 `?=&` 會被擋。

## 3. 檔案位置

| 項目 | Repo 路徑 | 備註 |
|---|---|---|
| 附加 CSS（最新 v4.8） | `site-fixes/additional-css-full-v4.css` | 複製頁：`Downloads/複製-完整附加CSS-v4.html` |
| Header JS（v4，WPCode JS Snippet） | `site-fixes/header-offset.js` | 複製頁：`Downloads/複製-WPCode-header-JS.html`；**live 仍是舊版，待用戶更新** |
| 首頁 Hero（FS1 賣點列） | `homepage-hero/hero-rawhtml-no-halloween.html` | 複製頁：`Downloads/homepage-hero/複製-首頁Hero代碼.html` |
| 首頁 Blog 段 v5 | `homepage-hero/blog-section-rawhtml.html` | `Downloads/複製-首頁Blog代碼.html` |
| 首頁激光打印 FS3 v5 | `homepage-hero/laser-food/laser-fs3-rawhtml.html` | `Downloads/複製-首頁激光打印食物代碼.html` |
| 首頁合作機構 v4 | `homepage-hero/partners-rawhtml.html` | `Downloads/複製-首頁合作機構代碼.html` |
| 優惠訊息條 v2 | `homepage-hero/member-offer/member-bar-v2-rawhtml.html` | `Downloads/複製-優惠訊息條代碼.html` |
| 活動場合／熱門套餐 | `homepage-hero/occasion-sets/build.py` | |
| 18404 公司到會頁 | `wp-pages/en/18404-corporate-catering-hk/build_corp.py` | |
| 雙 11 EDM | `1111-2026/build.py` → `email.html` | KV：`1111-2026/make_kv3.py` |
| 雙 11 圖片 | `1111-2026/img/` | `d11-kv.jpg`（C2 無膠囊）、`d11-rewards.jpg`、會員贈品圖 |
| 雙 11 KV 來源相 | `1111-2026/src/` | make_kv3.py 直接讀此資料夾 |
| Downloads 交付物備份 | `_backup/downloads-2026-11-11/` | 複製頁、預覽頁等 |

## 4. 雙 11（2026）最終內容

- 推廣期：2026-11-11 至 11-17（一連七天）；優惠碼 **DOUBLE11**；自動套用：`https://aoaodelivery.com/?wdr_coupon=DOUBLE11`
- 四重賞：滿 $1,100 全單 11% OFF；滿 $1,500 送 A1600 日式雞皮餃子（10 件，原價 $198）；滿 $2,200 再加送 A1500 避風塘海鮮豆腐（10 件，$178）；滿 $3,000 再加送 A0500 蜜蜜燒雞翼（10 件，$188）。
- 會員優惠照常：多買多賞（每滿 $1,500／$2,200／$3,000 送薯片／冷泡茶／紅白酒，無封頂）；舊會員上單每 $2,000 減 $100。
- EDM 次序：KV（C2）→ 優惠券卡（Design 2）→ 多謝語＋按鈕 → 四重賞圖 → 會員優惠兩張圖 → 總覽＋條款 → 頁尾。
- 未確認：DOUBLE11 是否已在 WooCommerce 設定（最低 $1,100）；贈品如何加入訂單；`?wdr_coupon` 是否生效；三款小食是否每款 10 件；`/1111/` landing 仍是舊「預購三重賞」內容。

## 5. 待辦（未完成）

- Header JS v4 未上 live（語言掣未移入金色條、仍顯示 ZH）。
- 首頁：Hero 相有其他品牌 logo（ServeAndWow 圍裙、McLaren 牌）要換；熱門套餐與 WIN95 之間有空 inner row；WIN95 圖仍有黑白叉燒。
- 首頁手機版各段左邊對齊待用戶截圖確認。
- SEO：重複節日產品（Halloween／中秋 vs Gourmet Set）；55 頁冇 meta description；82 頁有兩個 H1；首頁 schema 被標成 Article；sitemap 含 checkout／cart／my-account；冇頁面快取（TTFB ~1.3 秒）；preloader；兩個 jQuery。
- CLS：11 月 2 日已修 header（cls-fix.css）及派對分類快選區（伺服器版）；GSC 約 12 月初反映；可停用舊 `party-quickpick.js` snippet。
- 聖誕：landing page 原定 11-10 前上線（已過期）；需確認 2026 聖誕套餐是否上架、有否早鳥。策略文件：Claude Docs「Kitchen AO 聖誕頁面 SEO 策略 2026」。
- 18404：替換暫用相片及假評語；Pexels 圖上傳到 WP 媒體庫；產品卡 v2 選項未定。
- 到會推介（REC）頁需重寫以配合「香港到會推介」KW。
