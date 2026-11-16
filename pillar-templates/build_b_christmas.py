# -*- coding: utf-8 -*-
"""聖誕到會場景 Landing Option B（酒店網店極簡風：米白底、全襯線、黑色方角標籤、粗體大楷英文眉題）
沿用 build_a_christmas.py 的資料（套餐、價錢、人數表、FAQ），只換版面。輸出 b-christmas.html"""
import pathlib
HERE = pathlib.Path(__file__).parent
src = (HERE / 'build_a_christmas.py').read_text(encoding='utf-8')
D = {'__file__': str(HERE / 'build_a_christmas.py')}
exec(src.split("\nCSS = r'''")[0], D)
SER, PAX, DISH, OCC, FAQ, LD, IMG, WA, C = (D[k] for k in ['SER', 'PAX', 'DISH', 'OCC', 'FAQ', 'LD', 'IMG', 'WA', 'C'])
url, money = D['url'], D['money']
B = 'https://aoaodelivery.com/'

def card(s, a, b, pr, badge=True):
    eb = round(pr * .79)
    return (f'<a class="pc" href="{url(s, a, b)}"><div class="im"><img src="{s["img"]}" alt="{a}-{b}人{s["name"]}聖誕套餐" loading="lazy">'
            f'<img class="alt" src="{s["img2"]}" alt="" loading="lazy">' + ('<span class="tag">EARLY BIRD</span>' if badge else '') + '</div>'
            f'<p class="vd">KITCHEN AO · {s["name"]}</p><p class="nm">{a}–{b} 人聖誕套餐</p>'
            f'<p class="pr"><span class="now">{money(pr)}</span><span class="pe">MEGA79 後 {money(eb)}</span></p></a>')

TOP = [(SER[0], 5, 6, 1928), (SER[1], 8, 10, 2788), (SER[2], 48, 54, 12418)]
TILES = [(SER[0]['img'], '聖誕寶藏箱', '#beef'), (SER[1]['img'], '聖誕金雞獻禮', '#chk'), (SER[2]['img'], '聖誕開箱雙寶', '#dbl'), (IMG['rice'], '2026 聖誕新菜', '#new')]
INCL = ['寶箱煙燻慢煮美國牛翼板肉', '芒果粟子蓉冬日酥盒', '明太子芝士忌廉牛角酥', '西班牙辣肉腸熔岩芝士杯', '紅寶神石榴沙律系列', '皇帝蟹棒蟹肉芒果牛油果沙律',
        '雙重龍蝦三重芝士煲仔鍋飯', '玫瑰醬泡菜海蝦意大利飯', '聖誕馴鹿脆脆開心果朱古力撻', '聖誕神秘加配：聖誕樹芝士火腿拼盤']
LOOK = [(IMG['beef'], [(38, 46, 0), (70, 30, 1)], [(SER[0], 12, 16, 4588), (SER[0], 18, 22, 5888)]),
        (IMG['chk2'], [(45, 55, 0), (22, 30, 1)], [(SER[1], 12, 16, 4248), (SER[1], 26, 30, 7388)]),
        (IMG['chk1'], [(50, 50, 0), (78, 66, 1)], [(SER[2], 63, 68, 15368), (SER[2], 90, 100, 22888)])]
SEO_TXT = {
 'beef': f'聖誕寶藏箱以稀有的美國牛翼板肉為主角，慢煮至五成熟再以煙燻木料炙烤，配八款聖誕新菜，適合 5 至 40 人的家庭聖誕大餐、好友派對及<a href="{B}corporate-catering-hk/">公司聖誕派對到會</a>。全港限量 100 個，送到即可開箱上桌。',
 'chk': '聖誕金雞獻禮以本地原隻黃油雞配南乳醃製，低溫慢煮後高溫炙燒，皮脆肉嫩，再配聖誕玫瑰金巴利汁，中西合璧。由 5-6 人小型聖誕聚會到 35-40 人大型聖誕派對都有合適份量。',
 'dbl': f'聖誕開箱雙寶同時送上原隻黃油雞及寶箱煙燻牛翼板肉兩款主菜，專為 48 至 100 人的公司年終派對、學校及機構聖誕活動而設。如需正式報價及收據，可經<a href="{B}catering-quote-enquiry/">到會報價查詢</a>聯絡我們。',
}

