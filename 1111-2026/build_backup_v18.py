# -*- coding: utf-8 -*-
"""Kitchen AO 雙 11 年尾飯局預購 2026：Landing page（/1111/）＋ EDM
優惠數字未定，所有優惠位以〔待定〕顯示。文案全部書面語。
輸出：
  landing.html          預覽（完整頁面）
  landing-rawhtml.html  貼入 WPBakery Raw HTML
  email.html            FluentCRM Raw HTML
"""
import os, re
H = os.path.dirname(os.path.abspath(__file__))
B = 'https://aoaodelivery.com'
U = B + '/wp-content/uploads/'
LP = B + '/1111/'
WA = 'https://wa.me/85269011987?text=%E4%BD%A0%E5%A5%BD%EF%BC%8C%E6%88%91%E6%83%B3%E6%9F%A5%E8%A9%A2%E9%9B%99%2011%20%E5%84%AA%E6%83%A0'  # 你好，我想查詢雙 11 優惠
TBD = '〔待定〕'

# ---------- 產品（全部有圖） ----------
IMG = dict(
 gourmet=U + '2026/03/8-10_101-X-KITCHENAO-03-03-03-600x600.jpg',
 refresh=U + '2023/11/refreshmentparty-03-600x600.jpg',
 platter=U + '2023/10/KitchenAO_platter_thumbnail_%E5%B7%A5%E4%BD%9C%E5%8D%80%E5%9F%9F-1-600x600-1.png',
 staff=U + '2024/07/SM-Staff-Meal-Lv1-scaled.jpg',
 lunch=U + '2025/04/CAB-Commercial-Meal-Lv2_%E9%A0%81%E9%9D%A2_1-1-724x1024-1.jpg',
 corp=U + '2026/03/WhatsApp-Image-2026-03-25-at-3.58.36-PM-768x1024.jpeg',
 veg=U + '2025/05/9ee996d5-e50c-4745-b847-86d8e179c481-600x600.jpg',
 charsiu=U + '2019/06/Posts-04-scaled-600x600.jpg',
 claypot=U + '2026/03/WhatsApp-Image-2026-03-18-at-16.36.27-4.jpeg',
 kids=U + '2023/10/202308-KIDS-thumbnail-02.jpg',
 snacks=U + '2023/10/2.jpg',
 dessert=U + '2023/10/6.jpg',
)
# (key, 名稱, 描述, 原價文字, 連結)
SCENES = [
 ('corp', '🥂', '公司 Party', '一年的努力，值得一桌好菜', '部門聚餐、年尾慶功、Team Building', [
   ('gourmet', '美食派對 Gourmet Set', '8 至 54 人・熱食主菜', 'HK$1,988 起', '/product-category/party/foot-party/'),
   ('refresh', '輕食宴會 Refreshment Set', '12 至 40 人・酒會及茶點', 'HK$2,688 起', '/product-category/party/refreshment-set/'),
   ('platter', '5 人自選拼盤', '小型部門聚餐', 'HK$498', '/product/5-people-self-selected-platter/'),
   ('lunch', '商務餐盒', '16 款任選・獨立包裝', '按款式', '/product/business-lunch-box/')]),
 ('annual', '🏆', '年會、春茗', '年會的主角是同事，餐飲交給我們', 'Annual Dinner、春茗、頒獎禮', [
   ('corp', '公司到會及年會到會', '50 至 200 人・按人數報價', '按人數報價', '/corporate-catering-hk/'),
   ('staff', '員工膳食餐盒 Staff Meal', '大量訂購・準時送達', '按數量', '/product/staff-meal/'),
   ('gourmet', '美食派對 Gourmet Set', '30 人以上大型套餐', 'HK$5,188 起', '/product-category/party-set-by-people/30%e4%ba%ba%e4%bb%a5%e4%b8%8a%e5%88%86%e4%ba%ab%e9%81%b8%e9%a0%85/')]),
 ('cny', '🧧', '團年飯、開年飯', '團年飯在家吃，大廚送上門', '一家團聚，毋須下廚', [
   ('gourmet', '美食派對 Gourmet Set', '按人數選擇・8 人起', 'HK$1,988 起', '/product-category/party/foot-party/'),
   ('charsiu', '「香港燒」鹿兒島叉燒扒', '烤燶邊香草蜜糖・4 磅', '單點', '/product/m0140-roasted-kagoshima-pork-char-siu-with-herb-and-honey-glaze-4-pounds/'),
   ('claypot', '「冩樂」蟹皇左口魚煲仔飯', '清酒灸燒・可於套餐內選擇', '套餐內選擇', '/product-category/party-set-by-people/'),
   ('veg', '「素」味人生素食套餐', '6 至 26 人・長輩吃素之選', 'HK$1,388 起', '/product-category/party/vegetarians-set/')]),
 ('nye', '🎆', '12/31 除夕倒數', '倒數不用排隊，派對美食準時送到', '朋友聚會、家庭倒數派對', [
   ('platter', '5 人自選拼盤', '小型倒數派對', 'HK$498', '/product/5-people-self-selected-platter/'),
   ('snacks', '惹味小食', '單點加配・派對必備', '按款式', '/product-category/a-la-carte/snacks/'),
   ('dessert', '甜品', '倒數後的甜蜜時刻', '按款式', '/product-category/a-la-carte/dessert/'),
   ('kids', '派對大快樂兒童餐', '5 人起・小朋友一同倒數', 'HK$600 起', '/product-category/party/children/')]),
]
PEOPLE = [('2–6 人', '2-6'), ('7–11 人', '7-11'), ('12–16 人', '12-16'), ('18–25 人', '18-25'), ('30 人以上', '30'), ('100 人以上', '100')]
def ppl_url(k):
    m = {'2-6': '2-6人分享選項', '7-11': '7-11人分享選項', '12-16': '12-16人分享選項', '18-25': '18-25人分享選項', '30': '30人以上分享選項', '100': '100人以上分享選項'}[k]
    from urllib.parse import quote
    return B + '/product-category/party-set-by-people/' + quote(m).lower() + '/'
FAQ = [
 ('甚麼是雙 11 預購？', '於 11 月 8 日至 13 日以雙 11 價錢付款，鎖定優惠；送餐日期可於 2026 年 12 月 1 日至 2027 年 3 月 15 日期間再選擇。'),
 ('如何確認送餐日期？', '請於送餐日期最少 7 日前透過 WhatsApp 通知客服送餐日期、時間及地址，客服確認後即完成安排。'),
 ('哪些日子不適用？', '12 月 24 日至 26 日不適用。年三十及年初一至初三每日名額有限，先到先得，建議盡早確認日期。'),
 ('公司年會人數較多，可以報價嗎？', '可以。50 人以上的年會、春茗或頒獎禮，歡迎透過 WhatsApp 或報價表格查詢，客服會按人數及預算配搭餐單。'),
 ('預購後可以更改套餐嗎？', TBD + ' 更改及退款安排待確認後更新。'),
]

