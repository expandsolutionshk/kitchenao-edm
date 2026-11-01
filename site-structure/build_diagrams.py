# -*- coding: utf-8 -*-
# 產生 index.html（Mermaid 架構圖）。每個格子都顯示完整 URL，並可點擊打開。
import json, pathlib
B = 'https://aoaodelivery.com'
HERE = pathlib.Path(__file__).parent

TAGS = {'/delivery/': '支援頁', '/foodbook/': '支援頁', '/常見問題/': '支援頁', '/contacts/': '支援頁', '/catering-quote-enquiry/': '支援頁（報價）',
        '/about-kitchenao/': '信任頁', '/客人好評/': '信任頁', '/合作伙伴/': '信任頁', '/精選圖庫/': '信任頁',
        '/corporate-catering-hk/': '服務頁', '/business-event/': '服務頁', '/hong-kong-catering-recommendation/': '服務頁', '/服務概覽/': '服務頁',
        '/飲品及雞尾酒服務/': '服務頁', '/客製化紀念品訂製服務/': '服務頁', '/mooncake-preorder/': '推廣頁', '/地區到會分類/': '地區 Hub',
        '/boat-trip-bldg/': '舊 Landing 頁', '/partyfood-bldg/': '舊 Landing 頁', '/snacks-bldg/': '舊 Landing 頁', '/blog/': 'Blog 首頁',
        '/商務餐盒/': '舊產品頁', '/高級餐盒-2/': '舊產品頁', '/員工膳食餐盒/': '舊產品頁', '/皇家小食盒/': '舊產品頁', '/舌尖上的餐桌-頂級美食一盒盛/': '舊產品頁',
        '/en/corporate-catering-hk/': '服務頁（英文）', '/en/delivery/': '支援頁（英文）', '/sample-page/': '問題頁', '/ba620e385336-htm/': '問題頁（被入侵）', '/66695d0f41db-htm/': '問題頁（被入侵）', '/': '首頁'}
def page_tag(path, name):
    if path in TAGS: return TAGS[path]
    if not path: return '分組' if name in ('港島', '九龍', '新界') else '計劃中'
    if path.startswith('/catering/'): return '場景 Landing 頁'
    if path.startswith('/catering-'): return '地區頁'
    if path.startswith('/product-category/'): return '產品分類頁'
    if path.startswith('/product/'): return '產品頁'
    if path.startswith('/blog/tag/'): return 'Blog Tag 頁'
    if path.startswith('/blog/'): return 'Blog 文章'
    if path.startswith('/tag/'): return '舊 Tag（已 301）'
    return '頁面'
def N(i, name, path='', cls='ok'):
    return dict(id=i, name=name, url=(B + path) if path else '', cls=cls, tag=page_tag(path, name))

D = {}
# ---------- 全站總覽 ----------
D['全站總覽'] = dict(dir='LR', nodes=[
 N('H', '首頁', '/'), N('C', '場景總覽（新）', '/catering/', 'new'),
 N('B1', '船河', '/catering/boat-party/', 'new'), N('B2', '素食', '/catering/vegetarian/', 'new'), N('B3', '生日會', '/catering/birthday-party/', 'new'),
 N('B4', '公司午餐', '/catering/corporate-lunch/', 'new'), N('B5', '學校飯盒', '/catering/school-lunch-box/', 'new'), N('B6', '中秋節', '/catering/mid-autumn/', 'new'),
 N('B7', '萬聖節', '/catering/halloween/', 'new'), N('B8', '訂製食物', '/catering/custom-printed-food/', 'new'),
 N('B9', '野餐', '/catering/picnic/', 'new'), N('B10', '聖誕節', '/catering/christmas/', 'new'),
 N('P1', '派對套餐', '/product-category/party/'), N('P2', '人數選餐', '/product-category/party-set-by-people/'), N('P3', '單點', '/product-category/a-la-carte/'),
 N('P4', '商務活動', '/product-category/商務活動/'), N('P5', '配菜', '/product-category/配菜/'), N('P6', '派對用品', '/product-category/party-supplies/'),
 N('P7', '中秋套餐（slug 帶年份）', '/product-category/中秋佳節團圓套餐-2026/', 'old'), N('P8', '萬聖節狂嘩套餐', '/product-category/halloween-set/'), N('P9', 'Chill一下野餐盒', '/product-category/party/chill-box/'),
 N('BL', 'Blog（13 篇）', '/blog/'), N('D', '地區 hub（要補內容）', '/地區到會分類/', 'old'),
 N('S1', '送貨需知', '/delivery/'), N('S2', '購買流程', '/foodbook/'), N('S3', '常見問題', '/常見問題/'), N('S4', '聯絡我們', '/contacts/'), N('S5', '報價查詢', '/catering-quote-enquiry/'),
 N('T1', '關於 Kitchen AO', '/about-kitchenao/'), N('T2', '客人好評', '/客人好評/'), N('T3', '合作夥伴', '/合作伙伴/'), N('T4', '精選圖庫', '/精選圖庫/'),
 N('V1', '公司到會', '/corporate-catering-hk/'), N('V2', '企業商務到會', '/business-event/'), N('V3', '香港到會推介', '/hong-kong-catering-recommendation/'),
 N('V4', '服務概覽（幾乎空白）', '/服務概覽/', 'old'), N('V5', '飲品及雞尾酒服務', '/飲品及雞尾酒服務/'),
 N('X1', '船河舊 landing', '/boat-trip-bldg/', 'old'), N('X2', '派對舊 landing', '/partyfood-bldg/', 'old'), N('X3', '小食舊 landing', '/snacks-bldg/', 'old'),
 N('X4', '範例頁面（刪除）', '/sample-page/', 'bad'), N('HK1', '⚠️ 被入侵頁面', '/ba620e385336-htm/', 'bad'), N('HK2', '⚠️ 被入侵頁面', '/66695d0f41db-htm/', 'bad'),
], edges=['H --> C', 'C --> B1 & B2 & B3 & B4 & B5 & B6 & B7 & B8 & B9 & B10', 'H --> P1 & P2 & P3 & P4 & P5 & P6 & P7 & P8', 'P1 --> P9', 'H --> BL', 'H --> D',
          'H --> S1 & S2 & S3 & S4 & S5', 'H --> T1 & T2 & T3 & T4', 'H --> V1 & V2 & V3 & V4 & V5', 'H -.-> X1 & X2 & X3', 'H -.-> X4 & HK1 & HK2'])

# ---------- 船河 ----------
D['船河'] = dict(dir='LR', nodes=[
 N('H', '首頁', '/'), N('L', '船河 landing（新・交易型）', '/catering/boat-party/', 'new'), N('OLD', '舊 landing（現時 live）', '/boat-trip-bldg/', 'old'),
 N('C1', '船河套餐分類', '/product-category/party/boat-party-set/'),
 N('PR1', '15–20 人船河套餐', '/product/ao-15-20pax-boat-party-set/'), N('PR2', '21–25 人船河套餐', '/product/ao-21-25pax-boat-party-set/'),
 N('PR3', '26–30 人船河套餐', '/product/ao-26-30pax-狂歡派對船河套餐-boat-party-set/'), N('PR4', '31–35 人船河套餐', '/product/ao-31-35pax-狂歡派對船河套餐-boat-party-set/'),
 N('PR5', '36–40 人船河套餐', '/product/ao-36-40pax-狂歡派對船河套餐-boat-party-set/'),
 N('C2', '肉食盛盒', '/product-category/party/meat-monster/'), N('S1', '一口小食（單品）', '/product-category/a-la-carte/snacks/'),
 N('BG', '船P必備清單 blog', '/blog/boat-party-catering-guide/'), N('DL', '送貨需知：碼頭交收・運費', '/delivery/'),
], edges=['H --> L', 'OLD -- 301 或原址改版 --> L', 'L --> C1', 'C1 --> PR1 & PR2 & PR3 & PR4 & PR5', 'L --> C2', 'L --> S1', 'L <--> BG', 'L --> DL'])

