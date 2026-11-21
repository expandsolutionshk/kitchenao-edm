# -*- coding: utf-8 -*-
"""/catering/ v3（2026-11-21）：沿用派對頁舊版 ao-qp 設計（樣式已在 Additional CSS），
3 個 tab（按場合／按人數／按產品系列），每個 tab 底部有商務到會（滑鼠移上顯示），TOP 5 固定在底部。
不用 <script>：tab 用 radio，商務到會用 :hover / :focus-within。"""
from pathlib import Path
import base64
H = Path(__file__).parent
S = 'https://aoaodelivery.com'
def b(z, e): return f'<span class="ao-zh" data-no-translation>{z}</span><span class="ao-en" data-no-translation>{e}</span>'
TB = ' target="_blank" rel="noopener"'
LOGO = S + '/wp-content/uploads/2023/08/kitchenAO_logo-1.png'

OCC = [  # icon, zh, en, sub zh, sub en, url, cls, limit
 ('🎄','聖誕到會','Christmas Catering','5 至 100 人聖誕套餐・12 月 12 日至 27 日','Sets for 5 to 100・12 to 27 Dec','/catering/christmas/','is-xmas',('聖誕限定','Christmas Special')),
 ('🎂','生日派對','Birthday Parties','熱盤主菜、小食及甜品','Hot mains, snacks and desserts','/product-category/party/foot-party/','',None),
 ('🧸','兒童派對','Kids Parties','兒童餐及派對小食・5 人起','Kids meals and snacks・from 5 pax','/product-category/party/children/','',None),
 ('💼','公司活動','Corporate Events','年會、團年飯及員工聚餐','Annual dinners and staff gatherings','/corporate-catering-hk/','',None),
 ('🥂','酒會及開張','Receptions & Openings','Canapé、手指食物及會議茶點','Canapés, finger food and refreshments','/business-event/','',None),
 ('🍱','商務午餐','Office Lunch','商務餐盒、員工午餐及高級餐盒','Business and staff lunch boxes','/product-category/商務活動/commercial-lunch-box/','',None),
 ('🚤','船河派對','Junk Trips','碼頭交收・方便分發','Pier delivery・easy to share','/product-category/party/boat-party-set/','',None),
 ('🥗','素食聚會','Vegetarian Gatherings','「素」味人生素食套餐','Vegetarian party sets','/product-category/party/vegetarians-set/','',None),
 ('🧺','野餐及戶外','Picnics & Outdoors','Chill 一下野餐盒','Chill Picnic Box','/product-category/party/chill-box/','',None),
]
PPL = [('2 &#8211; 6','2-6人分享選項','小型聚會','Small gatherings','2_6'),('7 &#8211; 11','7-11人分享選項','家庭派對','Family parties','7_11'),
       ('12 &#8211; 16','12-16人分享選項','生日派對','Birthday parties','12_16'),('18 &#8211; 25','18-25人分享選項','公司／朋友聚餐','Office / friends&#8217; meals','18_25'),
       ('30+','30人以上分享選項','大型活動','Large events','30'),('100+','100人以上分享選項','企業活動','Corporate events','100')]

def occ_card(ic, z, e, dz, de, u, c, lim):
    m = f'<mark class="ao-qp-limit">{b(*lim)}</mark>' if lim else ''
    sub = '' if lim else f'<small>{b(dz, de)}</small>'
    name = f'<b>{b(z, e)}' + (f'<span class="ao-qp-l2"> {b(dz, de)}</span>' if lim else '') + '</b>'
    slug = u.strip('/').split('/')[-1]
    return f'<a class="{c}" href="{S}{u}"{TB} data-ga="hub_occ_{slug}"><i>{ic}</i>{m}<span>{name}{sub}</span></a>'

occ = ''.join(occ_card(*o) for o in OCC)
ppl = ''.join(f'<a href="{S}/product-category/party-set-by-people/{sl}/"{TB} data-ga="hub_ppl_{g}"><b>{n}<small>{b("人"," pax")}</small></b><em>{b(z,e)}</em></a>' for n, sl, z, e, g in PPL)