# =====================================================================
# LANDING
# =====================================================================
CSS = r'''
.a11{--k:#1A1A1A;--g:#C8A24A;--dg:#9A7B2E;--r:#C0392B;--bg:#FAF7F1;font-family:-apple-system,"PingFang HK","Microsoft JhengHei",sans-serif;color:var(--k);line-height:1.7;max-width:1180px;margin:0 auto}
.a11 *{box-sizing:border-box}
.a11 a{text-decoration:none}
.a11-bar{background:var(--k);color:#fff;text-align:center;font-size:14px;padding:9px 12px;border-radius:10px}
.a11-bar b{color:var(--g)}
.a11-hero{position:relative;margin-top:14px;border-radius:20px;overflow:hidden;background:radial-gradient(circle at 80% 20%,#3a2c12 0,#1A1A1A 55%);color:#fff;padding:46px 40px;display:grid;grid-template-columns:1.1fr 1fr;gap:30px;align-items:center}
.a11-hero .big{font-size:110px;line-height:1;font-weight:900;letter-spacing:-2px;color:var(--g);font-family:Georgia,serif}
.a11-hero .eb{letter-spacing:4px;font-size:13px;color:var(--g);font-weight:700}
.a11-hero h2{font-size:34px;line-height:1.35;margin:10px 0 8px;color:#fff}
.a11-hero p{color:#d8cfbf;margin:0 0 18px;font-size:16px}
.a11-hero .dates{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:22px}
.a11-hero .dates span{border:1px solid #6b5626;border-radius:30px;padding:5px 14px;font-size:13px;color:#f0e2bf}
.a11-btn{display:inline-block;padding:14px 28px;border-radius:40px;font-weight:700;font-size:16px;margin:0 8px 8px 0;cursor:pointer}
.a11-btn.p{background:var(--g);color:var(--k)}
.a11-btn.s{border:1px solid #fff;color:#fff}
.a11-btn.d{background:var(--k);color:#fff}
.a11-btn.o{border:1px solid var(--k);color:var(--k);background:#fff}
.a11-hero .imgs{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.a11-hero .imgs img{width:100%;aspect-ratio:1;object-fit:cover;border-radius:14px;border:2px solid #6b5626}
.a11-cd{display:flex;justify-content:center;align-items:center;gap:8px;margin:18px 0 6px;flex-wrap:wrap;font-size:15px}
.a11-cd b{background:var(--k);color:var(--g);border-radius:8px;padding:6px 10px;font-size:22px;min-width:48px;text-align:center;font-variant-numeric:tabular-nums}
.a11-sec{margin:44px 0 0}
.a11-h{text-align:center;margin-bottom:20px}
.a11-h .eb{color:var(--dg);font-size:13px;letter-spacing:3px;font-weight:700}
.a11-h h3{font-size:26px;margin:4px 0 6px}
.a11-h p{color:#7A7268;margin:0}
.a11-h:after{content:"";display:block;width:40px;height:2px;background:var(--g);margin:12px auto 0}
.a11-cp{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.a11-cp div{position:relative;background:#fff;border:2px dashed var(--g);border-radius:16px;padding:22px 16px;text-align:center}
.a11-cp div:before,.a11-cp div:after{content:"";position:absolute;top:50%;width:22px;height:22px;border-radius:50%;background:var(--bg);transform:translateY(-50%)}
.a11-cp div:before{left:-12px}.a11-cp div:after{right:-12px}
.a11-cp small{display:block;color:var(--dg);font-weight:700;letter-spacing:2px;font-size:12px}
.a11-cp strong{display:block;font-size:24px;margin:6px 0;color:var(--r)}
.a11-cp span{font-size:13px;color:#7A7268}
.a11-steps{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;counter-reset:s}
.a11-steps div{background:#fff;border-radius:16px;padding:22px 18px;border:1px solid #ECE6DA;counter-increment:s}
.a11-steps div:before{content:counter(s);display:inline-flex;width:34px;height:34px;border-radius:50%;background:var(--k);color:var(--g);font-weight:800;align-items:center;justify-content:center;margin-bottom:10px}
.a11-steps b{display:block;font-size:17px;margin-bottom:4px}
.a11-steps p{margin:0;color:#7A7268;font-size:14px}
.a11-note{background:#FBF7EE;border:1px solid var(--g);border-radius:14px;padding:14px 18px;margin-top:14px;font-size:14px;color:#6b4e16}
.a11-tabs{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin-bottom:16px;position:sticky;top:var(--a11top,0);z-index:5;background:var(--bg);padding:8px 0}
.a11-tabs button{border:1px solid var(--k);background:#fff;color:var(--k);border-radius:40px;padding:10px 18px;font-size:15px;font-weight:700;cursor:pointer;font-family:inherit}
.a11-tabs button.on{background:var(--k);color:#fff}
.a11-pane{display:none}.a11-pane.on{display:block}
.a11-pane .pl{text-align:center;margin:0 0 16px}
.a11-pane .pl b{display:block;font-size:22px}
.a11-pane .pl span{color:#7A7268;font-size:14px}
.a11-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.a11-pc{background:#fff;border-radius:16px;overflow:hidden;border:1px solid #ECE6DA;display:flex;flex-direction:column;color:var(--k)}
.a11-pc .im{position:relative;border:4px solid var(--g);border-bottom:0;border-radius:16px 16px 0 0;overflow:hidden}
.a11-pc .im img{width:100%;aspect-ratio:1;object-fit:cover;display:block}
.a11-pc .tag{position:absolute;left:0;top:0;background:var(--k);color:var(--g);font-weight:800;font-size:13px;padding:5px 10px;border-radius:0 0 12px 0;font-family:Georgia,serif;letter-spacing:1px}
.a11-pc .ft{position:absolute;left:0;right:0;bottom:0;background:var(--g);color:var(--k);text-align:center;font-size:12px;font-weight:700;padding:3px}
.a11-pc .tx{padding:12px 14px 14px;display:flex;flex-direction:column;flex:1}
.a11-pc b{font-size:15px;line-height:1.4}
.a11-pc small{color:#7A7268;font-size:13px;margin:2px 0 8px}
.a11-pc .pr{margin-top:auto;font-size:13px}
.a11-pc .pr del{color:#999;margin-right:6px}
.a11-pc .pr em{font-style:normal;color:var(--r);font-weight:800;font-size:15px}
.a11-pc .go{margin-top:10px;text-align:center;background:var(--k);color:#fff;border-radius:30px;padding:8px;font-size:14px;font-weight:700}
.a11-ppl{display:grid;grid-template-columns:repeat(6,1fr);gap:10px}
.a11-ppl a{display:block;text-align:center;border:1px solid var(--k);border-radius:40px;padding:11px 4px;color:var(--k);font-weight:700;background:#fff}
.a11-ppl a:hover{background:var(--k);color:#fff}
.a11 details{background:#fff;border:1px solid #ECE6DA;border-radius:12px;margin:8px 0;padding:0 16px}
.a11 summary{cursor:pointer;padding:14px 26px 14px 0;font-weight:700;list-style:none;position:relative}
.a11 summary::-webkit-details-marker{display:none}
.a11 summary:after{content:"";position:absolute;right:4px;top:50%;width:8px;height:8px;border-right:2px solid var(--dg);border-bottom:2px solid var(--dg);transform:translateY(-70%) rotate(45deg);transition:.2s}
.a11 details[open] summary:after{transform:translateY(-30%) rotate(-135deg)}
.a11 details p{margin:0 0 14px;color:#555}
.a11-end{margin:44px 0 20px;background:var(--k);color:#fff;border-radius:20px;padding:36px 20px;text-align:center}
.a11-end h3{color:var(--g);font-size:26px;margin:0 0 6px}
.a11-end p{color:#d8cfbf;margin:0 0 18px}
.a11-sticky{display:none}
.a11 .tbd{color:var(--r)}
.a11-hero .eb{margin-bottom:6px}
.a11-hero h2 span{color:var(--g)}
.a11-h h3 em{font-style:normal;color:var(--g);background:var(--k);padding:0 10px;border-radius:8px;margin-left:6px}
.a11-h.sm h3{font-size:22px}
.a11-tri{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.a11-tri a{position:relative;display:flex;flex-direction:column;align-items:center;text-align:center;background:#fff;border:1px solid #ECE6DA;border-radius:20px;padding:26px 18px 20px;color:var(--k);box-shadow:0 10px 26px rgba(40,24,15,.06);transition:transform .2s}
.a11-tri a:hover{transform:translateY(-4px)}
.a11-tri i{font-style:normal;font-size:30px;width:64px;height:64px;border-radius:50%;background:#FBF3E2;display:flex;align-items:center;justify-content:center;margin-bottom:10px}
.a11-tri small{color:var(--dg);font-weight:800;letter-spacing:2px}
.a11-tri b{font-size:19px;margin:2px 0 4px}
.a11-tri strong{font-size:30px;line-height:1.2;margin:4px 0}
.a11-tri span{color:#7A7268;font-size:14px}
.a11-tri em{font-style:normal;margin-top:12px;font-size:13px;font-weight:700;color:var(--dg)}
.a11-tri u{position:absolute;top:14px;right:14px;text-decoration:none;background:var(--r);color:#fff;font-size:12px;font-weight:800;padding:3px 9px;border-radius:20px}
.a11-lv{margin:52px 0 0;background:#fff;border-radius:24px;padding:34px 30px;border:1px solid #ECE6DA;scroll-margin-top:120px}
.a11-lv.dark{background:var(--k);color:#fff;border:0}
.a11-lvh{display:flex;align-items:center;gap:16px;margin-bottom:14px}
.a11-lvh .no{flex:none;font-family:Georgia,serif;font-size:54px;font-weight:900;line-height:1;color:var(--g)}
.a11-lvh small{color:var(--dg);font-weight:800;letter-spacing:2px}
.a11-lv.dark .a11-lvh small{color:var(--g)}
.a11-lvh h3{margin:2px 0 0;font-size:24px;line-height:1.35}
.a11-lv .lead{color:#5d534d;font-size:16px;margin:0 0 16px;max-width:820px}
.a11-lv.dark .lead{color:#d8cfbf}
.a11-ribbon{display:block;width:max-content;max-width:100%;margin:0 auto 18px;background:var(--g);color:var(--k);font-weight:800;padding:7px 26px;position:relative;font-size:14px}
.a11-ribbon:before,.a11-ribbon:after{content:"";position:absolute;top:0;bottom:0;width:14px;background:var(--g)}
.a11-ribbon:before{left:-12px;clip-path:polygon(0 0,100% 0,100% 100%,0 100%,45% 50%)}
.a11-ribbon:after{right:-12px;clip-path:polygon(0 0,100% 0,55% 50%,100% 100%,0 100%)}
.a11-how,.a11-terms{margin-top:14px}
.a11-shop{margin-top:34px;scroll-margin-top:120px}
.a11-tiers{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.a11-tier{position:relative;text-align:center;background:#FBF7EE;border:2px dashed var(--g);border-radius:18px;padding:34px 14px 22px}
.a11-tier .rib{position:absolute;top:-14px;left:50%;transform:translateX(-50%);background:var(--k);color:var(--g);font-size:12px;font-weight:800;padding:4px 14px;border-radius:20px;white-space:nowrap;letter-spacing:1px}
.a11-tier small{display:block;color:#7A7268}
.a11-tier strong{display:block;font-size:26px;margin:4px 0}
.a11-tier span{font-weight:700}
.a11-flag{display:flex;align-items:center;gap:12px;margin-top:18px;background:#fff1ec;border:1px solid #f3c9bd;border-radius:10px;padding:12px 16px;font-size:14px;color:#6b2a1e}
.a11-flag b{flex:none;background:var(--r);color:#fff;border-radius:8px;padding:4px 10px}
.a11-corp{display:grid;grid-template-columns:1.3fr 1fr;gap:26px;align-items:center}
.a11-corp img{width:100%;height:340px;object-fit:cover;border-radius:18px;border:3px solid var(--g)}
.a11-check{list-style:none;padding:0;margin:0 0 20px}
.a11-check li{padding:6px 0 6px 30px;position:relative}
.a11-check li:before{content:"✓";position:absolute;left:0;top:6px;width:20px;height:20px;border-radius:50%;background:var(--g);color:var(--k);font-size:12px;font-weight:900;display:flex;align-items:center;justify-content:center}
.a11-lv.dark .more a{color:var(--g)}
.a11-terms ul{margin:0 0 14px;padding-left:20px;color:#666;font-size:13.5px}
@media(max-width:760px){
 .a11-tri,.a11-tiers{grid-template-columns:1fr}.a11-tiers{gap:22px}
 .a11-lv{padding:26px 18px;border-radius:18px}.a11-lvh .no{font-size:42px}.a11-lvh h3{font-size:19px}
 .a11-corp{grid-template-columns:1fr}.a11-corp img{height:220px}
 .a11-flag{flex-direction:column;align-items:flex-start}
}
@media(max-width:900px){.a11-grid{grid-template-columns:repeat(2,1fr)}.a11-ppl{grid-template-columns:repeat(3,1fr)}}
@media(max-width:760px){
 .a11-hero{grid-template-columns:1fr;padding:30px 20px;text-align:center}.a11-hero .big{font-size:76px}.a11-hero h2{font-size:26px}.a11-hero .dates{justify-content:center}
 .a11-cp,.a11-steps{grid-template-columns:1fr}
 .a11-tabs{flex-wrap:nowrap;overflow-x:auto;justify-content:flex-start}.a11-tabs button{white-space:nowrap}
 .a11-sticky{display:flex;position:fixed;left:0;right:0;bottom:0;z-index:99;gap:8px;padding:10px 12px;background:rgba(26,26,26,.96)}
 .a11-sticky a{flex:1;text-align:center;border-radius:30px;padding:11px;font-weight:700;font-size:15px}
 .a11-sticky .p{background:var(--g);color:var(--k)}.a11-sticky .s{border:1px solid #fff;color:#fff}
}
'''