# ---------- 素食 ----------
D['素食'] = dict(dir='LR', nodes=[
 N('H', '首頁', '/'), N('LP', 'LP｜素食到會 Landing（新）', '/catering/vegetarian/', 'new'),
 N('C1', 'C1｜「素」味人生套餐分類', '/product-category/party/vegetarians-set/'),
 N('V1', 'P1｜6–8 人', '/product/ao-6-8pax-vegetarian-life/'), N('V2', 'P2｜10–12 人', '/product/ao-10-12pax-vegetarian-life/'),
 N('V3', 'P3｜16–19 人', '/product/ao-16-19pax-vegetarian-life/'), N('V4', 'P4｜22–26 人', '/product/ao-22-26pax-vegetarian-life/'),
 N('C2', 'C2｜素食單點（新分類）', '/product-category/a-la-carte/vegetarian/', 'new'),
 N('I1', '惹味蒜香焗茄子', '/product/a3900-grilled-garlic-eggplant/', 'old'), N('I2', '蒜香炒翠玉瓜', '/product/a62-stir-fried-zucchini-with-garlic-1-pounds/', 'old'),
 N('I3', '忌廉白汁菠菜', '/product/a59-spinach-with-cream-sauce-1-pounds/', 'old'), N('I4', '手壓香濃薯蓉', '/product/a61-hand-pressed-sweet-potato-puree-1-pounds/', 'old'),
 N('B1', 'B1｜素食到會推介（更新舊文）', '/blog/vegetarian-catering-hong-kong/', 'old'),
 N('B2', 'B2｜素食種類全攻略（支柱）', '/blog/vegetarian-types-guide/'),
 N('B3', 'B3｜初一十五食齋懶人包', '/blog/chu-yat-sap-ng-vegetarian-guide/', 'new'),
 N('B4', 'B4｜吃素好處與營養', '/blog/vegetarian-nutrition-protein/', 'new'),
 N('B5', 'B5｜一週素食菜單', '/blog/weekly-vegetarian-menu/', 'new'),
 N('B6', 'B6｜Vegan／Vegetarian 中文', '/blog/vegan-vegetarian-meaning/'),
 N('B7', 'B7｜植物肉、植物奶', '/blog/plant-based-meat-milk/', 'new'),
 N('T1', '舊 tag（已 301）', '/tag/素食到會/'), N('T2', 'Blog tag 頁（建議 noindex）', '/blog/tag/素食到會/', 'old'),
], edges=['H --> LP', 'LP --> C1 & C2', 'C1 --> V1 & V2 & V3 & V4', 'C2 --> I1 & I2 & I3 & I4', 'LP <--> B1', 'LP --> B2',
 'B1 -. "CTA：揀選「素」味人生套餐" .-> C1', 'B1 --> B2 & B3', 'B2 --> B3 & B4 & B6', 'B2 -. "CTA：素食到會" .-> LP',
 'B3 -. "CTA：初一十五訂素食到會" .-> LP', 'B4 --> B5 & B7', 'B5 -. "CTA：不想煮？素食單點" .-> C2', 'B5 -. "CTA：素食到會" .-> LP',
 'B6 --> B2 & B4', 'B7 -. "CTA：「素」味人生套餐" .-> C1', 'T1 -. 301 .-> C1', 'B1 -. noindex .-> T2'])

# ---------- 生日會 ----------
D['生日會'] = dict(dir='LR', nodes=[
 N('H', '首頁', '/'), N('L', '生日會 landing（新）', '/catering/birthday-party/', 'new'), N('OLD', '派對舊 landing', '/partyfood-bldg/', 'old'),
 N('C1', '兒童套餐', '/product-category/party/children/'), N('C2', '美食派對 5–85 人', '/product-category/party/foot-party/'),
 N('C3', '三層食物架', '/product-category/party-supplies/kid-food-stand/'), N('C4', '甜品', '/product-category/a-la-carte/dessert/'),
 N('B1', '小朋友生日會 blog', '/blog/kids-birthday-party-catering/'), N('B2', '激光打印食物 blog', '/blog/laser-printed-food-party/'),
], edges=['H --> L', 'OLD -- 301 --> L', 'L --> C1 & C2 & C3 & C4', 'L <--> B1', 'L <--> B2'])

# ---------- 公司午餐 ----------
D['公司午餐'] = dict(dir='LR', nodes=[
 N('H', '首頁', '/'), N('L', '公司午餐 landing（新）', '/catering/corporate-lunch/', 'new'), N('L0', '現有公司到會頁（評估）', '/corporate-catering-hk/', 'old'),
 N('C', '商務活動 hub', '/product-category/商務活動/', 'old'),
 N('C1', '員工膳食餐盒', '/product-category/商務活動/staff-meal/'), N('C2', '商務餐盒', '/product-category/商務活動/commercial-lunch-box/'),
 N('C3', '高級餐盒', '/product-category/商務活動/executive-premium-meal-box/'), N('C4', '皇家小食盒', '/product-category/商務活動/royal-snackers-box/'),
 N('C5', '九宮格 Canapés', '/product-category/商務活動/a-bit-of-cuisines-gourmet-in-a-box/'), N('C6', '單點商務小食', '/product-category/單點商務小食/'),
 N('RQ', '報價查詢', '/catering-quote-enquiry/'), N('BE', '企業商務到會（主題重疊）', '/business-event/', 'old'),
 N('B1', '公司活動到會 blog', '/blog/company-event-catering-guide/'), N('B2', '公司到會點揀 blog', '/blog/hong-kong-company-catering-how-to-choose/'),
 N('O1', '舊頁：商務餐盒', '/商務餐盒/', 'old'), N('O2', '舊頁：高級餐盒', '/高級餐盒-2/', 'old'), N('O3', '舊頁：員工膳食餐盒', '/員工膳食餐盒/', 'old'),
 N('O4', '舊頁：皇家小食盒', '/皇家小食盒/', 'old'), N('O5', '舊頁：舌尖上的餐桌', '/舌尖上的餐桌-頂級美食一盒盛/', 'old'),
], edges=['H --> L', 'L0 -. 301 或保留 .-> L', 'L --> C', 'C --> C1 & C2 & C3 & C4 & C5', 'L --> C6', 'L --> RQ', 'L <--> B1 & B2', 'BE -.-> L',
          'O2 -- 301 --> C3', 'O1 -- 301 --> C2', 'O3 -- 301 --> C1', 'O4 -- 301 --> C4', 'O5 -- 301 --> C5'])

# ---------- 學校飯盒 ----------
D['學校飯盒'] = dict(dir='LR', nodes=[
 N('H', '首頁', '/'), N('L', '學校飯盒 landing（新）', '/catering/school-lunch-box/', 'new'),
 N('N1', '學校飯盒產品（未有）', '', 'new'), N('C1', '輕食宴會（學校聯歡會）', '/product-category/party/refreshment-set/'),
 N('C2', '員工膳食餐盒（暫代）', '/product-category/商務活動/staff-meal/'), N('BN', '學校飯盒 blog（未有）', '', 'new'),
], edges=['H --> L', 'L --> N1 & C1 & C2', 'L <--> BN'])

# ---------- 中秋節 ----------
D['中秋節'] = dict(dir='LR', nodes=[
 N('H', '首頁', '/'), N('L', '中秋 landing（新・每年沿用）', '/catering/mid-autumn/', 'new'),
 N('C1', '中秋套餐分類（建議改 slug）', '/product-category/中秋佳節團圓套餐-2026/', 'old'), N('M', '月餅預訂', '/mooncake-preorder/'),
 N('B1', '中秋到會 blog', '/blog/mid-autumn-catering-hong-kong/'),
], edges=['H --> L', 'L --> C1', 'L <--> M', 'L <--> B1'])

# ---------- 萬聖節 ----------
D['萬聖節'] = dict(dir='LR', nodes=[
 N('H', '首頁', '/'), N('L', '萬聖節 landing（新・每年沿用）', '/catering/halloween/', 'new'),
 N('C1', '萬聖節狂嘩套餐分類', '/product-category/halloween-set/'),
 N('PR1', '5–6 人', '/product/ao-5-6pax-halloween萬聖節狂嘩套餐/'), N('PR2', '8–10 人', '/product/ao-8-10pax-halloween萬聖節狂嘩套餐/'),
 N('PR3', '12–16 人', '/product/ao-12-16pax-halloween萬聖節狂嘩套餐/'), N('PR4', '18–22 人', '/product/ao-18-22pax-halloween萬聖節狂嘩套餐/'),
 N('PR5', '26–30 人', '/product/ao-26-30pax-halloween萬聖節狂嘩套餐/'), N('PR6', '35–40 人', '/product/ao-35-40pax-halloween萬聖節狂嘩套餐/'),
 N('B1', '萬聖節到會 blog', '/blog/halloween-catering-hong-kong/'),
], edges=['H --> L', 'H --> C1', 'L --> C1', 'C1 --> PR1 & PR2 & PR3 & PR4 & PR5 & PR6', 'L <--> B1', 'B1 --> C1'])

