# -*- coding: utf-8 -*-
"""/catering/ v5（2026-11-21）：參考外賣平台版面，左邊篩選（場合／人數／類型），右邊結果。CSS :has() 篩選，無 script。"""
import sys; from pathlib import Path
H = Path(__file__).parent; sys.path.insert(0, str(H))
import build_catering_hub_v4 as W
V = W.V; S, TB, b = V.S, V.TB, V.b
U = S + '/wp-content/uploads/'
OCC = [('xmas','聖誕到會','Christmas','2026/11/20_26xmas-chick-5-6-600x600.jpg'),('bday','生日派對','Birthdays','2026/03/5-6_101-X-KITCHENAO-03-03-600x600.jpg'),
 ('kids','兒童派對','Kids Parties','2023/10/202308-KIDS-thumbnail-02-600x600.jpg'),('corp','公司活動','Corporate','2025/05/PHOTO-2025-03-14-16-33-30-2-600x800.jpeg'),
 ('recep','酒會及開張','Receptions','2025/04/WhatsApp-Image-2026-10-19-at-11.37.40-AM-600x600.jpeg'),('lunch','商務午餐','Office Lunch','2025/04/CAB-Commercial-Meal-Lv2_頁面_1-1-724x1024-1-600x600.jpg'),
 ('boat','船河派對','Junk Trips','2025/04/WhatsApp-Image-2025-04-12-at-4.08.26-PM-600x600.jpeg'),('veg','素食聚會','Vegetarian','2025/05/9ee996d5-e50c-4745-b847-86d8e179c481-600x600.jpg'),
 ('picnic','野餐及戶外','Picnics','2025/04/WhatsApp-Image-2025-04-12-at-4.08.18-PM-600x600.jpeg')]
PAX = [('p1','2–6 人','2–6 pax',2,6),('p2','7–11 人','7–11 pax',7,11),('p3','12–16 人','12–16 pax',12,16),('p4','18–25 人','18–25 pax',17,25),('p5','30 人以上','30+ pax',26,89),('p6','100 人以上','100+ pax',90,999)]
TYP = [('party','派對到會套餐','Party Sets'),('biz','商務餐盒及小食','Business Boxes'),('season','季節限定','Seasonal')]
C = '/product-category/'
SER = [  # key, zh, en, url, img, min price, pax ranges, pax label, occasions, type, price note
 ('xmas','聖誕派對到會套餐','Christmas Party Sets',C+'christmas-party-catering-set/','2026/11/20_26xmas-chick-5-6-600x600.jpg',1688,[(5,100)],('5–100 人','5–100 pax'),'xmas corp bday','season'),
 ('gourmet','美食派對 Gourmet Set','Gourmet Set',C+'party/foot-party/','2026/03/5-6_101-X-KITCHENAO-03-03-600x600.jpg',1388,[(5,85)],('5–85 人','5–85 pax'),'bday corp kids','party'),
 ('refresh','輕食宴會 Refreshment','Refreshment Set',C+'party/refreshment-set/','2023/11/refreshmentparty-03-600x600.jpg',2688,[(12,40)],('12–40 人','12–40 pax'),'corp recep','party'),
 ('meat','肉食獸套餐','Meat Lovers Set',C+'party/meat-monster/','2025/04/WhatsApp-Image-2025-04-14-at-6.13.46-PM-600x600.jpeg',1888,[(7,16)],('7–16 人','7–16 pax'),'bday corp','party'),
 ('kids','兒童派對套餐','Kids Party Sets',C+'party/children/','2023/10/202308-KIDS-thumbnail-02-600x600.jpg',500,[(5,999)],('5 人起','From 5 pax'),'kids bday','party'),
 ('couple','雙人套餐','Sets for Two',C+'party/set-for-two/','2023/10/202308-2pax-thumbnail_工作區域-1-600x600.jpg',438,[(2,2)],('2 人','2 pax'),'bday picnic','party'),
 ('veg','「素」味人生','Veggie Delight',C+'party/vegetarians-set/','2025/05/9ee996d5-e50c-4745-b847-86d8e179c481-600x600.jpg',1388,[(6,26)],('6–26 人','6–26 pax'),'veg corp bday','party'),
 ('boat','船河派對套餐','Boat Party Sets',C+'party/boat-party-set/','2025/04/WhatsApp-Image-2025-04-12-at-4.08.26-PM-600x600.jpeg',3358,[(15,40)],('15–40 人','15–40 pax'),'boat','party'),
 ('chill','Chill 一下野餐盒','Chill Picnic Box',C+'party/chill-box/','2025/04/WhatsApp-Image-2025-04-12-at-4.08.18-PM-600x600.jpeg',258,[(2,6)],('2–6 人','2–6 pax'),'picnic boat','party'),
 ('platter','手指食物拼盤','Finger Food Platter',C+'party/platter/','2023/10/KitchenAO_platter_thumbnail_工作區域-1-600x600-1.png',498,[(5,5)],('5 人','5 pax'),'recep bday boat','party'),
 ('lunchbox','商務餐盒','Business Lunch Box',C+'商務活動/commercial-lunch-box/','2025/04/CAB-Commercial-Meal-Lv2_頁面_1-1-724x1024-1-600x600.jpg',108,[(1,999)],('按份訂購','Per box'),'lunch corp','biz'),
 ('staff','員工膳食餐盒','Staff Meal Box',C+'商務活動/staff-meal/','2024/07/SM-Staff-Meal-Lv1-600x600.jpg',79,[(1,999)],('按份訂購','Per box'),'lunch corp','biz'),
 ('exec','高級餐盒 Executive','Executive Meal Box',C+'商務活動/executive-premium-meal-box/','2025/04/螢幕截圖-2026-10-17-下午5.20.52-593x600.png',248,[(1,999)],('按份訂購','Per box'),'lunch corp','biz'),
 ('snack','皇家小食盒','Royal Snackers Box',C+'商務活動/royal-snackers-box/','2025/04/Royal-Snacks-Box-600x600.jpg',150,[(1,999)],('按份訂購','Per box'),'recep corp','biz'),
 ('canape','九宮格 Canapé 盒','Canapé Gourmet Box',C+'商務活動/a-bit-of-cuisines-gourmet-in-a-box/','2025/04/WhatsApp-Image-2026-10-19-at-11.37.40-AM-600x600.jpeg',278,[(1,999)],('按份訂購','Per box'),'recep corp','biz'),
]
def paxcls(rs):
    return ' '.join(k for k, z, e, lo, hi in PAX if any(a <= hi and c >= lo for a, c in rs))
