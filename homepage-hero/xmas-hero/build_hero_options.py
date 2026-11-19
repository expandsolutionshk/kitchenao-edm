# 首頁 Hero 聖誕版：3 個 elegant 方案（圖片維持原狀）
from pathlib import Path
H = Path(__file__).parent
LPZ, LPE = 'https://aoaodelivery.com/catering/christmas/', 'https://aoaodelivery.com/en/catering/christmas/'
DL = lambda l: f"window.dataLayer=window.dataLayer||[];dataLayer.push({{event:'cta_click',cta_label:'{l}'}});"
def b(z, e): return f'<span class="ao-zh" data-no-translation>{z}</span><span class="ao-en" data-no-translation>{e}</span>'
def lp(cls, z, e, lab='xmas_lp'):
    return (f'<a class="{cls} ao-zh" data-no-translation href="{LPZ}" onclick="{DL(lab)}">{z}</a>'
            f'<a class="{cls} ao-en" data-no-translation href="{LPE}" onclick="{DL(lab)}">{e}</a>')
STAR = '<svg class="st" viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.5c.5 4.6 3.9 8 8.5 8.5-4.6.5-8 3.9-8.5 8.5-.5-4.6-3.9-8-8.5-8.5 4.6-.5 8-3.9 8.5-8.5z"/></svg>'
SERIF = '"Songti TC","Noto Serif TC",serif'
BASK = 'Baskerville,"Baskerville Old Face",Georgia,serif'
ICONS = ('<div class="ao-hf ao-hf-fs1"><div class="it"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 21h16M5 21v-7a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v7"/><path d="M5 16c1.2 0 1.2 1 2.3 1s1.2-1 2.4-1 1.2 1 2.3 1 1.2-1 2.3-1 1.2 1 2.4 1 1.1-1 2.3-1"/><path d="M8 12V9M12 12V9M16 12V9"/><path d="M8 6.5c0-.8.8-1.5 0-2.5-.8 1-0 1.7 0 2.5zM12 6.5c0-.8.8-1.5 0-2.5-.8 1 0 1.7 0 2.5zM16 6.5c0-.8.8-1.5 0-2.5-.8 1 0 1.7 0 2.5z"/></svg><b>'
 + b('生日派對到會','Birthday Parties') + '</b><span class="sb">' + b('小型至百人派對','Small to 100+ guests') + '</span></div><div class="it"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="7.5" width="18" height="12.5" rx="1.5"/><path d="M9 7.5V5.5A1.5 1.5 0 0 1 10.5 4h3A1.5 1.5 0 0 1 15 5.5v2M3 12.5h18"/></svg><b>'
 + b('公司活動餐飲','Corporate Catering') + '</b><span class="sb">' + b('年會、會議活動','Annual dinners, meetings') + '</span></div><div class="it"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 17h18M4.5 17a7.5 7.5 0 0 1 15 0"/><path d="M12 9.5V8M10.5 8h3M2.5 20h19"/></svg><b>'
 + b('精緻擺盤到會','Styled Platters') + '</b><span class="sb">' + b('擺盤送到現場','Delivered to your venue') + '</span></div></div>')
H1 = '<h1>' + b('香港到會服務<br><span class="ao-nw">派對・公司活動一站式安排</span>', 'Catering Services in Hong Kong<br>for Parties and Corporate Events') + '</h1>'
DS = '<p class="ao-ds">' + b('Kitchen AO 提供香港到會服務，由精緻擺盤、主打熱食到特色到會套餐，適合公司到會、派對到會、生日派對、家庭聚餐及品牌活動，全港送貨，讓每次聚會都更體面、更方便。',
 'Kitchen AO provides catering services in Hong Kong, from styled platters and signature hot dishes to themed catering sets, for corporate catering, party catering, birthdays, family gatherings and brand events, delivered across Hong Kong.') + '</p>'
