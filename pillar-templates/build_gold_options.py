# -*- coding: utf-8 -*-
# 聖誕 LP 金色標題｜三個方案對比（A 上一版／B 今個 session 亮金／C 優雅明體金）
import pathlib, re, shutil, subprocess, sys, tempfile, html
HERE = pathlib.Path(__file__).parent

def build(script):
    d = pathlib.Path(tempfile.mkdtemp())
    for f in HERE.iterdir():
        if f.is_file(): shutil.copy(f, d / f.name)
    shutil.copy(script, d / 'build_a_christmas.py')
    subprocess.run([sys.executable, 'build_a_christmas.py'], cwd=d, check=True, capture_output=True)
    return (d / 'a-christmas.html').read_text(encoding='utf-8'), (d / 'a-christmas-en.html').read_text(encoding='utf-8')

PA, PA_EN = build(HERE / '_bak' / 'build_a_christmas.before-gold.py')
PB, PB_EN = build(HERE / 'build_a_christmas.py')

# ---- C：優雅明體金（細字重、金屬金、闊字距，英文 Baskerville）----
ZHS = '"Chiron Sung HK","Songti TC","Noto Serif TC",serif'
BASK = 'Baskerville,"Baskerville Old Face","Songti TC",Georgia,serif'
GC = 'linear-gradient(180deg,#F7E9BE 0%,#E2C377 38%,#BE913A 68%,#E9CF86 100%)'
GW = 'linear-gradient(180deg,#B48A35 0%,#8E6A22 100%)'
T = '-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent'
C_CSS = (
    f'.axl .hero small{{font-family:{BASK}!important;font-style:italic;font-weight:400!important;font-size:clamp(19px,2.2vw,24px);letter-spacing:.04em;text-transform:none!important;background-image:{GC};{T}}}'
    f'.axl .hero h1{{font-family:{ZHS}!important;font-weight:500!important;letter-spacing:.08em;line-height:1.45;background-image:{GC};{T};filter:drop-shadow(0 1px 6px rgba(0,0,0,.35))}}'
    f'.axl .hero h1:after{{content:"";display:block;width:64px;height:1px;margin:14px 0 2px;background:#D9B45E}}'
    f'.axl .hp small{{font-family:{BASK}!important;font-weight:400!important;font-size:12.5px;letter-spacing:.34em;background-image:{GC};{T}}}'
    f'.axl .hp .hph{{font-family:{ZHS}!important;font-weight:500!important;font-size:24px!important;letter-spacing:.24em;background-image:{GC};{T}}}'
    f'.axl .hp .hps2{{font-family:{ZHS}!important;font-weight:400;font-size:14px;letter-spacing:.14em;background-image:{GC};{T}}}'
    f'.axl .hp .hpt2 span,.axl .hp .orn{{background-image:{GC};{T}}}'
    f'.axl .sh small{{font-family:{BASK}!important;font-style:italic;font-weight:400!important;font-size:19px;letter-spacing:.04em;background-image:{GW};{T}}}'
    f'.axl .sh h2,.axl .bxl .st,.axl .bxl .col h2{{font-family:{ZHS}!important;font-weight:500!important;letter-spacing:.1em}}'
    '.axl .sh h2:after,.axl .bxl .st:after{background:#BE913A;width:36px}'
    # 分類方格：置中、明體金字、幼金線、白色斜體英文
    '.axl .bxl .mg a:after{background:linear-gradient(180deg,rgba(0,0,0,0) 40%,rgba(0,0,0,.66) 100%)}'
    '.axl .bxl .mg .tt b{text-align:center}.axl .bxl .mg span.tt{text-align:center;padding-bottom:clamp(16px,2.6vw,28px)}'
    f'.axl .bxl .mg .tt b{{font-family:{ZHS}!important;font-weight:500!important;font-size:clamp(18px,2.4vw,28px);letter-spacing:.18em;background-image:{GC};{T};filter:drop-shadow(0 1px 4px rgba(0,0,0,.55))}}'
    '.axl .bxl .mg .tt i:before{content:"";display:block;width:34px;height:1px;background:#D9B45E;margin:8px auto 8px}'
    '.axl .bxl .mg .tt i{font-size:clamp(14px,1.8vw,20px);color:#F4EEE2;letter-spacing:.04em}'
    '@media(max-width:640px){.axl .bxl .mg .tt b{font-size:15px;letter-spacing:.1em}.axl .bxl .mg .tt i{font-size:12.5px}.axl .bxl .mg .tt i:before{margin:5px auto}}')
ENS = 'Baskerville,"Baskerville Old Face",Georgia,serif'
C_EN = (f'.axl .hero h1,.axl .hp .hph,.axl .hp .hps2,.axl .sh h2,.axl .bxl .st,.axl .bxl .col h2,.axl .bxl .mg .tt b{{font-family:{ENS}!important;font-weight:400!important}}'
        '.axl .hero h1{letter-spacing:.02em}.axl .hp .hph{letter-spacing:.12em}.axl .hp .hps2{letter-spacing:.06em}.axl .sh h2,.axl .bxl .st,.axl .bxl .col h2{letter-spacing:.02em}.axl .bxl .mg .tt b{letter-spacing:.06em}')