SERIES = f'''<a class="is-xmas" href="{S}/product-category/christmas-party-catering-set/?ao_ref=xmas26_hub"{TB} data-ga="hub_s_christmas"><i>🎄</i><mark class="ao-qp-limit">{b("聖誕限定","Christmas Special")}</mark><span><b>{b("聖誕派對到會套餐","Christmas Party Catering Sets")}<span class="ao-qp-l2"> {b("限量寶箱牛肉 × 原隻黃油雞","Limited Treasure Box Beef × Whole Yellow Chicken")}</span></b></span></a><a class="is-hot" href="{S}/product-category/party/foot-party/"{TB} data-ga="hub_s_gourmet"><i>⭐</i><span><b>{b("美食派對","Gourmet")}<span class="ao-qp-l2"> Gourmet Set</span></b><small>{b("人氣之選・熱食主菜","Popular choice・hot mains")}</small></span><em>{b("人氣","Popular")}</em></a><a href="{S}/product-category/party/refreshment-set/"{TB} data-ga="hub_s_refreshment"><i>🥂</i><span><b>{b("輕食宴會 Refreshment","Refreshment Set")}</b><small>{b("會議茶點・開幕酒會","Meetings・opening receptions")}</small></span></a><a href="{S}/product-category/party/meat-monster/"{TB} data-ga="hub_s_meat"><i>🍖</i><span><b>{b("肉食獸套餐","Meat Lovers Set")}</b><small>{b("上將海港之選","Harbour City favourite")}</small></span></a><a href="{S}/product-category/party/children/"{TB} data-ga="hub_s_kids"><i>🧸</i><span><b>{b("兒童派對套餐","Kids&#8217; Party Sets")}</b><small>{b("兒童生日派對","Children&#8217;s birthday parties")}</small></span></a><a href="{S}/product-category/party/set-for-two/"{TB} data-ga="hub_s_couple"><i>💑</i><span><b>{b("雙人套餐","Sets for Two")}</b><small>{b("二人慶祝・紀念日","Celebrations・anniversaries")}</small></span></a><a href="{S}/product-category/party/vegetarians-set/"{TB} data-ga="hub_s_veg"><i>🥗</i><span><b>{b("「素」味人生","Veggie Delight")}</b><small>{b("素食派對套餐","Vegetarian party sets")}</small></span></a><a href="{S}/product-category/party/boat-party-set/"{TB} data-ga="hub_s_boat"><i>🚤</i><span><b>{b("船河派對套餐","Boat Party Sets")}</b><small>{b("碼頭交收・方便分發","Pier pick-up・easy to share")}</small></span></a><a href="{S}/product-category/party/chill-box/"{TB} data-ga="hub_s_chill"><i>🧺</i><span><b>{b("Chill 一下野餐盒","Chill Picnic Box")}</b><small>{b("野餐・戶外活動","Picnics・outdoor events")}</small></span></a><a href="{S}/product-category/party/platter/"{TB} data-ga="hub_s_platter"><i>🍢</i><span><b>{b("手指食物拼盤","Party Platters")}</b><small>Finger Food・Platter</small></span></a><a href="{S}/product-category/a-la-carte/"{TB} data-ga="hub_s_alacarte"><i>🍽️</i><span><b>{b("單品","À la carte")}<span class="ao-qp-l2 ao-zh" data-no-translation> À la carte</span></b><small>{b("小食・主菜・甜品自由配搭","Snacks, mains and desserts to mix and match")}</small></span></a><a href="{S}/product-category/party-supplies/"{TB} data-ga="hub_s_supplies"><i>🎉</i><span><b>{b("派對用品","Party Supplies")}<span class="ao-qp-l2 ao-zh" data-no-translation> Party Supplies</span></b><small>{b("餐具・食物架・派對配件","Tableware・food stands・party accessories")}</small></span></a>'''

import json as _json
_D = _json.load(open('/sessions/great-festive-darwin/mnt/Desktop/cowork - aoao/xmas-2026/desc.json', encoding='utf-8'))
def _price(key, pax):
    for x in _D:
        if x['t'].startswith(f'AO {pax}pax ') and key in x['t']: return x['price']
    raise KeyError((key, pax))
