# -*- coding: utf-8 -*-
# 激光打印食物 blog 改版｜/blog/laser-printed-food-party/
# 沿用「香港到會避伏指南 2026」最新 blog 樣式：編輯風格 KV＋.ao-pf 內文元件＋.ao-bl 版面（右側欄、分享、有用投票）
import json, re, html, pathlib, runpy, urllib.parse
HERE = pathlib.Path(__file__).parent
ROOT = HERE.parent
PF = ROOT / 'pitfalls-blog'
U = 'https://aoaodelivery.com'
UP = U + '/wp-content/uploads'

# ---------- 共用樣式 ----------
_src = (PF / 'build.py').read_text(encoding='utf-8')
CSS = re.search(r"^CSS = r'''(.*?)'''", _src, re.S | re.M).group(1)
KVNS = runpy.run_path(str(PF / 'build_kv_ed.py'))           # 取 KV CSS、LOGO
KV_CSS, LOGO = KVNS['CSS'], KVNS['LOGO']
_tpl = (ROOT / 'vegetarian-blog' / 'b3-chu-yat-sap-ng-guide-WORDPRESS-layout.html').read_text(encoding='utf-8')
TPL_CSS = _tpl[:_tpl.index('<div class="ao-bl"')]
TPL_JS = _tpl[_tpl.index('</aside>') + 8:].split('</div>', 1)[1]

EXTRA = r'''
/* 馬卡龍相片放左、場合及企業活動放右 */
.ao-pf .si{display:grid;grid-template-columns:34% 1fr;gap:32px;align-items:start;margin:46px 0 0}
.ao-pf .sif{position:sticky;top:24px;margin:0}
.ao-pf .sif img{width:100%;height:auto}
.ao-pf .sic>h2:first-child{margin-top:0}
.ao-pf .sic .occ{grid-template-columns:1fr 1fr}
@media(max-width:767px){.ao-pf .si{display:flex;flex-direction:column;gap:0;margin-top:36px}.ao-pf .sic{display:contents}.ao-pf .sif{position:static;order:5;width:72%;max-width:300px;margin:6px auto 4px}.ao-pf .sic>*{order:1}.ao-pf .sic .occ{grid-template-columns:1fr}}
/* 激光打印 blog 專用 */
.ao-pf .prd{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;margin:18px 0}
.ao-pf .prd a{display:block;background:var(--iv);border-radius:6px;overflow:hidden;text-decoration:none;color:#141414}
.ao-pf .prd img{width:100%;aspect-ratio:1/1;object-fit:cover;border-radius:0}
.ao-pf .prd div{padding:14px 16px 16px}
.ao-pf .prd small{display:block;font-size:11.5px;letter-spacing:.22em;color:#9A7B2E;font-weight:800}
.ao-pf .prd b{display:block;font-size:18px;margin:4px 0 4px}
.ao-pf .prd span{display:block;font-size:15px;color:#4a443d;line-height:1.6}
.ao-pf .prd em{display:inline-block;margin-top:10px;font-style:normal;font-size:14px;font-weight:800;border-bottom:1.5px solid #C8A24A}
.ao-pf .gal{display:grid;grid-template-columns:1.25fr 1fr;gap:12px;margin:18px 0;aspect-ratio:16/10}
.ao-pf .gal>figure,.ao-pf .gal .r figure{height:100%;min-height:0;overflow:hidden}
.ao-pf .gal figure{margin:0}
.ao-pf .gal img{width:100%;height:100%;object-fit:cover;border-radius:6px}
.ao-pf .gal .r{display:grid;grid-template-rows:1fr 1fr;gap:12px}
.ao-pf .occ{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;margin:16px 0}
.ao-pf .occ div{border-top:2px solid #141414;padding:14px 2px 0}
.ao-pf .occ small{display:block;font-size:11.5px;letter-spacing:.22em;color:#9A7B2E;font-weight:800}
.ao-pf .occ b{display:block;font-size:17px;color:#141414;margin:4px 0 6px}
.ao-pf .occ p{font-size:15.5px;margin:0;color:#4a443d;line-height:1.75}
.ao-pf .stp{list-style:none;margin:16px 0;padding:0;counter-reset:s}
.ao-pf .stp li{counter-increment:s;position:relative;padding:4px 0 18px 64px;margin:0}
.ao-pf .stp li:before{content:"0" counter(s);position:absolute;left:0;top:0;width:46px;height:46px;border-radius:50%;background:#141414;color:#E4C77E;font-weight:900;font-size:16px;display:flex;align-items:center;justify-content:center}
.ao-pf .stp li:not(:last-child):after{content:"";position:absolute;left:22px;top:52px;bottom:4px;width:2px;background:var(--ln)}
.ao-pf .stp b{display:block;font-size:17px;color:#141414}
.ao-pf .stp span{display:block;font-size:15.5px;color:#4a443d;line-height:1.75}
.ao-pf figure.one img{width:100%}
@media(max-width:767px){
 .ao-pf .prd{grid-template-columns:1fr 1fr;gap:10px}
 .ao-pf .prd div{padding:10px 12px 12px}
 .ao-pf .prd b{font-size:15.5px}.ao-pf .prd span{font-size:13.5px}
 .ao-pf .gal{grid-template-columns:1fr;aspect-ratio:auto}
 .ao-pf .gal>figure{aspect-ratio:4/3}
 .ao-pf .gal .r{grid-template-rows:none;grid-template-columns:1fr 1fr}
 .ao-pf .gal .r figure{aspect-ratio:1/1}
 .ao-pf .occ{grid-template-columns:1fr}
 .ao-pf .tw.pr td:not(:first-child){display:block;font-size:15.5px}
 .ao-pf .tw.pr td:not(:first-child):before{display:none}
}
'''

