# -*- coding: utf-8 -*-
"""/catering/ v4（2026-11-21）：方案 B「Cocoa & Gold 品牌啡金」。資料沿用 v3；樣式全部自帶（.aob），唔再靠 Additional CSS 嘅 ao-qp。"""
import sys; from pathlib import Path
H = Path(__file__).parent; sys.path.insert(0, str(H))
import build_catering_hub_v3 as V
from xc_parts import SN, ST, GOSVG, HL
XC_CSS = (H / 'xc_css.txt').read_text(encoding='utf-8')
HOLLY = SN.split('<span class="hl l"')[0] if False else ''
S, TB, b = V.S, V.TB, V.b
IC = {
 '🎄':'M12 3l5 7h-3l4 6H6l4-6H7zM12 16v5', '🎂':'M4 21h16M5 21v-7h14v7M5 17c2 1.5 4-1.5 7 0s5-1.5 7 0M12 14v-3M12 8.5c-.9-.9 0-2 0-3.2.9 1.1 1 2.2 0 3.2z',
 '🧸':'M12 3a5 6 0 1 1 0 12a5 6 0 0 1 0-12zM11 15h2l-1 2zM12 17c0 2-2 2-2 4', '💼':'M3 8h18v11H3zM9 8V5h6v3M3 13h18',
 '🥂':'M8 3h8l-1 7a3 3 0 0 1-6 0zM12 13v7M8 21h8', '🍱':'M3 7h18v12H3zM3 11h18M12 11v8', '🚤':'M3 15h18l-3 5H6zM12 4v11M12 5l6 8h-6',
 '🥗':'M5 20C5 10 11 5 20 5c0 9-5 15-14 15M5 20l8-8', '🧺':'M3 10h18l-2 10H5zM7 10l5-6 5 6M9 14v3M15 14v3'}
def svg(k, w=22): return f'<svg viewBox="0 0 24 24" width="{w}" height="{w}" aria-hidden="true"><path d="{IC[k]}"/></svg>'

def xc(href, ga, t, sm):
    holly = V.HOLLY if hasattr(V, 'HOLLY') else ''
    return (f'<a class="xc" href="{href}"{TB} data-ga="{ga}">{SN}{HL}'
            f'<span class="tt">{ST}<span>{b(*t)}</span>{ST}</span><small>{b(*sm)}</small><span class="go">{b("立即查看","View")}{GOSVG}</span></a>')
occ = ''
for ic, z, e, dz, de, u, c, lim in V.OCC:
    sp = ' sp' if lim else ''
    mk = f'<mark>{b(*lim)}</mark>' if lim else ''
    slug = u.strip('/').split('/')[-1]
    if lim:
        occ += xc(f'{S}{u}', 'hub_occ_christmas', (z, e), ('5 至 100 人・12 月 12 至 27 日供應', '5 to 100 pax・12 to 27 Dec')); continue
    occ += f'<a class="cd{sp}" href="{S}{u}"{TB} data-ga="hub_occ_{slug}"><i>{svg(ic)}</i><span><b>{b(z, e)}</b><small>{b(dz, de)}</small></span>{mk}</a>'