def card(k, n, d, pr, u):
    return (f'<a class="a11-pc" href="{B}{u}" data-ga="1111_product" target="_blank">'
            f'<div class="im"><img src="{IMG[k]}" alt="{n}" loading="lazy"><span class="tag">11.11</span><span class="ft">年尾飯局預購</span></div>'
            f'<div class="tx"><b>{n}</b><small>{d}</small>'
            f'<div class="pr"><del>{pr}</del><em>雙 11 價 <span class="tbd">{TBD}</span></em></div>'
            f'<span class="go">加入預購</span></div></a>')

def landing():
    tabs = ''.join(f'<button type="button" data-t="{k}"{" class=on" if i == 0 else ""}>{ic} {name}</button>' for i, (k, ic, name, *_r) in enumerate(SCENES))
    panes = ''.join(
        f'<div class="a11-pane{" on" if i == 0 else ""}" data-p="{k}"><div class="pl"><b>「{pl}」</b><span>{sub}</span></div>'
        f'<div class="a11-grid">' + ''.join(card(*p) for p in prods) + '</div></div>'
        for i, (k, ic, name, pl, sub, prods) in enumerate(SCENES))
    ppl = ''.join(f'<a href="{ppl_url(k)}" target="_blank">{t}</a>' for t, k in PEOPLE)
    faq = ''.join(f'<details><summary>{q}</summary><p>{a.replace(TBD, chr(60)+"span class=tbd"+chr(62)+TBD+"</span>")}</p></details>' for q, a in FAQ)
    corp_list = ''.join(f'<li>{x}</li>' for x in ['11 月 11 日或之前確認年會報價', f'早鳥禮遇 <span class="tbd">{TBD}</span>', '優先安排 12 月至 2 月旺季檔期', '專人跟進餐單、人數及送餐安排'])
    tiers = ''.join(f'<div class="a11-tier"><div class="rib">滿額賞 0{i}</div><small>單一訂單滿</small><strong>HK$ <span class="tbd">{TBD}</span></strong><span>送 <span class="tbd">{TBD}</span></span></div>' for i in (1, 2, 3))
    body = f'''<div class="a11" id="a11">
<div class="a11-bar">🔥 <b>雙 11 年尾飯局預購三重賞</b>｜11 月 8 日至 13 日限定｜送餐期至 2027 年 3 月 15 日</div>

<section class="a11-hero">
 <div>
  <div class="eb">KITCHEN AO・11.11</div>
  <h2>雙 11 年尾飯局<br><span>預購三重賞</span></h2>
  <p>多謝你一直支持 Kitchen AO。今年雙 11，以 11 月的價錢預購年尾飯局，公司 Party、年會、團年飯及除夕倒數，一次安排妥當。</p>
  <div class="dates"><span>📅 付款：11/8 至 11/13</span><span>🚚 送餐：2026/12/1 至 2027/3/15</span></div>
  <a class="a11-btn p" href="#a11-tri" data-ga="1111_hero_tri">查看三重賞</a><a class="a11-btn s" href="#a11-3" data-ga="1111_hero_corp">企業早鳥報價</a>
 </div>
 <div class="imgs"><img src="{IMG['gourmet']}" alt="美食派對 Gourmet Set"><img src="{IMG['charsiu']}" alt="鹿兒島叉燒扒"><img src="{IMG['claypot']}" alt="蟹皇左口魚煲仔飯"><img src="{IMG['refresh']}" alt="輕食宴會套餐"></div>
</section>

<div class="a11-cd" id="a11cd"><span id="a11cdl">距離開賣</span><b id="a11d">0</b>日<b id="a11h">00</b>時<b id="a11m">00</b>分<b id="a11s">00</b>秒</div>

<section class="a11-sec" id="a11-tri">
 <div class="a11-h"><div class="eb">11.11 TRIPLE REWARDS</div><h3>無論公司或家庭，優惠都<em>三重加碼</em></h3></div>
 <div class="a11-tri">
  <a href="#a11-1" data-ga="1111_tri_1"><i>🔒</i><small>第一重</small><b>預購寄倉價</b><strong class="tbd">{TBD}</strong><span>11 月的價錢，年尾照樣享用</span><em>了解更多 ↓</em></a>
  <a href="#a11-2" data-ga="1111_tri_2"><i>🎁</i><small>第二重</small><b>滿額賞</b><strong class="tbd">{TBD}</strong><span>買得越多，送得越多</span><em>了解更多 ↓</em><u>限量</u></a>
  <a href="#a11-3" data-ga="1111_tri_3"><i>🏆</i><small>第三重</small><b>企業早鳥賞</b><strong class="tbd">{TBD}</strong><span>年會檔期優先安排</span><em>了解更多 ↓</em></a>
 </div>
</section>

<section class="a11-lv" id="a11-1">
 <div class="a11-lvh"><span class="no">01</span><div><small>第一重</small><h3>預購寄倉價：11 月的價錢，年尾照樣享用</h3></div></div>
 <p class="lead">指定年尾飯局套餐於 11 月 8 日至 13 日付款即享雙 11 價錢，送餐日期可於 2026 年 12 月 1 日至 2027 年 3 月 15 日期間再選擇。年會、團年飯及開年飯，一次預購妥當。</p>
 <div class="a11-ribbon">人人適用・指定套餐</div>
 <div class="a11-steps">
  <div><b>11/8 至 11/13 付款</b><p>以雙 11 價錢預購年尾飯局套餐，價錢即時鎖定。</p></div>
  <div><b>選擇送餐日期</b><p>送餐日期最少 7 日前，透過 WhatsApp 通知客服日期、時間及地址。</p></div>
  <div><b>準時送到</b><p>2026 年 12 月 1 日至 2027 年 3 月 15 日期間，全港送遞。</p></div>
 </div>
 <details class="a11-how"><summary>如何使用？</summary><p>完成付款後，訂單會標示為「雙 11 預購」。送餐日期最少 7 日前透過 WhatsApp 聯絡客服，提供訂單編號、送餐日期、時間及地址即可。12 月 24 日至 26 日不適用；年三十（2027 年 2 月 5 日）及年初一至初三每日名額有限，先到先得。</p></details>
 <div id="a11-shop" class="a11-shop">
  <div class="a11-h sm"><div class="eb">SHOP BY OCCASION</div><h3>按場合選擇年尾飯局</h3></div>
  <div class="a11-tabs" role="tablist">{tabs}</div>
  {panes}
 </div>
</section>

<section class="a11-lv" id="a11-2">
 <div class="a11-lvh"><span class="no">02</span><div><small>第二重</small><h3>滿額賞：買得越多，送得越多</h3></div></div>
 <p class="lead">雙 11 期間單一訂單滿指定金額，即可獲贈禮品。與預購寄倉價可同時使用，系統於結帳時自動計算。</p>
 <div class="a11-tiers">{tiers}</div>
 <div class="a11-flag"><b>限量 <span class="tbd">{TBD}</span> 份</b>送完即止，以付款時間先後為準。</div>
</section>

<section class="a11-lv dark" id="a11-3">
 <div class="a11-lvh"><span class="no">03</span><div><small>第三重</small><h3>企業早鳥賞：年會的主角是同事，餐飲交給我們</h3></div></div>
 <div class="a11-corp">
  <div>
   <p class="lead">12 月至 2 月是年會、團年飯及春茗旺季。於 11 月 11 日或之前確認報價，即享企業早鳥禮遇，並優先安排檔期。</p>
   <ul class="a11-check">{corp_list}</ul>
   <a class="a11-btn p" href="{WA}" target="_blank" data-ga="1111_corp_wa">WhatsApp 企業客戶專員</a><a class="a11-btn s" href="{B}/catering-quote-enquiry/" target="_blank" data-ga="1111_corp_form">填寫報價表格</a>
   <p class="more"><a href="{B}/corporate-catering-hk/" target="_blank">了解公司到會服務 →</a></p>
  </div>
  <img src="{IMG['corp']}" alt="Kitchen AO 公司年會到會" loading="lazy">
 </div>
</section>

<section class="a11-sec">
 <div class="a11-h"><div class="eb">BY GUESTS</div><h3>按人數選擇套餐</h3></div>
 <div class="a11-ppl">{ppl}</div>
</section>

<section class="a11-sec">
 <div class="a11-h"><div class="eb">FAQ</div><h3>雙 11 預購常見問題</h3></div>
 {faq}
</section>

<section class="a11-end">
 <h3>早一步預訂，旺季不用等</h3>
 <p>年三十及年會旺季名額有限，雙 11 先鎖定。</p>
 <a class="a11-btn p" href="#a11-shop" data-ga="1111_end_shop">立即預購</a><a class="a11-btn s" href="{WA}" target="_blank" data-ga="1111_end_wa">WhatsApp 查詢</a>
</section>

<details class="a11-terms"><summary>條款及細則</summary><ul>
 <li>雙 11 預購優惠只適用於 2026 年 11 月 8 日至 13 日期間完成付款的訂單。</li>
 <li>送餐期為 2026 年 12 月 1 日至 2027 年 3 月 15 日；12 月 24 日至 26 日不適用。</li>
 <li>年三十及年初一至初三每日名額有限，以確認日期先後為準。</li>
 <li>滿額賞禮品數量有限，送完即止；禮品不可兌換現金。</li>
 <li>更改、取消及退款安排：<span class="tbd">{TBD}</span></li>
 <li>如有任何爭議，Kitchen AO 保留最終決定權。</li>
</ul></details>

<div class="a11-sticky"><a class="p" href="#a11-shop" data-ga="1111_sticky_shop">立即預購</a><a class="s" href="{WA}" target="_blank" data-ga="1111_sticky_wa">WhatsApp</a></div>
</div>'''
    js = r'''(function(){var R=document.getElementById('a11');if(!R)return;
var T=R.querySelectorAll('.a11-tabs button'),P=R.querySelectorAll('.a11-pane');
[].forEach.call(T,function(b){b.addEventListener('click',function(){[].forEach.call(T,function(x){x.classList.toggle('on',x===b)});[].forEach.call(P,function(p){p.classList.toggle('on',p.getAttribute('data-p')===b.getAttribute('data-t'))});window.dataLayer=window.dataLayer||[];dataLayer.push({event:'cta_click',cta:'1111_tab_'+b.getAttribute('data-t')})})});
[].forEach.call(R.querySelectorAll('[data-ga]'),function(a){a.addEventListener('click',function(){window.dataLayer=window.dataLayer||[];dataLayer.push({event:'cta_click',cta:a.getAttribute('data-ga')})})});
var S=Date.UTC(2026,10,7,16,0,0),E=Date.UTC(2026,10,13,15,59,59);
function pad(n){return(n<10?'0':'')+n}
function tick(){var n=Date.now(),t,l;if(n<S){t=S-n;l='距離開賣'}else if(n<E){t=E-n;l='距離優惠結束'}else{document.getElementById('a11cd').style.display='none';return}
document.getElementById('a11cdl').textContent=l;var s=Math.floor(t/1000);document.getElementById('a11d').textContent=Math.floor(s/86400);document.getElementById('a11h').textContent=pad(Math.floor(s%86400/3600));document.getElementById('a11m').textContent=pad(Math.floor(s%3600/60));document.getElementById('a11s').textContent=pad(s%60)}
tick();setInterval(tick,1000);
var h=document.getElementById('header');if(h){R.style.setProperty('--a11top',(h.offsetHeight||0)+'px')}})();'''
    raw = f'<style>{CSS}</style>\n{body}\n<script>{js}</script>\n'
    open(os.path.join(H, 'landing-rawhtml.html'), 'w', encoding='utf-8').write(raw)
    prev = ('<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>雙 11 年尾飯局預購 2026｜Kitchen AO（預覽）</title><style>body{margin:0;background:#FAF7F1;padding:16px 16px 90px}'
            '.pv{max-width:1180px;margin:0 auto 14px;background:#fff8e6;border:1px dashed #d9a93b;border-radius:10px;padding:10px 14px;font:13px/1.6 sans-serif;color:#7a5a12}'
            '.pv h1{font-size:15px;margin:0}</style></head><body>'
            '<div class="pv"><h1>預覽｜WP 頁面標題（H1）：雙 11 年尾飯局預購 2026｜公司年會、團年飯到會｜網址：/1111/</h1>'
            '紅色〔待定〕＝優惠數字未決定。產品圖加「11.11」框只用 CSS，毋須另外做圖。</div>' + raw + '</body></html>')
    open(os.path.join(H, 'landing.html'), 'w', encoding='utf-8').write(prev)
    return raw