# ---------- 原有「雷射包人氣數據＋客人實況分享」區塊（保留不改） ----------
_lc = pathlib.Path('/sessions/great-festive-darwin/mnt/Desktop/cowork - aoao/blog/laser-blog-content.html').read_text(encoding='utf-8')
PROOF = _lc[_lc.index('<div class="ao-proof">'):_lc.index('</div><!-- /ao-proof-right -->') + len('</div><!-- /ao-proof-right -->')] + '\n</div>'
_ls = pathlib.Path('/sessions/great-festive-darwin/mnt/Desktop/cowork - aoao/blog/laser-blog-styles.css').read_text(encoding='utf-8').split('\n')
PROOF_CSS = '\n'.join(l for l in _ls[57:75])

# ---------- KV（編輯風格 A） ----------
KV_PHOTO = UP + '/2025/04/IMG_4266-e1788770926121.jpg'
KV_TXT = ['PARTY FOOD GUIDE · 2026', '香港到會新玩法', '激光', '打印食物', '2', '款熱賣刻字食物',
          '雷射包｜馬卡龍｜Logo｜祝福語', '最少 3 日前預訂', '2026 年版']
_chars = ''.join(sorted(set(''.join(KV_TXT) + '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.·｜ ')))
FONT = ('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@500;900&family=Playfair+Display:ital,wght@1,700;1,900&display=swap&text='
        + urllib.parse.quote(_chars) + '">')
KV = (FONT + '<style>' + KV_CSS + '</style>'
      '<div class="ao-ekv a"><div class="f"><div class="pp">'
      '<div class="mh"><span>PARTY FOOD GUIDE · 2026</span>' + LOGO + '</div>'
      '<div class="k">香港到會新玩法</div><div class="h">激光<br>打印食物</div>'
      '<div class="n"><b>2</b><span>款熱賣刻字食物</span></div><div class="tg">雷射包｜馬卡龍｜Logo｜祝福語</div>'
      '<div class="ft"><span>最少 3 日前預訂</span><span>2026 年版</span></div></div>'
      '<div class="ph"><picture><img class="bg" src="' + KV_PHOTO + '" alt="激光打印食物：雷射包刻上 Happy Birthday" width="1000" height="1153" fetchpriority="high" decoding="async"></picture></div>'
      '</div></div>')
KV = KV.replace('.ao-ekv.a .h{margin:.8cqw 0 0;font-family:"Noto Serif TC","Songti TC","PMingLiU",serif;font-weight:900;font-size:9cqw;',
                '.ao-ekv.a .h{margin:.8cqw 0 0;font-family:"Noto Serif TC","Songti TC","PMingLiU",serif;font-weight:900;font-size:7.6cqw;')