# ---------- 聖誕節 ----------
D['聖誕節'] = dict(dir='LR', nodes=[
 N('H', '首頁', '/'),
 N('LP', 'LP｜聖誕套餐分類（Landing page・11 月 10 日前）<br/>建議網址 /product-category/christmas-set/', '', 'new'),
 N('BL', '舊 Blog：聖誕到會（Landing page 上線當日 301）', '/blog/christmas-catering-hong-kong/', 'old'),
 N('B2', 'B2｜香港人聖誕餐吃甚麼？聖誕小食＋搵食工具（新文章）<br/>建議網址 /blog/christmas-food-hong-kong/', '', 'new'),
 N('EN', 'LP-EN｜英文聖誕 Landing page', '', 'new'),
 N('C2', '人數選餐', '/product-category/party-set-by-people/'), N('C3', '美食派對 Gourmet', '/product-category/party/foot-party/'),
 N('C4', '派對用品', '/product-category/party-supplies/'),
 N('S1', '惹味小食（單點）', '/product-category/a-la-carte/snacks/'), N('S2', '甜品（單點）', '/product-category/a-la-carte/dessert/'),
 N('V1', '公司到會（公司聖誕派對）', '/corporate-catering-hk/'), N('VE', '公司到會（英文）', '/en/corporate-catering-hk/'),
 N('DL', '送貨需知（平安夜送貨時段）', '/delivery/'), N('Q', '報價查詢', '/catering-quote-enquiry/'),
], edges=['H -- 首頁 banner --> LP', 'LP --> C2 & C3 & C4', 'LP -. "CTA：公司聖誕派對" .-> V1', 'LP -. "CTA：平安夜送貨安排" .-> DL',
 'LP -. "CTA：大型活動報價" .-> Q', 'BL == 301 ==> LP', 'B2 -. "搵食工具：產品連結" .-> S1 & S2', 'B2 -. "CTA：聖誕到會套餐" .-> LP', 'B2 -. "公司聖誕派對" .-> V1', 'LP <-. 中英版本 .-> EN', 'EN -. "CTA：Office Christmas party" .-> VE'])

# ---------- 野餐 ----------
D['野餐'] = dict(dir='LR', nodes=[
 N('H', '首頁', '/'), N('L', '野餐 landing（新）', '/catering/picnic/', 'new'),
 N('C1', 'Chill一下野餐盒分類', '/product-category/party/chill-box/'),
 N('PR1', 'Chill一下野餐盒（大）4–6 人', '/product/chill一picnic-big-for-4-6-persons/'), N('PR2', 'Chill一下野餐盒（細）', '/product/chill一picnic-small/'),
 N('S1', '惹味小食（單品）', '/product-category/a-la-carte/snacks/'), N('S2', '餐具及暖貼加配', '/product-category/party-supplies/thin-crust-pizza/'),
 N('BG', 'Blog 1：香港野餐好去處（地點搜尋工具・計劃中）', '', 'new'), N('DL', '送貨需知：公園入口交收', '/delivery/'),
], edges=['H --> L', 'L --> C1', 'C1 --> PR1 & PR2', 'L --> S1 & S2', 'L <--> BG', 'BG --> C1', 'L --> DL'])

# ---------- 訂製食物 ----------
D['訂製食物'] = dict(dir='LR', nodes=[
 N('H', '首頁', '/'), N('L', '訂製食物 campaign（新）', '/catering/custom-printed-food/', 'new'),
 N('OLD', '客製化紀念品訂製服務', '/客製化紀念品訂製服務/', 'old'), N('N1', '訂製食物分類（未有）', '', 'new'),
 N('P1', '雷射漢堡包（slug 要改）', '/product/船河小食/', 'old'), N('B1', '激光打印食物 blog', '/blog/laser-printed-food-party/'),
], edges=['H --> L', 'OLD -- 合併 --> L', 'L --> N1', 'N1 --> P1', 'L <--> B1'])

# ---------- 地區頁 ----------
dist = [('港島', [('中環', 'catering-central'), ('西營盤', 'catering-sai-ying-pun'), ('灣仔', 'catering-wan-chai'), ('銅鑼灣', 'catering-causewaybay'), ('北角', 'catering-north-point'), ('鰂魚涌', 'catering-quarry-bay')]),
        ('九龍', [('尖沙咀', 'catering-tsim-sha-tsui'), ('旺角', 'catering-mong-kok'), ('深水埗', 'catering-sham-shui-po'), ('九龍城', 'catering-kowloon-city'), ('觀塘', 'catering-kwun-tong'), ('九龍灣（建議新增）', ''), ('長沙灣（建議新增）', '')]),
        ('新界', [('沙田', 'catering-sha-tin'), ('荃灣', 'catering-tsuenwan'), ('元朗', 'catering-yuen-long'), ('屯門', 'catering-tuen-mun'), ('將軍澳（建議新增）', ''), ('葵涌（建議新增）', ''), ('西貢（建議新增）', '')])]
nodes = [N('H', '首頁', '/'), N('HUB', '地區 hub（要補內容）', '/地區到會分類/', 'old'), N('DL', '送貨需知：運費表', '/delivery/'), N('BOAT', '船河 landing', '/catering/boat-party/', 'new')]
edges = ['H --> HUB', 'DL -. 連去 .-> HUB']
for ri, (reg, items) in enumerate(dist):
    rid = f'R{ri}'; nodes.append(N(rid, reg, '', 'grp')); edges.append(f'HUB --> {rid}')
    prev = rid
    for di, (nm, slug) in enumerate(items):
        did = f'D{ri}_{di}'
        nodes.append(N(did, nm, f'/{slug}/' if slug else '', 'ok' if slug else 'new'))
        edges.append(f'{prev} --> {did}' if di == 0 else f'{prev} --- {did}')  # 同一區域的地區向下排成一欄
        prev = did
        if '西貢' in nm: edges.append(f'{did} -.-> BOAT')
D['地區頁'] = dict(dir='TB', nodes=nodes, edges=edges)


