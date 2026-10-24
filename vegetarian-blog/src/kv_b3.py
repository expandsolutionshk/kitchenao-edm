# B3 KV：中國日曆（撕日曆／通勝）主題 → ../kv-b3-preview.html
import os, html, urllib.parse
from kv_fresh import LOGO
HERE = os.path.dirname(os.path.abspath(__file__))

TXT = ('每月農曆初一・十五食齋懶人包原因・禁忌・日子一次看清12個月日子自動更新食齋日望日葷腥五辛茹素祈福宜忌'
       '每月農曆望日朔日宜忌茹素祈福葷腥五辛初一十五')
FONT = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@900&family=Noto+Sans+TC:wght@700'
        '&display=swap&text=' + urllib.parse.quote(''.join(sorted(set(TXT)))) + '">')

SER = "'Noto Serif TC','Songti TC',serif"
SAN = "'Noto Sans TC',-apple-system,'PingFang HK',sans-serif"
RED, INK, PAPER, GOLD = '#B5382B', '#2E2A26', '#F7EFDF', '#C9A24A'

CSS = f'''
.kx3{{position:relative;width:100%;aspect-ratio:16/9;container-type:inline-size;overflow:hidden;border:4px solid #CFE8CD;border-radius:6px;box-sizing:border-box;font-family:{SAN};
 background-color:{PAPER};background-image:radial-gradient(circle at 78% 46%,rgba(201,162,74,.22) 0 15cqw,transparent 15.2cqw),repeating-linear-gradient(0deg,rgba(150,110,60,.05) 0 .15cqw,transparent .15cqw 3cqw)}}
.kx3 *{{box-sizing:border-box}}
.kx3:before{{content:"";position:absolute;inset:1.6cqw;border:.25cqw solid rgba(181,56,43,.45);outline:.12cqw solid rgba(181,56,43,.3);outline-offset:-.8cqw;pointer-events:none;z-index:1}}
.kx3 .logo2{{position:absolute;right:2.6cqw;top:2.6cqw;z-index:9;display:inline-flex;align-items:center;height:4.3cqw;background:#fff;border:.25cqw solid #EAD9C0;border-radius:3cqw;padding:0 1.8cqw}}
.kx3 .logo2 img{{display:block!important;width:auto!important;max-width:none!important;margin:0!important;padding:0!important;border:0!important;box-shadow:none!important}}
.kx3 .logo2 .li{{height:2.3cqw!important}}.kx3 .logo2 .lt{{height:2cqw!important;margin-left:1cqw!important}}
.kx3 .tb{{position:absolute;z-index:3;left:6cqw;top:50%;transform:translateY(-50%);width:50cqw}}
.kx3 .kick{{display:inline-block;font:700 1.9cqw/1 {SAN};color:{RED};letter-spacing:.25cqw;border-bottom:.25cqw solid {RED};padding-bottom:.6cqw}}
.kx3 .big{{margin:1.6cqw 0 0!important;padding:0!important;border:0!important;font:900 6.6cqw/1.1 {SER};color:{INK};letter-spacing:.3cqw;white-space:nowrap;text-transform:none!important}}
.kx3 .sub{{margin:1cqw 0 0;font:900 4.2cqw/1.15 {SER};color:{RED};letter-spacing:.2cqw;white-space:nowrap}}
.kx3 .pill{{display:inline-flex;align-items:center;gap:.8cqw;margin:2.2cqw 0 0;font:700 2.3cqw/1 {SAN};color:{INK};background:#F1DDB7;border:.18cqw solid #D9BE8A;padding:1.1cqw 2.4cqw;border-radius:3cqw;box-shadow:0 .4cqw 0 #D9BE8A}}
.kx3 .pill:before{{content:"🏮";font-size:2.1cqw}}
.kx3 .badge{{position:absolute;z-index:6;left:41cqw;top:7cqw;width:11.5cqw;height:11.5cqw;border-radius:50%;background:{GOLD};color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;transform:rotate(-8deg);font:700 1.45cqw/1.25 {SAN};border:.35cqw solid #fff;box-shadow:0 .6cqw 1.4cqw rgba(90,60,20,.25)}}
.kx3 .badge b{{font:900 3cqw/1.05 {SER};color:#fff}}
.kx3 .cal{{position:absolute;z-index:4;right:9cqw;top:52%;transform:translateY(-50%);width:25cqw;height:33cqw}}
.kx3 .pg{{position:absolute;inset:0;background:#FFFCF5;border-radius:1cqw;box-shadow:0 1cqw 2.4cqw rgba(80,50,20,.22);overflow:hidden;display:flex;flex-direction:column}}
.kx3 .pg.back{{transform:rotate(-10deg) translate(-7cqw,1.2cqw);background:#FBF5EA}}.kx3 .pg.back .num{{justify-content:flex-start;padding-left:1.4cqw;font-size:7cqw}}
.kx3 .pg.front{{transform:rotate(3deg)}}
.kx3 .pg .hd{{background:{RED};color:#FFE9C9;font:700 1.7cqw/1 {SAN};letter-spacing:.5cqw;text-align:center;padding:2.6cqw 0 1.2cqw}}
.kx3 .pg .num{{flex:1;display:flex;align-items:center;justify-content:center;position:relative;font:900 9.6cqw/1 {SER};color:{RED};letter-spacing:.2cqw}}
.kx3 .pg.back .num{{color:#C9B8A2}}
.kx3 .pg .num i{{display:none}}
.kx3 .pg .num i.l{{left:1.6cqw}}.kx3 .pg .num i.r{{right:1.6cqw}}
.kx3 .pg .yj{{display:grid;grid-template-columns:1fr;border-top:.18cqw dashed #E2D3BC}}
.kx3 .pg .yj div{{display:flex;align-items:center;gap:1cqw;padding:.9cqw 2cqw;font:700 1.6cqw/1.3 {SAN};color:{INK};white-space:nowrap;letter-spacing:.2cqw}}
.kx3 .pg .yj div+div{{border-top:.18cqw dashed #E2D3BC}}
.kx3 .pg .yj b{{flex:none;width:2.6cqw;height:2.6cqw;border-radius:50%;display:flex;align-items:center;justify-content:center;font:900 1.5cqw/1 {SER};color:#fff;background:#4E7D46}}
.kx3 .pg .yj div+div b{{background:{RED}}}
.kx3 .ring{{position:absolute;z-index:6;top:-1.2cqw;width:1.8cqw;height:3.4cqw;border-radius:1cqw;background:linear-gradient(90deg,#6B5D4F,#B9AA98 50%,#6B5D4F);box-shadow:0 .2cqw .4cqw rgba(0,0,0,.3)}}
.kx3 .ring.a{{left:6cqw;transform:rotate(3deg)}}.kx3 .ring.b{{right:6cqw;transform:rotate(3deg)}}
@media(max-width:640px){{
 .kx3{{aspect-ratio:4/5;background-image:radial-gradient(circle at 50% 74%,rgba(201,162,74,.22) 0 30cqw,transparent 30.4cqw),repeating-linear-gradient(0deg,rgba(150,110,60,.05) 0 .3cqw,transparent .3cqw 6cqw)}}
 .kx3:before{{inset:3cqw;outline-offset:-1.5cqw}}
 .kx3 .logo2{{height:7.5cqw;padding:0 3cqw;right:5.5cqw;top:5.5cqw}}.kx3 .logo2 .li{{height:4cqw!important}}.kx3 .logo2 .lt{{height:3.4cqw!important;margin-left:1.6cqw!important}}
 .kx3 .tb{{left:8cqw;right:8cqw;top:15cqw;transform:none;width:auto}}
 .kx3 .kick{{font-size:3.6cqw;padding-bottom:1cqw}}.kx3 .big{{font-size:12.5cqw;margin-top:3cqw!important}}.kx3 .sub{{font-size:7.8cqw;margin-top:1.6cqw}}
 .kx3 .pill{{font-size:4.2cqw;padding:2cqw 4cqw;margin-top:3.6cqw}}.kx3 .pill:before{{font-size:3.8cqw}}
 .kx3 .badge{{width:20cqw;height:20cqw;left:auto;right:7cqw;top:auto;bottom:47cqw;font-size:2.5cqw}}.kx3 .badge b{{font-size:5.2cqw}}
 .kx3 .cal{{right:auto;left:50%;top:auto;bottom:7cqw;transform:translateX(-42%);width:44cqw;height:50cqw}}
 .kx3 .pg .hd{{font-size:3cqw;padding:4.6cqw 0 2cqw}}.kx3 .pg .num{{font-size:14.5cqw}}.kx3 .pg .num i{{font-size:2.4cqw}}.kx3 .pg .num i.l{{left:2.6cqw}}.kx3 .pg .num i.r{{right:2.6cqw}}
 .kx3 .pg .yj div{{font-size:2.8cqw;padding:1.6cqw 3.4cqw;gap:1.6cqw}}.kx3 .pg.back .num{{font-size:11cqw;padding-left:2.4cqw}}.kx3 .pg .yj b{{width:4.4cqw;height:4.4cqw;font-size:2.6cqw}}
 .kx3 .ring{{width:3cqw;height:5.6cqw;top:-2cqw}}.kx3 .ring.a{{left:10cqw}}.kx3 .ring.b{{right:10cqw}}
}}'''

