# -*- coding: utf-8 -*-
"""Blog 版面 mockup：同一個 template（blog-layout-template.html），換不同文章內容
v1＝B6 Vegan、Vegetarian 中文；v2＝B3 初一十五食齋懶人包"""
import os, re
H = os.path.dirname(os.path.abspath(__file__))
VB = os.path.join(H, '..', 'vegetarian-blog')
B = 'https://aoaodelivery.com'
REL = {
 'b2': ('/blog/vegetarian-types-guide/', B + '/wp-content/uploads/2026/10/veg-b2-thumb-1000x563-1-768x432.webp', '素食分類天書｜蛋奶素、五辛素、純素、蔬食有甚麼分別？'),
 'b1': ('/blog/vegetarian-catering-hong-kong/', B + '/wp-content/uploads/2026/10/veg-b1-vegetarian-catering-2026-kv-768x432.webp', '派對有素食朋友點安排？素食到會揀選全攻略'),
 'b6': ('/blog/vegan-vegetarian-meaning/', B + '/wp-content/uploads/2026/10/veg-b6-thumb-2000x1126-1-768x432.webp', 'Vegan、Vegetarian 中文是甚麼？港台歐美素食用詞'),
 'boat': ('/blog/boat-party-catering-guide/', B + '/wp-content/uploads/2026/09/boat-party-catering-2026-kv-768x432.jpg', '船P必備清單 2026｜遊船河準備、食物飲品份量懶人包'),
 'pic': ('/blog/hong-kong-picnic-spots-picnic-box/', B + '/wp-content/uploads/2026/10/hong-kong-picnic-spots-2026-kv-768x432.webp', '香港野餐好去處 2026｜33 個大草地、海景及寵物友善野餐地點'),
 'b3': ('/blog/chu-yat-sap-ng-vegetarian-guide/', B + '/wp-content/uploads/2026/11/veg-b3-kv-2000x1126-1-768x432.jpg', '初一十五食齋懶人包｜原因、禁忌及日子表'),
}
def rel(keys):
    return ''.join(f'\n    <a class="ao-rc" href="{B}{u}" target="_blank">' + (f'<img src="{i}" alt="" loading="lazy">' if i else '<img src="" alt="">') + f'<b>{t}</b></a>' for u, i, t in (REL[k] for k in keys) if i) + '\n   '

def _pi(n, pr, u, im): return f'\n   <a class="ao-pi" href="{B}{u}" target="_blank"><img src="{B}{im}" alt="" loading="lazy"><div><b>{n}</b><span>HK${pr:,}</span></div></a>'
def _pc(n, pr, u, im, btn): return f'\n    <a class="ao-pc" href="{B}{u}" target="_blank"><img src="{B}{im}" alt="{n}" loading="lazy"><div><b>{n}</b><span>HK${pr:,}</span><em>{btn}</em></div></a>'
VEGIMG = '/wp-content/uploads/2025/05/9ee996d5-e50c-4745-b847-86d8e179c481-600x600.jpg'
VEG = [('「素」味人生 6–8 人', 1388, '/product/ao-6-8pax-vegetarian-life/', VEGIMG), ('「素」味人生 10–12 人', 1988, '/product/ao-10-12pax-vegetarian-life/', VEGIMG),
       ('「素」味人生 16–19 人', 2988, '/product/ao-16-19pax-vegetarian-life/', VEGIMG), ('「素」味人生 22–26 人', 3788, '/product/ao-22-26pax-vegetarian-life/', VEGIMG)]
CHILLIMG = '/wp-content/uploads/2025/04/WhatsApp-Image-2025-04-12-at-4.08.18-PM-600x600.jpeg'
PICNIC = [('Chill 一下野餐盒（大）4–6 人', 628, '/product/chill一picnic-big-for-4-6-persons/', CHILLIMG), ('Chill 一下野餐盒（小）', 258, '/product/chill一picnic-small/', CHILLIMG),
          ('5 人自選拼盤', 498, '/product/5-people-self-selected-platter/', '/wp-content/uploads/2023/10/KitchenAO_platter_thumbnail_工作區域-1-600x600-1.png'),
          ('輕食宴會套餐 12–16 人', 2688, '/product/ao-12-16pax-refreshment-set/', '/wp-content/uploads/2023/11/refreshmentparty-03-600x600.jpg')]