# ---------- SEO 工作優先次序（2026-11-01）----------
# (優先, 頁面, 類型, 主攻字＋GSC 12 個月數據, 原因, 期限, 狀態, 連結)
PRI = [
 ('P0', '被入侵頁面×2、範例頁面', '技術', '—', '安全問題，影響全站信任度；如已處理可刪此行', '即時', '待確認', ''),
 ('P0', '公司到會 18404（中＋英）', '核心錢頁', '公司到會 1,155 曝光 #27；到會公司 1,618 #26；企業到會 347 #28', '檔案已做好，只差上載；12 月至 2 月年會及團年飯旺季前要上線', '11/3', '待上載', 'core-pages-kw.html#CORP'),
 ('P0', '客製化紀念品訂製服務', '服務頁', '贈品訂製 410 #57；紀念品訂製 296 #47', '頁面有錯要即改', '11/7', '未開始', 'core-pages-kw.html#GIFT'),
 ('P0', '/en/ 全站共用中文字眼', '技術', '「描述」「已售完」、側欄分類名', 'TranslatePress 改一次全站生效，約 10 分鐘', '11/7', '未開始', ''),
 ('P1', '聖誕到會 Landing page（中＋英）', 'Landing', '聖誕到會 602 #35；聖誕到會 2026 357 #36；聖誕到會套餐 232 #43', '季節 deadline，搜尋 11 月中開始升，12 月見頂', '11/10', '未開始（待確認火雞）', 'xmas-kw.html'),
 ('P1', '舊 Blog 聖誕到會 → 301 去 LP', '技術', '舊文 1,275 曝光 #22', 'LP 上線當日做，避免兩頁搶字', 'LP 上線當日', '未開始', 'xmas-kw.html'),
 ('P1', 'B2 聖誕小食 Blog（香港人聖誕餐吃甚麼）', 'Blog', '聖誕小食、聖誕派對食物、聖誕餐（GKP）', '要 2 至 3 星期被收錄，12 月前要上', '11/17', '未開始', 'xmas-kw.html'),
 ('P1', 'NB1 Annual Dinner 籌備全攻略', 'Blog', 'company annual dinner planning hk 256 #80；annual dinner 遊戲、抽獎禮物等約 1,000 搜尋量', '年會旺季前上線，連去公司到會', '11/24', '未開始', 'core-pages-kw.html#NB1'),
 ('P2', '派對到會套餐分類', '核心錢頁', '到會套餐 1,731 #9；派對到會 1,625 #26；party 到會 1,042 #20', '「到會套餐」已在第一頁，小改即可多拿點擊（Quick win）', '11 月', '已分配 KW', 'core-pages-kw.html#PARTY'),
 ('P2', '到會推介（中＋英）', '核心頁', '到會推介 537 #31；到會邊間好討論區 51 #12', '同首頁搶「到會公司」「公司到會」，改寫後分清角色', '12 月', '要改寫', 'core-pages-kw.html#REC'),
 ('P2', '首頁（中＋英）', '核心頁', '到會 2,792 #22；到會服務 2,499 #25', '全站最大曝光，排名升到第一頁效益最大', '12 月', '已分配 KW', 'core-pages-kw.html#HOME'),
 ('P2', '商務餐盒分類＋舊頁 /商務餐盒/ 301', '核心錢頁＋技術', '商務餐盒 574 #11；商務飯盒 721 #36；舊頁 1,091 曝光 #59', '舊頁搶字，301 後集中排名；商務餐盒接近第一頁', '12 月', '未開始', 'index.html#公司午餐'),
 ('P2', '地區頁（15 頁）', 'Landing', '荃灣到會 735 #6；元朗到會 671 #11；沙田到會 590 #10', '已接近第一頁，加內容及內鏈即可升；英文版待翻譯', '12 月', '要翻譯', 'index.html#地區頁'),
 ('P2', '商務活動', '核心頁', '商務到會 655 #29', '同公司到會分工：酒會、開張、發佈會', '12 月', '下一輪', 'core-pages-kw.html#BIZ'),
 ('P2', '團年飯 Blog（cny-reunion-dinner-guide）更新', 'Blog', '開年飯 314 #16；團年飯 188 #16', '1 月搜尋見頂，更新年份及加連結去公司到會', '1/10', '要更新', ''),
 ('P3', '生日會 Landing', 'Landing', '生日到會 1,037 #30；小朋友派對食物 517 #15；小朋友到會 437 #24', '曝光大但未有專頁，全年需求', '2027 Q1', '計劃中', 'index.html#生日會'),
 ('P3', '船河 Landing＋Blog 更新', 'Landing', '船河到會 896 #23；船河 806 #24；遊船河到會 438 #22', '4 至 10 月旺季，3 月前上線', '2027/3', '計劃中', 'index.html#船河'),
 ('P3', '素食 Landing＋Blog 1–7', 'Landing＋Blog', '素食到會 565 #14；素味人生 195 #8', '已有 KW 分配，可分批寫', '2027 Q1', '已分配 KW', 'vegetarian-kw.html'),
 ('P3', '舊 Blog 重寫：到會邊間好、到會中伏', 'Blog', '到會邊間好 600 曝光 #25', '支援到會推介', '2027 Q1', '第二輪', 'core-pages-kw.html#OLD1'),
 ('P3', '關於我們、常見問題', '信任頁', '品牌字（kitchen ao 1,671 #1）', 'E-E-A-T 及 AI search 信任度', '2027 Q1', '下一輪', 'core-pages-kw.html#ABOUT'),
 ('P3', '/en/ 產品及分類英文內容', '翻譯', '155 頁仍有中文', '先做 25 個分類描述', '12 月起分批', '已列清單', ''),
 ('P4', '野餐 Landing＋好去處 Blog', 'Landing＋Blog', '野餐盒 197 #4（17 click）', '曝光小但轉化好，春季前做', '2027/2', '計劃中', 'index.html#野餐'),
 ('P4', '保暖及保鮮用品 Blog 1–3', 'Blog', 'GSC 未有數據（GKP 字）', '資訊型，轉化較低；待確認產品', '2027 Q2', '待產品', 'thermal-kw.html'),
 ('P4', '學校飯盒 Landing', 'Landing', '學校到會 288 #51', '未有產品', '待產品', '計劃中', 'index.html#學校飯盒'),
 ('P4', '訂製食物 campaign', 'Landing', '激光打印食物（Blog 已有）', '先完成 GIFT 改錯', '2027', '計劃中', 'index.html#訂製食物'),
 ('P4', '中秋、萬聖節 Landing', 'Landing', '中秋到會 2026 339 #13；萬聖節到會 84 #6', '季節頁，下次推出前 2 個月做', '2027/7、2027/9', '計劃中', 'index.html#中秋節'),
 ('P4', 'Recipes 食譜', 'Blog', '—', '未有方向', '—', '未開始', 'core-pages-kw.html#RCP'),
]
import html as _h, urllib.parse as _u
PCOL = {'P0': '#E2574C', 'P1': '#C8A24A', 'P2': '#2B7BD0', 'P3': '#5E7E5C', 'P4': '#8A8172'}
PDESC = {'P0': '本週：即改或已做好待上載', 'P1': '11 月：季節 deadline', 'P2': '11 至 12 月：核心錢頁及 Quick win', 'P3': '2027 Q1', 'P4': '之後／待產品或季節'}
def _lnk(u):
    if not u: return ''
    if '#' in u: a, b = u.split('#', 1); u = a + '#' + _u.quote(b)
    return f'<a href="{u}">' + ('架構圖 →' if u.startswith('index.html') else 'KW 分配 →') + '</a>'
rows = ''.join(f'<tr><td><span class="pp" style="background:{PCOL[p]}">{p}</span></td><td><b>{_h.escape(n)}</b><br><small>{t}</small></td><td>{_h.escape(k)}</td><td>{_h.escape(w)}</td><td class="nw">{d}</td><td class="nw">{s}</td><td class="nw">{_lnk(l)}</td></tr>' for p, n, t, k, w, d, s, l in PRI)
PRI_HTML = ('<div class="pri"><h2>SEO 工作優先次序（2026-11-01）</h2><p class="pl">' + ''.join(f'<span><i style="background:{PCOL[p]}"></i>{p}｜{PDESC[p]}</span>' for p in PCOL) +
  '</p><p class="pn">排序準則：①季節 deadline ②交易型錢頁先於資訊型 Blog ③已接近第一頁（#5–#20）的字先做，回報最快 ④已做好未上載的先上。數據：GSC 12 個月（至 10-31）。</p>'
  '<div class="card"><table><thead><tr><th>優先</th><th>頁面</th><th>主攻字及 GSC（曝光／排名）</th><th>原因</th><th>期限</th><th>狀態</th><th></th></tr></thead><tbody>' + rows + '</tbody></table></div></div>')
PRI_CSS = '.pri h2{margin:0 0 8px;font-size:20px}.pri .pl span{display:inline-block;margin:0 14px 6px 0;font-size:13px}.pri .pl i{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:5px}.pri .pn{font-size:13px;color:#6b6252;margin:0 0 10px}.pri table{border-collapse:collapse;width:100%;font-size:14px}.pri th{background:#1A1A1A;color:#F7CE46;text-align:left;padding:8px 10px;white-space:nowrap}.pri td{border-top:1px solid #EEE6D6;padding:8px 10px;vertical-align:top}.pri td small{color:#8a8172}.pri .nw{white-space:nowrap}.pri .pp{display:inline-block;color:#fff;font-weight:800;border-radius:8px;padding:2px 8px}.pri a{color:#9A7B2E;font-weight:700}.pri{margin-bottom:22px}'


# ---------- 每日排程：每日 2 篇舊文＋1 篇新文，按「預計每年增加點擊」排先後 ----------
import datetime as _dt
CTR={3:.10,5:.055,8:.03,10:.02,15:.01,20:.005}
def tgt(pos):
    return 3 if pos<=10 else 5 if pos<=20 else 8 if pos<=30 else 10
