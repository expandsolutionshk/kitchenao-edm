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
.ao-tbl td.c{text-align:center;font-weight:800}.ao-tbl .y{color:#2C6E49}.ao-tbl .n{color:#C0392B}.ao-tbl .m{color:#9A7B2E}
.ao-tbl.ao-tbl-wrap{min-width:0!important}.ao-tbl-wrap th:first-child,.ao-tbl-wrap td:first-child{width:5em}
.ao-tag{display:inline-block;font-size:12px;font-weight:700;border-radius:20px;padding:1px 8px;margin:2px 4px 2px 0;background:#EEF6ED;color:#2C6E49;white-space:nowrap}
.ao-tag.w{background:#FFF4D6;color:#9A7B2E}.ao-tag.r{background:#FDE2E1;color:#B03A2E}
.ao-adv{background:#F4FBF3;border:1.5px solid #CFE8CD;border-radius:14px;padding:14px 18px 6px;margin:14px 0 20px}
.ao-adv .t{font-size:12px;font-weight:800;letter-spacing:2px;color:#2C6E49;margin:0 0 4px!important}
.ao-adv .r{display:flex;gap:12px;align-items:flex-start;padding:10px 0;border-top:1px dashed #CFE8CD}.ao-adv .t+.r{border-top:0}
.ao-adv .n{flex:0 0 34px;height:34px;border-radius:50%;background:#fff;border:1.5px solid #CFE8CD;display:flex;align-items:center;justify-content:center;font-size:18px}
.ao-adv b{display:block;color:#1F5A3A;font-size:16.5px;line-height:1.5}.ao-adv p{margin:2px 0 0!important;font-size:15.5px;line-height:1.7}
.ao-adv small{display:block;margin-top:3px;font-size:12.5px;color:#7a6a45;line-height:1.6}.ao-adv small a{color:#7a6a45!important;font-weight:600!important}
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

/* CTA green */
.ao-ctabox{position:relative;overflow:hidden;background:#EAF5E4 url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 360 220%22%3E %3Cg stroke=%22%231F5A3A%22 stroke-width=%223%22 stroke-linejoin=%22round%22 stroke-linecap=%22round%22%3E %3C%21-- leaf bg --%3E %3Cpath d=%22M300 20c40 10 55 50 40 85-35-5-60-40-40-85z%22 fill=%22%23BFE3B4%22/%3E%3Cpath d=%22M302 24c8 25 20 50 36 78%22 fill=%22none%22/%3E %3C%21-- carrot --%3E %3Cpath d=%22M196 150l70-58c10-8 24 6 16 16l-58 70c-8 9-37-19-28-28z%22 fill=%22%23F29A4A%22/%3E %3Cpath d=%22M240 120l12 10M222 140l12 10M206 158l10 9%22 fill=%22none%22/%3E %3Cpath d=%22M276 98c6-14 20-20 30-16-4 12-16 20-30 16zM280 104c14-2 26 6 28 16-12 2-24-4-28-16z%22 fill=%22%237CC36E%22/%3E %3C%21-- broccoli --%3E %3Cpath d=%22M110 200l6-56h22l6 56z%22 fill=%22%23B9DE9B%22/%3E %3Ccircle cx=%22104%22 cy=%22120%22 r=%2224%22 fill=%22%235DAE5A%22/%3E%3Ccircle cx=%22150%22 cy=%22118%22 r=%2224%22 fill=%22%235DAE5A%22/%3E%3Ccircle cx=%22127%22 cy=%2296%22 r=%2226%22 fill=%22%236CBF62%22/%3E%3Ccircle cx=%22127%22 cy=%22132%22 r=%2220%22 fill=%22%235DAE5A%22/%3E %3Ccircle cx=%22118%22 cy=%2292%22 r=%224%22 fill=%22%23fff%22 stroke=%22none%22 opacity=%22.7%22/%3E %3C%21-- tomato --%3E %3Ccircle cx=%22250%22 cy=%22182%22 r=%2230%22 fill=%22%23E8574A%22/%3E%3Cpath d=%22M250 152l6 10 12-2-8 9 6 10-12-4-8 8-2-12-11-4 11-5z%22 fill=%22%234E9E4B%22/%3E %3Cpath d=%22M236 172c4-6 9-8 13-8%22 fill=%22none%22 stroke=%22%23fff%22 stroke-width=%223%22 opacity=%22.8%22/%3E %3C%21-- mushroom --%3E %3Cpath d=%22M30 190c0-26 22-44 46-44s46 18 46 44z%22 fill=%22%23F3E3C9%22/%3E%3Cpath d=%22M58 190h36v22H58z%22 fill=%22%23FFF8EC%22/%3E %3Ccircle cx=%2260%22 cy=%22168%22 r=%226%22 fill=%22%23fff%22 stroke=%22none%22/%3E%3Ccircle cx=%2288%22 cy=%22160%22 r=%225%22 fill=%22%23fff%22 stroke=%22none%22/%3E %3C%21-- peas pod --%3E %3Cpath d=%22M150 210c20-26 60-30 84-22-18 22-58 32-84 22z%22 fill=%22%239BD07E%22/%3E%3Ccircle cx=%22178%22 cy=%22203%22 r=%226%22 fill=%22%236CBF62%22/%3E%3Ccircle cx=%22196%22 cy=%22199%22 r=%226%22 fill=%22%236CBF62%22/%3E%3Ccircle cx=%22214%22 cy=%22196%22 r=%225%22 fill=%22%236CBF62%22/%3E %3C/g%3E %3Cg fill=%22%23F7CE46%22 stroke=%22none%22%3E%3Ccircle cx=%2240%22 cy=%2240%22 r=%225%22/%3E%3Ccircle cx=%22210%22 cy=%2240%22 r=%224%22/%3E%3Ccircle cx=%22340%22 cy=%22150%22 r=%224%22/%3E%3C/g%3E %3C/svg%3E") no-repeat right -10px bottom -6px/320px auto!important;border:1.5px solid #CFE8CD;color:#24432F!important;padding:22px 24px!important}.ao-ctabox h3{color:#1F5A3A!important;max-width:62%}.ao-ctabox p{max-width:58%;color:#2F4A38}.ao-ctabox a.btn{background:#3F9D5A!important;color:#fff!important;border:3px solid #fff;box-shadow:0 4px 12px rgba(31,90,58,.25)}.ao-ctabox .ao-fri{background:#E8743B}@media(max-width:640px){.ao-ctabox{background-size:220px auto!important;padding-bottom:150px!important}.ao-ctabox h3,.ao-ctabox p{max-width:none}}
.ao-ctabox .cta-row{display:flex;flex-wrap:wrap;gap:14px;align-items:center;margin-top:6px;position:relative;z-index:1}.ao-ctabox a.cta-main{display:inline-flex;align-items:center;gap:10px;background:linear-gradient(180deg,#4BAF67,#3F9D5A);color:#fff!important;text-decoration:none!important;font-weight:800;font-size:16.5px;padding:11px 14px 11px 12px;border-radius:40px;border:3px solid #fff;box-shadow:0 5px 0 #2C6E49,0 10px 18px rgba(31,90,58,.25);transition:transform .15s,box-shadow .15s}.ao-ctabox a.cta-main .ic{display:inline-flex;align-items:center;justify-content:center;width:32px;height:32px;border-radius:50%;background:rgba(255,255,255,.2)}.ao-ctabox a.cta-main .ar{display:inline-flex;align-items:center;justify-content:center;width:26px;height:26px;border-radius:50%;background:#fff;color:#3F9D5A;font-size:15px;margin-left:2px;transition:transform .15s}.ao-ctabox a.cta-main:hover{transform:translateY(2px);box-shadow:0 3px 0 #2C6E49,0 6px 12px rgba(31,90,58,.25)}.ao-ctabox a.cta-main:hover .ar{transform:translateX(3px)}.ao-ctabox a.cta-wa{display:inline-flex;align-items:center;gap:10px;background:#fff;color:#1F5A3A!important;text-decoration:none!important;padding:8px 18px 8px 8px;border-radius:40px;border:2px solid #3F9D5A;box-shadow:0 4px 12px rgba(31,90,58,.12);transition:background .15s,transform .15s}.ao-ctabox a.cta-wa .ic{display:inline-flex;align-items:center;justify-content:center;width:34px;height:34px;border-radius:50%;background:#25D366;color:#fff}.ao-ctabox a.cta-wa b{display:block;font-size:15.5px;line-height:1.3;color:#1F5A3A}.ao-ctabox a.cta-wa small{display:block;font-size:12px;line-height:1.3;color:#5a7a63;font-weight:600}.ao-ctabox a.cta-wa:hover{background:#F4FBF3;transform:translateY(-1px)}@media(max-width:640px){.ao-ctabox .cta-row{flex-direction:column;align-items:stretch}.ao-ctabox a.cta-main,.ao-ctabox a.cta-wa{justify-content:center}}
/* end CTA */
.ao-tcap{margin:6px 0 18px;font-size:13px;color:#7a6a45;line-height:1.6}
/* mobile spacing */
.ao-article ul.ao-ck{list-style:none!important;padding-left:0!important}.ao-article ul.ao-ck li{padding-left:1.7em;text-indent:-1.7em;margin:8px 0}
.ao-article p{overflow-wrap:anywhere}
@media(max-width:640px){
.ao-article{font-size:16px!important;line-height:1.8!important;padding:0 2px}
.ao-article p{margin:0 0 14px!important}
.ao-h2{font-size:21px!important;margin:34px 0 12px!important;padding-top:12px!important}
.ao-h3{font-size:17.5px!important;margin:22px 0 8px!important}
.ao-article ul,.ao-article ol{padding-left:20px;margin:0 0 16px!important}.ao-article li{margin:6px 0!important}
.ao-qa,.ao-adv,.ao-tip,.ao-friline{padding:12px 14px!important;margin:12px 0 16px!important}
.ao-adv{padding-bottom:4px!important}.ao-adv .r{gap:10px}.ao-adv .n{flex-basis:30px;height:30px;font-size:16px}
.ao-intro{font-size:16px!important}
.ao-toc{padding:12px 14px!important}.ao-toc li{margin:4px 0!important}
.ao-tw{margin:12px 0 6px}.ao-tbl{font-size:14px}.ao-tbl th,.ao-tbl td{padding:9px 10px}
.ao-ctabox{padding:18px 16px 150px!important}
.ao-faqs summary{padding:11px 14px}.ao-faqs details>div{padding:0 14px 10px;font-size:15px}
.ao-src{padding:14px 14px!important;font-size:12px!important}.ao-src li{font-size:12px!important}.ao-src h2{font-size:15px!important}
}
/* end mobile */
/* desktop type */
@media(min-width:641px){
.ao-article{font-size:18px!important;line-height:1.85!important}
.ao-article p:not(.pl2):not(.kw):not(.t),.ao-article li,.ao-intro,.ao-toc a{font-size:18px!important;line-height:1.85!important}
.ao-h2{font-size:28px!important;line-height:1.35!important}
.ao-h3{font-size:21px!important;line-height:1.4!important}
.ao-adv .r p{font-size:17px!important;line-height:1.75!important}.ao-adv .r b{font-size:18px!important}.ao-adv small{font-size:13.5px!important}
.ao-tip,.ao-friline{font-size:17px!important;line-height:1.8!important}.ao-tip li{font-size:17px!important}
.ao-tbl{font-size:16px!important}.ao-tbl td{line-height:1.7!important}
.ao-faqs summary{font-size:18px!important}.ao-faqs details p{font-size:17px!important;line-height:1.8!important}
.ao-src{font-size:13px!important}.ao-src li{font-size:13px!important;line-height:1.7!important}.ao-src h2{font-size:15px!important}
.ao-ctabox p{font-size:17px!important}
}
/* end desktop */
</style>'''
B = 'https://aoaodelivery.com'
BLOGS = {
 'B1': ('派對有素食朋友點安排？素食到會揀選全攻略', B + '/blog/vegetarian-catering-hong-kong/'),
 'B2': ('素食分類天書：蛋奶素、五辛素、純素點分？', B + '/blog/vegetarian-types-guide/'),
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

def wp_page(pid, body, faqs, srcs, rel, kv_html=''):
    """WordPress 版：無 mockup bar、無 H1（文章標題即 H1）、關鍵字不高亮、CSS 壓成一行（避免 WordPress 在 <style> 內插入 <br />）"""
    import re as _re
    def one_line(block):
        def f(m):
            css = _re.sub(r'/\*.*?\*/', '', m.group(1), flags=_re.S)
            css = ' '.join(l.strip() for l in css.splitlines() if l.strip())
            css = _re.sub(r'\.no-hl[^{]*\{[^}]*\}', '', css)
            css = _re.sub(r'\.mk-bar[^{]*\{[^}]*\}', '', css)
            return '<style>' + css + '</style>'
        return _re.sub(r'<style>(.*?)</style>', f, block, flags=_re.S)
    body = body.replace('<div class="ao-ctabox"><h3>', '<div class="ao-ctabox"><span class="ao-fri">🎉 逢星期五落單「素」味人生自動 95 折</span><h3>')
    body = _re.sub(r'<mark class="kw">(.*?)</mark>', r'\1', body)
    rel_html = (('<h2 class="ao-h2">延伸閱讀</h2>' + rel_html(rel)) if rel else '') if False else ''
    out = (f'<div class="ao-article wp-exclude-emoji">\n{one_line(BOAT)}\n{one_line(EXTRA)}\n{kv_html}\n{body}\n'
           f'<h2 class="ao-h2" id="faq">常見問題</h2>\n{faq_html(faqs)}\n{sources_html(srcs)}\n</div>\n{faq_ld(faqs)}')
    return out
