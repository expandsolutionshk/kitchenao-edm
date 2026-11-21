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
DISH = {  # 精選菜式（取自產品頁自選菜式，2026-11-21）
 'xmas':[('燒南乳香慢煮原隻黃油雞','2026/11/20_26xmas-chicken-1-150x150.jpg'),('煙燻慢煮美國牛翼板肉','2026/11/20_26xmas-beef-box-300x300.jpg'),('芒果粟子蓉冬日酥盒','2026/11/20_26xmas-chestnut-pastry-150x150.jpg')],
 'gourmet':[('香草蜜糖鹿兒島叉燒扒','2026/03/WhatsApp-Image-2026-03-18-at-16.36.27-2-1-150x150.jpeg'),('紅酒慢燴和牛牛肋條','2019/06/Posts-34-600x600-1-150x150.jpg'),('雙色芝士吞拿魚脆法包','2019/06/Posts-06-150x150.jpg')],
 'refresh':[('香草蜜糖鹿兒島叉燒扒','2019/06/Posts-04-150x150.jpg'),('紅酒慢燴和牛牛肋條','2019/06/Posts-34-600x600-1-150x150.jpg'),('香烤沙嗲串燒','2019/06/Posts-10-150x150.jpg')],
 'couple':[('香草蜜糖鹿兒島叉燒扒','2019/06/Posts-04-150x150.jpg'),('蜜蜜燒雞翼配脆薯角','2019/06/Posts-16-150x150.jpg'),('雙色芝士吞拿魚脆法包','2019/06/Posts-06-150x150.jpg')],
 'platter':[('照燒鰻魚蛋沙律牛油酥盒','2019/06/Posts-15-150x150.jpg'),('香烤沙嗲串燒','2019/06/Posts-10-150x150.jpg'),('蜜蜜燒雞翼配脆薯角','2019/06/Posts-16-150x150.jpg')],
 'boat':[('香草蜜糖鹿兒島叉燒扒','2025/04/Posts-04-150x150.jpg'),('椰香咖哩海鮮龍脷柳','2025/04/KitchenAO_DEC2023-ALA-CARTE-03-150x150.jpg'),('日式雞皮餃子配洋蔥圈','2025/04/KitchenAO_MAY2023-ALA-CARTE-03-600x600-1-150x150.png')],
 'staff':[('皇牌番茄豬排飯','2025/04/SM1_Tomato_Pork_Chop_Rice.PNG-150x150.png'),('忌廉汁海鮮意粉','2025/04/SM2_Creamy_Seafood_Pasta-.PNG-150x150.png')],
 'meat':[('黑松露野菌蘆筍忌廉意粉','2019/06/Posts-18-150x150.jpg')],
 'chill':[('迷你芝士手打漢堡','2019/06/Posts-07-150x150.jpg')],
}
ALLD = {}
for _ln in (H / 'dishes.txt').read_text(encoding='utf-8').strip().split('\n'):
    _k, _n, _st, _ext, _c = _ln.split('~')
    _sm = _st + {'1': '-150x150', '0': ''}[_c[0]] + '.' + _ext
    _lg = _st + {'6': '-600x600', '3': '-300x300', '0': ''}[_c[1]] + '.' + _ext
    if _c[0] == '0': _sm = _lg
    ALLD.setdefault(_k, []).append((_n.replace('"', ''), _sm, _lg))
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
    dl = ALLD.get(k, [])
    def th(n, sm, lg):
        return f'<span class="dt"><img src="{U}{sm}" alt="{n}" width="150" height="150" loading="lazy" decoding="async"><span class="dp"><img src="{U}{lg}" alt="" width="300" height="300" loading="lazy" decoding="async"><em>{n}</em></span></span>'
    if dl:
        first = ''.join(th(*x) for x in dl[:6]); rest = ''.join(th(*x) for x in dl[6:])
        more = (f'<details class="dm"><summary>{b(f"查看全部 {len(dl)} 款菜式", f"See all {len(dl)} dishes")}</summary><div class="dg">{rest}</div></details>') if rest else ''
        dh = f'<div class="dw"><small class="dc">{b(f"可揀菜式 {len(dl)} 款", f"{len(dl)} dishes to choose")}</small><div class="dg">{first}</div>{more}</div>'
    else:
        dh = ''
    CART = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 8h14l-1.2 12H6.2z"/><path d="M9 8V6.5a3 3 0 0 1 6 0V8"/><path d="M12 11.5v5M9.5 14h5"/></svg>'
    cards += (f'<div class="{cls}"><a class="im" href="{S}{u}"{TB} data-ga="hub_card_{k}"><img src="{U}{img}" alt="{z}" width="600" height="600" loading="lazy" decoding="async">{flag}<span class="pb">{note}</span></a>'
              f'<div class="tx"><a class="tt" href="{S}{u}"{TB}><b>{b(z, e)}</b></a><span class="mt"><i>{b(*pl)}</i><em>{note}</em></span>{dh}<a class="cta" href="{S}{u}"{TB} data-ga="hub_cta_{k}">{CART}<span>{b("立即選購","Order Now")}</span></a></div></div>')