# kind O/N, series, name, note, impr(年), current pos (None=新), clicks now, target override, value
I=[
('O','corp','公司到會 18404 上載＋live check','檔案已做好；公司到會字群 7,079 曝光 #27',7079,27,7,None,'高'),
('O','gift','客製化紀念品訂製服務：改錯','3,566 曝光 #51',3566,51,10,None,'中'),
('O','party','派對到會套餐分類（中＋英）','27,486 曝光 #36',27486,36,95,None,'高'),
('O','biz','商務餐盒分類＋舊頁 /商務餐盒/ 301','商務字群 5,156 曝光 #30',5156,30,54,None,'高'),
('O','rec','到會推介（中＋英）','到會推介字群 8,237 曝光 #30',8237,30,30,None,'高'),
('O','home','首頁（中＋英）','33,658 曝光 #27（已有 623 click，多為品牌字）',33658,27,623,None,'高'),
('O','cny','Blog：團年飯 vs 開年飯（更新 2027）','633 曝光 #14；1 月見頂',633,14,2,None,'中'),
('O','corp','Blog：公司活動到會攻略','170 曝光 #19',170,19,3,None,'中'),
('O','corp','Blog：公司到會點揀','392 曝光 #36',392,36,0,None,'中'),
('O','biz','商務活動','商務到會 655 曝光 #29',655,29,0,None,'高'),
('O','area','地區頁：荃灣','1,526 曝光 #10',1526,9.8,25,None,'高'),
('O','area','地區頁：元朗','2,217 曝光 #11',2217,11,52,None,'高'),
('O','area','地區頁：沙田','1,308 曝光 #13',1308,13.2,21,None,'高'),
('O','area','地區頁：屯門','1,086 曝光 #12',1086,12.1,17,None,'高'),
('O','area','地區頁：北角','2,091 曝光 #23',2091,22.7,38,None,'高'),
('O','area','地區頁：鰂魚涌','922 曝光 #15',922,15,30,None,'高'),
('O','area','地區頁：觀塘','2,455 曝光 #26',2455,26.1,10,None,'高'),
('O','area','地區頁：旺角','1,100 曝光 #17',1100,17,1,None,'高'),
('O','area','地區頁：深水埗','686 曝光 #15',686,14.7,19,None,'高'),
('O','area','地區頁：尖沙咀','17 曝光 #16',17,16,0,None,'高'),
('O','area','地區頁：中環','998 曝光 #20',998,19.6,6,None,'高'),
('O','area','地區頁：銅鑼灣','1,171 曝光 #18',1171,18,4,None,'高'),
('O','area','地區頁：灣仔','843 曝光 #27',843,26.8,8,None,'高'),
('O','area','地區頁：西營盤','279 曝光 #26',279,26.5,6,None,'高'),
('O','area','地區頁：九龍城','320 曝光 #23',320,23.1,2,None,'高'),
('O','bday','兒童套餐分類','3,292 曝光 #18',3292,18,39,None,'高'),
('O','rec','舊 Blog：到會邊間好','600 曝光 #25',600,25,11,None,'中'),
('O','rec','舊 Blog：到會中伏','177 曝光 #9',177,8.6,3,None,'中'),
('O','veg','Blog：素食到會推介（vegB1）','KP 770／月；現 438 曝光 #14',9240,None,12,10,'高'),
('O','veg','Blog：素食種類全攻略（vegB2）','KP 47,030／月（大字難排）',564360,None,0,20,'低'),
('O','veg','Blog：Vegan／Vegetarian 中文（vegB6）','KP 2,700／月；現 114 曝光 #12',32400,None,1,10,'低'),
('O','bday','Blog：小朋友生日會','904 曝光 #37',904,36.6,2,None,'中'),
('O','trust','關於我們','1,467 曝光 #4',1467,4.2,22,None,'中'),
('O','trust','常見問題','82 曝光 #5（需要 CS 提供問題）',82,5.3,2,None,'中'),
('N','xmas','聖誕到會 Landing page（中文）','KP 3,540／月（12 月 30,010）；11/10 前上線，當日舊 Blog 301',42480,None,0,8,'高'),
('N','xmas','聖誕到會 Landing page（英文）','英文聖誕字量少',1884,None,0,10,'高'),
('N','xmas','Blog：香港人聖誕餐吃甚麼？','KP 14,170／月（12 月 91,160）',170040,None,0,20,'中'),
('N','corp','Blog：Annual Dinner 籌備全攻略（NB1）','資訊字約 1,000／月',12000,None,0,10,'中'),
('N','bday','生日會 Landing','生日字群 4,723 曝光',4723,None,0,8,'高'),
('N','veg','素食到會 Landing','KP 200／月＋GSC 963 曝光',2400,None,0,8,'高'),
('N','boat','船河 Landing','船河字群 2,492＋舊 landing 4,531 曝光（301 承接）',7023,None,7,8,'高'),
('N','veg','Blog：初一十五食齋懶人包（vegB3）','KP 1,510／月',18120,None,0,10,'低'),
('N','veg','Blog：吃素好處與營養（vegB4）','KP 1,060／月',12720,None,0,10,'低'),
('N','veg','Blog：一週素食菜單（vegB5）','KP 1,420／月',17040,None,0,10,'低'),
('N','veg','Blog：植物肉、植物奶（vegB7）','KP 490／月',5880,None,0,10,'低'),
('N','f1','Blog：F1 車手飲食＋觀賽派對到會','未做 KW 分析；GSC 未有數據',0,None,0,10,'低'),
('N','pic','野餐 Landing','野餐字群 474 曝光（野餐盒分類已 #9）',474,None,0,8,'高'),
('N','therm','Blog：食物保暖用品（thermB1）','KP 12,980／月（多為大字）；待確認 MUJI 產品',155760,None,0,20,'低'),
('N','therm','Blog：保鮮用品（thermB2）','KP 6,960／月',83520,None,0,20,'低'),
('N','therm','Blog：保溫杯、保溫瓶（thermB3）','KP 8,520／月',102240,None,0,20,'低'),
('N','gift','訂製食物 Landing','訂製字群 2,127 曝光 #50',2127,None,1,8,'中'),
('N','ma','中秋 Landing（每年沿用）','中秋字群 1,268 曝光；Blog 已有排名',1268,None,0,10,'中'),
('N','hal','萬聖節 Landing（每年沿用）','萬聖字群 163 曝光；Blog 已有排名',163,None,0,10,'中'),
]
_R=[]
for k,s,n,note,imp,pos,clk,t,val in I:
    t=t or tgt(pos); gain=max(0,round(imp*CTR[t]-clk))
    _R.append(dict(k=k,s=s,n=n,note=note,gain=gain,t=t,val=val))

SER = {'Blog：素食到會推介（vegB1）': 'vegB1', 'Blog：素食種類全攻略（vegB2）': 'vegB2', 'Blog：Vegan／Vegetarian 中文（vegB6）': 'vegB6', 'Blog：初一十五食齋懶人包（vegB3）': 'vegB3', 'Blog：吃素好處與營養（vegB4）': 'vegB4', 'Blog：一週素食菜單（vegB5）': 'vegB5', 'Blog：植物肉、植物奶（vegB7）': 'vegB7', 'Blog：食物保暖用品（thermB1）': 'thermB1', 'Blog：保鮮用品（thermB2）': 'thermB2', 'Blog：保溫杯、保溫瓶（thermB3）': 'thermB3', '聖誕到會 Landing page（中文）': 'xmasLP', '聖誕到會 Landing page（英文）': 'xmasLP-EN', 'Blog：香港人聖誕餐吃甚麼？': 'xmasB2', 'Blog：Annual Dinner 籌備全攻略（NB1）': 'corpB1', 'Blog：團年飯 vs 開年飯（更新 2027）': 'cnyB1', 'Blog：公司活動到會攻略': 'corpB2', 'Blog：公司到會點揀': 'corpB3', '舊 Blog：到會邊間好': 'recB1', '舊 Blog：到會中伏': 'recB2', 'Blog：小朋友生日會': 'bdayB1', '生日會 Landing': 'bdayLP', '素食到會 Landing': 'vegLP', '船河 Landing': 'boatLP', '野餐 Landing': 'picLP', '訂製食物 Landing': 'giftLP', '中秋 Landing（每年沿用）': 'maLP', '萬聖節 Landing（每年沿用）': 'halLP', 'Blog：F1 車手飲食＋觀賽派對到會': 'f1B1'}