CALCSS2 = """
.kx3 .cal{height:auto!important;container-type:inline-size;filter:drop-shadow(0 1.2cqw 1.6cqw rgba(60,30,10,.28))}
.kx3 .cal .pad{height:9cqw;margin:0 4cqw;background:linear-gradient(180deg,#F4EEDC,#E9E0C8);border-radius:4cqw 4cqw 0 0;border-bottom:1.6cqw solid #D9442A;position:relative}
.kx3 .cal .pad:after{content:"";position:absolute;left:3cqw;right:3cqw;bottom:-1.6cqw;height:1.6cqw;background:repeating-linear-gradient(90deg,#F7F3EA 0 .8cqw,transparent .8cqw 2.4cqw)}
.kx3 .cal .pp{position:relative;background:#FCFBF7;padding:5cqw 5cqw 5cqw;color:#D9442A;font-family:'Noto Sans TC',-apple-system,'PingFang HK',sans-serif;text-align:center;border-radius:0 0 1.2cqw 1.2cqw}
.kx3 .cal .mh{font:900 8.4cqw/1 'Arial Black','Helvetica Neue',Arial,sans-serif;letter-spacing:.6cqw}
.kx3 .cal .mid{position:relative;display:flex;align-items:center;justify-content:space-between;margin-top:2cqw}
.kx3 .cal .vt{writing-mode:vertical-rl;font:500 6.4cqw/1 'Noto Sans TC',sans-serif;letter-spacing:2.6cqw;color:#D9442A}
.kx3 .cal .bn{position:relative;font:900 44cqw/1 'Arial Black','Helvetica Neue',Arial,sans-serif;letter-spacing:-2cqw;color:#D9442A}
.kx3 .cal .bn i{position:absolute;left:-9cqw;top:2.4cqw;font-style:normal;color:#E4E0DA}.kx3 .cal .bn u{position:relative;text-decoration:none}
.kx3 .cal .wd{margin-top:1cqw;font:900 7.2cqw/1 'Arial Black','Helvetica Neue',Arial,sans-serif;letter-spacing:.5cqw}
.kx3 .cal .box{display:grid;grid-template-columns:1fr 1.25fr 1fr;margin-top:4cqw;border:.7cqw solid #D9442A;outline:.35cqw solid #D9442A;outline-offset:.9cqw}
.kx3 .cal .bx{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:1cqw;padding:3cqw 1cqw}
.kx3 .cal .bx b{font:900 13cqw/1 'Noto Serif TC',serif}
.kx3 .cal .bx span{font:700 5.6cqw/1.15 'Noto Sans TC',sans-serif;letter-spacing:.6cqw}
.kx3 .cal .bc{border-left:.5cqw solid #D9442A;border-right:.5cqw solid #D9442A;padding:2.4cqw 1cqw 3cqw}
.kx3 .cal .bc em{display:inline-block;font-style:normal;background:#D9442A;color:#FCFBF7;font:900 5.4cqw/1 'Noto Sans TC',sans-serif;letter-spacing:1cqw;padding:1.2cqw 2.6cqw 1.2cqw 3.6cqw;border-radius:5cqw}
.kx3 .cal .bc div{display:flex;align-items:center;justify-content:center;gap:1.6cqw;margin-top:2.4cqw}
.kx3 .cal .bc small{writing-mode:vertical-rl;font:500 4.4cqw/1 'Noto Sans TC',sans-serif;letter-spacing:1cqw}
.kx3 .cal .bc strong{writing-mode:vertical-rl;font:900 15cqw/1 'Noto Serif TC',serif;letter-spacing:1cqw}
.kx3 .cal .pg,.kx3 .cal .ring{display:none!important}
"""