# ---------- 內容 ----------
P_BURGER = U + '/product/a0700-handmade-mini-cheeseburger/'
P_MAC = U + '/product/d01-french-colorful-macarons-10-pieces/'
WA = 'https://wa.me/85269011987?text=' + urllib.parse.quote('你好，我想查詢激光打印食物（雷射包／馬卡龍刻字）的方案及報價。')

PRICE = [
 ('產品及價錢', f'<a href="{P_BURGER}">迷你芝士手打漢堡</a>：<b>$228／8 個</b>、<b>$408／15 個</b><br><a href="{P_MAC}">法式七彩馬卡龍</a>：<b>$198／10 個</b>'),
 ('最低訂購', '迷你芝士手打漢堡 8 個起、法式七彩馬卡龍 10 個起，即可預訂一組字'),
 ('打印費', '每個 <b>$10 至 $15</b>，視乎圖案或文字的複雜程度；簡單文字或單色線條 Logo 收費較低'),
 ('字數建議', '20 個英文字母以內'),
 ('落單方法', '最少 <b>3 日前</b>將字句或圖案 WhatsApp 給客服，確認打印詳情後付款預訂'),
]
OCC = [
 ('BIRTHDAY', '生日派對', '把壽星名字或 Happy Birthday 刻在雷射包上，切餅前已成為全場打卡焦點。'),
 ('CORPORATE', '公司活動及品牌推廣', '週年慶、發佈會或開幕酒會，把公司 Logo 刻在馬卡龍上，加深賓客對品牌的印象。'),
 ('WEDDING', '婚禮及回禮', '新人名字縮寫或日期刻在小食上，可作婚宴小食，亦可作賓客回禮。'),
 ('FESTIVE', '節日慶祝及紀念日', '聖誕、新年或紀念日，配合節日字句，令派對食物更有心思。'),
]
STEPS = [
 ('準備設計稿', '提供線條清晰、對比度高的單色圖案或文字，例如公司 Logo 向量圖（AI／EPS）或純黑色文字；漸變色或細節過多的圖像未必能完美呈現。'),
 ('WhatsApp 確認效果及報價', '客服會按設計複雜程度報價，並在生產前與你確認最終設計稿。'),
 ('付款預訂，按時送到', '最少 3 日前完成付款預訂；數量多於 30 個、設計較複雜或企業活動，建議提早 7 至 14 日預訂。'),
]
FAQ = [
 ('激光打印食物安全嗎？會改變食物味道嗎？',
  '激光打印過程安全，不使用油墨，亦不會添加任何物質，激光能量只作用於食物表層。過程或會令表面出現極輕微的焦糖化效果，類似烤麵包邊緣，對整體味道影響輕微。'),
 ('目前可以在哪些食物上激光打印？',
  '目前主要提供迷你芝士手打漢堡（雷射包）的包面，以及法式七彩馬卡龍的光滑餅面刻字服務。如想在其他食物上打印，歡迎查詢技術上是否可行。'),
 ('激光打印食物適合甚麼場合？',
  '適合生日派對、公司週年慶、發佈會、品牌推廣、婚禮、紀念日及節日聚會，亦可作散水餅或婚禮回禮小食。'),
 ('設計稿有甚麼要求？',
  '建議提供線條清晰、對比度高的單色圖案或文字，例如 Logo 向量圖（AI／EPS）或純黑色文字；英文字句建議 20 個字母以內。客服會在生產前與你確認設計稿。'),
 ('需要提前多久預訂？打印費多少？',
  '最少 3 日前預訂；數量多於 30 個、設計較複雜或節日旺季，請盡早預訂。打印費每個 $10 至 $15，視乎設計複雜程度而定。'),
]
REL = [
 ('生日派對', '小朋友生日會到會挑選指南', U + '/blog/kids-birthday-party-catering/'),
 ('公司活動', '香港公司活動到會攻略 2026', U + '/blog/company-event-catering-guide/'),
 ('避伏指南', '香港到會避伏指南 2026', U + '/blog/catering-pitfalls-guide/'),
]
TOC = [('what', '激光打印食物是甚麼？'), ('products', '兩款熱賣刻字食物'), ('price', '價錢、打印費及落單方法'),
       ('occasions', '適合甚麼場合？'), ('corporate', '企業活動：馬卡龍印公司 Logo'), ('steps', '設計稿要求及預訂 3 步'),
       ('faq', '激光打印食物常見問題'), ('conclusion', '編輯總結')]

