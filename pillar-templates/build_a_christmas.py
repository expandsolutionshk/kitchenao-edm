# -*- coding: utf-8 -*-
"""聖誕到會場景 Landing（Template A × 酒店網店風格）
輸出：a-christmas.html（單一檔案，CSS/JS 全部內嵌，可貼 WPBakery Raw HTML）"""
import json, pathlib, urllib.parse
HERE = pathlib.Path(__file__).parent
U = 'https://aoaodelivery.com/wp-content/uploads/2026/11/'
P = 'https://aoaodelivery.com/product/'
C = 'https://aoaodelivery.com/product-category/christmas-party-catering-set/'
WA = 'https://wa.me/85269011987?text=' + urllib.parse.quote('你好，我想查詢聖誕到會套餐。')
IMG = {k: U + f'20_26xmas-{v}.jpg' for k, v in dict(beef='beef-box', chk1='chicken-1', chk2='chicken-2', puff='chestnut-pastry', cro='mentaiko-crossant',
       tart='pistachio-tart', rice='bowl-jai', ris='korea-rice', salad='prawn-salad').items()}
SER = [
 dict(id='beef', name='聖誕寶藏箱', full='煙燻慢煮美國牛翼板肉盛宴', slug='treasure-box-beef', img=IMG['beef'], img2=IMG['rice'],
      desc='稀有下肩胛翼板肉，每頭牛僅約 2 至 3 公斤。慢煮至五成熟後以煙燻木料炙烤，以復古寶箱盛載，全港限量 100 個。',
      rows=[(5, 6, 1928), (8, 10, 3028), (12, 16, 4588), (18, 22, 5888), (26, 30, 7888), (35, 40, 9888)]),
 dict(id='chk', name='聖誕金雞獻禮', full='燒南乳香慢煮原隻黃油雞', slug='golden-roast-chicken', img=IMG['chk2'], img2=IMG['tart'],
      desc='本地原隻黃油雞以南乳醃製及鹽水浸漬，低溫慢煮後高溫炙燒至皮脆肉嫩，配聖誕玫瑰金巴利汁，專屬木箱盛載。',
      rows=[(5, 6, 1688), (8, 10, 2788), (12, 16, 4248), (18, 22, 5388), (26, 30, 7388), (35, 40, 9288)]),
 dict(id='dbl', name='聖誕開箱雙寶', full='原隻黃油雞 × 煙燻慢煮美國牛翼板肉', slug='twin-treasures-chicken-beef', img=IMG['chk1'], img2=IMG['beef'],
      desc='兩大主菜同場：燒南乳香慢煮原隻黃油雞及寶箱煙燻慢煮美國牛翼板肉，專為 48 至 100 人的公司年終派對及大型活動而設。',
      rows=[(48, 54, 12418), (63, 68, 15368), (78, 85, 19548), (90, 100, 22888)]),
]
def url(s, a, b): return f'{P}{a}-{b}pax-christmas-set-{s["slug"]}/'
def money(n): return f'HK${n:,.0f}'
def card(s, a, b, pr, top=False):
    eb = round(pr * .79)
    return (f'<a class="pc" href="{url(s, a, b)}"><div class="pc-im"><img src="{s["img"]}" alt="{a}-{b}人{s["name"]}聖誕套餐" loading="lazy">'
            f'<img class="alt" src="{s["img2"]}" alt="" loading="lazy"><span class="badge">Early Bird 七九折</span></div>'
            f'<p class="pc-k">{s["name"]}</p><p class="pc-n">{a}–{b} 人{s["full"]}聖誕套餐</p>'
            f'<p class="pc-p"><b>{money(pr)}</b><span>MEGA79 後約 {money(eb)}</span></p><p class="pc-pp">每位約 {money(pr / b)}–{money(pr / a)}</p></a>')
TOP = [(SER[0], 5, 6, 1928), (SER[1], 5, 6, 1688), (SER[0], 12, 16, 4588), (SER[1], 18, 22, 5388), (SER[2], 48, 54, 12418), (SER[2], 90, 100, 22888)]
PAX = [('5 至 6 人', '5-6 人套餐', ''), ('7 人', '8-10 人套餐', '或 5-6 人套餐加配單點'), ('8 至 10 人', '8-10 人套餐', ''), ('11 人', '12-16 人套餐', '或 8-10 人套餐加配單點'),
       ('12 至 16 人', '12-16 人套餐', ''), ('17 人', '18-22 人套餐', '或 12-16 人套餐加配單點'), ('18 至 22 人', '18-22 人套餐', ''), ('23 至 25 人', '26-30 人套餐', '或 18-22 人套餐加配單點'),
       ('26 至 30 人', '26-30 人套餐', ''), ('31 至 34 人', '35-40 人套餐', '或 26-30 人套餐加配單點'), ('35 至 40 人', '35-40 人套餐', ''), ('41 至 47 人', '48-54 人開箱雙寶', '或 35-40 人套餐加配單點'),
       ('48 至 54 人', '48-54 人開箱雙寶', ''), ('55 至 62 人', '63-68 人開箱雙寶', '或 48-54 人加配單點'), ('63 至 68 人', '63-68 人開箱雙寶', ''), ('69 至 77 人', '78-85 人開箱雙寶', '或 63-68 人加配單點'),
       ('78 至 85 人', '78-85 人開箱雙寶', ''), ('86 至 89 人', '90-100 人開箱雙寶', '或 78-85 人加配單點'), ('90 至 100 人', '90-100 人開箱雙寶', ''), ('100 人以上', '到會報價查詢', '')]
