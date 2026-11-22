# Kitchen AO 首頁「點解客人揀 / 甚麼是到會服務 / 客戶真實評價」兩個方案
import os
U='https://aoaodelivery.com/wp-content/uploads/'
F=[('2025/04/person_14933728-150x150.png','酒店級廚師團隊','由經驗廚師團隊主理，重視食材、味道與賣相，令每份到會餐點更有水準。','適合重視質素與形象的聚會場合'),
('2025/04/salad_649363-150x150.png','靈活客製餐單','可選預設套餐，亦可按活動形式加入單點美食，自由組合更貼近實際需要。','更方便配合人數、預算與口味'),
('2025/04/technical-support_3222533-150x150.png','專人準時送遞','由團隊安排送餐流程，重視時間管理，務求按預定時段將餐點送達。','重要場合更安心，減少臨場壓力'),
('2025/04/lunch-box_3101638-150x150.png','一站式派對配套','除咗餐飲選擇，亦可配搭部分派對用品與加配項目，安排更完整方便。','適合想一次過處理活動細節的客人')]
W=[('豐富餐單','由小食、主菜到甜品，配搭更靈活。'),('準時送達','按預訂時間送到活動場地，安排更安心。'),('適合多種場合','派對、商務午餐、會議茶點及節日聚會都適合。')]
R=[('Excellent service and food! Thank you KitchenAO。','Sinyi Chu','生日派對客戶'),
('公司活動當日準時送達，包裝整齊，方便同事自取，整體感覺專業又省心，之後都會再回購。','黃先生','公司活動餐飲客戶'),
('餐單配搭夠彈性，我哋按人數再加配單點小食就已經好夠，朋友都話方便又好食，整體體驗幾滿意。','林小姐','聚會到會客戶')]
GURL='https://maps.app.goo.gl/YvZdM4HqFCP7Pw9p6?g_st=ic'
BADGE=('<img class="bd" src="'+U+'2024/09/1badge-1-600x259.png" srcset="'+U+'2024/09/1badge-1-300x129.png 300w, '+U+'2024/09/1badge-1-600x259.png 600w" '
 'sizes="(max-width:480px) 80vw, 300px" width="300" height="129" loading="lazy" decoding="async" alt="酒店級廚師主理・航空級可重用盒・三層保溫勁暖・最多KOL自費推薦到會">')
def ic(p,t): return '<img class="ic" src="'+U+p+'" width="150" height="150" loading="lazy" decoding="async" alt="'+t+'">'
SERIF='"Noto Serif TC","Songti TC","Source Han Serif TC","PMingLiU",serif'
STAR='<span class="st" aria-label="5 星">★★★★★</span>'

