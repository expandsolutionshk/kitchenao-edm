# Kitchen AO — Blog 1 野餐地點推介（Demo，書面語版，2026-10-16 更新）
# python3 build.py  → preview.html（有 KW/PAA 黃色 highlight）＋ blog-picnic-WORDPRESS.html（無 highlight）
# 地點資料在 parks.py
import json, re, html as H, importlib.util, os
from urllib.parse import quote
HERE = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('parks', os.path.join(HERE, 'parks.py')); _m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
CATS, REGIONS, P = _m.CATS, _m.REGIONS, _m.P
_c = importlib.util.spec_from_file_location('combo', os.path.join(HERE, 'combo.py')); C = importlib.util.module_from_spec(_c); _c.loader.exec_module(C)  # 搜尋器、地圖、比較表、B 款地點卡
_k = importlib.util.spec_from_file_location('kv', os.path.join(HERE, 'kv.py')); KVM = importlib.util.module_from_spec(_k); _k.loader.exec_module(KVM)  # KV 方案

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

AIO = {
 'nt': '<mark class="kw">新界野餐地點</mark>以草地遼闊見稱：大埔海濱公園及清水灣大坑墩適合放風箏，塔門及南生圍則有海景與秘境風光；當中多個地點寵物友善，並設有鄰近停車場，最適合一家大小駕車前往。',
 'kln': '<mark class="kw">九龍野餐好去處</mark>首選海濱草地：西九文化區及啟德郵輪碼頭公園可飽覽維港景色，觀塘及茶果嶺海濱設有寵物指定範圍；佐敦谷公園及樂富配水庫休憩花園則有大片草坪，交通方便。',
 'hk': '<mark class="kw">港島野餐</mark>地點集中在海旁：添馬公園及中山紀念公園正對維港，數碼港海濱公園寵物友善兼易泊車；想避開人潮，可前往摩星嶺配水庫臨時花園，享受秘境草地與海景。',
}
regions = ''
for i, (rid, rname, rkw) in enumerate(REGIONS):
    ps = [p for p in P if p['r'] == rid]
    cards = ''.join(C.card(p) for p in ps)
    regions += f'''<section class="pk-region" data-region="{rid}">
  <div class="rhd"><h2 class="ao-h2" id="r-{rid}">{rkw}</h2><span class="rcount" data-r="{rid}" data-t="{len(ps)}">{len(ps)} 個地點</span></div>
  <p class="ao-aio">{AIO[rid]}</p>
  <div class="pk-list">{cards}</div>
</section>'''

chips_r = ''.join(f'<button type="button" class="pk-chip" data-f="r" data-v="{rid}">{rn}</button>' for rid, rn, _ in REGIONS)
chips_c = ''.join(f'<button type="button" class="pk-chip" data-f="cat" data-v="{k}">{v[0]} {v[1]}</button>' for k, v in CATS.items())
legend = ''.join(f'<span>{v[0]} {v[1]}</span>' for v in CATS.values())