UP = S + '/wp-content/uploads/'
XMASCAT = S + '/product-category/christmas-party-catering-set/?ao_ref=xmas26_hub'
def _xp(key): return {z: _price(key, z).replace('HK$','') for z in ['5-6','8-10','12-16','18-22','26-30','35-40','48-54','63-68','78-85','90-100'] if any(x['t'].startswith(f'AO {z}pax ') and key in x['t'] for x in _D)}
def _xu(slug): return lambda z: f'{S}/product/{z}pax-{slug}/?ao_ref=xmas26_hub'
GU = {'48-54':'ao-48-54pax-美食派對-gourmet-set-複製','63-68':'ao-63-68pax-美食派對-gourmet-set','78-85':'ao-78-85pax-美食派對-gourmet-set'}
CARDS = [
 dict(tag=('5-40 人．全港限量 100 個','5-40 pax · Limited to 100'), zn='聖誕寶藏箱．煙燻慢煮美國牛翼板肉盛宴｜聖誕套餐', en='Christmas Treasure Box · Smoked Slow-Cooked US Beef Chuck Flap Feast | Christmas Set',
      img=UP+'2026/11/2026-XMAS-IG-11-600x750.jpg', link=XMASCAT, price=_xp('寶藏箱'), url=_xu('christmas-set-treasure-box-beef'), dflt='12-16'),
 dict(tag=('5-40 人．全港限量 100 個','5-40 pax · Limited to 100'), zn='聖誕金雞獻禮．燒南乳香慢煮原隻黃油雞｜聖誕套餐', en='Christmas Golden Roast · Slow-Cooked Red Beancurd Whole Yellow Chicken | Christmas Set',
      img=UP+'2026/11/2026-XMAS-IG-10-600x750.jpg', link=XMASCAT, price=_xp('金雞'), url=_xu('christmas-set-golden-roast-chicken'), dflt='18-22'),
 dict(tag=('48-100 人．年尾大型派對首選','48-100 pax · For year-end celebrations'), zn='聖誕開箱雙寶．燒南乳香慢煮原隻黃油雞 × 煙燻慢煮美國牛翼板肉｜聖誕套餐', en='Christmas Twin Treasures · Whole Yellow Chicken × Smoked US Beef Chuck Flap | Christmas Set',
      img=UP+'2026/11/2026-XMAS-IG-16-600x750.jpg', link=XMASCAT, price=_xp('雙寶'), url=_xu('christmas-set-twin-treasures-chicken-beef'), dflt='48-54'),
 dict(tag=('人氣之選・熱食主菜','Popular choice · hot mains'), zn='美食派對．Gourmet Set', en='Gourmet Set · Party Catering',
      img=UP+'2026/03/12-16_101-X-KITCHENAO-03-03-03-03-600x600.jpg', link=S+'/product-category/party/foot-party/',
      price={'5-6':'1,388','8-10':'1,988','12-16':'2,988','18-22':'3,888','26-30':'5,188','35-40':'6,788','48-54':'9,188','63-68':'11,388','78-85':'13,588'},
      url=lambda z: f'{S}/product/{GU.get(z, "ao-"+z+"pax-gourmet-set")}/', dflt='12-16', reg=1),
 dict(tag=('會議茶點・開幕酒會','Meetings · opening receptions'), zn='輕食宴會套餐．Refreshment', en='Refreshment Set · Meetings &amp; Receptions',
      img=UP+'2023/11/refreshmentparty-04-600x600.jpg', link=S+'/product-category/party/refreshment-set/',
      price={'12-16':'2,688','18-22':'3,488','26-30':'4,688','35-40':'5,988'},
      url=lambda z: f'{S}/product/ao-{z}pax-refreshment-set/', dflt='18-22', reg=1),
]
def xcard(n, c):
    nm = f'aoX{n}'; sizes = list(c['price']); dz = lambda z: z.replace('-', '–')
    zn1, zn2 = c['zn'].split('．', 1); en1, en2 = c['en'].split(' · ', 1)
    radios = ''.join(f'<input class="ao-qp-r r{k+1}" type="radio" name="{nm}" id="{nm}-{k+1}"{" checked" if z == c["dflt"] else ""}>' for k, z in enumerate(sizes))
    titles = ''.join(f'<span class="v v{k+1}">{b(f"AO {z}pax {zn1}<i>{zn2}</i>", f"AO {z}pax {en1}<i>{en2}</i>")}</span>' for k, z in enumerate(sizes))
    prices = ''.join(f'<span class="v v{k+1}"><small>HK$</small><strong>{c["price"][z]}</strong></span>' for k, z in enumerate(sizes))
    cols = 'n4' if len(sizes) == 4 else ''
    chips = ''.join(f'<label class="c{k+1}" for="{nm}-{k+1}">{dz(z)}</label>' for k, z in enumerate(sizes))
    btns = ''.join(f'<a class="ao-hgo v v{k+1}" href="{c["url"](z)}"{TB} data-ga="hub_top{n}_{z}">{b("立即配搭菜式","Build Your Set")}</a>' for k, z in enumerate(sizes))
    return (f'<div class="ao-hx{" is-reg" if c.get("reg") else ""}">{radios}<a class="ao-qp-ph" href="{c["link"]}"{TB} data-ga="hub_top{n}_img"><img src="{c["img"]}" alt="{zn1}｜Kitchen AO" width="600" height="600" loading="lazy" decoding="async"><span class="ao-qp-rank">TOP {n}</span></a>'
            f'<span class="ao-qp-pi"><span class="ao-htag">{b(*c["tag"])}</span><b class="ao-hxt">{titles}</b><span class="ao-hsz {cols}">{chips}</span><span class="ao-hpr">{prices}</span><span class="ao-hcta">{btns}</span></span></div>')
top = ''.join(xcard(n+1, c) for n, c in enumerate(CARDS))

BIZ_ITEMS = [('🍱','商務飯盒','Business Lunch Boxes'),('🤝','團隊活動','Team Building'),('🥂','酒會小食','Finger Food &amp; Canapés'),('🎀','開張套餐','Opening Ceremony Sets'),('🎪','活動到會','Event Catering'),('🏆','周年晚宴','Annual Dinner'),('🍸','雞尾酒服務','Cocktail Service・Free Flow'),('🤵','服務生安排','Service Staff'),('📝','訂製食譜','Customised Recipes')]
biz_list = ''.join(f'<li data-no-translation><span class="ao-biz-ic">{ic}</span><span class="zh">{z}</span><span class="en">{e}</span></li>' for ic, z, e in BIZ_ITEMS)
WA_BIZ = 'https://api.whatsapp.com/send?phone=85269011987&amp;text=%E4%BC%81%E6%A5%AD%E5%8F%8A%E5%95%86%E5%8B%99%E5%88%B0%E6%9C%83%E6%9C%8D%E5%8B%99%E6%9F%A5%E8%A9%A2'
def biz(tag):
    return f'''<div class="ao-biz ao-hbiz"><div class="ao-biz-wrap"><span class="ao-biz-btn" role="button" tabindex="0" aria-haspopup="true"><span class="ao-biz-bi">💼</span><span class="ao-biz-tx">{b("商務到會 TIPS","Business Catering TIPS")}</span><span class="ao-biz-car">▾</span></span><div class="ao-biz-panel" role="region" aria-label="商務到會服務"><div class="ao-biz-ph"><span>FOR BUSINESS</span><b>{b("企業及商務到會服務","Corporate &amp; Business Catering")}</b></div><ul class="ao-biz-list">{biz_list}</ul><div class="ao-hbb"><a class="ao-biz-wa" href="{WA_BIZ}"{TB} data-ga="hub_biz_whatsapp_{tag}">{b("WhatsApp 聯絡企業客戶專員","WhatsApp our corporate team")}</a><a class="ao-biz-more" href="{S}/business-event/"{TB} data-ga="hub_biz_intro_{tag}">{b("商務活動簡介","Business events overview")}</a></div></div></div></div>'''

