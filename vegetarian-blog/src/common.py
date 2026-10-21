# -*- coding: utf-8 -*-
import json, re, html, pathlib
HERE = pathlib.Path(__file__).parent
BASE = HERE.read_text if False else None
BOAT = (HERE / 'boat.css').read_text(encoding='utf-8')
EXTRA = '''<style>
.ao-article mark.kw{background:#FFF176;color:inherit;padding:0 3px;border-radius:3px;}
.no-hl .ao-article mark.kw{background:none;padding:0;}
.mk-bar{position:sticky;top:0;z-index:50;max-width:900px;margin:0 auto 18px;background:#1A1A1A;color:#EDE6D6;border-radius:0 0 14px 14px;padding:10px 16px;font:13px/1.6 -apple-system,"PingFang HK",sans-serif;display:flex;flex-wrap:wrap;gap:8px 16px;align-items:center}
.mk-bar b{color:#F7CE46}.mk-bar a{color:#F7CE46}.mk-bar button{margin-left:auto;border:0;border-radius:20px;padding:4px 12px;background:#F7CE46;font:inherit;font-weight:700;cursor:pointer}
.ao-kv{border-radius:18px;padding:34px 28px;margin:0 0 22px;background:linear-gradient(135deg,#2C6E49 0%,#3F9D5A 55%,#C8A24A 140%);color:#fff;position:relative;overflow:hidden}
.ao-kv:after{content:"🥦🍄🥕";position:absolute;right:18px;bottom:10px;font-size:54px;opacity:.35}
.ao-kv .k{display:inline-block;background:#1A1A1A;color:#F7CE46;font-weight:800;font-size:13px;border-radius:30px;padding:4px 14px;margin:0 0 12px}
.ao-kv h1{margin:0 0 10px!important;font-size:30px!important;line-height:1.3!important;color:#fff!important;font-weight:900}
.ao-kv p{margin:0!important;font-size:15.5px;color:#F1F8EE;max-width:620px}
.ao-qa{background:#F4FBF3;border:1.5px solid #CFE8CD;border-radius:14px;padding:14px 18px;margin:14px 0 20px}
.ao-qa .t{font-size:12px;font-weight:800;letter-spacing:2px;color:#2C6E49;margin:0 0 6px}
.ao-qa p{margin:0!important}
.ao-tw{overflow-x:auto;margin:14px 0 6px;border-radius:12px;border:1px solid #EBE3D2}
.ao-tbl{border-collapse:collapse;width:100%;min-width:560px;font-size:15px;background:#fff}
.ao-tbl th{background:#1A1A1A;color:#F7CE46;font-weight:800;padding:10px 12px;text-align:left;white-space:nowrap}
.ao-tbl td{padding:10px 12px;border-top:1px solid #F0EADF;vertical-align:top;line-height:1.6}
.ao-tbl tr:nth-child(even) td{background:#FBF8F2}
.ao-tbl td.c{text-align:center;font-weight:800}.y{color:#2C6E49}.n{color:#C0392B}.m{color:#9A7B2E}
.ao-tag{display:inline-block;font-size:12px;font-weight:700;border-radius:20px;padding:1px 8px;margin:2px 4px 2px 0;background:#EEF6ED;color:#2C6E49;white-space:nowrap}
.ao-tag.w{background:#FFF4D6;color:#9A7B2E}.ao-tag.r{background:#FDE2E1;color:#B03A2E}
.ao-tip{background:#F4FBF3;border:1.5px solid #CFE8CD;border-radius:12px;padding:10px 14px;margin:16px 0;font-size:16px}
.ao-warn{background:#FFF8E6;border:1.5px solid #F2D58A;border-radius:12px;padding:12px 16px;margin:16px 0;font-size:15px}
.ao-faqs details{border:1px solid #EBE3D2;border-radius:12px;margin:0 0 10px;background:#fff}
.ao-faqs summary{cursor:pointer;padding:12px 16px;font-weight:800;color:#1A1A1A;list-style:none}
.ao-faqs summary::-webkit-details-marker{display:none}.ao-faqs summary:before{content:"Q　";color:#C8A24A}
.ao-faqs details>div{padding:0 16px 12px;font-size:16px}
.ao-ctabox{background:#1A1A1A;color:#EDE6D6;border-radius:16px;padding:20px 22px;margin:24px 0}
.ao-ctabox h3{color:#F7CE46!important;margin:0 0 8px!important;font-size:19px}
.ao-ctabox p{margin:0 0 12px!important}
.ao-ctabox a.btn{display:inline-block;background:#F7CE46;color:#1A1A1A!important;text-decoration:none!important;font-weight:800;border-radius:30px;padding:9px 18px;margin:4px 8px 0 0}
.ao-fri{display:inline-block;background:#E8743B;color:#fff;font-weight:800;font-size:13px;border-radius:20px;padding:3px 12px;margin:0 0 10px}
.ao-friline{background:#FFF1E6;border:1.5px solid #F5C6A5;border-radius:12px;padding:10px 14px;margin:12px 0;font-size:16px}
.ao-src{background:#FAF7F1;border-radius:14px;padding:16px 20px;margin:30px 0 10px;font-size:14px}
.ao-src h2{font-size:17px!important;margin:0 0 8px!important;padding:0!important}.ao-src h2:before{display:none}
.ao-src ol{margin:0;padding-left:20px}.ao-src li{margin:5px 0;line-height:1.6}.ao-src a{word-break:break-all;font-weight:500!important}
.ao-src .g{display:inline-block;font-size:11px;font-weight:800;border-radius:6px;padding:0 6px;margin-right:4px;background:#1A1A1A;color:#F7CE46}
.ao-rel{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:10px;margin:14px 0}
.ao-rel a{display:block;border:1px solid #EBE3D2;border-radius:12px;padding:12px 14px;text-decoration:none!important;background:#fff;font-size:15px}
.ao-rel a small{display:block;color:#7a6a45;font-weight:500;font-size:12.5px}
@media(max-width:640px){.ao-kv h1{font-size:24px!important}.ao-tbl{font-size:14px}}
</style>'''
B = 'https://aoaodelivery.com'
BLOGS = {
 'B1': ('派對有素食朋友點安排？素食到會揀選全攻略', B + '/blog/vegetarian-catering-hong-kong/'),
 'B2': ('素食種類全攻略｜蛋奶素、五辛素、純素、蔬食有甚麼分別？', B + '/blog/vegetarian-types-guide/'),
 'B3': ('初一十五食齋懶人包｜可以吃蛋嗎？食齋禁忌及 2026–2027 日子一覽', B + '/blog/chu-yat-sap-ng-vegetarian-guide/'),
 'B4': ('吃素好處與營養｜素食者怎樣補充蛋白質？Green Monday 一週一素入門', B + '/blog/vegetarian-nutrition-protein/'),
 'B5': ('一週素食菜單｜簡易素食食譜，不想煮可以點？', B + '/blog/weekly-vegetarian-menu/'),
 'B6': ('Vegan、Vegetarian 中文是甚麼？素食英文用語一覽', B + '/blog/vegan-vegetarian-meaning/'),
}
LP = B + '/catering/vegetarian/'
C1 = B + '/product-category/party/vegetarians-set/'
C2 = B + '/product-category/a-la-carte/vegetarian/'
def k(t): return f'<mark class="kw">{t}</mark>'
def link(pid, text=None):
    t, u = BLOGS[pid]; return f'<a href="{u}">{text or t}</a>'
