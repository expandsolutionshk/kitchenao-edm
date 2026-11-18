# -*- coding: utf-8 -*-
# 「聖誕主菜」段落｜三個排版方案（中英）
import pathlib, html, re
HERE = pathlib.Path(__file__).parent
P = (HERE / 'a-christmas.html').read_text(encoding='utf-8')
HEAD = P[P.index('<style>'):P.index('</head>')]
U = 'https://aoaodelivery.com/wp-content/uploads/2026/11/20_26xmas-'
T = {'zh': dict(g='Featuring our bespoke meats to WOW', b='2026 聖誕主菜', k='KITCHEN AO · 全港限量 100 個', more='查看套餐',
                items=[('chicken-2', '聖誕金雞獻禮', '燒南乳香慢煮原隻黃油雞', '原隻連木箱送到', '本地黃油雞以南乳醃製，低溫慢煮後高溫炙燒，皮脆肉嫩。', '#chk'),
                       ('beef-box', '聖誕寶藏箱', '煙燻慢煮美國牛翼板肉盛宴', '連復古寶箱送到', '稀有下肩胛翼板肉慢煮至五成熟，再以煙燻木料炙烤。', '#beef')]),
     'en': dict(g='Featuring our bespoke meats to WOW', b='Our Christmas Mains', k='KITCHEN AO · LIMITED TO 100 BOXES', more='View sets',
                items=[('chicken-2', 'Christmas Golden Roast', 'Slow-Cooked Red Beancurd Whole Yellow Chicken', 'Delivered with the Whole Box Set', 'Local yellow chicken in red beancurd marinade, slow-cooked then roasted for crisp skin.', '#chk'),
                       ('beef-box', 'Christmas Treasure Box', 'Smoked Slow-Cooked US Beef Chuck Flap Feast', 'Delivered with the Whole Treasure Box', 'Rare chuck flap, slow-cooked to medium then smoked over wood.', '#beef')])}
BASK = 'Baskerville,"Baskerville Old Face","Songti TC","Noto Serif TC",Georgia,serif'
SANS = '"Helvetica Neue","PingFang HK",Arial,sans-serif'
def head(t): return f'<div class="sh"><h2><span class="h2g lt">{t["g"]}</span><br><span class="h2b">{t["b"]}</span></h2></div>'

# A｜相片大圖＋底部疊字（雜誌封面感）
CSS_A = (f'.mo .ga{{display:grid;grid-template-columns:1fr 1fr;gap:24px}}.mo .ga a{{position:relative;display:block;aspect-ratio:4/5;overflow:hidden;text-decoration:none;background:#111}}'
         '.mo .ga img{width:100%;height:100%;object-fit:cover;transition:transform 1.2s}.mo .ga a:hover img{transform:scale(1.04)}'
         '.mo .ga .cp{position:absolute;inset:auto 0 0 0;padding:70px 28px 26px;background:linear-gradient(transparent,rgba(0,0,0,.82));color:#fff}'
         f'.mo .ga .k{{font:700 10.5px/1.4 {SANS};letter-spacing:.2em;color:#E4C77E;margin:0 0 10px}}'
         f'.mo .ga .n{{font-family:{BASK};font-size:clamp(24px,2.6vw,34px);line-height:1.2;margin:0 0 6px;color:#fff}}'
         f'.mo .ga .s{{font-family:{BASK};font-style:italic;font-size:15px;color:#E9E1D2;margin:0 0 12px}}'
         f'.mo .ga .d{{font:600 11px/1.4 {SANS};letter-spacing:.16em;text-transform:uppercase;color:#fff;display:inline-block;border-bottom:1px solid #C8A24A;padding-bottom:4px}}'
         '@media(max-width:640px){.mo .ga{grid-template-columns:1fr;gap:16px}.mo .ga .cp{padding:60px 20px 20px}}')
def A(t):
    return head(t) + '<div class="ga">' + ''.join(
        f'<a href="{h}"><img src="{U}{im}.jpg" alt="{n}"><div class="cp"><p class="k">{t["k"]}</p><p class="n">{n}</p><p class="s">{s}</p><span class="d">{d} →</span></div></a>'
        for im, n, s, d, x, h in t['items']) + '</div>'