# ---------- WP 位置：網址、在 WP 後台搜尋用的字 ----------
WP = {  # 名稱: (網址, 後台搜尋字, 位置)
 '公司到會 18404 上載＋live check': ('/corporate-catering-hk/', '香港公司到會', '頁面'),
 '客製化紀念品訂製服務：改錯': ('/客製化紀念品訂製服務/', '客製化紀念品訂製服務', '頁面'),
 '派對到會套餐分類（中＋英）': ('/product-category/party/', '派對到會套餐', '商品分類'),
 '商務餐盒分類＋舊頁 /商務餐盒/ 301': ('/product-category/商務活動/commercial-lunch-box/', '商務餐盒', '商品分類＋頁面'),
 '到會推介（中＋英）': ('/hong-kong-catering-recommendation/', '到會推介', '頁面'),
 '首頁（中＋英）': ('/', '首頁', '頁面'),
 'Blog：團年飯 vs 開年飯（更新 2027）': ('/blog/cny-reunion-dinner-guide/', '團年飯 vs 開年飯', '文章'),
 'Blog：公司活動到會攻略': ('/blog/company-event-catering-guide/', '香港公司活動到會攻略', '文章'),
 'Blog：公司到會點揀': ('/blog/hong-kong-company-catering-how-to-choose/', '香港公司到會指南', '文章'),
 '商務活動': ('/business-event/', '商務活動', '頁面'),
 '兒童套餐分類': ('/product-category/party/children/', '兒童套餐', '商品分類'),
 '舊 Blog：到會邊間好': ('/blog/hongkong-catering-2026-香港到會邊間好/', '香港到會邊間好', '文章'),
 '舊 Blog：到會中伏': ('/blog/catering-pitfalls-guide/', '香港到會避伏指南', '文章'),
 'Blog：素食到會推介（vegB1）': ('/blog/vegetarian-catering-hong-kong/', '素食到會揀選全攻略', '文章'),
 'Blog：素食種類全攻略（vegB2）': ('/blog/vegetarian-types-guide/', '素食分類天書', '文章'),
 'Blog：Vegan／Vegetarian 中文（vegB6）': ('/blog/vegan-vegetarian-meaning/', 'Vegan、Vegetarian 中文', '文章'),
 'Blog：小朋友生日會': ('/blog/kids-birthday-party-catering/', '小朋友生日會到會挑選指南', '文章'),
 '關於我們': ('/about-kitchenao/', '關於 Kitchen AO', '頁面'),
 '常見問題': ('/常見問題/', '常見問題', '頁面'),
 '聖誕到會 Landing page（中文）': ('/product-category/christmas-set/（建議）', '新建：商品分類「聖誕到會套餐」', '新建'),
 '聖誕到會 Landing page（英文）': ('/en/product-category/christmas-set/（建議）', '同上（英文內容）', '新建'),
 'Blog：香港人聖誕餐吃甚麼？': ('/blog/christmas-food-hong-kong/（建議）', '新建文章', '新建'),
 'Blog：Annual Dinner 籌備全攻略（NB1）': ('/blog/annual-dinner-planning-guide/（建議）', '新建文章', '新建'),
 '生日會 Landing': ('/catering/birthday-party/（建議）', '新建頁面', '新建'),
 '素食到會 Landing': ('/catering/vegetarian/（建議）', '新建頁面', '新建'),
 '船河 Landing': ('/catering/boat-party/（建議）', '新建頁面；舊頁「遊船河到會」301', '新建'),
 'Blog：初一十五食齋懶人包（vegB3）': ('/blog/chu-yat-sap-ng-vegetarian-guide/（建議）', '新建文章', '新建'),
 'Blog：吃素好處與營養（vegB4）': ('/blog/vegetarian-nutrition-protein/（建議）', '新建文章', '新建'),
 'Blog：一週素食菜單（vegB5）': ('/blog/weekly-vegetarian-menu/（建議）', '新建文章', '新建'),
 'Blog：植物肉、植物奶（vegB7）': ('/blog/plant-based-meat-milk/（建議）', '新建文章', '新建'),
 'Blog：F1 車手飲食＋觀賽派對到會': ('/blog/f1-driver-diet-watch-party/（建議）', '新建文章（貼 WORDPRESS 版）', '新建'),
 '野餐 Landing': ('/catering/picnic/（建議）', '新建頁面', '新建'),
 'Blog：食物保暖用品（thermB1）': ('（待定）', '新建文章', '新建'),
 'Blog：保鮮用品（thermB2）': ('（待定）', '新建文章', '新建'),
 'Blog：保溫杯、保溫瓶（thermB3）': ('（待定）', '新建文章', '新建'),
 '訂製食物 Landing': ('/catering/custom-printed-food/（建議）', '新建頁面', '新建'),
 '中秋 Landing（每年沿用）': ('/catering/mid-autumn/（建議）', '新建頁面', '新建'),
 '萬聖節 Landing（每年沿用）': ('/catering/halloween/（建議）', '新建頁面', '新建'),
}
_AREA = {'荃灣': ('catering-tsuenwan', '荃灣到會推介'), '元朗': ('catering-yuen-long', '元朗到會推介'), '沙田': ('catering-sha-tin', '沙田到會推介'),
 '屯門': ('catering-tuen-mun', '屯門到會推介'), '北角': ('catering-north-point', '北角到會推介'), '鰂魚涌': ('catering-quarry-bay', '鰂魚涌到會推介'),
 '觀塘': ('catering-kwun-tong', '觀塘到會推介'), '旺角': ('catering-mong-kok', '旺角到會推介'), '深水埗': ('catering-sham-shui-po', '深水埗到會推介'),
 '尖沙咀': ('catering-tsim-sha-tsui', '尖沙咀到會推介'), '中環': ('catering-central', '中環到會推介'), '銅鑼灣': ('catering-causewaybay', '銅鑼灣到會推介'),
 '灣仔': ('catering-wan-chai', '灣仔到會推介'), '西營盤': ('catering-sai-ying-pun', '西營盤到會推介'), '九龍城': ('catering-kowloon-city', '九龍城到會推介')}
for _k, (_s, _q) in _AREA.items(): WP['地區頁：' + _k] = (f'/{_s}/', _q, '頁面')
DONE = [  # 已完成：(名稱, 網址, 完成日期)
 ('送貨需知（中文）', '/delivery/', '2026-10-31'), ('送貨需知（英文）', '/en/delivery/', '2026-10-31'),
 ('聯絡我們（中＋英）', '/contacts/', '2026-10-29'),
 ('Blog：船P必備清單', '/blog/boat-party-catering-guide/', '已上線'), ('Blog：激光打印食物', '/blog/laser-printed-food-party/', '已上線'),
 ('Blog：香港野餐好去處', '/blog/hong-kong-picnic-spots-picnic-box/', '已上線'), ('Blog：中秋到會 2026', '/blog/mid-autumn-catering-hong-kong/', '已上線'),
 ('Blog：萬聖節到會 2026', '/blog/halloween-catering-hong-kong/', '已上線'),
 ('全站英文 Meta、英文 H1、英文選單', '/en/', '2026-10-29'), ('Blog 只留中文版（/en/blog/ 301）', '/blog/', '2026-10-29'),
]

DRAFT = {  # 製作中的草稿：(草稿網址, 狀態)
 'Blog：初一十五食齋懶人包（vegB3）': ('https://expandsolutionshk.github.io/kitchenao-edm/vegetarian-blog/b3-chu-yat-sap-ng-guide.html', '內文及 KV（A 媒體封面風）完成，有 WORDPRESS 版，可上載'),
 'Blog：F1 車手飲食＋觀賽派對到會': ('https://expandsolutionshk.github.io/kitchenao-edm/f1-blog/f1-driver-diet-watch-party.html', '內文完成，有 WORDPRESS 版，未上線'),
 'Blog：吃素好處與營養（vegB4）': ('https://expandsolutionshk.github.io/kitchenao-edm/vegetarian-blog/b4-vegetarian-nutrition.html', '初稿，未有 WORDPRESS 版及 KV'),
 'Blog：一週素食菜單（vegB5）': ('https://expandsolutionshk.github.io/kitchenao-edm/vegetarian-blog/b5-weekly-vegetarian-menu.html', '初稿，未有 WORDPRESS 版及 KV'),
}
PIN_O = ['公司到會 18404 上載＋live check', '客製化紀念品訂製服務：改錯']   # 已做好待上載／有錯要即改
PIN_N = ['Blog：初一十五食齋懶人包（vegB3）', '聖誕到會 Landing page（中文）', '聖誕到會 Landing page（英文）', 'Blog：F1 車手飲食＋觀賽派對到會', 'Blog：香港人聖誕餐吃甚麼？', 'Blog：Annual Dinner 籌備全攻略（NB1）', 'Blog：吃素好處與營養（vegB4）', 'Blog：一週素食菜單（vegB5）']  # 季節 deadline
def _order(kind, pins):
    L = [r for r in _R if r['k'] == kind]
    head = [next(r for r in L if r['n'] == p) for p in pins]
    rest = sorted([r for r in L if r['n'] not in pins], key=lambda r: -r['gain'])
    out = head + rest
    for i, r in enumerate(out, 1):
        r['id'] = f"{kind}{i}"; r['pin'] = r['n'] in pins
    return out
