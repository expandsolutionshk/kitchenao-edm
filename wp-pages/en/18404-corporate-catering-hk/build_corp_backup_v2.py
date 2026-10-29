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
.ao-corp .ao-scene{list-style:none;padding:0;margin:8px 0 16px;}
.ao-corp .ao-scene li{background:#FFF8E6;border:1.5px solid #E9D9AE;border-radius:12px;padding:12px 16px;margin:0 0 10px;}
.ao-corp .ao-scene b{display:block;color:#1A1A1A;font-size:16px;}
.ao-corp .ao-scene span{display:block;font-size:15px;color:#4A4238;}
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
.ao-corp .ao-kv{margin:0 0 14px;}
.ao-corp .ao-kv img{display:block;width:100%;height:auto;aspect-ratio:4/1;object-fit:cover;object-position:center;}
@media(max-width:600px){.ao-corp .ao-cards{grid-template-columns:1fr;}.ao-corp .ao-tabs{height:46px;}.ao-corp .ao-tabs a{flex:0 0 auto;padding:0 14px;font-size:14px;}.ao-corp .ao-kv img{aspect-ratio:3/1;}.ao-corp h2{font-size:21px;}.ao-corp .ao-cta a{width:100%;max-width:300px;}}
</style>'''

# 分頁：按下去只換內容；網址 #hash 同步，方便分享及 FAQ 直達
JS = '''<script>(function(){var r=document.querySelector(".ao-corp");if(!r)return;var n=r.querySelector(".ao-tabs");if(!n)return;var T=[].slice.call(n.querySelectorAll("a")),P=T.map(function(a){return document.getElementById(a.getAttribute("href").slice(1))});if(P.some(function(p){return !p}))return;r.classList.add("js-tabs");n.setAttribute("role","tablist");function show(i,push){T.forEach(function(a,k){var on=k===i;a.classList.toggle("on",on);a.setAttribute("aria-selected",on?"true":"false");P[k].classList.toggle("on",on);});var a=T[i];if(n.scrollWidth>n.clientWidth)n.scrollTo({left:a.offsetLeft-(n.clientWidth-a.offsetWidth)/2,behavior:"smooth"});if(push&&history.replaceState)history.replaceState(null,"","#"+P[i].id);}T.forEach(function(a,i){a.setAttribute("role","tab");P[i].setAttribute("role","tabpanel");a.addEventListener("click",function(e){e.preventDefault();show(i,true);var top=n.getBoundingClientRect().top+window.pageYOffset-120;if(window.pageYOffset>top)window.scrollTo({top:top,behavior:"smooth"});});});function fromHash(){var h=location.hash.slice(1);if(!h)return 0;var el=document.getElementById(h);if(!el)return 0;for(var k=0;k<P.length;k++){if(P[k]===el||P[k].contains(el))return k;}return 0;}var s=fromHash();show(s,false);if(location.hash&&s){setTimeout(function(){var el=document.getElementById(location.hash.slice(1));if(el)el.scrollIntoView({behavior:"smooth"});},150);}window.addEventListener("hashchange",function(){show(fromHash(),false);});})();</script>'''


def build(L):
    o = ['<div class="ao-corp">', CSS, '']
    o.append(L['intro'])
    o.append(f'<p class="ao-kv"><img loading="lazy" decoding="async" src="{P}/wp-content/uploads/2026/03/WhatsApp-Image-2026-03-25-at-3.58.36-PM-scaled.jpeg" alt="{L["img_alt"]}" width="800" height="400" /></p>')
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


# ---------------- 中文 ----------------
ZH_FAQ = [
    ('公司到會價錢是多少？', '按人數、菜式及送貨地區計算。參考價方面，Office Lunch 商務餐盒每位 HK$108 起，會議午餐高級餐盒每位 HK$248 起，Annual Dinner 及公司聚會每位 HK$300 起。'),
    ('公司到會要提前多少日預訂？', '建議盡早預訂，尤其是 12 月至農曆新年的公司活動旺季。所需日數視乎人數及菜式，可先透過 WhatsApp 向客服確認。'),
    ('公司到會有沒有素食選擇？', '有。請在查詢時說明素食人數及要求，例如是否需要全素或走五辛，客服會按要求安排菜單。'),
    ('Annual Dinner 到會大約需要多少預算？', '以每位 HK$300 起計算，100 人的 Annual Dinner 到會預算約 HK$30,000，包括迎賓小食、主菜及甜品。'),
    ('怎樣預訂公司到會？', '可透過 WhatsApp 852-6901-1987、電郵 info@aoaodelivery.com，或填寫網站的到會報價查詢表格。'),
]
ZH = dict(
    intro='<p>Kitchen AO 提供<strong>香港公司到會</strong>服務，按人數及預算為 Office Lunch、會議午餐、Annual Dinner、公司聚會及酒會安排餐單，人數由 10 人至 300 人均可配合，並設全港送貨。</p>',
    img_alt='Kitchen AO 公司到會 Annual Dinner 現場',
    nav_label='公司到會目錄',
    panes=[
        ('overview', '公司到會速覽', f'''
<h2>公司到會速覽：我們承辦哪些企業活動？</h2>
<p>公司到會（又稱企業到會）是由到會公司把食物送到辦公室或活動場地的餐飲服務。Kitchen AO 承辦以下企業活動，每個場景有不同的到會形式：</p>
<ul class="ao-scene">
<li><b>Office Lunch／員工飯盒</b><span>商務餐盒，每人一盒，方便日常員工午餐、培訓及加班膳食。</span></li>
<li><b>Meeting Lunch／會議午餐</b><span>高級餐盒，菜式及包裝較講究，適合客戶會議、董事會議及貴賓接待。</span></li>
<li><b>Annual Dinner／頒獎晚宴</b><span>迎賓小食、熱盤主菜及甜品，適合年會到會及頒獎禮。</span></li>
<li><b>公司聚會／Team Building</b><span>自助餐式到會套餐，適合員工聚會、節日派對及產品發佈。</span></li>
<li><b>酒會／開張／發佈會</b><span>Canapés 及 Finger Food，方便站立形式的酒會及開張活動。</span></li>
</ul>
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
<h3>為甚麼選擇 Kitchen AO 公司到會服務？</h3>
<ul>
<li><strong>按企業需要配搭：</strong>中西菜式均可配搭，並可加入素食及無麩質選擇，照顧不同同事的飲食需要。</li>
<li><strong>人數彈性：</strong>由 10 人部門午餐到 300 人的公司聚會，都可以按人數調整份量。</li>
<li><strong>保溫包裝：</strong>熱盤以保溫包裝送達，方便活動開始時直接上桌。</li>
<li><strong>清晰報價：</strong>提供人數、日期及預算後，客服會提供餐單、價錢及送貨安排。</li>
</ul>'''),
        ('office-lunch', 'Office Lunch', f'''
<h2>Office Lunch 到會及會議午餐</h2>
<p>Office Lunch 到會（午餐到會）適合部門午餐、培訓及會議。日常員工午餐可選商務餐盒，客戶會議及貴賓接待則建議選高級餐盒。</p>
<h3>Office Lunch／員工飯盒：商務餐盒 HK$108 起</h3>
<p>適合 10 至 100 人的員工午餐、培訓及加班膳食，每人一盒，方便分派及按人數訂購。詳情見{a("/product-category/商務活動/commercial-lunch-box/", "商務餐盒")}，另有{a("/product-category/商務活動/staff-meal/", "員工膳食餐盒")}可供選擇。</p>
<h3>Meeting Lunch／會議午餐：高級餐盒 HK$248 起</h3>
<p>適合 10 至 100 人的客戶會議、董事會議及貴賓接待，菜式及包裝較講究，令會議午餐更體面。詳情見{a("/product-category/商務活動/executive-premium-meal-box/", "高級餐盒")}。</p>
<h3>想加熱盤或小食？</h3>
<ul>
<li><strong>熱盤：</strong>{a("/product/m0500-honey-glazed-german-salted-pork-knuckle-1-pcs/", "蜜蜜糖德國鹹豬手")}、{a("/product/p03l-black-truffle-wild-mushroom-and-asparagus-cream-pasta-4-pounds/", "黑松露野菌蘆筍忌廉意粉")}</li>
<li><strong>小食：</strong>{a("/product/a0700-handmade-mini-cheeseburger/", "迷你芝士手打豬肉牛肉漢堡")}、{a("/product/a3400-deep-fried-sesame-shrimp-toast-with-thai-sauce/", "懷舊芝麻蝦滑多士")}、{a("/product/a1500-crispy-seafood-tofu-in-traditional-typhoon-shelter-style/", "避風塘炸海鮮豆腐")}</li>
<li><strong>沙律：</strong>{a("/product/s0300-smoked-salmon-caesar-salad/", "油香煙三文魚凱撒沙律")}</li>
</ul>
<p>想按人數一次過訂購，可參考{a("/product-category/party-set-by-people/", "人數選餐")}。</p>'''),
        ('annual-dinner', 'Annual Dinner', f'''
<h2>Annual Dinner 到會：年會、頒獎晚宴怎樣安排？</h2>
<p>Annual Dinner 到會一般以「迎賓小食、熱盤主菜、甜品」三部分組成，適合 50 至 200 人以上的年會到會及頒獎晚宴，每位 HK$300 起。菜式例子：</p>
<ul>
<li><strong>迎賓小食：</strong>{a("/product/c1201-照燒慢煮雞卷配牛油果蓉-1件/", "照燒慢煮雞卷配牛油果蓉")}、{a("/product/c0701-炙燒帶子芋頭紫椰菜串-1串/", "炙燒帶子芋頭紫椰菜串")}、{a("/product/c0101-一口和牛野菌串-1串/", "一口和牛野菌串")}</li>
<li><strong>主菜：</strong>{a("/product/ms02l-西京燒「富士金襴」威士忌白味噌燒鹿兒島叉燒/", "西京燒威士忌白味噌燒鹿兒島叉燒")}、{a("/product/m0315-homemade-black-truffle-butter-baked-cornish-hen-1-5-chickens/", "自家製黑松露牛油慢焗法國黃油雞")}、{a("/product/ps01l「冩樂」清酒煮蟹皇灸燒左口魚醬油㷛仔飯-4磅/", "清酒煮蟹皇灸燒左口魚醬油煲仔飯")}</li>
<li><strong>甜品：</strong>{a("/product/d01-french-colorful-macarons-10-pieces/", "法式七彩馬卡龍")}、{a("/product/d06-caramel-tart-10個/", "焦糖葡撻")}</li>
</ul>
<p>年會人數較多，建議先確定開席時間及場地是否有地方擺放食物，再安排送達時間。如需要侍應服務，可在查詢時一併提出。</p>'''),
        ('festive', '公司聚會', f'''
<h2>公司聚會及節日活動：聖誕派對、春茗、團年飯</h2>
<p>公司聚會到會以自助餐形式為主，適合 30 至 300 人的 Team Building、產品發佈及節日活動，每位 HK$300 起。12 月至農曆新年是公司活動旺季，聖誕派對、公司團年飯、公司開年飯及春茗到會的查詢較多，建議盡早預訂。</p>
<ul>
<li><strong>自助餐菜式例子：</strong>{a("/product/a1600-japanese-chicken-skin-dumplings-with-crispy-onion-rings/", "日式雞皮餃子配洋蔥圈")}、{a("/product/a3000-braised-abalone-vol-au-vent-with-mushrooms-in-oyster-sauce/", "蠔油鮑汁野菌鮑魚酥")}、{a("/product/a0200-grilled-satay-skewer-pork-and-chicken/", "香烤沙嗲串燒")}</li>
<li><strong>套餐：</strong>{a("/product-category/party/foot-party/", "美食派對 Gourmet 套餐")}，按人數由 5 人至 85 人選擇</li>
<li><strong>聖誕派對：</strong>可參考{a("/blog/christmas-catering-hong-kong/", "聖誕到會推介")}</li>
</ul>'''),
        ('business-event', '酒會開張', f'''
<h2>商務活動及酒會到會：酒會、開張、發佈會</h2>
<p>酒會、開張及發佈會一般以站立形式進行，適合 20 至 200 人以上，Canapés 及 Finger Food 較方便賓客取用，價錢按餐單報價。詳情可參考{a("/business-event/", "商務活動到會")}，或選擇{a("/product-category/商務活動/a-bit-of-cuisines-gourmet-in-a-box/", "舌尖上的餐桌九宮格 Canapés")}及{a("/product-category/商務活動/royal-snackers-box/", "皇家小食盒")}。</p>'''),
        ('price', '價錢及流程', f'''
<h2>公司到會價錢怎樣計算？</h2>
<p>公司到會價錢主要按人數、菜式及送貨地區計算。以下是預算例子：</p>
<div class="ao-tblwrap"><table>
<thead><tr><th>活動類型</th><th>人數</th><th>每位參考價</th><th>總預算例子</th><th>特色</th></tr></thead>
<tbody>
<tr><td>Office Lunch（商務餐盒）</td><td>20 人</td><td>HK$108</td><td>HK$2,160</td><td>每人一盒，方便分派</td></tr>
<tr><td>Meeting Lunch（高級餐盒）</td><td>20 人</td><td>HK$248</td><td>HK$4,960</td><td>適合會議及貴賓接待</td></tr>
<tr><td>Annual Dinner</td><td>80 人</td><td>HK$300</td><td>HK$24,000</td><td>熱盤主菜</td></tr>
<tr><td>Team Building</td><td>50 人</td><td>HK$300</td><td>HK$15,000</td><td>自助餐及小食</td></tr>
</tbody></table></div>
<p class="ao-note">運費按送貨地區計算；單一訂單滿 HK$1,450 全港免運費，詳情見{a("/delivery/", "送貨需知")}。</p>
<h2 id="process">公司到會預訂流程</h2>
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
EN = dict(
    intro='<p>Kitchen AO provides <strong>corporate catering in Hong Kong</strong> for office lunches, meeting lunches, annual dinners, company gatherings and receptions. We plan the menu around your headcount and budget, cater for 10 to 300 guests, and deliver across Hong Kong.</p>',
    img_alt='Kitchen AO corporate catering at a company annual dinner in Hong Kong',
    nav_label='Corporate catering contents',
    panes=[
        ('overview', 'Overview', f'''
<h2>Corporate Catering Hong Kong at a Glance: Which Events Do We Cater?</h2>
<p>Corporate catering is a food service where a catering company delivers meals to your office or event venue. Kitchen AO caters the following company events, each with its own catering format:</p>
<ul class="ao-scene">
<li><b>Office lunch / staff lunch boxes</b><span>Commercial lunch boxes, one per person, for everyday staff lunches, training and overtime meals.</span></li>
<li><b>Meeting lunch</b><span>Executive premium meal boxes with more refined dishes and packaging, for client meetings, board meetings and VIP guests.</span></li>
<li><b>Annual dinner / awards night</b><span>Welcome canapés, hot mains and desserts for annual dinners and award ceremonies.</span></li>
<li><b>Company gathering / team building</b><span>Buffet-style catering sets for staff gatherings, festive parties and product launches.</span></li>
<li><b>Reception / opening / product launch</b><span>Canapés and finger food for standing receptions and grand openings.</span></li>
</ul>
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
<h3>Why Choose Kitchen AO Corporate Catering Services?</h3>
<ul>
<li><strong>Menus built for business:</strong> Mix Chinese and Western dishes, with vegetarian and gluten-free options for colleagues with dietary needs.</li>
<li><strong>Flexible headcount:</strong> From a 10-person department lunch to a company gathering for 300, portions are adjusted to your numbers.</li>
<li><strong>Insulated packaging:</strong> Hot dishes arrive in insulated packaging, ready to serve when your event starts.</li>
<li><strong>Clear quotations:</strong> Share your headcount, date and budget, and our team will send a menu, price and delivery plan.</li>
</ul>'''),
        ('office-lunch', 'Office Lunch', f'''
<h2>Office Lunch Catering and Meeting Lunches</h2>
<p>Office lunch catering, or office catering in Hong Kong, suits department lunches, training sessions and meetings. Choose commercial lunch boxes for everyday staff lunches, and executive meal boxes for client meetings and VIP guests.</p>
<h3>Office Lunch / Staff Lunch Boxes: Commercial Lunch Box from HK$108</h3>
<p>For staff lunches, training and overtime meals of 10 to 100 people. One box per person makes it easy to hand out and order by headcount. See our {a("/product-category/商務活動/commercial-lunch-box/", "Commercial Lunch Box")} range, or the {a("/product-category/商務活動/staff-meal/", "Staff Meal Box")}.</p>
<h3>Meeting Lunch: Executive Premium Meal Box from HK$248</h3>
<p>For client meetings, board meetings and VIP guests of 10 to 100 people, with more refined dishes and packaging for a polished meeting lunch. See our {a("/product-category/商務活動/executive-premium-meal-box/", "Executive Premium Meal Box")}.</p>
<h3>Want to Add Hot Dishes or Snacks?</h3>
<ul>
<li><strong>Hot dishes:</strong> {a("/product/m0500-honey-glazed-german-salted-pork-knuckle-1-pcs/", "Honey Glazed German Pork Knuckle")}, {a("/product/p03l-black-truffle-wild-mushroom-and-asparagus-cream-pasta-4-pounds/", "Black Truffle Wild Mushroom Asparagus Cream Pasta")}</li>
<li><strong>Snacks:</strong> {a("/product/a0700-handmade-mini-cheeseburger/", "Mini Hand-Pattied Cheese Burgers")}, {a("/product/a3400-deep-fried-sesame-shrimp-toast-with-thai-sauce/", "Sesame Shrimp Toast")}, {a("/product/a1500-crispy-seafood-tofu-in-traditional-typhoon-shelter-style/", "Typhoon Shelter Style Crispy Seafood Tofu")}</li>
<li><strong>Salad:</strong> {a("/product/s0300-smoked-salmon-caesar-salad/", "Smoked Salmon Signature Caesar Salad")}</li>
</ul>
<p>To order by headcount in one go, see our {a("/product-category/party-set-by-people/", "party sets by number of guests")}.</p>'''),
        ('annual-dinner', 'Annual Dinner', f'''
<h2>Annual Dinner Catering: Planning Your Company Annual Dinner</h2>
<p>Planning a company annual dinner in Hong Kong? Annual dinner catering usually has three parts: welcome canapés, hot mains and desserts, suitable for annual dinners and award ceremonies of 50 to 200+ guests, from HK$300 per person. Sample dishes:</p>
<ul>
<li><strong>Welcome canapés:</strong> {a("/product/c1201-照燒慢煮雞卷配牛油果蓉-1件/", "Teriyaki Chicken Roll with Avocado")}, {a("/product/c0701-炙燒帶子芋頭紫椰菜串-1串/", "Seared Scallop, Taro &amp; Red Cabbage Skewer")}, {a("/product/c0101-一口和牛野菌串-1串/", "Wagyu &amp; Wild Mushroom Skewer")}</li>
<li><strong>Mains:</strong> {a("/product/ms02l-西京燒「富士金襴」威士忌白味噌燒鹿兒島叉燒/", "Saikyo Miso &amp; Whisky Glazed Kagoshima Char Siu")}, {a("/product/m0315-homemade-black-truffle-butter-baked-cornish-hen-1-5-chickens/", "Slow-roasted French Yellow Spring Chicken with Black Truffle Butter")}, {a("/product/ps01l「冩樂」清酒煮蟹皇灸燒左口魚醬油㷛仔飯-4磅/", "Sharaku Sake-Braised Crab Roe &amp; Seared Flounder Claypot Rice")}</li>
<li><strong>Desserts:</strong> {a("/product/d01-french-colorful-macarons-10-pieces/", "French Rainbow Macarons")}, {a("/product/d06-caramel-tart-10個/", "Caramel Portuguese Tarts")}</li>
</ul>
<p>For a large annual dinner, confirm your dinner start time and whether the venue has space to set up the food before arranging the delivery time. If you need service staff, let us know when you enquire.</p>'''),
        ('festive', 'Gatherings', f'''
<h2>Company Gatherings and Festive Events: Christmas Parties, Spring Dinners and Year-end Dinners</h2>
<p>Company gathering catering is usually buffet style, ideal for team building, product launches and festive events of 30 to 300 guests, from HK$300 per person. December to Chinese New Year is the busiest season for company events, with many enquiries for Christmas parties, year-end dinners and spring dinners, so we recommend booking early.</p>
<ul>
<li><strong>Sample buffet dishes:</strong> {a("/product/a1600-japanese-chicken-skin-dumplings-with-crispy-onion-rings/", "Japanese Chicken Skin Dumplings with Crispy Onion Rings")}, {a("/product/a3000-braised-abalone-vol-au-vent-with-mushrooms-in-oyster-sauce/", "Braised Abalone &amp; Wild Mushroom Puff Pastry")}, {a("/product/a0200-grilled-satay-skewer-pork-and-chicken/", "Grilled Satay Skewers")}</li>
<li><strong>Catering sets:</strong> {a("/product-category/party/foot-party/", "Gourmet party sets")} for 5 to 85 guests</li>
</ul>'''),
        ('business-event', 'Receptions', f'''
<h2>Business Event and Reception Catering: Receptions, Openings and Product Launches</h2>
<p>Receptions, openings and product launches are usually standing events for 20 to 200+ guests, so canapés and finger food are easiest for guests, quoted by menu. See our {a("/business-event/", "event catering")} page, or choose the {a("/product-category/商務活動/a-bit-of-cuisines-gourmet-in-a-box/", "Nine Delights Gourmet Canapés Box")} and {a("/product-category/商務活動/royal-snackers-box/", "Royal Snackers Box")}.</p>'''),
        ('price', 'Prices &amp; Booking', f'''
<h2>How Much Does Corporate Catering Cost in Hong Kong?</h2>
<p>Corporate catering prices depend mainly on headcount, menu and delivery area. Budget examples:</p>
<div class="ao-tblwrap"><table>
<thead><tr><th>Event type</th><th>Guests</th><th>Reference price per person</th><th>Total budget (example)</th><th>Highlights</th></tr></thead>
<tbody>
<tr><td>Office lunch (Commercial Lunch Box)</td><td>20</td><td>HK$108</td><td>HK$2,160</td><td>One box per person, easy to hand out</td></tr>
<tr><td>Meeting lunch (Executive Premium Meal Box)</td><td>20</td><td>HK$248</td><td>HK$4,960</td><td>For meetings and VIP guests</td></tr>
<tr><td>Annual dinner</td><td>80</td><td>HK$300</td><td>HK$24,000</td><td>Hot mains</td></tr>
<tr><td>Team building</td><td>50</td><td>HK$300</td><td>HK$15,000</td><td>Buffet and snacks</td></tr>
</tbody></table></div>
<p class="ao-note">Delivery fees depend on the delivery area. Orders of HK$1,450 or more get free delivery across Hong Kong. See {a("/delivery/", "Delivery Info")} for details.</p>
<h2 id="process">How to Book Corporate Catering</h2>
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