def prods(lst, btn='查看套餐', icon='🥗', more_url='/product-category/party/vegetarians-set/', more_text='查看全部素食套餐'):
    return dict(SIDE_PRODUCTS=''.join(_pi(*x) for x in lst), GRID_PRODUCTS=''.join(_pc(*x, btn) for x in lst), PROD_ICON=icon, MORE_URL=B + more_url, MORE_TEXT=more_text)
def tags(ts): return ''.join(f'<a href="{B}{u}">{x}</a>' for x, u in ts)
PAGES = [
 dict(out='blog-layout-v1.html', VER='v1', src='b6-vegan-vegetarian-meaning-WORDPRESS.html', SHORT='Vegan、Vegetarian 中文是甚麼？',
      H1='Vegan、Vegetarian 中文是甚麼？Flexitarian、Pescatarian 有何分別？港台歐美素食用詞一次看清', UPDATED='2026-10-24', READ='8',
      TAGS=tags([('素食分類', '/blog/vegetarian-types-guide/'), ('素食到會', '/blog/vegetarian-catering-hong-kong/'), ('素食套餐', '/product-category/party/vegetarians-set/')]), RELATED=rel(['b2', 'b1', 'b3']),
      CTA_T='派對有朋友吃素？', CTA_P='告訴我們人數及飲食要求，客服為你配搭素食到會餐單。', **prods(VEG)),
 dict(out='blog-layout-v2.html', VER='v2', src='b3-chu-yat-sap-ng-guide-WORDPRESS.html', SHORT='初一十五食齋懶人包',
      H1='初一十五食齋懶人包｜食齋原因、禁忌及未來 12 個月日子表', UPDATED='2026-11-01', READ='7',
      TAGS=tags([('素食分類', '/blog/vegetarian-types-guide/'), ('素食英文', '/blog/vegan-vegetarian-meaning/'), ('素食到會', '/blog/vegetarian-catering-hong-kong/'), ('素食套餐', '/product-category/party/vegetarians-set/')]), RELATED=rel(['b2', 'b1', 'b6']),
      CTA_T='初一十五想請齋？', CTA_P='告訴我們日子、人數及飲食要求（例如走五辛），客服為你配搭素食到會。', **prods(VEG)),
 dict(out='blog-layout-b2.html', VER='B2', src='b2-vegetarian-types-guide-WORDPRESS.html', SHORT='素食分類天書',
      H1='素食分類天書｜聚會有朋友吃素？新手一表看懂素食分類｜蛋奶素、五辛素、純素、蔬食有甚麼分別？', UPDATED='2026-10-24', READ='9',
      TAGS=tags([('素食英文', '/blog/vegan-vegetarian-meaning/'), ('初一十五', '/blog/chu-yat-sap-ng-vegetarian-guide/'), ('素食到會', '/blog/vegetarian-catering-hong-kong/'), ('素食套餐', '/product-category/party/vegetarians-set/')]), RELATED=rel(['b6', 'b3', 'b1']),
      CTA_T='聚會有朋友吃素？', CTA_P='告訴我們人數及吃素方式（蛋奶素、全素或走五辛），客服為你配搭素食到會。', **prods(VEG)),
 dict(out='blog-layout-picnic.html', VER='野餐', src='../picnic-blog/blog-picnic-WORDPRESS.html', SHORT='香港野餐好去處 2026', strip_own_end=True,
      H1='香港野餐好去處2026｜33個大草地、海景及寵物友善野餐地點', UPDATED='2026-10-24', READ='12',
      TAGS=tags([('野餐盒', '/product-category/party/chill-box/'), ('船河到會', '/blog/boat-party-catering-guide/'), ('派對小食', '/product-category/a-la-carte/snacks/')]), RELATED=rel(['boat', 'b1', 'b2']),
      CTA_T='去野餐想輕鬆啲？', CTA_P='告訴我們日期、人數及野餐地點，客服為你安排野餐盒及送貨時間。', **prods(PICNIC, '查看', '🧺', '/product-category/party/chill-box/', '查看全部野餐盒')),
]
def strip_blocks(h, starts):
    for st in starts:
        i = h.find(st)
        if i < 0: continue
        d = 0
        for m in re.finditer(r'<div\b|</div>', h[i:]):
            d += 1 if m.group(0) == '<div' else -1
            if d == 0: h = h[:i] + h[i + m.end():]; break
    return h