CTAS = ('<div class="ao-hero-ctas">'
 f'<a class="ao-hero-btn k" href="https://aoaodelivery.com/product-category/party/" onclick="{DL("view_menu")}">' + b('派對到會套餐','Party Catering Sets') + '</a>'
 f'<a class="ao-hero-btn g ao-zh" data-no-translation href="https://wa.me/85269011987?text=你好，我想查詢 Kitchen AO 到會餐單及報價" target="_blank" rel="noopener noreferrer" onclick="{DL("whatsapp")}">WhatsApp 查詢</a>'
 f'<a class="ao-hero-btn g ao-en" data-no-translation href="https://wa.me/85269011987?text=Hi, I would like to ask about Kitchen AO catering menus and quotes" target="_blank" rel="noopener noreferrer" onclick="{DL("whatsapp")}">WhatsApp Us</a>'
 f'<a class="ao-hero-btn o" href="https://aoaodelivery.com/catering-quote-enquiry/" onclick="{DL("quote_form")}">' + b('專人活動報價查詢','Get an Event Quote') + '</a></div>')
def IMGS(extra=''):
    return ('<div class="ao-hx-r"><div class="ao-hx-frame"><div class="ao-hero-rot">'
     '<img class="ao-hero-img" src="https://aoaodelivery.com/wp-content/uploads/2026/07/catering-hongkong-corporate.jpg" alt="Kitchen AO 到會服務與精緻食物擺設" width="1200" height="1400" fetchpriority="high" decoding="async">'
     '<img class="ao-hero-img ao-hero-img2" src="https://aoaodelivery.com/wp-content/uploads/2023/11/%E7%87%88%E7%AE%B1-05-1024x1024.png" alt="Kitchen AO 到會美食" width="1024" height="1024" loading="lazy" decoding="async">'
     f'</div>{extra}</div></div>')
SCRIPT = '<script>(function(){var en=/^en/i.test(document.documentElement.lang||"");var d=document.currentScript&&document.currentScript.parentNode;if(!d)return;[].forEach.call(d.querySelectorAll(en?".ao-zh":".ao-en"),function(x){x.parentNode.removeChild(x)})})();</script>'

# ---- 三款聖誕元素 ----
A_ROW = lp('ao-xa', f'{STAR}<span class="k">CHRISTMAS 2026</span><span class="t">聖誕到會套餐｜12 月 12 日至 27 日供應</span><span class="l">查看聖誕套餐</span>',
                     f'{STAR}<span class="k">CHRISTMAS 2026</span><span class="t">Christmas Catering｜12 to 27 Dec</span><span class="l">View Christmas Sets</span>')
B_TAG = lp('ao-xb', '<span class="hole"></span><em>Christmas 2026</em><span class="t">聖誕到會套餐</span><span class="d">12 月 12 日至 27 日｜5 至 100 人</span><span class="l">查看聖誕套餐</span>',
                     '<span class="hole"></span><em>Christmas 2026</em><span class="t">Christmas Catering</span><span class="d">12 to 27 Dec｜5 to 100 guests</span><span class="l">View Christmas Sets</span>', 'xmas_lp_tag')
C_TOP = f'<p class="ao-xc-orn"><i></i>{STAR}<em>The Christmas</em>{STAR}<i></i></p>'
SNOW = '<span class="sn" aria-hidden="true">' + ''.join(f'<i class="f{i}"></i>' for i in range(1, 11)) + '</span>'
HOLLY = '<svg viewBox="18 7 31 27" aria-hidden="true"><path class="lf" d="M30 22c-4-1-7-4-9-8 2 0 3-1 3-3 2 1 3 0 4-2 1 2 3 3 5 3-1 2 0 4 1 5-2 0-3 2-4 5z"/><path class="lf" d="M34 22c4-1 8-1 12 1-1 1-1 3 0 4-2 0-3 2-3 4-1-1-3-1-5 0 0-2-2-3-3-4 1-2 0-4-1-5z"/><path class="vn" d="M21 14c3 3 7 6 13 8M46 23c-4 0-8-1-12-1"/><circle class="bc" cx="31" cy="25" r="2.6"/><circle class="bc" cx="35.5" cy="27" r="2.6"/><circle class="bc" cx="31.5" cy="29.8" r="2.6"/></svg>'
FLAKES = ''.join(f'<i class="fk k{i}" aria-hidden="true"><svg viewBox="0 0 20 20"><path d="M10 1v18M2.2 5.5l15.6 9M2.2 14.5l15.6-9M8 2.5l2 2 2-2M8 17.5l2-2 2 2"/></svg></i>' for i in range(1, 6))
SNOW = SNOW.replace('</span>', FLAKES + '</span>', 1)
HL = f'<span class="hl l" aria-hidden="true">{HOLLY}</span><span class="hl r" aria-hidden="true">{HOLLY}</span>'
C_BTN = lp('ao-hero-btn ao-xc-btn', f'{SNOW}{HL}<span class="tt">{STAR}<span>聖誕到會套餐 2026</span>{STAR}</span><small>12 月 12 日至 27 日供應</small><span class="go">立即查看聖誕套餐<svg viewBox="0 0 10 10" aria-hidden="true"><path d="M3.5 1.5 7 5l-3.5 3.5"/></svg></span>', f'{SNOW}{HL}<span class="tt">{STAR}<span>Christmas Catering 2026</span>{STAR}</span><small>Available 12 to 27 Dec</small><span class="go">View Christmas Sets<svg viewBox="0 0 10 10" aria-hidden="true"><path d="M3.5 1.5 7 5l-3.5 3.5"/></svg></span>')