DISH = [('rice', '雙重龍蝦三重芝士煲仔鍋飯', '原個布袋芝士切開即流心，飯底吸滿濃郁龍蝦汁'), ('ris', '玫瑰醬泡菜海蝦意大利飯', '韓式玫瑰醬配泡菜，奶香柔和、微辣開胃'),
        ('puff', '芒果粟子蓉冬日酥盒', '日本栗子蓉配新鮮芒果粒，酸甜開胃的前菜'), ('cro', '明太子芝士忌廉牛角酥', '牛角酥夾入明太子芝士忌廉，鹹香柔滑'),
        ('salad', '紅寶神石榴沙律系列', '大蝦柚肉或煙火雞胸蜜桃兩款任選'), ('tart', '聖誕馴鹿脆脆開心果朱古力撻', '開心果白朱古力配脆脆，朱古力曲奇鹿角')]
OCC = [('公司聖誕派對', '部門聚餐、年終派對及客戶活動，按人數揀套餐，可索取正式報價。', 'https://aoaodelivery.com/corporate-catering-hk/', '公司聖誕派對到會'),
       ('家庭聖誕聚會', '5 至 10 人小型套餐，一款原隻主菜配前菜、沙律、主食及甜品，在家輕鬆開餐。', '#sets', '揀家庭聖誕套餐'),
       ('學校、教會及機構', '人數較多、年齡層闊，可加配兒童及素食選擇，並預先統計飲食需要。', 'https://aoaodelivery.com/catering-quote-enquiry/', '到會報價查詢'),
       ('素食朋友', '套餐以外可加配素食菜式，或選擇「素」味人生素食到會套餐。', 'https://aoaodelivery.com/product-category/party/vegetarians-set/', '素食到會套餐')]
FAQ = [
 ('聖誕到會要提早幾多日預訂？', '平安夜及聖誕節是全年到會高峰，熱門送貨時段較快額滿，建議盡早預訂。2026 年 11 月 30 日 23:59 前輸入優惠碼 MEGA79，聖誕套餐更可享七九折。'),
 ('平安夜及聖誕節可以送貨嗎？', '可以按落單頁面提供的日期及時段送貨。平安夜（12 月 24 日）及聖誕節（12 月 25 日）時段有限，建議預留至少 30 分鐘緩衝時間，詳情可參考送貨需知。'),
 ('聖誕到會套餐每位大約幾錢？', 'Kitchen AO 2026 聖誕套餐以原價計，每位約 HK$226 至 386，人數愈多每位愈低；11 月 30 日前以 MEGA79 再享七九折。'),
 ('聖誕大餐吃什麼？', '一桌完整的聖誕大餐一般包括一至兩款焦點主菜（例如原隻燒雞或燒牛肉）、前菜、沙律、意粉或飯，以及甜品。Kitchen AO 聖誕套餐已按人數配搭好以上各類菜式。'),
 ('聖誕套餐有沒有火雞？', '2026 年聖誕套餐的主菜為燒南乳香慢煮原隻黃油雞及寶箱煙燻慢煮美國牛翼板肉。如有其他主菜需要，歡迎 WhatsApp 查詢。'),
 ('10 人或 20 人聖誕派對應揀哪個套餐？', '10 人可選 8-10 人套餐；20 人可選 18-22 人套餐。人數介乎兩個套餐之間時，可選較大的套餐，或選較小的套餐再加配單點小食，詳見上方「按人數揀聖誕套餐」。'),
 ('聖誕套餐的菜式可以更換嗎？', '套餐菜式可按喜好自由配搭；部分精選菜式需另加差價，實際價錢以落單頁面選項為準。'),
 ('可以加素食或兒童菜式嗎？', '可以在套餐以外加配單點小食及甜品，素食朋友亦可選擇「素」味人生素食到會套餐。'),
 ('公司聖誕派對可以索取報價嗎？', '可以。公司、學校及機構訂購如需正式報價及收據，可經到會報價查詢聯絡我們。'),
 ('聖誕到會包括餐具嗎？', '落單時可選擇是否需要碟及餐具，亦可加配食物夾等用品。'),
]
LD = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}, ensure_ascii=False)
SNOW = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2v20M3.3 7l17.4 10M3.3 17L20.7 7M12 5l-2-2M12 5l2-2M12 19l-2 2M12 19l2 2" stroke="currentColor" stroke-width="1.4" fill="none" stroke-linecap="round"/></svg>'

