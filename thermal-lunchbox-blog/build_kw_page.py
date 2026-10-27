# -*- coding: utf-8 -*-
"""食物保暖用品／保鮮用品 KW 分配架構頁 → ../site-structure/thermal-kw.html
資料：kw_classified_v2.json（integrate.py 產生）＋ content.PRODUCTS
"""
import json, os, html
from content import PRODUCTS, PRICE_DATE, PROD_EXTRA

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'site-structure', 'thermal-kw.html')
R = json.load(open(os.path.join(HERE, 'kw_classified_v2.json'), encoding='utf-8'))
E = html.escape
fv = lambda v: '—' if v is None else f'{v:,}'

PG = {'Blog 1｜食物保暖用品篇': 'B1', 'Blog 2｜保鮮用品篇（建議另寫）': 'B2', '只作承接（不作目標）': 'H',
      '暫不使用（冰袋、冰磚）': 'Z', '不建議（另一主題：烘焙）': 'X', '不建議（暖包多指暖手包）': 'X'}
PAGES = {'B1': 'Blog 1｜食物保暖用品篇', 'B2': 'Blog 2｜保鮮用品篇', 'H': '只作承接（不作目標）',
         'Z': '暫不使用（冰袋、冰磚）', 'X': '不建議（烘焙紙、暖包）'}
for r in R:
    r['pg'] = PG[r['blog']]

TGT = ('全文主關鍵字', '主要', '次要', '長尾', 'FAQ')
ROLE_ORD = {'全文主關鍵字': 0, '主要': 1, '次要': 2, '長尾': 3, 'FAQ': 4}

# ---------------- 頁面設定 ----------------
CARDS = [
 dict(pg='B1', st='新文章', title='Blog 1｜食物保暖用品篇', url='/blog/thermal-lunch-box-guide/', ty='Blog（商業調查）',
      h1='保溫飯盒推介 2026：保溫便當盒、燜燒壺、加熱飯盒及保溫袋怎樣揀？學生及上班族帶飯指南',
      title_tag='【2026】保溫飯盒推介｜象印、虎牌、膳魔師保溫便當盒、燜燒壺及保溫袋比較',
      meta='保溫飯盒怎樣揀？比較象印、虎牌、膳魔師保溫便當盒及燜燒壺的保溫時間、容量及價錢，附加熱飯盒、保溫袋選購重點及學生帶飯建議。',
      focus='保溫飯盒（副：保溫飯盒推介、保溫便當盒）',
      note='只講「帶飯保溫」：保溫飯盒、燜燒壺、加熱飯盒、保溫袋。重點長尾：保溫飯盒推介、學生保溫飯盒、象印保溫飯盒、燜燒壺與保溫壺分別。保溫壺、保溫杯、保溫瓶（飲品）只用一個 H3 承接，不作目標。結尾以「派對及到會食物怎樣保溫？」帶到 Kitchen AO。',
      links=['→ Blog 2', '→ 派對用品：餐具及暖貼加配', '→ 派對到會套餐']),
 dict(pg='B2', st='新文章（建議另寫）', title='Blog 2｜保鮮用品篇', url='/blog/food-storage-wrap-bags-containers/', ty='Blog（資訊＋商業調查）',
      h1='保鮮紙、密實袋及保鮮盒怎樣揀？2026 保鮮用品推介及微波爐使用須知',
      title_tag='保鮮紙、密實袋、保鮮盒推介 2026｜可以入微波爐嗎？佳能 Glad、真空保鮮比較',
      meta='保鮮紙可以入微波爐嗎？密實袋尺寸怎樣揀？比較佳能 Glad 保鮮紙、Press\'n Seal、密實袋、玻璃及真空保鮮盒，附雪櫃收納及備餐保鮮貼士。',
      focus='保鮮紙（副：密實袋、保鮮盒）',
      note='這類大字的搜尋結果首頁多為 HKTVmall、惠康、YOHO 產品分類頁，所以文章以「可以入微波爐嗎」「可以蒸嗎」「尺寸」等問題型字切入，排名機會較大。',
      links=['→ Blog 1', '→ Chill 一下野餐盒']),
 dict(pg='H', st='不作目標', title='只作承接：飲品保溫壺／保溫杯／保溫瓶', url='', ty='—', h1='', title_tag='', meta='', focus='',
      note='搜尋量大（保溫壺 2,400、保溫杯 2,400、保溫瓶 1,600、象印保温壺 1,900），但搜尋者想買飲品水壺。只在 Blog 1 H3「燜燒壺與保溫壺有甚麼分別？」自然提及。', links=[]),
 dict(pg='Z', st='暫不使用', title='暫不使用：冰袋、冰磚', url='', ty='—', h1='', title_tag='', meta='', focus='',
      note='屬野餐及露營用品，暫時不放入任何頁面。', links=[]),
 dict(pg='X', st='不建議', title='不建議：烘焙紙、暖包', url='', ty='—', h1='', title_tag='', meta='', focus='',
      note='錫紙、牛油紙、烘焙紙屬烘焙主題；暖包多指暖手包，而且只在冬季有量。', links=[]),
]