xc = W.xc(f'{S}/catering/christmas/', 'hub_xmas_banner', ('聖誕到會 2026', 'Christmas Catering 2026'), ('5 至 100 人・12 月 12 至 27 日供應', '5 to 100 pax・12 to 27 Dec'))

HTML = f'''<section class="aob aov5" aria-labelledby="aob-title">
<div class="hd"><p class="ey">KITCHEN AO CATERING</p><h2 id="aob-title">{b("按場合揀選到會套餐","Choose Catering by Occasion")}</h2><p class="sb">{b("先揀活動場合，再按人數及預算選擇合適套餐，網上即可下單。","Pick your occasion, then choose a set by headcount and budget, and order online.")}</p></div>
<ul class="trust"><li>{b("網上即時下單","Order online")}</li><li>{b("全港送貨","Delivery across HK")}</li><li>{b("過千好評","1,000+ reviews")}</li><li>{b("名人及 KOL 推介","Loved by KOLs")}</li></ul>
<div class="lay">
<aside class="side" aria-label="篩選"><p class="st">{b("篩選","Filters")}</p>{side}</aside>
<div class="main">
<div class="xcw">{xc}</div>
<h3 class="h">{b("你想辦咩活動？","What are you planning?")}</h3>
<div class="tls">{tiles}</div>
<div class="rh"><h3 class="h">{b("到會套餐系列","Catering Sets")}</h3></div>
<div class="grid">{cards}<p class="cnt">{b("個系列符合篩選","sets match")}</p><a class="none" href="{V.WA}" target="_blank" rel="noopener">{b("搵唔到合適套餐？WhatsApp 專人為你度身配搭","Can&#8217;t find a fit? WhatsApp us for a tailored menu")}</a></div>
{W.biz("v5")}

</div></div>
<div class="tpw"><div class="tp"><div class="th"><span>{b("本週 TOP 5 人氣推介","This Week&#8217;s Top 5")}</span><small>CHEF&#8217;S PICKS</small></div><div class="ao-hubx"><div class="ao-qp-pop">{W.top}</div></div></div></div>
<div class="hp"><p>{b("仍未決定選擇哪一款？","Still deciding?")}</p><a href="{V.WA}" target="_blank" rel="noopener noreferrer" data-ga="hub_whatsapp">{b("WhatsApp 專人為你配搭餐單","WhatsApp us for a tailored menu")}</a></div>
</section>
<style>@@CSS@@</style>
'''
CSS5 = '''

.aov5 .tpw{padding:0 28px}
.aov5 .tpw .ao-qp-pop{display:grid!important;grid-auto-flow:column;grid-auto-columns:minmax(230px,1fr);grid-template-columns:none!important;gap:16px;overflow-x:auto;scroll-snap-type:x mandatory;padding-bottom:8px}
.aov5 .tpw .ao-hx{scroll-snap-align:start;flex:none!important}
@media (max-width:860px){.aov5 .tpw{padding:0 12px}.aov5 .tpw .ao-qp-pop{grid-auto-columns:72%}}
.aov5.thC .tpw{padding:0 40px}
@media (max-width:860px){.aov5.thC .tpw{padding:0 16px}}


.aov5 .sc{position:relative}
.aov5 .sc .im{position:relative;display:block;overflow:hidden}
.aov5 .tt,.aov5 .sc .im{color:inherit!important;text-decoration:none!important}
.aov5 .dw{margin-top:10px}
.aov5 .dc{display:block;margin:0 0 6px;font-size:12px;color:var(--mu);letter-spacing:.04em}
.aov5 .dg{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:4px}
.aov5 .dt{position:relative;display:block;aspect-ratio:1/1;background:#f3eee6;cursor:zoom-in}
.aov5 .dt>img{width:100%!important;height:100%!important;object-fit:cover;display:block}
.aov5 .dp{display:none;position:absolute;left:50%;bottom:calc(100% + 8px);z-index:40;width:200px;transform:translateX(-50%);background:#fff;border:1px solid var(--ln);box-shadow:0 18px 40px -16px rgba(0,0,0,.45);pointer-events:none}
.aov5 .dp img{width:200px!important;height:200px!important;object-fit:cover;display:block}
.aov5 .dp em{display:block;padding:8px 10px;font-style:normal;font-size:12.5px;line-height:1.5;color:#2b211b;text-align:center}
@media (hover:hover){.aov5 .dt:hover .dp{display:block}.aov5 .dt:hover{outline:1px solid var(--g);outline-offset:1px}}
.aov5 .dg .dt:nth-child(6n+1) .dp{left:0;transform:none}.aov5 .dg .dt:nth-child(6n) .dp{left:auto;right:0;transform:none}
.aov5 .dm{margin-top:4px}
.aov5 .dm summary{list-style:none;cursor:pointer;padding:6px 0 2px;font-size:12px;color:var(--mu);text-decoration:underline;text-underline-offset:3px}
.aov5 .dm summary::-webkit-details-marker{display:none}
.aov5 .dm[open] summary{display:none}
.aov5 .dm .dg{margin-top:4px}
.aov5 .cta svg{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round;flex:0 0 auto}

.aov5 .dh{display:flex;gap:6px;margin-top:6px}.aov5 .dh img{width:44px!important;height:44px!important;object-fit:cover;display:block}
.aov5 .dn{font-size:12px;color:var(--mu);line-height:1.6;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.aov5.thC .im{aspect-ratio:1/1!important}
.aov5.thC .dh{gap:8px;margin-top:10px}.aov5.thC .dh img{width:52px!important;height:52px!important}
.aov5.thC .dn{font-family:"Songti TC","Noto Serif TC",serif;letter-spacing:.04em;color:#7d7266}
@media (max-width:860px){.aov5.thC .dh img{width:40px!important;height:40px!important}.aov5.thC .dh{gap:5px}}

.aov5 .pb{display:none}
.aov5 .cta{align-self:flex-start;margin-top:4px;padding-bottom:2px;border-bottom:1px solid var(--g2);font-size:13px;font-weight:800;letter-spacing:.06em;color:#61443e}
.aov5 .trust{display:flex;justify-content:center;flex-wrap:wrap;gap:6px 22px;list-style:none!important;margin:0!important;padding:12px 16px!important;background:var(--c);color:#f0d39a;font-size:13px;font-weight:700;letter-spacing:.06em}
.aov5 .trust li{margin:0!important;list-style:none!important;display:flex;align-items:center;gap:6px}
.aov5 .trust li::before{content:"\\2713";font-weight:900;color:var(--g)}

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
THEMES = {}
THEMES['B'] = r'''
/* ===== B 暖色盛宴 Warm Feast ===== */
.aov5.thB{--c:#3a2418;--g:#E0A526;--g2:#D2552F;--bg:#FFF6EA;--ln:#f1dcc4;--mu:#8b6a55;--red:#D2552F}
.aov5.thB .hd{background:linear-gradient(180deg,rgba(70,30,10,.15) 0%,rgba(70,30,10,.55) 100%),radial-gradient(circle at 12% 28%,#ffd166 0 4px,transparent 5px),radial-gradient(circle at 86% 22%,#ff8a5b 0 5px,transparent 6px),radial-gradient(circle at 74% 78%,#ffd166 0 3px,transparent 4px),radial-gradient(circle at 22% 80%,#ff8a5b 0 3px,transparent 4px),url("@@PH@@-1152x1536.jpeg") center 50%/cover}
.aov5.thB .ey{color:#ffd166}.aov5.thB h2{font-family:inherit!important;font-weight:900!important;letter-spacing:.04em!important;font-size:36px!important}
.aov5.thB .trust{background:var(--red);color:#fff}.aov5.thB .trust li::before{color:#ffd166}
.aov5.thB .side{border-radius:20px;border-color:var(--ln)}
.aov5.thB .fr input:checked{border-color:var(--red)}
.aov5.thB .h{font-weight:900!important}
.aov5.thB .ti{border-radius:50%;box-shadow:0 6px 14px -8px rgba(58,36,24,.5)}
.aov5.thB .tl b{color:var(--red)}
.aov5.thB .sc{border-radius:20px;border:0;box-shadow:0 10px 26px -16px rgba(58,36,24,.45)}
.aov5.thB .sc:hover{transform:translateY(-4px) rotate(-.3deg);box-shadow:0 20px 34px -18px rgba(210,85,47,.55)}
.aov5.thB .im{aspect-ratio:1/1}
.aov5.thB .im mark{background:var(--red);color:#fff}
.aov5.thB .pb{display:inline-block;position:absolute;left:10px;bottom:10px;padding:5px 12px;border-radius:999px;background:#fff;color:var(--c);font-size:13px;font-weight:900;box-shadow:0 4px 12px rgba(0,0,0,.18)}
.aov5.thB .mt em{display:none}
.aov5.thB .mt i{background:#ffeccc;color:#9a4a12}
.aov5.thB .tx b{font-size:17px;font-weight:900}
.aov5.thB .cta{align-self:stretch;margin-top:8px;padding:10px 0;border:0;border-radius:999px;background:var(--red);color:#fff;text-align:center;font-size:14px;letter-spacing:.1em;transition:background .2s}
.aov5.thB .sc:hover .cta{background:#b8401d}
.aov5.thB .none{border-color:#f0b79f;color:var(--red)!important}
.aov5.thB .th{background:var(--red);color:#fff}.aov5.thB .th small{color:#ffd166}
.aov5.thB .tp{background:#ffeedd;border-color:var(--ln)}
.aov5.thB .hp a{background:var(--red);color:#fff!important}
@media (max-width:860px){.aov5.thB .fr:has(input:checked){background:var(--red);border-color:var(--red);color:#fff}.aov5.thB h2{font-size:26px!important}.aov5.thB .cta{padding:8px 0;font-size:13px}}
'''
THEMES['C'] = r'''
/* ===== C：跟聖誕頁（白底、黑色重點、細米色線、宋體，金色只做點綴）===== */
.aov5.thC{--c:#1d1714;--g:#C8A24A;--g2:#9A7B2E;--bg:#fff;--ln:#e6dccb;--mu:#7d7266;--k:#111;background:#fff!important}
.aov5.thC,.aov5.thC *,.aov5.thC *::before,.aov5.thC *::after{border-radius:0!important}
.aov5.thC .fr input,.aov5.thC .fr input::before{border-radius:50%!important}
.aov5.thC .hd{padding:56px 24px 52px;background:linear-gradient(180deg,rgba(0,0,0,.45) 0%,rgba(0,0,0,.82) 100%),url("@@PH@@-1152x1536.jpeg") center 50%/cover}
.aov5.thC .hd .ey{color:var(--g)}
.aov5.thC .hd h2{font-family:"Songti TC","Noto Serif TC",serif!important;font-weight:400!important;letter-spacing:.14em!important;color:#fff!important}
.aov5.thC .hd .sb{font-family:"Songti TC","Noto Serif TC",serif;letter-spacing:.06em;color:#e9e1d2}
.aov5.thC .trust{background:var(--k);color:#fff;border-top:1px solid #2a2622;font-family:"Songti TC","Noto Serif TC",serif;font-weight:400;letter-spacing:.16em}
.aov5.thC .trust li::before{color:var(--g)}
.aov5.thC .side{background:#fff;border:1px solid var(--ln);box-shadow:none}
.aov5.thC .side .st,.aov5.thC .fg h3{font-family:"Songti TC","Noto Serif TC",serif!important;font-weight:400!important;letter-spacing:.16em;color:var(--c)!important}
.aov5.thC .fg{border-top-color:#f0e9dc}
.aov5.thC .fr{color:#3d342e;font-weight:400;letter-spacing:.06em}
.aov5.thC .fr input{width:18px!important;height:18px!important;flex-basis:18px;border:1px solid #b9ab97;background:#fff}
.aov5.thC .fr input:checked{border:5px solid var(--k)}
.aov5.thC .h{font-family:"Songti TC","Noto Serif TC",serif;font-weight:400!important;letter-spacing:.14em!important;color:var(--c)!important}
.aov5.thC .h::after{content:"";display:block;width:40px;height:1px;margin-top:12px;background:var(--g)}
.aov5.thC .ti{background:#f5f1ea;box-shadow:0 0 0 1px var(--ln)!important}
.aov5.thC .tl b{font-family:"Songti TC","Noto Serif TC",serif;font-weight:400;letter-spacing:.08em;color:#3d342e}
.aov5.thC .cnt{color:var(--mu)}.aov5.thC .cnt::before{color:var(--c)}
.aov5.thC .sc{background:#fff;border:1px solid var(--ln);color:var(--c)!important;box-shadow:none}
.aov5.thC .sc:hover{transform:translateY(-3px);border-color:#cbbd9f;box-shadow:0 14px 28px -22px rgba(0,0,0,.45)}
.aov5.thC .im::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,transparent 55%,rgba(0,0,0,.6))}
.aov5.thC .im mark{z-index:2;background:var(--k)!important;color:#E4C77E!important;font-weight:400;letter-spacing:.18em;padding:3px 9px}
.aov5.thC .pb{display:inline-block;position:absolute;left:12px;bottom:10px;z-index:2;color:#fff;font-family:Baskerville,Georgia,serif;font-style:italic;font-size:17px;text-shadow:0 2px 8px rgba(0,0,0,.5)}
.aov5.thC .mt em{display:none}
.aov5.thC .mt i{background:transparent;border:1px solid var(--ln);color:#5a4f45;font-weight:400;letter-spacing:.06em}
.aov5.thC .tx b{font-family:"Songti TC","Noto Serif TC",serif;font-weight:400;letter-spacing:.08em}
.aov5.thC .cta{align-self:stretch;margin-top:8px;padding:10px 0;border:1px solid var(--k);color:var(--k);text-align:center;font-family:"Songti TC","Noto Serif TC",serif;font-weight:400;letter-spacing:.3em;transition:all .25s}
.aov5.thC .sc:hover .cta{background:var(--k);color:#E4C77E}
.aov5.thC .none{background:#faf8f4;border:1px solid var(--ln);color:var(--c)!important;font-family:"Songti TC","Noto Serif TC",serif;font-weight:400;letter-spacing:.12em}
.aov5.thC .bb{background:var(--k)!important;border:0!important;box-shadow:none!important;color:#fff}
.aov5.thC .bb>i{background:transparent!important}
.aov5.thC .bt b{color:#fff!important;font-family:"Songti TC","Noto Serif TC",serif;font-weight:400;letter-spacing:.16em}
.aov5.thC .bt small{color:#b9ad9c!important}
.aov5.thC .bm{color:#E4C77E!important;border-bottom-color:var(--g)!important;font-weight:400;letter-spacing:.16em}
.aov5.thC .bp{border:1px solid var(--ln)}
.aov5.thC .tp{background:#fff;border:0;border-top:1px solid var(--ln);box-shadow:none;padding-left:0;padding-right:0}
.aov5.thC .th{background:var(--k)!important;color:#E4C77E!important;border:0;box-shadow:none;padding:10px 28px}
.aov5.thC .th span{font-family:"Songti TC","Noto Serif TC",serif;font-weight:400;letter-spacing:.16em}
.aov5.thC .th small{color:#b9ad9c!important;font-family:Baskerville,Georgia,serif;font-style:italic;letter-spacing:.06em}
.aov5.thC .ao-hx{box-shadow:none!important}
.aov5.thC .ao-hx:not(.is-reg){background:var(--k)!important;border-color:var(--k)!important}
.aov5.thC .ao-hx.is-reg{background:#fff!important;border-color:var(--ln)!important}
.aov5.thC .hp{border-top-color:var(--ln)}.aov5.thC .hp p{color:#3d342e}
.aov5.thC .hp a{background:var(--k)!important;color:#E4C77E!important;font-family:"Songti TC","Noto Serif TC",serif;font-weight:400;letter-spacing:.2em}
.aov5.thC .hp a:hover{background:#000!important;color:#fff!important}
/* ===== Four Seasons 風：多留白、少裝飾、無剔號／emoji／徽章、文字連結代替框掣 ===== */
.aov5.thC .lay{gap:48px;padding:48px 40px 0}
.aov5.thC .trust{background:#fff;color:#5a5048;border-top:0;border-bottom:1px solid var(--ln);padding:16px!important;gap:0;font-size:12.5px;letter-spacing:.2em}
.aov5.thC .trust li::before{content:none!important}
.aov5.thC .trust li+li::before{content:""!important;display:inline-block;width:1px;height:12px;background:#d8cdbb;margin:0 22px}
.aov5.thC .side{border:0;border-right:1px solid var(--ln);padding:0 28px 0 0;background:transparent}
.aov5.thC .side .st{font-family:"Helvetica Neue",Arial,sans-serif!important;font-size:11px!important;letter-spacing:.32em!important;text-transform:uppercase;color:#8a7f73!important;margin-bottom:10px!important}
.aov5.thC .fg{border-top:1px solid #efe8db;padding-top:18px}
.aov5.thC .fr{font-size:14px;padding:7px 0}
.aov5.thC .h{font-size:26px!important}
.aov5.thC .h::after{content:none}
.aov5.thC .tls{gap:18px;margin-bottom:40px}
.aov5.thC .ti{box-shadow:none!important;width:104px;height:130px}
.aov5.thC .tl{flex-basis:104px;align-items:flex-start}
.aov5.thC .tl b{text-align:left;font-size:13.5px}
.aov5.thC .tl:hover .ti{transform:none;opacity:.85}
.aov5.thC .rh{margin-top:8px}
.aov5.thC .grid{gap:40px 28px}
.aov5.thC .sc{border:0!important;background:transparent!important}
.aov5.thC .sc:hover{transform:none;box-shadow:none!important}
.aov5.thC .sc:hover .im img{transform:scale(1.03)}
.aov5.thC .im{aspect-ratio:4/5}
.aov5.thC .im::after,.aov5.thC .im mark,.aov5.thC .pb{display:none!important}
.aov5.thC .tx{padding:16px 0 0;gap:8px}
.aov5.thC .tx b{font-size:18px}
.aov5.thC .mt{gap:10px;font-size:13px;color:#7d7266;letter-spacing:.04em}
.aov5.thC .mt i{border:0;padding:0;background:none;color:#7d7266;font-size:13px}
.aov5.thC .mt i::after{content:"";display:inline-block;width:1px;height:11px;background:#d8cdbb;margin-left:10px;vertical-align:-1px}
.aov5.thC .mt em{display:inline!important;font-weight:400;color:#7d7266}
.aov5.thC .cta{align-self:flex-start;margin-top:6px;padding:0 0 3px;border:0;border-bottom:1px solid var(--k);font-family:"Helvetica Neue",Arial,sans-serif;font-size:11.5px;letter-spacing:.28em;color:var(--k)}
.aov5.thC .sc:hover .cta{background:none;color:var(--k);border-bottom-color:var(--g)}
.aov5.thC .none{background:none;border:0;border-top:1px solid var(--ln);border-bottom:1px solid var(--ln);padding:20px;letter-spacing:.14em}
.aov5.thC .bz{margin-top:56px}
.aov5.thC .bb{background:#fff!important;color:var(--c)!important;border-top:1px solid var(--ln)!important;border-bottom:1px solid var(--ln)!important;padding:20px 4px}
.aov5.thC .bb>i{display:none}
.aov5.thC .bt b{color:var(--c)!important}
.aov5.thC .bt small{color:#7d7266!important}
.aov5.thC .bm{color:var(--k)!important;border-bottom-color:var(--k)!important;font-family:"Helvetica Neue",Arial,sans-serif;font-size:11.5px;letter-spacing:.28em}
.aov5.thC .bp li .ic{display:none}
.aov5.thC .tp{margin-top:64px;border-top:0;padding-top:0}
.aov5.thC .th{position:static;transform:none;display:block;text-align:left;background:none!important;color:var(--c)!important;padding:0 0 22px}
.aov5.thC .th span{font-size:26px}
.aov5.thC .th small{display:block;margin-top:4px;font-size:13px;color:#8a7f73!important}
.aov5.thC .hp{margin-top:56px;padding-top:36px}
@media (max-width:860px){
.aov5.thC .lay{padding:24px 16px 0;gap:20px}
.aov5.thC .side{border-right:0;padding:0;border-bottom:1px solid var(--ln)}
.aov5.thC .fg{border-top:0;padding-top:4px}
.aov5.thC .fr{border:0!important;background:none!important;padding:6px 4px;color:#8a7f73}
.aov5.thC .fr:has(input:checked){color:var(--k)!important;background:none!important;text-decoration:underline;text-underline-offset:6px}
.aov5.thC .trust{font-size:11.5px;letter-spacing:.1em}.aov5.thC .trust li+li::before{margin:0 10px}
.aov5.thC .grid{gap:28px 14px}.aov5.thC .tx b{font-size:15px}.aov5.thC .h,.aov5.thC .th span{font-size:21px!important}
.aov5.thC .ti{width:84px;height:105px}.aov5.thC .tl{flex-basis:84px}
}
/* 2026-11-21 回饋：卡加邊線、立即選購金色掣、篩選字大啲、信任列黑金有剔號 */
.aov5.thC .sc{border:1px solid var(--ln)!important;background:#fff!important;overflow:visible}
.aov5.thC .tx{padding:16px 16px 18px;flex:1;display:flex;flex-direction:column}.aov5.thC .sc{display:flex;flex-direction:column}.aov5.thC .tx .cta{margin-top:auto!important}.aov5.thC .tx>.mt,.aov5.thC .tx>.dw{margin-bottom:16px}
.aov5.thC .cta{align-self:stretch;display:flex;align-items:center;justify-content:center;gap:8px;margin-top:14px;padding:11px 0!important;background:#C8A24A;border:1px solid #C8A24A!important;color:#111!important;font-family:"Songti TC","Noto Serif TC",serif;font-size:14px!important;letter-spacing:.2em!important;text-decoration:none!important;transition:background .2s,color .2s}
.aov5.thC .cta:hover{background:#111;border-color:#111!important;color:#E4C77E!important}
.aov5.thC .sc:hover .cta{background:#C8A24A;color:#111}.aov5.thC .sc .cta:hover{background:#111;color:#E4C77E!important}
.aov5.thC .side .st{font-family:"Songti TC","Noto Serif TC",serif!important;font-size:22px!important;letter-spacing:.2em!important;text-transform:none;color:var(--c)!important;margin-bottom:14px!important}
.aov5.thC .fg h3{font-size:15.5px!important}
.aov5.thC .fr{font-size:15px}
.aov5.thC .trust{background:#111!important;color:#E4C77E!important;border-bottom:0!important;font-size:13px;letter-spacing:.16em}
.aov5.thC .trust li+li::before{content:"\2713"!important;display:inline!important;width:auto!important;height:auto!important;background:none!important;margin:0 6px 0 0!important;color:#E4C77E;font-weight:700}
.aov5.thC .trust li{margin:0 14px!important}
.aov5.thC .trust li::before{content:"\2713"!important;display:inline!important;width:auto;height:auto;background:none;margin:0 6px 0 0;color:#E4C77E;font-weight:700}
.aov5.thC .dc{font-family:"Songti TC","Noto Serif TC",serif}
@media (max-width:860px){.aov5.thC .tx{padding:12px 10px 14px}.aov5.thC .dg{grid-template-columns:repeat(4,minmax(0,1fr))}.aov5.thC .cta{font-size:13px!important;letter-spacing:.1em!important}.aov5.thC .side .st{display:none}.aov5.thC .fg h3{font-size:13.5px!important}.aov5.thC .trust li{margin:0 8px!important}}
/* 按鈕：黑底金字、粗黑體（跟「查看送貨需知」）*/
.aov5.thC .cta,.aov5.thC .hp a{background:#1a1816!important;border:1px solid #1a1816!important;color:#E4C77E!important;font-family:"Helvetica Neue","PingFang HK","Noto Sans TC",Arial,sans-serif!important;font-weight:700!important;font-size:14px!important;letter-spacing:.22em!important}
.aov5.thC .cta:hover,.aov5.thC .sc .cta:hover,.aov5.thC .hp a:hover{background:#C8A24A!important;border-color:#C8A24A!important;color:#111!important}
.aov5.thC .sc:hover .cta{background:#1a1816;color:#E4C77E}
.aov5.thC .cta svg{stroke-width:1.9}
@media (max-width:860px){.aov5.thC .cta{font-size:13px!important;letter-spacing:.12em!important}}
/* 全頁字體跟「立即選購」：粗黑體（聖誕掣保留原樣）*/
.aov5.thC,.aov5.thC *:not(.xc):not(.xc *){font-family:"Helvetica Neue","PingFang HK","Noto Sans TC",Arial,sans-serif!important;font-style:normal!important}
.aov5.thC .hd h2{font-weight:700!important;letter-spacing:.16em!important}
.aov5.thC .hd .sb{font-weight:500;letter-spacing:.08em}
.aov5.thC .h,.aov5.thC .th span{font-weight:700!important;letter-spacing:.16em!important}
.aov5.thC .th small{font-weight:700;font-size:11px!important;letter-spacing:.3em!important;text-transform:uppercase}
.aov5.thC .side .st{font-weight:700!important}
.aov5.thC .fg h3{font-weight:700!important;letter-spacing:.14em}
.aov5.thC .fr{font-weight:500}
.aov5.thC .tl b{font-weight:700;letter-spacing:.1em}
.aov5.thC .tx b{font-weight:700;letter-spacing:.08em;font-size:17px}
.aov5.thC .mt,.aov5.thC .dc,.aov5.thC .dm summary{font-weight:500}
.aov5.thC .trust{font-weight:700}
.aov5.thC .bt b{font-weight:700!important}
.aov5.thC .ao-hx .ao-hxt{font-weight:700!important;letter-spacing:.06em}
.aov5.thC .ao-hgo{font-weight:700;letter-spacing:.16em}
@media (max-width:860px){.aov5.thC .tx b{font-size:14.5px}}
/* 混合字體：大標題及套餐名用宋體，介面字用黑體 */
section.aob.aov5.thC .hd h2,section.aob.aov5.thC .h,section.aob.aov5.thC .th span,section.aob.aov5.thC .tx b,section.aob.aov5.thC .tx b span,section.aob.aov5.thC .tl b,section.aob.aov5.thC .tl b span,section.aob.aov5.thC .ao-hx .ao-hxt,section.aob.aov5.thC .ao-hx .ao-hxt *,section.aob.aov5.thC .hd h2 span,section.aob.aov5.thC .h span,section.aob.aov5.thC .th span span{font-family:"Songti TC","Noto Serif TC","PMingLiU",serif!important}
.aov5.thC .hd h2{font-weight:400!important;letter-spacing:.16em!important}
.aov5.thC .h,.aov5.thC .th span{font-weight:400!important;letter-spacing:.16em!important}
.aov5.thC .tx b{font-weight:600!important;letter-spacing:.06em;font-size:18px}
.aov5.thC .tl b{font-weight:600!important;letter-spacing:.08em}
.aov5.thC .ao-hx .ao-hxt{font-weight:600!important}
@media (max-width:860px){.aov5.thC .tx b{font-size:15px}}
@media (max-width:860px){.aov5.thC .side{background:#fff}.aov5.thC .fr{background:#fff;border:1px solid var(--ln);color:#3d342e}.aov5.thC .fr:has(input:checked){background:var(--k);border-color:var(--k);color:#E4C77E}}
'''
assert '<' not in CSS
OUT = HTML.replace('@@CSS@@', CSS)
assert '→' not in OUT and '<script' not in OUT
(H / 'catering-hub-v5-rawhtml.html').write_text(OUT, encoding='utf-8')
(H / 'catering-hub-v5-preview.html').write_text(f'<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>body{{margin:0;padding:20px 10px;background:#fff;font-family:-apple-system,"PingFang HK",sans-serif}}</style></head><body>{OUT}</body></html>', encoding='utf-8')
for t, tc in THEMES.items():
    c2 = (CSS + tc.replace('@@PH@@', W.PH))
    assert '<' not in c2
    o2 = HTML.replace('class="aob aov5"', f'class="aob aov5 th{t}"').replace('@@CSS@@', c2)
    (H / f'catering-hub-v5{t}-preview.html').write_text(f'<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>body{{margin:0;padding:20px 10px;background:#fff;font-family:-apple-system,"PingFang HK",sans-serif}}</style></head><body>{o2}</body></html>', encoding='utf-8')
    (H / f'catering-hub-v5{t}-rawhtml.html').write_text(o2, encoding='utf-8')
print('ok', len(OUT))