CSS = r'''
.axl{--ink:#1A1A1A;--sub:#5d534d;--g:#1E4A3B;--gd:#C8A24A;--bu:#8A453F;--iv:#FBF8F2;--ln:#E6DCC8;font-family:-apple-system,"PingFang HK","Microsoft JhengHei",sans-serif;color:var(--ink);background:#fff;line-height:1.75}
.axl *{box-sizing:border-box}.axl a{color:inherit}.axl img{max-width:100%;display:block}
.axl .ser{font-family:"Songti TC","Noto Serif TC","PMingLiU",serif}
.axl .bar{background:var(--g);color:#F3EBD6;text-align:center;font-size:13px;letter-spacing:.06em;padding:9px 14px}.axl .bar b{color:#F7CE46}
.axl .w{max-width:1240px;margin:0 auto;padding:0 24px}
.axl .crumb{font-size:12.5px;color:#9A8f7e;padding:14px 0}.axl .crumb a{text-decoration:none}
.axl .hero{position:relative;height:clamp(380px,62vw,620px);overflow:hidden;background:#111}
.axl .hero img{width:100%;height:100%;object-fit:cover;opacity:.82}
.axl .hero .in{position:absolute;inset:auto 0 0 0;padding:clamp(24px,5vw,56px);background:linear-gradient(transparent,rgba(0,0,0,.6));color:#fff}
.axl .hero small{letter-spacing:.42em;font-size:12px;color:#E9D29A}
.axl .hero h1{font-family:"Songti TC","Noto Serif TC",serif;font-weight:600;font-size:clamp(26px,4.6vw,46px);line-height:1.3;margin:10px 0 8px;color:#fff}
.axl .hero p{margin:0 0 18px;max-width:620px;color:#EFE7D6;font-size:clamp(14px,1.8vw,16px)}
.axl .btn{display:inline-block;text-decoration:none!important;font-size:14px;letter-spacing:.14em;padding:13px 28px;border:1px solid currentColor;margin:0 10px 10px 0;transition:.2s}
.axl .btn.p{background:var(--g);border-color:var(--g);color:#fff!important}.axl .btn.p:hover{background:#163a2e}
.axl .btn.o{color:#fff!important}.axl .btn.d{background:var(--ink);border-color:var(--ink);color:#E4C77E!important}
.axl .eb{background:var(--iv);border-bottom:1px solid var(--ln);text-align:center;padding:14px;font-size:14.5px}.axl .eb b{color:var(--bu)}.axl .eb .cd{font-variant-numeric:tabular-nums;color:var(--g);font-weight:700;margin-left:6px}
.axl .intro{max-width:820px;margin:0 auto;text-align:center;padding:clamp(44px,7vw,80px) 24px 24px}
.axl .intro h2,.axl .sh h2{font-family:"Songti TC","Noto Serif TC",serif;font-weight:600;font-size:clamp(24px,3.2vw,34px);margin:0 0 14px;letter-spacing:.04em}
.axl .intro p{color:var(--sub);font-size:15.5px;margin:0 0 12px}
.axl .pills{display:flex;gap:10px;flex-wrap:wrap;justify-content:center;padding:6px 24px 10px}
.axl .pills a{text-decoration:none;border:1px solid var(--ln);padding:8px 18px;font-size:13.5px;letter-spacing:.06em;background:#fff}.axl .pills a:hover{border-color:var(--g);color:var(--g)}
.axl section.s{padding:clamp(44px,6vw,76px) 0;border-top:1px solid #F1EBDD}
.axl .sh{text-align:center;max-width:760px;margin:0 auto 30px}.axl .sh small{display:block;letter-spacing:.38em;font-size:11.5px;color:#9A7B2E;margin-bottom:8px}.axl .sh p{color:var(--sub);margin:0}
.axl .rail{position:relative}.axl .track{display:grid;grid-auto-flow:column;grid-auto-columns:calc((100% - 72px)/4);gap:24px;overflow-x:auto;scroll-snap-type:x mandatory;scrollbar-width:none;padding-bottom:6px}
.axl .track::-webkit-scrollbar{display:none}
.axl .nav{position:absolute;top:34%;width:42px;height:42px;border-radius:50%;border:1px solid var(--ln);background:#fff;cursor:pointer;font-size:18px;z-index:2}.axl .nav.l{left:-14px}.axl .nav.r{right:-14px}
.axl .pc{display:block;text-decoration:none;scroll-snap-align:start;color:var(--ink)}
.axl .pc-im{position:relative;aspect-ratio:1/1;overflow:hidden;background:var(--iv)}.axl .pc-im img{width:100%;height:100%;object-fit:cover;transition:opacity .45s}
.axl .pc-im .alt{position:absolute;inset:0;opacity:0}.axl .pc:hover .pc-im .alt{opacity:1}
.axl .badge{position:absolute;left:10px;top:10px;background:var(--bu);color:#F3E3C0;font-size:11px;letter-spacing:.12em;padding:5px 10px}
.axl .pc-k{font-size:11px;letter-spacing:.3em;color:#9A7B2E;margin:14px 0 4px;text-transform:uppercase}
.axl .pc-n{font-family:"Songti TC","Noto Serif TC",serif;font-size:16px;font-weight:600;line-height:1.5;margin:0 0 6px}
.axl .pc-p{margin:0;font-size:14.5px}.axl .pc-p b{font-weight:600}.axl .pc-p span{display:block;color:var(--bu);font-size:13px}
.axl .pc-pp{margin:2px 0 0;font-size:12.5px;color:#9A8f7e}
.axl .row{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:32px;align-items:stretch;margin:0 0 56px}
.axl .row.rev{grid-template-columns:minmax(0,7fr) minmax(0,5fr)}.axl .row.rev .bn{order:2}
.axl .bn{position:relative;min-height:420px;overflow:hidden;background:#111;color:#fff;display:flex;align-items:flex-end}
.axl .bn img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.78}
.axl .bn .in{position:relative;padding:28px;background:linear-gradient(transparent,rgba(0,0,0,.65));width:100%}
.axl .bn small{letter-spacing:.38em;font-size:11px;color:#E9D29A}.axl .bn h3{font-family:"Songti TC","Noto Serif TC",serif;font-size:26px;font-weight:600;margin:6px 0 6px;color:#fff}
.axl .bn p{font-size:14px;color:#EFE7D6;margin:0 0 14px}.axl .bn a{color:#fff;font-size:13.5px;letter-spacing:.14em;border-bottom:1px solid #E9D29A;text-decoration:none}
.axl .grid3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:22px;align-content:start}
.axl .finder{max-width:760px;margin:0 auto 26px;display:flex;gap:10px;justify-content:center;flex-wrap:wrap;align-items:center}
.axl .finder input{width:140px;padding:12px 14px;border:1px solid var(--ln);font-size:16px}.axl .finder .res{flex-basis:100%;text-align:center;color:var(--g);font-weight:600;min-height:1.6em}
.axl table.px{width:100%;max-width:900px;margin:0 auto;border-collapse:collapse;font-size:14.5px}
.axl table.px th{background:var(--g);color:#F3EBD6;font-weight:600;text-align:left;padding:11px 14px;letter-spacing:.06em}
.axl table.px td{border-bottom:1px solid var(--ln);padding:10px 14px}.axl table.px tr.gap td{background:#FFF8E6}
.axl .occ{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:20px}
.axl .oc{border:1px solid var(--ln);padding:24px 22px;background:#fff}.axl .oc h3{font-family:"Songti TC","Noto Serif TC",serif;font-size:19px;margin:0 0 8px}.axl .oc p{font-size:14px;color:var(--sub);margin:0 0 14px}
.axl .oc a{font-size:13px;letter-spacing:.12em;color:var(--g);text-decoration:none;border-bottom:1px solid var(--g)}
.axl .dish{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:26px}
.axl .ds img{width:100%;height:auto;border:1px solid var(--ln);padding:4px;background:#fff}.axl .ds h3{font-family:"Songti TC","Noto Serif TC",serif;font-size:17px;margin:12px 0 4px}.axl .ds p{font-size:13.5px;color:var(--sub);margin:0;font-style:italic}
.axl .xs{display:inline-flex;align-items:center;gap:6px;background:linear-gradient(180deg,#A65A52,#8A453F);color:#EBD6A0;font-size:10.5px;letter-spacing:.2em;padding:5px 12px;box-shadow:inset 0 2px 0 rgba(235,214,160,.85),inset 0 -2px 0 rgba(235,214,160,.85)}.axl .xs svg{width:11px;height:11px}
.axl .split{display:grid;grid-template-columns:1fr 1fr;align-items:center;gap:0;background:var(--iv)}
.axl .split img{width:100%;height:100%;min-height:360px;object-fit:cover}.axl .split .tx{padding:clamp(28px,5vw,64px)}
.axl .split h2{font-family:"Songti TC","Noto Serif TC",serif;font-size:clamp(22px,2.8vw,30px);margin:0 0 12px}.axl .split p,.axl .split li{color:var(--sub);font-size:15px}.axl .split ul{padding-left:18px;margin:0 0 18px}
.axl .wide{position:relative;min-height:420px;display:flex;align-items:center;justify-content:center;text-align:center;color:#fff;overflow:hidden;background:#111}
.axl .wide img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.55}.axl .wide .in{position:relative;max-width:640px;padding:40px 24px}
.axl .wide h2{font-family:"Songti TC","Noto Serif TC",serif;font-size:clamp(24px,3.4vw,36px);margin:0 0 10px;color:#fff}.axl .wide p{color:#EFE7D6;margin:0 0 20px}
.axl .faq{max-width:860px;margin:0 auto}.axl details{border-top:1px solid var(--ln);padding:16px 4px}.axl details:last-child{border-bottom:1px solid var(--ln)}
.axl summary{cursor:pointer;font-family:"Songti TC","Noto Serif TC",serif;font-size:17px;font-weight:600;list-style:none;display:flex;justify-content:space-between;gap:14px}
.axl summary::-webkit-details-marker{display:none}.axl summary:after{content:"+";color:var(--gd);font-size:22px;line-height:1}.axl details[open] summary:after{content:"−"}
.axl details p{margin:10px 0 0;color:var(--sub);font-size:15px}
.axl .end{text-align:center;padding:56px 24px;background:var(--iv)}
.axl .sf{display:inline-block;width:16px;color:var(--gd);vertical-align:middle;margin:0 8px}
@media(max-width:980px){.axl .track{grid-auto-columns:calc((100% - 24px)/2)}.axl .row,.axl .row.rev{grid-template-columns:1fr}.axl .row.rev .bn{order:0}.axl .bn{min-height:320px}.axl .occ{grid-template-columns:1fr 1fr}.axl .dish{grid-template-columns:1fr 1fr}.axl .split{grid-template-columns:1fr}}
@media(max-width:640px){.axl .w{padding:0 16px}.axl .track{grid-auto-columns:78%}.axl .nav{display:none}.axl .grid3{grid-template-columns:1fr 1fr;gap:14px}.axl .occ{grid-template-columns:1fr}.axl .dish{grid-template-columns:1fr 1fr;gap:14px}.axl table.px{font-size:13.5px}.axl table.px td,.axl table.px th{padding:9px 8px}}
'''
def series_row(s, i):
    rev = ' rev' if i % 2 else ''
    return (f'<div class="row{rev}" id="{s["id"]}"><div class="bn"><img src="{s["img"]}" alt="{s["name"]}．{s["full"]}" loading="lazy"><div class="in">'
            f'<small>CHRISTMAS SET {i + 1:02d}</small><h3>{s["name"]}．{s["full"]}</h3><p>{s["desc"]}</p><a href="{C}{s["slug"]}/">查看系列全部套餐 →</a></div></div>'
            f'<div class="grid3">' + ''.join(card(s, a, b, pr) for a, b, pr in s['rows']) + '</div></div>')