# ---------------- 大綱 ----------------
OUTLINE = {
 'B1': [
  ('H2 1｜保溫飯盒、燜燒壺、加熱飯盒及保溫袋有甚麼分別？', None,
   ['開首 40 至 60 字快答，下面用 4 張類型卡（星星評分）作總覽，爭取精選摘要。']),
  ('H2 2｜保溫飯盒／保溫便當盒推介：材質、分層及品牌比較', 'C1',
   ['H3 2.1 保溫飯盒怎樣揀？不銹鋼、玻璃內盒及可微波內盒的分別', 'H3 2.2 學生保溫飯盒：小學生及兒童要注意甚麼？',
    'H3 2.3 象印、虎牌、膳魔師保溫飯盒邊隻好？', '產品段落 ×3']),
  ('H2 3｜燜燒壺、燜燒杯與湯壺：帶湯、粥及燜飯', 'C2',
   ['H3 3.1 燜燒壺與保溫壺有甚麼分別？（承接保溫壺、保溫杯、保溫瓶）', 'H3 3.2 燜燒壺用法及帶飯食譜', '產品段落 ×3']),
  ('H2 4｜加熱飯盒、電熱飯盒與自熱飯盒：辦公室沒有微波爐怎麼辦？', 'C3',
   ['H3 4.1 加熱飯盒與保溫飯盒有甚麼分別？', 'H3 4.2 USB、充電式及插電式加熱飯盒比較', '產品段落 ×3']),
  ('H2 5｜保溫袋、保冷袋與保溫箱：延長保溫及保冷時間', 'C7',
   ['H3 5.1 飯盒保溫袋可以撐多久？', 'H3 5.2 外賣、野餐及派對用保溫箱', '產品段落 ×3']),
  ('H2 6｜派對及到會食物怎樣保溫？', 'C8',
   ['Kitchen AO 轉化段：保溫碗、保溫盤、暖貼的用法，連去「餐具及暖貼加配」及到會套餐']),
  ('H2 7｜常見問題', 'FAQ', ['FAQPage schema，每題先用 1 至 2 句直接回答']),
 ],
 'B2': [
  ('H2 1｜保鮮紙、保鮮袋、保鮮盒用途有甚麼分別？', None, ['開首快答＋3 張類型卡（星星評分）']),
  ('H2 2｜保鮮紙、保鮮膜與保鮮貼：可以入微波爐或蒸嗎？', 'C5',
   ['H3 2.1 保鮮紙可以入微波爐嗎？可以蒸嗎？', 'H3 2.2 佳能與 Glad 是同一品牌嗎？Press\'n Seal 是甚麼？', '產品段落 ×3']),
  ('H2 3｜保鮮袋、密實袋與真空袋：尺寸及耐熱怎樣揀？', 'C6',
   ['H3 3.1 保鮮袋與密實袋有甚麼分別？', 'H3 3.2 密實袋尺寸、耐熱及慢煮用法', '產品段落 ×3']),
  ('H2 4｜保鮮盒、密實盒與真空保鮮盒：備餐及雪櫃收納', 'C4',
   ['H3 4.1 玻璃、塑膠保鮮盒哪種可以微波？', 'H3 4.2 抽真空機及真空保鮮盒值得買嗎？', '產品段落 ×3']),
  ('H2 5｜常見問題', 'FAQ', ['FAQPage schema']),
 ],
}

