# Kitchen AO — Blog 1 野餐地點推介（Demo，書面語版，2026-10-16 更新）
# python3 build.py  → preview.html（有 KW/PAA 黃色 highlight）＋ blog-picnic-WORDPRESS.html（無 highlight）
# 地點資料在 parks.py
import json, re, html as H, importlib.util, os
from urllib.parse import quote
HERE = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('parks', os.path.join(HERE, 'parks.py')); _m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
CATS, REGIONS, P = _m.CATS, _m.REGIONS, _m.P

UTM = 'ao_ref=picnic_blog1'
CHILL = 'https://aoaodelivery.com/product-category/party/chill-box/?' + UTM
BIG = 'https://aoaodelivery.com/product/chill%e4%b8%80picnic-big-for-4-6-persons/?' + UTM
PLATTER = 'https://aoaodelivery.com/product/5-people-self-selected-platter/?' + UTM
C2A = 'https://aoaodelivery.com/product/small-but-special-package-for-two/?' + UTM
C2B = 'https://aoaodelivery.com/product/luxury-ceremony-up-package-for-two/?' + UTM
IMG_C2A = 'https://aoaodelivery.com/wp-content/uploads/2023/10/202308-2pax-thumbnail_%E5%B7%A5%E4%BD%9C%E5%8D%80%E5%9F%9F-1-600x600.jpg'
IMG_C2B = 'https://aoaodelivery.com/wp-content/uploads/2023/10/202308-2pax-thumbnail-02-600x600.jpg'
WA = 'https://api.whatsapp.com/send?phone=85269011987&text=' + quote('你好，我想查詢 Chill一下野餐盒')
IMG_CHILL = 'https://aoaodelivery.com/wp-content/uploads/2025/04/WhatsApp-Image-2025-04-12-at-4.08.18-PM-600x400.jpeg'
IMG_PLATTER = 'https://aoaodelivery.com/wp-content/uploads/2023/10/KitchenAO_platter_thumbnail_%E5%B7%A5%E4%BD%9C%E5%8D%80%E5%9F%9F-1-600x600-1.png'
VAC = 'https://resource.data.one.gov.hk/td/carpark/'
N = len(P)

def tags(p):
    # 2026-10-17：第一個 tag 為「適合野餐」；只顯示 Y 的類別；寵物只在 Y／指定範圍時顯示
    t = ['<span class="pk-tag t-ok">🧺 適合野餐</span>']
    for c in p['cats']: t.append(f'<span class="pk-tag t-cat">{CATS[c][0]} {CATS[c][1]}</span>')
    if p['pet'] == 'Y': t.append('<span class="pk-tag t-pet">🐶 寵物友善</span>')
    elif p['pet'] == 'P': t.append('<span class="pk-tag t-pet2">🐾 寵物指定範圍</span>')
    return ''.join(t)

def petmap_btn(p):
    if not p.get('petmap'): return ''
    return f'<button type="button" class="pk-mapbtn" data-img="{p["petmap"]}" data-t="{H.escape(p["name"])}｜寵物共享公園範圍">🗺️ 查看寵物共享範圍地圖</button>'

def card(p):
    if p['car']:
        seen = set(); lis = ''
        for n, f in p['car']:
            btn = ''
            if f and f not in seen:
                seen.add(f); btn = f'<button type="button" class="pk-vac" data-src="{VAC}{f}">查看實時車位</button><span class="pk-vres"></span>'
            lis += f'<li><span class="nm">🅿️ {H.escape(n)}</span>{btn}</li>'
        carhtml = f'<div class="pk-car"><p class="lbl">鄰近停車場</p><ul>{lis}</ul></div>'
    else:
        carhtml = f'<div class="pk-car pk-car--none"><p class="lbl">鄰近停車場</p><p>⚠️ {p.get("carnote","暫無停車場資料")}</p></div>'
    data = f'data-r="{p["r"]}" data-car="{1 if p["car"] else 0}" data-pet="{p["pet"]}" data-cats="{" ".join(p["cats"])}"'
    return f'''<article class="pk-card" id="pk-{p['id']}" {data}>
  <div class="pk-ph"><span>📷 相片待補</span></div>
  <div class="pk-body">
    <h3 class="pk-h3">{p['name']} <small>{p['en']}</small></h3>
    <div class="pk-tags">{tags(p)}</div>
    <p class="pk-kw">目標關鍵字：<mark class="kw">{p['kw']}</mark></p>
    <p class="pk-intro">{p['intro']}</p>
    <p class="pk-tr"><b>🚇 交通：</b>{p['tr']}</p>
    <p class="pk-pet"><b>🐶 寵物：</b>{p['petnote']}</p>
    {petmap_btn(p)}
    {carhtml}
  </div>
</article>'''