# B｜相片在上、文字置中卡片（對稱、簡潔）
CSS_B = (f'.mo .gb{{display:grid;grid-template-columns:1fr 1fr;gap:40px;max-width:980px;margin:0 auto}}.mo .gb .c{{text-align:center}}'
         '.mo .gb .im{display:block;aspect-ratio:1/1;overflow:hidden;background:#111}.mo .gb img{width:100%;height:100%;object-fit:cover}'
         '.mo .gb .ln{width:1px;height:34px;background:#C8A24A;margin:0 auto 14px}'
         f'.mo .gb .k{{font:700 10.5px/1.4 {SANS};letter-spacing:.2em;color:#9A7B2E;margin:0 0 10px}}'
         f'.mo .gb .n{{font-family:{BASK};font-size:clamp(24px,2.4vw,30px);line-height:1.25;margin:0 0 6px}}'
         f'.mo .gb .s{{font-family:{BASK};font-style:italic;font-size:15px;color:var(--sub);margin:0 0 6px}}'
         '.mo .gb .d{font-size:14px;color:var(--sub);margin:0 0 16px}'
         f'.mo .gb .bt{{display:inline-block;font:700 11.5px/1 {SANS};letter-spacing:.2em;text-transform:uppercase;color:#9A7B2E;border:1px solid #C8A24A;padding:12px 26px;text-decoration:none}}'
         '.mo .gb .bt:hover{background:#C8A24A;color:#111}'
         '@media(max-width:640px){.mo .gb{grid-template-columns:1fr;gap:44px}}')
def B(t):
    return head(t) + '<div class="gb">' + ''.join(
        f'<div class="c"><a class="im" href="{h}"><img src="{U}{im}.jpg" alt="{n}"></a><div class="ln" style="margin-top:0"></div><p class="k">{t["k"]}</p>'
        f'<p class="n">{n}</p><p class="s">{s}</p><p class="d">{d}</p><a class="bt" href="{h}">{t["more"]}</a></div>'
        for im, n, s, d, x, h in t['items']) + '</div>'

# C｜左右交錯大圖＋編號（酒店餐廳頁感覺）
CSS_C = ('.mo .gc .r{display:grid;grid-template-columns:1.15fr 1fr;align-items:center;gap:0;margin:0 0 36px}.mo .gc .r.rv{grid-template-columns:1fr 1.15fr}.mo .gc .r.rv .im{order:2}'
         '.mo .gc .im{display:block;aspect-ratio:5/4;overflow:hidden;background:#111}.mo .gc img{width:100%;height:100%;object-fit:cover}'
         '.mo .gc .tx{padding:20px clamp(24px,5vw,72px)}'
         f'.mo .gc .no{{font-family:{BASK};font-style:italic;font-size:46px;line-height:1;color:#C8A24A;margin:0 0 14px}}'
         f'.mo .gc .k{{font:700 10.5px/1.4 {SANS};letter-spacing:.2em;color:#9A7B2E;margin:0 0 12px}}'
         f'.mo .gc .n{{font-family:{BASK};font-size:clamp(26px,2.8vw,38px);line-height:1.2;margin:0 0 8px}}'
         f'.mo .gc .s{{font-family:{BASK};font-style:italic;font-size:16px;color:var(--sub);margin:0 0 16px}}'
         '.mo .gc .x{font-size:15px;line-height:1.8;color:var(--sub);margin:0 0 14px;max-width:420px}'
         f'.mo .gc .d{{font:600 11px/1.4 {SANS};letter-spacing:.16em;text-transform:uppercase;color:#1A1A1A;margin:0 0 18px}}'
         f'.mo .gc .lk{{font-family:{BASK};font-style:italic;font-size:18px;color:#1A1A1A;text-decoration:none;border-bottom:1px solid #C8A24A;padding-bottom:3px}}'
         '@media(max-width:760px){.mo .gc .r,.mo .gc .r.rv{grid-template-columns:1fr}.mo .gc .r.rv .im{order:0}.mo .gc .tx{padding:22px 4px 0}.mo .gc .no{font-size:36px}}')
