# -*- coding: utf-8 -*-
"""雙 11 EDM Key Visual：3 個方向（email-safe table，漸變底有純色後備）"""
U = 'https://aoaodelivery.com/wp-content/uploads/'
HERO = U + '2023/11/%E7%87%88%E7%AE%B1-05-1024x1024.png'
GIFTS = [(U + '2023/10/KitchenAO_MAY2023-ALA-CARTE-03.png', '日式雞皮餃子'),
         (U + '2019/06/Posts-16-1024x1024.jpg', '蜜蜜燒雞翼'),
         (U + '2019/06/KitchenAO_MAY2023-ALA-CARTE-04.png', '避風塘海鮮豆腐')]

THEMES = {
 # key: (名稱, 後備底色, 漸變, 11.11 色, 標題色, 副題色, 卡片底, 卡片字, 膠囊底, 膠囊字)
 'A': ('黑金夜宴', '#141210', 'linear-gradient(160deg,#2a2118 0%,#141210 55%,#0b0a09 100%)', '#E4C77E', '#ffffff', '#CFC4AE', '#1f1b16', '#F4ECDD', '#C8A24A', '#141210'),
 'B': ('粉紫派對', '#B65AD8', 'linear-gradient(165deg,#F6A6C9 0%,#D66FD0 40%,#8E6BF0 100%)', '#ffffff', '#5B1A6E', '#ffffff', '#ffffff', '#5B1A6E', '#5B1A6E', '#ffffff'),
 'C': ('香檳奶油', '#F3E7D2', 'linear-gradient(170deg,#FBF4E8 0%,#F1E2C6 60%,#E6CFA4 100%)', '#B8862E', '#1A1A1A', '#6b5a3f', '#ffffff', '#1A1A1A', '#1A1A1A', '#E4C77E'),
}
TITLES = {
 'A': ('雙 11 年尾聚餐升級', '全網 89 折，滿 HK$1,500 再送人氣小食'),
 'B': ('派對美食　升級新體驗', '全網 89 折，滿額再送人氣小食'),
 'C': ('全網 89 折　滿額送小食', '年尾飯局提早安排，會員優惠照常享用'),
}

def kv(key, link='#', title=None):
    n, solid, grad, c11, ct, cs, cardbg, cardfg, pill, pillfg = THEMES[key]
    t, sub = title or TITLES[key]
    shadow = 'text-shadow:0 6px 18px rgba(0,0,0,.25);' if key != 'C' else ''
    gifts = ''.join(
        f'<td width="33.33%" valign="top" align="center" style="padding:0 5px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" bgcolor="{cardbg}" style="background:{cardbg};border-radius:12px;">'
        f'<tr><td align="center" style="padding:8px 8px 6px;"><img src="{src}" width="120" alt="{nm}" style="width:100%;max-width:120px;height:auto;display:block;border-radius:8px;"></td></tr>'
        f'<tr><td align="center" style="padding:0 6px 9px;color:{cardfg};font-size:12px;font-weight:bold;line-height:16px;">送 {nm}</td></tr></table></td>'
        for src, nm in GIFTS)
    return (
        f'<tr><td style="padding:0;"><a href="{link}" target="_blank" rel="noopener noreferrer" style="text-decoration:none;">'
        f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" bgcolor="{solid}" style="background:{solid};background-image:{grad};">'
        f'<tr><td align="center" style="padding:34px 18px 0;">'
        f'<p style="margin:0;color:{c11};font-family:\'Arial Black\',Arial,Helvetica,sans-serif;font-size:104px;line-height:100px;font-weight:900;font-style:italic;letter-spacing:-2px;{shadow}">11.11</p>'
        f'<p style="margin:14px 0 6px;color:{ct};font-size:30px;line-height:38px;font-weight:900;letter-spacing:2px;">{t}</p>'
        f'<p style="margin:0;color:{cs};font-size:15px;line-height:22px;font-weight:bold;">{sub}</p></td></tr>'
        f'<tr><td align="center" style="padding:16px 40px 0;"><img src="{HERO}" width="420" alt="Kitchen AO 到會美食" style="width:100%;max-width:420px;height:auto;display:block;margin:0 auto;"></td></tr>'
        f'<tr><td style="padding:14px 14px 0;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>{gifts}</tr></table></td></tr>'
        f'<tr><td align="center" style="padding:18px 18px 26px;"><table role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>'
        f'<td bgcolor="{pill}" style="background:{pill};border-radius:30px;padding:9px 20px;color:{pillfg};font-size:14px;font-weight:bold;letter-spacing:1px;">2026.11.11 至 11.17｜優惠碼 D11A／D11B</td></tr></table></td></tr>'
        '</table></a></td></tr>')

if __name__ == '__main__':
    import os
    H = os.path.dirname(os.path.abspath(__file__))
    blocks = ''
    for k in 'ABC':
        n = THEMES[k][0]
        blocks += (f'<div class="lab"><b>方案 {k}</b>{n}｜標題：「{TITLES[k][0]}」</div>'
                   f'<table role="presentation" width="600" align="center" cellpadding="0" cellspacing="0" style="width:100%;max-width:600px;margin:0 auto 10px;border-radius:14px;overflow:hidden;">{kv(k)}</table>')
    page = ('<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>雙 11 EDM Key Visual 方案</title>'
            '<style>body{margin:0;background:#EDEAE4;font-family:-apple-system,"PingFang HK","Noto Sans TC",sans-serif}.lab{max-width:600px;margin:28px auto 10px;padding:10px 16px;background:#141414;color:#F4ECDD;border-radius:10px;font-size:14px}.lab b{color:#E4C77E;margin-right:8px}'
            '.note{max-width:600px;margin:24px auto 0;font-size:13.5px;line-height:1.8;color:#5d534d}</style></head><body>'
            '<p class="note">三個方向都參考你提供的 11.11 圖：巨型斜體「11.11」、大標題、中間主角產品、下面一列浮卡（改為三款雙 11 贈品）、底部日期膠囊。設計方案亦按慣例參考 Four Seasons Sydney 的留白與層次。</p>'
            + blocks + '</body></html>')
    open(os.path.join(H, 'kv-options.html'), 'w', encoding='utf-8').write(page)
    print('ok')