# ---------- 方案一：酒店信箋（象牙白、左右編排） ----------
c1='''<style>
.aow1{--g:#9a7b4f;--gd:#c9a45c;--ln:#e6dccb;--ink:#1a1816;font-size:15px;line-height:1.75;color:#4a4540}
.aow1 *{box-sizing:border-box;border-radius:0}
.aow1 .wrap{max-width:1180px;margin:0 auto;padding:76px 24px}
.aow1 .ey{font-size:12px;letter-spacing:.28em;color:var(--g);text-transform:uppercase;margin:0 0 14px}
.aow1 h2{font-family:SERIF;font-weight:600;font-size:34px;line-height:1.3;color:var(--ink);margin:0 0 16px;letter-spacing:.04em}
.aow1 h3{font-family:SERIF;font-weight:600;font-size:20px;color:var(--ink);margin:0 0 8px;letter-spacing:.04em}
.aow1 p{margin:0}
.aow1 .why{background:#faf7f1}
.aow1 .g2{display:grid;grid-template-columns:minmax(260px,1fr) 2fr;gap:64px;align-items:start}
.aow1 .lead{color:#6b645b;max-width:340px}
.aow1 .bd{display:block;width:100%;max-width:300px;height:auto;margin:34px 0 0}
.aow1 .fx{display:grid;grid-template-columns:1fr 1fr;column-gap:48px}
.aow1 .f{border-top:1px solid var(--ln);padding:28px 0 32px;display:grid;grid-template-columns:52px 1fr;column-gap:20px}
.aow1 .f .ic{width:44px;height:44px;object-fit:contain;margin-top:4px}
.aow1 .no{display:block;font-family:SERIF;font-size:13px;color:var(--gd);letter-spacing:.2em;margin-bottom:6px}
.aow1 .nt{margin-top:12px;font-size:13px;color:var(--g);display:flex;align-items:center;gap:10px}
.aow1 .nt:before{content:"";width:18px;height:1px;background:var(--gd);flex:0 0 18px}
.aow1 .wc{margin-top:56px;background:#fff;border:1px solid var(--ln);display:grid;grid-template-columns:1fr 2fr}
.aow1 .wc .df{padding:40px;border-right:1px solid var(--ln)}
.aow1 .wc .df h2{font-size:26px}
.aow1 .wc .df p{color:#6b645b}
.aow1 .wc ul{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,1fr)}
.aow1 .wc li{padding:40px 28px;border-left:1px solid var(--ln)}
.aow1 .wc li:first-child{border-left:0}
.aow1 .wc li h3{font-size:18px}
.aow1 .wc li p{font-size:14px;color:#6b645b}
.aow1 .rev{background:#fff}
.aow1 .sc{border-top:1px solid var(--ln);margin-top:26px;padding-top:26px}
.aow1 .big{font-family:SERIF;font-size:64px;line-height:1;color:var(--ink)}
.aow1 .big small{font-size:20px;color:#8c857b;margin-left:6px}
.aow1 .st{color:var(--gd);letter-spacing:.18em;font-size:15px}
.aow1 .sc .st{display:block;margin:12px 0 4px;font-size:18px}
.aow1 .sc .lb{font-size:13px;color:#8c857b;letter-spacing:.08em}
.aow1 a.btn{display:inline-block;margin-top:24px;background:#1a1816;color:#E4C77E!important;text-decoration:none!important;padding:14px 26px;font-size:13px;font-weight:700;letter-spacing:.22em;border:1px solid #1a1816;transition:background .25s,color .25s}
.aow1 a.btn:hover{background:#E4C77E;color:#1a1816!important;border-color:#E4C77E}
.aow1 .qs{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.aow1 .q{border:1px solid var(--ln);padding:30px 26px 26px;display:flex;flex-direction:column;background:#fff}
.aow1 .q:before{content:"\\201C";font-family:SERIF;font-size:54px;line-height:.6;color:var(--gd);height:26px}
.aow1 .q p{flex:1;margin:10px 0 22px;color:#3d3833}
.aow1 .q .who{border-top:1px solid var(--ln);padding-top:16px}
.aow1 .q b{display:block;font-family:SERIF;font-weight:600;color:var(--ink);letter-spacing:.06em}
.aow1 .q i{font-style:normal;font-size:12px;color:#8c857b;letter-spacing:.08em}
.aow1 .q .st{font-size:12px;margin-bottom:6px;display:block}
@media(max-width:1024px){.aow1 .g2{grid-template-columns:1fr;gap:36px}.aow1 .lead{max-width:none}.aow1 .qs{grid-template-columns:1fr}.aow1 .wc{grid-template-columns:1fr}.aow1 .wc .df{border-right:0;border-bottom:1px solid var(--ln)}}
@media(max-width:680px){.aow1 .wrap{padding:56px 20px}.aow1 h2{font-size:28px}.aow1 .fx{grid-template-columns:1fr}.aow1 .wc ul{grid-template-columns:1fr}.aow1 .wc li{border-left:0;border-top:1px solid var(--ln);padding:24px}.aow1 .wc li:first-child{border-top:0}.aow1 .wc .df{padding:28px 24px}.aow1 .bd{max-width:260px}}
</style>'''.replace('SERIF',SERIF)
h=['<section class="aow1"><div class="why"><div class="wrap"><div class="g2"><div>',
 '<p class="ey">Why Kitchen AO</p><h2>點解客人揀 Kitchen AO</h2>',
 '<p class="lead">由食材、出品到配送安排，我哋希望每一個重要場合都更安心、更體面。</p>',BADGE,'</div><div class="fx">']