# =====================================================================
# EDM（沿用中秋團圓套餐 EDM 版型）
# =====================================================================
UTM = 'utm_source=edm&utm_medium=email&utm_campaign=1111_2026'
def u(path): return f'{B}{path}{"&" if "?" in path else "?"}{UTM}'
def btn_primary(t, href, w=320):
    return (f'<table role="presentation" cellpadding="0" cellspacing="0" align="center" class="btn-primary" width="100%" style="margin:0 auto;width:100%;max-width:{w}px;"><tr><td align="center" style="border-radius:40px;">'
            f'<a href="{href}" target="_blank" rel="noopener noreferrer" style="display:block;padding:16px 20px;font-size:18px;font-weight:bold;letter-spacing:1px;text-decoration:none;border-radius:40px;text-align:center;">{t}</a></td></tr></table>')
def btn_dark(t, href, w=320):
    return (f'<table role="presentation" cellpadding="0" cellspacing="0" align="center" width="100%" style="margin:0 auto;width:100%;max-width:{w}px;"><tr><td align="center" bgcolor="#1A1A1A" style="background:#1A1A1A;border-radius:40px;">'
            f'<a href="{href}" target="_blank" rel="noopener noreferrer" style="display:block;padding:15px 20px;color:#E4C77E;font-size:18px;font-weight:bold;letter-spacing:2px;text-decoration:none;border-radius:40px;text-align:center;">{t}</a></td></tr></table>')