def build():
    h = ['<div class="ao-pf">', '<style>' + CSS + EXTRA + PROOF_CSS + '</style>', KV]
    h.append('<p>食物真的可以刻字嗎？可以。透過<strong>食物激光雕刻</strong>技術，可以在漢堡包或馬卡龍表面準確刻上公司 Logo、名字或祝福語。一份普通的<strong>香港到會</strong>食物，刻上字句後即成為全場爭相拍照的主角。以下逐一拆解<strong>激光打印食物</strong>的做法、價錢及預訂注意事項。</p>')
    h.append('<div class="key"><div><i>01</i><b>刻上專屬字句</b><span>Logo、名字、祝福語皆可</span></div>'
             '<div><i>02</i><b>兩款熱賣食物</b><span>雷射包及馬卡龍刻字</span></div>'
             '<div><i>03</i><b>最少 3 日前預訂</b><span>WhatsApp 傳送設計稿即報價</span></div></div>')
    h.append('<nav class="toc ao-toc" aria-label="文章目錄"><span class="eb">Contents</span><ol>' + ''.join(f'<li><a href="#{a}">{t}</a></li>' for a, t in TOC) + '</ol></nav>')

    h.append('<h2 id="what">激光打印食物是甚麼？安心食用的食物激光雕刻</h2>')
    h.append('<p>激光打印食物，又稱<strong>食物激光雕刻</strong>，並非使用油墨，而是利用高度集中的光束能量，在食物表面準確刻上指定圖案或文字，過程就像為食物進行微型「烙印」。所用設備符合相關安全標準，不會改變到會食物原本的味道，可以安心食用。</p>')
    h.append('<p>Kitchen AO 已把這項技術應用於兩款熱賣的 <strong>Party Food</strong>：以手打豬肉及牛肉製成的迷你芝士手打漢堡（俗稱<strong>雷射包</strong>），以及法式七彩馬卡龍。曾有婚宴客人在漢堡包面刻上新人名字縮寫及一句與活動有關的金句，賓客拿起漢堡時看到字句，即時會心微笑。</p>')
    h.append('<div class="gal"><figure><img src="' + UP + '/2025/04/IMG_4266-e1788770926121.jpg" alt="激光打印漢堡：雷射包刻上 Happy Birthday" loading="lazy" decoding="async"></figure>'
             '<div class="r"><figure><img src="' + UP + '/2025/05/DSC01522-768x577.jpeg" alt="激光打印馬卡龍：企業活動 Logo 甜點" loading="lazy" decoding="async"></figure>'
             '<figure><img src="' + UP + '/2025/04/123-768x1024.jpg" alt="激光打印食物：訂製派對打卡食物" loading="lazy" decoding="async"></figure></div></div>')

    h.append('<h2 id="products">兩款熱賣刻字食物：雷射包及馬卡龍刻字</h2>')
    h.append('<div class="prd">'
             f'<a href="{P_BURGER}"><img src="{UP}/2019/06/Posts-07-768x768.jpg" alt="迷你芝士手打漢堡：激光刻字到會派對食物" loading="lazy"><div><small>雷射包</small><b>迷你芝士手打漢堡</b><span>手打豬肉及牛肉｜$228／8 個起</span><em>查看產品</em></div></a>'
             f'<a href="{P_MAC}"><img src="{UP}/2026/09/%E6%B3%95%E5%BC%8F%E4%B8%83%E5%BD%A9%E9%A6%AC%E5%8D%A1%E9%BE%8D-768x768.png" alt="法式七彩馬卡龍：激光刻字派對甜品" loading="lazy"><div><small>馬卡龍刻字</small><b>法式七彩馬卡龍</b><span>光滑餅面最適合印 Logo｜$198／10 個</span><em>查看產品</em></div></a>'
             '</div>')
    h.append('<p>想吃得豐富一點？可選購 <a href="' + U + '/product-category/party/foot-party/">美食派對套餐</a>，前菜、沙律、主食齊全，再加配激光刻字的迷你芝士手打漢堡及法式七彩馬卡龍。</p>')

    h.append('<h2 id="price">雷射包及馬卡龍刻字：價錢、打印費及落單方法</h2>')
    h.append('<div class="tw pr"><table><thead><tr><th>項目</th><th>詳情</th></tr></thead><tbody>'
             + ''.join(f'<tr><td>{a}</td><td><span>{b}</span></td></tr>' for a, b in PRICE) + '</tbody></table></div>')
    h.append('<p class="cap">打印費按圖案或文字複雜程度而定，落單前把設計稿 WhatsApp 給客服即可報實價。</p>')

    h.append('<div class="si"><figure class="sif"><img src="' + UP + '/2025/04/IMG_4265-768x939.jpg" alt="激光打印馬卡龍：企業活動訂製 Logo 甜點" width="768" height="939" loading="lazy" decoding="async"><figcaption>激光打印馬卡龍：光滑表面最適合印 Logo</figcaption></figure><div class="sic">')
    h.append('<h2 id="occasions">激光打印食物適合甚麼場合？</h2>')
    h.append('<div class="occ">' + ''.join(f'<div><small>{a}</small><b>{b}</b><p>{c}</p></div>' for a, b, c in OCC) + '</div>')
    h.append('<h2 id="corporate">企業活動到會：馬卡龍印公司 Logo，突顯品牌形象</h2>')
    h.append('<p>作為<strong>企業活動到會</strong>的主角，馬卡龍的光滑表面最適合印上公司 Logo，亦可為不同賓客印上名字作紀念品，令法式小甜品升級為企業活動專屬美食。只要提早預訂並提供線條清晰的設計稿，Kitchen AO 會提供具體的激光雕刻指引。</p>')
    h.append('</div></div>')
    h.append('<figure><img src="' + UP + '/2024/09/KirchenAO-Partnership_%E9%A0%81%E9%9D%A2_5-1024x465.jpg" alt="Kitchen AO 合作夥伴及服務機構：企業、醫療、教育及公共機構" loading="lazy" decoding="async"><figcaption>Kitchen AO 曾合作或服務過的部分企業、醫療、教育及公共機構</figcaption></figure>')
    h.append('<p>想了解公司活動的整體餐飲安排，可參考 <a href="' + U + '/corporate-catering-hk/">香港公司到會簡介</a>。</p>')

    h.append('<h2 id="steps">設計稿要求及預訂 3 步</h2>')
    h.append('<ol class="stp">' + ''.join(f'<li><b>{a}</b><span>{b}</span></li>' for a, b in STEPS) + '</ol>')

    h.append(PROOF)

    h.append('<h2 id="related">延伸閱讀</h2><div class="rel">' + ''.join(f'<a href="{u}"><small>{c}</small>{t}</a>' for c, t, u in REL) + '</div>')
    h.append('<h2 id="faq">激光打印食物常見問題（FAQ）</h2><div class="faq">'
             + ''.join(f'<details><summary>{q}</summary><div><p>{a}</p></div></details>' for q, a in FAQ) + '</div>')
    h.append('<h2 id="conclusion">編輯總結</h2><div class="sum"><p>激光打印食物不只是裝飾，更承載搞手為賓客準備的心意。無論是生日派對的祝福、公司活動的 Logo，還是婚禮的新人名字，一個刻上字句的雷射包或馬卡龍，已足以成為派對亮點。</p>'
             '<p>最少 3 日前把設計稿 <a href="' + WA + '" target="_blank" rel="noopener">WhatsApp 給客服</a>，即可確認效果及報價。</p></div>')
    sch = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}
    h.append('<script type="application/ld+json">' + json.dumps(sch, ensure_ascii=False) + '</script>')
    h.append('</div>')
    return '\n'.join(h)