# ---- 借用 Option B 的區塊（2x2 系列方格、開箱圓點、三個系列格、寶藏箱單品）----
if __name__ == '__main__':
    import subprocess, sys
    subprocess.run([sys.executable, str(HERE / 'build_b_christmas.py')], check=True)
    _BD = {'__file__': str(HERE / 'build_b_christmas.py')}
    exec((HERE / 'build_b_christmas.py').read_text(encoding='utf-8').split("\npage = f'''")[0], _BD)
    _bp = (HERE / 'b-christmas.html').read_text(encoding='utf-8')
    def _cut(start):
        i = _bp.index(start); return _bp[i:_bp.index('</section>', i) + 10]
    B_TILES = _cut('<section class="sec" id="sets"').replace('id="sets"', 'id="series"', 1)
    B_LOOK = _cut('<section class="sec"><div class="w"><h2 class="st">開箱')
    B_FEAT = _cut('<section class="sec" style="border-top:1px solid var(--ln)"><div class="w"><div class="pd">').replace('style="border-top:1px solid var(--ln)"', 'id="feature"', 1)
    B_COLS = ''.join(_BD['collection'](s, crumb=False) for s in (SER[2], SER[1], SER[0]))
    CSS += _BD['CSS'] + '.axl .bxl{background:transparent;font-size:16px}.axl .bxl details{padding:0}.axl .bxl .col:first-child{border-top:0;margin-top:0;padding-top:0}.axl .bxl summary{font-weight:400}\n'
