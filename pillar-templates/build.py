# 產生 3 個 template（a/b/c.html）。修改後執行：python3 build.py
import pathlib
HERE = pathlib.Path(__file__).parent

QS = '''<div class="ao-qs" id="quick">
 <div class="ao-qs-promo"><span class="ao-qs-badge">限時優惠</span><span class="ao-qs-ptx" data-ao="promo-text"></span><span class="ao-qs-cdw" data-ao="countdown"></span></div>
 <form data-ao="qs-form" novalidate>
  <p class="ao-qs-title">30 秒快速搵餐單</p>
  <label class="ao-qs-f"><span class="ao-qs-l"><i>1</i>活動人數</span><input id="qs-n" type="number" min="1" max="999" inputmode="numeric" placeholder="例如 20"></label>
  <label class="ao-qs-f"><span class="ao-qs-l"><i>2</i>活動類別</span><select id="qs-type"></select></label>
  <label class="ao-qs-f"><span class="ao-qs-l"><i>3</i>活動日期</span><input id="qs-date" type="date"></label>
  <p class="ao-qs-msg" data-ao="qs-msg"></p>
  <button type="submit" class="ao-qs-btn">立即提供餐單建議</button>
  <p class="ao-qs-fine">系統會按人數、日期檢查餐單供應及優惠碼是否適用。建議僅供參考，最終以產品頁及客服確認為準。</p>
 </form>
 <div class="ao-qs-res" data-ao="qs-result" hidden><div data-ao="qs-list"></div><button type="button" class="ao-qs-again" data-ao="qs-again">‹ 重新選擇</button></div>
</div>'''

SECTIONS = '''
<section class="ao-sec" id="pkgs"><div class="ao-wrap"><div class="ao-sec-hd"><p class="ao-eyebrow" data-ao="tag"></p><h2>主要套餐</h2><p>按人數選擇，一個系列一行，左右滑動查看更多。</p></div><div data-ao="pkgs"></div></div></section>
<section class="ao-sec ao-sec-alt" id="singles"><div class="ao-wrap"><div class="ao-sec-hd"><h2>其他單品</h2><p>想更豐富？可加配以下單品。</p></div><div class="ao-sgs" data-ao="singles"></div></div></section>
<section class="ao-sec" id="trust"><div class="ao-wrap"><div class="ao-sec-hd ao-c"><h2>Kitchen AO 深受信賴</h2></div><div class="ao-tcs" data-ao="trust"></div></div></section>
<section class="ao-sec ao-sec-alt" id="photos"><div class="ao-wrap"><div class="ao-sec-hd"><h2>客人到會真實回圖</h2><p>送到現場的真實樣子（以下為示例相片，請換上客人回圖）。</p></div><div class="ao-phs" data-ao="photos"></div></div></section>
<section class="ao-sec" id="reviews"><div class="ao-wrap"><div class="ao-sec-hd"><h2>Google Review 高評價</h2></div><div class="ao-rvs" data-ao="reviews"></div></div></section>
<section class="ao-sec ao-sec-alt" id="kol"><div class="ao-wrap"><div class="ao-sec-hd"><h2>KOL 人氣分享</h2></div><div class="ao-kols" data-ao="kol"></div></div></section>
<section class="ao-sec" id="services"><div class="ao-wrap"><div class="ao-sec-hd"><h2>到會服務</h2><p>由公司活動到婚禮派對，一站式安排餐飲及現場服務。</p></div><div class="ao-svs" data-ao="services"></div></div></section>
<section class="ao-sec ao-sec-alt" id="clients"><div class="ao-wrap"><div class="ao-sec-hd"><h2>部分合作機構展示</h2><p>以下為 Kitchen AO 曾合作或服務過的部分企業、醫療、教育及公共機構名單展示。</p></div><div class="ao-clients" data-ao="clients"></div>
 <div class="ao-bizcta"><h3>想了解企業或機構活動到會方案？</h3><p>無論是公司午餐、品牌發布、醫療機構活動、學校聚會、周年晚宴或節日安排，我們都可以按活動性質與預算提供更合適的餐飲配搭建議。</p><div class="ao-bizcta-btns"><a class="ao-btn ao-btn-dark" href="https://aoaodelivery.com/contacts/" target="_blank" rel="noopener">聯絡我們查詢</a><a class="ao-btn ao-btn-gold" href="https://wa.me/85269011987" target="_blank" rel="noopener">WhatsApp 即時查詢</a></div></div></div></section>
<section class="ao-sec" id="reels"><div class="ao-wrap"><div class="ao-sec-hd"><h2>Instagram 精選</h2><p><a href="https://www.instagram.com/kitchen.ao/" target="_blank" rel="noopener">@kitchen.ao</a></p></div><div class="ao-reels" data-ao="reels"></div></div></section>
<footer class="ao-foot"><p>Template 示範｜產品、價錢及連結取自 aoaodelivery.com（2026-09-29）；標示「示例」的內容需換上真實資料。</p></footer>
'''