# 類型卡（總覽）
TYPES = {
 'B1': [('保溫飯盒／保溫便當盒', [5, 2, 3], '小學生帶飯、無微波爐的上班族'),
        ('燜燒壺／燜燒杯', [5, 4, 5], '湯水、粥品、免火燜熟輕食'),
        ('加熱飯盒（USB／充電）', [5, 1, 3], '外勤工作、辦公室沒有微波爐'),
        ('保溫袋／保溫箱', [3, 4, 2], '配合飯盒延長保溫、野餐及派對')],
 'B2': [('保鮮紙／保鮮貼', [3, 3, 2], '碗碟封口、短時間保存'),
        ('保鮮袋／密實袋', [4, 4, 2], '急凍、醃肉、分裝'),
        ('保鮮盒／真空保鮮盒', [4, 5, 4], '備餐、雪櫃收納、翻熱')],
}
TYPE_CRIT = {'B1': ['保熱能力', '保冷／保鮮', '防漏密封'], 'B2': ['保鮮效果', '密封防漏', '微波／耐熱']}

# 產品評分：None＝官方未列／不適用
CRIT = {'B1': ['保熱能力', '保冷能力', '防漏密封', '份量'], 'B2': ['保鮮效果', '密封防漏', '微波爐適用', '性價比']}
RATE = {
 'https://www.hktvmall.com/p/H0569001_S_GJE-SL-NC09-ST': ([4, 2, 3, 4], '上班族（有微波爐可再翻熱）、食量中等', '官方未列保溫時數；內盒可微波翻熱'),
 'https://www.hktvmall.com/p/H5036001_S_LXB-A100-XC': ([5, 2, 3, 4], '中學生、上班族，飯和餸分開裝', '6 小時後保持 50°C 以上'),
 'https://www.thermos.com.hk/product/d004b821-b818-4163-b143-2421736cc46f': ([5, 3, 4, 3], '小學生、有湯汁的餸菜', '6 小時保持 60°C 以上'),
 'https://www.thermos.com.hk/product/ba9dc661-65d6-4a80-9a22-31aff4eb8d96': ([4, 4, 5, 2], '小朋友、一人份湯或粥', '6 小時：熱 59°C 以上／冷 11°C 以下'),
 'https://www.hktvmall.com/p/H0569001_S_GJE-SW-EAE50-AB': ([5, 5, 5, 3], '上班族燜燕麥、粥', '6 小時：熱 64°C 以上／冷 10°C 以下'),
 'https://www.hktvmall.com/p/H5036001_S_MCJ-K075-HC': ([5, 5, 5, 4], '食量較大、燜飯或湯麵', '6 小時：熱 70°C 以上／冷 8°C 以下'),
 'https://www.yohohongkong.com/zh-hk/product/98338': ([5, 1, 3, 5], '辦公室沒有微波爐、外勤', '50W 主動加熱，可充電'),
 'https://www.yohohongkong.com/zh-hk/product/188590': ([4, 1, 3, 5], '外勤、需要充電便攜', '40W 主動加熱，3200mAh'),
 'https://www.yohohongkong.com/zh-hk/product/492130': ([4, 1, 3, None], '外勤、短途出行', '可充電，多段溫度；容量未有標示'),
 'https://www.thermos.com.hk/p/REK-001H-BK': ([3, 3, None, 3], '已有 Thermos 食物罐的用家', '配合食物罐使用，延長保溫'),
 'https://www.yohohongkong.com/zh-hk/product/80121': ([1, 5, 3, 3], '夏天帶沙律、水果、凍飲', '袋身內置凝膠，冷凍 12 小時後毋須冰袋'),
 'https://www.yohohongkong.com/zh-hk/product/226394': ([5, 5, None, 5], '野餐、派對、外賣', '真空隔熱，保冷保溫兩用，20L'),
 'https://www.yohohongkong.com/zh-hk/product/114329': ([4, 5, 5, 3], '備餐、翻熱飯餸', '盒身可微波、焗爐、洗碗碟機'),
 'https://www.yohohongkong.com/zh-hk/product/116443': ([5, 4, None, 3], '水果、肉類延長保鮮', '抽真空保鮮；微波適用未能確認'),
 'https://onlineshop.muji.com.hk/products/4550583134433': ([3, 4, None, 5], '雪櫃收納、乾貨分裝', '$38；可否微波頁面未有註明'),
 'https://www.wellcome.com.hk/zh-hant/p/%E4%BD%B3%E8%83%BD%E4%BF%9D%E9%AE%AE%E7%B4%99%20200FT/i/101343913.html': ([3, 3, None, 5], '碗碟封口、短時間保存', '一般保鮮紙；翻熱請用微波爐專用款'),
 'https://www.wellcome.com.hk/zh-hant/p/%E4%BD%B3%E8%83%BD%E4%BF%9D%E9%AE%AE%E9%AD%94%E8%A1%93%E8%B2%BC%2030%E5%8E%98%E7%B1%B3%2070%E5%91%8E/i/115847548.html': ([4, 5, None, 3], '形狀不規則的容器、碗碟封口', '可直接黏貼容器及碗碟'),
 'https://www.wellcome.com.hk/zh-hant/p/%E4%BD%B3%E8%83%BD%E5%BE%AE%E6%B3%A2%E7%88%90%E4%BF%9D%E9%AE%AE%E7%B4%99%20100FT/i/101331506.html': ([3, 3, 5, 4], '翻熱飯餸時封口', '微波爐適用'),
 'https://www.wellcome.com.hk/zh-hant/p/%E4%BD%B3%E8%83%BD%E9%9B%99%E9%87%8D%E9%8E%96%E7%B7%8A%E5%AF%86%E5%AF%A6%E8%A2%8B%E4%B8%AD%2050PC/i/101335749.html': ([4, 5, None, 4], '急凍、醃肉', '雙重拉鏈'),
 'https://www.wellcome.com.hk/zh-hant/p/%E4%BD%B3%E8%83%BD%E9%A3%9F%E7%89%A9%E4%BF%9D%E9%AE%AE%E8%A2%8B%E5%A4%A7%E8%A2%8B%20100EA/i/101347619.html': ([3, 2, None, 5], '蔬果分裝', '一般食物保鮮袋，沒有拉鏈'),
 'https://www.yohohongkong.com/zh-hk/product/335649': ([4, 4, None, 5], '分裝、急凍', '拉鏈密實袋，19×20cm'),
}
BLOG_OF = {'C1': 'B1', 'C2': 'B1', 'C3': 'B1', 'C7': 'B1', 'C4': 'B2', 'C5': 'B2', 'C6': 'B2'}