def faq_html(faqs):
    return '<div class="ao-faqs">' + ''.join(f'<details><summary>{q}</summary><div><p>{a}</p></div></details>' for q, a in faqs) + '</div>'
def faq_ld(faqs):
    strip = lambda s: re.sub('<[^>]+>', '', s)
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": strip(q), "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in faqs]}, ensure_ascii=False) + '</script>'
def sources_html(srcs):
    return '<section class="ao-src"><h2>資料來源</h2><ol>' + ''.join(f'<li><span class="g">{g}</span>{n}：<a href="{u}" target="_blank" rel="noopener">{u}</a></li>' for g, n, u in srcs) + '</ol><p style="margin:8px 0 0!important;font-size:12.5px;color:#7a6a45">資料於 2026 年 10 月查閱。健康及營養資料只供一般參考，如有個別需要，請諮詢醫生或註冊營養師。</p></section>'
def rel_html(ids):
    return '<div class="ao-rel">' + ''.join(f'<a href="{BLOGS[i][1]}">{BLOGS[i][0].split("｜")[0]}<small>{BLOGS[i][0].split("｜")[1] if "｜" in BLOGS[i][0] else ""}</small></a>' for i in ids) + '</div>'
FRI_NOTE='逢星期五落單，「素」味人生套餐自動享 95 折（以網站結帳時顯示的價錢為準）'
def page(pid, meta_title, meta_desc, kwlist, kv_tag, kv_sub, body, faqs, srcs, rel, kv_html=None):
    title, url = BLOGS[pid]
    bar = f'<div class="mk-bar"><span><b>MOCKUP {pid}</b>　{html.escape(title)}</span><span>目標 URL：<a href="{url}" target="_blank">{url.replace(B, "")}</a></span><span>主攻：{"、".join(kwlist)}</span><button onclick="document.body.classList.toggle(\'no-hl\');this.textContent=document.body.classList.contains(\'no-hl\')?\'顯示關鍵字\':\'隱藏關鍵字\'">隱藏關鍵字</button></div>'
    body = body.replace('<div class="ao-ctabox"><h3>', '<div class="ao-ctabox"><span class="ao-fri">🎉 逢星期五落單「素」味人生自動 95 折</span><h3>')
    kv = kv_html or f'<div class="ao-kv"><span class="k">{kv_tag}</span><h1>{html.escape(title)}</h1><p>{kv_sub}</p></div>'
    doc = f'''<!DOCTYPE html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex">
<title>{html.escape(meta_title)}</title><meta name="description" content="{html.escape(meta_desc)}">
<!-- Meta Title（上線用）：{html.escape(meta_title)} -->
<!-- Meta Description（上線用）：{html.escape(meta_desc)} -->
<style>body{{margin:0;background:#FBF6EC;padding:0 16px 60px}}</style></head><body>
{bar}
<div class="ao-article">
{BOAT}
{EXTRA}
{kv}
{body}
<h2 class="ao-h2" id="faq">常見問題</h2>
{faq_html(faqs)}
{('<h2 class="ao-h2">延伸閱讀</h2>' + rel_html(rel)) if rel else ''}
{sources_html(srcs)}
</div>
{faq_ld(faqs)}
</body></html>'''
    return doc