WA = 'https://wa.me/85269011987?text=%E4%BD%A0%E5%A5%BD%EF%BC%8C%E6%88%91%E5%B7%B2%E5%9C%A8%20Kitchen%20AO%20%E7%B6%B2%E7%AB%99%E7%80%8F%E8%A6%BD%E9%81%8E%E6%B4%BE%E5%B0%8D%E5%88%B0%E6%9C%83%E9%A4%90%E5%96%AE%EF%BC%8C%E4%BD%86%E4%BB%8D%E6%9C%AA%E6%B1%BA%E5%AE%9A%E9%81%B8%E6%93%87%E5%93%AA%E4%B8%80%E6%AC%BE%EF%BC%8C%E6%83%B3%E6%9F%A5%E8%A9%A2%E4%BB%A5%E4%B8%8B%E5%95%8F%E9%A1%8C%EF%BC%9A'

B64 = base64.b64encode((H / 'ao-wow-cursor.png').read_bytes()).decode()
CSS = '''
.ao-hubx{margin-top:0!important}
.ao-hubx .ao-qp-head--photo{background-image:linear-gradient(180deg,rgba(24,16,11,.28) 0%,rgba(24,16,11,.5) 68%,#1d150f 100%),url("https://aoaodelivery.com/wp-content/uploads/2025/05/PHOTO-2025-03-14-16-33-30-2-1152x1536.jpeg")!important;background-position:center 50%!important;background-size:cover!important}
@media (max-width:640px){.ao-hubx .ao-qp-head--photo{background-image:linear-gradient(180deg,rgba(24,16,11,.28) 0%,rgba(24,16,11,.5) 68%,#1d150f 100%),url("https://aoaodelivery.com/wp-content/uploads/2025/05/PHOTO-2025-03-14-16-33-30-2-768x1024.jpeg")!important}}
.ao-hubx .ao-qp-r{position:absolute;opacity:0;width:1px;height:1px;pointer-events:none}
.ao-hubx .ao-qt{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin:0 0 6px}
.ao-hubx .ao-qt label{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px;min-height:64px;margin:0!important;padding:10px 8px;border-radius:14px;border:1px solid rgba(214,180,104,.3);background:rgba(255,255,255,.04);color:#e9dcc6;font-size:17px;font-weight:800;letter-spacing:1.5px;line-height:1.25;text-align:center;cursor:pointer;transition:all .25s ease}
.ao-hubx .ao-qt label i{display:inline-flex;align-items:center;justify-content:center;width:22px;height:22px;margin-right:6px;border-radius:50%;background:rgba(214,180,104,.25);color:#f0d39a;font-style:normal;font-size:12px;vertical-align:2px}
.ao-hubx .ao-qt label small{font-size:10.5px;font-weight:800;letter-spacing:2.5px;opacity:.65}
.ao-hubx .ao-qt label:hover{border-color:#c9a45c;background:rgba(201,164,92,.12)}
#aoHt1:checked ~ .ao-qt label[for=aoHt1],#aoHt2:checked ~ .ao-qt label[for=aoHt2],#aoHt3:checked ~ .ao-qt label[for=aoHt3]{background:linear-gradient(135deg,#f0d39a 0%,#d2a44e 100%);border-color:transparent;color:#241a12;box-shadow:0 8px 20px rgba(0,0,0,.4)}
#aoHt1:checked ~ .ao-qt label[for=aoHt1] i,#aoHt2:checked ~ .ao-qt label[for=aoHt2] i,#aoHt3:checked ~ .ao-qt label[for=aoHt3] i{background:#241a12;color:#f0d39a}
.ao-hubx #aoHt1:focus-visible ~ .ao-qt label[for=aoHt1],.ao-hubx #aoHt2:focus-visible ~ .ao-qt label[for=aoHt2],.ao-hubx #aoHt3:focus-visible ~ .ao-qt label[for=aoHt3]{outline:2px solid #f0d39a;outline-offset:3px}
.ao-hubx .ao-qp-tp{display:none}
#aoHt1:checked ~ .ao-qp-tps .ao-qp-tp1,#aoHt2:checked ~ .ao-qp-tps .ao-qp-tp2,#aoHt3:checked ~ .ao-qp-tps .ao-qp-tp3{display:block;animation:aoHtIn .3s ease}
@keyframes aoHtIn{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}
.ao-hubx .ao-qp-tp .ao-qp-box{margin-top:14px;padding:22px 20px}
.ao-hubx .ao-qp-tp1 .ao-qp-series{grid-template-columns:repeat(3,minmax(0,1fr))}
.ao-hubx .ao-qp-tp .ao-biz{margin:14px -36px 0}
.ao-hubx .ao-qp-sec--top{margin-top:52px}
.ao-hubx .ao-qp-tp1 .ao-qp-series a.is-xmas .ao-qp-l2{display:block;margin-top:4px;font-size:12.5px;font-weight:600;letter-spacing:.3px;line-height:1.5}
.ao-hubx .ao-biz-btn{text-decoration:none;user-select:none}
.ao-hubx .ao-biz-wrap:hover .ao-biz-btn,.ao-hubx .ao-biz-wrap:focus-within .ao-biz-btn{animation:none}
.ao-hubx .ao-biz-wrap:hover .ao-biz-car,.ao-hubx .ao-biz-wrap:focus-within .ao-biz-car{transform:rotate(180deg)}
.ao-hubx .ao-biz-wrap:hover .ao-biz-panel,.ao-hubx .ao-biz-wrap:focus-within .ao-biz-panel{opacity:1;visibility:visible;transform:translate(-50%,0)}
.ao-hubx .ao-biz-panel{z-index:30;cursor:auto}
.ao-hubx .ao-biz-ph{padding-bottom:12px}.ao-hubx .ao-biz-ph span{font-size:13px;letter-spacing:3.5px}.ao-hubx .ao-biz-ph b{margin-top:4px;font-size:22px;letter-spacing:1px}
.ao-hubx .ao-biz,.ao-hubx .ao-biz-btn,.ao-hubx .ao-biz-btn *{cursor:url("data:image/png;base64,__B64__") 1 1,pointer}
.ao-hubx .ao-biz-panel a{cursor:pointer}
.ao-hubx .ao-biz-panel{width:min(480px,92vw);padding:14px 16px 14px}
.ao-hubx .ao-biz-ph{margin:0 0 10px;padding:0 0 8px}
.ao-hubx .ao-biz-list{margin:0 0 10px!important}
.ao-hubx .ao-biz-list li{gap:8px;padding:5px 12px!important;font-size:14px;line-height:1.45;white-space:nowrap}
.ao-hubx .ao-biz-list li .zh{flex:0 0 auto;font-weight:800;color:#1e2a4a}
.ao-hubx .ao-biz-list li .en{margin-left:auto;min-width:0;overflow:hidden;text-overflow:ellipsis;font-size:12.5px;font-weight:600;color:#6b7a99;letter-spacing:.2px}
.ao-hubx .ao-hbb{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.ao-hubx .ao-hbb a{white-space:nowrap;display:flex;align-items:center;justify-content:center;margin:0!important;padding:11px 10px;font-size:14px;letter-spacing:.5px;text-align:center}
@media (max-width:640px){.ao-hubx .ao-biz-panel{padding:12px 12px}.ao-hubx .ao-biz-list li{padding:5px 10px!important;font-size:13.5px}.ao-hubx .ao-biz-list li .en{font-size:11.5px}.ao-hubx .ao-hbb{grid-template-columns:1fr;gap:6px}.ao-hubx .ao-hbb a{font-size:14px;padding:10px 8px;white-space:nowrap}}
.ao-hubx .ao-qp-pop .ao-hx{position:relative;display:flex;flex-direction:column;overflow:hidden;border-radius:0;border:1px solid rgba(200,162,74,.55);background:#111;color:#EDE6D8;box-shadow:0 10px 26px rgba(0,0,0,.45);transition:transform .25s ease,border-color .25s ease}
@media (hover:hover){.ao-hubx .ao-qp-pop .ao-hx:hover{transform:translateY(-4px);border-color:#C8A24A}}
.ao-hubx .ao-qp-pop .ao-qp-ph{aspect-ratio:4/5}
.ao-hubx .ao-qp-pop .ao-hx a{background:transparent;border:0;border-radius:0;box-shadow:none;overflow:visible;transform:none;color:inherit}
.ao-hubx .ao-qp-pop .ao-hx a.ao-qp-ph{display:block;overflow:hidden;border-bottom:1px solid rgba(200,162,74,.55)}
.ao-hubx .ao-qp-pop .ao-hx a.ao-hgo{display:none;padding:0 0 3px;border-bottom:1px solid #C8A24A}
.ao-hubx .ao-hx .ao-qp-ph{border-bottom:1px solid rgba(200,162,74,.55)}
.ao-hubx .ao-hx .ao-qp-rank{border-radius:0;background:#111;color:#E4C77E;box-shadow:inset 0 0 0 1px #C8A24A;letter-spacing:2px}
.ao-hubx .ao-hx .v{display:none}
.ao-hubx .ao-hpx{position:absolute;top:0;right:0;z-index:2;display:flex;align-items:baseline;gap:4px;background:#fff;border-left:1px solid #111;border-bottom:1px solid #111;padding:6px 8px 5px;line-height:1;box-shadow:inset 0 0 0 2px #fff,inset 0 0 0 3px rgba(200,162,74,.55)}
.ao-hubx .ao-hpx b{font:italic 400 15px/1 Baskerville,"Baskerville Old Face",Georgia,serif;color:#9A7B2E;letter-spacing:.02em}
.ao-hubx .ao-hpx i{font:700 8.5px/1 "Helvetica Neue","PingFang HK",Arial,sans-serif;font-style:normal;letter-spacing:.08em;color:#111}
.ao-hubx .ao-hx .ao-qp-pi{padding:14px 14px 16px;text-align:center;align-items:center}
.ao-hubx .ao-htag{font-size:10px;font-weight:600;letter-spacing:.18em;color:#C8A24A;line-height:1.5}
.ao-hubx .ao-hx .ao-hxt{margin:6px 0 0;font-family:"Songti TC","Noto Serif TC","PMingLiU",Baskerville,serif;font-size:16px;font-weight:600;line-height:1.45;color:#fff;letter-spacing:.04em}
.ao-hubx .ao-hx .ao-hxt i{display:block;margin-top:3px;font-style:normal;font-size:12px;font-weight:500;color:#cfc6b6;letter-spacing:.02em;line-height:1.55}
html[lang^="en"] .ao-hubx .ao-hx .ao-hxt{font-family:Baskerville,"Baskerville Old Face",Georgia,serif;font-weight:400}
.ao-hubx .ao-hpr{margin:12px 0 0;line-height:1}
.ao-hubx .ao-hpr small{margin-right:3px;font-size:11px;color:#C8A24A;letter-spacing:.08em}
.ao-hubx .ao-hpr strong{font-size:22px;font-weight:700;color:#fff;letter-spacing:.02em}
.ao-hubx .ao-hsz{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:6px;width:100%;margin:12px 0 0}
.ao-hubx .ao-hsz.n4{grid-template-columns:repeat(2,minmax(0,1fr))}
.ao-hubx .ao-hsz label{margin:0!important;padding:6px 2px;border:1px solid rgba(237,230,216,.4);border-radius:0;color:#fff;font:600 11.5px/1.2 "Helvetica Neue","PingFang HK",Arial,sans-serif;letter-spacing:.03em;text-align:center;cursor:pointer;transition:all .2s}
.ao-hubx .ao-hsz label:hover{border-color:#C8A24A;color:#E4C77E}
.ao-hubx .ao-hcta{margin-top:auto;padding-top:14px}
.ao-hubx .ao-hgo{font-family:"Songti TC","Noto Serif TC",Baskerville,Georgia,serif;font-size:15px;color:#E4C77E!important;border-bottom:1px solid #C8A24A;padding-bottom:3px;letter-spacing:.08em;text-decoration:none!important}
.ao-hubx .ao-hgo:hover{color:#fff!important;border-color:#fff}
.ao-hubx .ao-qp-pop .ao-hx.is-reg{background:#FBF7EF;border-color:#E3D3B5;color:#2b211b}
.ao-hubx .ao-hx.is-reg a.ao-qp-ph{border-bottom-color:#d6b468}
.ao-hubx .ao-hx.is-reg .ao-qp-rank{background:#2b211b;color:#f0d39a;box-shadow:none}
.ao-hubx .ao-hx.is-reg .ao-htag{color:#9A7B2E}
.ao-hubx .ao-hx.is-reg .ao-hxt{color:#2b211b}
.ao-hubx .ao-hx.is-reg .ao-hxt i{color:#7d6a55}
.ao-hubx .ao-hx.is-reg .ao-hsz label{border-color:#d9c9ab;color:#2b211b}
.ao-hubx .ao-hx.is-reg .ao-hsz label:hover{border-color:#2b211b;color:#2b211b}
.ao-hubx .ao-hx.is-reg .ao-hpr small{color:#9A7B2E}
.ao-hubx .ao-hx.is-reg .ao-hpr strong{color:#2b211b}
.ao-hubx .ao-qp-pop .ao-hx.is-reg a.ao-hgo{color:#7d5b27!important;border-bottom-color:#7d5b27}
.ao-hubx .ao-qp-pop .ao-hx.is-reg a.ao-hgo:hover{color:#2b211b!important;border-bottom-color:#2b211b}
.ao-hubx .ao-qp-series a.is-xmas{background:#111!important;border:1px solid #C8A24A!important;box-shadow:0 6px 18px rgba(0,0,0,.35)!important}
.ao-hubx .ao-qp-series a.is-xmas:hover{background:#1a1a1a!important}
.ao-hubx .ao-qp-series a.is-xmas i{background:rgba(200,162,74,.16)!important}
.ao-hubx .ao-qp-series a.is-xmas b{font-family:"Songti TC","Noto Serif TC",Baskerville,serif;letter-spacing:.06em}
.ao-hubx .ao-qp-series a.is-xmas .ao-qp-l2{color:#cfc6b6!important}
.ao-hubx .ao-qp-series a.is-xmas .ao-qp-limit{flex:0 0 auto;white-space:nowrap;border-radius:0!important;background:transparent!important;border:1px solid #C8A24A;color:#E4C77E!important;font-size:11px;font-weight:600;letter-spacing:.16em;padding:3px 8px;box-shadow:none!important;animation:none!important}
.ao-hubx .ao-hx .r1:checked ~ * .v1{display:inline}.ao-hubx .ao-hx .r1:checked ~ * a.v1{display:inline-block}.ao-hubx .ao-hx .r1:checked ~ * label.c1{background:#C8A24A;border-color:#C8A24A;color:#111}
.ao-hubx .ao-hx .r2:checked ~ * .v2{display:inline}.ao-hubx .ao-hx .r2:checked ~ * a.v2{display:inline-block}.ao-hubx .ao-hx .r2:checked ~ * label.c2{background:#C8A24A;border-color:#C8A24A;color:#111}
.ao-hubx .ao-hx .r3:checked ~ * .v3{display:inline}.ao-hubx .ao-hx .r3:checked ~ * a.v3{display:inline-block}.ao-hubx .ao-hx .r3:checked ~ * label.c3{background:#C8A24A;border-color:#C8A24A;color:#111}
.ao-hubx .ao-hx .r4:checked ~ * .v4{display:inline}.ao-hubx .ao-hx .r4:checked ~ * a.v4{display:inline-block}.ao-hubx .ao-hx .r4:checked ~ * label.c4{background:#C8A24A;border-color:#C8A24A;color:#111}
.ao-hubx .ao-hx .r5:checked ~ * .v5{display:inline}.ao-hubx .ao-hx .r5:checked ~ * a.v5{display:inline-block}.ao-hubx .ao-hx .r5:checked ~ * label.c5{background:#C8A24A;border-color:#C8A24A;color:#111}
.ao-hubx .ao-hx .r6:checked ~ * .v6{display:inline}.ao-hubx .ao-hx .r6:checked ~ * a.v6{display:inline-block}.ao-hubx .ao-hx .r6:checked ~ * label.c6{background:#C8A24A;border-color:#C8A24A;color:#111}
.ao-hubx .ao-hx .r7:checked ~ * .v7{display:inline}.ao-hubx .ao-hx .r7:checked ~ * a.v7{display:inline-block}.ao-hubx .ao-hx .r7:checked ~ * label.c7{background:#C8A24A;border-color:#C8A24A;color:#111}
.ao-hubx .ao-hx .r8:checked ~ * .v8{display:inline}.ao-hubx .ao-hx .r8:checked ~ * a.v8{display:inline-block}.ao-hubx .ao-hx .r8:checked ~ * label.c8{background:#C8A24A;border-color:#C8A24A;color:#111}
.ao-hubx .ao-hx .r9:checked ~ * .v9{display:inline}.ao-hubx .ao-hx .r9:checked ~ * a.v9{display:inline-block}.ao-hubx .ao-hx .r9:checked ~ * label.c9{background:#C8A24A;border-color:#C8A24A;color:#111}
.ao-hubx .ao-hx.is-reg .r1:checked ~ * label.c1{background:#2b211b;border-color:#2b211b;color:#f0d39a}.ao-hubx .ao-hx.is-reg .r2:checked ~ * label.c2{background:#2b211b;border-color:#2b211b;color:#f0d39a}.ao-hubx .ao-hx.is-reg .r3:checked ~ * label.c3{background:#2b211b;border-color:#2b211b;color:#f0d39a}.ao-hubx .ao-hx.is-reg .r4:checked ~ * label.c4{background:#2b211b;border-color:#2b211b;color:#f0d39a}.ao-hubx .ao-hx.is-reg .r5:checked ~ * label.c5{background:#2b211b;border-color:#2b211b;color:#f0d39a}.ao-hubx .ao-hx.is-reg .r6:checked ~ * label.c6{background:#2b211b;border-color:#2b211b;color:#f0d39a}.ao-hubx .ao-hx.is-reg .r7:checked ~ * label.c7{background:#2b211b;border-color:#2b211b;color:#f0d39a}.ao-hubx .ao-hx.is-reg .r8:checked ~ * label.c8{background:#2b211b;border-color:#2b211b;color:#f0d39a}.ao-hubx .ao-hx.is-reg .r9:checked ~ * label.c9{background:#2b211b;border-color:#2b211b;color:#f0d39a}
@media (max-width:1080px){.ao-hubx .ao-qp-pop .ao-hx{flex:0 0 31%;scroll-snap-align:start}}
@media (max-width:640px){.ao-hubx .ao-qp-pop .ao-hx{flex:0 0 66%}}
@media (max-width:960px){.ao-hubx .ao-qp-tp1 .ao-qp-series{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:640px){
.ao-hubx .ao-qt{gap:6px}
.ao-hubx .ao-qt label{min-height:58px;padding:8px 4px;font-size:13.5px;letter-spacing:.5px;border-radius:12px}
.ao-hubx .ao-qt label i{display:none}
.ao-hubx .ao-qt label small{font-size:9px;letter-spacing:1px}
.ao-hubx .ao-qp-tp .ao-qp-box{padding:16px 8px}
.ao-hubx .ao-qp-tp .ao-biz{margin:12px -14px 0}
.ao-hubx .ao-qp-sec--top{margin-top:44px}
}
@media (prefers-reduced-motion:reduce){.ao-hubx .ao-qp-tp{animation:none!important}}
'''
CSS = CSS.replace('__B64__', B64)
assert '<' not in CSS

