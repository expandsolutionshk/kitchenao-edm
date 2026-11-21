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
      desc='本地原隻黃油雞以南乳醃製及鹽水浸漬，低溫慢煮後高溫炙燒至皮脆肉嫩，配聖誕玫瑰金巴利汁，專屬木箱盛載，全港限量 100 個。',
      rows=[(5, 6, 1688), (8, 10, 2788), (12, 16, 4248), (18, 22, 5388), (26, 30, 7388), (35, 40, 9288)]),
 dict(id='dbl', name='聖誕開箱雙寶', full='燒南乳香慢煮原隻黃油雞 × 煙燻慢煮美國牛翼板肉', slug='twin-treasures-chicken-beef', img=IMG['chk1'], img2=IMG['beef'],
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
DISH = [('ris', '玫瑰醬泡菜海蝦意大利飯', '韓式玫瑰醬配泡菜，奶香柔和、微辣開胃'), ('puff', '芒果粟子蓉冬日酥盒', '日本栗子蓉配新鮮芒果粒，酸甜開胃的前菜'), ('rice', '雙重龍蝦三重芝士煲仔鍋飯', '原個布袋芝士切開即流心，飯底吸滿濃郁龍蝦汁'), ('tart', '聖誕馴鹿脆脆開心果朱古力撻', '開心果白朱古力配脆脆，朱古力曲奇鹿角'), ('salad', '紅寶神石榴沙律系列', '大蝦柚肉或煙火雞胸蜜桃兩款任選'), ('cro', '明太子芝士忌廉牛角酥', '牛角酥夾入明太子芝士忌廉，鹹香柔滑')]
OCC = [('公司聖誕派對', '部門聚餐、年終派對及客戶活動，按人數揀套餐，可索取正式報價。', 'https://aoaodelivery.com/catering-quote-enquiry/', '到會報價查詢'),
       ('家庭聖誕聚會', '5 至 10 人小型套餐，一款原隻主菜配前菜、沙律、主食及甜品，在家輕鬆開餐。', '#sets', '揀家庭聖誕套餐'),
       ('學校、教會及機構', '人數較多、年齡層闊，可加配兒童及素食選擇，並預先統計飲食需要。', 'https://aoaodelivery.com/catering-quote-enquiry/', '到會報價查詢'),
       ('素食朋友', '套餐以外可加配素食菜式，或選擇「素」味人生素食到會套餐。', 'https://aoaodelivery.com/product-category/party/vegetarians-set/', '素食到會套餐')]
FAQ = [
 ('聖誕到會要提早幾多日預訂？', '平安夜及聖誕節是全年到會高峰，熱門送貨時段較快額滿，建議盡早預訂。2026 年 11 月 30 日 23:59 前輸入優惠碼 MEGA79，聖誕套餐更可享七九折。'),
 ('聖誕套餐甚麼日子供應？', '聖誕套餐於 2026 年 12 月 12 日至 12 月 27 日供應及送貨。12 月 19 日前，其他套餐及單點照常供應；除企業訂單外，其他日子不供應聖誕套餐。供應情況會持續於網站更新，請留意送貨需知。'),
 ('平安夜及聖誕節可以送貨嗎？', '可以按落單頁面提供的日期及時段送貨。平安夜（12 月 24 日）及聖誕節（12 月 25 日）時段有限，建議預留至少 30 分鐘緩衝時間，詳情可參考送貨需知。'),
 ('聖誕到會套餐每位大約幾錢？', 'Kitchen AO 2026 聖誕套餐以原價計，每位約 HK$226 至 386，人數愈多每位愈低；11 月 30 日前以 MEGA79 再享七九折。'),
 ('聖誕大餐吃什麼？', '一桌完整的聖誕大餐一般包括一至兩款焦點主菜（例如原隻燒雞或燒牛肉）、前菜、沙律、意粉或飯，以及甜品。Kitchen AO 的聖誕大餐到會套餐已按人數配搭好以上各類菜式。'),
 ('聖誕套餐有沒有火雞？', '2026 年聖誕套餐的主菜為燒南乳香慢煮原隻黃油雞及寶箱煙燻慢煮美國牛翼板肉。如有其他主菜需要，歡迎 WhatsApp 查詢。'),
 ('10 人或 20 人聖誕派對應揀哪個套餐？', '10 人可選 8-10 人套餐；20 人可選 18-22 人套餐。人數介乎兩個套餐之間時，可選較大的套餐，或選較小的套餐再加配單點小食，詳見上方「按人數揀聖誕套餐」。'),
 ('聖誕套餐的菜式可以更換嗎？', '套餐菜式可按喜好自由配搭；部分精選菜式需另加差價，實際價錢以落單頁面選項為準。'),
 ('可以加素食或兒童菜式嗎？', '可以在套餐以外加配單點小食及甜品，素食朋友亦可選擇「素」味人生素食到會套餐。'),
 ('聖誕 party 到會可以送到 Party Room 或辦公室嗎？', '可以。聖誕到會外賣會送到指定地址樓下或車輛可停泊的位置；Party Room、辦公室及學校請先確認收貨安排。無論是聖誕外賣到會還是聖誕套餐到會，都建議預留至少 30 分鐘緩衝時間。'),
 ('公司聖誕派對可以索取報價嗎？', '可以。公司、學校及機構訂購如需正式報價及收據，可經到會報價查詢聯絡我們。'),
 ('聖誕到會包括餐具嗎？', '落單時可選擇是否需要碟及餐具，亦可加配食物夾等用品。'),
]
LD = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}, ensure_ascii=False)
SNOW = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2v20M3.3 7l17.4 10M3.3 17L20.7 7M12 5l-2-2M12 5l2-2M12 19l-2 2M12 19l2 2" stroke="currentColor" stroke-width="1.4" fill="none" stroke-linecap="round"/></svg>'