for n,(p,t,d,nt) in enumerate(F,1):
    h.append('<div class="f">'+ic(p,t)+'<div><span class="no">0%d</span><h3>%s</h3><p>%s</p><p class="nt">%s</p></div></div>'%(n,t,d,nt))
h.append('</div></div><div class="wc"><div class="df"><p class="ey">Catering</p><h2>甚麼是到會服務？</h2><p>到會服務是按活動需要，將預先準備好的美食準時送到指定地點，適合派對、公司活動、會議及家庭聚會。</p></div><ul>')
for t,d in W: h.append('<li><h3>%s</h3><p>%s</p></li>'%(t,d))
h.append('</ul></div></div></div><div class="rev"><div class="wrap"><div class="g2"><div>')
h.append('<p class="ey">Guest Reviews</p><h2>客戶真實評價</h2><p class="lead">來自派對聚會、公司活動及商務餐飲客戶的真實回饋，讓你更放心安排重要場合。</p>')
h.append('<div class="sc"><div class="big">4.8<small>/ 5</small></div>'+STAR+'<span class="lb">Google 商戶評價</span><br><a class="btn" href="'+GURL+'" target="_blank" rel="noopener">查看 Google 評論</a></div></div><div class="qs">')
for t,n,k in R: h.append('<div class="q"><p>%s</p><div class="who">%s<b>%s</b><i>%s</i></div></div>'%(t,STAR,n,k))
h.append('</div></div></div></div></section>')
o1=c1+''.join(h)