def radio(g, v, z, e, checked=False):
    return f'<label class="fr"><input type="radio" name="aof{g}" id="f-{g}-{v}"{" checked" if checked else ""}><span>{b(z, e)}</span></label>'
side = (f'<div class="fg"><h3>{b("活動場合","Occasion")}</h3>{radio("o","all","全部","All",True)}' + ''.join(radio('o', k, z, e) for k, z, e, _ in OCC) + '</div>'
        f'<div class="fg"><h3>{b("人數","Guests")}</h3>{radio("p","all","全部","All",True)}' + ''.join(radio('p', k, z, e) for k, z, e, *_ in PAX) + '</div>'
        f'<div class="fg"><h3>{b("類型","Type")}</h3>{radio("t","all","全部","All",True)}' + ''.join(radio('t', k, z, e) for k, z, e in TYP) + '</div>')
tiles = ''.join(f'<label class="tl" for="f-o-{k}"><span class="ti"><img src="{U}{img}" alt="" width="120" height="120" loading="lazy" decoding="async"></span><b>{b(z, e)}</b></label>' for k, z, e, img in OCC)
cards = ''
for k, z, e, u, img, mn, rs, pl, oc, ty in SER:
    cls = f'sc {ty} ' + ' '.join('o-' + o for o in oc.split()) + ' ' + paxcls(rs)
    note = b(f'每份 HK${mn:,} 起', f'From HK${mn:,} / box') if ty == 'biz' else b(f'HK${mn:,} 起', f'From HK${mn:,}')
    flag = f'<mark>{b("季節限定","Seasonal")}</mark>' if ty == 'season' else ('<mark>' + b('人氣','Popular') + '</mark>' if k == 'gourmet' else '')
    cards += (f'<a class="{cls}" href="{S}{u}"{TB} data-ga="hub_card_{k}"><span class="im"><img src="{U}{img}" alt="{z}" width="600" height="600" loading="lazy" decoding="async">{flag}</span>'
              f'<span class="tx"><b>{b(z, e)}</b><span class="mt"><i>{b(*pl)}</i><em>{note}</em></span></span></a>')
xc = W.xc(f'{S}/catering/christmas/', 'hub_xmas_banner', ('聖誕到會 2026', 'Christmas Catering 2026'), ('5 至 100 人・12 月 12 至 27 日供應', '5 to 100 pax・12 to 27 Dec'))