def section(opt, top='', mid='', ctas=CTAS, img_extra=''):
    return (f'<section class="ao-hero ao-hx ao-hx-{opt}"><div class="ao-hero-grid"><div class="ao-hx-l">{top}'
            f'<div class="ao-eb">KITCHEN AO HONG KONG CATERING</div>{H1}{DS}{mid}{ctas}{ICONS}</div>{IMGS(img_extra)}</div>{SCRIPT}</section>')
SEC = {'a': section('a', mid=A_ROW),
       'b': section('b', img_extra=B_TAG),
       'c': section('c', top=C_TOP, ctas=CTAS.replace('<div class="ao-hero-ctas">', '<div class="ao-hero-ctas">' + C_BTN, 1))}

BASE = f'''html[lang^="en"] .ao-hero .ao-zh{{display:none!important}}html:not([lang^="en"]) .ao-hero .ao-en{{display:none!important}}
.ao-hx{{box-sizing:border-box;width:100%;max-width:100%;overflow:hidden;text-align:left;padding:44px 20px;background:#fbf8f3;border-bottom:1px solid #EDE4D3}}.ao-hx *,.ao-hx *:before,.ao-hx *:after{{box-sizing:border-box}}.ao-hx h1,.ao-hx p,.ao-hx .ao-eb{{text-align:left}}
.ao-hx .ao-hero-grid{{max-width:1240px;margin:0 auto;display:grid;grid-template-columns:1.05fr .95fr;gap:40px;align-items:center}}
.ao-hx .ao-eb{{margin:0 0 16px;color:#9A7B2E;font-size:11.5px;font-weight:600;letter-spacing:.3em}}
.ao-hx h1{{margin:0 0 16px;color:#1d1714;font-family:{SERIF};font-size:42px;line-height:1.25;font-weight:600;letter-spacing:.05em}}
html[lang^="en"] .ao-hx h1{{font-family:{BASK};letter-spacing:.005em;font-weight:500}}
.ao-hx .ao-nw{{white-space:nowrap}}
.ao-hx .ao-ds{{margin:0 0 22px;max-width:620px;color:#5d534d;font-size:16.5px;line-height:1.95;text-wrap:pretty}}
.ao-hx .ao-ds a{{color:inherit;text-decoration:none;border-bottom:1px solid #C8A24A}}.ao-hx .ao-ds a:hover{{color:#9A7B2E}}
.ao-hx .ao-hero-ctas{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;max-width:620px;margin:0 0 20px}}
.ao-hx .ao-hero-btn{{display:flex!important;align-items:center;justify-content:center;min-height:50px;box-sizing:border-box;padding:12px 14px;border-radius:999px;text-align:center;white-space:nowrap;text-decoration:none!important;font-size:15px;font-weight:600;letter-spacing:.06em;line-height:1.2;transition:background .3s,color .3s,border-color .3s}}
.ao-hx .ao-hero-btn.k,.ao-hx .ao-hero-btn.g,.ao-hx .ao-hero-btn.o{{min-height:54px;border-radius:0;background:#1d1714;border:1px solid #1d1714;color:#fff!important;font-size:12.5px;font-weight:400;letter-spacing:.24em;text-transform:uppercase}}.ao-hx .ao-hero-btn.k:hover,.ao-hx .ao-hero-btn.g:hover,.ao-hx .ao-hero-btn.o:hover{{border-color:#000;background:#000;color:#E4C77E!important}}
html[lang^="en"] .ao-hx .ao-hero-btn{{white-space:normal;font-size:14px;line-height:1.25;padding:10px 12px}}html[lang^="en"] .ao-hx .ao-hero-btn.k,html[lang^="en"] .ao-hx .ao-hero-btn.g,html[lang^="en"] .ao-hx .ao-hero-btn.o{{font-size:11px;letter-spacing:.16em;white-space:nowrap;padding:10px 8px}}
.ao-hx .st{{width:11px;height:11px;fill:#B8913A;flex:0 0 auto}}
.ao-hx-frame{{position:relative;background:#fff;border-radius:26px;padding:14px;box-shadow:0 20px 40px rgba(40,24,15,.10)}}
.ao-hx .ao-hero-rot{{position:relative}}
.ao-hx .ao-hero-img{{display:block;width:100%;height:680px!important;object-fit:cover;object-position:center top;border-radius:18px}}
.ao-hx .ao-hero-img2{{position:absolute;top:0;left:0;opacity:0;object-fit:contain;background:#F3EEE4;animation:aoHeroFade 12s ease-in-out infinite}}
@keyframes aoHeroFade{{0%,42%{{opacity:0}}50%,92%{{opacity:1}}100%{{opacity:0}}}}
.ao-hf-fs1{{display:grid;grid-template-columns:repeat(3,1fr);max-width:620px;margin:0;background:rgba(255,255,255,.85);border-top:1px solid #1d1714;border-bottom:1px solid #1d1714}}.ao-hf-fs1 .it{{display:flex;flex-direction:column;align-items:center;text-align:center;padding:18px 8px 16px}}.ao-hf-fs1 .it+.it{{border-left:1px solid #E6DDCB}}.ao-hf-fs1 svg{{width:30px;height:30px;fill:none;stroke:#9A7B2E;stroke-width:1.1;stroke-linecap:round;stroke-linejoin:round;margin:0 0 10px}}.ao-hf-fs1 b{{font-size:14.5px;color:#1d1714;font-weight:600;letter-spacing:.14em}}.ao-hf-fs1 .sb{{font-size:12px;color:#8A8378;margin-top:4px;letter-spacing:.06em}}html[lang^="en"] .ao-hf-fs1 b{{letter-spacing:.08em;text-transform:uppercase;font-size:12.5px}}
@media (prefers-reduced-motion:reduce){{.ao-hx .ao-hero-img2{{animation:none}}}}
@media (max-width:960px){{.ao-hx .ao-hero-grid{{grid-template-columns:minmax(0,1fr);gap:0}}.ao-hx .ao-hx-l>*,.ao-hx .ao-hx-r{{min-width:0;max-width:100%}}.ao-hx .ao-hx-l{{display:contents}}.ao-hx .ao-hx-l>*{{order:1}}.ao-hx .ao-hx-r{{order:2;margin:0 0 22px}}.ao-hx .ao-hero-ctas{{order:3}}.ao-hx .ao-hf-fs1{{order:4}}.ao-hx h1{{font-size:34px}}.ao-hx .ao-hero-img{{height:520px!important}}}}
@media (max-width:640px){{.ao-hx{{padding:30px 16px}}.ao-hx h1{{font-size:26px;line-height:1.35}}html[lang^="en"] .ao-hx h1{{font-size:27px}}.ao-hx .ao-ds{{font-size:15px;line-height:1.85}}.ao-hx .ao-hero-ctas{{grid-template-columns:1fr;gap:10px;max-width:none}}.ao-hx .ao-hero-img{{height:420px!important}}.ao-hf-fs1 .it{{padding:14px 4px 12px}}.ao-hf-fs1 svg{{width:26px;height:26px}}.ao-hf-fs1 b{{font-size:12.5px;letter-spacing:.06em}}.ao-hf-fs1 .sb{{font-size:10.5px;letter-spacing:0}}}}
'''
OPT = {
'a': f'''/* A 金線連結 */.ao-xa{{display:flex;align-items:center;gap:12px;max-width:620px;box-sizing:border-box;margin:0 0 22px;padding:14px 2px;border-top:1px solid #C8A24A;border-bottom:1px solid #C8A24A;text-decoration:none!important;color:#1d1714}}
.ao-xa .k{{font-size:10.5px;letter-spacing:.3em;color:#9A7B2E;white-space:nowrap}}.ao-xa .t{{flex:1;font-family:{SERIF};font-size:15.5px;letter-spacing:.06em;color:#1d1714}}html[lang^="en"] .ao-xa .t{{font-family:{BASK};font-size:16px;letter-spacing:.01em}}
.ao-xa .l{{font-size:13.5px;letter-spacing:.08em;color:#1d1714;border-bottom:1px solid #1d1714;padding-bottom:2px;white-space:nowrap;transition:color .3s,border-color .3s}}.ao-xa:hover .l{{color:#9A7B2E;border-color:#9A7B2E}}
@media(max-width:640px){{.ao-xa{{flex-wrap:wrap;gap:6px 10px}}.ao-xa .t{{flex:1 1 100%;order:3;font-size:15px}}.ao-xa .l{{order:2;margin-left:auto}}}}''',
'b': f'''/* B 禮物吊牌 */.ao-xb{{position:absolute;left:34px;bottom:34px;z-index:3;display:flex;flex-direction:column;align-items:flex-start;width:230px;box-sizing:border-box;padding:30px 22px 20px;background:#fbf8f3;border:1px solid #C8A24A;border-radius:4px 4px 4px 4px;box-shadow:0 14px 30px -14px rgba(29,23,20,.45);text-decoration:none!important;color:#1d1714;transform:rotate(-2deg);transition:transform .4s}}
.ao-xb:hover{{transform:rotate(0) translateY(-3px)}}
.ao-xb .hole{{position:absolute;top:11px;left:50%;width:9px;height:9px;margin-left:-5px;border:1px solid #C8A24A;border-radius:50%;background:#fff}}
.ao-xb em{{font-family:{BASK};font-style:italic;font-size:17px;color:#9A7B2E;letter-spacing:.02em}}
.ao-xb .t{{margin:6px 0 4px;font-family:{SERIF};font-size:20px;letter-spacing:.06em}}html[lang^="en"] .ao-xb .t{{font-family:{BASK};font-size:21px;letter-spacing:0}}
.ao-xb .d{{font-size:12px;color:#7a6d63;letter-spacing:.04em}}
.ao-xb .l{{margin-top:14px;font-size:13px;letter-spacing:.1em;border-bottom:1px solid #1d1714;padding-bottom:2px}}.ao-xb:hover .l{{color:#9A7B2E;border-color:#9A7B2E}}
@media(max-width:640px){{.ao-xb{{left:24px;bottom:24px;width:200px;padding:26px 18px 16px}}.ao-xb .t{{font-size:18px}}}}''',
'c': f'''/* C 邀請卡 */.ao-xc-orn{{display:flex;align-items:center;gap:10px;max-width:620px;margin:0 0 18px}}.ao-xc-orn i{{flex:1;height:1px;background:#C8A24A;opacity:.7}}
.ao-xc-orn em{{font-family:{BASK};font-style:italic;font-size:18px;color:#9A7B2E;letter-spacing:.03em;white-space:nowrap}}
.ao-hx-c .ao-hero-ctas{{grid-template-columns:repeat(3,minmax(0,1fr));column-gap:12px;row-gap:14px;margin:6px 0 30px}}
.ao-hx .ao-xc-btn{{grid-column:1/-1;flex-direction:column;gap:4px;min-height:68px;margin-bottom:4px;border-radius:0!important;background:#1d1714;color:#F3E3B8!important;border:1px solid #1d1714;box-shadow:inset 0 0 0 5px #1d1714,inset 0 0 0 6px rgba(200,162,74,.8);font-family:{SERIF};font-size:15.5px;letter-spacing:.14em;font-weight:400}}
html[lang^="en"] .ao-hx .ao-xc-btn{{font-family:{BASK};letter-spacing:.04em;font-size:17px}}
.ao-hx .ao-xc-btn{{position:relative;overflow:hidden;isolation:isolate}}
.ao-hx .ao-xc-btn .tt,.ao-hx .ao-xc-btn small{{position:relative;z-index:2}}
.ao-hx .ao-xc-btn .tt{{display:inline-flex;align-items:center;gap:12px}}
.ao-hx .ao-xc-btn .st{{width:10px;height:10px;fill:#C8A24A;animation:aoXcTw 3.2s ease-in-out infinite}}.ao-hx .ao-xc-btn .tt .st:last-child{{animation-delay:1.6s}}
@keyframes aoXcTw{{0%,100%{{opacity:.35;transform:scale(.7) rotate(0)}}50%{{opacity:1;transform:scale(1.15) rotate(90deg)}}}}
.ao-hx .ao-xc-btn:before{{content:"";position:absolute;inset:6px;z-index:1;pointer-events:none;background:linear-gradient(90deg,transparent 0,rgba(228,199,126,0) 35%,rgba(228,199,126,.9) 50%,rgba(228,199,126,0) 65%,transparent 100%) top/300% 1px no-repeat,linear-gradient(90deg,transparent 0,rgba(228,199,126,0) 35%,rgba(228,199,126,.9) 50%,rgba(228,199,126,0) 65%,transparent 100%) bottom/300% 1px no-repeat;animation:aoXcLine 6s ease-in-out infinite}}
@keyframes aoXcLine{{0%{{background-position:100% 0,0% 100%}}50%{{background-position:0% 0,100% 100%}}100%{{background-position:100% 0,0% 100%}}}}
.ao-hx .ao-xc-btn .sn{{position:absolute;inset:0;z-index:1;pointer-events:none}}
.ao-hx .ao-xc-btn .sn i{{position:absolute;top:-6px;width:3px;height:3px;border-radius:50%;background:#F3E3B8;opacity:0;animation:aoXcSn 7s linear infinite}}
@keyframes aoXcSn{{0%{{opacity:0;transform:translate(0,0)}}15%{{opacity:.8}}85%{{opacity:.5}}100%{{opacity:0;transform:translate(14px,84px)}}}}
.ao-hx .ao-xc-btn .sn .f1{{left:6%;animation-delay:0s}}.ao-hx .ao-xc-btn .sn .f2{{left:15%;width:2px;height:2px;animation-delay:2.6s;animation-duration:8s}}.ao-hx .ao-xc-btn .sn .f3{{left:24%;animation-delay:4.8s}}.ao-hx .ao-xc-btn .sn .f4{{left:34%;width:2px;height:2px;animation-delay:1.3s;animation-duration:9s}}.ao-hx .ao-xc-btn .sn .f5{{left:46%;animation-delay:5.9s}}.ao-hx .ao-xc-btn .sn .f6{{left:57%;width:2px;height:2px;animation-delay:3.4s}}.ao-hx .ao-xc-btn .sn .f7{{left:67%;animation-delay:.7s;animation-duration:8.5s}}.ao-hx .ao-xc-btn .sn .f8{{left:77%;width:2px;height:2px;animation-delay:4.1s}}.ao-hx .ao-xc-btn .sn .f9{{left:86%;animation-delay:2s;animation-duration:7.5s}}.ao-hx .ao-xc-btn .sn .f10{{left:94%;width:2px;height:2px;animation-delay:6.3s}}
.ao-hx .ao-xc-btn{{transition:background .4s,box-shadow .4s}}.ao-hx .ao-xc-btn:hover{{background:#000;color:#fff!important;box-shadow:inset 0 0 0 5px #000,inset 0 0 0 6px #E4C77E,0 10px 24px -12px rgba(200,162,74,.55)}}.ao-hx .ao-xc-btn:hover .st{{fill:#E4C77E}}
@media (prefers-reduced-motion:reduce){{.ao-hx .ao-xc-btn .st,.ao-hx .ao-xc-btn:before,.ao-hx .ao-xc-btn .sn i{{animation:none}}.ao-hx .ao-xc-btn .sn{{display:none}}}}.ao-hx .ao-xc-btn small{{font-family:-apple-system,"PingFang HK",sans-serif;font-size:11px;letter-spacing:.14em;color:#C8A24A;font-weight:400}}

@media(max-width:640px){{.ao-xc-orn em{{font-size:16px}}.ao-hx-c .ao-hero-ctas{{grid-template-columns:1fr;row-gap:10px;margin:0 0 26px}}.ao-hx .ao-xc-btn{{margin-bottom:6px}}}}

.ao-hx .ao-xc-btn .hl{{position:absolute;top:50%;z-index:2;width:44px;height:38px;margin-top:-19px;pointer-events:none}}.ao-hx .ao-xc-btn .hl.l{{left:20px;transform-origin:30% 70%;animation:aoXcSw 5s ease-in-out infinite}}.ao-hx .ao-xc-btn .hl.r{{right:20px;transform:scaleX(-1);transform-origin:70% 70%;animation:aoXcSwR 5s ease-in-out infinite;animation-delay:-2.5s}}
.ao-hx .ao-xc-btn .hl svg{{width:100%;height:100%;overflow:visible}}.ao-hx .ao-xc-btn .hl .lf{{fill:rgba(200,162,74,.18);stroke:#C8A24A;stroke-width:1;stroke-linejoin:round}}.ao-hx .ao-xc-btn .hl .vn{{fill:none;stroke:#C8A24A;stroke-width:.7;opacity:.8}}.ao-hx .ao-xc-btn .hl .bc{{fill:#9E2B25;stroke:#E4C77E;stroke-width:.6}}
@keyframes aoXcSw{{0%,100%{{transform:rotate(-4deg)}}50%{{transform:rotate(4deg)}}}}@keyframes aoXcSwR{{0%,100%{{transform:scaleX(-1) rotate(-4deg)}}50%{{transform:scaleX(-1) rotate(4deg)}}}}
.ao-hx .ao-xc-btn .sn i{{width:4px;height:4px}}.ao-hx .ao-xc-btn .sn .fk{{width:12px;height:12px;background:none;border-radius:0;animation-name:aoXcFk;animation-duration:9s}}.ao-hx .ao-xc-btn .sn .fk svg{{width:100%;height:100%;fill:none;stroke:#F3E3B8;stroke-width:1.2;stroke-linecap:round}}
@keyframes aoXcFk{{0%{{opacity:0;transform:translate(0,0) rotate(0)}}15%{{opacity:.75}}85%{{opacity:.45}}100%{{opacity:0;transform:translate(-12px,90px) rotate(180deg)}}}}
.ao-hx .ao-xc-btn .sn .k1{{left:20%;animation-delay:1s}}.ao-hx .ao-xc-btn .sn .k2{{left:40%;width:9px;height:9px;animation-delay:4.5s}}.ao-hx .ao-xc-btn .sn .k3{{left:62%;animation-delay:2.8s;animation-duration:10s}}.ao-hx .ao-xc-btn .sn .k4{{left:80%;width:9px;height:9px;animation-delay:6.5s}}.ao-hx .ao-xc-btn .sn .k5{{left:52%;width:8px;height:8px;animation-delay:8s}}
.ao-hx .ao-xc-btn:hover .hl .lf{{fill:rgba(228,199,126,.3);stroke:#E4C77E}}
@media(max-width:640px){{.ao-hx .ao-xc-btn .hl{{width:34px;height:29px;margin-top:-15px}}.ao-hx .ao-xc-btn .hl.l{{left:14px}}.ao-hx .ao-xc-btn .hl.r{{right:14px}}}}
@media(max-width:360px){{.ao-hx .ao-xc-btn .hl{{width:28px;height:24px;margin-top:-12px}}}}
@media (prefers-reduced-motion:reduce){{.ao-hx .ao-xc-btn .hl{{animation:none!important}}}}

.ao-hx .ao-xc-btn{{min-height:96px;padding-top:14px;padding-bottom:14px;cursor:pointer;animation:aoXcGlow 2.8s ease-in-out infinite}}
@keyframes aoXcGlow{{0%,100%{{box-shadow:inset 0 0 0 5px #1d1714,inset 0 0 0 6px rgba(200,162,74,.8),0 0 0 0 rgba(200,162,74,0)}}50%{{box-shadow:inset 0 0 0 5px #1d1714,inset 0 0 0 6px rgba(228,199,126,1),0 0 0 6px rgba(200,162,74,.18)}}}}
.ao-hx .ao-xc-btn .go{{position:relative;z-index:2;display:inline-flex;align-items:center;gap:6px;margin-top:8px;padding:7px 16px 7px 18px;background:#C8A24A;color:#111;border-radius:999px;font-family:-apple-system,"PingFang HK","Helvetica Neue",sans-serif;font-size:12.5px;font-weight:600;letter-spacing:.12em;line-height:1;transition:background .3s}}
.ao-hx .ao-xc-btn .go svg{{width:10px;height:10px;fill:none;stroke:#111;stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round;animation:aoXcNudge 1.4s ease-in-out infinite}}
@keyframes aoXcNudge{{0%,100%{{transform:translateX(0)}}50%{{transform:translateX(4px)}}}}
.ao-hx .ao-xc-btn:hover .go{{background:#E4C77E}}
.ao-hx .ao-xc-btn:hover{{animation:none}}
html[lang^="en"] .ao-hx .ao-xc-btn .go{{letter-spacing:.08em;font-size:12px}}
@media(max-width:640px){{.ao-hx .ao-xc-btn{{min-height:100px}}.ao-hx .ao-xc-btn .go{{font-size:12px;padding:7px 14px 7px 16px}}}}
@media (prefers-reduced-motion:reduce){{.ao-hx .ao-xc-btn,.ao-hx .ao-xc-btn .go svg{{animation:none}}}}
/* 響應式 */
@media (min-width:961px) and (max-width:1200px){{.ao-hx .ao-hero-grid{{gap:28px}}.ao-hx h1{{font-size:clamp(30px,3.3vw,40px)}}.ao-hx .ao-hero-btn.k,.ao-hx .ao-hero-btn.g,.ao-hx .ao-hero-btn.o{{letter-spacing:.12em;padding:10px 8px;white-space:normal;line-height:1.35}}html[lang^="en"] .ao-hx .ao-hero-btn.k,html[lang^="en"] .ao-hx .ao-hero-btn.g,html[lang^="en"] .ao-hx .ao-hero-btn.o{{letter-spacing:.08em;white-space:normal;font-size:10.5px}}.ao-hx .ao-hero-img{{height:600px!important}}}}
@media (max-width:960px){{.ao-hx .ao-hero-grid{{max-width:680px}}.ao-hx .ao-ds,.ao-hx .ao-hero-ctas,.ao-hf-fs1,.ao-xc-orn{{max-width:none}}}}
@media (max-width:640px){{.ao-hx h1{{font-size:clamp(21px,6.9vw,26px)}}html[lang^="en"] .ao-hx h1{{font-size:clamp(19px,5.7vw,27px)}}.ao-hx .ao-hero-img{{height:auto!important;aspect-ratio:6/7}}.ao-hx .ao-hero-img2{{height:100%!important}}.ao-hx-frame{{padding:10px;border-radius:20px}}.ao-hx .ao-hero-img{{border-radius:14px}}.ao-hx .ao-xc-btn .tt{{gap:9px}}html[lang^="en"] .ao-hx .ao-xc-btn{{font-size:16px}}.ao-hx .ao-hero-btn.k,.ao-hx .ao-hero-btn.g,.ao-hx .ao-hero-btn.o{{min-height:50px}}}}
@media (max-width:440px){{.ao-hx .ao-nw{{white-space:normal}}.ao-hx h1{{font-size:clamp(20px,6.3vw,26px)}}}}
@media (max-width:360px){{.ao-hx{{padding:26px 12px}}.ao-hx .ao-eb{{letter-spacing:.2em;font-size:10.5px}}.ao-xc-orn em{{font-size:15px}}.ao-hf-fs1 b{{font-size:11.5px;letter-spacing:.02em}}}}
'''}