CSS = open(os.path.join(HERE, 'style.css')).read()
CSS += '\n/* ===== 搜尋器＋地圖＋比較表＋B 款地點卡（由 combo.py 生成）===== */\n.ao-picnic .pk-cmb{container-type:inline-size}\n.ao-picnic .pk-cmb *{box-sizing:border-box}\n' + C.scope_css(C.CSS, '.ao-picnic')
FAQ = [
 ('野餐幾點到達最容易找到位置？', '建議上午 11 時 30 分前或下午 3 時 30 分後到達：早到可佔樹蔭位置，下午到達則可避開正午烈日，還可欣賞日落。'),
 ('香港的公園可以野餐嗎？', '大部分康文署公園的草地均可野餐，但部分草坪會輪流開放或進行保養，出發前建議先查閱康文署網頁。'),
 ('可以帶狗去野餐嗎？', '可以，但須選擇寵物共享公園或准許寵物進入的草地，並以狗帶牽引。本文每個地點均有「🐶 寵物友善」標示，部分地點更附有康文署寵物共享範圍地圖。'),
 ('哪個野餐地點有停車場？', '可在上方搜尋器選擇「🚗 可泊車」，每個地點底部均列出鄰近停車場，部分更可即時查看實時車位。'),
 ('下雨天可以去哪裡野餐？', '雨天不宜在草地野餐，可考慮設有上蓋或樹蔭較多的地點，例如中山紀念公園；出發前亦應留意天文台天氣預報及草地開放安排。'),
 ('野餐食物哪裡買？', '如不想自行準備，可預訂 Kitchen AO「Chill一下野餐盒」，乾爽一口食，送到公園附近可停車位置交收。'),
 ('公園野餐可以燒烤嗎？', '大部分康文署公園均不准燒烤或使用明火，只可在指定燒烤場地進行；出發前請先查閱場地守則。'),
 ('野餐盒可以送到公園嗎？', '可以。Kitchen AO 會將野餐盒送到公園附近可停車位置，於車邊交收。滿 $1,450 全港免運費；滿 $700 九龍指定區域免運費，港島及新界區運費半價。'),
 ('野餐食物如何保鮮？', '海鮮、沙律及甜品等須以保冷袋連冰種存放，並於 2 小時內食用；炸物及一口小食則宜選乾爽、不漏汁的款式，方便攜帶。'),
 ('公眾假期去野餐要注意甚麼？', '熱門草地於假日人流較多，建議提早到達佔位，並盡量乘搭公共交通工具；如需駕車，可先在本文查看鄰近停車場及實時車位。'),
]
faq_html = ''.join(f'<details class="ao-faq"><summary><mark class="paa">{q}</mark></summary><div class="a">{a}</div></details>' for q, a in FAQ)
faq_ld = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}, ensure_ascii=False)