T = open(os.path.join(H, 'blog-layout-template.html'), encoding='utf-8').read()
for p in PAGES:
    art = open(os.path.join(VB, p['src']), encoding='utf-8').read().strip()
    if p.get('strip_own_end'): art = strip_blocks(art, ['<div class="ao-fb"', '<div class="ao-tagsec">', '<div class="ao-related">'])
    s = T.replace('{{ARTICLE}}', art)
    for k, v in p.items():
        if k.isupper(): s = s.replace('{{' + k + '}}', v)
    assert '{{' not in s, re.findall(r'\{\{\w+\}\}', s)
    open(os.path.join(H, p['out']), 'w', encoding='utf-8').write(s)
    print(p['out'], len(s), s.count('<h1'), len(re.findall(r'<div\b', s)), s.count('</div>'), len(re.findall(r'<h2[^>]*id=', s)))

# ---------- WordPress 版（一個 Raw HTML 貼上即可，不需要 snippet）----------
SNIP = open(os.path.join(H, 'wp', 'ao-blog-layout-snippet.txt'), encoding='utf-8').read()
WPCSS = re.search(r'<style id="ao-bl-css">(.*?)</style>', SNIP, re.S).group(1).strip()
WPCSS = WPCSS.replace('body.ao-bl-on .lafka_post_data_holder{max-width:1240px!important}',
                      '.lafka_post_data_holder:has(.ao-bl){max-width:1240px!important}')
WPOUT = {'blog-layout-v1.html': 'b6-vegan-vegetarian-meaning-WORDPRESS-layout.html',
         'blog-layout-v2.html': 'b3-chu-yat-sap-ng-guide-WORDPRESS-layout.html',
         'blog-layout-b2.html': 'b2-vegetarian-types-guide-WORDPRESS-layout.html',
         'blog-layout-picnic.html': '../picnic-blog/blog-picnic-WORDPRESS-layout.html'}
VOTEJS = ("(function(){var V=document.querySelector('.ao-bl .ao-vote');if(!V)return;"
          "[].forEach.call(V.querySelectorAll('.b'),function(b){b.style.cursor='pointer';b.addEventListener('click',function(){"
          "[].forEach.call(V.querySelectorAll('.b'),function(x){x.classList.remove('on')});b.classList.add('on');"
          "var q=V.querySelector('.q');if(q)q.textContent='多謝你的意見！';})});"
          "var c=V.querySelector('.cp');if(c)c.addEventListener('click',function(){var u=location.href.split('#')[0];"
          "if(navigator.clipboard)navigator.clipboard.writeText(u);c.textContent='✓ 已複製';setTimeout(function(){c.textContent='🔗 複製文章連結'},1600)});})();")
for src, dst in WPOUT.items():
    s = open(os.path.join(H, src), encoding='utf-8').read()
    a = s.index('<div class="ao-bl">'); b = s.rindex('<script>')
    block = s[a:b].rstrip()
    js = re.findall(r'<script>(.*?)</script>', s, re.S)[-1]
    out = '<style>' + WPCSS + '</style>\n' + block + '\n<script>' + js + '\n' + VOTEJS + '</script>\n'
    assert '<h1' not in out
    open(os.path.join(VB, dst), 'w', encoding='utf-8').write(out)
    print('WP', dst, len(out), len(re.findall(r'<div\b', out)), out.count('</div>'))