BASE_CSS = '''
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;font-family:-apple-system,BlinkMacSystemFont,"PingFang HK","Noto Sans HK","Microsoft JhengHei",sans-serif;color:#2a2620;line-height:1.6;-webkit-font-smoothing:antialiased}
img{max-width:100%;display:block}a{color:inherit}
.ao-wrap{max-width:1200px;margin:0 auto;padding:0 20px}
.ao-sec{padding:64px 0}.ao-sec-hd{margin-bottom:24px}.ao-sec-hd h2{font-size:30px;margin:0 0 6px;font-weight:900;letter-spacing:.5px}.ao-sec-hd p{margin:0;color:#6b6252}.ao-c{text-align:center}
.ao-eyebrow{font-weight:800;font-size:14px;margin:0 0 6px!important;color:var(--sc)!important}
[data-ao="filters"]{display:flex;gap:8px;overflow-x:auto;scrollbar-width:none;padding:12px 20px;max-width:1200px;margin:0 auto}[data-ao="filters"]::-webkit-scrollbar{display:none}
.ao-f{flex:0 0 auto;display:inline-flex;align-items:center;gap:6px;cursor:pointer;font:inherit;white-space:nowrap}
/* quick search */
.ao-qs{background:#fff;border-radius:18px;box-shadow:0 12px 40px rgba(0,0,0,.12);padding:18px;width:100%;max-width:440px}
.ao-qs-promo{display:flex;flex-wrap:wrap;align-items:center;gap:6px 10px;border-radius:12px;padding:10px 12px;font-size:13px}
.ao-qs-badge{font-weight:800;font-size:12px;padding:2px 8px;border-radius:6px}.ao-qs-ptx{flex:1 1 150px}
.ao-qs-cdw{display:flex;gap:4px}.ao-cd{font-size:11px;display:inline-flex;align-items:baseline;gap:2px}.ao-cd b{display:inline-block;min-width:26px;text-align:center;padding:3px 4px;border-radius:6px;font-size:14px}
.ao-qs-title{font-size:18px;font-weight:900;margin:16px 0 8px}
.ao-qs-f{display:block;margin:0 0 12px}.ao-qs-l{display:flex;align-items:center;gap:8px;font-size:14px;font-weight:800;margin-bottom:6px}.ao-qs-l i{font-style:normal;width:22px;height:22px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:12px}
.ao-qs input,.ao-qs select{width:100%;height:46px;border-radius:10px;border:1.5px solid #e2dccf;padding:0 12px;font:inherit;font-size:16px;background:#fff;color:#2a2620}
.ao-qs input:focus,.ao-qs select:focus{outline:none;border-color:var(--sc)}
.ao-qs-msg{color:#c0392b;font-size:13px;min-height:1em;margin:0 0 6px}
.ao-qs-btn{width:100%;height:52px;border:0;border-radius:30px;font:inherit;font-weight:900;font-size:17px;cursor:pointer}
.ao-qs-fine{font-size:11.5px;color:#8a8172;margin:10px 0 0;line-height:1.5}
.ao-qs-head{font-weight:900;font-size:16px;margin:14px 0 8px}.ao-qs-warn,.ao-qs-ok,.ao-qs-muted{font-size:13px;margin:0 0 6px;padding:6px 10px;border-radius:8px}.ao-qs-warn{background:#fff4e5;color:#8a5a00}.ao-qs-ok{background:#eaf7ee;color:#1f6b3a}.ao-qs-muted{background:#f4f2ee;color:#6b6252}
.ao-qs-item{display:flex;align-items:center;gap:12px;padding:10px;border:1.5px solid #eee7d9;border-radius:12px;margin:8px 0 0;text-decoration:none}.ao-qs-item:hover{border-color:var(--sc)}
.ao-qs-item img{width:64px;height:64px;object-fit:cover;border-radius:10px;flex:0 0 64px}.ao-qs-tx{flex:1;display:flex;flex-direction:column;font-size:13px;line-height:1.4}.ao-qs-tx em{font-style:normal;font-size:11px;font-weight:800;color:var(--sc)}.ao-qs-tx b{font-size:15px}.ao-qs-go{font-size:22px;color:#b0a794}
.ao-qs-wa{display:block;text-align:center;margin:12px 0 0;padding:12px;border-radius:30px;background:#25D366;color:#fff;font-weight:800;text-decoration:none}
.ao-qs-again{background:none;border:0;font:inherit;color:#6b6252;cursor:pointer;margin-top:8px;padding:6px 0}
/* packages */
.ao-series{margin:0 0 34px}.ao-series-hd{display:flex;justify-content:space-between;align-items:flex-end;gap:12px;margin-bottom:12px}.ao-series-hd h3{margin:0;font-size:20px;font-weight:900}.ao-series-hd p{margin:2px 0 0;color:#6b6252;font-size:14px}.ao-series-all{white-space:nowrap;font-weight:800;text-decoration:none;font-size:14px}
.ao-row{position:relative}.ao-track{display:flex;gap:16px;overflow-x:auto;scroll-snap-type:x mandatory;scrollbar-width:none;padding:4px 2px 10px}.ao-track::-webkit-scrollbar{display:none}
.ao-pc{flex:0 0 240px;scroll-snap-align:start;text-decoration:none;display:flex;flex-direction:column;overflow:hidden}
.ao-pc-img{display:block;aspect-ratio:1/1;overflow:hidden}.ao-pc-img img{width:100%;height:100%;object-fit:cover;transition:transform .3s}.ao-pc:hover .ao-pc-img img{transform:scale(1.05)}
.ao-pc-body{display:flex;flex-direction:column;gap:2px;padding:12px 14px 14px}.ao-pc-nm{font-size:16px}.ao-pc-pax{font-size:13px;color:#6b6252}.ao-pc-price{font-size:18px;font-weight:900}
.ao-rb{position:absolute;top:36%;z-index:2;width:40px;height:40px;border-radius:50%;border:0;cursor:pointer;font-size:24px;line-height:38px;display:none;box-shadow:0 4px 12px rgba(0,0,0,.18)}.ao-rb.prev{left:-12px}.ao-rb.next{right:-12px}.ao-row.ovf .ao-rb{display:block}
/* singles */
.ao-sgs{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:14px}.ao-sg{text-decoration:none;display:flex;flex-direction:column;overflow:hidden}.ao-sg img{aspect-ratio:4/3;object-fit:cover;width:100%}.ao-sg span{display:flex;flex-direction:column;padding:10px 12px}.ao-sg em{font-style:normal;font-size:11px;font-weight:800;color:var(--sc)}.ao-sg b{font-size:14px}
/* trust */
.ao-tcs{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}.ao-tc{border-radius:22px;padding:26px 20px 18px;text-align:center;display:flex;flex-direction:column;align-items:center;min-height:360px}
.ao-tc-k{margin:0;font-weight:800;font-size:15px}.ao-tc-v{margin:4px 0 0;font-size:44px;font-weight:900;line-height:1.1}.ao-tc-note{margin:4px 0 0;font-size:12px;color:#8a8172}
.ao-tc-boss{display:flex;gap:8px;justify-content:center;margin:14px 0 0;flex:1;align-items:flex-end}.ao-tc-boss img{width:120px;height:156px;object-fit:cover}
.ao-tc-foot{margin-top:auto;background:#fff;border-radius:14px;padding:14px;width:100%;font-size:14px;font-weight:700}
/* photos / reviews / kol / services / clients / reels */
.ao-phs{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}.ao-ph{margin:0;position:relative;border-radius:14px;overflow:hidden;aspect-ratio:1/1}.ao-ph img{width:100%;height:100%;object-fit:cover}.ao-ph figcaption{position:absolute;left:8px;bottom:8px;background:rgba(0,0,0,.55);color:#fff;font-size:11px;padding:2px 8px;border-radius:10px}
.ao-rvs{display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:14px}.ao-rv-sum,.ao-rv{border-radius:16px;padding:18px}.ao-rv-sum{text-align:center}.ao-rv-sum b{font-size:48px;display:block;line-height:1}.ao-rv-sum span{color:#F5B400;font-size:20px}.ao-rv-sum p{font-size:12px;color:#8a8172;margin:6px 0 0}
.ao-rv-top{display:flex;gap:10px;align-items:center;margin-bottom:8px}.ao-rv-top div{display:flex;flex-direction:column;font-size:13px}.ao-rv-top span{color:#F5B400}.ao-rv-av{width:36px;height:36px;border-radius:50%;display:flex!important;align-items:center;justify-content:center;background:#4285F4;color:#fff!important;font-weight:900}.ao-rv p{font-size:14px;margin:0;color:#4a4238}
.ao-kols{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}.ao-kol{border-radius:16px;padding:14px}.ao-kol-img{aspect-ratio:4/5;border-radius:12px;background:#e9e3d6;display:flex;align-items:center;justify-content:center;color:#8a7f6b;margin-bottom:10px}.ao-kol p{margin:4px 0 0;font-size:14px;color:#6b6252}
.ao-svs{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.ao-sv{text-decoration:none;border-radius:16px;padding:18px;display:flex;flex-direction:column;gap:4px}.ao-sv-ic{font-size:28px}.ao-sv b{font-size:16px}.ao-sv span:last-child{font-size:13px;color:#6b6252}
.ao-clients img{width:100%;border-radius:12px;background:#fff}
.ao-bizcta{margin-top:26px;border-radius:20px;padding:28px;text-align:center}.ao-bizcta h3{margin:0 0 8px;font-size:22px}.ao-bizcta p{margin:0 auto 16px;max-width:680px}
.ao-bizcta-btns{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}.ao-btn{display:inline-block;min-width:220px;text-align:center;padding:13px 22px;border-radius:40px;font-weight:800;text-decoration:none}
.ao-btn-dark{background:#1A1A1A;color:#F7CE46}.ao-btn-gold{background:#C8A24A;color:#1A1A1A}
.ao-reels{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;align-items:start}.ao-reel{min-height:200px}.ao-reel-ph{border:2px dashed #d8cfbd;border-radius:16px;aspect-ratio:9/16;display:flex;align-items:center;justify-content:center;text-align:center;color:#8a7f6b}
.ao-foot{text-align:center;font-size:12px;color:#8a8172;padding:30px 20px 60px}
@media(max-width:900px){.ao-tcs,.ao-kols,.ao-reels{grid-template-columns:1fr}.ao-rvs,.ao-svs{grid-template-columns:1fr 1fr}.ao-phs{grid-template-columns:1fr 1fr}.ao-tc{min-height:0}}
@media(max-width:600px){.ao-sec{padding:44px 0}.ao-sec-hd h2{font-size:24px}.ao-pc{flex-basis:70%}.ao-rb{display:none!important}.ao-svs{grid-template-columns:1fr 1fr}.ao-rvs{grid-template-columns:1fr}.ao-sgs{grid-template-columns:1fr 1fr}.ao-tc-v{font-size:36px}}
'''