# ---- 統一字款（跟 b-christmas）：全頁明體／Baskerville，英文眉題、按鈕、標籤、價錢用 Helvetica Neue 粗體 ----
SERIF = '"Baskerville","Songti TC","Noto Serif TC","PMingLiU",Georgia,serif'
SANS = '"Helvetica Neue","PingFang HK",Arial,sans-serif'
CSS += (f'.axl{{font-family:{SERIF}}}'
        f'.axl h1,.axl h2,.axl h3,.axl h4,.axl p,.axl li,.axl td,.axl summary,.axl .ser,.axl .hero h1,.axl .intro h2,.axl .sh h2,.axl .pc-n,.axl .bn h3,.axl .oc h3,.axl .ds h3,.axl .split h2,.axl .wide h2,.axl summary{{font-family:{SERIF}}}'
        '.axl h1,.axl h2,.axl h3,.axl .hero h1,.axl .intro h2,.axl .sh h2,.axl .pc-n,.axl .bn h3,.axl .oc h3,.axl .ds h3,.axl .split h2,.axl .wide h2,.axl summary{font-weight:400}'
        '.axl button,.axl input,.axl select{font-family:inherit}'
        f'.axl .btn,.axl .pc-k,.axl .badge,.axl .xs,.axl .hero small,.axl .sh small,.axl .bn small,.axl .bn a,.axl .oc a,.axl table.px th,.axl .pc-p b,.axl .bxl .k,.axl .bxl .bt,.axl .bxl .vd,.axl .bxl .tag,.axl .bxl .pr .now,.axl .bxl .pd .p2,.axl .bxl .pd summary,.axl .bxl .px th,.axl .bxl .oc a{{font-family:{SANS}}}'
        '.axl .btn,.axl .badge,.axl .xs,.axl table.px th{font-weight:700;text-transform:uppercase}.axl .pc-k,.axl .hero small,.axl .sh small,.axl .bn small{font-weight:800}.axl .pc-p b{font-weight:700;letter-spacing:.06em}\n'
        # 手機優化
        '@media(max-width:640px){.axl .bar{font-size:11.5px;padding:8px 12px}.axl .crumb{padding:10px 0;font-size:11.5px}'
        '.axl .hero{height:540px}.axl .hero .in{padding:28px 18px}.axl .hero h1{font-size:25px}.axl .hero p{font-size:14px}'
        '.axl .btn{padding:12px 18px;font-size:12px;letter-spacing:.1em;margin:0 6px 8px 0}.axl .eb{font-size:13.5px;padding:12px}'
        '.axl .intro{padding:36px 18px 12px}.axl .intro p{font-size:14.5px;text-align:left}.axl .intro h2,.axl .sh h2{font-size:23px}'
        '.axl .pills{flex-wrap:nowrap;overflow-x:auto;justify-content:flex-start;scrollbar-width:none;padding:6px 16px 12px}.axl .pills a{white-space:nowrap;flex:0 0 auto;font-size:13px;padding:7px 14px}'
        '.axl section.s{padding:40px 0}.axl .sh{margin-bottom:22px}.axl .sh p{font-size:14px}.axl .pc-n{font-size:15px}'
        '.axl .finder input{width:120px}.axl table.px th:nth-child(3),.axl table.px td:nth-child(3){font-size:12.5px}'
        '.axl .oc{padding:20px 18px}.axl .ds h3{font-size:15px}.axl .ds p{font-size:12.5px}'
        '.axl .split img{min-height:240px}.axl .split .tx{padding:28px 18px}.axl .wide{min-height:360px}'
        '.axl summary{font-size:15.5px}.axl details p{font-size:14px}.axl .end{padding:40px 18px}.axl .end .btn{display:block;margin:0 auto 10px;max-width:280px}'
        '.axl .bxl .mg{padding:0}.axl .bxl .look .lk-card .bt{display:block;text-align:center}}\n')