def C(t):
    return head(t) + '<div class="gc">' + ''.join(
        f'<div class="r{" rv" if i else ""}"><a class="im" href="{h}"><img src="{U}{im}.jpg" alt="{n}"></a><div class="tx"><p class="no">0{i+1}</p><p class="k">{t["k"]}</p>'
        f'<p class="n">{n}</p><p class="s">{s}</p><p class="x">{x}</p><p class="d">{d}</p><a class="lk" href="{h}">{t["more"]} →</a></div></div>'
        for i, (im, n, s, d, x, h) in enumerate(t['items'])) + '</div>'

OPTS = [('A', '大圖疊字', '兩張直身大圖並排，文字疊喺相片底部嘅黑色漸變上：金色小字、白色 Baskerville 名稱、斜體副名、金線「送到」字句。最有氣勢，似雜誌封面。', CSS_A, A),
        ('B', '置中卡片', '相片喺上，下面一條金色幼直線帶出置中文字，再加金框「查看套餐」按鈕。左右對稱，最簡潔清楚。', CSS_B, B),
        ('C', '左右交錯＋編號', '每款一行，大圖同文字左右交錯，加金色斜體編號 01、02、一句菜式介紹同「查看套餐 →」連結。參考酒店餐廳頁做法，最有質感。', CSS_C, C)]
def doc(lang, css, body):
    return (f'<!doctype html><html lang="{"en" if lang == "en" else "zh-HK"}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">{HEAD}<style>{css}</style></head>'
            f'<body style="margin:0"><div class="axl"><section class="s mo"><div class="w">{body}</div></section></div></body></html>')
rows = ''
for k, t, d, css, fn in OPTS:
    z = html.escape(doc('zh', css, fn(T['zh'])), quote=True); e = html.escape(doc('en', css, fn(T['en'])), quote=True)
    ez = html.escape(doc('en', css, fn(T['en'])), quote=True)
    rows += (f'<section class="op"><h2>Option {k}｜{t}</h2><p class="d">{d}</p>'
             f'<div class="r"><div><div class="lab">桌面（英文）</div><iframe class="dk" srcdoc="{ez}"></iframe><div class="lab" style="margin-top:14px">桌面（中文）</div><iframe class="dk" srcdoc="{z}"></iframe></div>'
             f'<div><div class="lab">手機（英文）</div><iframe class="mb" srcdoc="{e}"></iframe></div></div></section>')
page = ('<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>聖誕主菜段落｜三個排版方案</title>'
        '<style>body{margin:0;background:#ECE8E0;font-family:-apple-system,"PingFang HK",sans-serif;color:#222}.w0{max-width:1700px;margin:0 auto;padding:24px 20px 80px}'
        'h1{font-size:20px;margin:0 0 4px}.nt{font-size:13px;color:#777;margin:0 0 10px}.op{margin:30px 0 0;padding-top:18px;border-top:2px solid #cfc6b6}.op h2{font-size:18px;margin:0 0 4px}.d{font-size:13.5px;color:#555;margin:0 0 12px;max-width:900px}'
        '.r{display:grid;grid-template-columns:minmax(0,1fr) 390px;gap:22px;align-items:start}.lab{font-size:12px;color:#888;margin:0 0 6px}iframe{border:0;width:100%;background:#fff;display:block}.dk{height:820px}.mb{width:390px;height:1640px}'
        '@media(max-width:1100px){.r{grid-template-columns:1fr}}</style></head><body><div class="w0">'
        '<h1>聖誕主菜段落｜三個排版方案</h1><p class="nt">標題保持 H2 gold「Featuring our bespoke meats to WOW」＋ H2 black。每款有桌面中英及手機英文。請用瀏覽器開啟以載入相片。</p>'
        + rows + '</div></body></html>')
(HERE / '聖誕主菜-三個排版方案.html').write_text(page, encoding='utf-8')
print('ok')