def stars(v):
    if v is None:
        return '<span class="na">官方未列／不適用</span>'
    return '<span class="stars">' + '★' * v + '<i>' + '★' * (5 - v) + '</i></span>'


def product_block(p, b):
    cat, brand, name, size, spec, price, shop, url, note = p
    sku, img = PROD_EXTRA[url]
    sc, scene, basis = RATE[url]
    rate = '<br>'.join(f'{E(c)}：{stars(v)}' for c, v in zip(CRIT[b], sc))
    nt = f'<br>備註：{E(note)}' if note else ''
    return f'''<div class="pt"><img src="{E(img)}" alt="{E(name)}" loading="lazy" referrerpolicy="no-referrer">
<p class="iu">圖片：<a href="{E(img)}" target="_blank" rel="noopener">{E(img)}</a></p>
<p>品牌：{E(brand)}<br>產品名稱：{E(name)}<br>型號：{E(sku)}<br>容量：{E(size)}<br>重點規格：{E(spec)}<br>價錢（HKD）：{E(price)}（{E(shop)}，{E(PRICE_DATE)}記錄）<br>購買連結：<a href="{E(url)}" target="_blank" rel="nofollow noopener">{E(url)}</a></p>
<p>{rate}<br><span class="basis">評分根據：{E(basis)}</span></p>
<p>適合場景／族群：{E(scene)}{nt}</p></div>'''