def raw(o): return SEC[o] + f'\n<style>\n{BASE}{OPT[o]}\n</style>\n'
for o in 'abc':
    r = raw(o); assert '船河' not in r and '→' not in r and '聖誕大餐' not in r and '<' not in (BASE+OPT[o])
    (H / f'hero-xmas-option-{o}-rawhtml.html').write_text(r, encoding='utf-8')
LBL = {'a': ('A｜金線連結', '在簡介和按鈕之間加一條上下金色細線的聖誕連結列，最低調。'),
       'b': ('B｜禮物吊牌', '在圖片左下角掛一張米白禮物吊牌，像真實包裝上的 gift tag。'),
       'c': ('C｜邀請卡', '頂部加「The Christmas Edition」金線裝飾，按鈕上方加一個黑底金邊的聖誕按鈕，像晚宴邀請卡。')}
css_all = BASE + ''.join(OPT.values())
body = ''.join(f'<div class="lb"><b>{LBL[o][0]}</b><span>{LBL[o][1]}</span></div>{SEC[o]}' for o in 'abc')
for lang, fn in (('zh-HK', 'Hero聖誕-三款-zh.html'), ('en', 'Hero聖誕-三款-en.html')):
    (H / fn).write_text(f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>首頁 Hero 聖誕版 3 款</title><style>body{{margin:0;font-family:-apple-system,"PingFang HK",sans-serif;background:#fff}}.lb{{position:sticky;top:0;z-index:9;display:flex;gap:14px;align-items:baseline;padding:12px 20px;background:#1d1714;color:#fff;font-size:13px}}.lb b{{color:#E4C77E;font-size:15px;letter-spacing:.06em;white-space:nowrap}}.lb span{{color:#d8cfbf}}{css_all}</style></head><body>{body}</body></html>', encoding='utf-8')
print('ok')