SNACKS = [
 ('迷你芝士手打牛肉漢堡', '皇牌一口漢堡，大人小朋友都啱。', 'a0700-handmade-mini-cheeseburger', '2019/06/Posts-07-scaled-600x600.jpg'),
 ('九層塔香酥雞', '乾身炸物，放涼後依然香脆。', 'a2800-crispy-basil-chicken-dice', '2023/12/KitchenAO_DEC2023-ALA-CARTE-03-600x600.jpg'),
 ('香烤沙嗲串燒（豬雞）', '附竹籤，毋須餐具即可享用。', 'a0200-grilled-satay-skewer-pork-and-chicken', '2019/06/Posts-10-scaled-600x600.jpg'),
 ('焗雙色芝士吞拿魚脆法包', '脆法包作底，方便單手取食。', 'a0100-baked-double-cheese-tuna-crostini', '2019/06/Posts-06-scaled-600x600.jpg'),
 ('芝士海鮮牛角酥', '酥皮小食，賣相精緻適合打卡。', 'a1800-cheesy-seafood-and-pork-floss-croissant', '2023/10/KitchenAO_JUN2023-ALA-CARTE-04-600x600.png'),
 ('蜜蜜燒雞翼配脆薯角', '人氣派對小食，一口一件。', 'a0500-honey-glazed-chicken-wings-w-potato-wedges', '2019/06/Posts-16-scaled-600x600.jpg'),
]
snack_html = ''.join(f'<a class="pk-sn" href="https://aoaodelivery.com/product/{slug}/?{UTM}" target="_blank" rel="noopener"><img src="https://aoaodelivery.com/wp-content/uploads/{img}" alt="{n}｜Kitchen AO 野餐小食" loading="lazy"><span class="sn-b"><b>{n}</b><i>查看單點小食</i></span></a>' for n, d, slug, img in SNACKS)
FBJS = "<script>(function(){var f=document.getElementById('aoFb');if(!f)return;var m=f.querySelector('.ao-fb-msg');\nvar U=function(){return location.href.split('#')[0]},T='香港野餐好去處｜全港野餐地點搜尋器（可泊車、寵物友善）';f.querySelector('.ao-fb-wa').onclick=function(){window.open('https://wa.me/?text='+encodeURIComponent(T+' '+U()),'_blank','noopener');(window.dataLayer=window.dataLayer||[]).push({event:'share_article',method:'whatsapp'})};f.querySelector('.ao-fb-fbk').onclick=function(){window.open('https://www.facebook.com/sharer/sharer.php?u='+encodeURIComponent(U()),'_blank','noopener');(window.dataLayer=window.dataLayer||[]).push({event:'share_article',method:'facebook'})};f.querySelector('.ao-fb-copy').onclick=function(){var u=location.href.split('#')[0];(navigator.clipboard?navigator.clipboard.writeText(u):Promise.reject()).then(function(){m.textContent='已複製連結'}).catch(function(){m.textContent=u})};\nf.querySelectorAll('.ao-fb-b').forEach(function(b){b.onclick=function(){f.querySelectorAll('.ao-fb-b').forEach(function(x){x.disabled=true;x.classList.toggle('on',x===b)});m.textContent='多謝你的意見！';(window.dataLayer=window.dataLayer||[]).push({event:'article_feedback',feedback:b.dataset.v,article:'picnic-blog1'})}})})();</script>"
BODY = f'''<div class="ao-article ao-picnic wp-exclude-emoji">
<style>
{CSS}
</style>

<div class="pk-kvg"><iframe class="kd" srcdoc="{H.escape(KVM.KV_G_HTML, quote=True)}" title="香港野餐勝地大全 KV" scrolling="no"></iframe><iframe class="km" srcdoc="{H.escape(KVM.KV_GM_HTML, quote=True)}" title="香港野餐勝地大全 KV（手機版）" scrolling="no"></iframe></div>
<p class="pk-h1note">H1：【香港野餐勝地大全】{N} 個大草地／海景／隱世公園推介｜野餐泊車、寵物友善地點一鍵搜尋</p>

<div class="ao-introcard">
<p class="ao-q">🧺 想找<mark class="kw">香港野餐好去處</mark>？</p>
<p class="ao-intro">香港地方雖小，但也有不少<mark class="kw">野餐好去處</mark>：無敵海景、大片真草地、<mark class="kw">隱世野餐地點</mark>及特色園林應有盡有，更可與狗狗一同野餐。Kitchen AO 整合了全港 {N} 個<mark class="kw">香港野餐地點</mark>，按新界、九龍及港島分類，並可按「可泊車」、「寵物友善」及公園特色等類別篩選；每個地點均列出鄰近停車場，想尋找理想位置<mark class="kw">駕車野餐</mark>，一按即可找到。</p>
</div>

<nav class="ao-toc"><div class="t">目錄</div><ul>
<li><a href="#hk-table">野餐地點一覽表</a></li>
<li><a href="#pk-tool">全港野餐地點搜尋器</a></li>
{''.join(f'<li><a href="#r-{rid}">{rkw}</a></li>' for rid, rn, rkw in REGIONS)}
<li><a href="#dog">帶狗狗野餐須知</a></li>
<li><a href="#food">野餐食物及物資清單</a></li>
<li><a href="#chill">Kitchen AO 野餐盒推介</a></li>
<li><a href="#faq">野餐常見問題</a></li>
<li><a href="#tips">編輯總結｜野餐注意事項</a></li>
</ul></nav>

{C.TABLE("h2", "ao-h2")}

<h2 class="ao-h2" id="pk-tool">🔍 全港野餐地點搜尋器</h2>
<p class="ao-aio">只需兩步，即可找到合適的野餐地點：先選擇新界、九龍或港島，再按需要篩選可泊車、寵物友善及地點類別，按「確定搜尋」即可。無論想找<mark class="kw">野餐泊車</mark>地點，還是<mark class="kw">狗狗野餐好去處</mark>，都能一鍵找到。</p>
<div class="pk-cmb">
{C.FILTER}
{C.MAP('h3')}
<p class="empty" id="empty">沒有符合條件的地點，請嘗試減少篩選條件。</p>
{regions}
</div>

<h2 class="ao-h2" id="dog">🐶 帶狗狗野餐須知</h2>
<p class="ao-aio"><mark class="kw">狗狗野餐</mark>應選擇<mark class="kw">狗狗寵物公園</mark>（康文署「寵物共享公園」）或准許寵物進入的草地，例如西九文化區、彭福公園及清水灣大坑墩；出發前宜先查看寵物共享範圍地圖，並遵守以下守則：</p>
<div class="ao-why"><ul>
<li><b>全程使用狗帶：</b>根據漁農自然護理署及康文署守則，絕大部分公眾地方及「寵物共享公園」內，所有狗隻必須時刻以狗帶（長度以不超逾 2 米為佳）牽引。</li>
<li><b>不讓狗狗離開視線：</b>隨時留意狗狗動向，並觀察牠與其他狗狗的互動。</li>
<li><b>自備糧水：</b>帶備足夠食水及狗糧，炎熱天氣須留意中暑。</li>
<li><b>處理排泄物：</b>帶備狗袋，保持草地清潔。</li>
</ul></div>

<h2 class="ao-h2" id="food">🥪 戶外<mark class="kw">野餐食物</mark>應帶甚麼？物資清單與保存須知</h2>
<p class="ao-aio"><mark class="kw">野餐小食</mark>宜選一口份量、乾爽不漏汁的款式，例如迷你漢堡、炸雞及串燒，方便單手取食；海鮮、沙律及甜品須以保冷袋連冰種存放，並於 2 小時內食用。</p>
<div class="pk-check"><p><b>🧺 野餐用品清單</b></p><ul><li><mark class="kw">野餐墊</mark>（防水底）</li><li>保冷袋及冰種</li><li>濕紙巾、垃圾袋</li><li>防曬及驅蚊用品</li><li>寵物糧水（如帶同狗狗）</li></ul></div>

<!-- ===== 產品（最後才介紹）===== -->
<h2 class="ao-h2" id="chill">🧺 Kitchen AO <mark class="kw">野餐盒</mark>｜送到附近可停車位置</h2>
<p class="ao-aio">不想花 4 小時準備食物再搬到公園？Kitchen AO 野餐盒、小食拼盤及二人套餐主打乾爽一口食、免餐具，送到公園附近可停車位置交收，<mark class="kw">野餐食物哪裡買</mark>一次解決。</p>
<p class="psub">選擇人數及套餐，按「揀選心水餐單」後於網站揀選菜式並完成訂購。滿 $1,450 全港免運費；滿 $700 九龍指定區域免運費，港島及新界區運費半價，於地面可停車位置車邊交收。</p>
<div class="pgrid">{C.pcards_for("?"+UTM)}</div>
<h3 class="ao-h3">🍗 野餐單點小食推介</h3>
<p>除了野餐盒，亦可按人數及口味加配單點小食。以下 6 款乾爽、一口份量、毋須餐具，最適合帶到草地享用。</p>
<div class="pk-sngrid">{snack_html}</div>
<p class="pk-snall"><a href="https://aoaodelivery.com/product-category/a-la-carte/snacks/?{UTM}" target="_blank" rel="noopener">查看全部惹味小食 →</a></p>
<div class="ao-cta ao-cta--2"><a class="pk-btn" href="{CHILL}">🧺 瀏覽全部野餐盒</a><a class="pk-btn pk-btn--wa" href="{WA}" target="_blank" rel="noopener">WhatsApp 查詢</a></div>
<div class="pk-ship"><p><b>訂購野餐盒 免運費須知：</b>單一訂單滿 HK$1,450 即享全港免運費（離島及邊境禁區等不派送地區除外）；單一訂單滿 HK$700，九龍指定區域免運費，港島及新界區運費半價。標準派送時段為上午 11:00 至晚上 8:30，時段外派送需另收附加費。食物會送到公園附近可停車位置於車邊交收；惡劣天氣改期、派送失敗等安排，請於下單前參閱<a href="https://aoaodelivery.com/delivery/" target="_blank" rel="noopener">「重要送貨須知」</a>。</p></div>

<h2 class="ao-h2" id="faq">❓ 野餐常見問題 FAQ</h2>
{faq_html}

<h2 class="ao-h2" id="tips">📝 編輯總結｜野餐注意事項：天氣、草地開放、場地守則及垃圾處理</h2>
<p>揀好地點、準備好食物後，出發前不妨再檢視以下幾項<mark class="kw">野餐注意事項</mark>，讓整個野餐玩得開心亦玩得安心。</p>
<h3 class="ao-h3">出發前留意天氣及草地開放安排</h3>
<p>出發前一天應留意香港天文台的天氣預報；康文署部分草坪會輪流開放或進行保養，出發前宜先查閱場地網頁，以免白行一趟。</p>
<h3 class="ao-h3">防曬、防蚊及補充水分</h3>
<p>草地大多缺乏遮蔭，宜帶備防曬用品、帽子及足夠食水；黃昏時分蚊蟲較多，記得預備驅蚊用品。</p>
<h3 class="ao-h3">遵守場地守則</h3>
<p>大部分公園不准燒烤或使用明火，寵物亦只可進入指定範圍；放風箏、踏單車等活動，亦應先了解各場地規定。</p>
<h3 class="ao-h3">垃圾處理：全部帶走</h3>
<p>預備足夠垃圾袋，將廚餘、膠樽及包裝全部帶走，保持草地清潔，讓下一位野餐人士同樣可以享受。</p>
<p>一次成功的野餐，往往取決於出發前的準備。只要按本文搜尋器揀選合適地點，再配合合適的食物及交收安排，便能輕鬆享受一個悠閒的下午。如希望省卻準備功夫，歡迎選擇 Kitchen AO 的<a href="{CHILL}">Chill一下野餐盒</a>。</p>

<div class="ao-fb" id="aoFb"><span class="ao-fb-sh"><button type="button" class="ao-fb-wa">💬 WhatsApp 分享</button><button type="button" class="ao-fb-fbk">📘 Facebook 分享</button><button type="button" class="ao-fb-copy">🔗 複製連結</button></span><span class="ao-fb-q">呢篇文章有冇幫到你？</span><button type="button" class="ao-fb-b" data-v="yes">👍 有用</button><button type="button" class="ao-fb-b" data-v="no">👎 一般</button><span class="ao-fb-msg" aria-live="polite"></span></div>

<div class="ao-tagsec"><span class="lbl">此文章相關 Tag</span><div class="ao-tags"><span>野餐好去處</span><span>香港野餐</span><span>狗狗野餐</span><span>野餐泊車</span><span>野餐盒</span></div></div>

<div class="ao-related"><p class="ao-related-t">📖 延伸閱讀</p>
<a href="https://aoaodelivery.com/blog/boat-party-catering-guide/">船P必備清單 2026｜遊船河準備、食物飲品份量懶人包 →</a>
<a href="https://aoaodelivery.com/blog/kids-birthday-party-catering/">【香港家長必讀】小朋友生日會到會挑選指南 →</a>
<a href="https://aoaodelivery.com/blog/company-event-catering-guide/">香港公司活動到會攻略 2026｜Budget、餐單、服務全指南 →</a>
</div>

{C.SRCS}
{C.POPUPS}
</div>
<script type="application/ld+json">{faq_ld}</script>
{C.LEAF_CSS}{C.SCRIPTS}
{FBJS}
'''