OLDQ, NEWQ = _order('O', PIN_O), _order('N', PIN_N)
# 已上線：保留編號，從排程移除，放入「已完成」
LAUNCHED = {'Blog：素食種類全攻略（vegB2）': ('/blog/vegetarian-types-guide/', '2026-11-01 前'),
            'Blog：Vegan／Vegetarian 中文（vegB6）': ('/blog/vegan-vegetarian-meaning/', '2026-11-01 前')}
for _r in OLDQ + NEWQ:
    if _r['n'] in LAUNCHED: DONE.append((f"{_r['id']} {SER.get(_r['n'], '')}｜{_r['n']}", *LAUNCHED[_r['n']]))
OLDQ = [r for r in OLDQ if r['n'] not in LAUNCHED]; NEWQ = [r for r in NEWQ if r['n'] not in LAUNCHED]
TODAY = (_dt.date(2026, 11, 1), ['公司到會 18404 上載＋live check'], ['Blog：初一十五食齋懶人包（vegB3）'])  # 今日做的項目
def _days(start, n):
    d, out = start, []
    while len(out) < n:
        if d.weekday() < 5: out.append(d)
        d += _dt.timedelta(days=1)
    return out
_TO = [r for r in OLDQ if r['n'] in TODAY[1]]; _TN = [r for r in NEWQ if r['n'] in TODAY[2]]
OLDQ = [r for r in OLDQ if r not in _TO]; NEWQ = [r for r in NEWQ if r not in _TN]
_n = max((len(OLDQ) + 1) // 2, len(NEWQ))
_W = '一二三四五六日'
_VC = {'高': '#3BAA5C', '中': '#C8A24A', '低': '#8A8172'}
def _cell(r):
    tag = f'<span class="tg">{r["id"]}</span>' + (f'<span class="tg s">{SER[r["n"]]}</span>' if r['n'] in SER else '')
    dr = DRAFT.get(r['n'])
    pin = (' <span class="pinf" style="color:#2B7BD0">📝 已有草稿</span>' if dr else ' <span class="pinf">📌 deadline／已完成</span>') if r['pin'] else ''
    drl = f'<div class="wp">📝 草稿：<a href="{dr[0]}" target="_blank">預覽</a>｜{_h.escape(dr[1])}</div>' if dr else ''
    u, q, where = WP.get(r['n'], ('', '', ''))
    href = (B + u) if u.startswith('/') and '（' not in u else ''
    ul = (f'<a href="{href}" target="_blank">{_h.escape(u)}</a>' if href else _h.escape(u))
    wp = (f'<div class="wp">🔗 {ul}<br>WP 搜尋（{where}）：<code class="cp" title="按一下複製">{_h.escape(q)}</code></div>' if u else '')
    return (f'{tag}<b>{_h.escape(r["n"])}</b>{pin}{wp}{drl}<small>+{r["gain"]:,} click／年｜生意價值 '
            f'<i style="color:{_VC[r["val"]]};font-style:normal;font-weight:800">{r["val"]}</i>｜{_h.escape(r["note"])}</small>')
_srow = []
_d0 = TODAY[0]
_srow.append(f'<tr class="today"><td class="nw"><b>今日</b><br>{_d0.month}/{_d0.day}（{_W[_d0.weekday()]}）</td><td>' + ''.join(f'<div class="it">{_cell(r)}</div>' for r in _TO) + '</td><td>' + ''.join(f'<div class="it">{_cell(r)}</div>' for r in _TN) + '</td></tr>')
for i, d in enumerate(_days(_d0 + _dt.timedelta(days=1), _n)):
    o = OLDQ[i*2:i*2+2]; nw = NEWQ[i] if i < len(NEWQ) else None
    oc = '<div class="it">' + '</div><div class="it">'.join(_cell(r) for r in o) + '</div>' if o else '—'
    nc = '<div class="it">' + _cell(nw) + '</div>' if nw else '—'
    _srow.append(f'<tr><td class="nw">{d.month}/{d.day}（{_W[d.weekday()]}）</td><td>{oc}</td><td>{nc}</td></tr>')
DONE_HTML = ('<div class="pri"><h2>✅ 已完成（' + str(len(DONE)) + ' 項）</h2><div class="card"><table><thead><tr><th>頁面</th><th>網址</th><th>完成</th></tr></thead><tbody>' +
  ''.join(f'<tr><td><b>{_h.escape(n)}</b></td><td><a href="{B}{u}" target="_blank">{B}{_h.escape(u)}</a></td><td class="nw">{d}</td></tr>' for n, u, d in DONE) + '</tbody></table></div></div>')
SCHED_HTML = DONE_HTML + ('<div class="pri"><h2>每日排程（每個工作日 2 篇舊文＋1 篇新文）</h2><p class="pn">'
  '<b>排序：</b>📌 先做有 deadline 或已完成待上載的項目，📝 已有草稿的接著完成，其餘按「預計每年增加點擊」由高至低。'
  '<b>編號：</b>O＝舊文／舊頁，N＝新文／新頁；系列另加標籤（例如 xmasB2、vegB3、thermB1）。<br>'
  '<b>點擊估算：</b>GSC 12 個月曝光（新文用 Keyword Planner 月搜×12）× 目標排名 CTR − 現有點擊。目標排名：現時 #1–10 → #3；#11–20 → #5；#21–30 → #8；#30 以後或新文 → #10；大字為主的資訊文 → #20。只作排序參考。'
  '<br><b>生意價值：</b>高＝交易型頁面（會帶來查詢及訂單）；低＝資訊型 Blog（點擊多但轉化低）。'
  f'<br>舊文 {len(OLDQ)} 項、新文 {len(NEWQ)} 項，約 {_n} 個工作日完成（只計星期一至五）。已移除：船P必備清單、激光打印食物、野餐好去處、中秋及萬聖節 Blog（已上線）。</p>'
  '<div class="card"><table><thead><tr><th>日期</th><th>舊文／舊頁（2 篇）</th><th>新文／新頁（1 篇）</th></tr></thead><tbody>' + ''.join(_srow) + '</tbody></table></div></div>')
PRI_HTML = PRI_HTML.replace('<div class="pri">', SCHED_HTML + '<div class="pri">', 1)
PRI_CSS += '.pri tr.today td{background:#FFF8E6}.pri .wp{font-size:13px;margin:3px 0 2px;color:#4A4238}.pri .wp code{background:#FFF4D6;border:1px solid #E9D9AE;border-radius:6px;padding:1px 6px;cursor:pointer;font-family:inherit}.pri .wp code.ok{background:#E3F4E8;border-color:#3BAA5C}.pri .tg{display:inline-block;background:#1A1A1A;color:#F7CE46;font-size:12px;font-weight:800;border-radius:6px;padding:1px 7px;margin-right:6px}.pri .tg.s{background:#E3F1FB;color:#2B7BD0}.pri .it{padding:4px 0}.pri .it+.it{border-top:1px dashed #EEE6D6}.pri .pinf{font-size:12px;color:#E2574C;font-weight:700}'

# ---------- render ----------
CLS = ['classDef new fill:#E3F4E8,stroke:#3BAA5C', 'classDef old fill:#FFF4D6,stroke:#C8A24A', 'classDef bad fill:#FDE2E1,stroke:#E2574C',
       'classDef ok fill:#E3F1FB,stroke:#2B7BD0', 'classDef grp fill:#1A1A1A,stroke:#1A1A1A,color:#F7CE46']
def mm(d):
    L = [f"flowchart {d['dir']}"]
    for n in d['nodes']:
        url = n['url'] or '（未有 URL）'
        lab = (f"<span class='t'>{n['tag']}</span><br/><b>{n['name']}</b>" + ('' if n['tag'] == '分組' else f"<br/><span class='u'>{url}</span>")).replace('"', "'")
        L.append(f'{n["id"]}["{lab}"]:::{n["cls"]}')
    L += d['edges']
    for n in d['nodes']:
        if n['url']: L.append(f'click {n["id"]} "{n["url"]}" _blank')
    L += CLS
    return '\n'.join(L)

V = {k: mm(v) for k, v in D.items()}
html = '''<!DOCTYPE html>
<html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Kitchen AO Site Structure 架構圖</title>
<script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script>
<style>
body{margin:0;font-family:-apple-system,"PingFang HK","Noto Sans HK",sans-serif;background:#FBF6EC;color:#2a2620}
header{background:#1A1A1A;color:#F7CE46;padding:18px 24px}header h1{margin:0;font-size:20px}header p{margin:4px 0 0;color:#C9BFA8;font-size:13px}
nav{display:flex;gap:8px;flex-wrap:wrap;padding:14px 24px;background:#fff;border-bottom:1px solid #eee;position:sticky;top:0;z-index:5}
nav button{border:1.5px solid #1A1A1A;background:#fff;border-radius:30px;padding:7px 14px;font:inherit;font-size:14px;cursor:pointer}
nav button.on{background:#C8A24A;border-color:#C8A24A;font-weight:800}
.dd{position:relative}.dd>button:after{content:' ▾'}.dd .menu{display:none;position:absolute;top:110%;left:0;background:#fff;border:1.5px solid #1A1A1A;border-radius:14px;padding:6px;min-width:150px;box-shadow:0 8px 24px rgba(0,0,0,.12);z-index:9}.dd.open .menu{display:block}.dd .menu button{display:block;width:100%;text-align:left;border:0;border-radius:10px;margin:2px 0}.dd .menu button.on{background:#C8A24A}
section{display:none;padding:20px 24px 60px}section.on{display:block}
.card{background:#fff;border-radius:16px;padding:16px;box-shadow:0 2px 12px rgba(0,0,0,.05);overflow:auto}
.legend{font-size:13px;color:#6b6252;margin:0 0 12px}.legend span{display:inline-block;padding:2px 10px;border-radius:8px;margin-right:6px}
.kwlink{display:inline-block;margin:0 0 10px;background:#1A1A1A;color:#F7CE46;font-weight:700;font-size:15px;padding:8px 16px;border-radius:20px;text-decoration:none}.kwlink:hover{background:#C8A24A;color:#1A1A1A}
.new{background:#E3F4E8}.old{background:#FFF4D6}.bad{background:#FDE2E1}.ok{background:#E3F1FB}
.mermaid .nodeLabel,.mermaid .nodeLabel *{font-size:16px!important;line-height:1.35}.mermaid .nodeLabel b{font-size:17px!important}.mermaid .u{font-size:13px!important;color:#444;word-break:break-all}.mermaid .node{cursor:pointer}.mermaid .t{display:inline-block;font-size:13px!important;font-weight:700;color:#fff!important;background:#1A1A1A;border-radius:10px;padding:2px 9px;margin-bottom:4px}.mermaid .grp .t{background:#C8A24A;color:#1A1A1A!important}
__PRICSS__
</style></head><body>
<header><h1>Kitchen AO 網站架構圖（Site Structure）</h1><p>每個格子顯示完整 URL，按一下可打開該頁｜由主表整理，2026-10-19 更新（素食加入 6 篇 Blog 及 KW 分配頁）</p></header>
<nav id="nav"></nav><div id="views"></div>
<script>
const V = __V__;
const PRI = __PRI__;
mermaid.initialize({startOnLoad:false,securityLevel:'loose',themeVariables:{fontSize:'17px'},flowchart:{htmlLabels:true,curve:'basis',wrappingWidth:460,nodeSpacing:40,rankSpacing:55}});
const nav=document.getElementById('nav'),views=document.getElementById('views');
const GROUPS={'Seasonal':['中秋節','萬聖節','聖誕節']};const KWPAGE={'素食':'vegetarian-kw.html','聖誕節':'xmas-kw.html'};const LINKS={};const SLINKS={};const LABEL={'素食':'🥦 素食','聖誕節':'🎄 聖誕節'};const inGrp={};for(const [g,ks] of Object.entries(GROUPS))ks.forEach(k=>inGrp[k]=g);
const made={};let first=null;
const BTN={};function show(b,s,top,k){if(k&&history.replaceState)history.replaceState(null,'','#'+encodeURIComponent(k));document.querySelectorAll('nav button').forEach(x=>x.classList.remove('on'));document.querySelectorAll('section').forEach(x=>x.classList.remove('on'));b.classList.add('on');if(top)top.classList.add('on');s.classList.add('on');document.querySelectorAll('.dd').forEach(d=>d.classList.remove('open'));const pre=s.querySelector('pre');if(!pre.dataset.done){mermaid.run({nodes:[pre]}).then(()=>pre.dataset.done=1);}}
for(const [k,code] of Object.entries(V)){
  const s=document.createElement('section');
  s.innerHTML='<p class="legend"><span class="new">綠＝新建／建議新增</span><span class="old">黃＝要整理</span><span class="ok">藍＝已有</span><span class="bad">紅＝緊急</span></p><div class="card"><pre class="mermaid"></pre></div>';
  s.querySelector('pre').textContent=code;views.appendChild(s);
  if(k==='全站總覽'){const d=document.createElement('div');d.innerHTML=PRI;s.insertBefore(d,s.firstChild);}
  (SLINKS[k]||[]).forEach(([t,u])=>{const a=document.createElement('a');a.href=u;a.textContent=t;a.className='kwlink';s.insertBefore(a,s.firstChild);});
  const b=document.createElement('button');b.textContent=LABEL[k]||k;let top=null;
  const g=inGrp[k];
  if(g){if(!made[g]){const d=document.createElement('div');d.className='dd';const t=document.createElement('button');t.textContent=g;t.onclick=e=>{e.stopPropagation();d.classList.toggle('open');};const m=document.createElement('div');m.className='menu';d.append(t,m);nav.appendChild(d);made[g]={d,t,m};}
    made[g].m.appendChild(b);top=made[g].t;
    (LINKS[g]||[]).forEach(([t,u])=>{if(made[g]['l'+u])return;const a=document.createElement('button');a.textContent=t;a.onclick=e=>{e.stopPropagation();location.href=u;};made[g].m.appendChild(a);made[g]['l'+u]=1;});}
  else nav.appendChild(b);
  b.onclick=e=>{e.stopPropagation();if(KWPAGE[k]){location.href=KWPAGE[k];return;}show(b,s,top,k);};BTN[k]=b;
  if(!first)first=b;
}
{const h=decodeURIComponent(location.hash.slice(1));if(KWPAGE[h])location.replace(KWPAGE[h]);else setTimeout(()=>(BTN[h]||first).click(),0);}
const ck=document.createElement('button');ck.textContent='🏢 核心頁面 KW 分配';ck.onclick=e=>{e.stopPropagation();location.href='core-pages-kw.html';};nav.appendChild(ck);
document.addEventListener('click',()=>document.querySelectorAll('.dd').forEach(d=>d.classList.remove('open')));
document.addEventListener('click',e=>{const c=e.target.closest('code.cp');if(!c)return;navigator.clipboard&&navigator.clipboard.writeText(c.textContent);c.classList.add('ok');setTimeout(()=>c.classList.remove('ok'),1200);});
window.addEventListener('hashchange',()=>{const h=decodeURIComponent(location.hash.slice(1));if(KWPAGE[h])location.href=KWPAGE[h];else if(BTN[h])BTN[h].click();});
</script></body></html>'''
(HERE / 'index.html').write_text(html.replace('__V__', json.dumps(V, ensure_ascii=False)).replace('__PRI__', json.dumps(PRI_HTML, ensure_ascii=False)).replace('__PRICSS__', PRI_CSS), encoding='utf-8')
(HERE / 'diagrams.json').write_text(json.dumps(V, ensure_ascii=False), encoding='utf-8')
print('ok', {k: len(v['nodes']) for k, v in D.items()})