regions = ''
for i, (rid, rname, rkw) in enumerate(REGIONS):
    ps = [p for p in P if p['r'] == rid]
    cards = ''.join(card(p) for p in ps)
    regions += f'''<section class="pk-region" data-region="{rid}">
  <h2 class="ao-h2" id="r-{rid}">{"一二三"[i]}、{rname}野餐（{len(ps)} 個地點）</h2>
  <p class="ao-aio">【AIO 直接解答｜待撰寫 50–80 字】<mark class="kw">{rkw}</mark>可以去哪裡？以下 {len(ps)} 個地點已按可泊車、寵物友善及地點類別標示。</p>
  <div class="pk-grid">{cards}</div>
</section>'''

chips_r = ''.join(f'<button type="button" class="pk-chip" data-f="r" data-v="{rid}">{rn}</button>' for rid, rn, _ in REGIONS)
chips_c = ''.join(f'<button type="button" class="pk-chip" data-f="cat" data-v="{k}">{v[0]} {v[1]}</button>' for k, v in CATS.items())
legend = ''.join(f'<span>{v[0]} {v[1]}</span>' for v in CATS.values())

CSS = open(os.path.join(HERE, 'style.css')).read()
JS = open(os.path.join(HERE, 'tool.js')).read()
FAQ = [
 ('野餐幾點到達最容易找到位置？', '建議上午 11 時 30 分前或下午 3 時 30 分後到達：早到可佔樹蔭位置，下午到達則可避開正午烈日，還可欣賞日落。'),
 ('香港的公園可以野餐嗎？', '大部分康文署公園的草地均可野餐，但部分草坪會輪流開放或進行保養，出發前建議先查閱康文署網頁。'),
 ('可以帶狗去野餐嗎？', '可以，但須選擇寵物共享公園或准許寵物進入的草地，並以狗帶牽引。本文每個地點均有「🐶 寵物友善」標示，部分地點更附有康文署寵物共享範圍地圖。'),
 ('哪個野餐地點有停車場？', '可在上方搜尋器選擇「🚗 可泊車」，每個地點底部均列出鄰近停車場，部分更可即時查看實時車位。'),
 ('下雨天可以去哪裡野餐？', '可考慮設有上蓋的空中花園，例如啟德郵輪碼頭公園，或樹蔭較多的中山紀念公園及九龍公園。'),
 ('野餐食物哪裡買？', '如不想自行準備，可預訂 Kitchen AO「Chill一下野餐盒」，乾爽一口食，送到公園附近可停車位置交收。'),
]
faq_html = ''.join(f'<details class="ao-faq"><summary><mark class="paa">{q}</mark></summary><div class="a">{a}</div></details>' for q, a in FAQ)
faq_ld = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}, ensure_ascii=False)