CSS = r'''
.bxl{--bg:#FAFAF5;--ink:#111;--mut:#6b6b66;--ln:#DADAD2;--tile:#ECECE6;--acc:#24453A;background:var(--bg);color:var(--ink);font-family:"Baskerville","Songti TC","Noto Serif TC","PMingLiU",Georgia,serif;font-size:17px;line-height:1.75}
.bxl *{box-sizing:border-box}.bxl h1,.bxl h2,.bxl h3,.bxl p,.bxl li,.bxl td,.bxl summary{font-family:"Baskerville","Songti TC","Noto Serif TC","PMingLiU",Georgia,serif}.bxl button,.bxl input{font-family:inherit}.bxl a{color:inherit}.bxl img{display:block;max-width:100%}
.bxl .k{font-family:"Helvetica Neue","PingFang HK",Arial,sans-serif;font-weight:800;text-transform:uppercase;letter-spacing:.16em}
.bxl .mq{background:#1C1C1C;color:#fff;font-size:11px;overflow:hidden;white-space:nowrap;padding:8px 0}
.bxl .mq div{display:inline-block;padding-left:100%;animation:bxlmq 38s linear infinite}.bxl .mq span{margin-right:80px;letter-spacing:.12em}
@keyframes bxlmq{to{transform:translateX(-100%)}}
.bxl .w{max-width:1320px;margin:0 auto;padding:0 32px}
.bxl .hero{position:relative;height:clamp(420px,70vh,720px);overflow:hidden;background:#000}
.bxl .hero img{width:100%;height:100%;object-fit:cover;opacity:.8}
.bxl .hero .in{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;color:#fff;padding:0 20px}
.bxl .hero .k{font-size:clamp(26px,4.4vw,48px);letter-spacing:.06em;line-height:1.25;margin:0 0 10px;text-shadow:0 2px 18px rgba(0,0,0,.35)}
.bxl .hero h1{font-weight:400;font-size:clamp(17px,2.2vw,22px);margin:0 0 22px;letter-spacing:.08em;color:#fff}
.bxl .bt{display:inline-block;text-decoration:none!important;font-family:"Helvetica Neue","PingFang HK",Arial,sans-serif;font-size:12.5px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;padding:13px 26px;background:#1C1C1C;color:#fff!important;border:1px solid #1C1C1C;transition:.2s}
.bxl .bt:hover{background:transparent;color:#1C1C1C!important}.bxl .bt.gl{background:rgba(0,0,0,.35);border-color:rgba(255,255,255,.35)}.bxl .bt.gl:hover{background:#fff}
.bxl .bt.ln{background:transparent;color:#1C1C1C!important}.bxl .bt.ln:hover{background:#1C1C1C;color:#fff!important}
.bxl .cr{font-size:12.5px;color:var(--mut);padding:18px 0}.bxl .cr a{text-decoration:none}
.bxl .rt{text-align:center;max-width:860px;margin:0 auto;padding:clamp(40px,6vw,72px) 24px}
.bxl .rt h2,.bxl .st{font-weight:400;font-size:clamp(24px,2.8vw,34px);line-height:1.4;margin:0 0 12px;text-align:center}
.bxl .rt p,.bxl .sd{color:var(--mut);font-size:15px;margin:0 auto;max-width:880px;text-align:center}
.bxl .sec{padding:clamp(40px,6vw,88px) 0}
.bxl .g3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:28px;margin-top:36px}
.bxl .g4{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:24px;margin-top:32px}
.bxl .pc{display:block;text-decoration:none;text-align:center}
.bxl .pc .im{position:relative;aspect-ratio:1/1;background:var(--tile);overflow:hidden}
.bxl .pc .im img{width:100%;height:100%;object-fit:cover;transition:opacity .5s,transform 1.2s}.bxl .pc .im .alt{position:absolute;inset:0;opacity:0}
.bxl .pc:hover .im .alt{opacity:1}.bxl .pc:hover .im img{transform:scale(1.03)}
.bxl .tag{position:absolute;right:12px;top:12px;background:#111;color:#fff;font:800 10.5px/1 "Helvetica Neue",Arial,sans-serif;letter-spacing:.1em;padding:7px 9px}
.bxl .vd{font:700 10.5px/1 "Helvetica Neue","PingFang HK",Arial,sans-serif;letter-spacing:.16em;margin:18px 0 8px;color:#333}
.bxl .nm{font-size:16.5px;margin:0 0 6px;line-height:1.5}
.bxl .pr{margin:0;font-size:14px}.bxl .pr .now{font-family:"Helvetica Neue",Arial,sans-serif;font-weight:700;letter-spacing:.06em}.bxl .pr .pe{display:block;color:var(--mut);font-size:13px;background:none;border:0;padding:0;text-align:inherit}
.bxl .mg{display:grid;grid-template-columns:1fr 1fr;gap:16px;max-width:880px;margin:0 auto}
.bxl .mg a{position:relative;display:block;aspect-ratio:1/1;overflow:hidden;background:#000;text-decoration:none}
.bxl .mg img{width:100%;height:100%;object-fit:cover;opacity:.82;transition:transform 1.2s}.bxl .mg a:hover img{transform:scale(1.05)}
.bxl .mg span{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;color:#fff;font-size:clamp(18px,2.4vw,26px);letter-spacing:.06em;text-shadow:0 2px 14px rgba(0,0,0,.45)}
.bxl .look{display:grid;grid-template-columns:44px minmax(0,1fr) minmax(0,300px) 44px;gap:28px;align-items:center;max-width:980px;margin:36px auto 0}
.bxl .lk-im{position:relative;aspect-ratio:1/1;overflow:hidden;background:#000}.bxl .lk-im img{width:100%;height:100%;object-fit:cover}
.bxl .dot{position:absolute;width:26px;height:26px;margin:-13px 0 0 -13px;border-radius:50%;background:rgba(255,255,255,.35);border:0;cursor:pointer;padding:0}
.bxl .dot:after{content:"";position:absolute;inset:8px;border-radius:50%;background:#fff}.bxl .dot.on{background:rgba(255,255,255,.75)}
.bxl .lk-card .pc .im{aspect-ratio:1/1}.bxl .lk-card .bt{margin-top:14px}
.bxl .arw{width:40px;height:40px;border-radius:50%;border:1px solid var(--ln);background:#fff;cursor:pointer;font-size:16px;color:#555}
.bxl .pips{display:flex;gap:4px;justify-content:center;margin-top:10px}.bxl .pips i{width:28px;height:28px;cursor:pointer;position:relative}.bxl .pips i:after{content:'';position:absolute;left:11px;top:11px;width:6px;height:6px;border-radius:50%;background:#bbb}.bxl .pips i.on:after{background:#111}
.bxl .col{border-top:1px solid var(--ln);padding-top:clamp(40px,5vw,72px);margin-top:clamp(40px,5vw,72px)}
.bxl .col h2{font-weight:400;font-size:clamp(26px,3vw,38px);margin:0 0 6px;text-align:left}
.bxl .col .meta{display:flex;justify-content:space-between;align-items:baseline;gap:16px;flex-wrap:wrap;border-bottom:1px solid var(--ln);padding-bottom:14px;font-size:13px;color:var(--mut)}
.bxl .col .sx{color:var(--mut);font-size:15px;max-width:900px;margin:30px 0 0}.bxl .col .sx a{color:var(--ink)}
.bxl .pd{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(28px,5vw,72px);max-width:1080px;margin:0 auto;align-items:start}
.bxl .pd .im{position:relative}.bxl .pd .im img{width:100%;aspect-ratio:1/1;object-fit:cover}
.bxl .pd h2{font-weight:400;font-size:clamp(24px,2.6vw,32px);line-height:1.35;margin:6px 0 8px;text-align:left}
.bxl .pd .p2{font-family:"Helvetica Neue",Arial,sans-serif;font-weight:700;font-size:14px;letter-spacing:.06em;padding-bottom:18px;border-bottom:1px solid var(--ln);margin:0 0 18px}
.bxl .pd .p2 .pe2{color:var(--mut);font-weight:400;margin-left:10px;font-size:13px}
.bxl .pd p,.bxl .pd li{font-size:15px;color:#333}.bxl .pd ul{padding-left:0;list-style:none;margin:6px 0 16px}.bxl .pd li:before{content:"• "}
.bxl .pd .note{color:var(--acc)}
.bxl details{border-top:1px solid var(--ln)}.bxl details:last-of-type{border-bottom:1px solid var(--ln)}
.bxl summary{cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center;gap:14px;padding:16px 2px}
.bxl summary::-webkit-details-marker{display:none}.bxl summary:after{content:"+";font:300 20px/1 Arial,sans-serif}.bxl details[open] summary:after{content:"−"}
.bxl .pd summary{font:800 12px/1.4 "Helvetica Neue","PingFang HK",Arial,sans-serif;letter-spacing:.16em}
.bxl details .bd{padding:0 2px 18px;color:var(--mut);font-size:15px}
.bxl .fq summary{font-size:17.5px}
.bxl .px{width:100%;max-width:880px;margin:30px auto 0;border-collapse:collapse;font-size:15px}
.bxl .px th{font:800 11px/1.4 "Helvetica Neue","PingFang HK",Arial,sans-serif;letter-spacing:.16em;text-align:left;padding:12px 10px;border-bottom:1px solid #111}
.bxl .px td{padding:11px 10px;border-bottom:1px solid var(--ln)}.bxl .px td:nth-child(3){color:var(--mut)}
.bxl .fd{display:flex;gap:0;justify-content:center;margin:26px auto 0;max-width:420px}.bxl .fd input{flex:1;border:1px solid #111;border-right:0;background:transparent;padding:12px 14px;font-size:16px;font-family:inherit}
.bxl .fd .bt{border-radius:0}.bxl #bxl-res{text-align:center;min-height:1.7em;margin:14px 0 0;font-size:15px}
.bxl .dish{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:36px 28px;margin-top:36px}
.bxl .dish .im{aspect-ratio:4/5;background:var(--tile);overflow:hidden}.bxl .dish img{width:100%;height:100%;object-fit:cover}
.bxl .dish h3{font-weight:400;font-size:17px;margin:16px 0 4px;text-align:center}.bxl .dish p{font-size:14px;color:var(--mut);margin:0;text-align:center}
.bxl .mm{display:grid;grid-template-columns:minmax(0,7fr) minmax(0,5fr);gap:clamp(28px,5vw,72px);align-items:center;max-width:1180px;margin:0 auto}
.bxl .mm .pics{position:relative;height:clamp(340px,40vw,520px)}
.bxl .mm .pics img{position:absolute;object-fit:cover}.bxl .mm .pics .a{left:0;top:0;width:62%;height:78%}.bxl .mm .pics .b{right:0;bottom:0;width:52%;height:66%;border:10px solid var(--bg)}
.bxl .mm h2{font-weight:400;font-size:clamp(24px,2.6vw,32px);margin:0 0 14px}.bxl .mm p{color:var(--mut);font-size:15px;margin:0 0 22px}
.bxl .oc{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:0;border-top:1px solid var(--ln);border-bottom:1px solid var(--ln);margin-top:32px}
.bxl .oc div{padding:26px 22px;border-right:1px solid var(--ln)}.bxl .oc div:last-child{border-right:0}
.bxl .oc h3{font-weight:400;font-size:18px;margin:0 0 8px}.bxl .oc p{color:var(--mut);font-size:14px;margin:0 0 14px}
.bxl .oc a{font:800 11px/1 "Helvetica Neue","PingFang HK",Arial,sans-serif;letter-spacing:.16em;text-decoration:underline;text-underline-offset:5px}
.bxl .fb{position:relative;height:clamp(380px,56vh,560px);overflow:hidden;background:#000;color:#fff;text-align:center}
.bxl .fb img{width:100%;height:100%;object-fit:cover;opacity:.62}.bxl .fb .in{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:20px}
.bxl .fb h2{font-weight:400;font-size:clamp(24px,3vw,36px);margin:0 0 10px;color:#fff}.bxl .fb p{margin:0 0 22px;color:#eee;font-size:15px;max-width:560px}
.bxl .nl{text-align:center;padding:clamp(48px,6vw,80px) 24px;border-top:1px solid var(--ln)}
@media(max-width:980px){.bxl .g4{grid-template-columns:repeat(2,minmax(0,1fr))}.bxl .look{grid-template-columns:1fr;max-width:520px}.bxl .look .arw{display:none}.bxl .pd,.bxl .mm{grid-template-columns:1fr}.bxl .oc{grid-template-columns:1fr 1fr}.bxl .oc div:nth-child(2){border-right:0}.bxl .oc div:nth-child(-n+2){border-bottom:1px solid var(--ln)}}
@media(max-width:640px){.bxl .w{padding:0 18px}.bxl .g3.top3{grid-auto-flow:column;grid-template-columns:none;grid-auto-columns:72%;overflow-x:auto;scroll-snap-type:x mandatory;gap:14px;scrollbar-width:none}.bxl .g3.top3 .pc{scroll-snap-align:start}.bxl .col h2{font-size:24px}.bxl .col .meta{justify-content:flex-start;font-size:12.5px;padding-bottom:10px}.bxl .col .meta span:empty{display:none}.bxl .pc .vd{font-size:9.5px;letter-spacing:.1em;margin:12px 0 6px}.bxl .pc .nm{font-size:15px;margin:0 0 2px}.bxl .pr{font-size:13.5px}.bxl .pr .pe{font-size:12px}.bxl .tag{right:8px;top:8px;font-size:9.5px;padding:5px 7px}.bxl .col .sx{font-size:14px;margin-top:22px}.bxl .look{gap:16px}.bxl .lk-card .pc .im{aspect-ratio:4/3}.bxl .lk-card{text-align:center}.bxl .pd h2{font-size:22px}.bxl .pd .vd{font-size:10.5px}.bxl .pd .p2 .pe2{display:block;margin:4px 0 0}.bxl .mm .pics{height:300px}.bxl .fb{height:380px}.bxl .st{font-size:24px}.bxl .sec{padding:44px 0}.bxl .g3{grid-template-columns:1fr 1fr;gap:16px}.bxl .g4{gap:14px}.bxl .mg{gap:8px}.bxl .dish{grid-template-columns:1fr 1fr;gap:24px 14px}.bxl .oc{grid-template-columns:1fr}.bxl .oc div{border-right:0;border-bottom:1px solid var(--ln)}.bxl .px{font-size:13.5px}.bxl .px td,.bxl .px th{padding:9px 6px}.bxl .nm{font-size:15px}}
'''