SIDE_CSS = """<style>@media(max-width:1024px){.ao-bl-aside .ao-meta,.ao-bl-aside .ao-bshare{display:none!important}.ao-bl-aside{gap:14px}}
@media(max-width:767px){.ao-bl .ao-fb{gap:10px 8px;padding:16px}.ao-bl .ao-fb .aoshare{margin-bottom:4px}.ao-bl .ao-fb-q{flex:1 1 100%}.ao-bl .ao-fb .ao-fb-b{flex:1 1 0;text-align:center}.ao-bl .ao-fb-msg{flex:1 1 100%}}
.ao-bl .ao-fee{background:#141414;border-color:#141414;color:#EDE6D8}.ao-bl .ao-fee h4{color:#C8A24A!important}
.ao-bl .ao-fee p{margin:0;padding:7px 0;border-top:1px solid #2c2a26;display:flex;justify-content:space-between;gap:10px;font-size:13.5px}.ao-bl .ao-fee h4+p{border-top:0}
.ao-bl .ao-fee p b{color:#E4C77E;font-size:15px}</style>"""
FB = re.search(r"^FB = \((.*?)\)\n", _src, re.S | re.M).group(1)
FB = eval('(' + FB + ')')
TAGS = ('<div class="ao-sec"><h3>相關主題</h3><div class="ao-tags">'
        f'<a href="{U}/blog/kids-birthday-party-catering/">生日派對</a><a href="{U}/blog/company-event-catering-guide/">公司活動</a>'
        f'<a href="{U}/%e5%ae%a2%e8%a3%bd%e5%8c%96%e7%b4%80%e5%bf%b5%e5%93%81%e8%a8%82%e8%a3%bd%e6%9c%8d%e5%8b%99/">訂製紀念品</a><a href="{U}/product-category/party/foot-party/">美食派對套餐</a></div></div>')