SRC = {
 'chp': ('政府', '衞生署衞生防護中心〈均衡素食的要點〉', 'https://www.chp.gov.hk/tc/static/90050.html'),
 'chp_en': ('政府', 'Centre for Health Protection, Department of Health — Key Points of a Balanced Vegetarian Diet', 'https://www.chp.gov.hk/en/static/90050.html'),
 'shs': ('政府', '衞生署學生健康服務〈素食與營養〉（2023 年 6 月修訂）', 'https://www.studenthealth.gov.hk/tc_chi/health/health_dn/health_dn_vdn.html'),
 'fhs': ('政府', 'Family Health Service, Department of Health — Plan Wisely for Vegetarian Diet', 'https://www.fhs.gov.hk/english/health_info/woman/30123.html'),
 'chp_diet': ('政府', '衞生署衞生防護中心〈健康飲食原則概要〉', 'https://www.chp.gov.hk/tc/static/109964.html'),
 'hko26': ('政府', '香港天文台〈2026（丙午 - 肖馬）年公曆與農曆日期對照表〉', 'https://www.hko.gov.hk/tc/gts/time/calendar/text/files/T2026c.txt'),
 'hko27': ('政府', '香港天文台〈2027（丁未 - 肖羊）年公曆與農曆日期對照表〉', 'https://www.hko.gov.hk/tc/gts/time/calendar/text/files/T2027c.txt'),
 'hol27': ('政府', 'GovHK〈2027 年公眾假期〉', 'https://www.gov.hk/tc/about/abouthk/holiday/2027.htm'),
 'hku': ('大學', '香港大學傳譯課程〈中英雙語時事詞彙：flexitarian 彈性素食者〉', 'https://www.interpreting.hku.hk/glossary/?p=63771'),
 'zdic': ('辭典', '漢典〈五葷〉', 'https://www.zdic.net/hant/五葷'),
 'gm': ('機構', 'MICHELIN Guide〈Green Monday 創辦人楊大偉專訪〉', 'https://guide.michelin.com/mo/zh_HK/article/people/michelin-restaurants-david-yeung-green-monday-founder-plant-based-meals'),
 'wef': ('機構', 'World Economic Forum — David Yeung（Green Monday 創辦人）', 'https://weforum.org/people/david-yeung'),
 'ao_set': ('Kitchen AO', '「素」味人生素食到會套餐（產品分類及價目）', 'https://aoaodelivery.com/product-category/party/vegetarians-set/'),
 'ao_68': ('Kitchen AO', 'AO 6-8pax「素」味人生（菜式選擇及預訂須知）', 'https://aoaodelivery.com/product/ao-6-8pax-vegetarian-life/'),
 'ao_del': ('Kitchen AO', '送貨需知及免運費優惠', 'https://aoaodelivery.com/delivery/'),
}