def look_slide(i, im, dots, prods):
    d = ''.join(f'<button class="dot{" on" if j == 0 else ""}" type="button" style="left:{x}%;top:{y}%" data-p="{j}" aria-label="查看套餐"></button>' for x, y, j in dots)
    cards = ''.join(f'<div class="lc" data-p="{j}"{"" if j == 0 else " hidden"}>{card(*p, badge=False)}<a class="bt" href="{url(p[0], p[1], p[2])}">查看套餐</a></div>' for j, p in enumerate(prods))
    return (f'<div class="ls" data-i="{i}"{"" if i == 0 else " hidden"}><div class="look"><button class="arw" type="button" data-d="-1" aria-label="上一組">‹</button>'
            f'<div class="lk-im"><img src="{im}" alt="{prods[0][0]["name"]}聖誕套餐" loading="lazy">{d}</div><div class="lk-card">{cards}</div>'
            f'<button class="arw" type="button" data-d="1" aria-label="下一組">›</button></div></div>')

def collection(s, crumb=True):
    n = len(s['rows'])
    return (f'<div class="col" id="{s["id"]}"><p class="k" style="font-size:11px;margin:0 0 8px;color:#333">{s["full"]}</p><h2>{s["name"]}</h2>'
            f'<div class="meta"><span>{"首頁 / 聖誕到會 / " + s["name"] if crumb else ""}</span><span>{n} 款套餐 · <a href="{C}{s["slug"]}/">查看系列頁</a></span></div>'
            f'<div class="g{"3" if n % 3 == 0 else "4"}">' + ''.join(card(s, a, b, pr) for a, b, pr in s['rows']) + f'</div><p class="sx">{SEO_TXT[s["id"]]}</p></div>')