page = f'''<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>聖誕到會 2026｜聖誕大餐外賣及派對套餐｜Kitchen AO</title>
<meta name="description" content="Kitchen AO 2026 聖誕到會套餐：5 至 100 人，原隻黃油雞、寶箱煙燻牛翼板肉及八款聖誕新菜，公司聖誕派對及家庭聚會皆宜。11 月 30 日前 MEGA79 七九折。">
<style>body{{margin:0}}{CSS}</style><script type="application/ld+json">{LD}</script></head><body>
<div class="axl">
<div class="bar"><b>Mega Early Bird</b>｜聖誕套餐輸入優惠碼 <b>MEGA79</b> 享七九折，至 2026 年 11 月 30 日 23:59</div>
<div class="w crumb"><a href="https://aoaodelivery.com/">首頁</a> / <a href="https://aoaodelivery.com/catering/">到會場景</a> / 聖誕到會</div>
<div class="hero"><img src="{IMG['chk1']}" alt="聖誕到會 2026：燒南乳香慢煮原隻黃油雞聖誕套餐"><div class="in"><div class="w" style="padding:0">
<small>CHRISTMAS 2026 · KITCHEN AO</small><h1>聖誕到會 2026｜聖誕大餐外賣及派對套餐</h1>
<p>原隻黃油雞、寶箱煙燻牛翼板肉及八款聖誕新菜，5 至 100 人聖誕派對一站配搭，送到你的餐桌。</p>
<a class="btn p" href="#sets">選購聖誕套餐</a><a class="btn o" href="{WA}" target="_blank" rel="noopener">WhatsApp 查詢</a></div></div></div>
<div class="eb">早鳥優惠：輸入 <b>MEGA79</b> 聖誕套餐享七九折（21% OFF）<span class="cd" id="axl-cd"></span></div>
<div class="intro"><h2 class="ser">2026 聖誕到會套餐</h2>
<p>Kitchen AO 聖誕到會套餐專為 5 至 100 人的聖誕聚會而設，由家庭聖誕大餐、好友派對到公司聖誕派對，都可以按人數揀選。今年三大系列分別以寶箱煙燻慢煮美國牛翼板肉、燒南乳香慢煮原隻黃油雞為主角，配前菜、沙律、意粉及飯和甜品，一份聖誕到會餐單就能照顧全場賓客。</p>
<p>平安夜及聖誕節是全年聖誕訂餐高峰，送貨時段有限，建議盡早預訂。</p></div>
<nav class="pills"><a href="#top">精選推介</a><a href="#beef">聖誕寶藏箱</a><a href="#chk">聖誕金雞獻禮</a><a href="#dbl">聖誕開箱雙寶</a><a href="#pax">按人數揀</a><a href="#occ">按場合揀</a><a href="#new">聖誕新菜</a><a href="#delivery">送貨安排</a><a href="#faq">常見問題</a></nav>
<section class="s" id="top"><div class="w"><div class="sh"><small>OUR TOP PICKS</small><h2>聖誕到會精選推介</h2><p>由 5 人家庭聖誕大餐到 100 人公司聖誕派對，先看最受歡迎的六款聖誕套餐。</p></div>
<div class="rail"><button class="nav l" type="button" aria-label="上一個">‹</button><div class="track">{"".join(card(*t) for t in TOP)}</div><button class="nav r" type="button" aria-label="下一個">›</button></div></div></section>
<div class="bxl">{B_TILES}{B_LOOK}</div>
<section class="s" id="sets"><div class="w"><div class="sh"><small>CHRISTMAS SETS</small><h2>三大聖誕套餐系列</h2><p>全部套餐均可自由配搭菜式，部分精選菜式需另加差價。</p></div>
<div class="bxl">{B_COLS}</div></div></section>
<div class="bxl">{B_FEAT}</div>
<section class="s" id="pax" style="background:var(--iv)"><div class="w"><div class="sh"><small>FIND YOUR SET</small><h2>按人數揀聖誕套餐</h2><p>輸入出席人數，即時建議合適的聖誕到會套餐。</p></div>
<div class="finder"><input id="axl-n" type="number" min="1" max="999" inputmode="numeric" placeholder="例如 20"><button class="btn p" type="button" id="axl-go" style="margin:0">建議套餐</button><div class="res" id="axl-res"></div></div>
<table class="px"><thead><tr><th>出席人數</th><th>建議套餐</th><th>另一選擇</th></tr></thead><tbody>
{"".join(f'<tr{" class=gap" if c else ""}><td>{a}</td><td>{b}</td><td>{c}</td></tr>' for a, b, c in PAX)}</tbody></table></div></section>
<section class="s" id="occ"><div class="w"><div class="sh"><small>FOR EVERY OCCASION</small><h2>聖誕到會推介：按場合揀套餐</h2></div>
<div class="occ">{"".join(f'<div class="oc"><h3>{t}</h3><p>{d}</p><a href="{u}">{l} →</a></div>' for t, d, u, l in OCC)}</div></div></section>
<section class="s" id="new"><div class="w"><div class="sh"><span class="xs">{SNOW}XMAS SPECIAL</span><h2 style="margin-top:14px">2026 聖誕新菜</h2><p>今年聖誕套餐全新加入的前菜、沙律、意粉及飯和甜品。</p></div>
<div class="dish">{"".join(f'<div class="ds"><img src="{IMG[k]}" alt="{n}" loading="lazy"><h3>{n}</h3><p>{d}</p></div>' for k, n, d in DISH)}</div></div></section>
<section class="s" id="addon" style="padding-top:0;border-top:0"><div class="w"><div class="sh"><small>ADD-ONS</small><h2>聖誕小食及甜品加配</h2><p>人數較多或想更豐富，可加配單點小食及甜品。</p></div>
<div class="occ"><div class="oc"><h3>惹味小食</h3><p>雞翼、迷你漢堡、九層塔香酥雞等派對熱門小食。</p><a href="https://aoaodelivery.com/product-category/a-la-carte/snacks/">選購小食 →</a></div>
<div class="oc"><h3>甜品</h3><p>馬卡龍、芝士撻等一口甜品，為聖誕派對作結。</p><a href="https://aoaodelivery.com/product-category/a-la-carte/dessert/">選購甜品 →</a></div>
<div class="oc"><h3>派對用品</h3><p>餐具、暖貼及三層食物架，方便擺放及保溫。</p><a href="https://aoaodelivery.com/product-category/party-supplies/">選購用品 →</a></div>
<div class="oc"><h3>聖誕神秘加配</h3><p>聖誕樹芝士火腿拼盤，派對焦點冷盤，上桌即成拍照焦點。</p><a href="#sets">於套餐內加配 →</a></div></div></div></section>
<section class="split" id="delivery"><img src="{IMG['beef']}" alt="平安夜及聖誕節到會送貨安排" loading="lazy"><div class="tx"><small style="letter-spacing:.38em;font-size:11.5px;color:#9A7B2E">DELIVERY</small>
<h2>平安夜及聖誕節送貨安排</h2><ul><li>平安夜（12 月 24 日）及聖誕節（12 月 25 日）熱門時段較快額滿，宜盡早確定日期及時間。</li><li>預留至少 30 分鐘緩衝時間，避免開餐與送貨時間太接近。</li><li>落單時寫清楚收貨人、電話及大廈資料；Party Room、辦公室及學校請先確認收貨安排。</li></ul>
<a class="btn d" href="https://aoaodelivery.com/delivery/">查看送貨需知</a></div></section>
<section class="wide" id="corp"><img src="{IMG['rice']}" alt="公司聖誕派對到會" loading="lazy"><div class="in"><small style="letter-spacing:.38em;font-size:11.5px;color:#E9D29A">CORPORATE</small>
<h2>公司聖誕派對到會</h2><p>部門聚餐、年終派對及客戶活動，按人數配搭聖誕套餐，可索取正式報價及收據。</p>
<a class="btn p" href="https://aoaodelivery.com/corporate-catering-hk/">公司到會方案</a><a class="btn o" href="https://aoaodelivery.com/catering-quote-enquiry/">到會報價查詢</a></div></section>
<section class="s" id="faq"><div class="w"><div class="sh"><small>FAQ</small><h2>聖誕到會常見問題</h2></div><div class="faq">
{"".join(f'<details{" open" if i == 0 else ""}><summary>{q}</summary><p>{a}</p></details>' for i, (q, a) in enumerate(FAQ))}</div></div></section>
<div class="end"><p class="ser" style="font-size:22px;margin:0 0 6px">今年聖誕，交給 Kitchen AO</p><p style="color:var(--sub);margin:0 0 18px">5 至 100 人聖誕到會套餐，11 月 30 日前 MEGA79 七九折。</p>
<a class="btn p" href="#sets">選購聖誕套餐</a><a class="btn d" href="{WA}" target="_blank" rel="noopener">WhatsApp 查詢</a></div>
</div>
<script>(function(){{var end=new Date('2026-11-30T23:59:59+08:00').getTime(),cd=document.getElementById('axl-cd');function t(){{var s=Math.max(0,Math.floor((end-Date.now())/1000));if(!cd)return;cd.textContent=s?'｜尚餘 '+Math.floor(s/86400)+' 天 '+Math.floor(s%86400/3600)+' 小時':'';}}t();setInterval(t,60000);
document.querySelectorAll('.axl .rail').forEach(function(r){{var tr=r.querySelector('.track');r.querySelectorAll('.nav').forEach(function(b){{b.addEventListener('click',function(){{tr.scrollBy({{left:(b.classList.contains('l')?-1:1)*tr.clientWidth*.8,behavior:'smooth'}})}})}})}});
var S=[[5,6,'5-6 人套餐（寶藏箱 HK$1,928／金雞獻禮 HK$1,688）'],[8,10,'8-10 人套餐（寶藏箱 HK$3,028／金雞獻禮 HK$2,788）'],[12,16,'12-16 人套餐（寶藏箱 HK$4,588／金雞獻禮 HK$4,248）'],[18,22,'18-22 人套餐（寶藏箱 HK$5,888／金雞獻禮 HK$5,388）'],[26,30,'26-30 人套餐（寶藏箱 HK$7,888／金雞獻禮 HK$7,388）'],[35,40,'35-40 人套餐（寶藏箱 HK$9,888／金雞獻禮 HK$9,288）'],[48,54,'48-54 人開箱雙寶（HK$12,418）'],[63,68,'63-68 人開箱雙寶（HK$15,368）'],[78,85,'78-85 人開箱雙寶（HK$19,548）'],[90,100,'90-100 人開箱雙寶（HK$22,888）']];
function go(){{var n=parseInt(document.getElementById('axl-n').value,10),r=document.getElementById('axl-res');if(!n||n<1){{r.textContent='請輸入人數';return;}}if(n>100){{r.textContent='100 人以上請經到會報價查詢聯絡我們';return;}}
for(var i=0;i<S.length;i++){{if(n<=S[i][1]){{r.textContent=(n>=S[i][0]?'建議：':'建議：')+S[i][2]+(n<S[i][0]&&i>0?'，或 '+S[i-1][0]+'-'+S[i-1][1]+' 人套餐加配單點':'');return;}}}}}}
var L=document.getElementById('bxl-look');if(L){{var sl=L.querySelectorAll('.ls'),pp=L.querySelectorAll('.pips i'),cur=0;
function show(i){{cur=(i+sl.length)%sl.length;sl.forEach(function(s,k){{s.hidden=k!==cur}});pp.forEach(function(p,k){{p.className=k===cur?'on':''}});}}
pp.forEach(function(p,k){{p.addEventListener('click',function(){{show(k)}})}});L.querySelectorAll('.arw').forEach(function(b){{b.addEventListener('click',function(){{show(cur+ +b.dataset.d)}})}});
sl.forEach(function(s){{s.querySelectorAll('.dot').forEach(function(d){{d.addEventListener('click',function(){{s.querySelectorAll('.dot').forEach(function(x){{x.classList.toggle('on',x===d)}});s.querySelectorAll('.lc').forEach(function(c){{c.hidden=c.dataset.p!==d.dataset.p}})}})}})}});}}
document.getElementById('axl-go').addEventListener('click',go);document.getElementById('axl-n').addEventListener('keydown',function(e){{if(e.key==='Enter')go();}});}})();</script>
</body></html>'''
(HERE / 'a-christmas.html').write_text(page, encoding='utf-8')
print('ok', len(page))
# ---- WordPress 版：只保留 <style>、FAQ 結構化數據、內容及互動 JS，直接貼入 WPBakery Raw HTML ----
import re as _re
_st = _re.search(r'<style>.*?</style>', page, _re.S).group(0).replace('body{margin:0}', '')
_ld = _re.search(r'<script type="application/ld\+json">.*?</script>', page, _re.S).group(0)
_bd = page[page.index('<body>') + 6:page.index('</body>')].strip()
# ---- 中英自動切換：中文區塊 .ao-zh、英文區塊 .ao-en（data-no-translation），按 <html lang> 顯示 ----
import json as _json, sys as _sys
_sys.path.insert(0, str(HERE)); import en_christmas as EN
_CJK = _re.compile(r'[㐀-鿿]')
_js_i = _bd.rindex('<script>'); _js = _bd[_js_i:]; _html = _bd[:_js_i]
_miss = []
def _t(x):
    r = EN.tr(x)
    if r is None: _miss.append(x); return x
    return r
