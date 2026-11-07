# -*- coding: utf-8 -*-
"""首頁兩個 section（活動場合／熱門套餐）各 3 個設計方案
輸出：options-preview.html（全部預覽）＋ 6 個 WPBakery Raw HTML 檔"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
P = 'https://aoaodelivery.com'
U = P + '/wp-content/uploads/'

# ---------- 內容（書面語，已優化） ----------
S1 = dict(eb='OCCASIONS', h2='按活動場合選擇香港到會服務',
          sub='由生日派對到公司活動，Kitchen AO 按人數及場合配搭餐單，準時送到指定地點。')
SCENES = [
    dict(k='party', n='01', t='派對到會', d='生日會、朋友聚會及家庭聚餐，套餐份量靈活，方便多人分享。', tip='小型聚會至百人派對均可安排',
         img=U + '2026/03/8-10_101-X-KITCHENAO-03-03-03-768x768.jpg', url=P + '/product-category/party/', go='查看派對套餐',
         ic='<path d="M5.8 11.3 2 22l10.7-3.79"/><path d="M4 3h.01M22 8h.01M15 2h.01M22 20h.01"/><path d="m22 2-2.24.75a2.9 2.9 0 0 0-1.96 3.12c.1.86-.57 1.63-1.45 1.63h-.38c-.86 0-1.6.6-1.76 1.44L14 10"/><path d="m11 13 6.5-6.5"/><path d="M11 2.06v.68c0 .86-.6 1.6-1.44 1.76L9 4.67"/><path d="M8.5 8.5 15.5 15.5"/>'),
    dict(k='corp', n='02', t='公司活動到會', d='會議茶點、開幕酒會及員工聚餐，準時送達，商務場合更體面。', tip='會議、酒會及員工活動',
         img=U + '2023/11/IMG_2358.jpg', url=P + '/corporate-catering-hk/', go='了解公司到會',
         ic='<rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>'),
    dict(k='boat', n='03', t='船河到會及商務午餐', d='船河聚會、戶外活動及商務午餐，保溫包裝，方便攜帶及分發。', tip='兼顧賣相與實用',
         img=U + '2025/04/WhatsApp-Image-2025-04-12-at-4.08.26-PM-600x600.jpeg', url=P + '/product-category/party/boat-party-set/', go='查看船河套餐',
         ic='<path d="M2 21c.6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1 .6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1"/><path d="M19.38 20A11.6 11.6 0 0 0 21 14l-9-4-9 4c0 2.9.94 5.34 2.81 7.76"/><path d="M19 13V7a2 2 0 0 0-2-2H7a2 2 0 0 0-2 2v6"/><path d="M12 10v4M12 2v3"/>'),
]
S2 = dict(eb='POPULAR SETS', h2='熱門到會套餐推介',
          sub='精選適合派對、公司聚會及輕食場合的人氣餐單，按人數快速開始預訂。')
SETS = [
    dict(lab='PARTY SET', t='美食派對到會套餐', d='熱盤主菜、小食及甜品一應俱全，適合生日會、朋友聚餐及節日慶祝。', meta='8 至 85 人', pr='HK$1,988 起',
         img=U + '2026/03/8-10_101-X-KITCHENAO-03-03-03-768x768.jpg', url=P + '/product-category/party/', go='查看套餐'),
    dict(lab='REFRESHMENT', t='輕食宴會套餐', d='一口大小的精緻小食，適合會議茶點、開幕活動及下午茶聚會。', meta='12 至 40 人', pr='HK$2,688 起',
         img=U + '2023/11/refreshmentparty-03-768x768.jpg', url=P + '/product-category/party/refreshment-set/', go='查看套餐'),
    dict(lab='À LA CARTE', t='單點美食精選', d='自由配搭小食、主菜、甜品及飲品，加配或自組專屬餐單都方便。', meta='小食・主菜・甜品・飲品', pr='按需要配搭',
         img=U + '2019/06/Posts-16-scaled-600x600.jpg', url=P + '/product-category/a-la-carte/', go='查看美食'),
]

def sv(path, cls='sv'):
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{path}</svg>'

BASE = '''.{c}{{max-width:1180px;margin:0 auto;padding:64px 20px 40px;box-sizing:border-box;color:#3A342B;font-family:inherit}}
.{c} *{{box-sizing:border-box}}
.{c} a{{text-decoration:none !important;color:inherit}}
.{c} .hd{{margin:0 0 30px}}
.{c} .eb{{font-size:11.5px;letter-spacing:.3em;color:#8A8378;margin:0 0 8px !important}}
.{c} h2{{position:relative;font-size:30px !important;font-weight:900 !important;color:#141414 !important;margin:0 0 12px !important;padding:18px 0 0 !important;line-height:1.3 !important;border:0 !important}}
.{c} h2:before{{content:"";position:absolute;left:0;top:0;width:46px;height:4px;border-radius:3px;background:#C8A24A}}
.{c} .sub{{font-size:16px;line-height:1.8;color:#5d574f;margin:0 !important;max-width:640px}}
.{c} .t{{font-weight:900 !important;color:#141414;margin:0 !important}}
.{c} br{{display:none}}
@media(max-width:860px){{.{c}{{padding:44px 16px 28px}}.{c} h2{{font-size:24px !important}}.{c} .sub{{font-size:15px}}}}
'''
def head(c, S, center=False):
    al = ' style="text-align:center"' if center else ''
    return f'<div class="hd"{al}><p class="eb">{S["eb"]}</p><h2>{S["h2"]}</h2><p class="sub"{" style=&quot;margin:0 auto !important&quot;" if False else ""}>{S["sub"]}</p></div>'

# ================= Section 1：活動場合 =================
def s1_a():
    c = 'ao-occ-a'
    css = BASE.format(c=c) + f'''.{c} .grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}}
.{c} .card{{display:flex;flex-direction:column;background:#fff;border:1px solid #E6E1D8;border-radius:18px;overflow:hidden;transition:box-shadow .2s,transform .2s}}
.{c} .card:hover{{box-shadow:0 16px 36px rgba(20,18,16,.12);transform:translateY(-3px)}}
.{c} .im{{position:relative;aspect-ratio:4/3;overflow:hidden;background:#F3F0EA}}
.{c} .im img{{position:absolute;inset:0;width:100% !important;height:100% !important;object-fit:cover;margin:0 !important;transition:transform .5s}}
.{c} .card:hover .im img{{transform:scale(1.04)}}
.{c} .ic{{position:absolute;left:18px;bottom:-24px;width:52px;height:52px;border-radius:50%;background:#141414;color:#E4C77E;display:flex;align-items:center;justify-content:center;z-index:1;box-shadow:0 6px 16px rgba(0,0,0,.18)}}
.{c} .im{{overflow:visible}}.{c} .im .ph{{position:absolute;inset:0;overflow:hidden}}
.{c} .sv{{width:24px;height:24px}}
.{c} .tx{{padding:38px 22px 22px;display:flex;flex-direction:column;flex:1}}
.{c} .t{{font-size:20px !important;margin:0 0 8px !important}}
.{c} .d{{font-size:15px;line-height:1.75;color:#5d574f;margin:0 0 16px !important;flex:1}}
.{c} .ft{{display:flex;justify-content:space-between;align-items:center;gap:10px;padding-top:14px;border-top:1px solid #EFE9DD}}
.{c} .tip{{font-size:12.5px;font-weight:700;color:#8A6D24;background:#FBF6EA;border:1px solid #E8D9B2;border-radius:20px;padding:4px 10px;white-space:nowrap}}
.{c} .go{{font-size:14px;font-weight:800;color:#141414;border-bottom:1.5px solid #C8A24A;padding-bottom:2px;white-space:nowrap}}
@media(max-width:860px){{.{c} .grid{{grid-template-columns:1fr;gap:18px}}}}'''
    cards = ''.join(f'<a class="card" href="{s["url"]}"><div class="im"><div class="ph"><img src="{s["img"]}" alt="{s["t"]}｜Kitchen AO" loading="lazy"></div><span class="ic">{sv(s["ic"])}</span></div>'
                    f'<div class="tx"><p class="t">{s["t"]}</p><p class="d">{s["d"]}</p><div class="ft"><span class="tip">{s["tip"]}</span><span class="go">{s["go"]}</span></div></div></a>' for s in SCENES)
    return c, css, head(c, S1) + f'<div class="grid">{cards}</div>'

def s1_b():
    c = 'ao-occ-b'
    css = BASE.format(c=c) + f'''.{c} .grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}}
.{c} .card{{position:relative;display:block;aspect-ratio:3/4;border-radius:18px;overflow:hidden;background:#222}}
.{c} .card img{{position:absolute;inset:0;width:100% !important;height:100% !important;object-fit:cover;margin:0 !important;transition:transform .6s}}
.{c} .card:hover img{{transform:scale(1.05)}}
.{c} .card:after{{content:"";position:absolute;inset:0;background:linear-gradient(0deg,rgba(12,10,8,.92) 0%,rgba(12,10,8,.5) 45%,rgba(12,10,8,0) 72%)}}
.{c} .tx{{position:absolute;left:0;right:0;bottom:0;z-index:1;padding:24px 24px 26px}}
.{c} .n{{display:block;font-size:13px;font-weight:800;letter-spacing:.2em;color:#E4C77E;margin:0 0 8px}}
.{c} .t{{font-size:24px !important;color:#fff !important;margin:0 0 8px !important}}
.{c} .d{{font-size:14.5px;line-height:1.7;color:#DCD3C2;margin:0 0 16px !important}}
.{c} .go{{display:inline-block;font-size:13.5px;font-weight:800;color:#141414;background:#E4C77E;border-radius:40px;padding:9px 18px}}
.{c} .card:hover .go{{background:#fff}}
@media(max-width:860px){{.{c} .grid{{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;gap:14px;scrollbar-width:none;margin-right:-16px;padding-right:16px}}.{c} .card{{flex:0 0 80%;scroll-snap-align:start}}}}'''
    cards = ''.join(f'<a class="card" href="{s["url"]}"><img src="{s["img"]}" alt="{s["t"]}｜Kitchen AO" loading="lazy"><div class="tx"><span class="n">{s["n"]}</span><p class="t">{s["t"]}</p><p class="d">{s["d"]}</p><span class="go">{s["go"]}</span></div></a>' for s in SCENES)
    return c, css, head(c, S1) + f'<div class="grid">{cards}</div>'

def s1_c():
    c = 'ao-occ-c'
    css = BASE.format(c=c) + f'''.{c}{{max-width:none;background:#F7F5F0;padding:64px 20px 56px}}
.{c} .in{{max-width:1180px;margin:0 auto}}
.{c} .grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:0;border-top:1px solid #E2D6BC}}
.{c} .card{{display:flex;flex-direction:column;padding:30px 28px 26px;border-right:1px solid #E2D6BC;transition:background .2s}}
.{c} .card:last-child{{border-right:0}}
.{c} .card:hover{{background:#fff}}
.{c} .top{{display:flex;align-items:center;justify-content:space-between;margin:0 0 22px}}
.{c} .n{{font-size:34px;font-weight:900;color:#E2D6BC;line-height:1}}
.{c} .ic{{width:50px;height:50px;border-radius:50%;background:#141414;color:#E4C77E;display:flex;align-items:center;justify-content:center}}
.{c} .sv{{width:23px;height:23px}}
.{c} .t{{font-size:21px !important;margin:0 0 10px !important}}
.{c} .d{{font-size:15px;line-height:1.8;color:#5d574f;margin:0 0 6px !important}}
.{c} .tip{{font-size:13px;color:#8A6D24;font-weight:700;margin:0 0 20px !important}}
.{c} .go{{margin-top:auto;align-self:flex-start;font-size:14px;font-weight:800;color:#141414;border-bottom:1.5px solid #C8A24A;padding-bottom:2px}}
@media(max-width:860px){{.{c}{{padding:44px 16px 36px}}.{c} .grid{{grid-template-columns:1fr}}.{c} .card{{border-right:0;border-bottom:1px solid #E2D6BC;padding:24px 4px}}}}'''
    cards = ''.join(f'<a class="card" href="{s["url"]}"><div class="top"><span class="n">{s["n"]}</span><span class="ic">{sv(s["ic"])}</span></div><p class="t">{s["t"]}</p><p class="d">{s["d"]}</p><p class="tip">{s["tip"]}</p><span class="go">{s["go"]}</span></a>' for s in SCENES)
    return c, css, '<div class="in">' + head(c, S1) + f'<div class="grid">{cards}</div></div>'

# ================= Section 2：熱門套餐 =================
def s2_a():
    c = 'ao-set-a'
    css = BASE.format(c=c) + f'''.{c} .grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}}
.{c} .card{{display:flex;flex-direction:column;background:#F7F5F0;border-radius:20px;padding:14px;transition:box-shadow .2s}}
.{c} .card:hover{{box-shadow:0 14px 30px rgba(20,18,16,.10)}}
.{c} .im{{position:relative;aspect-ratio:1/1;border-radius:14px;overflow:hidden;background:#fff}}
.{c} .im img{{position:absolute;inset:0;width:100% !important;height:100% !important;object-fit:cover;margin:0 !important;transition:transform .5s}}
.{c} .card:hover .im img{{transform:scale(1.04)}}
.{c} .lab{{position:absolute;left:12px;top:12px;font-size:11px;font-weight:800;letter-spacing:.18em;color:#141414;background:rgba(255,255,255,.92);padding:5px 10px;border-radius:20px}}
.{c} .tx{{padding:16px 6px 4px;display:flex;flex-direction:column;flex:1}}
.{c} .t{{font-size:19px !important;margin:0 0 8px !important}}
.{c} .d{{font-size:14.5px;line-height:1.75;color:#5d574f;margin:0 0 14px !important;flex:1}}
.{c} .ft{{display:flex;justify-content:space-between;align-items:flex-end;gap:10px;padding-top:14px;border-top:1px solid #E2D6BC}}
.{c} .meta{{display:block;font-size:12.5px;color:#8A8378}}
.{c} .pr{{display:block;font-size:16px;font-weight:900;color:#9A7B2E}}
.{c} .go{{font-size:14px;font-weight:800;color:#141414;border-bottom:1.5px solid #C8A24A;padding-bottom:2px;white-space:nowrap}}
@media(max-width:860px){{.{c} .grid{{grid-template-columns:1fr;gap:16px}}}}'''
    cards = ''.join(f'<a class="card" href="{s["url"]}"><div class="im"><img src="{s["img"]}" alt="{s["t"]}｜Kitchen AO" loading="lazy"><span class="lab">{s["lab"]}</span></div>'
                    f'<div class="tx"><p class="t">{s["t"]}</p><p class="d">{s["d"]}</p><div class="ft"><div><span class="meta">{s["meta"]}</span><span class="pr">{s["pr"]}</span></div><span class="go">{s["go"]}</span></div></div></a>' for s in SETS)
    return c, css, head(c, S2) + f'<div class="grid">{cards}</div>'

def s2_b():
    c = 'ao-set-b'
    css = BASE.format(c=c) + f'''.{c}{{max-width:none;background:#141414;padding:64px 20px 56px}}
.{c} .in{{max-width:1180px;margin:0 auto}}
.{c} .eb{{color:#D9C48A !important}}.{c} h2{{color:#fff !important}}.{c} .sub{{color:#CFCAC0 !important}}
.{c} .grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}}
.{c} .card{{display:flex;flex-direction:column;background:#1E1B18;border:1px solid #3a3226;border-radius:18px;overflow:hidden;transition:border-color .2s}}
.{c} .card:hover{{border-color:#C8A24A}}
.{c} .im{{position:relative;aspect-ratio:1/1;overflow:hidden}}
.{c} .im img{{position:absolute;inset:0;width:100% !important;height:100% !important;object-fit:cover;margin:0 !important;transition:transform .5s}}
.{c} .card:hover .im img{{transform:scale(1.04)}}
.{c} .tx{{padding:20px 20px 22px;display:flex;flex-direction:column;flex:1}}
.{c} .lab{{font-size:11px;font-weight:800;letter-spacing:.22em;color:#C8A24A;margin:0 0 8px}}
.{c} .t{{font-size:20px !important;color:#fff !important;margin:0 0 8px !important}}
.{c} .d{{font-size:14.5px;line-height:1.7;color:#BFB8AC;margin:0 0 16px !important;flex:1}}
.{c} .ft{{display:flex;justify-content:space-between;align-items:center;gap:10px}}
.{c} .pr{{font-size:15px;font-weight:900;color:#E4C77E}}
.{c} .go{{font-size:13.5px;font-weight:800;color:#141414;background:#E4C77E;border-radius:40px;padding:9px 18px;white-space:nowrap}}
.{c} .card:hover .go{{background:#fff}}
@media(max-width:860px){{.{c}{{padding:44px 16px 36px}}.{c} .grid{{grid-template-columns:1fr;gap:16px}}}}'''
    cards = ''.join(f'<a class="card" href="{s["url"]}"><div class="im"><img src="{s["img"]}" alt="{s["t"]}｜Kitchen AO" loading="lazy"></div>'
                    f'<div class="tx"><span class="lab">{s["lab"]}</span><p class="t">{s["t"]}</p><p class="d">{s["d"]}</p><div class="ft"><span class="pr">{s["meta"]}｜{s["pr"]}</span><span class="go">{s["go"]}</span></div></div></a>' for s in SETS)
    return c, css, '<div class="in">' + head(c, S2) + f'<div class="grid">{cards}</div></div>'

def s2_c():
    c = 'ao-set-c'
    css = BASE.format(c=c) + f'''.{c} .list{{display:grid;gap:18px}}
.{c} .row{{display:grid;grid-template-columns:300px 1fr auto;gap:28px;align-items:center;background:#fff;border:1px solid #E6E1D8;border-radius:18px;padding:16px 28px 16px 16px;transition:box-shadow .2s}}
.{c} .row:hover{{box-shadow:0 14px 30px rgba(20,18,16,.10)}}
.{c} .im{{position:relative;aspect-ratio:16/10;border-radius:12px;overflow:hidden;background:#F3F0EA}}
.{c} .im img{{position:absolute;inset:0;width:100% !important;height:100% !important;object-fit:cover;margin:0 !important}}
.{c} .lab{{font-size:11px;font-weight:800;letter-spacing:.22em;color:#9A7B2E;margin:0 0 6px}}
.{c} .t{{font-size:21px !important;margin:0 0 8px !important}}
.{c} .d{{font-size:15px;line-height:1.75;color:#5d574f;margin:0 0 10px !important}}
.{c} .meta{{font-size:13px;color:#8A8378}}
.{c} .rt{{text-align:right}}
.{c} .pr{{display:block;font-size:18px;font-weight:900;color:#141414;margin:0 0 12px;white-space:nowrap}}
.{c} .go{{display:inline-block;font-size:14px;font-weight:800;color:#fff;background:#141414;border-radius:40px;padding:11px 22px;white-space:nowrap}}
.{c} .row:hover .go{{background:#C8A24A;color:#141414}}
@media(max-width:860px){{.{c} .row{{grid-template-columns:1fr;gap:14px;padding:14px 14px 18px}}.{c} .rt{{text-align:left;display:flex;justify-content:space-between;align-items:center}}.{c} .pr{{margin:0}}}}'''
    rows = ''.join(f'<a class="row" href="{s["url"]}"><div class="im"><img src="{s["img"]}" alt="{s["t"]}｜Kitchen AO" loading="lazy"></div>'
                   f'<div class="mid"><p class="lab">{s["lab"]}</p><p class="t">{s["t"]}</p><p class="d">{s["d"]}</p><span class="meta">{s["meta"]}</span></div>'
                   f'<div class="rt"><span class="pr">{s["pr"]}</span><span class="go">{s["go"]}</span></div></a>' for s in SETS)
    return c, css, head(c, S2) + f'<div class="list">{rows}</div>'

OPTS = [
 ('s1-a', '活動場合｜方案 A：白卡＋圓形 icon', '4:3 相片、黑底金色 icon 疊在相片底部，下面標題、說明、米金色標籤及文字連結。最清楚，配合首頁其他白卡。', s1_a),
 ('s1-b', '活動場合｜方案 B：直身大相＋圖上文字', '3:4 直身相做主角，文字疊在相片下方，金色按鈕；手機可左右滑動。最有質感及吸引力。', s1_b),
 ('s1-c', '活動場合｜方案 C：米白全幅＋編號三欄', '參考 Chanterelle 賣點卡：大編號 01／02／03、黑金 icon、幼線分隔，不用相片，最簡潔、載入最快。', s1_c),
 ('s2-a', '熱門套餐｜方案 A：米白卡＋內縮相片', '同 18404 產品卡方案 C 一致：米白底、相片內縮、英文標籤、人數及價錢、金線下「查看套餐」。', s2_a),
 ('s2-b', '熱門套餐｜方案 B：黑色全幅段', '黑底卡＋金色價錢及按鈕，與 18404 黑色 Hero 呼應，同上一段白色 section 形成黑白分段。', s2_b),
 ('s2-c', '熱門套餐｜方案 C：橫向清單', '左相、中間介紹、右邊價錢及黑色按鈕，似餐單列表，最易比較三款套餐；手機變直排。', s2_c),
]

def raw(c, css, body):
    return f'<section class="{c}">\n<style>\n{css}\n</style>\n{body}\n</section>\n'

if __name__ == '__main__':
    prev = ['<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>首頁兩個 section：各 3 個方案</title>'
            '<style>body{margin:0;font-family:-apple-system,"PingFang HK",sans-serif;background:#fff}.lab{max-width:1180px;margin:40px auto 0;padding:12px 20px;background:#EEE9DF;border-radius:10px;font-size:14px;color:#5d534d;line-height:1.6}.lab b{color:#141414;font-size:16px;display:block}.lab code{font-size:12px;color:#9A7B2E}</style></head><body>']
    for key, name, desc, fn in OPTS:
        c, css, body = fn()
        r = raw(c, css, body)
        open(os.path.join(HERE, f'{key}-rawhtml.html'), 'w', encoding='utf-8').write(r)
        prev.append(f'<div class="lab"><b>{name}</b>{desc}<br><code>Raw HTML 檔：{key}-rawhtml.html</code></div>' + r)
    prev.append('</body></html>')
    open(os.path.join(HERE, 'options-preview.html'), 'w', encoding='utf-8').write('\n'.join(prev))
    print('ok')