COUPON_URL = 'https://aoaodelivery.com/?wdr_coupon=DOUBLE11&utm_source=edm&utm_medium=email&utm_campaign=1111_2026'
GIFT = dict(
 a1600=('A1600 日式雞皮餃子配酥炸洋蔥圈', 198, U + '2023/10/KitchenAO_MAY2023-ALA-CARTE-03.png', '/product/a1600-japanese-chicken-skin-dumplings-with-crispy-onion-rings/'),
 a0500=('A0500 蜜蜜燒雞翼配脆薯角', 188, U + '2019/06/Posts-16-1024x1024.jpg', '/product/a0500-honey-glazed-chicken-wings-w-potato-wedges/'),
 a1500=('A1500 避風塘炸海鮮豆腐配海鮮甜醬', 178, U + '2019/06/KitchenAO_MAY2023-ALA-CARTE-04.png', '/product/a1500-crispy-seafood-tofu-in-traditional-typhoon-shelter-style/'),
)
GH = 'https://expandsolutionshk.github.io/kitchenao-edm/1111-2026/img/'
MEMBER = {'B1': ('精選堅果或薯片 1 包', GH + 'd11-member-chips.jpg'), 'B2': ('「有得解」或冷泡茶 6 包', GH + 'd11-member-tea.jpg'), 'B3': ('精選紅白葡萄酒 1 枝', GH + 'd11-member-wine.jpg')}
TIERS = [('B1', '1,500', ['a1600']), ('B2', '2,200', ['a1600', 'a1500']), ('B3', '3,000', ['a1600', 'a1500', 'a0500'])]
RED = '#C0392B'