def cal():
    return ('<div class="cal"><div class="pad"></div><div class="pp"><div class="mh">LUNAR DAY</div>'
            '<div class="mid"><span class="vt">每月農曆</span><span class="bn"><i>1</i><u>15</u></span><span class="vt">初一十五</span></div>'
            '<div class="wd">FULL MOON</div>'
            '<div class="box"><div class="bx"><b>忌</b><span>葷腥</span><span>五辛</span></div>'
            '<div class="bx bc"><em>食齋日</em><div><small>望日</small><strong>十五</strong><small>農曆</small></div></div>'
            '<div class="bx"><b>宜</b><span>茹素</span><span>祈福</span></div></div></div></div>')

def kv(tag='div'):
    return (f'<div class="kx3">{LOGO}<div class="tb"><span class="kick">每月農曆初一・十五</span>'
            f'<{tag} class="big">初一十五食齋</{tag}><div class="sub">懶人包</div><span class="pill">原因・禁忌・日子一次看清</span></div>'
            '<div class="badge">12 個月<b>日子</b>自動更新</div>' + cal() + '</div>')

def block(tag='div'):
    return f'<div class="ao-b3kv" style="margin:0 0 22px">{FONT}<style>{(CSS + CALCSS2).replace(chr(10), "")}</style>{kv(tag)}</div>'

if __name__ == '__main__':
    b = block()
    doc = f'<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body style="margin:0;padding:10px;background:#fff">{b}</body></html>'
    page = (f'<!doctype html><html><head><meta charset="utf-8"><meta name="robots" content="noindex"><title>B3 KV</title></head><body style="margin:0;background:#EEF1EA;display:flex;gap:14px;padding:14px;align-items:flex-start">'
            f'<iframe srcdoc="{html.escape(doc)}" style="width:900px;height:540px;border:0;background:#fff"></iframe>'
            f'<iframe srcdoc="{html.escape(doc)}" style="width:390px;height:520px;border:0;background:#fff"></iframe></body></html>')
    open(os.path.join(HERE, '..', 'kv-b3-preview.html'), 'w', encoding='utf-8').write(page)
    print('ok')
