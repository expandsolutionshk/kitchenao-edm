# -*- coding: utf-8 -*-
# Hero CTA 按鈕三個方案（只改 Hero 內 .btn.p）
import pathlib, re, html
HERE = pathlib.Path(__file__).parent
P = (HERE / 'a-christmas.html').read_text(encoding='utf-8')
PE = (HERE / 'a-christmas-en.html').read_text(encoding='utf-8')
BASK = 'Baskerville,"Baskerville Old Face",Georgia,serif'
OPTS = [
 ('A', '金色幼框', '透明底、1px 金框、金色字；滑鼠移上時金色填滿、字轉黑。跟供應日期列的黑金線條一致。',
  '.axl .hero .btn.p{background:transparent!important;border:1px solid #C8A24A!important;color:#E4C77E!important;font-size:13px;letter-spacing:.24em;padding:14px 34px;position:relative;overflow:hidden;z-index:0}'
  '.axl .hero .btn.p:before{content:"";position:absolute;inset:0;background:#C8A24A;transform:scaleX(0);transform-origin:left;transition:transform .45s cubic-bezier(.6,0,.2,1);z-index:-1}'
  '.axl .hero .btn.p:hover{color:#111!important}.axl .hero .btn.p:hover:before{transform:scaleX(1)}'),
 ('B', '金屬金實底', '柔金漸變實底、黑字、細字距大楷；滑鼠移上時有一道光掃過。最搶眼，CTA 最清楚。',
  '.axl .hero .btn.p{background:linear-gradient(180deg,#E9CF86 0%,#C8A24A 55%,#B38A35 100%)!important;border:0!important;color:#141414!important;font-size:13px;font-weight:700;letter-spacing:.22em;padding:15px 36px;position:relative;overflow:hidden;box-shadow:0 6px 20px rgba(0,0,0,.35)}'
  '.axl .hero .btn.p:after{content:"";position:absolute;top:0;bottom:0;left:0;width:40%;background:linear-gradient(100deg,transparent,rgba(255,255,255,.55),transparent);transform:translateX(-150%) skewX(-20deg);transition:transform .7s}'
  '.axl .hero .btn.p:hover:after{transform:translateX(320%) skewX(-20deg)}'),
 ('C', '文字連結＋金線', '不用按鈕框：Baskerville 斜體白字＋金色箭嘴，下面一條金線；滑鼠移上時金線伸長、箭嘴向右移。最低調高雅，酒店網站常用。',
  f'.axl .hero .btn.p{{background:transparent!important;border:0!important;padding:6px 0 10px!important;font-family:{BASK}!important;font-style:italic;font-weight:400!important;text-transform:none!important;letter-spacing:.03em!important;font-size:20px!important;color:#fff!important;position:relative}}'
  '.axl .hero .btn.p:after{content:" \\2192";color:#E4C77E;font-style:normal;display:inline-block;margin-left:10px;transition:transform .3s}'
  '.axl .hero .btn.p:before{content:"";position:absolute;left:0;bottom:0;height:1px;width:60%;background:#C8A24A;transition:width .4s}'
  '.axl .hero .btn.p:hover:before{width:100%}.axl .hero .btn.p:hover:after{transform:translateX(6px)}'
  '@media(max-width:640px){.axl .hero .btn.p{display:inline-block!important;width:auto!important;font-size:18px!important}}'),
]
def frag(p, css, en=False):
    head = p[p.index('<style>'):p.index('</head>')]
    if en:
        i = p.index('<div class="ao-en" data-no-translation>'); p = p[i:p.index('<script>', i)]
    hero = p[p.index('<div class="hero">'):p.index('<details class="xav2">')]
    if not en:  # C 款中文按鈕不用大楷
        pass
    return (f'<!doctype html><html lang="{"en" if en else "zh-HK"}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">{head}<style>{css}</style></head>'
            f'<body style="margin:0"><div class="axl">{hero}</div></body></html>')
rows = ''
for k, t, d, css in OPTS:
    z = html.escape(frag(P, css), quote=True); e = html.escape(frag(PE, css, True), quote=True)
    rows += (f'<section class="op"><h2>Option {k}｜{t}</h2><p class="d">{d}</p><div class="r">'
             f'<div><div class="lab">桌面（中文）</div><iframe class="dk" srcdoc="{z}"></iframe></div>'
             f'<div><div class="lab">手機（英文）</div><iframe class="mb" srcdoc="{e}"></iframe></div></div></section>')
page = ('<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Hero 按鈕｜三個方案</title>'
        '<style>body{margin:0;background:#ECE8E0;font-family:-apple-system,"PingFang HK",sans-serif;color:#222}.w0{max-width:1640px;margin:0 auto;padding:24px 20px 80px}'
        'h1{font-size:20px;margin:0 0 4px}.nt{font-size:13px;color:#777;margin:0 0 10px}.op{margin:30px 0 0;padding-top:18px;border-top:2px solid #cfc6b6}.op h2{font-size:18px;margin:0 0 4px}.d{font-size:13.5px;color:#555;margin:0 0 12px}'
        '.r{display:grid;grid-template-columns:minmax(0,1fr) 390px;gap:22px;align-items:start}.lab{font-size:12px;color:#888;margin:0 0 6px}iframe{border:0;width:100%;height:640px;background:#111;display:block}.mb{width:390px;height:560px}'
        '@media(max-width:1100px){.r{grid-template-columns:1fr}}</style></head><body><div class="w0">'
        '<h1>Hero 按鈕｜三個方案</h1><p class="nt">動畫約 3 秒後按鈕出現；桌面可把滑鼠移到按鈕上看 hover 效果。請用瀏覽器開啟以載入相片。</p>'
        + rows + '</div></body></html>')
(HERE / 'Hero按鈕-三個方案.html').write_text(page, encoding='utf-8')
print('ok')