def kw_chips(b, c):
    if c == 'FAQ':
        rs = [r for r in R if r['pg'] == b and r['role'] == 'FAQ']
    else:
        rs = [r for r in R if r['pg'] == b and r['cat'] == c and r['role'] in TGT and r['role'] != 'FAQ']
    rs.sort(key=lambda r: (ROLE_ORD[r['role']], -(r['vol'] or 0)))
    cls = {'全文主關鍵字': 'm0', '主要': 'm1', '次要': 'm2', '長尾': 'm3', 'FAQ': 'm4'}
    return ''.join(f'<span class="chip {cls[r["role"]]}{" fo" if r.get("focus") else ""}">{E(r["kw"])}<small>{fv(r["vol"])}</small></span>' for r in rs)


def outline_html(b):
    out = []
    for h2, c, items in OUTLINE[b]:
        body = ''.join(f'<li>{E(i)}</li>' for i in items)
        chips = kw_chips(b, c) if c else ''
        extra = ''
        if c is None:
            crit = TYPE_CRIT[b]
            extra = '<div class="types">' + ''.join(
                f'<div class="tc"><h5>{E(n)}</h5><ul class="rate">' + ''.join(f'<li><span>{E(cn)}</span>{stars(v)}</li>' for cn, v in zip(crit, sc))
                + f'</ul><p class="aud"><b>適合場景／族群</b>{E(sc2)}</p></div>' for n, sc, sc2 in TYPES[b]) + '</div>'
        prods = ''
        if c in BLOG_OF:
            ps = [p for p in PRODUCTS if p[0] == c]
            prods = '<div class="plist">' + ''.join(product_block(p, b) for p in ps) + '</div>'
        out.append(f'<div class="sec"><h4>{E(h2)}</h4><ul class="h3">{body}</ul>'
                   + (f'<div class="chips">{chips}</div>' if chips else '') + extra + prods + '</div>')
    return ''.join(out)


def card(cd):
    b = cd['pg']
    rs = [r for r in R if r['pg'] == b]
    tgt = [r for r in rs if r['role'] in TGT]
    top = sorted(tgt or rs, key=lambda r: (ROLE_ORD.get(r['role'], 9), -(r['vol'] or 0)))[:8]
    kws = ''.join(f'<li><mark>{E(r["kw"])}</mark><span>KP {fv(r["vol"])}</span></li>' for r in top)
    seo = ''
    if cd['h1']:
        seo = (f'<div class="seo"><p><small>建議 H1</small>{E(cd["h1"])}</p><p><small>SEO Title</small>{E(cd["title_tag"])}</p>'
               f'<p><small>Meta Description</small>{E(cd["meta"])}</p><p><small>Focus Keyword</small><mark>{E(cd["focus"])}</mark></p></div>')
    u = f'<p class="u">{E(cd["url"])}（建議網址）</p>' if cd['url'] else '<p class="u">—</p>'
    lns = ''.join(f'<span class="ln">{E(x)}</span>' for x in cd['links'])
    return (f'<div class="pc{" x" if b in "XZH" else ""}" data-pg="{b}"><div class="ph"><b>{b}</b><span class="st">{E(cd["st"])}</span></div>'
            f'<h3>{E(cd["title"])}</h3>{u}<p class="ty">{E(cd["ty"])}</p>{seo}'
            f'<div class="num"><div><b>{len(rs)}</b><small>關鍵字</small></div><div><b>{sum((r["vol"] or 0) for r in rs):,}</b><small>KP 月均合計</small></div>'
            f'<div><b>{len(tgt)}</b><small>要佈局</small></div></div><ul class="kw">{kws}</ul><p class="note">{E(cd["note"])}</p>'
            f'<div class="lns">{lns}</div>' + (f'<a class="mock" href="#outline-{b}">📝 查看大綱及產品段落</a>' if b in ('B1', 'B2') else '')
            + f'<button class="more" data-pg="{b}">查看全部關鍵字 ↓</button></div>')


