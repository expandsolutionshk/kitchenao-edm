# -*- coding: utf-8 -*-
"""/catering/ 到會場景：簡單場景分類（2026-11-21）"""
from pathlib import Path
H = Path(__file__).parent
S = 'https://aoaodelivery.com'
def b(z, e): return f'<span class="ao-zh" data-no-translation>{z}</span><span class="ao-en" data-no-translation>{e}</span>'
def L(p): return S + p
SCENES = [
 ('CHRISTMAS 2026', '聖誕到會', 'Christmas Catering', '5 至 100 人聖誕套餐，12 月 12 日至 27 日供應', 'Sets for 5 to 100 guests, 12 to 27 Dec', '/catering/christmas/', 1),
 ('BIRTHDAY', '生日派對', 'Birthday Parties', '美食派對套餐：熱盤主菜、小食及甜品', 'Gourmet party sets with mains, snacks and desserts', '/product-category/party/foot-party/', 0),
 ('KIDS', '兒童派對', 'Kids Parties', '兒童餐及派對小食，5 人起', 'Kids meals and party snacks, from 5 guests', '/product-category/party/children/', 0),
 ('CORPORATE', '公司活動', 'Corporate Events', '年會、團年飯及員工聚餐', 'Annual dinners and staff gatherings', '/corporate-catering-hk/', 0),
 ('RECEPTION', '酒會及開張', 'Receptions & Openings', 'Canapés、手指食物及會議茶點', 'Canapés, finger food and meeting refreshments', '/business-event/', 0),
 ('OFFICE LUNCH', '商務午餐', 'Office Lunch', '商務餐盒、員工午餐及高級餐盒', 'Business lunch boxes and staff meals', '/product-category/商務活動/commercial-lunch-box/', 0),
 ('JUNK TRIP', '船河派對', 'Junk Trips', '船河套餐及易拿易分享小食', 'Boat party sets and easy-share snacks', '/product-category/party/boat-party-set/', 0),
 ('VEGETARIAN', '素食聚會', 'Vegetarian Gatherings', '素食及蛋奶素套餐', 'Vegetarian and lacto-ovo sets', '/product-category/party/vegetarians-set/', 0),
 ('PICNIC', '野餐', 'Picnics', '野餐盒，一盒搞掂', 'Ready-to-go picnic boxes', '/product-category/party/chill-box/', 0),
]
PPL = [('2 – 6', '小型聚會', 'Small gatherings', '2-6人分享選項'), ('7 – 11', '家庭派對', 'Family parties', '7-11人分享選項'),
       ('12 – 16', '生日派對', 'Birthday parties', '12-16人分享選項'), ('18 – 25', '公司／朋友聚餐', 'Office & friends', '18-25人分享選項'),
       ('30+', '大型活動', 'Large events', '30人以上分享選項'), ('100+', '企業活動', 'Corporate events', '100人以上分享選項')]
CH = '<svg viewBox="0 0 10 10" aria-hidden="true"><path d="M3.5 1.5 7 5l-3.5 3.5"/></svg>'
DL = lambda l: f"window.dataLayer=window.dataLayer||[];dataLayer.push({{event:'cta_click',cta_label:'{l}'}});"
cards = ''.join(
    f'<a class="sc{" xm" if x else ""}" href="{L(u)}" onclick="{DL("hub_scene_" + k.lower().replace(" ", "_"))}"><small>{k}</small><b>{b(z, e)}</b><span>{b(dz, de)}</span><i>{b("查看套餐", "View sets")}{CH}</i></a>'
    for k, z, e, dz, de, u, x in SCENES)
ppl = ''.join(f'<a href="{L("/product-category/party-set-by-people/" + slug + "/")}" onclick="{DL("hub_ppl_" + n.replace(" ", "").replace("–", "_").replace("+", "plus"))}"><b>{n}<small>{b("人", "pax")}</small></b><em>{b(z, e)}</em></a>' for n, z, e, slug in PPL)

BIZ = [('🍱','商務飯盒','Business lunch boxes'),('🤝','Team Building','Team building'),('🥂','酒會 Finger Food 及 Canapé','Finger food & canapés'),
       ('🎀','簡易開張套餐','Opening ceremony sets'),('🎪','Event 活動','Events'),('🏆','Annual Dinner','Annual dinners'),
       ('🍸','Cocktail 服務（Free Flow、Cocktail Bar）','Cocktail service (free flow, bar)'),('🤵','服務生安排','Service staff'),('📝','訂製食譜 Customised Recipe','Customised recipes')]
