"""公司到會（18404）中英 Raw HTML 產生器
python3 build_corp.py → zh-rawhtml.html（Extra class：ao-zh）、en-rawhtml.html（Extra class：ao-en）
Tab 做法：所有內容都在 HTML 內（Google 可讀取）；JavaScript 載入後才把非當前分頁隱藏，沒有 JS 時全部顯示。
"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
P = 'https://aoaodelivery.com'
WA = 'https://wa.me/85269011987'

CSS = '''<style>
.page-id-18404 h1.heading-title{word-break:keep-all;text-wrap:balance;}
.ao-corp{max-width:860px;margin:0 auto;padding-top:28px;color:#3A342B;font-size:16px;line-height:1.8;}
.ao-corp h2{font-size:24px;font-weight:900;color:#1A1A1A;margin:32px 0 12px;padding-left:12px;border-left:6px solid #C8A24A;line-height:1.4;scroll-margin-top:110px;}
.ao-corp h3{font-size:18px;font-weight:800;color:#1A1A1A;margin:24px 0 8px;scroll-margin-top:110px;}
.ao-corp p{margin:0 0 14px;}
.ao-corp ul,.ao-corp ol{margin:0 0 16px;padding-left:22px;}
.ao-corp li{margin:0 0 6px;}
.ao-corp a{color:#9A7B2E;font-weight:700;}
.ao-corp .ao-tabwrap{position:relative;margin:18px 0 0;}
.ao-corp .ao-tabs{display:flex;align-items:stretch;height:50px;border-top:1px solid #EEE9DF;border-bottom:1px solid #EEE9DF;overflow-x:auto;overflow-y:hidden;scrollbar-width:none;-webkit-overflow-scrolling:touch;box-sizing:border-box;}
.ao-corp .ao-tabs::-webkit-scrollbar{display:none;}
.ao-corp .ao-tabs a{flex:1 0 auto;display:flex;align-items:center;justify-content:center;height:100%;box-sizing:border-box;padding:0 16px;font-size:15px;line-height:1;font-weight:700;color:#8A8172;text-decoration:none;white-space:nowrap;box-shadow:inset 0 -2px 0 transparent;transition:color .2s,box-shadow .2s;}
.ao-corp .ao-tabs a:hover{color:#1A1A1A;}
.ao-corp .ao-tabs a.on{color:#9A7B2E;box-shadow:inset 0 -2px 0 #C8A24A;}
.ao-corp.js-tabs .ao-pane{display:none;}
.ao-corp.js-tabs .ao-pane.on{display:block;animation:aoFade .25s ease;}
.ao-corp.js-tabs .ao-pane > h2:first-child{margin-top:22px;}
@keyframes aoFade{from{opacity:0;}to{opacity:1;}}
.ao-corp .ao-scene{display:flex;flex-wrap:wrap;justify-content:center;gap:14px;margin:12px 0 18px;}
.ao-corp .ao-scene a{position:relative;display:block;box-sizing:border-box;width:calc((100% - 28px)/3);background:#F4F7FA;border:1.5px solid #DCE3EA;border-radius:16px;padding:20px 16px 18px;text-align:center;text-decoration:none;color:#4A4238;font-weight:400;transition:border-color .2s,transform .2s;}
.ao-corp .ao-scene a:hover{border-color:#C8A24A;transform:translateY(-2px);}
.ao-corp .ao-scene .no{display:inline-block;width:26px;height:26px;line-height:26px;border-radius:50%;background:#45566E;color:#fff;font-size:13px;font-weight:800;}
.ao-corp .ao-scene .ic{display:block;font-size:26px;line-height:1;margin:10px 0 8px;}
.ao-corp .ao-scene b{display:block;color:#1A1A1A;font-size:16px;font-weight:900;margin:0 0 4px;}
.ao-corp .ao-scene .d{display:block;font-size:14px;line-height:1.6;color:#5A5246;}
.ao-corp .ao-scene .m{display:inline-block;margin-top:8px;font-size:13px;font-weight:800;color:#9A7B2E;background:#FFF8E6;border-radius:20px;padding:2px 10px;}
.ao-corp .ao-scene a.hot{background:#EEF4EC;border-color:#5E7E5C;}
.ao-corp .ao-scene a.hot .no{background:#5E7E5C;}
.ao-corp .ao-scene .tag{position:absolute;top:-11px;right:12px;background:#5E7E5C;color:#fff;font-size:12px;font-weight:800;padding:2px 10px;border-radius:12px;}
.ao-corp .ao-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:8px 0 16px;}
.ao-corp .ao-cards a{display:block;background:#fff;border:1.5px solid #EBE3D2;border-radius:14px;padding:14px 16px;text-decoration:none;color:#3A342B;font-weight:400;}
.ao-corp .ao-cards a:hover{border-color:#C8A24A;}
.ao-corp .ao-cards b{display:block;color:#1A1A1A;font-size:16px;margin-bottom:4px;}
.ao-corp .ao-cards span{font-size:14px;color:#6B6252;}
.ao-corp table{width:100%;border-collapse:collapse;margin:0 0 10px;font-size:15px;border:1px solid #EBE3D2;}
.ao-corp th{background:#1A1A1A;color:#F7CE46;text-align:left;padding:9px 12px;font-weight:800;}
.ao-corp td{border-top:1px solid #EBE3D2;padding:9px 12px;vertical-align:top;}
.ao-corp td:first-child{font-weight:800;color:#1A1A1A;background:#FAF7F1;}
.ao-corp .ao-tblwrap{overflow-x:auto;-webkit-overflow-scrolling:touch;}
.ao-corp .ao-faq{border:1px solid #EBE3D2;border-radius:12px;margin:0 0 10px;background:#fff;}
.ao-corp .ao-faq summary{cursor:pointer;list-style:none;padding:13px 44px 13px 16px;font-weight:800;color:#1A1A1A;position:relative;}
.ao-corp .ao-faq summary::-webkit-details-marker{display:none;}
.ao-corp .ao-faq summary:after{content:"+";position:absolute;right:16px;top:50%;margin-top:-14px;font-size:22px;color:#C8A24A;}
.ao-corp .ao-faq[open] summary:after{content:"\\2212";}
.ao-corp .ao-faq .a{padding:0 16px 14px;color:#4A4238;}
.ao-corp .ao-note{font-size:14px;color:#6B6252;}
.ao-corp .ao-cta{display:flex;justify-content:center;flex-wrap:wrap;gap:12px;margin:30px 0 10px;}
.ao-corp .ao-cta a{display:block;width:280px;box-sizing:border-box;text-align:center;background:#C8A24A!important;color:#1A1A1A!important;font-size:16px;font-weight:800;line-height:1.4;white-space:nowrap;padding:14px 20px;border:2px solid #C8A24A;border-radius:40px;text-decoration:none!important;transition:background .2s,color .2s;}
.ao-corp .ao-cta a:hover{background:#1A1A1A!important;color:#F7CE46!important;border-color:#1A1A1A;}
.ao-corp .ao-cta a.alt{background:#1A1A1A!important;color:#F7CE46!important;border-color:#1A1A1A;}
.ao-corp .ao-cta a.alt:hover{background:#C8A24A!important;color:#1A1A1A!important;border-color:#C8A24A;}
.ao-corp img{max-width:100%;height:auto;border-radius:14px;}
.ao-corp .ao-kv{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:0 0 14px;}
.ao-corp .ao-kv img{display:block;width:100%;height:auto;aspect-ratio:2/3;object-fit:cover;border-radius:14px;}
.ao-corp .ao-kv img.k1{object-position:50% 30%;}
.ao-corp .ao-kv img.k2{object-position:50% 55%;}
@media(max-width:768px){.ao-corp .ao-scene a{width:calc((100% - 14px)/2);}}
@media(max-width:600px){.ao-corp .ao-cards{grid-template-columns:1fr;}.ao-corp .ao-scene a{width:100%;}.ao-corp .ao-tabs{height:46px;}.ao-corp .ao-tabs a{flex:0 0 auto;padding:0 14px;font-size:14px;}.ao-corp .ao-kv{gap:6px;}.ao-corp .ao-kv img{aspect-ratio:3/4;border-radius:10px;}.ao-corp h2{font-size:21px;}.ao-corp .ao-cta a{width:100%;max-width:300px;}}
</style>'''

# 分頁：按下去只換內容；網址 #hash 同步，方便分享及 FAQ 直達
JS = '''<script>(function(){var r=document.querySelector(".ao-corp");if(!r)return;var n=r.querySelector(".ao-tabs");if(!n)return;var T=[].slice.call(n.querySelectorAll("a")),P=T.map(function(a){return document.getElementById(a.getAttribute("href").slice(1))});if(P.some(function(p){return !p}))return;r.classList.add("js-tabs");n.setAttribute("role","tablist");function show(i,push){T.forEach(function(a,k){var on=k===i;a.classList.toggle("on",on);a.setAttribute("aria-selected",on?"true":"false");P[k].classList.toggle("on",on);});var a=T[i];if(n.scrollWidth>n.clientWidth)n.scrollTo({left:a.offsetLeft-(n.clientWidth-a.offsetWidth)/2,behavior:"smooth"});if(push&&history.replaceState)history.replaceState(null,"","#"+P[i].id);}T.forEach(function(a,i){a.setAttribute("role","tab");P[i].setAttribute("role","tabpanel");a.addEventListener("click",function(e){e.preventDefault();show(i,true);var top=n.getBoundingClientRect().top+window.pageYOffset-120;if(window.pageYOffset>top)window.scrollTo({top:top,behavior:"smooth"});});});function fromHash(){var h=location.hash.slice(1);if(!h)return 0;var el=document.getElementById(h);if(!el)return 0;for(var k=0;k<P.length;k++){if(P[k]===el||P[k].contains(el))return k;}return 0;}var s=fromHash();show(s,false);if(location.hash&&s){setTimeout(function(){var el=document.getElementById(location.hash.slice(1));if(el)el.scrollIntoView({behavior:"smooth"});},150);}window.addEventListener("hashchange",function(){show(fromHash(),false);});[].slice.call(r.querySelectorAll('a[href^="#"]')).forEach(function(l){if(n.contains(l))return;l.addEventListener("click",function(e){var el=document.getElementById(l.getAttribute("href").slice(1));if(!el)return;for(var k=0;k<P.length;k++){if(P[k]===el||P[k].contains(el)){e.preventDefault();show(k,true);var top=n.getBoundingClientRect().top+window.pageYOffset-120;window.scrollTo({top:top,behavior:"smooth"});return;}}});});})();</script>'''


def build(L):
    o = ['<div class="ao-corp">', CSS, '']
    o.append(L['intro'])
    o.append(f'<div class="ao-kv"><img class="k1" decoding="async" src="{P}/wp-content/uploads/2026/03/WhatsApp-Image-2026-03-25-at-3.58.36-PM-scaled.jpeg" alt="{L["img_alt"]}" width="600" height="300" /><img class="k2" decoding="async" src="{P}/wp-content/uploads/2023/11/IMG_2358.jpg" alt="{L["img_alt2"]}" width="600" height="300" /></div>')
    o.append(f'<div class="ao-tabwrap"><nav class="ao-tabs" aria-label="{L["nav_label"]}">')
    for i, (pid, label, _) in enumerate(L['panes']):
        on = ' class="on"' if i == 0 else ''
        o.append(f'<a href="#{pid}"{on}>{label}</a>')
    o.append('</nav></div>')
    for pid, label, html in L['panes']:
        o.append(f'<section class="ao-pane" id="{pid}">\n{html.strip()}\n</section>')
    faq = L['faq']
    o.append('<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}, ensure_ascii=False, separators=(',', ':')) + '</script>')
    o.append('<script type="application/ld+json">' + json.dumps(L['service'], ensure_ascii=False, separators=(',', ':')) + '</script>')
    o.append(L['cta'])
    o.append(L['updated'])
    o.append(JS)
    o.append('</div>')
    return '\n'.join(o) + '\n'


def faq_html(faq):
    return '\n'.join(f'<details class="ao-faq"><summary>{q}</summary><div class="a">{a}</div></details>' for q, a in faq)


def a(path, text):
    return f'<a href="{P}{path}">{text}</a>'


def scene(items):
    o = ['<div class="ao-scene">']
    for i, (href, ic, title, desc, meta, tag) in enumerate(items, 1):
        cls = ' class="hot"' if tag else ''
        t = f'<span class="tag">{tag}</span>' if tag else ''
        o.append(f'<a href="#{href}"{cls}>{t}<span class="no">{i}</span><span class="ic" aria-hidden="true">{ic}</span><b>{title}</b><span class="d">{desc}</span><span class="m">{meta}</span></a>')
    o.append('</div>')
    return '\n'.join(o)


# ---------------- 中文 ----------------
ZH_FAQ = [
    ('公司到會價錢是多少？', '按人數、菜式及送貨地區計算。參考價方面，Office Lunch 商務餐盒每位 HK$108 起，會議午餐高級餐盒每位 HK$248 起，Annual Dinner 及公司聚會每位 HK$300 起。'),
    ('公司到會要提前多少日預訂？', '建議盡早預訂，尤其是 12 月至農曆新年的公司活動旺季。所需日數視乎人數及菜式，可先透過 WhatsApp 向客服確認。'),
    ('公司到會有沒有素食選擇？', '有。請在查詢時說明素食人數及要求，例如是否需要全素或走五辛，客服會按要求安排菜單。'),
    ('Annual Dinner 到會大約需要多少預算？', '以每位 HK$300 起計算，100 人的 Annual Dinner 到會預算約 HK$30,000，包括迎賓小食、主菜及甜品。'),
    ('怎樣預訂公司到會？', '可透過 WhatsApp 852-6901-1987、電郵 info@aoaodelivery.com，或填寫網站的到會報價查詢表格。'),
]
ZH_SCENES = [
    ('office-lunch', '🍱', 'Office Lunch／員工飯盒', '商務餐盒每人一盒，日常午餐、培訓及加班膳食都適用', '10 至 100 人｜HK$108 起', ''),
    ('office-lunch', '💼', 'Meeting Lunch／會議午餐', '高級餐盒更講究，客戶會議及貴賓接待更體面', '10 至 100 人｜HK$248 起', ''),
    ('annual-dinner', '🏆', 'Annual Dinner／頒獎晚宴', '迎賓小食、熱盤主菜到壓軸甜品，撐起整晚排場', '50 至 200 人以上｜HK$300 起', '年尾旺季'),
    ('festive', '🎉', '公司聚會／Team Building', '自助餐形式自由取用，員工聚會及節日派對首選', '30 至 300 人｜HK$300 起', ''),
    ('business-event', '🥂', '酒會／開張／發佈會', 'Canapés 及 Finger Food 一口一件，邊走邊交流', '20 至 200 人以上｜按餐單報價', ''),
]
ZH = dict(
    intro='<p>由每日的一盒午餐，到年尾的週年晚宴，公司活動的餐飲往往是同事最記得的細節。Kitchen AO 的<strong>香港公司到會</strong>服務，按人數及預算為企業度身安排餐單，由 10 人部門午餐到 300 人公司聚會都可以配合，並設全港送貨。</p>',
    img_alt='Kitchen AO 團隊在公司活動現場準備到會食物',
    img_alt2='Kitchen AO 侍應在商務活動現場擺放自助餐到會餐點',
    nav_label='公司到會目錄',
    panes=[
        ('overview', '公司到會速覽', f'''
<h2>Kitchen AO 公司到會服務：由午餐盒到年會，五種企業到會方案</h2>
<p>作為香港到會公司，Kitchen AO 為企業提供一站式公司到會服務。由日常員工飯盒、客戶會議午餐，到 Annual Dinner、公司聚會及酒會開張，我們都有對應的餐盒、套餐及小食方案，並按人數及預算度身配搭，全港送貨。按下卡片即可查看各項服務詳情：</p>
{scene(ZH_SCENES)}
<h3>人數及預算一覽</h3>
<div class="ao-tblwrap"><table>
<thead><tr><th>活動類型</th><th>人數</th><th>到會形式</th><th>每位參考價</th></tr></thead>
<tbody>
<tr><td>Office Lunch／員工飯盒</td><td>10 至 100 人</td><td>{a("/product-category/商務活動/commercial-lunch-box/", "商務餐盒")}</td><td>HK$108 起</td></tr>
<tr><td>Meeting Lunch／會議午餐</td><td>10 至 100 人</td><td>{a("/product-category/商務活動/executive-premium-meal-box/", "高級餐盒")}</td><td>HK$248 起</td></tr>
<tr><td>Annual Dinner／頒獎晚宴</td><td>50 至 200 人以上</td><td>迎賓小食、熱盤主菜、甜品</td><td>HK$300 起</td></tr>
<tr><td>公司聚會／Team Building</td><td>30 至 300 人</td><td>自助餐式到會套餐</td><td>HK$300 起</td></tr>
<tr><td>酒會／開張／發佈會</td><td>20 至 200 人以上</td><td>Canapés、Finger Food</td><td>按餐單報價</td></tr>
</tbody></table></div>
<p class="ao-note">以上公司到會推介配搭為參考價，實際價錢按人數、菜式及送貨地區計算。</p>
<h3>企業客戶選擇 Kitchen AO 公司到會服務的四個原因</h3>
<ul>
<li><strong>菜單跟著活動走：</strong>中西菜式自由配搭，並設素食及無麩質選擇，照顧不同同事的飲食需要。</li>
<li><strong>人數可多可少：</strong>由 10 人部門午餐到 300 人公司聚會，份量都可以按人數調整。</li>
<li><strong>熱盤保持溫度：</strong>熱盤以保溫包裝送達，活動一開始即可上桌。</li>
<li><strong>報價清楚直接：</strong>提供人數、日期及預算，客服便會提供餐單、價錢及送貨安排。</li>
</ul>'''),
        ('office-lunch', 'Office Lunch', f'''
<h2>Office Lunch 到會：日常午餐與會議午餐，兩種需要兩種選擇</h2>
<p>午餐到會看似簡單，其實最考細節。每日的員工午餐要準時送到、方便分派；與客戶開會時的一頓午餐，則代表公司的待客之道。Office Lunch 到會因此可分兩類：</p>
<h3>員工飯盒：商務餐盒 HK$108 起</h3>
<p>適合 10 至 100 人的日常午餐、內部培訓及加班膳食。每人一盒，派發快捷，亦方便按人數增減。詳情見{a("/product-category/商務活動/commercial-lunch-box/", "商務餐盒")}，另有{a("/product-category/商務活動/staff-meal/", "員工膳食餐盒")}可供選擇。</p>
<h3>會議午餐：高級餐盒 HK$248 起</h3>
<p>適合 10 至 100 人的客戶會議、董事會議及貴賓接待。菜式及包裝更講究，即使是一頓會議午餐，也能為公司形象加分。詳情見{a("/product-category/商務活動/executive-premium-meal-box/", "高級餐盒")}。</p>
<h3>想更豐富？加配熱盤及小食</h3>
<ul>
<li><strong>熱盤：</strong>{a("/product/m0500-honey-glazed-german-salted-pork-knuckle-1-pcs/", "蜜蜜糖德國鹹豬手")}、{a("/product/p03l-black-truffle-wild-mushroom-and-asparagus-cream-pasta-4-pounds/", "黑松露野菌蘆筍忌廉意粉")}</li>
<li><strong>小食：</strong>{a("/product/a0700-handmade-mini-cheeseburger/", "迷你芝士手打豬肉牛肉漢堡")}、{a("/product/a3400-deep-fried-sesame-shrimp-toast-with-thai-sauce/", "懷舊芝麻蝦滑多士")}、{a("/product/a1500-crispy-seafood-tofu-in-traditional-typhoon-shelter-style/", "避風塘炸海鮮豆腐")}</li>
<li><strong>沙律：</strong>{a("/product/s0300-smoked-salmon-caesar-salad/", "油香煙三文魚凱撒沙律")}</li>
</ul>
<p>想按人數一次過訂購，可參考{a("/product-category/party-set-by-people/", "人數選餐")}。</p>'''),
        ('annual-dinner', 'Annual Dinner', f'''
<h2>Annual Dinner 到會：年會的排場，由餐桌開始</h2>
<p>一場成功的年會，餐飲節奏與台上節目同樣重要。Annual Dinner 到會一般分為三部分：賓客入場時的迎賓小食、正式開席的熱盤主菜，以及為晚宴作結的甜品。這個配搭適合 50 至 200 人以上的年會到會及頒獎晚宴，每位 HK$300 起。菜式參考：</p>
<ul>
<li><strong>迎賓小食：</strong>{a("/product/c1201-照燒慢煮雞卷配牛油果蓉-1件/", "照燒慢煮雞卷配牛油果蓉")}、{a("/product/c0701-炙燒帶子芋頭紫椰菜串-1串/", "炙燒帶子芋頭紫椰菜串")}、{a("/product/c0101-一口和牛野菌串-1串/", "一口和牛野菌串")}</li>
<li><strong>主菜：</strong>{a("/product/ms02l-西京燒「富士金襴」威士忌白味噌燒鹿兒島叉燒/", "西京燒威士忌白味噌燒鹿兒島叉燒")}、{a("/product/m0315-homemade-black-truffle-butter-baked-cornish-hen-1-5-chickens/", "自家製黑松露牛油慢焗法國黃油雞")}、{a("/product/ps01l「冩樂」清酒煮蟹皇灸燒左口魚醬油㷛仔飯-4磅/", "清酒煮蟹皇灸燒左口魚醬油煲仔飯")}</li>
<li><strong>甜品：</strong>{a("/product/d01-french-colorful-macarons-10-pieces/", "法式七彩馬卡龍")}、{a("/product/d06-caramel-tart-10個/", "焦糖葡撻")}</li>
</ul>
<p><strong>籌備貼士：</strong>人數較多的年會，宜先確定開席時間及場地擺放食物的空間，再安排送達時間。如需要侍應服務，可在查詢時一併提出。</p>'''),
        ('festive', '公司聚會', f'''
<h2>公司聚會及節日活動：聖誕派對、春茗、團年飯，旺季宜早預訂</h2>
<p>每年 12 月至農曆新年，是企業活動最密集的時段。由聖誕派對、公司團年飯、公司開年飯到春茗到會，查詢都明顯增加。公司聚會到會多採用自助餐形式，賓客可隨意取用，最適合 30 至 300 人的 Team Building、產品發佈及節日聚會，每位 HK$300 起。</p>
<ul>
<li><strong>自助餐菜式參考：</strong>{a("/product/a1600-japanese-chicken-skin-dumplings-with-crispy-onion-rings/", "日式雞皮餃子配洋蔥圈")}、{a("/product/a3000-braised-abalone-vol-au-vent-with-mushrooms-in-oyster-sauce/", "蠔油鮑汁野菌鮑魚酥")}、{a("/product/a0200-grilled-satay-skewer-pork-and-chicken/", "香烤沙嗲串燒")}</li>
<li><strong>套餐：</strong>{a("/product-category/party/foot-party/", "美食派對 Gourmet 套餐")}，按人數由 5 人至 85 人選擇</li>
<li><strong>聖誕派對：</strong>可參考{a("/blog/christmas-catering-hong-kong/", "聖誕到會推介")}</li>
</ul>'''),
        ('business-event', '酒會開張', f'''
<h2>酒會、開張及發佈會：站著吃，也要吃得精緻</h2>
<p>酒會及開張活動多以站立形式進行，賓客邊走邊交流，一口一件的 Canapés 及 Finger Food 最合適，既方便取用，又不會打斷談話。這類活動適合 20 至 200 人以上，價錢按餐單報價。詳情可參考{a("/business-event/", "商務活動到會")}，或選擇{a("/product-category/商務活動/a-bit-of-cuisines-gourmet-in-a-box/", "舌尖上的餐桌九宮格 Canapés")}及{a("/product-category/商務活動/royal-snackers-box/", "皇家小食盒")}。</p>'''),
        ('price', '價錢及流程', f'''
<h2>公司到會價錢怎樣計算？四個預算例子</h2>
<p>公司到會的價錢主要由人數、菜式及送貨地區決定。以下例子可作初步預算參考：</p>
<div class="ao-tblwrap"><table>
<thead><tr><th>活動類型</th><th>人數</th><th>每位參考價</th><th>總預算例子</th><th>特色</th></tr></thead>
<tbody>
<tr><td>Office Lunch（商務餐盒）</td><td>20 人</td><td>HK$108</td><td>HK$2,160</td><td>每人一盒，方便分派</td></tr>
<tr><td>Meeting Lunch（高級餐盒）</td><td>20 人</td><td>HK$248</td><td>HK$4,960</td><td>適合會議及貴賓接待</td></tr>
<tr><td>Annual Dinner</td><td>80 人</td><td>HK$300</td><td>HK$24,000</td><td>熱盤主菜</td></tr>
<tr><td>Team Building</td><td>50 人</td><td>HK$300</td><td>HK$15,000</td><td>自助餐及小食</td></tr>
</tbody></table></div>
<p class="ao-note">運費按送貨地區計算；單一訂單滿 HK$1,450 全港免運費，詳情見{a("/delivery/", "送貨需知")}。</p>
<h2 id="process">公司到會預訂流程：四步完成</h2>
<ol>
<li><strong>提供資料：</strong>人數、日期、送達時間、地址、預算及特別飲食要求。</li>
<li><strong>收取餐單及報價：</strong>客服按資料提供建議餐單。</li>
<li><strong>確認訂單及付款：</strong>可使用轉數快或 PayMe 等方式付款。</li>
<li><strong>活動當日：</strong>按約定時間送達。</li>
</ol>
<p>船河及戶外活動另行報價。可以直接填寫{a("/catering-quote-enquiry/", "到會報價查詢")}，或參考我們的{a("/合作伙伴/", "合作夥伴與服務實績")}。</p>'''),
        ('faq', '常見問題', '<h2>公司到會常見問題</h2>\n' + faq_html(ZH_FAQ)),
    ],
    faq=ZH_FAQ,
    service={"@context": "https://schema.org", "@type": "Service", "serviceType": "公司到會", "name": "Kitchen AO 香港公司到會", "areaServed": {"@type": "Place", "name": "香港"}, "provider": {"@type": "Organization", "name": "Kitchen AO", "url": "https://aoaodelivery.com/"}, "url": "https://aoaodelivery.com/corporate-catering-hk/"},
    cta=f'<div class="ao-cta"><a class="alt" href="{P}/catering-quote-enquiry/">到會報價查詢</a><a href="{WA}?text=%E5%85%AC%E5%8F%B8%E5%88%B0%E6%9C%83%E6%9F%A5%E8%A9%A2" target="_blank" rel="noopener">WhatsApp 查詢公司到會</a></div>',
    updated='<p class="ao-note">最後更新：2026 年 10 月</p>',
)

# ---------------- English ----------------
EN_FAQ = [
    ('How much does corporate catering cost?', 'It depends on headcount, menu and delivery area. As a reference, office lunch commercial lunch boxes start from HK$108 per person, meeting lunch executive meal boxes from HK$248 per person, and annual dinners and company gatherings from HK$300 per person.'),
    ('How far in advance should I book corporate catering?', 'We recommend booking as early as possible, especially during the busy company event season from December to Chinese New Year. The lead time depends on headcount and menu, so please check with our team on WhatsApp first.'),
    ('Do you offer vegetarian options for corporate catering?', 'Yes. Tell us how many vegetarian guests you have and their requirements, such as vegan or no five pungent spices, and we will arrange the menu accordingly.'),
    ('What budget do I need for annual dinner catering?', 'From HK$300 per person, annual dinner catering for 100 guests costs about HK$30,000, including welcome canapés, mains and desserts.'),
    ('How do I book corporate catering?', 'Contact us on WhatsApp at 852-6901-1987, email info@aoaodelivery.com, or fill in the catering quote enquiry form on our website.'),
]
EN_SCENES = [
    ('office-lunch', '🍱', 'Office Lunch', 'One commercial lunch box per person for everyday lunches, training and overtime meals', '10 to 100 guests | from HK$108', ''),
    ('office-lunch', '💼', 'Meeting Lunch', 'Executive meal boxes with a more refined touch for client meetings and VIP guests', '10 to 100 guests | from HK$248', ''),
    ('annual-dinner', '🏆', 'Annual Dinner', 'From welcome canapés and hot mains to a sweet finale, built for the big night', '50 to 200+ guests | from HK$300', 'Peak season'),
    ('festive', '🎉', 'Team Building', 'Help-yourself buffets for staff gatherings and festive parties', '30 to 300 guests | from HK$300', ''),
    ('business-event', '🥂', 'Receptions &amp; Openings', 'Bite-sized canapés and finger food that keep guests mingling', '20 to 200+ guests | quoted by menu', ''),
]
EN = dict(
    intro='<p>From the daily lunch box to the year-end annual dinner, the food is often what colleagues remember most about a company event. Kitchen AO provides <strong>corporate catering in Hong Kong</strong> with menus tailored to your headcount and budget, from a 10-person department lunch to a company gathering of 300, with delivery across Hong Kong.</p>',
    img_alt='Kitchen AO team preparing corporate catering at a company event in Hong Kong',
    img_alt2='Kitchen AO staff setting up a catering buffet at a business event',
    nav_label='Corporate catering contents',
    panes=[
        ('overview', 'Overview', f'''
<h2>Our Corporate Catering Services in Hong Kong: Five Solutions, from Lunch Boxes to Annual Dinners</h2>
<p>As a Hong Kong catering company, Kitchen AO offers one-stop corporate catering services. From everyday staff lunch boxes and client meeting lunches to annual dinners, company gatherings and grand openings, we have meal boxes, catering sets and canapés for every occasion, tailored to your headcount and budget, with delivery across Hong Kong. Tap a card to see each service:</p>
{scene(EN_SCENES)}
<h3>Headcount and Budget at a Glance</h3>
<div class="ao-tblwrap"><table>
<thead><tr><th>Event type</th><th>Guests</th><th>Catering format</th><th>Reference price per person</th></tr></thead>
<tbody>
<tr><td>Office lunch / staff lunch boxes</td><td>10 to 100</td><td>{a("/product-category/商務活動/commercial-lunch-box/", "Commercial Lunch Box")}</td><td>From HK$108</td></tr>
<tr><td>Meeting lunch</td><td>10 to 100</td><td>{a("/product-category/商務活動/executive-premium-meal-box/", "Executive Premium Meal Box")}</td><td>From HK$248</td></tr>
<tr><td>Annual dinner / awards night</td><td>50 to 200+</td><td>Welcome canapés, hot mains, desserts</td><td>From HK$300</td></tr>
<tr><td>Company gathering / team building</td><td>30 to 300</td><td>Buffet-style catering sets</td><td>From HK$300</td></tr>
<tr><td>Reception / opening / product launch</td><td>20 to 200+</td><td>Canapés and finger food</td><td>Quoted by menu</td></tr>
</tbody></table></div>
<p class="ao-note">Reference prices only. Final prices depend on headcount, menu and delivery area.</p>
<h3>Four Reasons Companies Choose Kitchen AO Corporate Catering Services</h3>
<ul>
<li><strong>Menus that fit the occasion:</strong> Mix Chinese and Western dishes, with vegetarian and gluten-free options for colleagues with dietary needs.</li>
<li><strong>Any headcount:</strong> From a 10-person department lunch to a company gathering of 300, portions are adjusted to your numbers.</li>
<li><strong>Hot food, served hot:</strong> Hot dishes arrive in insulated packaging, ready to serve as soon as your event begins.</li>
<li><strong>Straightforward quotes:</strong> Share your headcount, date and budget, and our team will send a menu, price and delivery plan.</li>
</ul>'''),
        ('office-lunch', 'Office Lunch', f'''
<h2>Office Lunch Catering: Two Kinds of Lunch, Two Solutions</h2>
<p>Office catering in Hong Kong may look simple, but the details matter. Everyday staff lunches need to arrive on time and be easy to hand out, while a lunch served at a client meeting reflects how your company treats its guests. That is why office lunch catering comes in two forms:</p>
<h3>Staff Lunch Boxes: Commercial Lunch Box from HK$108</h3>
<p>For everyday lunches, in-house training and overtime meals of 10 to 100 people. One box per person makes distribution quick and lets you adjust numbers easily. See our {a("/product-category/商務活動/commercial-lunch-box/", "Commercial Lunch Box")} range, or the {a("/product-category/商務活動/staff-meal/", "Staff Meal Box")}.</p>
<h3>Meeting Lunch: Executive Premium Meal Box from HK$248</h3>
<p>For client meetings, board meetings and VIP guests of 10 to 100 people. More refined dishes and packaging mean even a working lunch leaves a good impression. See our {a("/product-category/商務活動/executive-premium-meal-box/", "Executive Premium Meal Box")}.</p>
<h3>Want More? Add Hot Dishes and Snacks</h3>
<ul>
<li><strong>Hot dishes:</strong> {a("/product/m0500-honey-glazed-german-salted-pork-knuckle-1-pcs/", "Honey Glazed German Pork Knuckle")}, {a("/product/p03l-black-truffle-wild-mushroom-and-asparagus-cream-pasta-4-pounds/", "Black Truffle Wild Mushroom Asparagus Cream Pasta")}</li>
<li><strong>Snacks:</strong> {a("/product/a0700-handmade-mini-cheeseburger/", "Mini Hand-Pattied Cheese Burgers")}, {a("/product/a3400-deep-fried-sesame-shrimp-toast-with-thai-sauce/", "Sesame Shrimp Toast")}, {a("/product/a1500-crispy-seafood-tofu-in-traditional-typhoon-shelter-style/", "Typhoon Shelter Style Crispy Seafood Tofu")}</li>
<li><strong>Salad:</strong> {a("/product/s0300-smoked-salmon-caesar-salad/", "Smoked Salmon Signature Caesar Salad")}</li>
</ul>
<p>To order by headcount in one go, see our {a("/product-category/party-set-by-people/", "party sets by number of guests")}.</p>'''),
        ('annual-dinner', 'Annual Dinner', f'''
<h2>Annual Dinner Catering: A Memorable Night Starts at the Table</h2>
<p>Planning a company annual dinner in Hong Kong? The pace of the food matters as much as the show on stage. Annual dinner catering usually comes in three parts: welcome canapés as guests arrive, hot mains once dinner begins, and desserts to close the evening. This format suits annual dinners and award ceremonies of 50 to 200+ guests, from HK$300 per person. Sample dishes:</p>
<ul>
<li><strong>Welcome canapés:</strong> {a("/product/c1201-照燒慢煮雞卷配牛油果蓉-1件/", "Teriyaki Chicken Roll with Avocado")}, {a("/product/c0701-炙燒帶子芋頭紫椰菜串-1串/", "Seared Scallop, Taro &amp; Red Cabbage Skewer")}, {a("/product/c0101-一口和牛野菌串-1串/", "Wagyu &amp; Wild Mushroom Skewer")}</li>
<li><strong>Mains:</strong> {a("/product/ms02l-西京燒「富士金襴」威士忌白味噌燒鹿兒島叉燒/", "Saikyo Miso &amp; Whisky Glazed Kagoshima Char Siu")}, {a("/product/m0315-homemade-black-truffle-butter-baked-cornish-hen-1-5-chickens/", "Slow-roasted French Yellow Spring Chicken with Black Truffle Butter")}, {a("/product/ps01l「冩樂」清酒煮蟹皇灸燒左口魚醬油㷛仔飯-4磅/", "Sharaku Sake-Braised Crab Roe &amp; Seared Flounder Claypot Rice")}</li>
<li><strong>Desserts:</strong> {a("/product/d01-french-colorful-macarons-10-pieces/", "French Rainbow Macarons")}, {a("/product/d06-caramel-tart-10個/", "Caramel Portuguese Tarts")}</li>
</ul>
<p><strong>Planning tip:</strong> For a large annual dinner, confirm your dinner start time and the space available at the venue for setting up the food before arranging the delivery time. If you need service staff, let us know when you enquire.</p>'''),
        ('festive', 'Gatherings', f'''
<h2>Company Gatherings and Festive Events: Book Early for Christmas, Spring and Year-end Dinners</h2>
<p>December to Chinese New Year is the busiest time of year for company events, with enquiries rising for Christmas parties, year-end dinners and spring dinners. Company gathering catering is usually served as a buffet so guests can help themselves, ideal for team building, product launches and festive gatherings of 30 to 300 guests, from HK$300 per person.</p>
<ul>
<li><strong>Sample buffet dishes:</strong> {a("/product/a1600-japanese-chicken-skin-dumplings-with-crispy-onion-rings/", "Japanese Chicken Skin Dumplings with Crispy Onion Rings")}, {a("/product/a3000-braised-abalone-vol-au-vent-with-mushrooms-in-oyster-sauce/", "Braised Abalone &amp; Wild Mushroom Puff Pastry")}, {a("/product/a0200-grilled-satay-skewer-pork-and-chicken/", "Grilled Satay Skewers")}</li>
<li><strong>Catering sets:</strong> {a("/product-category/party/foot-party/", "Gourmet party sets")} for 5 to 85 guests</li>
</ul>'''),
        ('business-event', 'Receptions', f'''
<h2>Receptions, Openings and Product Launches: Finger Food Done Right</h2>
<p>Receptions and grand openings are usually standing events where guests mingle as they eat, so bite-sized canapés and finger food work best: easy to pick up, and they never interrupt a conversation. These events suit 20 to 200+ guests and are quoted by menu. See our {a("/business-event/", "event catering")} page, or choose the {a("/product-category/商務活動/a-bit-of-cuisines-gourmet-in-a-box/", "Nine Delights Gourmet Canapés Box")} and {a("/product-category/商務活動/royal-snackers-box/", "Royal Snackers Box")}.</p>'''),
        ('price', 'Prices &amp; Booking', f'''
<h2>How Much Does Corporate Catering Cost in Hong Kong? Four Budget Examples</h2>
<p>Corporate catering prices depend mainly on headcount, menu and delivery area. Use these examples as a starting point for your budget:</p>
<div class="ao-tblwrap"><table>
<thead><tr><th>Event type</th><th>Guests</th><th>Reference price per person</th><th>Total budget (example)</th><th>Highlights</th></tr></thead>
<tbody>
<tr><td>Office lunch (Commercial Lunch Box)</td><td>20</td><td>HK$108</td><td>HK$2,160</td><td>One box per person, easy to hand out</td></tr>
<tr><td>Meeting lunch (Executive Premium Meal Box)</td><td>20</td><td>HK$248</td><td>HK$4,960</td><td>For meetings and VIP guests</td></tr>
<tr><td>Annual dinner</td><td>80</td><td>HK$300</td><td>HK$24,000</td><td>Hot mains</td></tr>
<tr><td>Team building</td><td>50</td><td>HK$300</td><td>HK$15,000</td><td>Buffet and snacks</td></tr>
</tbody></table></div>
<p class="ao-note">Delivery fees depend on the delivery area. Orders of HK$1,450 or more get free delivery across Hong Kong. See {a("/delivery/", "Delivery Info")} for details.</p>
<h2 id="process">How to Book Corporate Catering in Four Steps</h2>
<ol>
<li><strong>Send us your details:</strong> headcount, date, delivery time, address, budget and any dietary requirements.</li>
<li><strong>Receive a menu and quotation:</strong> our team will suggest a menu based on your details.</li>
<li><strong>Confirm and pay:</strong> payment methods include FPS and PayMe.</li>
<li><strong>On the day:</strong> delivery at the agreed time.</li>
</ol>
<p>Boat parties and outdoor events are quoted separately. Fill in our {a("/catering-quote-enquiry/", "catering quote enquiry")} form, or see our {a("/合作伙伴/", "partners and service records")}.</p>'''),
        ('faq', 'FAQ', '<h2>Corporate Catering FAQ</h2>\n' + faq_html(EN_FAQ)),
    ],
    faq=EN_FAQ,
    service={"@context": "https://schema.org", "@type": "Service", "serviceType": "Corporate catering", "name": "Kitchen AO Corporate Catering Hong Kong", "areaServed": {"@type": "Place", "name": "Hong Kong"}, "provider": {"@type": "Organization", "name": "Kitchen AO", "url": "https://aoaodelivery.com/"}, "url": "https://aoaodelivery.com/en/corporate-catering-hk/"},
    cta=f'<div class="ao-cta"><a class="alt" href="{P}/catering-quote-enquiry/">Get a Catering Quote</a><a href="{WA}?text=Corporate%20catering%20enquiry" target="_blank" rel="noopener">WhatsApp Us About Corporate Catering</a></div>',
    updated='<p class="ao-note">Last updated: October 2026</p>',
)

if __name__ == '__main__':
    open(os.path.join(HERE, 'zh-rawhtml.html'), 'w', encoding='utf-8').write(build(ZH))
    open(os.path.join(HERE, 'en-rawhtml.html'), 'w', encoding='utf-8').write(build(EN))
    print('ok')
