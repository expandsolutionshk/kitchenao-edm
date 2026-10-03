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
        '/sample-page/': '問題頁', '/ba620e385336-htm/': '問題頁（被入侵）', '/66695d0f41db-htm/': '問題頁（被入侵）', '/': '首頁'}
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
 N('P1', '派對套餐', '/product-category/party/'), N('P2', '人數選餐', '/product-category/party-set-by-people/'), N('P3', '單點', '/product-category/a-la-carte/'),
 N('P4', '商務活動', '/product-category/商務活動/'), N('P5', '配菜', '/product-category/配菜/'), N('P6', '派對用品', '/product-category/party-supplies/'),
 N('P7', '中秋套餐（slug 帶年份）', '/product-category/中秋佳節團圓套餐-2026/', 'old'),
 N('BL', 'Blog（13 篇）', '/blog/'), N('D', '地區 hub（要補內容）', '/地區到會分類/', 'old'),
 N('S1', '送貨需知', '/delivery/'), N('S2', '購買流程', '/foodbook/'), N('S3', '常見問題', '/常見問題/'), N('S4', '聯絡我們', '/contacts/'), N('S5', '報價查詢', '/catering-quote-enquiry/'),
 N('T1', '關於 Kitchen AO', '/about-kitchenao/'), N('T2', '客人好評', '/客人好評/'), N('T3', '合作夥伴', '/合作伙伴/'), N('T4', '精選圖庫', '/精選圖庫/'),
 N('V1', '公司到會', '/corporate-catering-hk/'), N('V2', '企業商務到會', '/business-event/'), N('V3', '香港到會推介', '/hong-kong-catering-recommendation/'),
 N('V4', '服務概覽（幾乎空白）', '/服務概覽/', 'old'), N('V5', '飲品及雞尾酒服務', '/飲品及雞尾酒服務/'),
 N('X1', '船河舊 landing', '/boat-trip-bldg/', 'old'), N('X2', '派對舊 landing', '/partyfood-bldg/', 'old'), N('X3', '小食舊 landing', '/snacks-bldg/', 'old'),
 N('X4', '範例頁面（刪除）', '/sample-page/', 'bad'), N('HK1', '⚠️ 被入侵頁面', '/ba620e385336-htm/', 'bad'), N('HK2', '⚠️ 被入侵頁面', '/66695d0f41db-htm/', 'bad'),
], edges=['H --> C', 'C --> B1 & B2 & B3 & B4 & B5 & B6 & B7 & B8', 'H --> P1 & P2 & P3 & P4 & P5 & P6 & P7', 'H --> BL', 'H --> D',
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
 N('H', '首頁', '/'), N('L', '素食 landing（新）', '/catering/vegetarian/', 'new'),
 N('C1', '「素」味人生套餐分類', '/product-category/party/vegetarians-set/'),
 N('V1', '6–8 人', '/product/ao-6-8pax-vegetarian-life/'), N('V2', '10–12 人', '/product/ao-10-12pax-vegetarian-life/'),
 N('V3', '16–19 人', '/product/ao-16-19pax-vegetarian-life/'), N('V4', '22–26 人', '/product/ao-22-26pax-vegetarian-life/'),
 N('C2', '素食單品（新分類）', '/product-category/a-la-carte/vegetarian/', 'new'),
 N('I1', '惹味蒜香焗茄子', '/product/a3900-grilled-garlic-eggplant/', 'old'), N('I2', '蒜香炒翠玉瓜', '/product/a62-stir-fried-zucchini-with-garlic-1-pounds/', 'old'),
 N('I3', '忌廉白汁菠菜', '/product/a59-spinach-with-cream-sauce-1-pounds/', 'old'), N('I4', '手壓香濃薯蓉', '/product/a61-hand-pressed-sweet-potato-puree-1-pounds/', 'old'),
 N('BG', '素食到會 blog（要更新）', '/blog/vegetarian-catering-hong-kong/', 'old'),
 N('T1', '舊 tag（已 301）', '/tag/素食到會/'), N('T2', 'Blog tag 頁（建議 noindex）', '/blog/tag/素食到會/', 'old'),
], edges=['H --> L', 'L --> C1', 'C1 --> V1 & V2 & V3 & V4', 'L --> C2', 'C2 --> I1 & I2 & I3 & I4', 'L <--> BG', 'T1 -.-> C1', 'BG -.-> T2'])

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
 N('H', '首頁', '/'), N('L', '萬聖節 landing（新）', '/catering/halloween/', 'new'), N('N1', '萬聖節套餐（未有）', '', 'new'),
 N('C1', '美食派對（暫代）', '/product-category/party/foot-party/'), N('B1', '萬聖節 blog（H1 要修正）', '/blog/halloween-catering-hong-kong/', 'old'),
], edges=['H --> L', 'L --> N1 & C1', 'L <--> B1'])

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
section{display:none;padding:20px 24px 60px}section.on{display:block}
.card{background:#fff;border-radius:16px;padding:16px;box-shadow:0 2px 12px rgba(0,0,0,.05);overflow:auto}
.legend{font-size:13px;color:#6b6252;margin:0 0 12px}.legend span{display:inline-block;padding:2px 10px;border-radius:8px;margin-right:6px}
.new{background:#E3F4E8}.old{background:#FFF4D6}.bad{background:#FDE2E1}.ok{background:#E3F1FB}
.mermaid .nodeLabel,.mermaid .nodeLabel *{font-size:16px!important;line-height:1.35}.mermaid .nodeLabel b{font-size:17px!important}.mermaid .u{font-size:13px!important;color:#444;word-break:break-all}.mermaid .node{cursor:pointer}.mermaid .t{display:inline-block;font-size:13px!important;font-weight:700;color:#fff!important;background:#1A1A1A;border-radius:10px;padding:2px 9px;margin-bottom:4px}.mermaid .grp .t{background:#C8A24A;color:#1A1A1A!important}
</style></head><body>
<header><h1>Kitchen AO 網站架構圖（Site Structure）</h1><p>每個格子顯示完整 URL，按一下可打開該頁｜由主表整理，2026-10-03</p></header>
<nav id="nav"></nav><div id="views"></div>
<script>
const V = __V__;
mermaid.initialize({startOnLoad:false,securityLevel:'loose',themeVariables:{fontSize:'17px'},flowchart:{htmlLabels:true,curve:'basis',wrappingWidth:460,nodeSpacing:40,rankSpacing:55}});
const nav=document.getElementById('nav'),views=document.getElementById('views');let i=0;
for(const [k,code] of Object.entries(V)){
  const b=document.createElement('button');b.textContent=k;nav.appendChild(b);
  const s=document.createElement('section');
  s.innerHTML='<p class="legend"><span class="new">綠＝新建／建議新增</span><span class="old">黃＝要整理</span><span class="ok">藍＝已有</span><span class="bad">紅＝緊急</span></p><div class="card"><pre class="mermaid"></pre></div>';
  s.querySelector('pre').textContent=code;views.appendChild(s);
  b.onclick=async()=>{document.querySelectorAll('nav button').forEach(x=>x.classList.remove('on'));document.querySelectorAll('section').forEach(x=>x.classList.remove('on'));b.classList.add('on');s.classList.add('on');const pre=s.querySelector('pre');if(!pre.dataset.done){await mermaid.run({nodes:[pre]});pre.dataset.done=1;}};
  if(i++===0)setTimeout(()=>b.click(),0);
}
</script></body></html>'''
(HERE / 'index.html').write_text(html.replace('__V__', json.dumps(V, ensure_ascii=False)), encoding='utf-8')
(HERE / 'diagrams.json').write_text(json.dumps(V, ensure_ascii=False), encoding='utf-8')
print('ok', {k: len(v['nodes']) for k, v in D.items()})