page = f'''<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>聖誕到會 2026｜聖誕大餐外賣及派對套餐｜Kitchen AO</title>
<meta name="description" content="Kitchen AO 2026 聖誕到會套餐：5 至 100 人，原隻黃油雞、寶箱煙燻牛翼板肉及八款聖誕新菜，公司聖誕派對及家庭聚會皆宜。11 月 30 日前 MEGA79 七九折。">
<style>body{{margin:0}}{CSS}</style><script type="application/ld+json">{LD}</script></head><body>
<div class="bxl">
<div class="mq"><div>{"".join('<span>聖誕套餐輸入優惠碼 MEGA79 享七九折，優惠至 2026 年 11 月 30 日 23:59　·　平安夜及聖誕節送貨時段有限，請盡早預訂</span>' for _ in range(3))}</div></div>
<div class="hero"><img src="{IMG['chk1']}" alt="聖誕到會 2026：燒南乳香慢煮原隻黃油雞聖誕套餐"><div class="in">
<p class="k">Christmas, Boxed with Care</p><h1>聖誕到會 2026｜聖誕大餐外賣及派對套餐</h1><a class="bt gl" href="#sets">選購聖誕套餐</a></div></div>
<div class="w cr"><a href="{B}">首頁</a> / <a href="#">到會場景</a> / 聖誕到會</div>
<div class="rt"><h2>早鳥輸入 MEGA79，聖誕套餐享七九折</h2><p>優惠至 2026 年 11 月 30 日 23:59<span id="bxl-cd"></span>，於結帳頁面輸入優惠碼即可。</p></div>
<section class="sec" id="top" style="padding-top:0"><div class="w"><h2 class="st">聖誕到會精選推介</h2>
<p class="sd">Kitchen AO 聖誕到會套餐為 5 至 100 人的聖誕聚會而設。原隻主菜配前菜、沙律、意粉及飯和甜品，一份聖誕到會餐單照顧全場，由家庭聖誕大餐、好友派對到公司聖誕派對都合適。</p>
<div class="g3 top3">{"".join(card(*t) for t in TOP)}</div></div></section>
<section class="sec" id="sets" style="padding-top:0"><div class="w"><div class="mg">{"".join(f'<a href="{h}"><img src="{im}" alt="{t}" loading="lazy"><span>{t}</span></a>' for im, t, h in TILES)}</div></div></section>
<section class="sec"><div class="w"><h2 class="st">開箱，就是聖誕</h2><p class="sd">按圖上的圓點，看看每款主菜屬於哪個聖誕套餐。</p>
<div id="bxl-look">{"".join(look_slide(i, *l) for i, l in enumerate(LOOK))}<div class="pips">{"".join(f'<i class="{"on" if i == 0 else ""}" role="button" tabindex="0" aria-label="第 {i + 1} 組"></i>' for i in range(len(LOOK)))}</div></div></div></section>
<section class="sec" style="padding-top:0"><div class="w">{"".join(collection(s) for s in SER)}</div></section>
<section class="sec" style="border-top:1px solid var(--ln)"><div class="w"><div class="pd">
<div class="im"><img src="{IMG['beef']}" alt="寶箱煙燻慢煮美國牛翼板肉" loading="lazy"><span class="tag">EARLY BIRD</span></div>
<div><p class="vd" style="margin-top:0">KITCHEN AO · 全港限量 100 個</p><h2>聖誕寶藏箱．煙燻慢煮美國牛翼板肉盛宴</h2>
<p class="p2">HK$1,928 起<span class="pe2">MEGA79 後 HK$1,523 起</span></p>
<p>下肩胛翼板肉在日式燒肉稱為「羽下肉」或「座布團」，每頭牛僅約 2 至 3 公斤。油花細密均勻，慢煮至五成熟後以煙燻木料高溫炙烤，外層焦香、內裏鎖住肉汁，以復古寶箱盛載，開箱一刻就是全場焦點。</p>
<p class="note">平安夜及聖誕節是全年聖誕訂餐高峰，送貨時段有限，建議盡早預訂。</p>
<p style="margin-bottom:0">套餐包括：</p><ul>{"".join(f"<li>{x}</li>" for x in INCL)}</ul>
<a class="bt" href="#beef">選擇人數</a>
<div style="margin-top:28px"><details><summary>套餐配搭說明</summary><div class="bd">套餐菜式可按喜好自由配搭；部分精選菜式需另加差價，實際價錢以落單頁面選項為準。</div></details>
<details><summary>溫馨提示</summary><div class="bd">煲仔鍋飯一般以原煲盛載；如瓦煲缺貨，會以錫紙盤代替，恕不另行通知。</div></details>
<details><summary>送貨安排</summary><div class="bd">預留至少 30 分鐘緩衝時間；Party Room、辦公室及學校請先確認收貨安排。詳情見<a href="{B}delivery/">送貨需知</a>。</div></details></div></div></div></div></section>
<section class="sec" id="pax" style="border-top:1px solid var(--ln)"><div class="w"><h2 class="st">按人數揀聖誕套餐</h2><p class="sd">輸入出席人數，即時建議合適的聖誕到會套餐。</p>
<div class="fd"><input id="bxl-n" type="number" min="1" inputmode="numeric" placeholder="出席人數"><button class="bt" id="bxl-go" type="button">建議套餐</button></div><p id="bxl-res"></p>
<table class="px"><thead><tr><th>出席人數</th><th>建議套餐</th><th>另一選擇</th></tr></thead><tbody>{"".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for a, b, c in PAX)}</tbody></table></div></section>
<section class="sec" id="new" style="border-top:1px solid var(--ln)"><div class="w"><p class="k" style="text-align:center;font-size:11px;margin:0 0 10px">Xmas Special</p><h2 class="st">2026 聖誕新菜</h2>
<p class="sd">今年聖誕套餐全新加入的前菜、沙律、意粉及飯和甜品。</p>
<div class="dish">{"".join(f'<div><div class="im"><img src="{IMG[k]}" alt="{n}" loading="lazy"></div><h3>{n}</h3><p>{d}</p></div>' for k, n, d in DISH)}</div></div></section>
<section class="sec" style="border-top:1px solid var(--ln)"><div class="w"><div class="mm"><div class="pics"><img class="a" src="{IMG['ris']}" alt="公司聖誕派對到會" loading="lazy"><img class="b" src="{IMG['salad']}" alt="聖誕派對沙律" loading="lazy"></div>
<div><p class="k" style="font-size:11px;margin:0 0 10px">Corporate</p><h2>公司聖誕派對到會</h2><p>部門聚餐、年終派對及客戶活動，按人數配搭聖誕套餐。公司、學校及機構訂購如需正式報價及收據，歡迎聯絡我們。</p>
<a class="bt" href="{B}corporate-catering-hk/">了解更多</a> <a class="bt ln" href="{B}catering-quote-enquiry/">到會報價查詢</a></div></div>
<h2 class="st" id="occ" style="margin-top:clamp(56px,7vw,96px)">聖誕到會推介：按場合揀</h2>
<div class="oc">{"".join(f'<div><h3>{t}</h3><p>{d}</p><a href="{u}">{l}</a></div>' for t, d, u, l in OCC)}</div></div></section>
<section class="fb" id="delivery"><img src="{IMG['tart']}" alt="平安夜及聖誕節到會送貨" loading="lazy"><div class="in"><p class="k" style="font-size:11px;margin:0 0 10px">Delivery</p>
<h2>平安夜及聖誕節送貨安排</h2><p>12 月 24 日及 25 日熱門時段較快額滿，宜盡早確定日期及時間，並預留至少 30 分鐘緩衝。</p><a class="bt gl" href="{B}delivery/">送貨需知</a></div></section>
<section class="sec fq" id="faq"><div class="w" style="max-width:900px"><h2 class="st">聖誕到會常見問題</h2><div style="margin-top:30px">
{"".join(f'<details{" open" if i == 0 else ""}><summary>{q}</summary><div class="bd">{a}</div></details>' for i, (q, a) in enumerate(FAQ))}</div></div></section>
<div class="nl"><h2 class="st">今年聖誕，交給 Kitchen AO</h2><p class="sd" style="margin-bottom:24px">5 至 100 人聖誕到會套餐，WhatsApp 即時查詢。</p>
<a class="bt" href="#sets">選購聖誕套餐</a> <a class="bt ln" href="{WA}" target="_blank" rel="noopener">WhatsApp 查詢</a></div>
</div>
<script>(function(){{var R=document.querySelector('.bxl');
var end=new Date('2026-11-30T23:59:59+08:00').getTime(),cd=document.getElementById('bxl-cd');function t(){{var s=Math.max(0,Math.floor((end-Date.now())/1000));cd.textContent=s?'（尚餘 '+Math.floor(s/86400)+' 天 '+Math.floor(s%86400/3600)+' 小時）':'';}}t();setInterval(t,60000);
var L=document.getElementById('bxl-look'),sl=L.querySelectorAll('.ls'),pp=L.querySelectorAll('.pips i'),cur=0;
function show(i){{cur=(i+sl.length)%sl.length;sl.forEach(function(s,k){{s.hidden=k!==cur}});pp.forEach(function(p,k){{p.className=k===cur?'on':''}});}}
pp.forEach(function(p,k){{p.addEventListener('click',function(){{show(k)}})}});L.querySelectorAll('.arw').forEach(function(b){{b.addEventListener('click',function(){{show(cur+ +b.dataset.d)}})}});
sl.forEach(function(s){{s.querySelectorAll('.dot').forEach(function(d){{d.addEventListener('click',function(){{s.querySelectorAll('.dot').forEach(function(x){{x.classList.toggle('on',x===d)}});s.querySelectorAll('.lc').forEach(function(c){{c.hidden=c.dataset.p!==d.dataset.p}})}})}})}});
var S=[[5,6,'5-6 人套餐（寶藏箱 HK$1,928／金雞獻禮 HK$1,688）'],[8,10,'8-10 人套餐（寶藏箱 HK$3,028／金雞獻禮 HK$2,788）'],[12,16,'12-16 人套餐（寶藏箱 HK$4,588／金雞獻禮 HK$4,248）'],[18,22,'18-22 人套餐（寶藏箱 HK$5,888／金雞獻禮 HK$5,388）'],[26,30,'26-30 人套餐（寶藏箱 HK$7,888／金雞獻禮 HK$7,388）'],[35,40,'35-40 人套餐（寶藏箱 HK$9,888／金雞獻禮 HK$9,288）'],[48,54,'48-54 人開箱雙寶（HK$12,418）'],[63,68,'63-68 人開箱雙寶（HK$15,368）'],[78,85,'78-85 人開箱雙寶（HK$19,548）'],[90,100,'90-100 人開箱雙寶（HK$22,888）']];
function go(){{var n=parseInt(document.getElementById('bxl-n').value,10),r=document.getElementById('bxl-res');if(!n||n<1){{r.textContent='請輸入人數';return;}}if(n>100){{r.textContent='100 人以上請經到會報價查詢聯絡我們';return;}}
for(var i=0;i<S.length;i++){{if(n<=S[i][1]){{r.textContent='建議：'+S[i][2]+(n<S[i][0]&&i>0?'，或 '+S[i-1][0]+'-'+S[i-1][1]+' 人套餐加配單點':'');return;}}}}}}
document.getElementById('bxl-go').addEventListener('click',go);document.getElementById('bxl-n').addEventListener('keydown',function(e){{if(e.key==='Enter')go();}});}})();</script>
</body></html>'''
(HERE / 'b-christmas.html').write_text(page, encoding='utf-8')
print('ok', len(page))