ASIDE = ('<aside class="ao-bl-aside">'
         '<div class="ao-meta"><span>作者</span><b>Kitchen AO 編輯部</b><span>更新</span><b>2026-11-18</b><span>閱讀</span><b>約 6 分鐘</b></div>'
         '<div class="ao-sc toc"><h4>目錄</h4><div class="ao-prog"><i id="prog"></i></div><ol class="ao-toc2" id="toc"></ol></div>'
         '<div class="ao-bshare" aria-label="分享文章"><b>分享</b><a href="#" id="cpl" class="cp" title="複製連結"><i class="fas fa-link"></i><em>複製</em></a>'
         '<a href="#" id="shwa" class="wa" target="_blank" rel="noopener" title="分享到 WhatsApp"><i class="fab fa-whatsapp"></i><em>WhatsApp</em></a>'
         '<a href="#" id="shfb" class="fb" target="_blank" rel="noopener" title="分享到 Facebook"><i class="fab fa-facebook-f"></i><em>Facebook</em></a>'
         '<a href="#" id="shig" class="ig" title="分享到 Instagram"><i class="fab fa-instagram"></i><em>IG</em></a></div>'
         '<div class="ao-sc"><h4>🍔 推介產品</h4><div class="ao-pl">'
         f'<a class="ao-pi" href="{P_BURGER}" target="_blank"><img src="{UP}/2019/06/Posts-07-768x768.jpg" alt="" loading="lazy"><div><b>迷你芝士手打漢堡（雷射包）</b><span>$228／8 個起</span></div></a>'
         f'<a class="ao-pi" href="{P_MAC}" target="_blank"><img src="{UP}/2026/09/%E6%B3%95%E5%BC%8F%E4%B8%83%E5%BD%A9%E9%A6%AC%E5%8D%A1%E9%BE%8D-768x768.png" alt="" loading="lazy"><div><b>法式七彩馬卡龍</b><span>$198／10 個</span></div></a>'
         '</div></div>'
         '<div class="ao-sc ao-fee"><h4>刻字收費一覽</h4><p><b>$10–$15</b>每個打印費</p><p><b>8／10 個</b>漢堡／馬卡龍起訂</p><p><b>3 日</b>最少預訂時間</p></div>'
         '<div class="ao-cta2"><b>想刻 Logo 或祝福語？</b><p>把字句或圖案 WhatsApp 給客服，確認效果及報價。</p><a href="' + WA + '" target="_blank">WhatsApp 查詢</a></div>'
         '</aside>')