U2=['https://aoaodelivery.com/product-category/party/','https://aoaodelivery.com/product-category/party/platter/','https://aoaodelivery.com/product-category/a-la-carte/']
W2=[('到會套餐','按人數揀現成套餐，主菜、小食同甜品已經配好。'),('Finger Food 小食','一口大小，企住食都方便，適合酒會及派對。'),('單點加配','按口味再加主菜、甜品或飲品，份量更啱心水。')]
NT2=['質素・形象兼顧','人數・預算・口味任配','準時送達・安心省時','餐飲・派對用品一次搞掂']
# ---------- 方案二：黑金禮賓（置中、評價黑底） ----------
c2='''<style>
.aow2{--g:#9a7b4f;--gd:#c9a45c;--gl:#E4C77E;--ln:#e6dccb;--ink:#1a1816;font-size:15px;line-height:1.75;color:#4a4540}
.aow2 *{box-sizing:border-box;border-radius:0}
.aow2 .wrap{max-width:1180px;margin:0 auto;padding:80px 24px}
.aow2 .ey{font-size:12px;letter-spacing:.3em;color:var(--g);text-transform:uppercase;margin:0 0 14px}
.aow2 h2{font-family:SERIF;font-weight:600;font-size:36px;line-height:1.3;color:var(--ink);margin:0 0 16px;letter-spacing:.05em}
.aow2 h3{font-family:SERIF;font-weight:600;font-size:19px;color:var(--ink);margin:0 0 10px;letter-spacing:.05em}
.aow2 p{margin:0}
.aow2 .hd{text-align:center;max-width:640px;margin:0 auto}
.aow2 .hd p.sub{color:#6b645b}
.aow2 .hd p.sub span{display:block}
.aow2 .hon{display:flex;align-items:center;justify-content:center;gap:28px;margin:34px auto 0}
.aow2 .hon:before,.aow2 .hon:after{content:"";height:1px;background:var(--ln);flex:1;max-width:220px}
.aow2 .bd{width:300px;max-width:70vw;height:auto;display:block}
.aow2 .fx{display:grid;grid-template-columns:repeat(4,1fr);margin-top:52px;border-top:1px solid var(--ln);border-bottom:1px solid var(--ln)}
.aow2 .f{text-align:center;padding:40px 26px;border-left:1px solid var(--ln);display:flex;flex-direction:column}
.aow2 .f:first-child{border-left:0}
.aow2 .f .ic{width:48px;height:48px;object-fit:contain;display:block;margin:0 auto 20px}
.aow2 .f p{font-size:14px;color:#6b645b}
.aow2 .nt{margin-top:auto!important;padding-top:16px;border-top:1px solid var(--ln);font-size:14px!important;font-weight:600;letter-spacing:.12em;color:var(--g)!important}
.aow2 .f>p:not(.nt){margin-bottom:18px}
.aow2 .wc{margin-top:56px;background:#f6f1e7;display:grid;grid-template-columns:5fr 7fr;gap:48px;padding:48px 52px;align-items:center}
.aow2 .wc h2{font-size:28px}
.aow2 .wc li h3 a.hl{color:inherit!important;text-decoration:none!important;border-bottom:1px solid var(--gd);padding-bottom:2px;transition:color .25s,border-color .25s}
.aow2 .wc li h3 a.hl:hover{color:var(--g)!important;border-color:var(--g)}
.aow2 .wc .df p{color:#5e574e}
.aow2 .wc ol{list-style:none;margin:0;padding:0;counter-reset:w}
.aow2 .wc li{counter-increment:w;display:grid;grid-template-columns:48px 1fr;align-items:baseline;padding:16px 0;border-top:1px solid #e1d6c3}
.aow2 .wc li:first-child{border-top:0}
.aow2 .wc li:before{content:counter(w,upper-roman);font-family:SERIF;color:var(--gd);font-size:18px;letter-spacing:.1em}
.aow2 .wc li h3{display:inline;font-size:17px;margin-right:12px}
.aow2 .wc li span{font-size:14px;color:#5e574e}
.aow2 .rev{background:#111;color:#d9d2c5}
.aow2 .rev .ey{color:var(--gd)}
.aow2 .rev h2{color:#fff}
.aow2 .rev .hd p.sub{color:#b9b1a3}
.aow2 .st{color:var(--gl);letter-spacing:.2em}
.aow2 .rt{display:flex;align-items:center;justify-content:center;flex-wrap:wrap;gap:18px 26px;margin:34px 0 0}
.aow2 .big{font-family:SERIF;font-size:56px;line-height:1;color:var(--gl)}
.aow2 .big small{font-size:18px;color:#8f8879;margin-left:6px}
.aow2 .rt .lb{font-size:13px;color:#b9b1a3;letter-spacing:.1em;display:block}
.aow2 .rt .st{font-size:18px}
.aow2 a.btn{display:inline-block;border:1px solid var(--gl);color:var(--gl)!important;text-decoration:none!important;padding:13px 26px;font-size:13px;font-weight:700;letter-spacing:.22em;transition:background .25s,color .25s}
.aow2 a.btn:hover{background:var(--gl);color:#111!important}
.aow2 .qs{display:grid;grid-template-columns:repeat(3,1fr);margin-top:52px;border-top:1px solid rgba(228,199,126,.28)}
.aow2 .q{padding:36px 30px 6px;border-left:1px solid rgba(228,199,126,.28);display:flex;flex-direction:column}
.aow2 .q:first-child{border-left:0}
.aow2 .q .st{font-size:13px}
.aow2 .q p{flex:1;font-family:SERIF;font-size:16px;line-height:1.85;color:#f1ece3;margin:14px 0 22px}
.aow2 .q b{display:block;color:#fff;font-weight:600;letter-spacing:.06em}
.aow2 .q i{font-style:normal;font-size:12px;color:#8f8879;letter-spacing:.1em}
@media(max-width:1024px){.aow2 .fx{grid-template-columns:1fr 1fr}.aow2 .f:nth-child(3){border-left:0}.aow2 .f:nth-child(n+3){border-top:1px solid var(--ln)}.aow2 .wc{grid-template-columns:1fr;gap:20px;padding:40px}.aow2 .qs{grid-template-columns:1fr}.aow2 .q{border-left:0;border-top:1px solid rgba(228,199,126,.28);padding:30px 4px}.aow2 .q:first-child{border-top:0}}
@media(max-width:680px){.aow2 .wrap{padding:60px 20px}.aow2 h2{font-size:28px}.aow2 .fx{grid-template-columns:1fr}.aow2 .f{border-left:0!important;border-top:1px solid var(--ln);padding:30px 12px}.aow2 .f:first-child{border-top:0}.aow2 .wc{padding:30px 22px}.aow2 .hon{gap:14px}.aow2 .bd{width:260px}}
</style>'''.replace('SERIF',SERIF)
h=['<section class="aow2"><div class="wrap"><div class="hd"><p class="ey">Why Kitchen AO</p><h2>到會邊間好？點解客人揀 Kitchen AO</h2>',
 '<p class="sub"><span>作為香港到會服務品牌，由食材、出品到配送安排，</span><span>我哋希望每一個重要場合都更安心、更體面。</span></p></div><div class="hon">',BADGE,'</div><div class="fx">']