BODY = f'''<div class="ao-article ao-picnic">
<style>
{CSS}
</style>

<div class="pk-kv"><div><p class="pk-kv-pill">2026 香港野餐好去處</p><p class="pk-kv-t">香港野餐勝地大全</p><p class="pk-kv-s">{N} 個大草地／海景／隱世公園推介 × 懶人野餐全攻略</p></div><span class="pk-kv-note">KV 待製作（1600 × 900）</span></div>
<p class="pk-h1note">H1：【香港野餐勝地大全】{N} 個大草地／海景／隱世公園推介 x 懶人野餐全攻略</p>

<div class="ao-introcard">
<p class="ao-q">🧺 想找<mark class="kw">香港野餐好去處</mark>？</p>
<p class="ao-intro">香港地方雖小，但也有不少<mark class="kw">野餐好去處</mark>：無敵海景、大片真草地、<mark class="kw">隱世野餐地點</mark>及特色園林應有盡有，更可與狗狗一同野餐。Kitchen AO 整合了全港 {N} 個<mark class="kw">香港野餐地點</mark>，按港島、九龍及新界分類，並可按「可泊車」「寵物友善」及地點類別篩選；每個地點均列出鄰近停車場，方便<mark class="kw">駕車野餐</mark>。</p>
</div>

<div class="ao-tagsec"><span class="lbl">此文章相關 Tag</span><div class="ao-tags"><span>野餐好去處</span><span>香港野餐</span><span>狗狗野餐</span><span>野餐泊車</span><span>野餐盒</span></div></div>

<nav class="ao-toc"><div class="t">目錄</div><ul>
<li><a href="#pk-tool">全港野餐地點搜尋器</a></li>
{''.join(f'<li><a href="#r-{rid}">{"一二三"[i]}、{rn}野餐</a></li>' for i, (rid, rn, _) in enumerate(REGIONS))}
<li><a href="#dog">帶狗狗野餐須知</a></li>
<li><a href="#food">野餐食物及物資清單</a></li>
<li><a href="#faq">野餐常見問題</a></li>
<li><a href="#chill">Kitchen AO 野餐盒推介</a></li>
</ul></nav>

<h2 class="ao-h2" id="pk-tool">🔍 全港野餐地點搜尋器</h2>
<p class="ao-aio">【AIO 直接解答｜待撰寫 50–80 字】先選擇地區，再以三個條件篩選：<mark class="kw">野餐泊車</mark>、<mark class="kw">狗狗野餐好去處</mark>，以及大草地、秘境、海景及特色園林等地點類別。</p>
<div class="pk-tool" id="pkTool">
  <div class="pk-row"><span class="pk-lab">① 地區</span><button type="button" class="pk-chip on" data-f="r" data-v="all">全部</button>{chips_r}</div>
  <div class="pk-row"><span class="pk-lab">② 條件</span><button type="button" class="pk-chip" data-f="car" data-v="1">🚗 可泊車</button><button type="button" class="pk-chip" data-f="pet" data-v="Y">🐶 寵物友善</button></div>
  <div class="pk-row"><span class="pk-lab">③ 類別</span>{chips_c}</div>
  <div class="pk-foot"><span id="pkCount">顯示全部 {N} 個地點</span><button type="button" class="pk-reset" id="pkReset">重設</button></div>
  <div class="pk-legend">{legend}<span>🚗 可泊車</span><span>🐶 寵物友善</span><span>🐾 寵物指定範圍</span></div>
</div>
<p class="pk-empty" id="pkEmpty" hidden>沒有符合條件的地點，請嘗試減少篩選條件。</p>

{regions}

<h2 class="ao-h2" id="dog">🐶 帶狗狗野餐須知</h2>
<p class="ao-aio">【AIO 直接解答｜待撰寫】<mark class="kw">狗狗野餐</mark>前，記得選擇准許寵物進入的草地，並遵守以下守則：</p>
<div class="ao-why"><ul>
<li><b>全程使用狗帶：</b>根據漁農自然護理署及康文署守則，絕大部分公眾地方及「寵物共享公園」內，所有狗隻必須時刻以狗帶（長度以不超逾 2 米為佳）牽引。</li>
<li><b>不讓狗狗離開視線：</b>隨時留意狗狗動向，並觀察牠與其他狗狗的互動。</li>
<li><b>自備糧水：</b>帶備足夠食水及狗糧，炎熱天氣須留意中暑。</li>
<li><b>處理排泄物：</b>帶備狗袋，保持草地清潔。</li>
</ul></div>

<h2 class="ao-h2" id="food">🥪 戶外<mark class="kw">野餐食物</mark>應帶甚麼？物資清單與保存須知</h2>
<p class="ao-aio">【AIO 直接解答｜待撰寫】<mark class="kw">野餐小食</mark>宜選一口份量、乾爽不漏汁；海鮮及沙律須以保冷袋存放，並於 2 小時內食用。</p>
<div class="pk-check"><p><b>🧺 野餐用品清單</b></p><ul><li><mark class="kw">野餐墊</mark>（防水底）</li><li>保冷袋及冰種</li><li>濕紙巾、垃圾袋</li><li>防曬及驅蚊用品</li><li>寵物糧水（如帶同狗狗）</li></ul></div>

<h2 class="ao-h2" id="faq">❓ 野餐常見問題 FAQ</h2>
{faq_html}

<!-- ===== 產品（最後才介紹）===== -->
<h2 class="ao-h2" id="chill">🍱 Kitchen AO <mark class="kw">野餐盒</mark>，惹味小食推介</h2>
<p class="ao-aio">不想花 4 小時準備食物再搬到公園？Kitchen AO 野餐盒、小食拼盤及二人套餐主打乾爽一口食、免餐具，送到公園附近可停車位置交收，<mark class="kw">野餐食物哪裡買</mark>一次解決。</p>
<div class="pk-prod">
  <a class="pk-pcard" href="{BIG}"><img src="{IMG_CHILL}" alt="Chill一下野餐盒（大）4–6 人" loading="lazy"><div><p class="pn">Chill一下野餐盒（大）</p><p class="pp">4–6 人份　<b>$628</b></p><p class="pd">9 款小食：迷你芝士手打牛肉漢堡、千島汁蜜桃大蝦沙律杯、九層塔香酥雞等</p></div></a>
  <a class="pk-pcard" href="{PLATTER}"><img src="{IMG_PLATTER}" alt="5 人自選拼盤" loading="lazy"><div><p class="pn">5 人自選拼盤</p><p class="pp">5 人份　<b>$498</b></p><p class="pd">自選小食組合，適合多人野餐</p></div></a>
  <a class="pk-pcard" href="{C2A}"><img src="{IMG_C2A}" alt="二人小確幸套餐" loading="lazy"><div><p class="pn">二人小確幸套餐</p><p class="pp">2 人份　<b>$438</b></p><p class="pd">二人享樂拼盤、清新沙律、意大利麵及惹味主食，適合二人野餐</p></div></a>
  <a class="pk-pcard" href="{C2B}"><img src="{IMG_C2B}" alt="二人豪華儀式感UP!套餐" loading="lazy"><div><p class="pn">二人豪華儀式感UP!套餐</p><p class="pp">2 人份　<b>$588</b></p><p class="pd">升級版二人套餐，拼盤、沙律、意大利麵及主食選擇更豐富</p></div></a>
</div>
<div class="ao-cta ao-cta--2"><a class="pk-btn" href="{CHILL}">🧺 瀏覽全部野餐盒</a><a class="pk-btn pk-btn--wa" href="{WA}" target="_blank" rel="noopener">WhatsApp 查詢</a></div>
<p class="pk-note">※ 交收安排：送到公園附近可停車位置於車邊交收；消費滿 $1,450 免運費。</p>

<div class="ao-related"><p class="ao-related-t">📖 延伸閱讀</p>
<a href="#">【駕車野餐好去處】香港野餐泊車地圖（Blog 2，待撰寫）→</a>
<a href="https://aoaodelivery.com/blog/kids-birthday-party-catering/">【香港家長必讀】小朋友生日會到會挑選指南 →</a>
</div>

<div class="pk-modal" id="pkModal" hidden><div class="pk-mbox"><button type="button" class="pk-mx" aria-label="關閉">✕</button><p class="pk-mt"></p><img alt="寵物共享公園範圍地圖"><p class="pk-msrc">地圖來源︰康文署</p></div></div>
</div>
<script type="application/ld+json">{faq_ld}</script>
<script>{JS}</script>
'''