ppl = ''.join(f'<a class="pp" href="{S}/product-category/party-set-by-people/{sl}/"{TB} data-ga="hub_ppl_{g}"><b>{n.replace(" &#8211; ","–")}<small>{b("人"," pax")}</small></b><em>{b(z,e)}</em></a>' for n, sl, z, e, g in V.PPL)
SER = [('/product-category/christmas-party-catering-set/?ao_ref=xmas26_hub','christmas',('聖誕派對到會套餐','Christmas Party Sets'),('限量寶箱牛肉 × 原隻黃油雞','Limited Treasure Box Beef × Whole Chicken'),('聖誕限定','Christmas Special')),
 ('/product-category/party/foot-party/','gourmet',('美食派對 Gourmet Set','Gourmet Set'),('人氣之選・熱食主菜','Popular choice・hot mains'),('人氣','Popular')),
 ('/product-category/party/refreshment-set/','refreshment',('輕食宴會 Refreshment','Refreshment Set'),('會議茶點・開幕酒會','Meetings・opening receptions'),None),
 ('/product-category/party/meat-monster/','meat',('肉食獸套餐','Meat Lovers Set'),('上將海港之選','Harbour City favourite'),None),
 ('/product-category/party/children/','kids',('兒童派對套餐','Kids&#8217; Party Sets'),('兒童生日派對','Children&#8217;s birthday parties'),None),
 ('/product-category/party/set-for-two/','couple',('雙人套餐','Sets for Two'),('二人慶祝・紀念日','Celebrations・anniversaries'),None),
 ('/product-category/party/vegetarians-set/','veg',('「素」味人生','Veggie Delight'),('素食派對套餐','Vegetarian party sets'),None),
 ('/product-category/party/boat-party-set/','boat',('船河派對套餐','Boat Party Sets'),('碼頭交收・方便分發','Pier pick-up・easy to share'),None),
 ('/product-category/party/chill-box/','chill',('Chill 一下野餐盒','Chill Picnic Box'),('野餐・戶外活動','Picnics・outdoor events'),None),
 ('/product-category/party/platter/','platter',('手指食物拼盤','Party Platters'),('Finger Food・Platter','Finger Food・Platter'),None),
 ('/product-category/a-la-carte/','alacarte',('單品 À la carte','À la carte'),('小食・主菜・甜品自由配搭','Mix snacks, mains and desserts'),None),
 ('/product-category/party-supplies/','supplies',('派對用品 Party Supplies','Party Supplies'),('餐具・食物架・派對配件','Tableware・food stands・accessories'),None)]
EMO = ['🎄','⭐','🥂','🍖','🧸','💑','🥗','🚤','🧺','🍢','🍽️','🎉']
ser = xc(f'{S}{SER[0][0]}', 'hub_s_christmas', SER[0][2], SER[0][3]) + ''.join(f'<a class="sr{" sp" if i == 0 else ""}" href="{S}{u}"{TB} data-ga="hub_s_{g}"><i>{EMO[i]}</i><span><b>{b(*n)}</b><small>{b(*d)}</small></span>{f"<mark>{b(*m)}</mark>" if m else ""}</a>' for i, (u, g, n, d, m) in enumerate(SER) if i > 0)

top = V.top  # 5 張卡（聖誕 3 + 平日 2），class ao-hx / ao-hx is-reg
biz_list = ''.join(f'<li data-no-translation><span class="ic">{ic}</span><span class="zh">{z}</span><span class="en">{e}</span></li>' for ic, z, e in V.BIZ_ITEMS)
def biz(tag):
    return f'''<div class="bz"><div class="bw"><span class="bb" role="button" tabindex="0" aria-haspopup="true"><i>💼</i><span class="bt"><b>{b("商務到會 TIPS","Business Catering TIPS")}</b><small>{b("公司活動、年會、酒會及商務餐盒，9 項企業服務一覽","Corporate events, annual dinners, receptions and lunch boxes: 9 services")}</small></span><span class="bm">{b("查看服務","See services")}<em aria-hidden="true"></em></span></span><div class="bp" role="region" aria-label="商務到會服務"><div class="bh"><small>FOR BUSINESS</small><b>{b("企業及商務到會服務","Corporate &amp; Business Catering")}</b></div><ul>{biz_list}</ul><div class="bbt"><a class="bwa" href="{V.WA_BIZ}"{TB} data-ga="hub_biz_whatsapp_{tag}">{b("WhatsApp 聯絡企業客戶專員","WhatsApp our corporate team")}</a><a class="bmo" href="{S}/business-event/"{TB} data-ga="hub_biz_intro_{tag}">{b("商務活動簡介","Business events overview")}</a></div></div></div></div>'''
def tab(n, z, e, en):
    return f'<label for="aoB{n}" class="tb tb{n}"><em>{n}</em><span>{b(z, e)}</span></label>'