FONT = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Chiron+Sung+HK:wght@400;500&display=swap">'
def mkc(p, en=False):
    css = C_CSS + (C_EN if en else '')
    return p.replace('</style>', css + '</style>' + FONT, 1).replace('<small>CHRISTMAS 2026 · KITCHEN AO</small>', '<small>Christmas 2026 · Kitchen AO</small>')
MFIX = re.search(r"MFIX = \((.*?)\)\nCSS \+= MFIX", (HERE / 'build_a_christmas.py').read_text(encoding='utf-8'), re.S).group(1)
MFIX = ''.join(eval('[' + MFIX.replace("'\n        '", "','") + ']'))
PA = PA.replace('</style>', MFIX + '</style>', 1); PA_EN = PA_EN.replace('</style>', MFIX + '</style>', 1)
PC = mkc(PB)
PC_EN = mkc(PB_EN, True)

def frag(p, en=False):
    head = p[p.index('<style>'):p.index('</head>')]          # 全部 <style>＋字體 link
    if en:
        i = p.index('<div class="ao-en" data-no-translation>'); p = p[i:p.index('<script>', i)]
    sfx = '-en' if en else ''
    hero = p[p.index('<div class="hero">'):p.index('<div class="eb">')]
    i = p.index(f'<section class="sec" id="series{sfx}"'); tiles = p[i:p.index('</section>', i) + 10]
    sh = re.search(rf'<section class="s" id="top{sfx}"><div class="w">(<div class="sh">.*?</div>)', p, re.S).group(1)
    hp = re.search(r'<div class="hp">.*?</div>', p, re.S).group(0)
    return (f'<!doctype html><html lang="{"en" if en else "zh-HK"}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">{head}</head>'
            f'<body style="margin:0"><div class="axl">{hero}<div class="bxl">{tiles}</div><section class="s"><div class="w">{sh}</div></section>'
            f'<section class="s" style="padding-top:0"><div class="w">{hp}</div></section></div></body></html>')

def review(en):
    O = [('A', 'Previous version' if en else '上一版', '啞金 #C8A24A、Helvetica 粗體英文眉題、方格文字置中。', PA_EN if en else PA),
         ('B', 'Bright gold' if en else '今個 session：亮金', '亮金漸變、粗體標題、方格文字左下角，白底眉題 Baskerville 斜體深金。', PB_EN if en else PB),
         ('C', 'Elegant serif gold' if en else '新方案：優雅明體金',
          ('金屬感柔金；英文標題改 Baskerville 細字重；' if en else '金屬感柔金、中文改細字重明體（Chiron Sung HK）加闊字距；') + 'Hero 眉題用「Our Top Picks」同款 Baskerville 斜體；方格置中加幼金線，參考酒店式低調金。', PC_EN if en else PC)]
    rows = ''
    for k, t, d, p in O:
        src = html.escape(frag(p, en), quote=True)
        rows += (f'<section class="op"><h2>Option {k}｜{t}</h2><p class="d">{d}</p><div class="r">'
                 f'<div><div class="lab">桌面</div><iframe class="dk" srcdoc="{src}"></iframe></div>'
                 f'<div><div class="lab">手機 390px</div><iframe class="mb" srcdoc="{src}"></iframe></div></div></section>')
    t = '聖誕 LP（英文版）｜金色標題三個方案' if en else '聖誕 LP｜金色標題三個方案'
    return ('<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>' + t + '</title>'
        '<style>body{margin:0;background:#ECE8E0;font-family:-apple-system,"PingFang HK",sans-serif;color:#222}.w0{max-width:1640px;margin:0 auto;padding:24px 20px 80px}'
        'h1{font-size:20px;margin:0 0 4px}.nt{font-size:13px;color:#777;margin:0 0 10px}.op{margin:34px 0 0;padding-top:20px;border-top:2px solid #cfc6b6}.op h2{font-size:18px;margin:0 0 4px}.d{font-size:13.5px;color:#555;margin:0 0 14px}'
        '.r{display:grid;grid-template-columns:minmax(0,1fr) 390px;gap:22px;align-items:start}.lab{font-size:12px;color:#888;margin:0 0 6px}iframe{border:0;width:100%;background:#fff;display:block}.mb{width:390px}'
        '@media(max-width:1100px){.r{grid-template-columns:1fr}}</style></head><body><div class="w0">'
        '<h1>' + t + '</h1><p class="nt">只顯示有改動的部分：Hero、分類方格、白底段落標題、首頁式黑色段落。請用瀏覽器開啟以載入相片及字體。</p>'
        + rows +
        '</div><script>function fit(f){try{var d=f.contentDocument;f.style.height=d.documentElement.scrollHeight+"px"}catch(e){}}'
        'document.querySelectorAll("iframe").forEach(function(f){f.addEventListener("load",function(){fit(f);setTimeout(function(){fit(f)},800);setTimeout(function(){fit(f)},2500)})});</script></body></html>')

(HERE / '聖誕LP-金色標題-三個方案.html').write_text(review(False), encoding='utf-8')
(HERE / '聖誕LP-金色標題-三個方案-EN.html').write_text(review(True), encoding='utf-8')
print('ok')