def _tr_text(seg):
    s = seg.strip()
    if not _CJK.search(s): return seg
    i = seg.index(s); return seg[:i] + _t(s) + seg[i + len(s):]
def _tr_tag(tag):
    tag = _re.sub(r'(alt|aria-label|placeholder)="([^"]*)"', lambda m: f'{m[1]}="{_t(m[2])}"' if _CJK.search(m[2]) else m[0], tag)
    tag = _re.sub(r'\bid="([^"]+)"', r'id="\1-en"', tag)
    tag = _re.sub(r'href="#([^"]+)"', r'href="#\1-en"', tag)
    tag = tag.replace('href="https://aoaodelivery.com/', 'href="https://aoaodelivery.com/en/')
    return tag
_en_html = ''.join(_tr_tag(p) if p.startswith('<') else _tr_text(p) for p in _re.split(r'(<[^>]+>)', _html))
_en_html = _en_html.replace(WA.split('?text=')[1], urllib.parse.quote("Hi, I'd like to enquire about Christmas catering sets."))
_en_js = _re.sub(r"'([^']*[㐀-鿿][^']*)'", lambda m: "'" + _t(m[1]).replace("'", "\\'") + "'", _js)
_en_js = _re.sub(r"getElementById\('([\w-]+)'\)", r"getElementById('\1-en')", _en_js).replace("'.axl .rail'", "'.ao-en .axl .rail'")
_zh_js = _js.replace("'.axl .rail'", "'.ao-zh .axl .rail'")
assert not _miss, _miss
_left = [x for x in _CJK.findall(_en_html + _en_js)]
assert not _left, ''.join(_left)[:200]
_ld_en = _json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": EN.D[q], "acceptedAnswer": {"@type": "Answer", "text": EN.D[a]}} for q, a in FAQ]}, ensure_ascii=False)
_ld_js = ('<script>(function(){var en=/^en/i.test(document.documentElement.lang||""),s=document.createElement("script");s.type="application/ld+json";'
          f's.text=en?{_json.dumps(_ld_en, ensure_ascii=False)}:{_json.dumps(LD, ensure_ascii=False)};document.head.appendChild(s);}})();</script>')