def tag(n, z, e, en_small):
    return f'<label for="aoHt{n}"><span><i>{n}</i>{b(z, e)}</span><small>{en_small}</small></label>'

HTML = f'''<section class="ao-qp ao-qp--a ao-hubx" aria-labelledby="ao-hub-title">
<div class="ao-qp-head ao-qp-head--photo"><p class="ao-qp-eyebrow">Kitchen AO Catering</p><h2 id="ao-hub-title" class="ao-qp-title">{b("按場合揀選到會套餐","Choose Catering by Occasion")}</h2><span class="ao-qp-orn" aria-hidden="true"><i></i>◆<i></i></span><p class="ao-qp-sub">{b("先揀活動場合，再按人數及預算選擇合適套餐，網上即可下單。","Pick your occasion, then choose a set by headcount and budget, and order online.")}</p></div>
<input class="ao-qp-r" type="radio" name="aoHt" id="aoHt1" checked><input class="ao-qp-r" type="radio" name="aoHt" id="aoHt2"><input class="ao-qp-r" type="radio" name="aoHt" id="aoHt3">
<div class="ao-qt" role="tablist">{tag(1,"🎉 按場合","🎉 By Occasion","BY OCCASION")}{tag(2,"👥 按人數","👥 By Headcount","BY GUESTS")}{tag(3,"🍽️ 按產品系列","🍽️ By Series","OUR MENU")}</div>
<div class="ao-qp-tps">
<div class="ao-qp-tp ao-qp-tp1"><div class="ao-qp-sec ao-qp-box ao-qp-box--ser"><div class="ao-qp-series">{occ}</div></div>{biz("occ")}</div>
<div class="ao-qp-tp ao-qp-tp2"><div class="ao-qp-sec ao-qp-box ao-qp-box--ppl"><div class="ao-qp-ppl">{ppl}</div></div>{biz("ppl")}</div>
<div class="ao-qp-tp ao-qp-tp3"><div class="ao-qp-sec ao-qp-box ao-qp-box--ser"><div class="ao-qp-series">{SERIES}</div></div>{biz("ser")}</div>
</div>
<div class="ao-qp-sec ao-qp-sec--top"><div class="ao-qp-tophead"><span class="ao-qp-toptag">{b("🔥 本週","🔥 This Week&#8217;s")} <b>TOP 5</b> {b("人氣推介","Popular Picks")}<small>CHEF&#8217;S PICKS</small></span></div><div class="ao-qp-slider"><div class="ao-qp-pop">{top}</div></div></div>
<div class="ao-qp-help"><p>{b("仍未決定選擇哪一款？","Still deciding?")}</p><a href="{WA}" target="_blank" rel="noopener noreferrer" data-ga="hub_whatsapp">{b("WhatsApp 專人為你配搭餐單","WhatsApp us for a tailored menu")}</a></div>
</section>
<style>{CSS}</style>
'''
assert '→' not in HTML and '<script' not in HTML
(H / 'catering-hub-v3-rawhtml.html').write_text(HTML, encoding='utf-8')

