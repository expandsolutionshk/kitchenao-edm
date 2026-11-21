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
WA_ZH = 'https://wa.me/85269011987?text=%E4%BD%A0%E5%A5%BD%EF%BC%8C%E6%88%91%E6%83%B3%E6%9F%A5%E8%A9%A2%E5%88%B0%E6%9C%83%E5%A5%97%E9%A4%90'
WA_EN = 'https://wa.me/85269011987?text=Hi%2C%20I%20would%20like%20to%20ask%20about%20catering%20sets'
HTML = f'''<section class="ao-hub">
<div class="hd"><small>KITCHEN AO CATERING</small><h2>{b("按場合揀選到會套餐", "Choose Catering by Occasion")}</h2><p>{b("先揀活動場合，再按人數及預算選擇合適套餐，網上即可下單。", "Pick your occasion, then choose a set by headcount and budget, and order online.")}</p></div>
<div class="grid">{cards}</div>
<div class="hd hd2"><small>BY GUESTS</small><h2>{b("按人數選擇", "Choose by Headcount")}</h2></div>
<div class="ppl">{ppl}</div>
<div class="cta"><p>{b("未決定揀哪款？告訴我們人數及場合，專人為你配搭餐單。", "Not sure which set? Tell us your headcount and occasion and we will tailor a menu.")}</p>
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
@media(max-width:960px){{.ao-hub .grid{{grid-template-columns:repeat(2,minmax(0,1fr))}}.ao-hub .ppl{{grid-template-columns:repeat(3,minmax(0,1fr))}}}}
@media(max-width:640px){{.ao-hub{{padding:28px 14px 44px}}.ao-hub .hd h2{{font-size:24px}}.ao-hub .grid{{gap:10px}}.ao-hub .sc{{min-height:0;padding:16px 14px 14px}}.ao-hub .sc b{{font-size:18px}}.ao-hub .sc span{{font-size:12.5px}}.ao-hub .sc small{{font-size:9.5px;letter-spacing:.2em}}.ao-hub .sc.xm{{grid-column:1/-1}}.ao-hub .ppl{{gap:8px}}.ao-hub .ppl b{{font-size:20px}}.ao-hub .cta a{{display:flex;margin:8px 0}}}}
</style>
'''
assert '→' not in HTML
(H / 'catering-hub-rawhtml.html').write_text(HTML, encoding='utf-8')
for lang, fn in (('zh-HK', 'catering-hub-preview.html'), ('en', 'catering-hub-preview-en.html')):
    (H / fn).write_text(f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>body{{margin:0;font-family:-apple-system,"PingFang HK",sans-serif;background:#fff}}</style></head><body>{HTML}</body></html>', encoding='utf-8')
print('ok')