def edm_card(k, n, d, pr, path):
    return (f'<td class="stack" width="50%" valign="top" style="padding:6px;"><a href="{u(path)}" target="_blank" rel="noopener noreferrer" style="text-decoration:none;">'
            f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#ffffff;border:3px solid #C8A24A;border-radius:14px;overflow:hidden;">'
            f'<tr><td style="padding:0;font-size:0;line-height:0;"><img src="{IMG[k]}" width="280" alt="{n}" style="width:100%;height:auto;display:block;"></td></tr>'
            f'<tr><td style="padding:10px 12px 12px;background:#ffffff;"><p style="margin:0 0 3px;color:#1A1A1A;font-size:15px;font-weight:bold;line-height:20px;">{n}</p>'
            f'<p style="margin:0 0 6px;color:#7A7268;font-size:13px;line-height:17px;">{d}</p>'
            f'<p style="margin:0;font-size:13px;"><span style="color:#7A7268;">{pr}</span>　<span style="color:{RED};font-weight:bold;">雙 11 再減 11%</span></p></td></tr></table></a></td>')

def code_box(code, dark=False):
    bg = '#ffffff' if dark else '#1A1A1A'; fg = '#1A1A1A' if dark else '#C8A24A'
    return (f'<table role="presentation" cellpadding="0" cellspacing="0" align="center" style="margin:0 auto;"><tr>'
            f'<td style="padding:6px 12px;color:#9A8F7E;font-size:12px;font-weight:bold;letter-spacing:2px;">優惠碼</td>'
            f'<td bgcolor="{bg}" style="background:{bg};border-radius:10px;padding:10px 24px;color:{fg};font-family:Arial,Helvetica,sans-serif;font-size:26px;line-height:30px;font-weight:bold;letter-spacing:4px;">{code}</td>'
            '</tr></table>')