MERMAID = '''flowchart LR
B1["B1 食物保暖用品篇<br/>保溫飯盒推介"] <--> B2["B2 保鮮用品篇<br/>保鮮紙、密實袋、保鮮盒"]
B1 -. CTA .-> S["派對用品：餐具及暖貼加配"]
B1 -. CTA .-> P["派對到會套餐"]
B2 -. CTA .-> C["Chill 一下野餐盒"]
H["保溫壺／保溫杯／保溫瓶<br/>（只作承接）"] -.-> B1
classDef b fill:#E3F4E8,stroke:#6FAE82
classDef k fill:#1A1A1A,color:#F7CE46,stroke:#1A1A1A
classDef h fill:#F3F3F3,stroke:#BBB,color:#777
class B1,B2 b
class S,P,C k
class H h'''

DATA = {'rows': [dict(kw=r['kw'], gkp=r['gkp'], pg=r['pg'], cat=r['catname'], role=r['role'], kp=r['vol'],
                      m3=r['m3'], yoy=r['yoy'], h2=r['h2'], src=r['src'], brand=r['brand']) for r in R],
        'pages': PAGES}

tot = len(R)
CSS = open(os.path.join(HERE, 'kw_page.css'), encoding='utf-8').read()
page = f'''<!DOCTYPE html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex">
<title>保暖及保鮮用品 KW 架構｜Kitchen AO</title>
<script src="https://cdn.jsdelivr.net/npm/mermaid@11.4.1/dist/mermaid.min.js"></script>
<style>{CSS}</style></head><body>
<header><h1>🍱 食物保暖及保鮮用品 KW 分配架構（2 篇 Blog）</h1><p>資料：Google Keyword Planner（保溫.xlsx＋2026-10-28 新增查詢）、Google 自動建議｜共 {tot} 個字｜產品價錢記錄：{PRICE_DATE}</p></header>
<div class="wrap">
<div class="rule"><b>分配原則：</b>一個關鍵字只分配到一篇，避免自家頁面互搶排名。帶飯保溫（保溫飯盒、燜燒壺、加熱飯盒、保溫袋）→ Blog 1；保鮮（保鮮紙、密實袋、保鮮盒、真空）→ Blog 2；飲品保溫壺、保溫杯、保溫瓶 → 只在 Blog 1 一個 H3 承接；冰袋、冰磚 → 暫不使用；烘焙紙、暖包 → 不建議。每篇只刻意佈局「主要／次要／長尾／FAQ」，其餘列為「自然涵蓋」，不用逐個寫入。</div>
<h2>內鏈架構</h2><div class="card"><pre class="mermaid">{E(MERMAID)}</pre></div>
<h2>頁面分配總覽</h2><div class="grid">{''.join(card(c) for c in CARDS)}</div>
<h2 id="outline-B1">Blog 1 大綱及產品段落</h2>
<p class="leg"><span class="chip m0">全文主關鍵字</span><span class="chip m1">H2 主要</span><span class="chip m2">次要</span><span class="chip m3">長尾</span><span class="chip m4">FAQ</span><span class="chip m3 fo">重點長尾（已確認）</span>｜產品評分為 Kitchen AO 編輯評分，按官方規格及產品類型評估，並非實測。</p>
<div class="card">{outline_html('B1')}</div>
<h2 id="outline-B2">Blog 2 大綱及產品段落</h2>
<div class="card">{outline_html('B2')}</div>
<h2 id="all">全部關鍵字</h2>
<div class="card"><div class="tools"><select id="pg"><option value="">全部頁面</option></select><select id="ro"><option value="">全部角色</option></select><input id="q" placeholder="搜尋關鍵字…"><span id="cnt"></span><button id="dl" class="dl">⬇ 下載 CSV（按目前篩選及排序）</button></div>
<div style="max-height:70vh;overflow:auto"><table id="tb"></table></div></div>
</div>
<script>
const D={json.dumps(DATA, ensure_ascii=False)};
mermaid.initialize({{startOnLoad:true,securityLevel:'loose',flowchart:{{htmlLabels:true}}}});
const sel=document.getElementById('pg'),ro=document.getElementById('ro');
Object.entries(D.pages).forEach(([k,v])=>{{const o=document.createElement('option');o.value=k;o.textContent=k+' '+v;sel.appendChild(o)}});
[...new Set(D.rows.map(r=>r.role))].forEach(v=>{{const o=document.createElement('option');o.value=v;o.textContent=v;ro.appendChild(o)}});
const f=n=>n==null||n===''?'—':Number(n).toLocaleString();
const C=[['kw','關鍵字',1],['pg','頁面'],['cat','產品類別'],['role','角色'],['kp','KP 月均'],['m3','3 個月變化'],['yoy','按年變化'],['h2','放置位置'],['src','資料來源']];
const RO={{'全文主關鍵字':0,'主要':1,'次要':2,'長尾':3,'FAQ':4}};
let sk=null,sd=1,cur=[];
function th(k,t){{const on=sk===k;return `<th class="s${{on?' on':''}}" data-k="${{k}}">${{t}} <i>${{on?(sd>0?'▲':'▼'):'⇅'}}</i></th>`}}
function draw(){{const pg=sel.value,r0=ro.value,q=document.getElementById('q').value.trim().toLowerCase();
let rs=D.rows.filter(r=>(!pg||r.pg===pg)&&(!r0||r.role===r0)&&(!q||(r.kw+' '+r.gkp).toLowerCase().includes(q)));
if(sk)rs.sort((a,b)=>{{let x=a[sk],y=b[sk];if(sk==='kp'){{if(x==null)return 1;if(y==null)return -1;return (x-y)*sd}}return String(x||'').localeCompare(String(y||''),'zh-HK')*sd}});
else rs.sort((a,b)=>a.pg.localeCompare(b.pg)||((RO[a.role]??9)-(RO[b.role]??9))||((b.kp||0)-(a.kp||0)));
cur=rs;
document.getElementById('tb').innerHTML='<tr>'+C.map(([k,t])=>th(k,t)).join('')+'</tr>'+rs.map(r=>'<tr>'+C.map(([k,t,mk])=>k==='kp'?`<td class=n>${{f(r.kp)}}</td>`:`<td>${{mk&&(RO[r.role]??9)<5?'<mark>'+r[k]+'</mark>':(r[k]??'')}}</td>`).join('')+'</tr>').join('');
document.querySelectorAll('#tb th.s').forEach(t=>t.onclick=()=>{{const k=t.dataset.k;if(sk===k)sd=-sd;else{{sk=k;sd=k==='kp'?-1:1}}draw()}});
document.getElementById('cnt').textContent=rs.length+' 項';}}
function csv(){{const esc=v=>{{v=v==null?'':String(v);return /[",\\n]/.test(v)?'"'+v.replace(/"/g,'""')+'"':v}};
const head=C.map(c=>c[1]);head.splice(2,0,'頁面名稱');
const lines=[head.map(esc).join(',')].concat(cur.map(r=>{{const v=C.map(([k])=>r[k]);v.splice(2,0,D.pages[r.pg]||'');return v.map(esc).join(',')}}));
const b=new Blob(['\\ufeff'+lines.join('\\n')],{{type:'text/csv;charset=utf-8'}});const a=document.createElement('a');
a.href=URL.createObjectURL(b);a.download=`保暖保鮮KW${{sel.value?'_'+sel.value:''}}.csv`;document.body.appendChild(a);a.click();a.remove();}}
sel.onchange=draw;ro.onchange=draw;document.getElementById('q').oninput=draw;document.getElementById('dl').onclick=csv;
document.querySelectorAll('.more').forEach(b=>b.onclick=()=>{{sel.value=b.dataset.pg;draw();document.getElementById('all').scrollIntoView({{behavior:'smooth'}})}});
draw();
</script></body></html>'''
open(OUT, 'w', encoding='utf-8').write(page)
print('ok', OUT, len(page))