PH = 'https://aoaodelivery.com/wp-content/uploads/2025/05/PHOTO-2025-03-14-16-33-30-2'

HTML = f'''<section class="aob" aria-labelledby="aob-title">
<div class="hd"><p class="ey">KITCHEN AO CATERING</p><h2 id="aob-title">{b("按場合揀選到會套餐","Choose Catering by Occasion")}</h2><p class="sb">{b("先揀活動場合，再按人數及預算選擇合適套餐，網上即可下單。","Pick your occasion, then choose a set by headcount and budget, and order online.")}</p></div>
<input class="r r1" type="radio" name="aoB" id="aoB1" checked><input class="r r2" type="radio" name="aoB" id="aoB2"><input class="r r3" type="radio" name="aoB" id="aoB3">
<div class="tabs">{tab(1,"按場合","By Occasion","")}{tab(2,"按人數","By Headcount","")}{tab(3,"按產品系列","By Series","")}</div>
<div class="pn p1"><div class="g3">{occ}</div>{biz("occ")}</div>
<div class="pn p2"><div class="g6">{ppl}</div>{biz("ppl")}</div>
<div class="pn p3"><div class="g3">{ser}</div>{biz("ser")}</div>
<div class="tp"><div class="th"><span>{b("本週 TOP 5 人氣推介","This Week&#8217;s Top 5")}</span><small>CHEF&#8217;S PICKS</small></div><div class="ao-hubx"><div class="ao-qp-pop">{top}</div></div></div>
<div class="hp"><p>{b("仍未決定選擇哪一款？","Still deciding?")}</p><a href="{V.WA}" target="_blank" rel="noopener noreferrer" data-ga="hub_whatsapp">{b("WhatsApp 專人為你配搭餐單","WhatsApp us for a tailored menu")}</a></div>
</section>
<style>@@CSS@@</style>
'''