prev = '''<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>【2026香港野餐好去處】港九新界海景、大草地及隱世公園野餐地點推介</title></head><body style="margin:0;padding:24px 20px;background:#fff">
<div class="pk-demo-bar">DEMO｜<mark class="kw">黃色</mark>＝目標關鍵字／PAA　<label><input type="checkbox" id="hlToggle" checked> 顯示 highlight</label></div>
''' + BODY + '''<script>document.getElementById('hlToggle').onchange=function(){document.body.classList.toggle('no-hl',!this.checked)};</script></body></html>'''

# ---- 試做：文章頂部 Hero 搜尋區（真實篩選器放入 KV 位置）→ preview-hero.html ----
_IM = KVM.IMG
HERO = f"""<section class="pk-hero" aria-label="全港野餐地點搜尋器">
<img class="hbg" src="{_IM['cwb']}" alt="清水灣郊野公園" referrerpolicy="no-referrer" fetchpriority="high" loading="eager" decoding="async" width="960" height="720">
<span class="hlogo"><img src="{KVM._LG_ICON}" alt="" width="43" height="22" style="display:block!important;width:43px!important;height:22px!important;max-width:none!important;margin:0!important;border:0!important;box-shadow:none!important"><img class="lt" src="{KVM._LG_TEXT}" alt="Kitchen AO" width="114" height="19" style="display:block!important;width:114px!important;height:19px!important;max-width:none!important;margin:0!important;border:0!important;box-shadow:none!important"></span>
<div class="hgrid">
 <div class="hl">
  <p class="hpill">2026 香港野餐好去處</p>
  <p class="httl">全港野餐<span>地點搜尋器</span></p>
  <p class="hsub">{N} 個野餐地點 × 新界｜九龍｜港島</p>
  <p class="hsub2">可泊車、寵物友善野餐地點一鍵搜尋</p>
  {C.FILTER}
 </div>
 <div class="hr">
  <figure class="hp p1"><img src="{_IM['tpwp']}" alt="大埔海濱公園" referrerpolicy="no-referrer" loading="lazy"><figcaption><b style="color:{C.RC['nt']}">新界</b>大埔海濱公園</figcaption></figure>
  <figure class="hp p2"><img src="{_IM['ktct']}" alt="啟德郵輪碼頭公園" referrerpolicy="no-referrer" loading="lazy"><figcaption><b style="color:{C.RC['kln']}">九龍</b>啟德郵輪碼頭公園</figcaption></figure>
  <figure class="hp p3"><img src="{_IM['tamar']}" alt="添馬公園" referrerpolicy="no-referrer" loading="lazy"><figcaption><b style="color:{C.RC['hk']}">港島</b>添馬公園</figcaption></figure>
  <button type="button" class="hbox openP"><img src="{KVM.BOX}" alt="Kitchen AO 酒店級野餐盒" loading="lazy"><span>⭐ 推介酒店級野餐盒</span></button>
 </div>
</div>
</section>"""
HERO_CSS = """<style>
.ao-picnic .pk-hero{position:relative;container-type:inline-size;margin:0 0 20px;border-radius:18px;overflow:hidden;background:#3F6E4B;line-height:1.5}
.ao-picnic .pk-hero img{font-size:0}.ao-picnic .pk-hero .hbg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.ao-picnic .hlogo{position:absolute;right:18px;top:16px;z-index:3;display:inline-flex;align-items:center;gap:8px;height:42px;padding:0 16px;background:#fff;border:2px solid #1A1A1A;border-radius:30px}.ao-picnic .hlogo img{display:block;height:22px;width:auto}.ao-picnic .hlogo .lt{height:19px}
.ao-picnic .hgrid{position:relative;z-index:2;display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,1fr);gap:24px;padding:26px 26px 26px}
.ao-picnic .hpill{display:inline-block;margin:0 0 10px!important;background:#1A1A1A;color:#F7CE46;font-weight:900;font-size:15px;padding:5px 16px;border-radius:30px}
.ao-picnic .httl{margin:0!important;font-size:46px;font-weight:900;line-height:1.15;color:#fff;-webkit-text-stroke:6px #1A1A1A!important;paint-order:stroke fill;text-shadow:0 5px 0 #1A1A1A;letter-spacing:1px}.ao-picnic .httl span{color:#F7CE46}
.ao-picnic .hsub{margin:10px 0 0!important;font-size:19px;font-weight:900;color:#1A1A1A;-webkit-text-stroke:5px #fff!important;paint-order:stroke fill}
.ao-picnic .hsub2{display:inline-block;margin:12px 0 14px!important;background:#F7CE46;color:#1A1A1A;font-weight:900;font-size:16px;padding:6px 14px;box-shadow:4px 4px 0 #1A1A1A}
.ao-picnic .pk-hero .flt{margin:0;box-shadow:0 8px 24px rgba(0,0,0,.3)}
.ao-picnic .hr{position:relative;min-height:420px}
.ao-picnic .hp{position:absolute;margin:0;width:46%;background:#fff;padding:8px 8px 0;box-shadow:0 8px 20px rgba(0,0,0,.35)}.ao-picnic .hp img{display:block;width:100%;aspect-ratio:4/3;object-fit:cover;background:#E3EFDF}
.ao-picnic .hp figcaption{padding:6px 0 8px;font-size:13px;font-weight:900;color:#1A1A1A;text-align:center;line-height:1.3}.ao-picnic .hp figcaption b{margin-right:6px}
.ao-picnic .hp.p1{left:0;top:40px;transform:rotate(-5deg)}.ao-picnic .hp.p2{right:0;top:58px;transform:rotate(4deg)}.ao-picnic .hp.p3{left:8%;top:205px;transform:rotate(3deg);z-index:1}
.ao-picnic .hbox{position:absolute;right:4%;bottom:6px;width:42%;padding:4px 4px 46px;border:0;border-radius:14px;background:#fff;box-shadow:0 12px 28px rgba(0,0,0,.35);transform:rotate(-2deg);cursor:pointer;font-family:inherit;transition:transform .1s}
.ao-picnic .hbox:active{transform:rotate(-2deg) translateY(2px)}.ao-picnic .hbox img{display:block;width:100%;aspect-ratio:16/10;object-fit:cover;border-radius:10px}.ao-picnic .hbox span{position:absolute;left:-14px;right:-14px;bottom:9px;display:block;padding:7px 6px;text-align:center;font-size:14px;font-weight:900;color:#1A1A1A;background:#F7CE46;box-shadow:0 4px 10px rgba(0,0,0,.3)}.ao-picnic .hbox span::before,.ao-picnic .hbox span::after{content:'';position:absolute;bottom:-8px;border-top:8px solid #B8901E}.ao-picnic .hbox span::before{left:0;border-left:14px solid transparent}.ao-picnic .hbox span::after{right:0;border-right:14px solid transparent}
@container (max-width:760px){
 .ao-picnic .hgrid{grid-template-columns:1fr;gap:14px;padding:64px 14px 16px}
 .ao-picnic .httl{font-size:34px;-webkit-text-stroke:5px #1A1A1A!important;text-shadow:0 4px 0 #1A1A1A}.ao-picnic .hsub{font-size:16px}.ao-picnic .hsub2{font-size:14px}
 .ao-picnic .hr{order:-1;min-height:0;display:grid;grid-template-columns:repeat(3,1fr);gap:8px}
 .ao-picnic .hp{position:static;width:auto;padding:5px 5px 0}.ao-picnic .hp figcaption{font-size:11px}.ao-picnic .hp figcaption b{display:block;margin:0}
 .ao-picnic .hbox{display:none}
 .ao-picnic .hlogo{right:12px;top:12px;height:36px;padding:0 12px}.ao-picnic .hlogo img{width:35px!important;height:18px!important}.ao-picnic .hlogo .lt{width:90px!important;height:15px!important}
}
</style>"""
import re as _re
_m = _re.search(r'<div class="pk-kvg">.*?</iframe></div>', BODY, _re.S)
BODY_HERO = BODY.replace(C.FILTER, '', 1)
BODY_HERO = BODY_HERO.replace(_m.group(0), HERO_CSS + HERO, 1)
# H1 說明、引言卡及目錄移到搜尋結果（地點介紹）之後
_i = BODY_HERO.index('<p class="pk-h1note">'); _j = BODY_HERO.index('</nav>', _i) + len('</nav>')
_blk = BODY_HERO[_i:_j]; BODY_HERO = BODY_HERO[:_i] + BODY_HERO[_j:]
_k = BODY_HERO.index('<h2 class="ao-h2" id="dog">')
BODY_HERO = BODY_HERO[:_k] + _blk + '\n\n' + BODY_HERO[_k:]
# ---- 搜尋結果分頁：地圖／地點列表／比較表 ----
_tbl = C.TABLE("h2", "ao-h2")
BODY_HERO = BODY_HERO.replace(_tbl, '', 1)
_i = BODY_HERO.index('<h2 class="ao-h2" id="pk-tool">'); _j = BODY_HERO.index('</p>', BODY_HERO.index('<p class="ao-aio">', _i)) + 4
BODY_HERO = BODY_HERO[:_i] + f'''<h2 class="ao-h2 rh" id="pk-tool">🔍 全港野餐地點搜尋結果</h2>
<p class="ao-aio">我們精選全港 {N} 個熱門野餐地點，按新界、九龍及港島分區列出，每個地點均附鄰近停車場及寵物資料；無論想找<mark class="kw">野餐泊車</mark>地點，還是<mark class="kw">狗狗野餐好去處</mark>，都可以一目了然。</p>
<div class="rbar" id="results"><span class="rcnt">📍 全部 {N} 個地點</span><span class="rfil">未設條件</span></div>
<div class="rtabs" role="tablist"><button type="button" class="on" data-tab="map">🗺️ 地圖及地點列表</button><button type="button" data-tab="table">📊 野餐地點一覽表</button></div>''' + BODY_HERO[_j:]
_map = C.MAP('h3')
BODY_HERO = BODY_HERO.replace(_map, '<div class="rpanel on" data-tab="map">' + _map, 1)
_r = BODY_HERO.index(regions) + len(regions)
BODY_HERO = BODY_HERO[:_r] + '</div><div class="rpanel" data-tab="table">' + _tbl.replace('<details class="cmp">', '<details class="cmp" open>', 1) + '</div>' + BODY_HERO[_r:]
BODY_HERO = BODY_HERO.replace('</style><section class="pk-hero"', """
.ao-picnic .rh{margin-top:28px!important}
.ao-picnic .rbar{display:flex;flex-wrap:wrap;align-items:center;gap:8px 14px;margin:0 0 12px;padding:12px 16px;border-radius:14px;background:#F4FBF3;border:1.5px solid #CFE8CD}
.ao-picnic .rcnt{font-size:16px;font-weight:900;color:#1A1A1A}.ao-picnic .rfil{font-size:14px;font-weight:700;color:#2C6E49}
.ao-picnic .rmod{margin-left:auto;border:2px solid #1A1A1A;background:#fff;color:#1A1A1A;border-radius:30px;padding:6px 14px;font-weight:800;font-size:13.5px;cursor:pointer;box-shadow:2px 2px 0 #1A1A1A;font-family:inherit}.ao-picnic .rmod:active{transform:translate(2px,2px);box-shadow:none}
.ao-picnic .rtabs{display:grid;grid-template-columns:repeat(2,1fr);gap:8px;margin:0 0 14px}
.ao-picnic .rtabs button{border:2px solid #2C6E49;background:#fff;color:#2C6E49;border-radius:12px;padding:10px 6px;font-weight:900;font-size:15px;cursor:pointer;box-shadow:2px 2px 0 #2C6E49;font-family:inherit;transition:transform .08s,box-shadow .08s}
.ao-picnic .rtabs button.on{background:#3F9D5A;color:#fff;transform:translate(2px,2px);box-shadow:none}
.ao-picnic .rpanel{display:none}.ao-picnic .rpanel.on{display:block}
.ao-picnic .rpanel .cmp>summary,.ao-picnic .rpanel .tclose{display:none!important}.ao-picnic .rpanel #hk-table{border-bottom:0;padding-bottom:0}.ao-picnic .rpanel #hk-table .ao-h2{margin-top:6px!important}
@media(max-width:640px){.ao-picnic .rtabs button{font-size:13.5px;padding:9px 4px}.ao-picnic .rmod{margin-left:0}}
</style><section class="pk-hero" """.rstrip(), 1)
prev_hero = prev.replace(BODY, BODY_HERO)
if __name__ == '__main__':
    # 2026-10-18：正式版改用 Hero 搜尋區＋分頁版本
    open(os.path.join(HERE, 'preview.html'), 'w').write(prev_hero)
    open(os.path.join(HERE, 'index.html'), 'w').write(prev_hero)
    wp = re.sub(r'<mark class="(?:kw|paa)">(.*?)</mark>', r'\1', BODY_HERO)
    wp = re.sub(r'<p class="pk-kw">.*?</p>', '', wp)
    wp = re.sub(r'<p class="pk-h1note">.*?</p>', '', wp)
    open(os.path.join(HERE, 'blog-picnic-WORDPRESS.html'), 'w').write(wp)
    print('parks', N, 'car', sum(1 for p in P if p['car']), 'pet', sum(1 for p in P if p['pet'] == 'Y'), 'maps', sum(1 for p in P if p.get('petmap')))