HTML = f'''<section class="aob aov5" aria-labelledby="aob-title">
<div class="hd"><p class="ey">KITCHEN AO CATERING</p><h2 id="aob-title">{b("按場合揀選到會套餐","Choose Catering by Occasion")}</h2><p class="sb">{b("先揀活動場合，再按人數及預算選擇合適套餐，網上即可下單。","Pick your occasion, then choose a set by headcount and budget, and order online.")}</p></div>
<div class="lay">
<aside class="side" aria-label="篩選"><p class="st">{b("篩選","Filters")}</p>{side}</aside>
<div class="main">
<div class="xcw">{xc}</div>
<h3 class="h">{b("你想辦咩活動？","What are you planning?")}</h3>
<div class="tls">{tiles}</div>
<div class="rh"><h3 class="h">{b("到會套餐系列","Catering Sets")}</h3></div>
<div class="grid">{cards}<p class="cnt">{b("個系列符合篩選","sets match")}</p><a class="none" href="{V.WA}" target="_blank" rel="noopener">{b("搵唔到合適套餐？WhatsApp 專人為你度身配搭","Can&#8217;t find a fit? WhatsApp us for a tailored menu")}</a></div>
{W.biz("v5")}
<div class="tp"><div class="th"><span>{b("本週 TOP 5 人氣推介","This Week&#8217;s Top 5")}</span><small>CHEF&#8217;S PICKS</small></div><div class="ao-hubx"><div class="ao-qp-pop">{W.top}</div></div></div>
</div></div>
<div class="hp"><p>{b("仍未決定選擇哪一款？","Still deciding?")}</p><a href="{V.WA}" target="_blank" rel="noopener noreferrer" data-ga="hub_whatsapp">{b("WhatsApp 專人為你配搭餐單","WhatsApp us for a tailored menu")}</a></div>
</section>
<style>@@CSS@@</style>
'''
CSS5 = '''
.aov5{max-width:1240px}
.aov5 .hd{padding:44px 24px 48px}
.aov5 .lay{display:grid;grid-template-columns:250px minmax(0,1fr);gap:28px;padding:28px 28px 0;align-items:start}
.aov5 .side{position:sticky;top:130px;padding:22px 20px;background:#fff;border:1px solid var(--ln);border-radius:16px}
.aov5 .side .st{margin:0 0 6px!important;font-size:19px;font-weight:800;color:var(--c)}
.aov5 .fg{padding:14px 0 6px;border-top:1px solid #f0e6d3;margin-top:12px}
.aov5 .fg:first-of-type{border-top:0;margin-top:0}
.aov5 .fg h3{margin:0 0 8px!important;font-size:14px!important;font-weight:800!important;letter-spacing:.06em;color:var(--c)!important;line-height:1.4!important}
.aov5 .fr{display:flex;align-items:center;gap:10px;margin:0!important;padding:6px 0;font-size:14.5px;font-weight:600;color:#3f2f2a;cursor:pointer}
.aov5 .fr input{-webkit-appearance:none;appearance:none;flex:0 0 20px;width:20px!important;height:20px!important;margin:0!important;border:2px solid #b9a88e;border-radius:50%;background:#fff;cursor:pointer;transition:all .2s;position:static!important;opacity:1!important;pointer-events:auto}
.aov5 .fr input:checked{border:6px solid var(--c)}
.aov5 .fr input:focus-visible{outline:2px solid var(--g);outline-offset:2px}
.aov5 .fr:hover span{color:var(--c)}
.aov5 .main{min-width:0}.aov5 .side{min-width:0}.aov5 .xcw{min-width:0;overflow:hidden;border-radius:14px}
.aov5 .xcw{margin:0 0 26px}.aov5 .xcw .xc{min-height:88px!important}
.aov5 .h{margin:0 0 14px!important;font-size:24px!important;font-weight:800!important;color:var(--c)!important;letter-spacing:.02em;line-height:1.3!important}
.aov5 .tls{display:flex;gap:14px;overflow-x:auto;padding:2px 2px 12px;margin:0 0 22px;scrollbar-width:thin}
.aov5 .tl{flex:0 0 96px;display:flex;flex-direction:column;align-items:center;gap:8px;margin:0!important;cursor:pointer}
.aov5 .ti{display:block;width:96px;height:96px;border-radius:16px;overflow:hidden;background:#efe2c4;box-shadow:0 0 0 2px transparent;transition:box-shadow .2s,transform .2s}
.aov5 .ti img{width:100%!important;height:100%!important;object-fit:cover;display:block}
.aov5 .tl b{font-size:13.5px;font-weight:700;color:#61443e;text-align:center;line-height:1.3}
.aov5 .tl:hover .ti{transform:translateY(-2px)}
.aov5 .grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px;counter-reset:aoc}
.aov5 .cnt{grid-column:1/-1;order:-1;margin:-6px 0 0!important;font-size:13.5px;color:var(--mu)}
.aov5 .cnt::before{content:counter(aoc) " ";font-weight:800;color:var(--c)}
html[lang^="en"] .aov5 .cnt::before{content:counter(aoc) " "}
.aov5 .sc{counter-increment:aoc;display:flex;flex-direction:column;background:#fff;border:1px solid var(--ln);border-radius:16px;overflow:hidden;color:var(--c)!important;transition:transform .25s,box-shadow .25s}
.aov5 .sc:hover{transform:translateY(-3px);box-shadow:0 16px 30px -20px rgba(43,27,23,.55)}
.aov5 .im{position:relative;display:block;aspect-ratio:4/3;overflow:hidden;background:#efe2c4}
.aov5 .im img{width:100%!important;height:100%!important;object-fit:cover;display:block;transition:transform .5s}
.aov5 .sc:hover .im img{transform:scale(1.04)}
.aov5 .im mark{position:absolute;left:10px;right:auto;top:10px;padding:3px 10px;border-radius:999px;background:var(--c);color:#f0d39a;font-size:11px;font-weight:800;letter-spacing:.06em}
.aov5 .tx{display:flex;flex-direction:column;gap:6px;padding:12px 14px 14px}
.aov5 .tx b{font-size:16px;font-weight:800;line-height:1.35}
.aov5 .mt{display:flex;align-items:center;gap:8px;flex-wrap:wrap;font-size:13px;color:var(--mu)}
.aov5 .mt i{font-style:normal;padding:2px 8px;border-radius:999px;background:#f3e8d2;color:#61443e;font-weight:700;font-size:12px}
.aov5 .mt em{font-style:normal;font-weight:700;color:var(--c)}
.aov5 .none{grid-column:1/-1;display:block;padding:14px 18px;border:1px dashed #cdb98f;border-radius:14px;text-align:center;font-size:14px;font-weight:700;color:#61443e!important;background:#fffdf8}
.aov5 .none:hover{border-color:var(--c);color:var(--c)!important}
.aov5 .bz{margin:30px 0 0}.aov5 .bw{max-width:none}
.aov5 .tp{margin:46px 0 0}
.aov5 .hp{margin:30px 28px 0}
@media (max-width:1080px){.aov5 .grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:860px){
.aov5 .lay{grid-template-columns:minmax(0,1fr);gap:16px;padding:18px 12px 0}
.aov5 .side{min-width:0;position:static;padding:12px 12px 4px;border-radius:14px}
.aov5 .side .st{display:none}
.aov5 .fg{display:flex;align-items:center;gap:8px;overflow-x:auto;padding:4px 0 10px;margin:0;border:0;scrollbar-width:none}
.aov5 .fg::-webkit-scrollbar{display:none}
.aov5 .fg h3{flex:0 0 auto;margin:0 4px 0 0!important;font-size:12.5px!important}
.aov5 .fr{flex:0 0 auto;padding:6px 12px;border:1px solid var(--ln);border-radius:999px;background:#fffdf8;font-size:13px;gap:0}
.aov5 .fr input{display:none}
.aov5 .fr:has(input:checked){background:var(--c);border-color:var(--c);color:#f0d39a}
.aov5 .h{font-size:19px!important}
.aov5 .tl{flex-basis:76px}.aov5 .ti{width:76px;height:76px;border-radius:14px}.aov5 .tl b{font-size:12px}
.aov5 .grid{gap:10px}.aov5 .tx{padding:10px}.aov5 .tx b{font-size:14px}.aov5 .mt{font-size:12px}
.aov5 .hp{margin:24px 12px 0}
}
'''
rules = []
for k, *_ in OCC:
    rules.append(f'.aov5:has(#f-o-{k}:checked) .sc:not(.o-{k}){{display:none}}')
    rules.append(f'.aov5:has(#f-o-{k}:checked) .tl[for="f-o-{k}"] .ti{{box-shadow:0 0 0 3px var(--g)}}.aov5:has(#f-o-{k}:checked) .tl[for="f-o-{k}"] b{{color:var(--c)}}')
for k, *_ in PAX: rules.append(f'.aov5:has(#f-p-{k}:checked) .sc:not(.{k}){{display:none}}')
for k, *_ in TYP: rules.append(f'.aov5:has(#f-t-{k}:checked) .sc:not(.{k}){{display:none}}')
CSS = W.CSS + CSS5 + '\n'.join(rules)
assert '<' not in CSS
OUT = HTML.replace('@@CSS@@', CSS)
assert '→' not in OUT and '<script' not in OUT
(H / 'catering-hub-v5-rawhtml.html').write_text(OUT, encoding='utf-8')
(H / 'catering-hub-v5-preview.html').write_text(f'<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>body{{margin:0;padding:20px 10px;background:#fff;font-family:-apple-system,"PingFang HK",sans-serif}}</style></head><body>{OUT}</body></html>', encoding='utf-8')
print('ok', len(OUT))