SERIES = [
 ('🎄','聖誕到會套餐','Christmas Sets','期間限定・12 月 12 日至 27 日','Limited: 12 to 27 Dec','/catering/christmas/','xm','限定','Limited'),
 ('⭐','美食派對 Gourmet Set','Gourmet Set','人氣之選・熱食主菜','Popular, hot mains','/product-category/party/foot-party/','hot','人氣','Popular'),
 ('🥂','輕食宴會 Refreshment','Refreshment Sets','會議茶點・開幕酒會','Meetings and receptions','/product-category/party/refreshment-set/','','',''),
 ('🍖','肉食獸套餐','Meat Monster Sets','上將海港之選','For meat lovers','/product-category/party/meat-monster/','','',''),
 ('🧸','兒童派對套餐','Kids Party Sets','兒童生日派對','Kids birthday parties','/product-category/party/children/','','',''),
 ('💑','雙人套餐','Sets for Two','二人慶祝・紀念日','Celebrations for two','/product-category/party/set-for-two/','','',''),
 ('🥗','「素」味人生','Vegetarian Sets','素食派對套餐','Vegetarian party sets','/product-category/party/vegetarians-set/','','',''),
 ('🚤','船河派對套餐','Junk Trip Sets','碼頭交收・方便分發','Pier delivery, easy to share','/product-category/party/boat-party-set/','','',''),
 ('🧺','Chill 一下野餐盒','Picnic Boxes','野餐・戶外活動','Picnics and outdoors','/product-category/party/chill-box/','','',''),
 ('🍢','手指食物拼盤','Finger Food Platters','Finger Food・Platter','Finger food platters','/product-category/party/platter/','','',''),
 ('🍽️','單品 À la carte','À la carte','小食・主菜・甜品自由配搭','Mix snacks, mains and desserts','/product-category/a-la-carte/','','',''),
 ('🎉','派對用品 Party Supplies','Party Supplies','餐具・食物架・派對配件','Tableware and party accessories','/product-category/party-supplies/','','',''),
]
UP = 'https://aoaodelivery.com/wp-content/uploads/'
TOP = [
 ('AO 12 - 16 人聖誕到會套餐（寶箱牛扒）','12 to 16 pax Christmas Set (Treasure Box Beef)','期間限定・聖誕新菜式','Limited, new Christmas dishes','HK$4,588','/product/12-16pax-christmas-set-treasure-box-beef/',UP+'2026/11/2026-XMAS-IG-11-600x750.jpg','xm'),
 ('AO 12 - 16 人美食派對 Gourmet Set','12 to 16 pax Gourmet Set','人氣之選・熱食主菜','Popular, hot mains','HK$2,988','/product/ao-12-16pax-gourmet-set/',UP+'2026/03/12-16_101-X-KITCHENAO-03-03-03-03-600x600.jpg',''),
 ('派對大快樂兒童餐（5 人起）','Kids Party Meal (from 5 pax)','兒童生日派對・自選人數','Kids parties, choose headcount','HK$600 起','/product/party-big-happy-kids-meal-select-the-number-of-people-5-people-or-more/',UP+'2023/10/202308-KIDS-thumbnail_工作區域-1-600x600.jpg',''),
 ('AO 18 - 22 人輕食宴會套餐 Refreshment','18 to 22 pax Refreshment Set','會議茶點・開幕酒會','Meetings and receptions','HK$3,488','/product/ao-18-22pax-refreshment-set/',UP+'2023/11/refreshmentparty-04-600x600.jpg',''),
 ('AO 36 - 40 人狂歡派對船河套餐','36 to 40 pax Junk Trip Party Set','Boat Party Set・碼頭交收','Pier delivery','HK$6,332','/product/ao-36-40pax-狂歡派對船河套餐-boat-party-set/',UP+'2025/04/WhatsApp-Image-2025-04-12-at-4.08.26-PM-600x600.jpeg',''),
]
WA_BIZ = 'https://wa.me/85269011987?text=%E4%BC%81%E6%A5%AD%E5%8F%8A%E5%95%86%E5%8B%99%E5%88%B0%E6%9C%83%E6%9C%8D%E5%8B%99%E6%9F%A5%E8%A9%A2'
def sid(u): return u.strip('/').split('/')[-1][:24]
biz = ''.join(f'<li><span class="ic">{i}</span>{b(z,e)}</li>' for i,z,e in BIZ)
ser = ''.join(f'<a class="se{(" "+c) if c else ""}" href="{L(u)}" onclick="{DL("hub_series_"+sid(u))}"><i>{ic}</i><span><b>{b(z,e)}</b><small>{b(dz,de)}</small></span>' + (f'<em>{b(tz,te)}</em>' if tz else '') + '</a>' for ic,z,e,dz,de,u,c,tz,te in SERIES)
top = ''.join(f'<a class="tp{(" "+c) if c else ""}" href="{L(u)}" onclick="{DL("hub_top"+str(n+1))}"><span class="ph"><img src="{img}" alt="{z}" width="600" height="600" loading="lazy" decoding="async"><small>TOP {n+1}</small></span><span class="tx"><b>{b(z,e)}</b><small>{b(dz,de)}</small><strong>{pr}</strong><i>{b("查看詳情","View details")}{CH}</i></span></a>' for n,(z,e,dz,de,pr,u,img,c) in enumerate(TOP))