BIL = ('<style>html[lang^="en"] .ao-zh{display:none!important}html:not([lang^="en"]) .ao-en{display:none!important}'
       # 全闊：不論 theme 容器多闊，都撐滿整個視窗
       'html,body{overflow-x:clip}.ao-zh>.axl,.ao-en>.axl{width:100vw;max-width:100vw;margin-left:calc(50% - 50vw);margin-right:calc(50% - 50vw)}</style>')
_bil_body = (f'<div class="ao-zh" data-no-translation>\n{_html.strip()}\n</div>\n<div class="ao-en" data-no-translation>\n{_en_html.strip()}\n</div>\n'
             # 只保留當前語言：另一語言整段從頁面移除（Google 渲染後只有一組 H1–H4）
             + '<script>(function(){var en=/^en/i.test(document.documentElement.lang||"");var r=document.querySelector(en?".ao-zh":".ao-en");if(r)r.parentNode.removeChild(r);})();</script>\n'
             + _zh_js.replace('<script>(function(){', '<script>(function(){if(!document.querySelector(".ao-zh .axl"))return;', 1)
             + '\n' + _en_js.replace('<script>(function(){', '<script>(function(){if(!document.querySelector(".ao-en .axl"))return;', 1) + '\n' + _ld_js)
# 英文預覽版（獨立檔，lang=en）
_en_page = ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>Christmas Catering 2026 | Christmas Dinner Delivery &amp; Party Sets | Kitchen AO</title>'
            f'<style>body{{margin:0}}</style>{_st}{BIL}</head><body>{_bil_body}</body></html>')
(HERE / 'a-christmas-en.html').write_text(_en_page, encoding='utf-8')
wp = ('<!-- Kitchen AO 聖誕到會場景頁 /catering/christmas/ ：整段貼入 WPBakery Raw HTML。中文頁顯示中文，/en/ 頁自動顯示英文。'
      'Title／Meta／Focus KW 請在 Rank Math 及 TranslatePress 設定。 -->\n' + _st + '\n' + BIL + '\n' + _bil_body + '\n')
(HERE / 'wp').mkdir(exist_ok=True)
(HERE / 'wp' / 'a-christmas-wp.html').write_text(wp, encoding='utf-8')
print('wp ok', len(wp))