CSS = r'''
.axl .xav{max-width:760px;margin:18px auto 6px;background:#111;border:1px solid rgba(200,162,74,.75);color:#EDE6D8;padding:14px 18px 12px;font-family:"Helvetica Neue","PingFang HK",Arial,sans-serif}
.axl .xav-h{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;border-bottom:1px solid rgba(200,162,74,.35);padding-bottom:8px;margin-bottom:6px}
.axl .xav-h b{font-size:14.5px;letter-spacing:.08em;color:#fff;font-weight:600}
.axl .xav-h i{font-family:Baskerville,"Baskerville Old Face",Georgia,serif;font-style:italic;font-size:20px;color:#E4C77E}
.axl .xav ul{list-style:none;margin:0;padding:0}
.axl .xav li{position:relative;padding-left:20px;margin:5px 0;font-size:14px;line-height:1.7;color:#D9D2C3}
.axl .xav li:before{content:"";position:absolute;left:0;top:.42em;width:12px;height:12px;background:url("data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 24 24%27%3E%3Cg stroke=%27%23C8A24A%27 stroke-width=%271.6%27 fill=%27none%27 stroke-linecap=%27round%27%3E%3Cpath d=%27M12 2v20M3.3 7l17.4 10M3.3 17L20.7 7%27/%3E%3C/g%3E%3C/svg%3E") center/contain no-repeat}
.axl .xav a{color:#E4C77E!important;text-decoration:none;border-bottom:1px solid rgba(200,162,74,.7)}
.axl .hp{background:#111;color:#EDE6D8;text-align:center;padding:40px 20px 34px;margin:0 0 30px}
.axl .hp small{display:block;font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;font-size:11px;letter-spacing:.36em;color:#C8A24A;text-transform:uppercase}
.axl .hp .hpt{font-family:Baskerville,"Baskerville Old Face",Georgia,serif;font-style:italic;font-weight:400;font-size:34px;line-height:1.3;color:#fff;margin:14px 0 10px;letter-spacing:.02em}
.axl .hp .hpt2{font-family:Baskerville,"Baskerville Old Face",Georgia,serif;font-style:italic;font-size:21px;line-height:1.4;color:#EDE6D8;margin:0 0 10px}
.axl .hp .hpt2 span{color:#C8A24A;letter-spacing:.06em}
.axl .hp .hps{font-family:"Helvetica Neue","PingFang HK",Arial,sans-serif;font-size:14px;color:#9b948a;margin:0;line-height:1.8}
.axl .hp .hps:empty{display:none}
.axl .hp .orn{color:#C8A24A;font-size:12px;letter-spacing:.6em;margin:12px 0 0;padding-left:.6em}
.axl .hp .hph{font-family:"Helvetica Neue","PingFang HK",Arial,sans-serif;font-size:13px!important;font-weight:600;letter-spacing:.12em;color:#C8A24A;margin:12px 0 0!important;line-height:1.9}
.axl .hp .hps2{font-family:"Helvetica Neue","PingFang HK",Arial,sans-serif;font-size:13px;color:#C8A24A;letter-spacing:.12em;margin:0;line-height:1.9}
.axl .hp .hpn{font-size:13px;color:#9b948a;margin:14px 0 0}
@media(max-width:640px){.axl .hp .hpt{font-size:26px}.axl .hp .hpt2{font-size:17px}.axl .xav{margin:14px 14px 4px}}

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
.axl .intro h1,.axl .intro h2,.axl .sh h2{font-family:"Songti TC","Noto Serif TC",serif;font-weight:600;font-size:clamp(24px,3.2vw,34px);margin:0 0 14px;letter-spacing:.04em}
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
    B_TILES = B_TILES.replace('<div class="w"><div class="mg">', '<div class="w"><div class="sh tsh"><h2><span class="h2g lt">Open the Box! It&#8217;s Christmas!</span><br><span class="h2b">三大聖誕套餐系列</span></h2></div><p class="sd tsd">精心呈獻三大聖誕套餐，照顧不同聚會需要，與摯愛分享開箱的寶藏。</p><div class="mg">', 1)
    for _n, _f, _d in (('聖誕寶藏箱', '煙燻慢煮美國牛翼板肉盛宴', '適合 5 至 40 人'), ('聖誕金雞獻禮', '燒南乳香慢煮原隻黃油雞', '適合 5 至 40 人'), ('聖誕開箱雙寶', '原隻黃油雞 × 煙燻美國牛翼板肉', '適合 48 至 100 人'), ('2026 聖誕新菜', '前菜、沙律、意粉及飯和甜品', '全新菜式一覽')):
        B_TILES = B_TILES.replace(f'<span>{_n}</span>', f'<span class="tl"><b>{_n}</b><i class="tf">{_f}</i><em>{_d}</em></span>', 1)
    PANEL = '<div class="hp hpg"><p class="hpt">Open the Box! It&#8217;s Christmas!</p><p class="mt2 hpp"><span class="pr a"><span class="en">Hours to slow-cook.</span><span class="zh">慢煮數小時</span></span><span class="pr b"><span class="en">Minutes to smoke.</span><span class="zh">煙燻數分鐘</span></span><br><span class="pr c"><span class="en l2">One second to <b>WOW</b></span><span class="zh">開箱<b>驚喜</b>只需一秒</span></span></p><p class="orn">✦ ✦ ✦</p><p class="hps2">每款均可配八款 XMAS SPECIAL 全新菜式</p><p class="hpn">全部套餐均可自由配搭菜式，部分精選菜式需另加差價。</p></div>'
    B_TILES = B_TILES.replace('<a href="#top"', PANEL + '<a class="nd" href="#top"', 1) if '<a href="#top"' in B_TILES else B_TILES.replace('<a href="#new"', PANEL + '<a class="nd" href="#new"', 1)
    import re as _re0
    B_TILES = _re0.sub(r'(<a href="#dbl"><img src=")[^"]*(")', r'\1https://aoaodelivery.com/wp-content/uploads/2026/11/2026-XMAS-IG-16.jpg\2 class="ig16"', B_TILES, 1)
    B_LOOK = _cut('<section class="sec"><div class="w"><h2 class="st">開箱')
    B_FEAT = _cut('<section class="sec" style="border-top:1px solid var(--ln)"><div class="w"><div class="pd">').replace('style="border-top:1px solid var(--ln)"', 'id="feature"', 1)
    B_COLS = ''.join(_BD['collection'](s, crumb=False) for s in (SER[2], SER[1], SER[0]))
    import re
    B_COLS = re.sub(r'(href="[^"]*/(\d+)-(\d+)pax-christmas-set-[^"]*"><div class="im">.*?)<span class="tag">EARLY BIRD</span>', lambda m: m.group(1) + f'<span class="tag px"><b>{m.group(2)}–{m.group(3)}</b><i>pax</i></span>', B_COLS)
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
        '.axl .intro{padding:36px 18px 12px}.axl .intro p{font-size:14.5px;text-align:left}.axl .intro h1,.axl .intro h2,.axl .sh h2{font-size:23px}'
        '.axl .pills{flex-wrap:nowrap;overflow-x:auto;justify-content:flex-start;scrollbar-width:none;padding:6px 16px 12px}.axl .pills a{white-space:nowrap;flex:0 0 auto;font-size:13px;padding:7px 14px}'
        '.axl section.s{padding:40px 0}.axl .sh{margin-bottom:22px}.axl .sh p{font-size:14px}.axl .pc-n{font-size:15px}'
        '.axl .finder input{width:120px}.axl table.px th:nth-child(3),.axl table.px td:nth-child(3){font-size:12.5px}'
        '.axl .oc{padding:20px 18px}.axl .ds h3{font-size:15px}.axl .ds p{font-size:12.5px}'
        '.axl .split img{min-height:240px}.axl .split .tx{padding:28px 18px}.axl .wide{min-height:360px}'
        '.axl summary{font-size:15.5px}.axl details p{font-size:14px}.axl .end{padding:40px 18px}.axl .end .btn{display:block;margin:0 auto 10px;max-width:280px}'
        '.axl .bxl .mg{padding:0}.axl .bxl .look .lk-card .bt{display:block;text-align:center}}\n')
CSS += r'''
/* ---- 段落眉題：Baskerville 斜體深金（Our Top Picks 款）---- */
.axl .sh small{display:inline-block!important;font-family:Baskerville,"Baskerville Old Face","Songti TC",Georgia,serif!important;font-style:italic;font-weight:400!important;font-size:19px!important;letter-spacing:.04em!important;text-transform:none!important;background-image:linear-gradient(180deg,#C8961A 0%,#9C6C08 100%);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent!important;margin-bottom:6px!important}
.axl .sh h2:after,.axl .bxl .st:after{content:"";display:block;width:44px;height:1px;margin:14px auto 0;background:#C8961A}
@media(max-width:640px){.axl .sh small{font-size:17px!important}}
/* ---- 供應日期：全闊黑金摺合列 ---- */
.axl .xav2{background:#111;color:#EDE6D8;border-top:1px solid rgba(200,162,74,.55);border-bottom:1px solid rgba(200,162,74,.55);font-family:"Helvetica Neue","PingFang HK",Arial,sans-serif}
.axl .xav2 summary{list-style:none;cursor:pointer;display:block;padding:12px 0}
.axl .xav2 summary:after,.axl .xav2[open] summary:after{content:none!important;display:none!important}.axl .xav2 summary .w{font-family:"Helvetica Neue","PingFang HK",Arial,sans-serif}.axl .xav2 summary::-webkit-details-marker{display:none}.axl .xav2 summary::marker{content:""}
.axl .xav2 summary .w{display:flex;align-items:center;justify-content:center;gap:8px;flex-wrap:wrap;font-size:14.5px;letter-spacing:.06em;color:#fff;font-weight:600}
.axl .xav2 summary svg{flex:none;display:block}
.axl .xav2 summary i{font-family:Baskerville,"Baskerville Old Face",Georgia,serif;font-style:italic;font-weight:400;font-size:20px;color:#E4C77E;letter-spacing:.02em}
.axl .xav2 summary em{font-style:normal;font-size:12px;color:#C8A24A;letter-spacing:.14em;margin-left:14px;font-weight:600}
.axl .xav2 summary em:after{content:" ▾"}.axl .xav2[open] summary em:after{content:" ▴"}
.axl .xav2 .bd{border-top:1px solid rgba(200,162,74,.3);background:#161616;padding:12px 0 14px}
.axl .xav2 ul{list-style:none;margin:0 auto;padding:0;max-width:720px}
.axl .xav2 li{position:relative;padding-left:20px;margin:5px 0;font-size:14px;line-height:1.7;color:#D9D2C3}
.axl .xav2 li:before{content:"";position:absolute;left:0;top:.42em;width:12px;height:12px;background:url("data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 24 24%27%3E%3Cg stroke=%27%23C8A24A%27 stroke-width=%271.6%27 fill=%27none%27 stroke-linecap=%27round%27%3E%3Cpath d=%27M12 2v20M3.3 7l17.4 10M3.3 17L20.7 7%27/%3E%3C/g%3E%3C/svg%3E") center/contain no-repeat}
.axl .xav2 a{color:#E4C77E!important;text-decoration:none;border-bottom:1px solid rgba(200,162,74,.7)}
@media(max-width:640px){.axl .xav2 summary .w{font-size:13px;gap:6px}.axl .xav2 summary i{font-size:17px}.axl .xav2 summary em{margin-left:6px}.axl .xav2 li{font-size:13px}}
/* ---- Hero 動態文字（CSS motion）---- */
.axl .hero img{animation:axKB 20s ease-in-out infinite alternate;transform-origin:60% 50%}
.axl .hero .in{background:linear-gradient(transparent,rgba(0,0,0,.72) 55%)}
.axl .hero .in>.w{position:relative}
.axl .hero .m0{display:block;font-family:"Helvetica Neue",Helvetica,Arial,sans-serif!important;font-size:12px;font-weight:700;letter-spacing:.38em;text-transform:uppercase;color:#C8A24A}
.axl .hero .mt1{margin:18px 0 0!important;max-width:none}.axl .hero .mt1 .t{position:relative;display:inline-block;font-family:Baskerville,"Baskerville Old Face",Georgia,serif!important;font-style:italic;font-weight:400;font-size:clamp(30px,4.6vw,52px);line-height:1.15;color:#fff;animation:axOpen 1.5s .9s cubic-bezier(.7,0,.2,1) both}.axl .hero .mt1 .z{display:block;font-family:"Songti TC","Noto Serif TC",serif;font-size:clamp(22px,2.8vw,32px);letter-spacing:.3em;color:#E4C77E;margin-top:12px;}.axl .hero .mt1 .z1,.axl .hero .mt1 .z2{display:inline-block;animation:axUp 1.1s 2.4s cubic-bezier(.2,.6,.2,1) both}.axl .hero .mt1 .z2{animation-delay:3s}@keyframes axOpen{0%{opacity:0;clip-path:inset(0 50% 0 50%);filter:blur(4px)}100%{opacity:1;clip-path:inset(-25% -5% -25% -5%);filter:none}}@keyframes axGlow{0%{text-shadow:none}35%{text-shadow:0 0 18px rgba(240,210,130,.85),0 0 42px rgba(200,162,74,.5)}100%{text-shadow:0 0 6px rgba(200,162,74,.25)}}@keyframes axSweep{to{transform:translateX(420%) skewX(-18deg)}}
.axl .hp .mt2{font-family:Baskerville,"Baskerville Old Face",Georgia,serif!important;font-style:italic;font-size:clamp(18px,2.1vw,23px);line-height:1.45;color:#EDE6D8;margin:4px 0 6px!important}.axl .hp .mt2 .pr{margin:0 14px 8px!important;text-align:center}.axl .hp .mt2 .pr .zh{color:#9b948a}
.axl .hp .mt2 .pr{display:inline-block;vertical-align:top;margin:0 22px 6px 0}.axl .hp .mt2 .pr .en{display:block}.axl .hp .mt2 .pr .zh{display:block;font-family:"Songti TC","Noto Serif TC",serif;font-style:normal;font-size:13.5px;letter-spacing:.14em;color:#cfc7b8;margin-top:2px}.axl .hp .mt2 .pr .zh:empty{display:none}.axl .hp .mt2 .zh b{font-size:1.15em;letter-spacing:.14em}.axl .hp .mt2 .pr{opacity:0}.axl .hp.in .mt2 .pr{animation:axUpNb 1.6s .3s cubic-bezier(.2,.6,.2,1) both}.axl .hp.in .mt2 .pr.b{animation-delay:1.4s}.axl .hp.in .mt2 .pr.c{animation-delay:2.5s}
.axl .hp .mt2 .l2{font-size:1.55em;line-height:1.2}
.axl .hp .mt2 b{display:inline-block;font-weight:400;letter-spacing:.06em;background:linear-gradient(100deg,#B8913A 20%,#F6E3A6 45%,#C8A24A 60%,#B8913A 80%);background-size:250% 100%;-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent;animation:axShine 3.2s 4.6s linear infinite}.axl .hp .mt2 b{opacity:0}.axl .hp.in .mt2 b{animation:axPop 1.1s 3.4s cubic-bezier(.3,1.6,.5,1) both,axShine 3.2s 4.6s linear infinite}
.axl .hero .mt3{font-size:14px!important;color:#cfc7b8!important;margin:0!important;letter-spacing:.06em;animation:axFade 1.2s 5.1s both}
.axl .hero .mt3:empty{display:none}
.axl .hero .mln{display:block;height:1px;width:64px;background:#C8A24A;margin:16px 0 14px;transform-origin:left;animation:axLine 1s 3.7s ease-out both}
.axl .hero h1{font-size:clamp(19px,2.4vw,26px)!important;color:#EFE7D6!important;margin:0 0 16px!important;letter-spacing:.04em;animation:axFade 1s 5s both}
.axl .hero .mbt{animation:axFade 1s 3.9s both}
.axl .hero .spk{position:absolute;color:#E4C77E;font-size:14px;line-height:1;opacity:0;animation:axTw 3.6s ease-in-out infinite;pointer-events:none}
.axl .hero .spk.s1{left:58%;top:4px;animation-delay:1.8s}.axl .hero .spk.s2{left:72%;top:46px;font-size:10px;animation-delay:2.9s}.axl .hero .spk.s3{left:46%;top:-18px;font-size:9px;animation-delay:4s}
@keyframes axKB{from{transform:scale(1)}to{transform:scale(1.08)}}
@keyframes axTrack{from{opacity:0;letter-spacing:.9em}to{opacity:1;letter-spacing:.38em}}
@keyframes axUp{from{opacity:0;transform:translateY(14px);filter:blur(6px)}to{opacity:1;transform:none;filter:none}}@keyframes axUpNb{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}
@keyframes axFade{from{opacity:0}to{opacity:1}}
@keyframes axPop{0%{opacity:0;transform:scale(.6)}100%{opacity:1;transform:scale(1)}}
@keyframes axShine{from{background-position:100% 0}to{background-position:-150% 0}}
@keyframes axLine{from{transform:scaleX(0)}to{transform:scaleX(1)}}
@keyframes axTw{0%,100%{opacity:0;transform:scale(.5) rotate(0)}50%{opacity:1;transform:scale(1) rotate(45deg)}}
@media(max-width:640px){.axl .hero .m0{font-size:10.5px;letter-spacing:.3em}.axl .hero .mt1 .t{font-size:28px}.axl .hero .mt1 .z{font-size:21px;letter-spacing:.24em}.axl .hp .mt2{font-size:16px}.axl .hp .mt2 .pr{margin-right:16px}.axl .hp .mt2 .pr .zh{font-size:12px;letter-spacing:.1em}.axl .hero .mt3{font-size:13px!important}.axl .hero .mln{margin:12px 0 10px}.axl .hero h1{font-size:18px!important;margin-bottom:14px!important}.axl .hero .spk.s1{left:78%}.axl .hero .spk.s2{left:88%}.axl .hero .spk.s3{left:66%}}
@media(prefers-reduced-motion:reduce){.axl .hero *,.axl .hp *{animation:none!important;opacity:1!important}}
'''
_EB = {'OUR TOP PICKS': 'Our Top Picks', 'FIND YOUR SET': 'Find Your Set', 'FOR EVERY OCCASION': 'For Every Occasion', 'ADD-ONS': 'Add-ons'}
CSS += '/* Hero CTA：Option A 金色幼框 */.axl .hero .btn.p{background:transparent!important;border:1px solid #C8A24A!important;color:#E4C77E!important;font-size:13px;letter-spacing:.24em;padding:14px 34px;position:relative;overflow:hidden;z-index:0}.axl .hero .btn.p:before{content:"";position:absolute;inset:0;background:#C8A24A;transform:scaleX(0);transform-origin:left;transition:transform .45s cubic-bezier(.6,0,.2,1);z-index:-1}.axl .hero .btn.p:hover{color:#111!important}.axl .hero .btn.p:hover:before{transform:scaleX(1)}\n'
CSS += '/* 標題樣式：H2 gold（Our Top Picks 款）＋ H2 black */.axl .h2g{display:inline-block;font-family:Baskerville,"Baskerville Old Face","Songti TC",Georgia,serif!important;font-style:italic;font-weight:400!important;font-size:clamp(19px,2vw,24px);letter-spacing:.04em;background-image:linear-gradient(180deg,#C8961A 0%,#9C6C08 100%);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent;margin-bottom:6px}html:not([lang^="en"]) .axl .h2g{font-style:normal;letter-spacing:.12em}html:not([lang^="en"]) .axl .h2g.lt{font-style:italic;letter-spacing:.04em}.axl .h2b{display:inline-block;font-family:"Baskerville","Songti TC","Noto Serif TC","PMingLiU",Georgia,serif;font-weight:400;color:var(--ink);font-size:clamp(24px,3.2vw,34px);letter-spacing:.04em;line-height:1.35}.axl .intro h1.hh{line-height:1.2}.axl .intro h1.hh br{display:block}@media(max-width:640px){.axl .h2g{font-size:17px}.axl .h2b{font-size:23px}}\n'
CSS += '/* 手機 Hero：固定左右留白、加深底部漸暗、標題唔再因字距動畫移位 */@media(max-width:640px){.axl .hero .in{padding:28px 20px 30px!important;background:linear-gradient(180deg,rgba(0,0,0,0) 0%,rgba(0,0,0,.55) 30%,rgba(0,0,0,.86) 100%)!important}.axl .hero .in>.w{padding:0!important;margin:0!important;max-width:none!important}.axl .hero .mt1 .t{white-space:nowrap;font-size:min(28px,7.4vw)!important}.axl .hero .m0{text-shadow:0 1px 6px rgba(0,0,0,.6)}.axl .crumb{padding:10px 20px!important}}\n'
HERO_IMG = 'img/xmas-lp-hero-box-v2.jpg'
HERO_URL = 'https://aoaodelivery.com/wp-content/uploads/2026/11/xmas-lp-hero-box-v2.jpg'
CSS += '/* Hero 背景圖：寶藏箱（已去 logo），限制最大闊度，唔撐滿；文字出完先出圖 */.axl .hero{background:#000!important}.axl .hero .hbox{position:absolute;top:0;right:max(0px,calc(50% - 640px));left:auto;height:100%;aspect-ratio:4/5;max-width:min(56%,600px);opacity:0;-webkit-mask-image:linear-gradient(90deg,transparent 0,#000 1px,#000 calc(100% - 1px),transparent 100%);mask-image:linear-gradient(90deg,transparent 0,#000 1px,#000 calc(100% - 1px),transparent 100%);animation:axImg 1.4s 1.6s ease-out forwards;z-index:1}@keyframes axImg{from{opacity:0;transform:scale(1.04)}to{opacity:1;transform:scale(1)}}.axl .hero .in{background:transparent!important;top:0;display:flex;align-items:flex-end}.axl .hero .in>.w{width:100%}.axl .hero .spk{color:#F6E3A6!important;text-shadow:0 0 6px rgba(246,227,166,.8),0 0 14px rgba(200,162,74,.45);animation:axTw2 3.2s ease-in-out infinite!important}.axl .hero .spk.s1{left:62%!important;top:-40px!important;font-size:16px!important;animation-delay:.6s!important}.axl .hero .spk.s2{left:78%!important;top:30px!important;font-size:11px!important;animation-delay:1.5s!important}.axl .hero .spk.s3{left:48%!important;top:-90px!important;font-size:9px!important;animation-delay:2.3s!important}.axl .hero .spk.s4{left:90%!important;top:-120px!important;font-size:13px!important;animation-delay:3.1s!important}.axl .hero .spk.s5{left:70%!important;top:-170px!important;font-size:8px!important;animation-delay:1s!important}@keyframes axTw2{0%,100%{opacity:0;transform:scale(.3) rotate(0)}45%{opacity:1;transform:scale(1.15) rotate(45deg)}60%{opacity:1;transform:scale(1) rotate(60deg)}}@media(max-width:640px){.axl .hero{height:auto!important;display:flex;flex-direction:column}.axl .hero .hbox{position:relative;right:auto;width:100%;max-width:520px;margin:0 auto;height:auto;aspect-ratio:4/5;-webkit-mask-image:linear-gradient(180deg,#000 70%,transparent 100%);mask-image:linear-gradient(180deg,#000 70%,transparent 100%)}.axl .hero .in{position:relative!important;inset:auto!important;margin-top:-70px;background:transparent!important}.axl .hero .spk.s1{left:72%!important;top:-150px!important;font-size:14px!important}.axl .hero .spk.s2{left:86%!important;top:-60px!important}.axl .hero .spk.s3{left:12%!important;top:-210px!important}.axl .hero .spk.s4{left:40%!important;top:-260px!important}.axl .hero .spk.s5{left:60%!important;top:-320px!important}}\n'
HERO_OPEN = 'img/xmas-lp-hero-open.jpg'
HERO_OPEN_URL = 'https://aoaodelivery.com/wp-content/uploads/2026/11/xmas-lp-hero-open.jpg'
CSS += '/* 開箱互動：金鎖匙 Open it → 開箱金光、換相、出煙 */.axl .hero .hbox img.hbg{position:absolute;inset:0;width:100%!important;height:100%!important;object-fit:cover;opacity:1;margin:0}.axl .hero .hbox .h1i{object-position:50% 60%;transition:opacity 1.1s ease .35s,transform 1.4s ease .35s;animation:axKB 22s 3s ease-in-out infinite alternate;transform-origin:50% 60%}.axl .hero .hbox .h2i{object-position:50% 35%;opacity:0!important;transform:scale(1.08);transition:opacity 1.2s ease .5s,transform 2.4s cubic-bezier(.2,.7,.2,1) .5s;animation:none}.axl .hero.open .hbox .h1i{opacity:0!important;transform:scale(1.06)}.axl .hero.open .hbox .h2i{opacity:1!important;transform:scale(1)}.axl .hero .hbox.shake{animation:axShake .45s ease-in-out;opacity:1}.axl .hero.open .hbox{opacity:1;animation:none}@keyframes axShake{0%,100%{transform:none}20%{transform:rotate(-1.4deg)}40%{transform:rotate(1.2deg)}60%{transform:rotate(-.8deg)}80%{transform:rotate(.5deg)}}.axl .hero .hkey{position:absolute;left:51.5%;top:70%;transform:translate(-50%,-50%);z-index:3;display:flex;flex-direction:column;align-items:center;gap:6px;background:none;border:0;padding:8px;cursor:pointer;opacity:0;animation:axFade .8s 2s forwards}.axl .hero .hkey svg{filter:drop-shadow(0 0 6px rgba(246,227,166,.8));transition:transform .45s cubic-bezier(.3,1.5,.5,1);animation:axKey 2.4s 2.6s ease-in-out infinite}.axl .hero .hkey:before{content:"";position:absolute;left:50%;top:22px;width:58px;height:58px;margin:-29px 0 0 -29px;border:1px solid rgba(228,199,126,.7);border-radius:50%;animation:axRing 2.4s 2.6s ease-out infinite;opacity:0}.axl .hero .hkey em{font-family:Baskerville,"Baskerville Old Face",Georgia,serif;font-style:italic;font-size:15px;color:#F4E6C0;letter-spacing:.06em;text-shadow:0 1px 6px rgba(0,0,0,.8)}.axl .hero .hkey:hover svg{transform:rotate(-12deg) scale(1.1)}.axl .hero.open .hkey{opacity:0!important;pointer-events:none;transition:opacity .4s .3s}.axl .hero.open .hkey svg{transform:rotate(90deg) scale(1.15)}@keyframes axKey{0%,100%{transform:translateY(0)}50%{transform:translateY(-4px)}}@keyframes axRing{0%{opacity:.8;transform:scale(.6)}100%{opacity:0;transform:scale(1.5)}}.axl .hero .hfl{position:absolute;left:51.5%;top:62%;width:10px;height:10px;margin:-5px 0 0 -5px;border-radius:50%;background:radial-gradient(circle,rgba(255,240,200,.95),rgba(232,196,110,.55) 35%,transparent 70%);opacity:0;z-index:2;pointer-events:none}.axl .hero.open .hfl{animation:axFlash 1.4s .3s ease-out forwards}@keyframes axFlash{0%{opacity:0;transform:scale(1)}25%{opacity:1;transform:scale(40)}100%{opacity:0;transform:scale(70)}}.axl .hero .hsm{position:absolute;inset:0;z-index:2;pointer-events:none;overflow:hidden}.axl .hero .hsm i{position:absolute;left:var(--xd);top:var(--yd);width:26%;aspect-ratio:1;margin:-13% 0 0 -13%;border-radius:50%;background:radial-gradient(circle,rgba(240,236,228,.6) 0%,rgba(225,220,210,.25) 45%,transparent 70%);filter:blur(9px);opacity:0}.axl .hero.open .hsm i{animation:axSmoke 5.5s var(--dl) ease-out infinite}@keyframes axSmoke{0%{opacity:0;transform:translate(0,10%) scale(.5)}18%{opacity:.75}55%{opacity:.35}100%{opacity:0;transform:translate(10%,-150%) scale(2.2)}}@media(max-width:640px){.axl .hero .hsm i{left:var(--xm);top:var(--ym)}.axl .hero .hkey{top:72%}.axl .hero .hkey svg{width:38px;height:15px}.axl .hero .hkey em{font-size:14px}.axl .hero .hfl{top:64%}}@media(prefers-reduced-motion:reduce){.axl .hero .hsm{display:none}}\n'
CSS += '/* Open it 下面加箭嘴，指向金鎖匙 */.axl .hero .hkey .hint{position:absolute;left:50%;bottom:100%;transform:translateX(-50%);display:flex;flex-direction:column;align-items:center;gap:4px;margin-bottom:2px;white-space:nowrap}.axl .hero .hkey .arw{display:block;width:1px;height:22px;background:linear-gradient(rgba(228,199,126,0),#E4C77E);position:relative;animation:axArw 1.6s ease-in-out infinite}.axl .hero .hkey .arw:after{content:"";position:absolute;left:50%;bottom:0;width:7px;height:7px;margin-left:-4px;border-right:1px solid #E4C77E;border-bottom:1px solid #E4C77E;transform:rotate(45deg)}@keyframes axArw{0%,100%{transform:translateY(-3px);opacity:.6}50%{transform:translateY(3px);opacity:1}}\n'
CSS += '/* Open it 明顯啲 */.axl .hero .hkey svg{width:54px!important;height:21px!important;filter:drop-shadow(0 0 8px rgba(246,227,166,.95)) drop-shadow(0 0 16px rgba(200,162,74,.6))!important}.axl .hero .hkey em{font-size:19px!important;color:#F6E3A6!important;background:rgba(10,9,7,.55);padding:3px 14px 4px;border:1px solid rgba(228,199,126,.6);border-radius:20px;text-shadow:0 0 8px rgba(246,227,166,.6)!important}.axl .hero .hkey .arw{height:30px!important;width:1.5px!important}.axl .hero .hkey .arw:after{width:9px!important;height:9px!important;margin-left:-5px!important;border-width:1.5px!important}.axl .hero .hkey:before{width:72px!important;height:72px!important;margin:-36px 0 0 -36px!important;border-width:1.5px!important}@media(max-width:640px){.axl .hero .hkey em{font-size:17px!important}}\n'
CSS += '/* 精選推介：單點新菜滑動 */.axl section[id^="top"] .sh h2{margin:0 0 10px}.axl section[id^="top"] .sh .sm{font-size:14px;color:var(--sub)}.axl .dc .pc-im{border:1px solid var(--ln)}.axl .dc .pc-k{font-size:10.5px;letter-spacing:.2em;color:#9A7B2E;margin:12px 0 4px}.axl .dc .pc-n{margin:0 0 4px}.axl .dc .dcd{font-size:13px;color:var(--sub);line-height:1.6;margin:0}\n'
DM_ZH = (HERE / 'dish-menu-zh.html').read_text(encoding='utf-8')
DM_EN = (HERE / 'dish-menu-en.html').read_text(encoding='utf-8')

def _msh(zh):
    a, lab, c, ok, pd, w, sh, msg = (('ao-menu', '分享餐牌', '複製連結', '已複製連結', '下載 PDF', 'WhatsApp', '分享', 'Kitchen AO 2026 聖誕餐牌：') if zh else
                                 ('ao-menu-en', 'Share this menu', 'Copy link', 'Link copied', 'Download PDF', 'WhatsApp', 'Share', 'Kitchen AO Christmas Menu 2026: '))
    return (f'<div class="msh" data-a="{a}" data-ok="{ok}" data-m="{msg}"><span class="ml">{lab}</span>'
            f'<button type="button" class="mc"><svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M10 14a4.5 4.5 0 0 0 6.4 0l3.2-3.2a4.5 4.5 0 0 0-6.4-6.4L12 5.6"/><path d="M14 10a4.5 4.5 0 0 0-6.4 0l-3.2 3.2a4.5 4.5 0 0 0 6.4 6.4l1.2-1.2"/></g></svg><span>{c}</span></button>'
            f'<a class="mp" href="pdf/kitchen-ao-christmas-menu-2026-zh.pdf" target="_blank" rel="noopener" download><svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4v11M7 10l5 5 5-5"/><path d="M5 19h14"/></g></svg><span>{pd}</span></a>'
            f'</div>')
_EYE = '>KITCHEN AO · CHRISTMAS MENU</p>'
_CARD = '<div style="background:#FFFCF5'
DM_ZH = DM_ZH.replace(_CARD, _msh(True) + _CARD, 1); DM_EN = DM_EN.replace(_CARD, _msh(False) + _CARD, 1)
CSS += ('/* 分享餐牌 */.axl .msh{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:8px;margin:-12px 0 26px}'
 '.axl .msh .ml{font-size:12px;letter-spacing:.14em;color:#9A7B2E;margin-right:4px}'
 '.axl .msh button,.axl .msh a{display:inline-flex;align-items:center;gap:6px;font:600 12px/1 "Helvetica Neue","PingFang HK",Arial,sans-serif;letter-spacing:.04em;color:#1A1A1A;background:#fff;border:1px solid #C8A24A;padding:8px 12px;cursor:pointer;text-decoration:none;transition:background .2s,color .2s}'
 '.axl .msh button:hover,.axl .msh a:hover{background:#C8A24A;color:#111}.axl .msh .mc.ok{background:#1E4A3B;border-color:#1E4A3B;color:#fff}'
 '.axl .msh .mn{display:none}.axl .msh.can .mn{display:inline-flex}'
 '@media(max-width:640px){.axl .msh .ml{flex-basis:100%;text-align:center;margin:0 0 2px}}\n')
CSS += '/* 精選推介：桌面一次顯示 6 款；菜式詳細介紹按鈕 */@media(min-width:1025px){.axl section[id^="top"] .track{grid-auto-columns:calc((100% - 80px)/5)!important;gap:20px;scroll-snap-type:none!important;scroll-behavior:auto}}.axl section[id^="top"] .dbt{text-align:center;margin:28px 0 0}.axl section[id^="top"] .dbt .btn{margin:0}.axl section[id^="dishes"]{border-top:1px solid var(--ln)}\n'
CSS += '/* 手機 slider 箭嘴 */@media(max-width:1024px){.axl section[id^="top"] .nav{display:flex!important;align-items:center;justify-content:center;width:36px;height:36px;font-size:17px;top:calc(39vw - 18px);background:rgba(255,255,255,.92);border:1px solid #C8A24A;color:#9A7B2E;box-shadow:0 2px 8px rgba(0,0,0,.18);padding:0;line-height:1}.axl section[id^="top"] .nav.l{left:4px}.axl section[id^="top"] .nav.r{right:4px}}@media(min-width:641px) and (max-width:1024px){.axl section[id^="top"] .nav{top:calc(23vw - 18px)}}\n'
CSS += '/* Hero 文字唔可以被右邊圖片遮住：文字區最闊 = 剩餘位置 */@media(min-width:641px){.axl .hero .m0,.axl .hero .mt1,.axl .hero .mln,.axl .hero .mbt{max-width:calc(100% - min(56%,600px) - 36px);position:relative;z-index:2}.axl .hero .mt1 .t{white-space:normal;font-size:clamp(28px,3.6vw,52px)!important}.axl .hero .mt1 .z{font-size:clamp(19px,2.2vw,32px)!important}.axl .hero .m0{letter-spacing:.3em!important}.axl .hero .btn.p{padding:14px 26px;letter-spacing:.18em}}@media(min-width:641px) and (max-width:900px){.axl .hero .hbox{max-width:46%}.axl .hero .m0,.axl .hero .mt1,.axl .hero .mln,.axl .hero .mbt{max-width:calc(54% - 36px)}.axl .hero .m0{font-size:11px;letter-spacing:.2em!important;white-space:nowrap}}\n'
CSS += '/* 聖誕主菜：Option B 置中卡片 */.mo .gb{display:grid;grid-template-columns:1fr 1fr;gap:40px;max-width:980px;margin:0 auto}.mo .gb .c{text-align:center}.mo .gb .im{display:block;aspect-ratio:1/1;overflow:hidden;background:#111}.mo .gb img{width:100%;height:100%;object-fit:cover}.mo .gb .ln{width:1px;height:34px;background:#C8A24A;margin:0 auto 14px}.mo .gb .k{font:700 10.5px/1.4 "Helvetica Neue","PingFang HK",Arial,sans-serif;letter-spacing:.2em;color:#9A7B2E;margin:0 0 10px}.mo .gb .n{font-family:Baskerville,"Baskerville Old Face","Songti TC","Noto Serif TC",Georgia,serif;font-size:clamp(24px,2.4vw,30px);line-height:1.25;margin:0 0 6px}.mo .gb .s{font-family:Baskerville,"Baskerville Old Face","Songti TC","Noto Serif TC",Georgia,serif;font-style:italic;font-size:15px;color:var(--sub);margin:0 0 6px}.mo .gb .d{font-size:14px;color:var(--sub);margin:0 0 16px}.mo .gb .bt{display:inline-block;font:700 11.5px/1 "Helvetica Neue","PingFang HK",Arial,sans-serif;letter-spacing:.2em;text-transform:uppercase;color:#9A7B2E;border:1px solid #C8A24A;padding:12px 26px;text-decoration:none}.mo .gb .bt:hover{background:#C8A24A;color:#111}@media(max-width:640px){.mo .gb{grid-template-columns:1fr;gap:44px}}\n'
CSS += '/* 頁內導覽：捲動時置頂＋跟住段落亮起 */.axl .pills{position:-webkit-sticky;position:sticky;top:var(--ao-top,0px);z-index:50;background:rgba(255,255,255,.96);-webkit-backdrop-filter:blur(6px);backdrop-filter:blur(6px);border-bottom:0;margin:0;transition:box-shadow .3s;padding:10px 24px!important}.axl .pills a{transition:background .25s,color .25s,border-color .25s}.axl .pills+section.s,.axl .pills+*+section.s{border-top:0!important}.axl .stk.stuck{box-shadow:0 6px 14px -10px rgba(0,0,0,.35)}.axl .pills a.on{background:#111;border-color:#111;color:#E4C77E!important}.axl section[id]{scroll-margin-top:calc(var(--ao-top,0px) + 70px)}@media(max-width:640px){.axl .pills{display:grid!important;grid-template-columns:repeat(4,minmax(0,1fr));grid-auto-flow:row;gap:6px!important;overflow:visible;padding:8px 12px!important}.axl .pills::-webkit-scrollbar{display:none}.axl .pills a{font-size:12px!important;padding:6px 2px!important;text-align:center;white-space:normal!important;line-height:1.25;letter-spacing:.02em;display:flex;align-items:center;justify-content:center;min-width:0}html[lang^="en"] .axl .pills a{font-size:11px!important}}\n'
CSS += '/* 餐牌錨點及按鈕 */.axl .anc{display:block;height:0;scroll-margin-top:calc(var(--ao-top,0px) + 80px)}.axl section[id^="top"] .dbt{display:flex;flex-wrap:wrap;gap:12px;justify-content:center}.axl section[id^="top"] .dbt .btn{margin:0}.axl .btn.m{background:#fff;border:1px solid #C8A24A;color:#9A7B2E!important}.axl .btn.m:hover{background:#C8A24A;color:#111!important}\n'
CSS += '/* 英文版 Hero 副句字體 */.axl .ao-en-hero .z{}.ao-en .axl .hero .mt1 .z,.ao-en.axl .hero .mt1 .z{font-family:Baskerville,"Baskerville Old Face",Georgia,serif!important;font-style:italic;letter-spacing:.02em!important}\n'
CSS += '/* 時間軸提早 */.axl .hero .mt1 .z1{animation-delay:1.7s!important}.axl .hero .mt1 .z2{animation-delay:2s!important}.axl .hero .mln{animation-delay:2.8s!important}.axl .hero .mbt{animation-delay:3s!important}\n'
CSS += '/* Open the Box 逐字淡入（2026-11-21）*/.axl .hero .mt1 .t{animation:none!important;clip-path:none!important;filter:none!important;opacity:1!important}.axl .hero .mt1 .t .ow{display:inline-block;opacity:0;transform:translateY(.45em);filter:blur(6px);animation:axWord 1.1s cubic-bezier(.2,.7,.2,1) forwards;animation-delay:calc(.45s + var(--i) * .16s)}@keyframes axWord{60%{filter:blur(0)}to{opacity:1;transform:none;filter:blur(0)}}@media (prefers-reduced-motion:reduce){.axl .hero .mt1 .t .ow{animation:none;opacity:1;transform:none;filter:none}}\n'
CSS += '/* 開箱，就是聖誕 ⇄ 今年，交給 Kitchen AO 自動切換 */.axl .hero .mt1 .zs{position:relative;display:block;height:1.45em;overflow:hidden}.axl .hero .mt1 .zl{position:absolute;left:0;top:0;white-space:nowrap;transform:translateY(110%);opacity:0;transition:transform .9s cubic-bezier(.6,0,.2,1),opacity .9s}.axl .hero .mt1 .zl.on{transform:none;opacity:1}.axl .hero .mt1 .zl.out{transform:translateY(-110%);opacity:0}\n'
CSS += '.axl .bxl .tsd{margin:0 auto 26px!important;max-width:620px;font-style:italic;line-height:1.8}\n'
CSS += '/* 主菜及新菜相片 mouse over：跟分類方格一樣慢慢放大 */.axl .mo .gb .im,.axl .dc .pc-im{overflow:hidden}.axl .mo .gb .im img,.axl .dc .pc-im img{transition:transform 1.2s ease,opacity .6s ease}@media(hover:hover){.axl .mo .gb .c:hover .im img,.axl .dc:hover .pc-im img{transform:scale(1.05);opacity:.88}}\n'
import base64 as _b64
WM = 'data:image/png;base64,' + _b64.b64encode((HERE / 'img' / 'kitchen-ao-wordmark-gold.png').read_bytes()).decode()
CSS += '.axl .hero .mt1 img.wm{display:inline-block;height:.78em!important;width:auto!important;max-width:none!important;vertical-align:-.04em;margin:0 0 0 .45em!important;opacity:1!important;animation:none!important;object-fit:contain;position:static;transform:none}\n'
CSS += '.axl .bxl .tsh{margin:0 auto 10px!important}.axl .bxl .tsh h2{margin:0}.axl .bxl .tsh h2:after{display:none}.axl .bxl .mg span.tl{flex-direction:column;gap:6px;text-align:center;padding:0 12px}.axl .bxl .mg .tl b{font-weight:400}.axl .bxl .mg .tl em{font-style:italic;font-family:Baskerville,"Baskerville Old Face","Songti TC",Georgia,serif;font-size:.62em;letter-spacing:.08em;color:#F1E3BC}@media(max-width:640px){.axl .bxl .mg .tl em{font-size:.7em}}html:not([lang^="en"]) .axl .bxl .mg .tl em,html:not([lang^="en"]) .axl .bxl .tsd{font-style:normal}\n'
CSS += '/* 三大系列方格：3＋1，左下黑色 step flow */.axl .bxl section[id^="series"] .mg{grid-template-columns:repeat(3,1fr);max-width:1180px;grid-template-areas:"a b c" "p p d"}.axl .bxl section[id^="series"] .mg>a:nth-of-type(1){grid-area:a}.axl .bxl section[id^="series"] .mg>a:nth-of-type(2){grid-area:b}.axl .bxl section[id^="series"] .mg>a:nth-of-type(3){grid-area:c}.axl .bxl section[id^="series"] .mg>a.nd{grid-area:d}.axl .bxl .mg .hpg{grid-area:p;margin:0!important;display:flex;flex-direction:column;justify-content:center;padding:28px 20px}.axl .bxl .mg .hpg .hpt{margin-top:0}.axl .mg .hpg span{position:static;inset:auto;display:inline;font-size:inherit;letter-spacing:inherit;color:inherit;text-shadow:none;align-items:initial;justify-content:initial}.axl .mg .hpg .mt2 .pr{display:inline-block}.axl .mg .hpg .mt2 .pr .en,.axl .mg .hpg .mt2 .pr .zh{display:block}@media(max-width:640px){.axl .bxl section[id^="series"] .mg{grid-template-columns:1fr 1fr;grid-template-areas:"a b" "c d" "p p"}.axl .bxl .mg .hpg{padding:30px 14px}}\n'
CSS += '.axl .bxl .mg img.ig16{object-position:50% 0}\n'
CSS += '/* 套餐卡右上：人數標籤（黑框白底金字，貼角） */.axl .tag.px{position:absolute!important;inset:0 0 auto auto!important;margin:0!important;width:auto!important;display:flex!important;align-items:baseline;gap:5px;background:#fff!important;color:#9A7B2E!important;border:0;border-left:1px solid #111;border-bottom:1px solid #111;padding:9px 13px 8px!important;line-height:1;letter-spacing:0!important;box-shadow:inset 0 0 0 3px #fff,inset 0 0 0 4px rgba(200,162,74,.55)}.axl .tag.px b{font:italic 400 17px/1 Baskerville,"Baskerville Old Face",Georgia,serif!important;color:#9A7B2E;letter-spacing:.02em}.axl .tag.px i{font:700 9.5px/1 "Helvetica Neue","PingFang HK",Arial,sans-serif!important;font-style:normal;letter-spacing:.08em;color:#111}@media(max-width:640px){.axl .tag.px{padding:7px 9px 6px!important}.axl .tag.px b{font-size:14px!important}.axl .tag.px i{font-size:8.5px!important}}\n'

# ---- 三大系列：首頁式（左圖＋右文字＋人數 tab 換相換價＋立即配搭菜式）----
U26 = 'https://aoaodelivery.com/wp-content/uploads/2026/11/'
XS = [
 dict(s=SER[2], k='48-100 人 · 年尾大型派對首選', d='兩大主菜同場，以寶箱及專屬木箱送上',
      imgs=['2026-XMAS-IG-16.jpg']),
 dict(s=SER[1], k='5-40 人 · 全港限量 100 個', d='以專屬木箱原盒送上',
      imgs=['2026-XMAS-IG-10.jpg']),
 dict(s=SER[0], k='5-40 人 · 全港限量 100 個', d='以復古寶箱原箱送上',
      imgs=['2026-XMAS-IG-11-scaled.jpg']),
]
def xs_row(x, n):
    S = x['s']; a0, b0, p0 = S['rows'][0]
    tabs = ''.join(f'<button type="button" class="xt{" on" if j == 0 else ""}" data-u="{url(S, a, b)}" data-i="{U26}{x["imgs"][j % len(x["imgs"])]}" '
                   f'data-p="{pr:,.0f}" data-e="{round(pr * .79):,.0f}">{a}–{b} pax</button>' for j, (a, b, pr) in enumerate(S['rows']))
    return (f'<div class="xr{" xrv" if n % 2 else ""}" id="{S["id"]}"><div class="xim"><img class="{"trim" if "IG-11" in x["imgs"][0] else ""}" src="{U26}{x["imgs"][0]}" alt="{S["name"]}．{S["full"]}" loading="lazy"><span class="tag px"><b>{a0}–{b0}</b><i>pax</i></span></div>'
            f'<div class="xtx"><p class="xk">{x["k"]}</p><h3 class="xn">{S["name"]}</h3><p class="xf">{S["full"]}</p><p class="xd">{x["d"]}</p>'
            f'<p class="xds">{S["desc"]}</p>'
            f'<p class="xp">HK$<em class="pv">{p0:,.0f}</em></p><p class="xe"><span>MEGA79 後</span> HK$<b class="ev">{round(p0 * .79):,.0f}</b></p>'
            f'<div class="xtabs n{len(S["rows"])}">{tabs}</div>'
            f'<p class="xcta"><a class="xgo" href="{url(S, a0, b0)}">立即配搭菜式 →</a><a class="xall" href="{C}{S["slug"]}/">查看系列頁</a></p></div></div>')
XS_ROWS = '<div class="xsr">' + ''.join(xs_row(x, n) for n, x in enumerate(XS)) + '</div>'
CSS += ('/* 三大系列：黑色全闊、首頁式排版 */'
 '.axl section[id^="sets"]{background:#111;color:#EDE6D8;border-top:0!important}'
 '.axl .xsr .xr{display:grid;grid-template-columns:minmax(0,440px) minmax(0,1fr);gap:clamp(28px,5vw,64px);align-items:center;max-width:1040px;margin:0 auto;padding:clamp(34px,5vw,56px) 0;border-top:1px solid rgba(200,162,74,.35)}'
 '.axl .xsr .xr:first-child{border-top:0;padding-top:8px}.axl .xsr .xr.xrv{grid-template-columns:minmax(0,1fr) minmax(0,440px)}.axl .xsr .xr.xrv .xim{order:2}'
 '.axl .xsr .xim{position:relative;aspect-ratio:4/5;overflow:hidden;background:#000}'
 '.axl .xsr .xim img{width:100%!important;height:100%!important;object-fit:cover;transition:opacity .45s ease,transform 1.2s ease}.axl .xsr .xim img.fd{opacity:0}'
 '@media(hover:hover){.axl .xsr .xr:hover .xim img{transform:scale(1.04)}}'
 '.axl .xsr .tag.px{position:absolute!important}'
 '.axl .xsr .xtx{text-align:center}'
 '.axl .xsr .xk{font:700 11.5px/1.5 "Helvetica Neue","PingFang HK",Arial,sans-serif!important;letter-spacing:.2em;color:#C8A24A;margin:0 0 12px!important}'
 '.axl .xsr .xn{font-size:clamp(26px,3vw,36px)!important;color:#fff!important;margin:0 0 6px!important;font-weight:400;line-height:1.3}'
 '.axl .xsr .xf{font-size:clamp(15px,1.6vw,18px)!important;color:#EDE6D8;margin:0 0 6px!important}'
 '.axl .xsr .xd{font-size:14px!important;color:#9b948a;margin:0 0 14px!important}'
 '.axl .xsr .xds{font-size:14px!important;line-height:1.85;color:#cfc7b8;max-width:520px;margin:0 auto 18px!important}'
 '.axl .xsr .xp{font:400 13px/1 "Helvetica Neue",Arial,sans-serif!important;color:#C8A24A;margin:0 0 6px!important;letter-spacing:.06em}.axl .xsr .xp em{font-style:normal;font-size:28px;color:#fff;font-weight:600;margin-left:2px}'
 '.axl .xsr .xe{font-size:13px!important;color:#9b948a;margin:0 0 18px!important}.axl .xsr .xe b{font-weight:400}'
 '.axl .xsr .xtabs{display:flex;flex-wrap:wrap;justify-content:center;gap:8px;margin:0 0 22px}.axl .xsr .xtabs.n6{display:grid;grid-template-columns:repeat(3,auto);justify-content:center}.axl .xsr .xim img.trim{transform:scale(1.04);transform-origin:60% 50%}@media(hover:hover){.axl .xsr .xr:hover .xim img.trim{transform:scale(1.08)}}.axl .xsr .xim .tag.px{z-index:2}'
 '.axl .xsr .xt{font:600 13px/1 "Helvetica Neue","PingFang HK",Arial,sans-serif;letter-spacing:.04em;color:#EDE6D8;background:transparent;border:1px solid rgba(237,230,216,.55);padding:10px 14px;cursor:pointer;transition:all .25s}'
 '.axl .xsr .xt:hover{border-color:#C8A24A;color:#E4C77E}.axl .xsr .xt.on{background:#C8A24A;border-color:#C8A24A;color:#111}'
 '.axl .xsr .xcta{margin:0!important;display:flex;flex-direction:column;align-items:center;gap:12px}'
 '.axl .xsr .xgo{font-family:Baskerville,"Baskerville Old Face","Songti TC",Georgia,serif;font-size:19px;color:#E4C77E!important;text-decoration:none;border-bottom:1px solid #C8A24A;padding-bottom:4px;letter-spacing:.06em}'
 '.axl .xsr .xgo:hover{color:#fff!important;border-color:#fff}'
 '.axl .xsr .xall{font-size:12.5px;color:#9b948a!important;text-decoration:none;letter-spacing:.08em}.axl .xsr .xall:hover{color:#E4C77E!important}'
 '@media(max-width:760px){.axl .xsr .xr,.axl .xsr .xr.xrv{grid-template-columns:1fr;gap:22px}.axl .xsr .xr.xrv .xim{order:0}.axl .xsr .xim{max-width:420px;width:100%;margin:0 auto}.axl .xsr .xt{padding:9px 11px;font-size:12px}}\n')

# ---- 精選套餐介紹：三個系列 slider ----
_INCL = _BD['INCL']
_FT = [
 dict(id='beef', img=IMG['beef'], px='5–40', k='KITCHEN AO · 全港限量 100 個', n='聖誕寶藏箱．煙燻慢煮美國牛翼板肉盛宴', p=1928,
      d='下肩胛翼板肉在日式燒肉稱為「羽下肉」或「座布團」，每頭牛僅約 2 至 3 公斤。油花細密均勻，慢煮至五成熟後以煙燻木料高溫炙烤，外層焦香、內裏鎖住肉汁，以復古寶箱盛載，開箱一刻就是全場焦點。',
      inc=_INCL),
 dict(id='chk', img=IMG['chk2'], px='5–40', k='KITCHEN AO · 全港限量 100 個', n='聖誕金雞獻禮．燒南乳香慢煮原隻黃油雞', p=1688,
      d='本地優質黃油雞以南乳醬醃製，烹調前先以鹽水浸漬令肉質入味；低溫慢煮後以高溫炙燒逼出皮下脂肪，外皮金黃酥脆、內裏鮮嫩多汁，配聖誕玫瑰金巴利汁，以專屬木箱盛載。',
      inc=['燒南乳香慢煮原隻黃油雞'] + _INCL[1:]),
 dict(id='dbl', img='https://aoaodelivery.com/wp-content/uploads/2026/11/2026-XMAS-IG-16.jpg', px='48–100', k='KITCHEN AO · 48 至 100 人', n='聖誕開箱雙寶．燒南乳香慢煮原隻黃油雞 × 煙燻慢煮美國牛翼板肉', p=12418,
      d='兩大主菜同場：寶箱煙燻慢煮美國牛翼板肉配燒南乳香慢煮原隻黃油雞，以寶箱及專屬木箱一同送上，專為 48 至 100 人的公司年終派對及大型活動而設。',
      inc=['燒南乳香慢煮原隻黃油雞'] + _INCL),
]
def _ft(f, i):
    return (f'<div class="fs{" on" if i == 0 else ""}"><div class="pd"><div class="im"><img src="{f["img"]}" alt="{f["n"]}" loading="lazy"><span class="tag px"><b>{f["px"]}</b><i>pax</i></span></div>'
            f'<div><p class="vd" style="margin-top:0">{f["k"]}</p><h2>{f["n"]}</h2>'
            f'<p class="p2">HK${f["p"]:,} 起<span class="pe2">MEGA79 後 HK${round(f["p"] * .79):,} 起</span></p>'
            f'<p>{f["d"]}</p><p style="margin-bottom:0">套餐可搭配：</p><ul>' + ''.join(f'<li>{x}</li>' for x in f['inc']) + '</ul>'
            f'<a class="bt" href="#{f["id"]}">選擇人數</a></div></div></div>')
FEAT_SL = ('<section class="sec" id="feature"><div class="w"><div class="fsl">'
           '<button class="fn l" type="button" aria-label="上一個">‹</button><button class="fn r" type="button" aria-label="下一個">›</button>'
           + ''.join(_ft(f, i) for i, f in enumerate(_FT)) +
           '<div class="fdots">' + ''.join(f'<i class="{"on" if i == 0 else ""}" role="button" tabindex="0" aria-label="第 {i + 1} 款"></i>' for i in range(len(_FT))) + '</div>'
                      '</div></div></section>')
CSS += ('/* 套餐介紹 slider */.axl .fsl{position:relative;max-width:1080px;margin:0 auto}'
 '.axl .fsl .fs{display:none;animation:axFade .6s ease both}.axl .fsl .fs.on{display:block}'
 '.axl .fsl .fn{position:absolute;top:min(26vw,250px);z-index:3;width:42px;height:42px;border-radius:50%;border:1px solid #C8A24A;background:rgba(255,255,255,.95);color:#9A7B2E;font-size:19px;cursor:pointer;display:flex;align-items:center;justify-content:center;padding:0;line-height:1}'
 '.axl .fsl .fn.l{left:-20px}.axl .fsl .fn.r{right:-20px}'
 '.axl .fsl .fdots{display:flex;justify-content:center;gap:12px;margin:24px 0 0}.axl .fsl .fdots i{width:8px;height:8px;border-radius:50%;background:#d8cfbd;cursor:pointer}.axl .fsl .fdots i.on{background:#9A7B2E}'
 '.axl .fsl .fcom{max-width:1080px;margin:26px auto 0}'
 '.axl .fsl .pd .im img{height:auto}'
 '@media(max-width:760px){.axl .fsl .pd{grid-template-columns:1fr}.axl .fsl .fn{top:calc(50vw - 21px);width:36px;height:36px}.axl .fsl .fn.l{left:4px}.axl .fsl .fn.r{right:4px}}\n')
CSS += '/* 導覽＋供應日期列一齊置頂 */.axl .stk{position:-webkit-sticky;position:sticky;top:var(--ao-top,0px);z-index:50}.axl .stk .pills{position:static!important;top:auto}.axl .stk .xav2{padding:0!important;border-top:0!important}.axl .stk .xav2 summary{padding:7px 0!important;min-height:0}.axl .stk .xav2 summary .w{padding-top:0!important;padding-bottom:0!important}.axl .stk .xav2 summary .w{font-size:13px!important;gap:6px}.axl .stk .xav2 summary i{font-size:16px!important}.axl .stk .xav2 summary svg{width:13px;height:13px}.axl .stk .xav2 summary em{font-size:11px!important}.axl .stk .xav2 .bd{max-height:60vh;overflow:auto}.axl section[id],.axl .anc{scroll-margin-top:calc(var(--ao-top,0px) + 40px)!important}@media(max-width:640px){.axl .stk .xav2 summary .w{font-size:12px!important}.axl .stk .xav2 summary i{font-size:14.5px!important}.axl section[id],.axl .anc{scroll-margin-top:calc(var(--ao-top,0px) + 45px)!important}}\n'
CSS += '.axl #delivery .dlx,.axl section[id^="delivery"] .dlx{margin-top:26px;border-top:1px solid var(--ln)}.axl section[id^="delivery"] .dlx details{padding:12px 2px}.axl section[id^="delivery"] .dlx summary{font-size:15px}.axl section[id^="delivery"] .dlx .bd{font-size:14px;color:var(--sub);margin:8px 0 2px;line-height:1.8}\n'
CSS += '.axl .hero .spk{z-index:4!important}\n'
CSS += '/* 捲動出場效果 */.axl.rvj .rv{opacity:0;transform:translateY(26px);transition:opacity .9s ease,transform 1s cubic-bezier(.2,.7,.2,1)}.axl.rvj .rv.rvd{opacity:1;transform:none}.axl.rvj .sh h2:after,.axl.rvj .bxl .st:after{transform:scaleX(0);transition:transform 1s .45s cubic-bezier(.2,.7,.2,1)}.axl.rvj .rvd h2:after,.axl.rvj .rvd .st:after{transform:scaleX(1)}.axl.rvj .rvd .h2g{background-image:linear-gradient(100deg,#9C6C08 0%,#C8961A 35%,#F6E3A6 50%,#C8961A 65%,#9C6C08 100%)!important;background-size:260% 100%;animation:axGs 2.2s .3s ease-out both}@keyframes axGs{from{background-position:100% 0}to{background-position:0 0}}.axl.rvj .rvd .xk,.axl.rvj .rvd .mn-k,.axl.rvj .rvd .k{animation:axTk 1.2s ease-out both}@keyframes axTk{from{letter-spacing:.5em;opacity:0}to{opacity:1}}@media(prefers-reduced-motion:reduce){.axl.rvj .rv{opacity:1!important;transform:none!important;transition:none!important}.axl.rvj .rvd .h2g{animation:none!important}}\n'
CSS += '/* 送貨段落：限闊、相片高度 */.axl .split{max-width:1192px;margin:clamp(40px,6vw,76px) auto;align-items:stretch}.axl .split>img{min-height:0!important;height:100%!important;max-height:none;aspect-ratio:auto;object-position:50% 100%}@media(max-width:900px){.axl .split{margin:0 16px 40px}.axl .split>img{height:auto!important;aspect-ratio:4/3;max-height:none}}@media(max-width:640px){.axl .split>img{aspect-ratio:16/10}}\n'
CSS += '/* Responsive 優化 */.axl .crumb{padding-left:24px!important;padding-right:24px!important}@media(min-width:641px){.axl .hero .m0,.axl .hero .mt1,.axl .hero .mln,.axl .hero .mbt{max-width:min(640px,calc(56vw - 56px))!important}.axl .hero .mt1 .t{white-space:normal!important;font-size:clamp(28px,3.5vw,50px)!important}}@media(min-width:641px) and (max-width:1024px){.axl .hero .hbox{max-width:44%!important}.axl .hero .mt1 .z{font-size:clamp(18px,2.6vw,26px)!important;letter-spacing:.2em}}@media(max-width:640px){.axl .crumb{padding-left:16px!important;padding-right:16px!important}}\n'
CSS += '@media(max-width:640px){.axl .hero .mbt{text-align:center}.axl .hero .btn.p{margin:0 auto 10px!important;max-width:300px}}\n'
CSS += '@media(max-width:640px){.axl section[id^="top"] .dbt{flex-wrap:nowrap!important;gap:6px!important;padding:0 2px}.axl section[id^="top"] .dbt .btn{flex:1 1 0;min-width:0;padding:9px 4px!important;font-size:11px!important;letter-spacing:.02em!important;white-space:normal;line-height:1.3;text-align:center;display:flex!important;align-items:center;justify-content:center}}@media(max-width:360px){.axl section[id^="top"] .dbt .btn{font-size:10px!important}}\n'
CSS += '/* 排版：避免單字孤行 */.axl p,.axl li,.axl .bd,.axl summary,.axl .dcd{text-wrap:pretty}.axl h1,.axl h2,.axl h3,.axl .xn,.axl .xf,.axl .xd,.axl .xds,.axl .sh p,.axl .tsd,.axl .mn-n,.axl .gb .s,.axl .gb .d,.axl .hp p,.axl .wide p,.axl .end p,.axl .pc-n,.axl .tl b,.axl .tl em,.axl .xk{text-wrap:balance}\n'
CSS += '@media(min-width:761px){.axl .wide{min-height:420px}.axl .wide>img{left:50%!important;right:auto!important;width:min(980px,100%)!important;height:100%!important;top:0!important;bottom:auto!important;object-fit:cover!important;object-position:center 50%!important;transform:translateX(-50%);-webkit-mask-image:linear-gradient(90deg,transparent 0,#000 16%,#000 84%,transparent 100%);mask-image:linear-gradient(90deg,transparent 0,#000 16%,#000 84%,transparent 100%)}}\n'
CSS += '@media(max-width:760px){.axl .wide{display:block!important;min-height:0!important}.axl .wide>img{position:static!important;display:block;width:100%!important;height:auto!important;aspect-ratio:auto;object-fit:contain;opacity:1!important}.axl .wide>.in{max-width:none;padding:28px 20px 34px!important;background:#111}}\n'
CSS += '@media(min-width:641px){.axl .bxl section[id^="series"] .mg{align-items:stretch}.axl .bxl section[id^="series"] .mg>a.nd{aspect-ratio:auto!important;height:auto;min-height:100%}.axl .bxl .mg .hpg{padding:24px 20px!important}.axl .bxl .mg .hpg .hpt{font-size:clamp(22px,2.4vw,32px)!important}}\n'
CSS += '@media(min-width:641px) and (max-width:1240px){.axl .pills{gap:6px!important;flex-wrap:nowrap!important;justify-content:center}.axl .pills a{padding:8px 11px!important;font-size:12.5px!important;white-space:nowrap}}\n'
_HE = '</svg>\n<p style="text-align:center !important;font-size:clamp(9.5px,2.6vw,11px);letter-spacing:.3em;color:#9A7B2E;margin:0 0 26px">KITCHEN AO'
_WMI = f'</svg>\n<img class="mwm" src="{WM}" alt="Kitchen AO" width="290" height="50">'
DM_ZH = DM_ZH.replace(_HE, _WMI + _HE[6:], 1); DM_EN = DM_EN.replace(_HE, _WMI + _HE[6:], 1)
DM_ZH = DM_ZH.replace('>KITCHEN AO · CHRISTMAS MENU</p>', '>CHRISTMAS MENU</p>', 1); DM_EN = DM_EN.replace('>KITCHEN AO · CHRISTMAS MENU</p>', '>CHRISTMAS MENU</p>', 1)
CSS += '.axl img.mwm{display:block;width:150px!important;height:auto!important;margin:4px auto 12px!important;filter:none}@media(max-width:640px){.axl img.mwm{width:120px!important}}\n'
CSS += '/* 按人數揀：黑金色調 */.axl section[id^="pax"]{background:#fff!important}.axl table.px th{background:#111!important;color:#E4C77E!important;border-bottom:1px solid #C8A24A}.axl table.px td{border-bottom:1px solid #EFE6D2!important}.axl table.px tr.gap td{background:#FBF6EA!important;color:#6b5f52}.axl table.px td:nth-child(2){color:#1A1A1A;font-weight:600}.axl .finder input{border:1px solid #C8A24A!important;background:#fff}.axl .finder input:focus{outline:none;box-shadow:0 0 0 2px rgba(200,162,74,.35)}.axl .finder .btn.p,.axl .finder button{background:#111!important;border-color:#111!important;color:#E4C77E!important}.axl .finder .btn.p:hover,.axl .finder button:hover{background:#C8A24A!important;border-color:#C8A24A!important;color:#111!important}.axl .finder .res,.axl #axl-res,.axl [id^="axl-res"]{color:#9A7B2E!important}\n'
CSS += '.axl .bxl .mg .tl i.tf{display:block;font-style:normal;font-family:"Songti TC","Noto Serif TC",Georgia,serif;font-size:.6em;letter-spacing:.06em;color:#fff;opacity:.92;line-height:1.4;max-width:90%;margin:0 auto}html[lang^="en"] .axl .bxl .mg .tl i.tf{font-family:Baskerville,"Baskerville Old Face",Georgia,serif;font-style:italic;letter-spacing:.02em}.axl .bxl .mg .tl em{margin-top:2px}@media(max-width:640px){.axl .bxl .mg .tl i.tf{font-size:.62em;max-width:96%;line-height:1.35}}\n'
CSS += '/* 手機：收起主題選單列的空白位，導覽貼住金色 bar */@media(max-width:1024px){#header .main_menu_holder{height:0!important;min-height:0!important;padding-top:0!important;padding-bottom:0!important;border:0!important;overflow:visible!important}}\n'
# ---- 手機排版修正：方格文字留邊、縮細；Hero 兩個按鈕同闊上下排 ----
MFIX = ('@media(max-width:640px){.axl .bxl .mg span{padding:0 10px;font-size:15px;line-height:1.35;letter-spacing:.03em;text-align:center}'
        '.axl .hero .btn{display:block;width:100%;max-width:300px;box-sizing:border-box;text-align:center;margin:0 0 10px}'
        '.axl .hero h1{font-size:24px;line-height:1.35}.axl .hero p{line-height:1.6;margin-bottom:16px}}\n')
CSS += MFIX
page = f'''<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>聖誕到會 2026｜聖誕大餐外賣及派對套餐｜Kitchen AO</title>
<meta name="description" content="Kitchen AO 聖誕套餐 2026｜聖誕到會及聖誕外賣：5 至 100 人原隻黃油雞、寶箱煙燻牛翼板肉及八款聖誕新菜，公司聖誕派對及家庭聚會皆宜。">
<style>body{{margin:0}}{CSS}</style><script type="application/ld+json">{LD}</script></head><body>
<div class="axl">
<div class="hero"><div class="hbox"><img class="hbg h1i" src="{HERO_IMG}" alt="聖誕到會 2026：聖誕寶藏箱" width="1200" height="1500"><img class="hbg h2i" src="{HERO_OPEN}" alt="開箱：聖誕寶藏箱、原隻黃油雞及聖誕新菜" loading="lazy" width="1200" height="1500"><span class="hfl"></span><span class="hsm"><i style="--xd:50%;--yd:23%;--xm:50%;--ym:23%;--dl:.6s"></i><i style="--xd:46%;--yd:19.5%;--xm:46%;--ym:19.5%;--dl:2.2s"></i><i style="--xd:17%;--yd:59%;--xm:17%;--ym:59%;--dl:1.1s"></i><i style="--xd:21%;--yd:55%;--xm:21%;--ym:55%;--dl:2.9s"></i><i style="--xd:78%;--yd:57%;--xm:78%;--ym:57%;--dl:1.6s"></i><i style="--xd:74%;--yd:53%;--xm:74%;--ym:53%;--dl:3.5s"></i><i style="--xd:84%;--yd:13.5%;--xm:84%;--ym:13.5%;--dl:2.0s"></i><i style="--xd:80%;--yd:10%;--xm:80%;--ym:10%;--dl:4.1s"></i></span><button class="hkey" type="button" aria-label="Open the box"><svg viewBox="0 0 64 24" width="44" height="17" aria-hidden="true"><g fill="none" stroke="#E4C77E" stroke-width="2.2" stroke-linecap="round"><circle cx="11" cy="12" r="7.5"/><circle cx="11" cy="12" r="2.6"/><path d="M18.5 12H58M48 12v6M54 12v5"/></g></svg><span class="hint"><em>Open it</em><b class="arw" aria-hidden="true"></b></span></button></div><div class="in"><div class="w" style="padding:0">
<span class="spk s1">✦</span><span class="spk s2">✦</span><span class="spk s3">✦</span><span class="spk s4">✦</span><span class="spk s5">✦</span><small class="m0">Christmas Catering 2026</small><p class="mt1"><span class="t"><span class="ow" style="--i:0">Open</span> <span class="ow" style="--i:1">the</span> <span class="ow" style="--i:2">Box!</span> <span class="ow" style="--i:3">It&#8217;s</span> <span class="ow" style="--i:4">Christmas!</span></span><span class="z"><span class="zs"><span class="zl on"><span class="z1">開箱，</span><span class="z2">就是聖誕</span></span><span class="zl">今年，交給<img class="wm" src="{WM}" alt="Kitchen AO" width="290" height="50"></span></span></span></p><span class="mln"></span><div class="mbt"><a class="btn p" href="#sets">選購聖誕套餐</a></div></div></div></div>

<div class="intro"><h1 class="ser hh"><span class="h2g">聖誕到會 2026</span><br><span class="h2b">聖誕大餐外賣及派對套餐</span></h1>
<p>Kitchen AO 聖誕到會套餐專為 5 至 100 人的聖誕聚會而設，由家庭聖誕大餐、好友派對到公司聖誕派對，都可以按人數揀選。今年三大系列分別以寶箱煙燻慢煮美國牛翼板肉、燒南乳香慢煮原隻黃油雞為主角，配前菜、沙律、意粉及飯和甜品，一份聖誕到會餐單就能照顧全場賓客。不論是在家慶祝的聖誕節到會，還是公司 Xmas 到會，網上揀好套餐即可預訂，聖誕外賣直送府上或辦公室。</p>
</div>
<div class="stk"><nav class="pills" aria-label="頁內導覽"><a href="#top">聖誕新菜</a><a href="#mains">聖誕主菜</a><a href="#series">套餐系列</a><a href="#pax">按人數揀</a><a href="#corp">公司派對</a><a href="#delivery">送貨安排</a><a href="#faq">常見問題</a><a href="#ao-menu">聖誕餐牌</a></nav></div><details class="xav2"><summary><div class="w"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><g stroke="#C8A24A" stroke-width="1.5" fill="none" stroke-linecap="round"><path d="M12 2v20M3.3 7l17.4 10M3.3 17L20.7 7M12 5l-2-2M12 5l2-2M12 19l-2 2M12 19l2 2"/></g></svg><span>聖誕套餐只限</span><i>12.12 – 12.27</i><span>供應</span><em>詳情</em></div></summary><div class="bd"><div class="w"><ul><li>12 月 19 日前，其他套餐及單點照常供應。</li><li>除企業訂單外，其他日子不供應<a href="https://aoaodelivery.com/product-category/christmas-party-catering-set/" target="_blank" rel="noopener">聖誕套餐</a></li><li>套餐供應情況會持續於網站更新，請密切留意網站內容及參閱<a href="https://aoaodelivery.com/delivery/" target="_blank" rel="noopener">送貨需知</a></li></ul></div></div></details>
<section class="s" id="top"><div class="w"><div class="sh"><h2><span class="h2g">聖誕到會精選推介</span><br><span class="h2b">2026 聖誕新菜式</span></h2><p class="sm">今年聖誕套餐全新加入的前菜、沙律、意粉及飯和甜品。</p></div>
<div class="rail"><button class="nav l" type="button" aria-label="上一個">‹</button><div class="track">{"".join(f'<div class="pc dc"><div class="pc-im"><img src="{IMG[k]}" alt="{n}" loading="lazy"></div><p class="pc-k">XMAS SPECIAL</p><p class="pc-n">{n}</p></div>' for k, n, d in DISH)}</div><button class="nav r" type="button" aria-label="下一個">›</button></div><p class="dbt"><a class="btn d" href="#ao-dish-details">菜式詳細介紹</a><a class="btn m" href="#ao-menu">查看完整聖誕餐牌</a><a class="btn m pdfb" href="pdf/kitchen-ao-christmas-menu-2026-zh.pdf" target="_blank" rel="noopener" download>下載餐牌 PDF</a></p></div></section>
<section class="s mo" id="mains"><div class="w"><div class="sh"><h2><span class="h2g lt">Featuring our bespoke meats to WOW</span><br><span class="h2b">2026 聖誕主菜</span></h2></div><div class="gb"><div class="c"><a class="im" href="#chk"><img loading="lazy" src="{IMG['chk2']}" alt="聖誕金雞獻禮"></a><div class="ln" style="margin-top:0"></div><p class="k">KITCHEN AO · 全港限量 100 個</p><p class="n">聖誕金雞獻禮</p><p class="s">燒南乳香慢煮原隻黃油雞</p><p class="d">原隻連木箱送到</p><a class="bt" href="#chk">查看套餐</a></div><div class="c"><a class="im" href="#beef"><img loading="lazy" src="{IMG['beef']}" alt="聖誕寶藏箱"></a><div class="ln" style="margin-top:0"></div><p class="k">KITCHEN AO · 全港限量 100 個</p><p class="n">聖誕寶藏箱</p><p class="s">煙燻慢煮美國牛翼板肉盛宴</p><p class="d">連復古寶箱送到</p><a class="bt" href="#beef">查看套餐</a></div></div></div></section>
<div class="bxl">{B_TILES}</div>
<section class="s" id="sets"><div class="w">
{XS_ROWS}</div></section>
<div class="bxl">{FEAT_SL}</div>
<section class="s" id="pax" style="background:var(--iv)"><div class="w"><div class="sh"><small>FIND YOUR SET</small><h2>按人數揀聖誕套餐</h2><p>輸入出席人數，即時建議合適的聖誕到會套餐。</p></div>
<div class="finder"><input id="axl-n" type="number" min="1" max="999" inputmode="numeric" placeholder="例如 20"><button class="btn p" type="button" id="axl-go" style="margin:0">建議套餐</button><div class="res" id="axl-res"></div></div>
<table class="px"><thead><tr><th>出席人數</th><th>建議套餐</th><th>另一選擇</th></tr></thead><tbody>
{"".join(f'<tr{" class=gap" if c else ""}><td>{a}</td><td>{b}</td><td>{c}</td></tr>' for a, b, c in PAX)}</tbody></table></div></section>
<section class="wide" id="corp"><img src="{IMG['rice']}" alt="公司聖誕派對到會" loading="lazy"><div class="in"><small style="letter-spacing:.38em;font-size:11.5px;color:#E9D29A">CORPORATE</small>
<h2>公司聖誕派對到會</h2><p>部門聚餐、年終派對及客戶活動，按人數配搭聖誕套餐，可索取正式報價及收據。</p>
<a class="btn o" href="https://aoaodelivery.com/catering-quote-enquiry/">到會報價查詢</a></div></section>
<section class="s" id="occ"><div class="w"><div class="sh"><small>FOR EVERY OCCASION</small><h2>聖誕到會推介：按場合揀套餐</h2></div>
<div class="occ">{"".join(f'<div class="oc"><h3>{t}</h3><p>{d}</p><a href="{u}">{l} →</a></div>' for t, d, u, l in OCC)}</div></div></section>

<section class="s" id="addon" style="padding-top:0;border-top:0"><div class="w"><div class="sh"><small>ADD-ONS</small><h2>聖誕小食及甜品加配</h2><p>人數較多或想令聖誕美食到會更豐富，可加配單點小食及甜品，一併安排聖誕小食到會。</p></div>
<div class="occ"><div class="oc"><h3>惹味小食</h3><p>雞翼、迷你漢堡、九層塔香酥雞等派對熱門小食。</p><a href="https://aoaodelivery.com/product-category/a-la-carte/snacks/">選購小食 →</a></div>
<div class="oc"><h3>甜品</h3><p>馬卡龍、芝士撻等一口甜品，為聖誕派對作結。</p><a href="https://aoaodelivery.com/product-category/a-la-carte/dessert/">選購甜品 →</a></div>
<div class="oc"><h3>派對用品</h3><p>餐具、暖貼及三層食物架，方便擺放及保溫。</p><a href="https://aoaodelivery.com/product-category/party-supplies/">選購用品 →</a></div>
<div class="oc"><h3>聖誕神秘加配</h3><p>聖誕樹芝士火腿拼盤，派對焦點冷盤，上桌即成拍照焦點。</p><a href="{WA}" target="_blank" rel="noopener">WhatsApp 查詢 →</a></div></div></div></section>
<section class="split" id="delivery"><img src="https://aoaodelivery.com/wp-content/uploads/2026/11/photo-1764009699066-473e36008bab.jpeg" alt="平安夜及聖誕節到會送貨安排" loading="lazy"><div class="tx"><small style="letter-spacing:.38em;font-size:11.5px;color:#9A7B2E">DELIVERY</small>
<h2>平安夜及聖誕節送貨安排</h2><ul><li>聖誕套餐供應及送貨日期為 12 月 12 日至 27 日；12 月 19 日前，其他套餐及單點照常供應。</li><li>平安夜（12 月 24 日）及聖誕節（12 月 25 日）熱門時段較快額滿，宜盡早確定日期及時間。</li><li>聖誕大餐外送覆蓋全港，標準運費已包括送達指定地址樓下或車輛可停泊的位置。</li><li>預留至少 30 分鐘緩衝時間，避免開餐與送貨時間太接近。</li><li>落單時寫清楚收貨人、電話及大廈資料；Party Room、辦公室及學校請先確認收貨安排。</li></ul>
<a class="btn d" href="https://aoaodelivery.com/delivery/">查看送貨需知</a><div class="dlx"><details><summary>套餐配搭說明</summary><div class="bd">套餐菜式可按喜好自由配搭；部分精選菜式需另加差價，實際價錢以落單頁面選項為準。</div></details><details><summary>溫馨提示</summary><div class="bd">煲仔鍋飯一般以原煲盛載；如瓦煲缺貨，會以錫紙盤代替，恕不另行通知。</div></details><details><summary>送貨安排</summary><div class="bd">Kitchen AO 提供全港到會送貨服務，標準運費已包括將食物送達指定地址樓下或車輛可停泊的位置。預留至少 30 分鐘緩衝時間；Party Room、辦公室及學校請先確認收貨安排。詳情見<a href="https://aoaodelivery.com/delivery/">送貨需知</a>。</div></details></div></div></section>
<section class="s" id="faq"><div class="w"><div class="sh"><small>FAQ</small><h2>聖誕到會常見問題</h2></div><div class="faq">
{"".join(f'<details{" open" if i == 0 else ""}><summary>{q}</summary><p>{a}</p></details>' for i, (q, a) in enumerate(FAQ))}</div></div></section>
<section class="s" id="dishes"><div class="w" style="max-width:820px">@@DISHES@@</div></section>
<div class="end"><p class="ser" style="font-size:22px;margin:0 0 6px">今年聖誕，交給 Kitchen AO</p><p style="color:var(--sub);margin:0 0 18px">5 至 100 人聖誕到會套餐，11 月 30 日前 MEGA79 七九折。</p>
<a class="btn p" href="#sets">選購聖誕套餐</a><a class="btn d" href="{WA}" target="_blank" rel="noopener">WhatsApp 查詢</a></div>
</div>
<script>(function(){{var ax=document.querySelectorAll('.axl');if(!('IntersectionObserver' in window))return;var Q=['.sh','.mo .gb .c','.xsr .xr','section[id^="series"] .mg>*','.fsl','.occ>.oc','.split .tx','.split>img','.wide>.in','.faq details','.end','.msh','.hp.hpg'];ax.forEach(function(a){{if(a.closest('.ao-zh,.ao-en')===null&&a.parentNode&&a.parentNode.classList&&a.parentNode.classList.contains('ao-x'))return;a.classList.add('rvj');var io=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{e.target.classList.add('rvd');io.unobserve(e.target)}}}})}},{{threshold:.12,rootMargin:'0px 0px -6% 0px'}});Q.forEach(function(q){{a.querySelectorAll(q).forEach(function(el){{if(el.closest('.hero'))return;el.classList.add('rv');var i=[].indexOf.call(el.parentNode.children,el);el.style.transitionDelay=Math.min(i,6)*.08+'s';io.observe(el)}})}})}})}})();
</script>
<script>(function(){{var end=new Date('2026-11-30T23:59:59+08:00').getTime(),cd=document.getElementById('axl-cd');function t(){{var s=Math.max(0,Math.floor((end-Date.now())/1000));if(!cd)return;cd.textContent=s?'｜尚餘 '+Math.floor(s/86400)+' 天 '+Math.floor(s%86400/3600)+' 小時':'';}}t();setInterval(t,60000);
document.querySelectorAll('.axl .rail').forEach(function(r){{var tr=r.querySelector('.track');r.querySelectorAll('.nav').forEach(function(b){{b.addEventListener('click',function(){{var c=tr.firstElementChild,st=innerWidth<1025&&c?c.offsetWidth+16:tr.clientWidth*.8;tr.scrollBy({{left:(b.classList.contains('l')?-1:1)*st,behavior:'smooth'}})}})}})}});
var S=[[5,6,'5-6 人套餐（寶藏箱 HK$1,928／金雞獻禮 HK$1,688）'],[8,10,'8-10 人套餐（寶藏箱 HK$3,028／金雞獻禮 HK$2,788）'],[12,16,'12-16 人套餐（寶藏箱 HK$4,588／金雞獻禮 HK$4,248）'],[18,22,'18-22 人套餐（寶藏箱 HK$5,888／金雞獻禮 HK$5,388）'],[26,30,'26-30 人套餐（寶藏箱 HK$7,888／金雞獻禮 HK$7,388）'],[35,40,'35-40 人套餐（寶藏箱 HK$9,888／金雞獻禮 HK$9,288）'],[48,54,'48-54 人開箱雙寶（HK$12,418）'],[63,68,'63-68 人開箱雙寶（HK$15,368）'],[78,85,'78-85 人開箱雙寶（HK$19,548）'],[90,100,'90-100 人開箱雙寶（HK$22,888）']];
function go(){{var n=parseInt(document.getElementById('axl-n').value,10),r=document.getElementById('axl-res');if(!n||n<1){{r.textContent='請輸入人數';return;}}if(n>100){{r.textContent='100 人以上請經到會報價查詢聯絡我們';return;}}
for(var i=0;i<S.length;i++){{if(n<=S[i][1]){{r.textContent=(n>=S[i][0]?'建議：':'建議：')+S[i][2]+(n<S[i][0]&&i>0?'，或 '+S[i-1][0]+'-'+S[i-1][1]+' 人套餐加配單點':'');return;}}}}}}
var L=document.getElementById('bxl-look');if(L){{var sl=L.querySelectorAll('.ls'),pp=L.querySelectorAll('.pips i'),cur=0;
function show(i){{cur=(i+sl.length)%sl.length;sl.forEach(function(s,k){{s.hidden=k!==cur}});pp.forEach(function(p,k){{p.className=k===cur?'on':''}});}}
pp.forEach(function(p,k){{p.addEventListener('click',function(){{show(k)}})}});L.querySelectorAll('.arw').forEach(function(b){{b.addEventListener('click',function(){{show(cur+ +b.dataset.d)}})}});
sl.forEach(function(s){{s.querySelectorAll('.dot').forEach(function(d){{d.addEventListener('click',function(){{s.querySelectorAll('.dot').forEach(function(x){{x.classList.toggle('on',x===d)}});s.querySelectorAll('.lc').forEach(function(c){{c.hidden=c.dataset.p!==d.dataset.p}})}})}})}});}}
document.querySelectorAll('.axl .hero .hkey').forEach(function(k){{k.addEventListener('click',function(){{var h=k.closest('.hero'),b=h.querySelector('.hbox');b.classList.add('shake');setTimeout(function(){{b.classList.remove('shake');h.classList.add('open')}},420);if(window.dataLayer)dataLayer.push({{event:'xmas_lp_open_box'}})}})}});
document.querySelectorAll('.axl section[id^="top"] .track').forEach(function(t){{function c(){{if(innerWidth<1025)return;var f=t.firstElementChild;if(f&&!t.dataset.o){{t.scrollLeft=(f.offsetWidth+20)/2;t.dataset.o=1}}}}c()}});
(function(){{var nav=document.querySelector('.axl .pills');if(!nav)return;var ls=[].slice.call(nav.querySelectorAll('a')),cur=null;function top(){{var h=0;['#header','#lafka-header-sticky','.lafka-sticky-header','header.sticky','.site-header.is-sticky','#wpadminbar'].forEach(function(q){{var e=document.querySelector(q);if(e){{var cs=getComputedStyle(e);if(cs.position==='fixed'||cs.position==='sticky'){{h=Math.max(h,e.getBoundingClientRect().bottom);[].forEach.call(e.querySelectorAll('#logo,#logo img,.logo,.custom-logo'),function(l){{var r=l.getBoundingClientRect();if(r.height&&r.bottom<innerHeight/2)h=Math.max(h,r.bottom)}})}}}}}});document.querySelector('.axl').style.setProperty('--ao-top',Math.max(0,h)+'px')}}function spy(){{var r=(nav.closest('.stk')||nav).getBoundingClientRect();(nav.closest('.stk')||nav).classList.toggle('stuck',r.top<=parseFloat(getComputedStyle(document.querySelector('.axl')).getPropertyValue('--ao-top')||0)+1&&scrollY>0);var y=r.bottom+Math.min(160,innerHeight*.3),id=null;ls.forEach(function(a){{var t=document.getElementById(a.getAttribute('href').slice(1));if(t&&t.getBoundingClientRect().top<=y)id=a}});if(id!==cur){{if(cur)cur.classList.remove('on');cur=id;if(cur){{cur.classList.add('on');if(nav.scrollWidth>nav.clientWidth)nav.scrollTo({{left:cur.offsetLeft-nav.clientWidth/2+cur.offsetWidth/2,behavior:'smooth'}})}}}}}}ls.forEach(function(a){{a.addEventListener('click',function(){{if(cur)cur.classList.remove('on');cur=a;a.classList.add('on');lock=Date.now()}})}});var lock=0,_spy=spy;spy=function(){{if(Date.now()-lock>900)_spy()}};top();spy();addEventListener('scroll',function(){{top();spy()}},{{passive:true}});addEventListener('resize',function(){{top();spy()}});addEventListener('load',top)}})();
document.querySelectorAll('.axl .hero .zs').forEach(function(z){{var ls=z.querySelectorAll('.zl'),i=0;if(ls.length<2)return;setTimeout(function(){{setInterval(function(){{var a=ls[i];i=(i+1)%ls.length;var b=ls[i];a.classList.remove('on');a.classList.add('out');b.classList.remove('out');void b.offsetWidth;b.classList.add('on');setTimeout(function(){{a.classList.remove('out')}},950)}},4000)}},3800)}});
document.querySelectorAll('.axl .xsr .xr').forEach(function(r){{var im=r.querySelector('.xim img'),tg=r.querySelector('.xim .tag b'),pv=r.querySelector('.pv'),ev=r.querySelector('.ev'),go=r.querySelector('.xgo');r.querySelectorAll('.xt').forEach(function(b){{b.addEventListener('click',function(){{r.querySelectorAll('.xt').forEach(function(x){{x.classList.toggle('on',x===b)}});pv.textContent=b.dataset.p;ev.textContent=b.dataset.e;go.href=b.dataset.u;tg.textContent=b.textContent.replace(' pax','');if(im.getAttribute('src')!==b.dataset.i){{im.classList.add('fd');var n=new Image();n.onload=function(){{im.src=b.dataset.i;im.classList.remove('fd')}};n.src=b.dataset.i;setTimeout(function(){{im.classList.remove('fd')}},1500)}}}})}})}});
document.querySelectorAll('.axl .fsl').forEach(function(w){{var ss=w.querySelectorAll('.fs'),ds=w.querySelectorAll('.fdots i'),c=0;function go(i){{c=(i+ss.length)%ss.length;ss.forEach(function(x,k){{x.classList.toggle('on',k===c)}});ds.forEach(function(x,k){{x.classList.toggle('on',k===c)}})}}w.querySelector('.fn.l').addEventListener('click',function(){{go(c-1)}});w.querySelector('.fn.r').addEventListener('click',function(){{go(c+1)}});ds.forEach(function(d,k){{d.addEventListener('click',function(){{go(k)}})}});var x0=null;w.addEventListener('touchstart',function(e){{x0=e.touches[0].clientX}},{{passive:true}});w.addEventListener('touchend',function(e){{if(x0===null)return;var dx=e.changedTouches[0].clientX-x0;if(Math.abs(dx)>50)go(c+(dx<0?1:-1));x0=null}})}});
document.querySelectorAll('.axl .msh').forEach(function(m){{var u=location.href.split('#')[0]+'#'+m.dataset.a,c=m.querySelector('.mc'),t=c.querySelector('span'),t0=t.textContent;function dl(e){{if(window.dataLayer)dataLayer.push({{event:'xmas_menu_share',method:e}})}}c.addEventListener('click',function(){{function ok(){{c.classList.add('ok');t.textContent=m.dataset.ok;setTimeout(function(){{c.classList.remove('ok');t.textContent=t0}},2000)}}if(navigator.clipboard&&navigator.clipboard.writeText)navigator.clipboard.writeText(u).then(ok,fb);else fb();function fb(){{var x=document.createElement('textarea');x.value=u;x.style.position='fixed';x.style.opacity='0';document.body.appendChild(x);x.select();try{{document.execCommand('copy');ok()}}catch(e){{prompt('',u)}}document.body.removeChild(x)}}dl('copy')}});}});
var HP=document.querySelectorAll('.axl .hp');if('IntersectionObserver' in window){{var io=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target)}}}})}},{{threshold:0,rootMargin:'0px 0px -35% 0px'}});HP.forEach(function(h){{io.observe(h)}})}}else HP.forEach(function(h){{h.classList.add('in')}});
document.getElementById('axl-go').addEventListener('click',go);document.getElementById('axl-n').addEventListener('keydown',function(e){{if(e.key==='Enter')go();}});}})();</script>
</body></html>'''
for _a, _b in _EB.items(): page = page.replace(f'<small>{_a}</small>', f'<small>{_b}</small>')
def _imgfix(m):
    t = m.group(0)
    if 'decoding=' not in t: t = t.replace('<img ', '<img decoding="async" ', 1)
    if 'class="hbg h1i"' in t: return t.replace('<img ', '<img fetchpriority="high" ', 1)
    if 'loading=' not in t: t = t.replace('<img ', '<img loading="lazy" ', 1)
    return t
page = re.sub(r'<img [^>]*>', _imgfix, page)
page = page.replace('href="#new"', 'href="#top"')
(HERE / 'a-christmas.html').write_text(page.replace(' →', '').replace('→', '').replace('@@DISHES@@', DM_ZH), encoding='utf-8')
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
for _k, _v in EN.HERO_ZH.items(): _en_html = _en_html.replace(_k, _v)
_en_html = _en_html.replace('@@DISHES@@', DM_EN)
# 2026-11-21：英文版 Hero 副句唔再顯示中文
_en_html = _en_html.replace('<span class="z1">開箱，</span><span class="z2">就是聖誕</span>', '<span class="z1">Hours to slow-cook,&nbsp;</span><span class="z2">one second to WOW</span>')
_en_html = _en_html.replace('<span class="zl">今年，交給<img', '<span class="zl">This year, leave it to&nbsp;<img')
_en_html = _en_html.replace('kitchen-ao-christmas-menu-2026-zh.pdf', 'kitchen-ao-christmas-menu-2026-en.pdf')
_en_html = _en_html.replace('</a>。', '</a>.').replace(' →', '').replace('→', '')
_html = _html.replace(' →', '').replace('→', '').replace('</a>，', '</a>, ')
_html = _html.replace('@@DISHES@@', DM_ZH)
_ld_en = _json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": EN.D[q], "acceptedAnswer": {"@type": "Answer", "text": EN.D[a]}} for q, a in FAQ]}, ensure_ascii=False)
_ld_js = ('<script>(function(){var en=/^en/i.test(document.documentElement.lang||""),s=document.createElement("script");s.type="application/ld+json";'
          f's.text=en?{_json.dumps(_ld_en, ensure_ascii=False)}:{_json.dumps(LD, ensure_ascii=False)};document.head.appendChild(s);}})();</script>')
BIL = ('<style>html[lang^="en"] .ao-zh{display:none!important}html:not([lang^="en"]) .ao-en{display:none!important}'
       # 呢頁：收起主題主選單；body 唔可以做捲動容器，否則置頂導覽失效
       'body{overflow:visible!important;overflow-x:clip!important}'
       # 全闊：不論 theme 容器多闊，都撐滿整個視窗
       'html,body{overflow-x:clip}.ao-zh>.axl,.ao-en>.axl{width:100vw;max-width:100vw;margin-left:calc(50% - 50vw);margin-right:calc(50% - 50vw)}</style>')
_bil_body = (f'<div class="ao-zh" data-no-translation>\n{_html.strip()}\n</div>\n<div class="ao-en" data-no-translation>\n{_en_html.strip()}\n</div>\n'
             # 只保留當前語言：另一語言整段從頁面移除（Google 渲染後只有一組 H1–H4）
             + '<script>(function(){var en=/^en/i.test(document.documentElement.lang||"");var r=document.querySelector(en?".ao-zh":".ao-en");if(r)r.parentNode.removeChild(r);})();</script>\n'
             + _zh_js.replace('<script>(function(){', '<script>(function(){if(!document.querySelector(".ao-zh .axl"))return;', 1)
             + '\n' + _en_js.replace('<script>(function(){', '<script>(function(){if(!document.querySelector(".ao-en .axl"))return;', 1) + '\n' + _ld_js)
# 英文預覽版（獨立檔，lang=en）
_en_page = ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>Christmas Catering Hong Kong 2026 | Christmas Dinner Delivery &amp; Party Sets | Kitchen AO</title><meta name="description" content="Christmas catering in Hong Kong for 5 to 100 guests: whole yellow chicken, smoked beef chuck flap in a treasure box and eight new dishes. Xmas catering for home and Xmas party catering for the office.">'
            f'<style>body{{margin:0}}</style>{_st}{BIL}</head><body>{_bil_body}</body></html>')
(HERE / 'a-christmas-en.html').write_text(_en_page, encoding='utf-8')
wp = ('<!-- Kitchen AO 聖誕到會場景頁 /catering/christmas/ ：整段貼入 WPBakery Raw HTML。中文頁顯示中文，/en/ 頁自動顯示英文。'
      'Title／Meta／Focus KW 請在 Rank Math 及 TranslatePress 設定。 -->\n' + _st + '\n' + BIL + '\n' + _bil_body + '\n')
(HERE / 'wp').mkdir(exist_ok=True)
wp = wp.replace(HERO_IMG, HERO_URL).replace(HERO_OPEN, HERO_OPEN_URL)
wp = wp.replace('href="pdf/kitchen-ao-christmas-menu-2026', 'href="https://aoaodelivery.com/wp-content/uploads/2026/11/kitchen-ao-christmas-menu-2026')
import sys as _sys; _sys.path.insert(0, str(HERE.parent / 'tools'))
import img_opt as _io
def _sz(fn, tag):
    if fn.startswith('20_26xmas'): return '(max-width:640px) 75vw, 300px'
    if fn.startswith('photo-'): return '(max-width:768px) 100vw, 600px'
    if fn.startswith('2026-XMAS-IG'): return '(max-width:640px) 100vw, 480px'
    return '(max-width:640px) 100vw, 600px'
wp, _n = _io.opt(wp, _sz); print('img_opt', _n)
# 2026-11-21：大圖（主菜、相簿、產品卡、橫幅）唔再用 300px sizes，避免高解像度螢幕模糊
import re as _re
def _sharp(m):
    tag = m.group(0); ctx = wp[max(0, m.start() - 220):m.start()]
    if '20_26xmas' not in tag or 'class="pc-im"' in ctx[-80:]: return tag
    if 'class="wide"' in ctx[-120:] or 'class="wide"' in tag:
        fn = _re.search(r'20_26xmas-[a-z0-9-]+?(?=-\d+x\d+)', tag).group(0)
        tag = tag.replace('1024w"', '1024w, https://aoaodelivery.com/wp-content/uploads/2026/11/%s.jpg 1667w"' % fn, 1)
        return _re.sub(r'sizes="[^"]*"', 'sizes="(max-width:980px) 100vw, 980px"', tag, 1)
    return _re.sub(r'sizes="[^"]*"', 'sizes="(max-width:640px) 92vw, 520px"', tag, 1)
wp = _re.sub(r'<img\b[^>]*>', _sharp, wp)
(HERE / 'wp' / 'a-christmas-wp.html').write_text(wp, encoding='utf-8')
print('wp ok', len(wp))
