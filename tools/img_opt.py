# -*- coding: utf-8 -*-
"""把代碼內的 WordPress 原圖改用 WP 已自動產生的細尺寸（srcset），不用重新上載圖片。2026-11-21"""
import re
U = 'https://aoaodelivery.com/wp-content/uploads/2026/11/'
P45 = [(240, '-240x300'), (600, '-600x750'), (768, '-768x960'), (819, '-819x1024')]
SQ = [(300, '-300x300'), (600, '-600x600'), (768, '-768x768'), (1024, '-1024x1024')]
T = {}
for n in ['xmas-home-chestnut-pastry', 'xmas-home-kimchi-prawn-risotto', 'xmas-home-lobster-claypot-rice', 'xmas-home-pomegranate-salad',
          'xmas-home-crab-mango-salad', 'xmas-home-pistachio-tart', '2026-XMAS-IG-16', '2026-XMAS-IG-10']:
    T[n + '.jpg'] = (n, '.jpg', P45, 1080)
for n in ['xmas-lp-hero-open', 'xmas-lp-hero-box-v2']:
    T[n + '.jpg'] = (n, '.jpg', P45, 1200)
T['2026-XMAS-IG-11-scaled.jpg'] = ('2026-XMAS-IG-11', '.jpg', P45 + [(1229, '-1229x1536')], 2048)
T['26XMAS-banner-scaled.jpg'] = ('26XMAS-banner', '.jpg', [(600, '-600x253'), (768, '-768x324'), (1024, '-1024x432'), (1536, '-1536x648')], 2560)
T['photo-1764009699066-473e36008bab.jpeg'] = ('photo-1764009699066-473e36008bab', '.jpeg', [(600, '-600x900'), (768, '-768x1152'), (1024, '-1024x1536')], 1200)
for n in ['20_26xmas-chicken-2', '20_26xmas-bowl-jai', '20_26xmas-beef-box', '20_26xmas-prawn-salad', '20_26xmas-pistachio-tart',
          '20_26xmas-mentaiko-crossant', '20_26xmas-korea-rice', '20_26xmas-chestnut-pastry']:
    T[n + '.jpg'] = (n, '.jpg', SQ, 1667)

def _srcset(fn):
    base, ext, sz, full = T[fn]
    parts = ['%s%s%s%s %dw' % (U, base, suf, ext, w) for w, suf in sz]  # 不放原圖，最大用 819／1024／1229／1536 版（2026-11-21）
    mid = [s for s in sz if s[0] == 768] or sz[-1:]
    return ', '.join(parts), '%s%s%s%s' % (U, base, mid[0][1], ext)

def opt(html, sizes_for=None):
    """sizes_for(fn, tag) -> sizes 字串；預設手機全寬、電腦 600px。"""
    n = 0
    def rep_img(m):
        nonlocal n
        tag = m.group(0)
        if 'srcset=' in tag:
            return tag
        sm = re.search(r'src="%s([^"?]+)"' % re.escape(U), tag)
        if not sm or sm.group(1) not in T:
            return tag
        fn = sm.group(1)
        ss, mid = _srcset(fn)
        sz = (sizes_for(fn, tag) if sizes_for else None) or '(max-width:640px) 100vw, 600px'
        n += 1
        return tag.replace(sm.group(0), 'src="%s" srcset="%s" sizes="%s"' % (mid, ss, sz), 1)
    html = re.sub(r'<img\b[^>]*>', rep_img, html)
    # 其他引用（例如 data-i 換圖屬性）改用 768 版
    def rep_attr(m):
        fn = m.group(2)
        return m.group(1) + (_srcset(fn)[1] if fn in T else U + fn) + '"'
    html = re.sub(r'(data-i=")%s([^"?]+)"' % re.escape(U), rep_attr, html)
    return html, n