T = {}

# ---------- A：金黑經典（Bowtie 式左右分欄） ----------
T['a'] = dict(name='A｜金黑經典', css='''
:root{--sc:#2BB3C7}body{background:#fff}
.top{position:sticky;top:0;z-index:20;background:#1A1A1A}
.ao-f{border:1.5px solid #4a4a4a;background:transparent;color:#EDE6D6;border-radius:30px;padding:8px 16px;font-size:15px}.ao-f.on{background:#C8A24A;border-color:#C8A24A;color:#1A1A1A;font-weight:800}
.hero{background:#FBF6EC;padding:48px 0 56px}.hero .ao-wrap{display:grid;grid-template-columns:1.15fr .85fr;gap:40px;align-items:start}
.hero-tag{display:inline-block;background:var(--sc);color:#fff;font-weight:800;font-size:14px;padding:4px 12px;border-radius:6px}
.hero h1{font-size:46px;line-height:1.2;margin:14px 0 10px;font-weight:900}.hero-sub{font-size:18px;color:#5a5244;margin:0 0 16px}
.hero [data-ao="stats"]{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:22px}.ao-stat{background:#1A1A1A;color:#F7CE46;font-weight:800;font-size:14px;padding:6px 12px;border-radius:8px}
.hero-img{border-radius:20px;overflow:hidden;aspect-ratio:16/10;box-shadow:0 10px 30px rgba(0,0,0,.12)}.hero-img img{width:100%;height:100%;object-fit:cover}
.hero .ao-qs{justify-self:end;position:sticky;top:80px}
.ao-qs-promo{background:#1A1A1A;color:#fff}.ao-qs-badge{background:#C8A24A;color:#1A1A1A}.ao-cd{color:#ccc}.ao-cd b{background:#333;color:#fff}
.ao-qs-l i{background:#1A1A1A;color:#F7CE46}.ao-qs-btn{background:#C8A24A;color:#1A1A1A}.ao-qs-btn:hover{background:#1A1A1A;color:#F7CE46}
.ao-sec-alt{background:#FBF6EC}
.ao-pc{background:#fff;border:1px solid #eee4cf;border-radius:16px}.ao-pc-price{color:#9A7B2E}.ao-series-all{color:#9A7B2E}
.ao-rb{background:#1A1A1A;color:#F7CE46}
.ao-sg{background:#fff;border-radius:14px;border:1px solid #eee4cf}
.ao-tc{background:#FBF1DC}.ao-tc-k{color:#9A7B2E}.ao-tc-v{color:#1A1A1A}
.ao-rv-sum,.ao-rv{background:#fff;border:1px solid #eee4cf}.ao-kol{background:#fff}.ao-sv{background:#fff;border:1px solid #eee4cf}.ao-sv:hover{border-color:#C8A24A}
.ao-bizcta{background:#1A1A1A;color:#fff}.ao-bizcta .ao-btn-dark{background:#fff;color:#1A1A1A}
@media(max-width:900px){.hero .ao-wrap{grid-template-columns:1fr}.hero .ao-qs{justify-self:stretch;max-width:none;position:static}.hero h1{font-size:34px}}
''', hero='''<header class="hero"><div class="ao-wrap"><div><span class="hero-tag" data-ao="tag"></span><h1 data-ao="title"></h1><p class="hero-sub" data-ao="sub"></p><div data-ao="stats"></div><div class="hero-img"><img data-ao="hero-img" alt=""></div></div>''' + QS + '''</div></header>''')