CSS = '''
html[lang^="en"] .aob .ao-zh{display:none!important}html:not([lang^="en"]) .aob .ao-en{display:none!important}
.aob{--c:#2b1b17;--g:#d4a93a;--g2:#a88445;--cr:#fdfaed;--bg:#F6F0E4;--ln:#eadcc1;--mu:#8a7360;max-width:1180px;margin:0 auto 32px;padding:0 0 34px;background:var(--bg);border-radius:22px;overflow:visible;color:var(--c);font-family:inherit;box-sizing:border-box}
.aob *{box-sizing:border-box}.aob a{text-decoration:none!important}
.aob .hd{position:relative;border-radius:22px 22px 0 0;text-align:center;padding:52px 24px 82px;background:linear-gradient(180deg,rgba(43,27,23,.55) 0%,rgba(43,27,23,.78) 100%),url("@@PH@@-1152x1536.jpeg") center 50%/cover;color:var(--cr)}
.aob .ey{margin:0 0 10px!important;font-size:11px;font-weight:700;letter-spacing:.34em;color:var(--g);text-align:center!important}
.aob h2{margin:0!important;font-family:"Songti TC","Noto Serif TC",serif!important;font-size:32px!important;font-weight:600!important;letter-spacing:.1em!important;line-height:1.35!important;color:var(--cr)!important;text-shadow:0 2px 14px rgba(0,0,0,.35)}
html[lang^="en"] .aob h2{font-family:Baskerville,"Baskerville Old Face",Georgia,serif!important;letter-spacing:.02em!important}
.aob .sb{margin:12px 0 0!important;font-size:15px;color:#f1e4c8;text-align:center!important}
.aob .r,.aob input[type=radio]{position:absolute!important;opacity:0!important;width:1px!important;height:1px!important;margin:0!important;pointer-events:none;-webkit-appearance:none;appearance:none}
.aob .ao-hx{position:relative}
.aob .ao-hcta{padding-top:12px}.aob .ao-hpr{margin-top:14px}
.aob .tabs{position:relative;z-index:2;display:grid;grid-template-columns:repeat(3,1fr);gap:6px;max-width:780px;margin:-34px auto 26px;padding:6px;background:var(--cr);border-radius:999px;box-shadow:0 16px 32px -16px rgba(43,27,23,.55)}
.aob .tb{display:flex;align-items:center;justify-content:center;gap:10px;margin:0!important;padding:13px 8px;border-radius:999px;color:#61443e;cursor:pointer;transition:background .25s,color .25s}
.aob .tb em{display:inline-flex;align-items:center;justify-content:center;width:22px;height:22px;border-radius:50%;background:#efe2c4;color:#61443e;font-style:normal;font-size:11px;font-weight:800}
.aob .tb span{font-size:16px;font-weight:700;letter-spacing:.08em}
.aob .tb:hover{background:#f3e8d2}
.aob .r1:checked~.tabs .tb1,.aob .r2:checked~.tabs .tb2,.aob .r3:checked~.tabs .tb3{background:var(--c);color:#f0d39a}
.aob .r1:checked~.tabs .tb1 em,.aob .r2:checked~.tabs .tb2 em,.aob .r3:checked~.tabs .tb3 em{background:var(--g);color:var(--c)}
.aob .r1:focus-visible~.tabs .tb1,.aob .r2:focus-visible~.tabs .tb2,.aob .r3:focus-visible~.tabs .tb3{outline:2px solid var(--g);outline-offset:2px}
.aob .pn{display:none;padding:0 34px}
.aob .r1:checked~.p1,.aob .r2:checked~.p2,.aob .r3:checked~.p3{display:block;animation:aobIn .3s ease}
@keyframes aobIn{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}
.aob .g3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.aob .g6{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:10px}
.aob .cd,.aob .sr{position:relative;display:flex;align-items:center;gap:14px;padding:18px;background:#fffdf8;border:1px solid var(--ln);border-radius:14px;color:var(--c)!important;transition:border-color .25s,transform .25s,box-shadow .25s}
.aob .cd:hover,.aob .sr:hover{border-color:var(--g);transform:translateY(-2px);box-shadow:0 12px 24px -18px rgba(43,27,23,.55)}
.aob .cd i{flex:0 0 46px;height:46px;display:flex;align-items:center;justify-content:center;border-radius:50%;background:var(--c);color:var(--g)}
.aob .cd i svg{display:block;fill:none;stroke:currentColor;stroke-width:1.4;stroke-linecap:round;stroke-linejoin:round}
.aob .cd span,.aob .sr span{display:flex;flex-direction:column;min-width:0}
.aob .cd b,.aob .sr b{font-size:16px;font-weight:700;line-height:1.35}
.aob .cd small,.aob .sr small{margin-top:2px;font-size:12.5px;color:var(--mu);line-height:1.45}
.aob .sp{background:var(--c);border-color:var(--c)}.aob .sp b{color:var(--cr)}.aob .sp small{color:#cbb994}.aob .cd.sp i{background:var(--g);color:var(--c)}
.aob mark{position:absolute;top:10px;right:10px;padding:2px 9px;border-radius:999px;background:var(--g);color:var(--c);font-size:10.5px;font-weight:800;letter-spacing:.06em;white-space:nowrap}
.aob .sr i{flex:0 0 46px;height:46px;display:flex;align-items:center;justify-content:center;border-radius:50%;background:#f3e8d2;font-style:normal;font-size:21px;line-height:1}
.aob .sr.sp i{background:rgba(212,169,58,.22)}
.aob .sr i img.emoji{width:1em!important;height:1em!important;margin:0!important}
.aob .sr mark{background:#efe2c4;color:#61443e}.aob .sr.sp mark{background:var(--g);color:var(--c)}
.aob .pp{display:flex;flex-direction:column;align-items:center;gap:6px;padding:20px 6px;background:#fffdf8;border:1px solid var(--ln);border-radius:14px;color:var(--c)!important;transition:all .25s}
.aob .pp b{font-size:24px;font-weight:800;line-height:1;white-space:nowrap}.aob .pp b small{margin-left:3px;font-size:12px;color:var(--g2)}
.aob .pp em{font-style:normal;font-size:12px;color:var(--mu);text-align:center}
.aob .pp:hover{background:var(--c);border-color:var(--c);color:#f0d39a!important}.aob .pp:hover em{color:#cbb994}
.aob .bz{display:flex;justify-content:center;margin:20px 0 0}
.aob .bw{position:relative;width:100%;max-width:760px}
.aob .bb{display:flex;align-items:center;gap:14px;width:100%;padding:14px 18px;border-radius:14px;background:#fff;border:1px solid var(--ln);color:var(--c);cursor:url("data:image/png;base64,@@B64@@") 1 1,pointer;user-select:none;transition:border-color .25s,box-shadow .25s}
.aob .bw:hover .bb,.aob .bw:focus-within .bb{border-color:var(--g);box-shadow:0 12px 26px -18px rgba(43,27,23,.55)}
.aob .bb>i{flex:0 0 44px;height:44px;display:flex;align-items:center;justify-content:center;border-radius:12px;background:#f3e8d2;font-style:normal;font-size:20px;line-height:1}
.aob .bb>i img.emoji{width:1em!important;height:1em!important;margin:0!important}
.aob .bt{display:flex;flex-direction:column;min-width:0;text-align:left}
.aob .bt b{font-size:15.5px;font-weight:800;letter-spacing:.06em}
.aob .bt small{margin-top:2px;font-size:12.5px;color:var(--mu);line-height:1.45}
.aob .bm{margin-left:auto;flex:0 0 auto;display:inline-flex;align-items:center;gap:8px;padding-bottom:2px;border-bottom:1px solid var(--g2);font-size:13px;font-weight:700;letter-spacing:.08em;color:#61443e;white-space:nowrap}
.aob .bm em{width:6px;height:6px;border-right:1.5px solid currentColor;border-bottom:1.5px solid currentColor;transform:rotate(45deg) translateY(-2px);transition:transform .25s}
.aob .bw:hover .bm em,.aob .bw:focus-within .bm em{transform:rotate(-135deg)}
.aob .bp{position:absolute;left:50%;top:calc(100% + 12px);z-index:30;width:min(480px,92vw);padding:16px 16px 14px;border-radius:16px;background:#fff;color:var(--c);box-shadow:0 24px 50px rgba(43,27,23,.35);opacity:0;visibility:hidden;transform:translate(-50%,-8px);transition:opacity .22s,transform .22s,visibility .22s;cursor:auto}
.aob .bp::before{content:"";position:absolute;left:0;right:0;top:-14px;height:14px}
.aob .bp::after{content:"";position:absolute;left:50%;top:-7px;width:14px;height:14px;background:#fff;transform:translateX(-50%) rotate(45deg)}
.aob .bw:hover .bp,.aob .bw:focus-within .bp{opacity:1;visibility:visible;transform:translate(-50%,0)}
.aob .bh{text-align:center;margin:0 0 10px;padding:0 0 10px;border-bottom:1px solid var(--ln)}
.aob .bh small{display:block;font-size:13px;font-weight:800;letter-spacing:.32em;color:var(--g2)}
.aob .bh b{display:block;margin-top:4px;font-size:22px;font-weight:800;letter-spacing:.06em}
.aob .bp ul{list-style:none!important;margin:0 0 12px!important;padding:0!important;border:1px solid var(--ln);border-radius:12px;overflow:hidden}
.aob .bp li{display:flex;align-items:center;gap:8px;margin:0!important;padding:6px 12px!important;font-size:14px;line-height:1.45;white-space:nowrap;list-style:none!important}
.aob .bp li:nth-child(odd){background:#faf5ea}.aob .bp li .zh{font-weight:800}.aob .bp li .en{margin-left:auto;min-width:0;overflow:hidden;text-overflow:ellipsis;font-size:12.5px;font-weight:600;color:var(--mu)}
.aob .bbt{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.aob .bbt a{display:flex;align-items:center;justify-content:center;padding:11px 10px;border-radius:999px;font-size:14px;font-weight:800;letter-spacing:.04em;white-space:nowrap;text-align:center;cursor:pointer}
.aob .bwa{background:var(--g);color:var(--c)!important}.aob .bwa:hover{background:var(--c);color:#f0d39a!important}
.aob .bmo{border:1.5px solid var(--c);color:var(--c)!important}.aob .bmo:hover{background:var(--c);color:#fff!important}
.aob .tp{margin:44px 34px 0;padding:34px 18px 20px;position:relative;border-radius:18px;background:#efe5d2;border:1px solid var(--ln)}
.aob .th{position:absolute;left:50%;top:0;transform:translate(-50%,-50%);display:inline-flex;align-items:baseline;gap:10px;padding:10px 26px;border-radius:999px;background:var(--c);color:#f0d39a;white-space:nowrap;box-shadow:0 10px 22px -12px rgba(43,27,23,.7)}
.aob .th span{font-size:18px;font-weight:800;letter-spacing:.08em}.aob .th small{font-size:10.5px;font-weight:700;letter-spacing:.26em;color:var(--g)}
.aob .ao-qp-pop{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:12px;margin:0}
.aob .ao-qp-ph{position:relative;display:block;overflow:hidden}.aob .ao-qp-ph img{display:block;width:100%!important;height:100%!important;object-fit:cover;transition:transform .5s}
.aob .ao-hx:hover .ao-qp-ph img{transform:scale(1.04)}
.aob .ao-qp-rank{position:absolute;left:10px;top:10px;padding:4px 10px;font-size:11.5px;font-weight:800;letter-spacing:.14em}
.aob .ao-qp-pi{display:flex;flex-direction:column;flex:1}
.aob .hp{display:flex;align-items:center;justify-content:center;flex-wrap:wrap;gap:10px 18px;margin:28px 34px 0;padding-top:24px;border-top:1px solid var(--ln)}
.aob .hp p{margin:0!important;font-size:15px;color:#61443e}
.aob .hp a{display:inline-block;padding:13px 30px;border-radius:999px;background:var(--c);color:#f0d39a!important;font-size:15px;font-weight:800;letter-spacing:.04em}
.aob .hp a:hover{background:var(--g);color:var(--c)!important}

/* 商務到會：用返原本藍色 */
.aob .bb{background:linear-gradient(135deg,#2c4a86 0%,#1e2a4a 100%);border-color:#1e2a4a;color:#fff;box-shadow:0 12px 26px -16px rgba(10,20,50,.7)}
.aob .bw:hover .bb,.aob .bw:focus-within .bb{border-color:#8caae6;box-shadow:0 14px 30px -14px rgba(10,20,50,.75),0 0 0 2px rgba(140,170,230,.35)}
.aob .bb>i{background:#fff}
.aob .bt b{color:#fff}.aob .bt small{color:#c4d1ee}
.aob .bm{color:#fff;border-bottom-color:#8caae6}
.aob .bh{border-bottom:2px solid #e3e9f5}.aob .bh small{color:#5b77b3}.aob .bh b{color:#1e2a4a}
.aob .bp ul{border-color:#e3e9f5}.aob .bp li:nth-child(odd){background:#f5f8fd}.aob .bp li+li{border-top:1px solid #edf1f8}
.aob .bp li .zh{color:#1e2a4a}.aob .bp li .en{color:#5b77b3}
.aob .bmo{border-color:#1e2a4a;color:#1e2a4a!important}.aob .bmo:hover{background:#1e2a4a;color:#fff!important}
@media (max-width:1080px){.aob .ao-qp-pop{display:flex;gap:12px;overflow-x:auto;scroll-snap-type:x mandatory;-webkit-overflow-scrolling:touch;padding:4px 2px 10px;scrollbar-width:none}.aob .ao-qp-pop::-webkit-scrollbar{display:none}}
@media (max-width:960px){.aob .g3{grid-template-columns:repeat(2,minmax(0,1fr))}.aob .g6{grid-template-columns:repeat(3,minmax(0,1fr))}}
@media (max-width:640px){
.aob{border-radius:16px}.aob .hd{border-radius:16px 16px 0 0}.aob .hd{padding:38px 16px 68px;background-image:linear-gradient(180deg,rgba(43,27,23,.55) 0%,rgba(43,27,23,.78) 100%),url("@@PH@@-768x1024.jpeg")}
.aob h2{font-size:24px!important;letter-spacing:.06em!important}.aob .sb{font-size:13.5px}
.aob .tabs{margin:-28px 10px 18px;gap:4px;padding:5px}.aob .tb{padding:11px 4px;gap:0}.aob .tb em{display:none}.aob .tb span{font-size:13.5px;letter-spacing:.02em}
.aob .pn{padding:0 12px}.aob .g3{gap:8px}.aob .g6{gap:8px}
.aob .cd,.aob .sr{gap:10px;padding:14px 10px;flex-direction:column;align-items:flex-start}.aob .sr i{flex:0 0 36px;width:36px;height:36px;font-size:17px}
.aob .cd i{flex:0 0 36px;width:36px;height:36px}.aob .cd b,.aob .sr b{font-size:14.5px}.aob .cd small,.aob .sr small{font-size:11.5px}
.aob mark{top:8px;right:8px;font-size:9.5px;padding:2px 7px}
.aob .pp{padding:14px 4px}.aob .pp b{font-size:19px}
.aob .bbt{grid-template-columns:1fr;gap:6px}.aob .bb{gap:10px;padding:12px}.aob .bb>i{flex-basis:38px;height:38px;font-size:17px}.aob .bt b{font-size:14.5px}.aob .bt small{font-size:11.5px}.aob .bm span{display:none}.aob .bm{border:0;padding:0}.aob .bp li{padding:5px 10px!important;font-size:13.5px}.aob .bp li .en{font-size:11.5px}
.aob .tp{margin:40px 10px 0;padding:32px 8px 12px}.aob .th{padding:8px 18px}.aob .th span{font-size:15px}.aob .th small{display:none}
.aob .hp{margin:24px 12px 0;flex-direction:column}.aob .hp a{width:100%;text-align:center}
}
@media (prefers-reduced-motion:reduce){.aob .pn{animation:none!important}.aob *{transition:none!important}}
'''
# TOP 5 卡樣式：沿用 v3（.ao-hubx .ao-hx...），抽出相關規則
import re
v3css = V.CSS
keep = [l for l in v3css.split('\n') if ('.ao-hx' in l or '.ao-hpr' in l or '.ao-hsz' in l or '.ao-htag' in l or '.ao-hgo' in l or '.ao-qp-pop .ao-qp-ph' in l)]
CSS += '\n'.join(keep)
# 聖誕卡用品牌深啡取代純黑
CSS = CSS.replace('background:#111;color:#EDE6D8', 'background:#2b1b17;color:#EDE6D8').replace('.ao-hx .ao-qp-rank{border-radius:0;background:#111', '.ao-hx .ao-qp-rank{border-radius:0;background:#2b1b17')
CSS += '\n' + XC_CSS + '\n.aob .xc small{letter-spacing:.06em!important;line-height:1.5}@media(max-width:640px){.aob .xc small{font-size:11px!important;letter-spacing:.02em!important}}'
CSS = CSS.replace('@@B64@@', V.B64).replace('@@PH@@', PH)
assert '<' not in CSS
OUT = HTML.replace('@@CSS@@', CSS)
assert '→' not in OUT and '<script' not in OUT
(H / 'catering-hub-v4-rawhtml.html').write_text(OUT, encoding='utf-8')
for lang, fn in (('zh-HK','catering-hub-v4-preview.html'),('en','catering-hub-v4-preview-en.html')):
    (H / fn).write_text(f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>body{{margin:0;padding:20px 10px;background:#fff;font-family:-apple-system,"PingFang HK",sans-serif}}</style></head><body>{OUT}</body></html>', encoding='utf-8')
print('ok', len(OUT))