def wrap(article):
    return (TPL_CSS + SIDE_CSS + '<div class="ao-bl"><main class="ao-bl-main" id="art">' + article +
            '<div class="ao-end">' + FB + TAGS + '</div></main>' + ASIDE + '</div>' + TPL_JS)

art = wrap(build())
(HERE / 'laser-blog-WORDPRESS.html').write_text(art, encoding='utf-8')
TITLE = '激光打印食物｜雷射包、馬卡龍刻字價錢及預訂攻略｜香港到會派對新玩法'
prev = ('<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex">'
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css"><title>預覽｜' + TITLE + '</title>'
        '<style>body{margin:0;background:#fff;font-family:-apple-system,"PingFang HK","Microsoft JhengHei",sans-serif}.wrap{max-width:1240px;margin:0 auto;padding:28px 20px 60px}'
        '.t{font-size:30px;line-height:1.35;font-weight:900;margin:8px 0 16px;color:#141414}@media(max-width:767px){.t{font-size:23px}}</style></head><body><div class="wrap">'
        '<div class="t">' + TITLE + '</div>' + art + '</div></body></html>')
(HERE / 'laser-blog-preview.html').write_text(prev, encoding='utf-8')

F = [('文章標題（WP 標題／H1）', TITLE),
     ('Rank Math SEO Title', '激光打印食物｜雷射包・馬卡龍刻字價錢及預訂｜Kitchen AO'),
     ('Meta Description', '香港到會新玩法：激光打印食物把公司 Logo、名字、祝福語刻上雷射包及馬卡龍。漢堡 $228／8 個起、打印費每個 $10–$15，最少 3 日前預訂，WhatsApp 即時報價。'),
     ('Focus Keyword', '激光打印食物, 雷射包, 馬卡龍刻字, 食物激光雕刻, 香港到會')]
rows = ''.join(f'<div class="r"><b>{k}</b><span class="n">{len(v)} 字</span><button data-v="{html.escape(v)}">複製</button><input readonly value="{html.escape(v)}"></div>' for k, v in F)
pg = f'''<!doctype html><html lang="zh-HK"><meta charset="utf-8"><title>複製｜激光打印食物 blog</title>
<style>body{{font-family:-apple-system,"PingFang HK",sans-serif;max-width:1100px;margin:30px auto;padding:0 16px;color:#222}}h2{{font-size:18px}}.r{{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin:8px 0}}.r b{{min-width:200px;font-size:14px}}.r input{{flex:1 1 480px;padding:7px;border:1px solid #ccc;border-radius:6px}}.n{{font-size:12px;color:#888}}textarea{{width:100%;height:55vh;font:12px monospace}}button{{background:#141414;color:#C8A24A;border:1px solid #C8A24A;padding:7px 16px;cursor:pointer;border-radius:4px}}ol{{font-size:14px;line-height:1.8}}</style>
<h2>激光打印食物 blog｜更新步驟</h2>
<ol><li>WP → 文章 → 編輯「laser-printed-food-party」，<b>slug 不要改</b>。</li><li>標題改為下方「文章標題」。</li><li>刪除全部舊內容，用 WPBakery「Raw HTML」（或自訂 HTML 區塊）貼上下方代碼。</li><li>精選圖片保留原本雷射包相片即可。Rank Math 更新 Title、Description 及 Focus Keyword；如已有 FAQ schema 請刪除（代碼已包括）。</li></ol>
<h2>SEO 欄位</h2>{rows}
<h2>文章代碼</h2><button id="b">複製全部代碼</button>
<textarea id="t" readonly>{html.escape(art)}</textarea>
<script>document.querySelectorAll(".r button").forEach(x=>x.onclick=()=>navigator.clipboard.writeText(x.dataset.v).then(()=>{{x.textContent="已複製";setTimeout(()=>x.textContent="複製",1500)}}));b.onclick=()=>navigator.clipboard.writeText(t.value).then(()=>{{b.textContent="已複製";setTimeout(()=>b.textContent="複製全部代碼",1500)}})</script></html>'''
(HERE / '複製-激光打印食物blog.html').write_text(pg, encoding='utf-8')
print(len(art))