prev = '''<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>【2026香港野餐好去處】港九新界海景、大草地及隱世公園野餐地點推介</title></head><body style="margin:0;padding:24px 14px;background:#fff">
<div class="pk-demo-bar">DEMO｜<mark class="kw">黃色</mark>＝目標關鍵字／PAA　<label><input type="checkbox" id="hlToggle" checked> 顯示 highlight</label></div>
''' + BODY + '''<script>document.getElementById('hlToggle').onchange=function(){document.body.classList.toggle('no-hl',!this.checked)};</script></body></html>'''
if __name__ == '__main__':
    open(os.path.join(HERE, 'preview.html'), 'w').write(prev)
    open(os.path.join(HERE, 'index.html'), 'w').write(prev)
    wp = re.sub(r'<mark class="(?:kw|paa)">(.*?)</mark>', r'\1', BODY)
    wp = re.sub(r'<p class="pk-kw">.*?</p>', '', wp)
    wp = re.sub(r'<p class="pk-h1note">.*?</p>', '', wp)
    open(os.path.join(HERE, 'blog-picnic-WORDPRESS.html'), 'w').write(wp)
    print('parks', N, 'car', sum(1 for p in P if p['car']), 'pet', sum(1 for p in P if p['pet'] == 'Y'), 'maps', sum(1 for p in P if p.get('petmap')))