# 預覽：加入 Additional CSS 內已有的 ao-qp 樣式（本地 party-quickpick.css）+ 聖誕卡 + 中英切換
base = (H.parent.parent / 'homepage-hero/quickpick/party-quickpick.css').read_text(encoding='utf-8')
XMAS = '''.ao-qp-pop a.is-xmas{background:linear-gradient(180deg,#1E4A3B 0%,#143328 100%);border-color:#C8A24A;color:#F3EBD6 !important}.ao-qp-pop a.is-xmas em{color:#E9D29A}.ao-qp-pop a.is-xmas .ao-qp-pr strong{color:#F0D39A}.ao-qp-pop a.is-xmas .ao-qp-ph{border-bottom-color:#C8A24A}.ao-qp-pop a.is-xmas .ao-qp-btn{background:linear-gradient(135deg,#F0D39A,#C8A24A);color:#143328}.ao-qp-pop a.is-xmas .ao-qp-rank{background:#C8A24A;color:#143328}.ao-qp-series a.is-xmas{background:linear-gradient(135deg,#1E4A3B 0%,#143328 100%);border:1.5px solid #C8A24A}.ao-qp-series a.is-xmas b{color:#fff;font-size:16px}.ao-qp-series a.is-xmas .ao-qp-l2{color:#E9D29A}.ao-qp-series a.is-xmas i{background:rgba(200,162,74,.2)}.ao-qp-series a.is-xmas .ao-qp-limit{background:linear-gradient(135deg,#F0D39A,#C8A24A);color:#143328}
html[lang^="en"] .ao-zh{display:none !important}html:not([lang^="en"]) .ao-en{display:none !important}'''
for lang, fn in (('zh-HK','catering-hub-v3-preview.html'),('en','catering-hub-v3-preview-en.html')):
    (H / fn).write_text(f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>body{{margin:0;padding:20px 12px;font-family:-apple-system,"PingFang HK",sans-serif;background:#fff}}{base}{XMAS}</style></head><body>{HTML}</body></html>', encoding='utf-8')
print('ok', len(HTML))