for (p,t,d,_),nt in zip(F,NT2): h.append('<div class="f">'+ic(p,t)+'<h3>%s</h3><p>%s</p><p class="nt">%s</p></div>'%(t,d,nt))
h.append('</div><div class="wc"><div class="df"><p class="ey">The Menu</p><h2>香港到會服務，食物點揀？</h2><p>由 Finger Food、小食拼盤到主菜甜品，到會套餐按人數配好，亦可再加單點，派對、公司活動及節日聚會都啱用。</p></div><ol>')
for (t,d),u in zip(W2,U2): h.append('<li><div><h3><a class="hl" href="%s">%s</a></h3><span>%s</span></div></li>'%(u,t,d))
h.append('</ol></div></div><div class="rev"><div class="wrap"><div class="hd"><p class="ey">Guest Reviews</p><h2>Kitchen AO 好唔好？客戶真實評價</h2><p class="sub"><span>來自派對聚會、公司活動及商務餐飲客戶的真實回饋，</span><span>讓你更放心安排重要場合。</span></p></div>')
h.append('<div class="rt"><div class="big">4.8<small>/ 5</small></div><div>'+STAR+'<span class="lb">Google 商戶評價</span></div><a class="btn" href="'+GURL+'" target="_blank" rel="noopener">查看 Google 評論</a></div><div class="qs">')
for t,n,k in R: h.append('<div class="q">%s<p>%s</p><b>%s</b><i>%s</i></div>'%(STAR,t,n,k))
h.append('</div></div></div></section>')
o2=c2+''.join(h)

for s in (o1,o2):
    assert '<script' not in s and '——' not in s and '→' not in s
D='/sessions/great-festive-darwin/mnt/Downloads/'
H=os.path.dirname(os.path.abspath(__file__))+'/'
open(H+'why-reviews-option1-rawhtml.html','w').write(o1)
open(H+'why-reviews-option2-rawhtml.html','w').write(o2)
open(D+'首頁-點解揀我們+評價-方案1-酒店信箋-rawhtml.html','w').write(o1)
open(D+'首頁-點解揀我們+評價-方案2-黑金禮賓-SEO版-rawhtml.html','w').write(o2)
pv=lambda t,b:'<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+t+'</title><style>body{margin:0;font-family:"Rubik","Noto Sans TC","PingFang HK",sans-serif}.lbl{background:#333;color:#fff;font:13px sans-serif;padding:10px 20px;letter-spacing:.1em}</style></head><body>'+b+'</body></html>'
open(H+'why-reviews-preview.html','w').write(pv('Kitchen AO 首頁方案2','<div class="lbl">方案 2｜黑金禮賓（SEO 版）</div>'+o2))
open(D+'首頁-點解揀我們+評價-方案2-SEO版-預覽.html','w').write(open(H+'why-reviews-preview.html').read())
print(len(o1),len(o2))