# ---------- B：清新卡片（全幅相片 + 浮動搜尋卡） ----------
T['b'] = dict(name='B｜清新卡片', css='''
:root{--sc:#2BB3C7}body{background:#F6F5F2}
.top{position:sticky;top:0;z-index:20;background:#fff;border-bottom:1px solid #ece8df}
[data-ao="filters"]{gap:0;padding:0 12px}
.ao-f{border:0;background:none;color:#7a7263;padding:16px 18px 13px;font-size:15px;border-bottom:3px solid transparent;flex-direction:column;gap:2px}.ao-f-ic{font-size:20px}.ao-f.on{color:#1A1A1A;font-weight:800;border-bottom-color:var(--sc)}
.hero{position:relative;min-height:560px;display:flex;align-items:center;overflow:hidden}
.hero-bg{position:absolute;inset:0}.hero-bg img{width:100%;height:100%;object-fit:cover;filter:saturate(1.05)}.hero-bg:after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(15,15,15,.78) 0%,rgba(15,15,15,.45) 55%,rgba(15,15,15,.15) 100%)}
.hero .ao-wrap{position:relative;display:grid;grid-template-columns:1fr 420px;gap:40px;align-items:center;width:100%;padding-top:40px;padding-bottom:40px}
.hero-txt{color:#fff}.hero-tag{display:inline-block;border:1.5px solid rgba(255,255,255,.7);border-radius:30px;padding:4px 14px;font-size:14px;font-weight:700}
.hero h1{font-size:48px;line-height:1.2;margin:16px 0 10px;font-weight:900}.hero-sub{font-size:18px;opacity:.9;margin:0 0 18px}
.hero [data-ao="stats"]{display:grid;grid-template-columns:repeat(4,auto);gap:0;justify-content:start;border-top:1px solid rgba(255,255,255,.3);padding-top:16px}.ao-stat{padding:0 18px;border-left:1px solid rgba(255,255,255,.3);font-weight:800}.ao-stat:first-child{padding-left:0;border-left:0}
.ao-qs{background:rgba(255,255,255,.96);backdrop-filter:blur(8px)}
.ao-qs-promo{background:#F1FAFC;color:#1a4d57;border:1px solid #cdeef4}.ao-qs-badge{background:var(--sc);color:#fff}.ao-cd{color:#5b7d84}.ao-cd b{background:#fff;color:#1a4d57;border:1px solid #cdeef4}
.ao-qs-l i{background:var(--sc);color:#fff}.ao-qs-btn{background:#1A1A1A;color:#fff}.ao-qs-btn:hover{background:var(--sc)}
.ao-sec{background:#F6F5F2}.ao-sec-alt{background:#fff}
.ao-series{background:#fff;border-radius:20px;padding:20px;box-shadow:0 2px 10px rgba(0,0,0,.04)}
.ao-series-hd h3:before{content:"";display:inline-block;width:6px;height:18px;border-radius:3px;background:var(--sc);margin-right:10px;vertical-align:-2px}
.ao-pc{background:#F6F5F2;border-radius:14px;flex-basis:220px}.ao-pc-price{color:#1A1A1A}.ao-series-all{color:var(--sc)}
.ao-rb{background:#fff;color:#1A1A1A}
.ao-sgs{grid-template-columns:repeat(auto-fill,minmax(260px,1fr))}.ao-sg{flex-direction:row;align-items:center;background:#F6F5F2;border-radius:14px}.ao-sg img{width:88px;height:88px;aspect-ratio:auto;flex:0 0 88px}
.ao-tc{background:#EAF7FA}.ao-tc-k{color:#1f7f8f}.ao-tc-v{color:#1A1A1A}
.ao-rv-sum,.ao-rv{background:#fff}.ao-kol{background:#F6F5F2}.ao-sv{background:#fff;box-shadow:0 2px 10px rgba(0,0,0,.05)}.ao-sv:hover{box-shadow:0 6px 20px rgba(0,0,0,.1)}
.ao-bizcta{background:linear-gradient(135deg,#1A1A1A,#3a3a3a);color:#fff}.ao-bizcta .ao-btn-dark{background:#fff;color:#1A1A1A}
@media(max-width:900px){.hero .ao-wrap{grid-template-columns:1fr}.hero h1{font-size:34px}.hero [data-ao="stats"]{grid-template-columns:1fr 1fr;gap:8px}.ao-stat{border:0!important;padding:0!important}.ao-qs{max-width:none}}
''', hero='''<header class="hero"><div class="hero-bg"><img data-ao="hero-img" alt=""></div><div class="ao-wrap"><div class="hero-txt"><span class="hero-tag" data-ao="tag"></span><h1 data-ao="title"></h1><p class="hero-sub" data-ao="sub"></p><div data-ao="stats"></div></div>''' + QS + '''</div></header>''')

