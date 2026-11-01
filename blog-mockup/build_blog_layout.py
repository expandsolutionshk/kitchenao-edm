# -*- coding: utf-8 -*-
"""Blog 版面 mockup：同一個 template（blog-layout-template.html），換不同文章內容
v1＝B6 Vegan、Vegetarian 中文；v2＝B3 初一十五食齋懶人包"""
import os, re
H = os.path.dirname(os.path.abspath(__file__))
VB = os.path.join(H, '..', 'vegetarian-blog')
B = 'https://aoaodelivery.com'
REL = {
 'b2': ('/blog/vegetarian-types-guide/', B + '/wp-content/uploads/2026/10/veg-b2-thumb-1000x563-1-300x169.webp', '素食分類天書｜蛋奶素、五辛素、純素、蔬食有甚麼分別？'),
 'b1': ('/blog/vegetarian-catering-hong-kong/', B + '/wp-content/uploads/2026/10/veg-b1-vegetarian-catering-2026-kv-300x169.webp', '派對有素食朋友點安排？素食到會揀選全攻略'),
 'b6': ('/blog/vegan-vegetarian-meaning/', '', 'Vegan、Vegetarian 中文是甚麼？港台歐美素食用詞'),
 'b3': ('/blog/chu-yat-sap-ng-vegetarian-guide/', '', '初一十五食齋懶人包｜原因、禁忌及日子表'),
}
def rel(keys):
    return ''.join(f'\n    <a class="ao-rc" href="{B}{u}" target="_blank">' + (f'<img src="{i}" alt="" loading="lazy">' if i else '<img src="" alt="">') + f'<b>{t}</b></a>' for u, i, t in (REL[k] for k in keys)) + '\n   '
def tags(ts): return ''.join(f'<a href="#">{x}</a>' for x in ts)
PAGES = [
 dict(out='blog-layout-v1.html', VER='v1', src='b6-vegan-vegetarian-meaning-WORDPRESS.html', SHORT='Vegan、Vegetarian 中文是甚麼？',
      H1='Vegan、Vegetarian 中文是甚麼？Flexitarian、Pescatarian 有何分別？港台歐美素食用詞一次看清', UPDATED='2026-10-24', READ='8',
      TAGS=tags(['素食知識', '素食英文', '素食到會']), RELATED=rel(['b2', 'b1', 'b3']),
      CTA_T='派對有朋友吃素？', CTA_P='告訴我們人數及飲食要求，客服為你配搭素食到會餐單。'),
 dict(out='blog-layout-v2.html', VER='v2', src='b3-chu-yat-sap-ng-guide-WORDPRESS.html', SHORT='初一十五食齋懶人包',
      H1='初一十五食齋懶人包｜食齋原因、禁忌及未來 12 個月日子表', UPDATED='2026-11-01', READ='7',
      TAGS=tags(['初一十五', '素食知識', '素食到會']), RELATED=rel(['b2', 'b1', 'b6']),
      CTA_T='初一十五想請齋？', CTA_P='告訴我們日子、人數及飲食要求（例如走五辛），客服為你配搭素食到會。'),
]
T = open(os.path.join(H, 'blog-layout-template.html'), encoding='utf-8').read()
for p in PAGES:
    s = T.replace('{{ARTICLE}}', open(os.path.join(VB, p['src']), encoding='utf-8').read().strip())
    for k, v in p.items():
        if k.isupper(): s = s.replace('{{' + k + '}}', v)
    assert '{{' not in s, re.findall(r'\{\{\w+\}\}', s)
    open(os.path.join(H, p['out']), 'w', encoding='utf-8').write(s)
    print(p['out'], len(s), s.count('<h1'), len(re.findall(r'<div\b', s)), s.count('</div>'), len(re.findall(r'<h2[^>]*id=', s)))