def edm():
    src = open(os.path.join(H, '..', 'midautumn-sets-2026-v2', 'index.html'), encoding='utf-8').read().split('\n')
    head = '\n'.join(src[7:65])
    tail = '\n'.join(src[213:236] + src[272:284] + src[298:])
    head = head.replace('<title>Kitchen AO 中秋團圓套餐 2026</title>', '<title>Kitchen AO 雙 11 四重賞</title>')
    head = re.sub(r'(<div style="display:none;max-height:0;[^>]*>\n).*?(\n</div>)', r'\1雙 11 四重賞｜一連七天｜滿 HK$1,100 全網 11% OFF，滿 HK$1,500 起再送人氣小食｜優惠碼 DOUBLE11\2', head, flags=re.S)
    tail = re.sub(r'utm_campaign=midautumn2026', 'utm_campaign=1111_2026', tail)
    for a, b in [('睇 Reels →', '觀看 Reels →'), ('大品牌活動都揀 Kitchen AO', '大品牌活動之選 Kitchen AO'), ('需於套餐內揀選', '可於套餐內選擇'),
                 ('以下為人氣主菜，可於「人數選餐」套餐內揀選', '以下為人氣主菜，可於「人數選餐」套餐內選擇'), ('👥 按人數揀套餐 →', '👥 按人數選擇套餐 →'),
                 ('大量訂購 / 想度身訂造餐單？', '大量訂購或度身訂造餐單'), ('%E6%94%B6%E5%88%B0%E9%9B%BB%E9%83%B5%E6%8E%A8%E5%BB%A3%E6%83%B3%E6%9F%A5%E8%A9%A2', WA.split('text=')[1])]:
        tail = tail.replace(a, b)
    nav = (f'<tr><td style="padding:14px 20px 12px;background:#ffffff;border-bottom:2px solid #C8A24A;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0">'
           f'<tr><td align="center" style="padding-bottom:11px;"><a href="{u("/")}" target="_blank" rel="noopener noreferrer"><img class="hlogo" src="{B}/wp-content/uploads/2023/08/kitchenAO_logo_horizontal.png" width="185" alt="Kitchen AO" style="width:185px;height:auto;margin:0 auto;display:block;"></a></td></tr>'
           f'<tr><td align="center" class="nav"><table role="presentation" cellpadding="0" cellspacing="0" align="center" style="border-collapse:collapse;"><tr>'
           f'<td class="navblk" bgcolor="#1A1A1A" style="background:#1A1A1A;border-radius:6px 0 0 6px;"><a href="{u("/")}" target="_blank" rel="noopener noreferrer" style="display:block;padding:8px 13px;color:#ffffff;font-size:14px;font-weight:bold;text-decoration:none;white-space:nowrap;">網站首頁</a></td>'
           f'<td class="navblk" bgcolor="#1A1A1A" style="background:#1A1A1A;border-left:1px solid #C8A24A;"><a href="{u("/product-category/party/")}" target="_blank" rel="noopener noreferrer" style="display:block;padding:8px 13px;color:#ffffff;font-size:14px;font-weight:bold;text-decoration:none;white-space:nowrap;">快速查看餐單</a></td>'
           f'<td class="navblk" bgcolor="#1A1A1A" style="background:#1A1A1A;border-radius:0 6px 6px 0;border-left:1px solid #C8A24A;"><a href="{WA}" target="_blank" rel="noopener noreferrer" style="display:block;padding:8px 13px;color:#ffffff;font-size:14px;font-weight:bold;text-decoration:none;white-space:nowrap;">WhatsApp</a></td>'
           f'</tr></table></td></tr></table></td></tr>')
    greet = ('<tr><td style="padding:11px 24px;background:#FBF7EE;border-bottom:1px solid #EEE6D6;"><div style="font-size:14.5px;color:#1A1A1A;font-weight:bold;">{{contact.first_name|"朋友"}}，你好 👋</div>'
             '<div style="font-size:13.5px;color:#9A8f7e;margin-top:3px;">電子報・2026 年 11 月・雙 11 優惠號</div></td></tr>')
    kv = (f'<tr><td style="padding:0;background:#F3E7D2;font-size:0;line-height:0;"><a href="{u("/")}" target="_blank" rel="noopener noreferrer">'
          f'<img src="{GH}d11-kv.jpg" width="680" alt="11.11 一連七天：滿 HK$1,100 全網 11% OFF，滿 HK$1,500 起再送人氣小食，最多送 3 款" style="width:100%;max-width:680px;height:auto;display:block;border:0;"></a></td></tr>')
    coupon = ('<tr><td style="padding:28px 40px 32px;background:#F3E7D2;">'
              '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" bgcolor="#ffffff" style="background:#ffffff;border:1px solid #C8A24A;"><tr><td style="padding:6px;">'
              '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border:1px solid #E6D3A6;"><tr><td align="center" style="padding:26px 20px 24px;">'
              '<p style="margin:0;padding-left:5px;color:#9A7B2E;font-family:\'Helvetica Neue\',Helvetica,Arial,sans-serif;font-size:11px;letter-spacing:5px;">PROMOTION CODE</p>'
              '<p style="margin:12px 0 0;padding-left:8px;color:#1A1A1A;font-family:\'Helvetica Neue\',Helvetica,Arial,sans-serif;font-size:34px;line-height:40px;font-weight:300;letter-spacing:8px;">DOUBLE11</p>'
              '<table role="presentation" cellpadding="0" cellspacing="0" align="center" style="margin:16px auto 14px;"><tr><td width="60" style="border-top:1px solid #C8A24A;font-size:0;line-height:0;">&nbsp;</td></tr></table>'
              '<p style="margin:0;color:#5d534d;font-size:14px;letter-spacing:1px;">優惠期　2026.11.11 至 11.17</p></td></tr></table></td></tr></table></td></tr>')
    intro = ('<tr><td align="center" style="padding:34px 40px 6px;background:#ffffff;"><div style="width:46px;height:4px;border-radius:3px;background:#C8A24A;margin:0 auto 18px;"></div>'
             '<p style="margin:0 auto;max-width:460px;color:#5d534d;font-size:15.5px;line-height:1.95;">多謝你一直支持 Kitchen AO。雙 11 一連七天，網站下單滿 HK$1,100，輸入優惠碼 DOUBLE11 即享全網 11% OFF；滿 HK$1,500 起更可額外獲贈人氣小食，會員優惠亦照常享用。</p></td></tr>')
    # ---- 優惠 B ----
    def gift_td(k):
        n, p, img, path = GIFT[k]
        return (f'<td width="33.33%" valign="top" align="center" style="padding:4px;"><a href="{u(path)}" target="_blank" rel="noopener noreferrer" style="text-decoration:none;">'
                f'<img src="{img}" width="150" alt="{n}" style="width:100%;max-width:150px;height:auto;display:block;margin:0 auto 6px;border-radius:10px;">'
                f'<p style="margin:0;color:#1A1A1A;font-size:12.5px;line-height:17px;font-weight:bold;">{n.split(" ", 1)[1]}</p>'
                f'<p style="margin:2px 0 0;color:#9A8F7E;font-size:12px;">10 件・原價 HK${p}</p></a></td>')
    def tier(t, amt, ks):
        val = sum(GIFT[k][1] for k in ks)
        more = '或以上' if t == 'B3' else ''
        lv = {'B1': '第二賞', 'B2': '第三賞', 'B3': '第四賞'}[t]
        cells = ''.join(gift_td(k) for k in ks) + ''.join('<td width="33.33%"></td>' for _ in range(3 - len(ks)))
        return (f'<tr><td style="padding:8px 20px;background:#F3E7D2;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#ffffff;border:1px solid #E3CFA6;border-radius:14px;"><tr><td style="padding:16px 14px 14px;">'
                f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td valign="middle"><span style="display:inline-block;background:#C8A24A;color:#1A1A1A;font-size:12px;font-weight:bold;padding:3px 10px;border-radius:10px;">{lv}</span>'
                f'<span style="color:#1A1A1A;font-size:18px;font-weight:800;margin-left:8px;">滿 HK${amt}{more}</span></td>'
                f'<td align="right" valign="middle" style="color:#9A7B2E;font-size:13px;font-weight:bold;white-space:nowrap;">送 {len(ks)} 款・小食總值 HK${val}</td></tr></table>'
                f'<p style="margin:6px 0 10px;color:#7A6A50;font-size:13.5px;">全單 11% OFF 之外，再送：</p>'
                f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#FBF7EE;border-radius:10px;"><tr>{cells}</tr></table>'
                '</td></tr></table></td></tr>')
    tier1 = ('<tr><td style="padding:8px 20px;background:#F3E7D2;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#1A1A1A;border-radius:14px;"><tr><td style="padding:18px 16px;">'
             '<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td valign="middle"><span style="display:inline-block;background:#C8A24A;color:#1A1A1A;font-size:12px;font-weight:bold;padding:3px 10px;border-radius:10px;">第一賞</span>'
             '<span style="color:#ffffff;font-size:18px;font-weight:800;margin-left:8px;">滿 HK$1,100</span></td>'
             '<td align="right" valign="middle" style="color:#E4C77E;font-family:Arial,Helvetica,sans-serif;font-size:30px;font-weight:900;white-space:nowrap;">11% OFF</td></tr></table>'
             '<p style="margin:8px 0 0;color:#CFC4AE;font-size:14px;line-height:21px;">全網所有套餐及單點，全單即減 11%。</p></td></tr></table></td></tr>')
    offB = ('<tr><td align="center" style="padding:30px 20px 10px;background:#F3E7D2;">'
            '<p style="margin:0 0 4px;color:#9A7B2E;font-size:12px;font-weight:bold;letter-spacing:3px;">FOUR REWARDS</p>'
            '<p style="margin:0 0 4px;color:#1A1A1A;font-size:24px;line-height:32px;font-weight:800;">雙 11 四重賞</p>'
            + '</td></tr>'
            + f'<tr><td style="padding:16px 0 0;background:#F3E7D2;font-size:0;line-height:0;"><a href="{u("/")}" target="_blank" rel="noopener noreferrer"><img src="{GH}d11-rewards.jpg" width="680" alt="雙 11 四重賞：第一賞滿 HK$1,100 全單 11% OFF；第二賞滿 HK$1,500 送日式雞皮餃子 10 件（原價 $198）；第三賞滿 HK$2,200 再加送避風塘海鮮豆腐 10 件（原價 $178）；第四賞滿 HK$3,000 再加送蜜蜜燒雞翼 10 件（原價 $188）" style="width:100%;max-width:680px;height:auto;display:block;border:0;"></a></td></tr>'
            + '<tr><td style="padding:0 0 22px;background:#F3E7D2;font-size:0;line-height:0;">&nbsp;</td></tr>')
    member2 = ('<tr><td align="center" style="padding:30px 24px 6px;background:#ffffff;">'
               '<p style="margin:0 0 4px;color:#9A7B2E;font-size:12px;font-weight:bold;letter-spacing:3px;">MEMBER ZONE</p>'
               '<p style="margin:0 0 6px;color:#1A1A1A;font-size:22px;line-height:30px;font-weight:800;">雙 11 優惠以外，會員優惠照常享用</p>'
               '<p style="margin:0;color:#7A7268;font-size:14.5px;line-height:22px;">網站下單，「多買多賞」及舊會員專屬優惠可與雙 11 四重賞同時享用。</p></td></tr>'
               f'<tr><td style="padding:14px 20px 8px;background:#ffffff;"><a href="{u("/%e6%9c%80%e6%96%b0%e6%b6%88%e6%81%af/")}" target="_blank" rel="noopener noreferrer"><img src="https://aoaodelivery.com/wp-content/uploads/2024/10/%E6%9C%83%E5%93%A1%E5%84%AA%E6%83%A0_%E5%B7%A5%E4%BD%9C%E5%8D%80%E5%9F%9F-1-2048x852.jpg" width="640" alt="多買多賞：網站下單每滿 HK$1,500 送精選堅果或薯片 1 包，每滿 HK$2,200 送「有得解」或冷泡茶 6 包，每滿 HK$3,000 送精選紅白葡萄酒 1 枝，無封頂" style="width:100%;max-width:640px;height:auto;display:block;border:0;border-radius:12px;"></a></td></tr>'
               f'<tr><td style="padding:8px 20px 26px;background:#ffffff;"><a href="{u("/%e6%9c%80%e6%96%b0%e6%b6%88%e6%81%af/")}" target="_blank" rel="noopener noreferrer"><img src="https://aoaodelivery.com/wp-content/uploads/2024/10/%E6%9C%83%E5%93%A1%E5%84%AA%E6%83%A0-02-2048x852.jpg" width="640" alt="舊會員專屬優惠：上一張訂單金額每 HK$2,000，是次消費減 HK$100，如此類推" style="width:100%;max-width:640px;height:auto;display:block;border:0;border-radius:12px;"></a></td></tr>')
    # ---- 會員優惠照常享用 ----
    mrow = lambda amt, g: (f'<tr><td style="padding:9px 0;border-bottom:1px solid #EEE3CC;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>'
                           f'<td width="110" valign="middle" style="color:#1A1A1A;font-size:15px;font-weight:800;">每滿 HK${amt}</td>'
                           f'<td valign="middle" style="color:#5d534d;font-size:14.5px;line-height:20px;">送 {g}</td></tr></table></td></tr>')
    member = ('<tr><td style="padding:28px 20px 8px;background:#ffffff;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#FBF7EE;border:1px solid #E8D9B2;border-radius:14px;"><tr><td style="padding:20px 20px 18px;">'
              '<p style="margin:0 0 2px;color:#9A7B2E;font-size:12px;font-weight:bold;letter-spacing:3px;">MEMBER ZONE</p>'
              '<p style="margin:0 0 6px;color:#1A1A1A;font-size:20px;font-weight:800;">會員優惠照常享用</p>'
              '<p style="margin:0 0 8px;color:#7A7268;font-size:14px;line-height:21px;">雙 11 優惠以外，網站原有的會員「多買多賞」亦同時適用，無封頂：</p>'
              '<table role="presentation" width="100%" cellpadding="0" cellspacing="0">'
              + mrow('1,500', '精選堅果或薯片 1 包') + mrow('2,200', '「有得解」或冷泡茶 6 包') + mrow('3,000', '精選紅白葡萄酒 1 枝')
              + '</table>'
              '<p style="margin:12px 0 0;color:#1A1A1A;font-size:14px;line-height:21px;"><b>舊會員專屬：</b>上次訂單滿 HK$2,000，今次自動減 HK$100，如此類推。</p>'
              f'<p style="margin:12px 0 0;padding:10px 12px;background:#ffffff;border-radius:8px;color:#6b2a1e;font-size:13.5px;line-height:20px;"><b>例如</b>：訂單滿 HK$1,500，輸入 D11B 即享全單 89 折，送日式雞皮餃子配酥炸洋蔥圈，再加會員多買多賞精選堅果或薯片 1 包。</p>'
              '</td></tr></table></td></tr>')
    scenes = ''
    for k, ic, name, pl, sub, prods in SCENES:
        rows = ''.join('<tr>' + ''.join(edm_card(*p) for p in prods[i:i + 2]) + ('<td class="stack" width="50%"></td>' if len(prods[i:i + 2]) == 1 else '') + '</tr>' for i in range(0, len(prods), 2))
        scenes += (f'<tr><td align="center" style="padding:30px 30px 4px;background:#ffffff;"><p style="margin:0 0 4px;color:#9A7B2E;font-size:14px;font-weight:bold;">{ic} {name}</p>'
                   f'<p style="margin:0 0 4px;color:#1A1A1A;font-size:20px;font-weight:800;line-height:28px;">「{pl}」</p><p style="margin:0;color:#7A7268;font-size:14px;">{sub}</p>'
                   '<div style="width:40px;height:2px;background:#C8A24A;margin:10px auto 0;"></div></td></tr>'
                   f'<tr><td style="padding:12px 16px 6px;background:#ffffff;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0">{rows}</table></td></tr>')
    sc_head = ('<tr><td align="center" style="padding:30px 30px 0;background:#ffffff;"><p style="margin:0 0 4px;color:#9A7B2E;font-size:13px;font-weight:bold;letter-spacing:3px;">SHOP BY OCCASION</p>'
               '<p style="margin:0;color:#1A1A1A;font-size:21px;font-weight:800;">年尾飯局，按場合選擇</p></td></tr>')
    ppl_btn = lambda t, k: f'<td width="33.33%" align="center" style="padding:4px;"><a href="{ppl_url(k)}?{UTM}" target="_blank" rel="noopener noreferrer" style="display:block;padding:11px 4px;border:1px solid #1A1A1A;border-radius:40px;color:#1A1A1A;font-size:15px;font-weight:bold;text-decoration:none;">{t}</a></td>'
    ppl = ('<tr><td align="center" style="padding:26px 30px 2px;background:#ffffff;"><p style="margin:0 0 6px;color:#1A1A1A;font-size:21px;font-weight:800;">按人數選擇套餐</p><p style="margin:0;color:#7A7268;font-size:15px;">由 2 人至 100 人以上，均有合適選擇</p></td></tr>'
           '<tr><td style="padding:10px 16px 6px;background:#ffffff;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0">'
           '<tr>' + ''.join(ppl_btn(*p) for p in PEOPLE[:3]) + '</tr><tr>' + ''.join(ppl_btn(*p) for p in PEOPLE[3:]) + '</tr></table></td></tr>')
    info = ('<tr><td align="center" style="padding:18px 30px 6px;background:#ffffff;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#FBF7EE;border:1px solid #C8A24A;border-radius:14px;"><tr><td align="left" style="padding:16px 18px;">'
            '<p style="margin:0;color:#8a5a00;font-size:15px;font-weight:700;line-height:1.9;">📅 優惠期：2026 年 11 月 11 日至 17 日<br>'
            '🏷️ 優惠碼：DOUBLE11<br>🎁 滿 HK$1,100 全網 11% OFF；滿 HK$1,500 起再送人氣小食<br>⭐ 會員多買多賞及舊會員優惠照常享用</p></td></tr></table></td></tr>'
            f'<tr><td align="center" style="padding:18px 30px 30px;background:#ffffff;">{btn_primary("立即預訂索取四重賞", u("/"), 300)}'
            '<table role="presentation" cellpadding="0" cellspacing="0" align="center" width="100%" style="margin:10px auto 0;width:100%;max-width:300px;"><tr><td align="center" style="border-radius:40px;">'
            f'<a href="{WA}" target="_blank" rel="noopener noreferrer" style="display:block;padding:12px 20px;background:#ffffff;border:1.5px solid #1A1A1A;color:#1A1A1A;font-size:17px;font-weight:bold;letter-spacing:1px;text-decoration:none;border-radius:40px;text-align:center;">WhatsApp 查詢</a></td></tr></table></td></tr>'
            '<tr><td style="padding:0 30px 26px;background:#ffffff;"><p style="margin:0;color:#9A8F7E;font-size:12px;line-height:19px;">'
            '條款：優惠只適用於 2026 年 11 月 11 日至 17 日期間於網站完成付款的訂單；贈品按單一訂單金額計算；贈品數量有限，送完即止，不可兌換現金；如有任何爭議，Kitchen AO 保留最終決定權。</p></td></tr>')
    cta1 = f'<tr><td align="center" style="padding:20px 30px 34px;background:#ffffff;">{btn_dark("立即預訂索取四重賞", u("/"))}</td></tr>'
    html = ('<!--\n============================================================\nKitchen AO — 2026 雙 11 四重賞 EDM — Raw HTML for FluentCRM\n'
            '版型沿用 2026 中秋團圓套餐 EDM（黑金 clean 風）\n優惠期 11/11 至 11/17｜優惠碼 DOUBLE11｜滿 $1,100 11% OFF＋滿 $1,500/$2,200/$3,000 送小食\n============================================================\n-->\n'
            + head + '\n' + nav + greet + kv + coupon + intro + cta1 + offB + member2 + info + '\n' + tail.replace('{{crm.business_name}}', '{{crm.business_name}}<br><a href="##crm.unsubscribe_url##" style="color:#9A8F7E;text-decoration:underline;">取消訂閱</a>', 1) + '\n')
    open(os.path.join(H, 'email.html'), 'w', encoding='utf-8').write(html)
    return html

r = landing(); e = edm()
for n, s in [('landing', r), ('email', e)]:
    print(n, len(s), len(re.findall(r'<table\b', s)), s.count('</table>'), len(re.findall(r'<div\b', s)), s.count('</div>'))