# ---------- C：活力主題色（每個場景換主色） ----------
T['c'] = dict(name='C｜活力主題色', css='''
:root{--sc:#2BB3C7}body{background:#FFFDF8}
.top{position:sticky;top:0;z-index:20;background:#FFFDF8;box-shadow:0 2px 12px rgba(0,0,0,.06)}
[data-ao="filters"]{gap:10px;padding:12px 20px}
.ao-f{border:2px solid #1A1A1A;background:#fff;color:#1A1A1A;border-radius:14px;padding:8px 14px;font-size:15px;font-weight:700;box-shadow:3px 3px 0 #1A1A1A;transition:transform .15s}.ao-f:hover{transform:translate(-1px,-1px)}.ao-f.on{background:var(--sc);color:#fff;box-shadow:3px 3px 0 #1A1A1A}
.hero{background:var(--sc);position:relative;overflow:hidden;padding:56px 0 90px;transition:background .3s}
.hero:after{content:"";position:absolute;left:-5%;right:-5%;bottom:-60px;height:120px;background:#FFFDF8;border-radius:50%}
.hero .ao-wrap{position:relative;z-index:1;display:grid;grid-template-columns:1fr 420px;gap:36px;align-items:center}
.hero-txt{color:#fff}.hero-tag{display:inline-block;background:#fff;color:#1A1A1A;border:2px solid #1A1A1A;border-radius:30px;padding:4px 14px;font-weight:800;font-size:14px;box-shadow:2px 2px 0 #1A1A1A}
.hero h1{font-size:46px;line-height:1.2;margin:16px 0 10px;font-weight:900;text-shadow:3px 3px 0 rgba(0,0,0,.25)}.hero-sub{font-size:18px;margin:0 0 18px}
.hero [data-ao="stats"]{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:20px}.ao-stat{background:#fff;color:#1A1A1A;border:2px solid #1A1A1A;border-radius:30px;padding:5px 12px;font-weight:800;font-size:14px}
.hero-img{width:260px;height:260px;border-radius:50%;overflow:hidden;border:6px solid #fff;box-shadow:6px 6px 0 #1A1A1A}.hero-img img{width:100%;height:100%;object-fit:cover}
.ao-qs{border:2.5px solid #1A1A1A;box-shadow:8px 8px 0 #1A1A1A;border-radius:22px}
.ao-qs-promo{background:#1A1A1A;color:#fff}.ao-qs-badge{background:var(--sc);color:#fff}.ao-cd{color:#bbb}.ao-cd b{background:#fff;color:#1A1A1A}
.ao-qs-l i{background:var(--sc);color:#fff;border:2px solid #1A1A1A}.ao-qs input,.ao-qs select{border:2px solid #1A1A1A}
.ao-qs-btn{background:var(--sc);color:#fff;border:2.5px solid #1A1A1A;box-shadow:4px 4px 0 #1A1A1A}.ao-qs-btn:active{transform:translate(2px,2px);box-shadow:2px 2px 0 #1A1A1A}
.ao-sec-alt{background:#fff}
.ao-series-hd h3{display:inline-block;background:var(--sc);color:#fff;padding:4px 14px;border-radius:10px;border:2px solid #1A1A1A}
.ao-pc{background:#fff;border:2px solid #1A1A1A;border-radius:18px;box-shadow:4px 4px 0 #1A1A1A}.ao-pc-price{display:inline-block;align-self:flex-start;background:var(--sc);color:#fff;padding:0 10px;border-radius:8px;margin-top:4px}.ao-series-all{color:#1A1A1A}
.ao-track{padding:4px 6px 14px}
.ao-rb{background:var(--sc);color:#fff;border:2px solid #1A1A1A}
.ao-sg{background:#fff;border:2px solid #1A1A1A;border-radius:16px}
.ao-tc{background:#fff;border:2.5px solid #1A1A1A;box-shadow:6px 6px 0 var(--sc)}.ao-tc-k{color:#1A1A1A}.ao-tc-v{color:var(--sc)}.ao-tc-foot{border:2px solid #1A1A1A}
.ao-rv-sum,.ao-rv,.ao-kol,.ao-sv{background:#fff;border:2px solid #1A1A1A}.ao-sv:hover{background:var(--sc);color:#fff}.ao-sv:hover span:last-child{color:#fff}
.ao-bizcta{background:var(--sc);color:#fff;border:2.5px solid #1A1A1A;box-shadow:6px 6px 0 #1A1A1A}
@media(max-width:900px){.hero .ao-wrap{grid-template-columns:1fr}.hero h1{font-size:34px}.hero-img{width:180px;height:180px}.ao-qs{max-width:none}}
''', hero='''<header class="hero"><div class="ao-wrap"><div class="hero-txt"><span class="hero-tag" data-ao="tag"></span><h1 data-ao="title"></h1><p class="hero-sub" data-ao="sub"></p><div data-ao="stats"></div><div class="hero-img"><img data-ao="hero-img" alt=""></div></div>''' + QS + '''</div></header>''')