WA_ZH = 'https://wa.me/85269011987?text=%E4%BD%A0%E5%A5%BD%EF%BC%8C%E6%88%91%E6%83%B3%E6%9F%A5%E8%A9%A2%E5%88%B0%E6%9C%83%E5%A5%97%E9%A4%90'
WA_EN = 'https://wa.me/85269011987?text=Hi%2C%20I%20would%20like%20to%20ask%20about%20catering%20sets'
HTML = f'''<section class="ao-hub">
<div class="hd"><small>KITCHEN AO CATERING</small><h2>{b("按場合揀選到會套餐", "Choose Catering by Occasion")}</h2><p>{b("先揀活動場合，再按人數及預算選擇合適套餐，網上即可下單。", "Pick your occasion, then choose a set by headcount and budget, and order online.")}</p></div>
<div class="grid">{cards}</div>
<div class="hd hd2"><small>01 ・ BY GUESTS</small><h2>{b("按人數選擇", "Choose by Headcount")}</h2></div>
<div class="ppl">{ppl}</div>
<details class="biz"><summary><span class="bi">💼</span><span class="bt">{b("商務到會 TIPS", "Business Catering Tips")}</span><span class="bs">{b("企業及商務到會服務", "Corporate catering services")}</span><span class="car" aria-hidden="true"></span></summary>
<div class="bp"><div class="bh"><small>FOR BUSINESS</small><b>{b("企業及商務到會服務", "Corporate & Business Catering")}</b></div><ul>{biz}</ul>
<div class="bb"><a class="bw ao-zh" data-no-translation href="{WA_BIZ}" target="_blank" rel="noopener" onclick="{DL('hub_biz_whatsapp')}">WhatsApp 聯絡企業客戶專員</a><a class="bw ao-en" data-no-translation href="{WA_BIZ}" target="_blank" rel="noopener" onclick="{DL('hub_biz_whatsapp')}">WhatsApp Our Corporate Team</a><a class="bm" href="{L('/business-event/')}" onclick="{DL('hub_biz_intro')}">{b("商務活動簡介", "Business Events")}</a></div>
<p class="wow"><img src="https://aoaodelivery.com/wp-content/uploads/2023/08/kitchenAO_logo-1.png" alt="Kitchen AO" width="97" height="60" loading="lazy">We Serve, We WOW</p></div></details>
<div class="hd hd2"><small>02 ・ OUR MENU</small><h2>{b("按系列選擇", "Choose by Series")}</h2></div>
<div class="ser">{ser}</div>
<div class="hd hd2"><small>03 ・ CHEF'S PICKS</small><h2>{b("本週 TOP 5 人氣推介", "This Week's Top 5")}</h2></div>
<div class="top">{top}</div>
<div class="cta"><p>{b("仍未決定選擇哪一款？告訴我們人數及場合，專人為你配搭餐單。", "Not sure which set? Tell us your headcount and occasion and we will tailor a menu.")}</p>
<a class="wa ao-zh" data-no-translation href="{WA_ZH}" target="_blank" rel="noopener" onclick="{DL('hub_whatsapp')}">WhatsApp 查詢</a><a class="wa ao-en" data-no-translation href="{WA_EN}" target="_blank" rel="noopener" onclick="{DL('hub_whatsapp')}">WhatsApp Us</a>
<a class="qt" href="{L('/catering-quote-enquiry/')}" onclick="{DL('hub_quote')}">{b("專人活動報價查詢", "Get an Event Quote")}</a></div>
</section>
<style>
html[lang^="en"] .ao-hub .ao-zh{{display:none!important}}html:not([lang^="en"]) .ao-hub .ao-en{{display:none!important}}
.ao-hub{{max-width:1180px;margin:0 auto;padding:40px 20px 56px;box-sizing:border-box;color:#1d1714;font-family:inherit}}
.ao-hub *{{box-sizing:border-box}}.ao-hub a{{text-decoration:none!important}}
.ao-hub .hd{{text-align:center;margin:0 0 26px}}.ao-hub .hd2{{margin:52px 0 20px}}
.ao-hub .hd small{{display:block;font-size:11px;letter-spacing:.3em;color:#9A7B2E;margin:0 0 8px}}
.ao-hub .hd h2{{margin:0 0 8px!important;font-family:"Songti TC","Noto Serif TC",serif;font-size:30px;font-weight:600;letter-spacing:.06em;line-height:1.35;color:#1d1714}}
html[lang^="en"] .ao-hub .hd h2{{font-family:Baskerville,"Baskerville Old Face",Georgia,serif;letter-spacing:.01em}}
.ao-hub .hd p{{margin:0 auto!important;max-width:620px;font-size:15px;line-height:1.8;color:#6b625a}}
.ao-hub .grid{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}}
.ao-hub .sc{{position:relative;display:flex;flex-direction:column;min-height:168px;padding:22px 22px 18px;background:#fff;border:1px solid #E6DDCB;border-radius:4px;color:#1d1714!important;transition:border-color .25s,box-shadow .25s,transform .25s}}
.ao-hub .sc:hover{{border-color:#C8A24A;box-shadow:0 12px 26px -16px rgba(40,24,15,.35);transform:translateY(-2px)}}
.ao-hub .sc small{{font-size:10.5px;letter-spacing:.28em;color:#9A7B2E;margin:0 0 10px}}
.ao-hub .sc b{{font-family:"Songti TC","Noto Serif TC",serif;font-size:22px;font-weight:600;letter-spacing:.06em;line-height:1.3;margin:0 0 6px}}
html[lang^="en"] .ao-hub .sc b{{font-family:Baskerville,"Baskerville Old Face",Georgia,serif;font-weight:500;letter-spacing:0}}
.ao-hub .sc span{{font-size:13.5px;line-height:1.7;color:#6b625a;flex:1}}
.ao-hub .sc i{{display:inline-flex;align-items:center;gap:6px;margin-top:14px;font-style:normal;font-size:12.5px;letter-spacing:.14em;color:#1d1714;border-bottom:1px solid #C8A24A;padding-bottom:3px;align-self:flex-start}}
.ao-hub .sc i svg{{width:9px;height:9px;fill:none;stroke:currentColor;stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round;transition:transform .25s}}.ao-hub .sc:hover i svg{{transform:translateX(3px)}}
.ao-hub .sc.xm{{background:#1d1714;border-color:#1d1714;box-shadow:inset 0 0 0 5px #1d1714,inset 0 0 0 6px rgba(200,162,74,.7)}}
.ao-hub .sc.xm small{{color:#C8A24A}}.ao-hub .sc.xm b{{color:#F3E3B8}}.ao-hub .sc.xm span{{color:#d8cfbf}}.ao-hub .sc.xm i{{color:#E4C77E}}
.ao-hub .ppl{{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:12px}}
.ao-hub .ppl a{{display:flex;flex-direction:column;align-items:center;gap:4px;padding:16px 8px;background:#fbf8f3;border:1px solid #E6DDCB;border-radius:4px;color:#1d1714!important;transition:border-color .25s,background .25s}}
.ao-hub .ppl a:hover{{border-color:#1d1714;background:#fff}}
.ao-hub .ppl b{{font-family:Baskerville,Georgia,serif;font-size:24px;font-weight:500;line-height:1.1}}.ao-hub .ppl b small{{font-family:inherit;font-size:12px;margin-left:3px;color:#9A7B2E}}
.ao-hub .ppl em{{font-style:normal;font-size:12.5px;color:#6b625a;text-align:center}}
.ao-hub .cta{{margin:44px auto 0;max-width:760px;padding:24px;text-align:center;border-top:1px solid #E6DDCB;border-bottom:1px solid #E6DDCB}}
.ao-hub .cta p{{margin:0 0 16px!important;font-size:15px;color:#3a332d}}
.ao-hub .cta a{{display:inline-flex;align-items:center;justify-content:center;min-height:48px;padding:0 26px;margin:4px 6px;font-size:13px;letter-spacing:.18em;color:#fff!important;background:#1d1714;border:1px solid #1d1714}}
.ao-hub .cta a:hover{{background:#000;color:#E4C77E!important}}.ao-hub .cta a.qt{{background:transparent;color:#1d1714!important}}.ao-hub .cta a.qt:hover{{background:#1d1714;color:#fff!important}}
.ao-hub .biz{{margin:22px auto 0;max-width:900px;border:1px solid #1d1714;background:#fff}}
.ao-hub .biz summary{{list-style:none;display:flex;align-items:center;gap:12px;padding:16px 20px;cursor:pointer;background:#1d1714;color:#F3E3B8}}
.ao-hub .biz summary::-webkit-details-marker{{display:none}}
.ao-hub .biz .bi{{font-size:18px}}.ao-hub .biz .bt{{font-size:15px;font-weight:600;letter-spacing:.12em}}.ao-hub .biz .bs{{font-size:12.5px;color:#cdbf9f;letter-spacing:.06em}}
.ao-hub .biz .car{{margin-left:auto;width:9px;height:9px;border-right:1.5px solid #E4C77E;border-bottom:1.5px solid #E4C77E;transform:rotate(45deg);transition:transform .25s}}
.ao-hub .biz[open] .car{{transform:rotate(-135deg)}}
.ao-hub .bp{{padding:22px 24px 18px}}.ao-hub .bh{{text-align:center;margin:0 0 16px}}.ao-hub .bh small{{display:block;font-size:10.5px;letter-spacing:.3em;color:#9A7B2E}}.ao-hub .bh b{{font-family:"Songti TC","Noto Serif TC",serif;font-size:20px;font-weight:600;letter-spacing:.06em}}
.ao-hub .bp ul{{list-style:none!important;margin:0!important;padding:0!important;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px 18px}}
.ao-hub .bp li{{display:flex;align-items:center;gap:8px;margin:0!important;padding:9px 0;border-bottom:1px solid #EFE8DA;font-size:13.5px;line-height:1.4;color:#3a332d}}.ao-hub .bp li .ic{{flex:0 0 auto;font-size:15px}}
.ao-hub .bb{{display:flex;justify-content:center;flex-wrap:wrap;gap:10px;margin:18px 0 0}}
.ao-hub .bb a{{display:inline-flex;align-items:center;justify-content:center;min-height:44px;padding:0 22px;font-size:13px;letter-spacing:.14em;border:1px solid #1d1714}}
.ao-hub .bb .bw{{background:#1d1714;color:#fff!important}}.ao-hub .bb .bm{{color:#1d1714!important}}.ao-hub .bb a:hover{{background:#000;color:#E4C77E!important}}
.ao-hub .wow{{display:flex;align-items:center;justify-content:center;gap:10px;margin:16px 0 0!important;font-family:Baskerville,Georgia,serif;font-style:italic;font-size:14px;color:#9A7B2E}}.ao-hub .wow img{{width:auto;height:30px}}
.ao-hub .ser{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}}
.ao-hub .se{{display:flex;align-items:center;gap:12px;padding:14px 16px;background:#fff;border:1px solid #E6DDCB;border-radius:4px;color:#1d1714!important;transition:border-color .25s,box-shadow .25s}}
.ao-hub .se:hover{{border-color:#C8A24A;box-shadow:0 10px 22px -16px rgba(40,24,15,.35)}}
.ao-hub .se i{{flex:0 0 40px;height:40px;display:flex;align-items:center;justify-content:center;border-radius:50%;background:#F6F0E4;font-style:normal;font-size:18px}}
.ao-hub .se > span{{display:flex;flex-direction:column;min-width:0;flex:1}}.ao-hub .se b{{font-size:14.5px;font-weight:600;line-height:1.35}}.ao-hub .se small{{font-size:12px;color:#7a7066;line-height:1.4;margin-top:2px}}
.ao-hub .se em{{flex:0 0 auto;padding:3px 9px;font-style:normal;font-size:10.5px;letter-spacing:.1em;border:1px solid #C8A24A;color:#9A7B2E}}
.ao-hub .se.xm{{background:#1d1714;border-color:#1d1714}}.ao-hub .se.xm i{{background:rgba(200,162,74,.18)}}.ao-hub .se.xm b{{color:#F3E3B8}}.ao-hub .se.xm small{{color:#cdbf9f}}.ao-hub .se.xm em{{color:#E4C77E}}
.ao-hub .top{{display:grid;grid-auto-flow:column;grid-auto-columns:calc((100% - 64px) / 5);gap:16px;overflow-x:auto;scroll-snap-type:x mandatory;padding:0 0 10px;-webkit-overflow-scrolling:touch}}
.ao-hub .tp{{scroll-snap-align:start;display:flex;flex-direction:column;background:#fff;border:1px solid #E6DDCB;border-radius:4px;overflow:hidden;color:#1d1714!important;transition:border-color .25s,box-shadow .25s}}
.ao-hub .tp:hover{{border-color:#C8A24A;box-shadow:0 12px 26px -16px rgba(40,24,15,.35)}}
.ao-hub .tp .ph{{position:relative;display:block;aspect-ratio:1/1;overflow:hidden;background:#f3eee6}}.ao-hub .tp img{{width:100%;height:100%;object-fit:cover;display:block;transition:transform .5s}}.ao-hub .tp:hover img{{transform:scale(1.04)}}
.ao-hub .tp .ph small{{position:absolute;left:10px;top:10px;padding:4px 9px;font-size:10.5px;letter-spacing:.18em;background:#1d1714;color:#E4C77E}}
.ao-hub .tp .tx{{display:flex;flex-direction:column;gap:4px;padding:14px 14px 16px;flex:1}}.ao-hub .tp b{{font-size:14px;font-weight:600;line-height:1.45}}.ao-hub .tp .tx > small{{font-size:12px;color:#7a7066}}
.ao-hub .tp strong{{margin-top:auto;padding-top:8px;font-family:Baskerville,Georgia,serif;font-size:18px;font-weight:500;color:#1d1714}}
.ao-hub .tp i{{display:inline-flex;align-items:center;gap:6px;margin-top:8px;font-style:normal;font-size:12px;letter-spacing:.14em;border-bottom:1px solid #C8A24A;padding-bottom:3px;align-self:flex-start}}.ao-hub .tp i svg{{width:9px;height:9px;fill:none;stroke:currentColor;stroke-width:1.6}}
.ao-hub .tp.xm .ph small{{background:#7a1f1f;color:#F3E3B8}}
@media(max-width:960px){{.ao-hub .ser{{grid-template-columns:repeat(2,minmax(0,1fr))}}.ao-hub .bp ul{{grid-template-columns:repeat(2,minmax(0,1fr))}}.ao-hub .top{{grid-auto-columns:40%}}}}
@media(max-width:640px){{.ao-hub .ser{{grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}}.ao-hub .se{{position:relative;flex-direction:column;align-items:flex-start;gap:8px;padding:12px 10px}}.ao-hub .se i{{flex:0 0 32px;width:32px;height:32px;font-size:15px}}.ao-hub .se b{{font-size:13px}}.ao-hub .se small{{font-size:11px}}.ao-hub .se em{{position:absolute;top:10px;right:8px;font-size:9.5px;padding:2px 6px}}.ao-hub .bp{{padding:18px 14px 14px}}.ao-hub .bp ul{{grid-template-columns:1fr}}.ao-hub .bp li{{padding:7px 0;font-size:13px}}.ao-hub .biz .bs{{display:none}}.ao-hub .top{{grid-auto-columns:68%;gap:10px}}.ao-hub .bb a{{flex:1 1 100%}}}}
@media(max-width:960px){{.ao-hub .grid{{grid-template-columns:repeat(2,minmax(0,1fr))}}.ao-hub .ppl{{grid-template-columns:repeat(3,minmax(0,1fr))}}}}
@media(max-width:640px){{.ao-hub{{padding:28px 14px 44px}}.ao-hub .hd h2{{font-size:24px}}.ao-hub .grid{{gap:10px}}.ao-hub .sc{{min-height:0;padding:16px 14px 14px}}.ao-hub .sc b{{font-size:18px}}.ao-hub .sc span{{font-size:12.5px}}.ao-hub .sc small{{font-size:9.5px;letter-spacing:.2em}}.ao-hub .sc.xm{{grid-column:1/-1}}.ao-hub .ppl{{gap:8px}}.ao-hub .ppl b{{font-size:20px}}.ao-hub .cta a{{display:flex;margin:8px 0}}}}
</style>
'''
assert '→' not in HTML
(H / 'catering-hub-rawhtml.html').write_text(HTML, encoding='utf-8')
for lang, fn in (('zh-HK', 'catering-hub-preview.html'), ('en', 'catering-hub-preview-en.html')):
    (H / fn).write_text(f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>body{{margin:0;font-family:-apple-system,"PingFang HK",sans-serif;background:#fff}}</style></head><body>{HTML}</body></html>', encoding='utf-8')
print('ok')