for k, t in T.items():
    html = f'''<!DOCTYPE html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Kitchen AO 場景到會 Landing — Template {t['name']}</title>
<style>{BASE_CSS}{t['css']}</style></head><body>
<nav class="top" aria-label="場景篩選"><div data-ao="filters"></div></nav>
{t['hero']}
{SECTIONS}
<script src="data.js"></script><script src="engine.js"></script></body></html>'''
    (HERE / f'{k}.html').write_text(html, encoding='utf-8')

cards = ''.join(f'<a class="c" href="./{k}.html"><b>{t["name"]}</b><span>打開 template ›</span></a>' for k, t in T.items())
(HERE / 'index.html').write_text(f'''<!DOCTYPE html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Kitchen AO 場景 Landing Page — 3 個 Template</title>
<style>body{{margin:0;background:#1A1A1A;color:#EDE6D6;font-family:-apple-system,"PingFang HK",sans-serif;display:flex;min-height:100vh;align-items:center;justify-content:center;padding:30px}}.b{{max-width:560px;width:100%}}h1{{color:#F7CE46;font-size:22px}}p{{color:#C9BFA8;font-size:14px}}.c{{display:flex;justify-content:space-between;background:#242424;border:1px solid #3a3a3a;border-radius:14px;padding:18px 20px;margin:0 0 12px;text-decoration:none;color:#EDE6D6}}.c:hover{{border-color:#C8A24A}}.c span{{color:#C8A24A}}</style></head><body><div class="b">
<h1>Kitchen AO 場景 Landing Page — Template v1</h1><p>2026-09-29｜最頂篩選 tag（船河、素食、生日會、公司午餐、學校飯盒、中秋節、萬聖節、訂製食物），切換後 Hero、快速搜尋、主要套餐及單品會一齊更新。</p>{cards}</div></body></html>''', encoding='utf-8')
print('built')
