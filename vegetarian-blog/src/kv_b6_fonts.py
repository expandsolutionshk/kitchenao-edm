# B6 KV P1（海報＋字典詞條）：5 款字體＋素食配色 → ../kv-b6-fonts.html
import os, html, random, urllib.parse
from kv_fresh import LOGO
from kv_frame_d import veg, U as SVGU, NAMES
HERE = os.path.dirname(os.path.abspath(__file__))
IMG = 'https://aoaodelivery.com/wp-content/uploads/2026/10/veg-b2-kv-vegan.jpg'
TXT = '素食英文速查2026Vegan中文是甚麼？素食英文一表看清附到外國餐廳的點餐英文中英對照25+素食用語純素（全素）不吃任何動物來源食品，包括肉、蛋、奶及蜜糖veganoun·adj.'

def gf(family_query):   # Google Fonts，只下載用到的字（text= 子集），檔案很細
    return f'<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family={family_query}&display=swap&text={urllib.parse.quote(TXT)}">'

def line(name, col):
    return SVGU(veg(name, chalk=True).replace('#FFFFFF', col).replace('stroke-width="2.4"', 'stroke-width="1.6"'))

THEMES = [
 ('F1｜粉圓體 Huninn（圓潤親切）', 'Huninn', "'Huninn',sans-serif", "'Huninn',sans-serif",
  dict(bg='#F4F1E4', h='#2F6B3F', sub='#E07A2E', pill='#5C9E4A', pillsh='#3F7A33', badge='#E07A2E', badgeb='#FFF3C4', kick='#5C9E4A', dd='#9CBF84', zh='#E07A2E'),
  '圓角黑體，筆畫圓潤可愛，配橙綠色，最有親切的生活感。'),
 ('F2｜霞鶩文楷 LXGW WenKai TC（手寫楷書）', 'LXGW+WenKai+TC:wght@700', "'LXGW WenKai TC',serif", "'LXGW WenKai TC',serif",
  dict(bg='#F3EEDF', h='#3B5D2E', sub='#B5532D', pill='#6B8E4E', pillsh='#4F6E38', badge='#3B5D2E', badgeb='#F2D16B', kick='#6B8E4E', dd='#A8B98A', zh='#B5532D'),
  '似手寫的楷書，帶點書卷和自然感，配橄欖綠及陶土紅，最有「素食天書」的味道。'),
 ('F3｜Chiron GoRound TC（現代圓黑）', 'Chiron+GoRound+TC:wght@800', "'Chiron GoRound TC',sans-serif", "'Chiron GoRound TC',sans-serif",
  dict(bg='#EFF5EA', h='#1F6B4A', sub='#F08C1F', pill='#2E9E6B', pillsh='#1F7A50', badge='#2E9E6B', badgeb='#FFE58A', kick='#2E9E6B', dd='#8FC4A2', zh='#F08C1F'),
  '粗身圓黑體，乾淨現代，配薄荷綠及芒果橙，最清新年輕。'),
 ('F4｜思源宋體 Noto Serif TC（雜誌襯線）', 'Noto+Serif+TC:wght@900', "'Noto Serif TC',serif", "'Noto Serif TC',serif",
  dict(bg='#F6F2E8', h='#24452F', sub='#7A9A3A', pill='#24452F', pillsh='#152C1D', badge='#7A9A3A', badgeb='#FFF1B8', kick='#7A9A3A', dd='#B3C29A', zh='#7A9A3A'),
  '粗襯線宋體，似雜誌刊頭，配深墨綠及牛油果綠，最有質感。'),
 ('F5｜昭源宋體 Chiron Sung HK（香港字形）', 'Chiron+Sung+HK:wght@900', "'Chiron Sung HK',serif", "'Chiron Sung HK',serif",
  dict(bg='#F5EFE2', h='#355E3B', sub='#C8553D', pill='#355E3B', pillsh='#223F27', badge='#C8553D', badgeb='#FFE9A8', kick='#C8553D', dd='#B9A27A', zh='#C8553D'),
  '按香港字形標準設計的宋體，配森林綠及番茄紅，最有本地感。'),
]

def css(fh, fw, c):
    return f'''
.kx{{position:relative;width:100%;aspect-ratio:16/9;container-type:inline-size;overflow:hidden;font-family:-apple-system,"PingFang HK",sans-serif;border:4px solid #CFE8CD;border-radius:6px;box-sizing:border-box;
 background-color:{c["bg"]};background-image:repeating-linear-gradient(90deg,rgba(120,110,60,.05) 0 .2cqw,transparent .2cqw 2.6cqw),repeating-linear-gradient(90deg,rgba(120,110,60,.04) 0 .1cqw,transparent .1cqw 7.3cqw),radial-gradient(ellipse at 70% 30%,rgba(255,255,255,.7),transparent 60%)}}
.kx *{{box-sizing:border-box}}
.kx .dd{{position:absolute;aspect-ratio:1;background:no-repeat center/contain;opacity:.6;pointer-events:none;z-index:1}}
.kx .logo2{{position:absolute;right:2cqw;top:2cqw;z-index:9;display:inline-flex;align-items:center;height:4.3cqw;background:#fff;border:.25cqw solid #DCEFD6;border-radius:3cqw;padding:0 1.8cqw}}.kx .logo2 img{{display:block;width:auto}}.kx .logo2 .li{{height:2.3cqw}}.kx .logo2 .lt{{height:2cqw;margin-left:1cqw}}
.kx .tb{{position:absolute;z-index:3;left:5cqw;top:50%;transform:translateY(-50%);width:50cqw}}
.kx .kick{{display:inline-block;font:700 1.9cqw/1 {fh};color:{c["kick"]};letter-spacing:.2cqw}}
.kx .big{{margin:1.2cqw 0 0;font:{fw} 5.2cqw/1.15 {fh};color:{c["h"]};letter-spacing:.1cqw;-webkit-text-stroke:.25cqw #fff;paint-order:stroke fill;text-shadow:.3cqw .35cqw 0 rgba(40,70,40,.18);white-space:nowrap}}
.kx .sub{{margin:1cqw 0 0;font:{fw} 3.9cqw/1.15 {fh};color:{c["sub"]};letter-spacing:.15cqw;white-space:nowrap}}
.kx .pill{{display:inline-flex;align-items:center;gap:.8cqw;margin:2cqw 0 0;font:700 1.8cqw/1 {fh};color:#fff;background:{c["pill"]};padding:1cqw 2.2cqw;border-radius:3cqw;box-shadow:0 .4cqw 0 {c["pillsh"]}}}
.kx .pill:before{{content:"🌱";font-size:1.6cqw}}
.kx .badge{{position:absolute;z-index:6;left:33cqw;top:6cqw;width:11cqw;height:11cqw;border-radius:50%;background:{c["badge"]};color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;transform:rotate(10deg);box-shadow:0 .5cqw 1.2cqw rgba(40,60,30,.25);border:.35cqw solid #fff;font:700 1.35cqw/1.25 {fh}}}
.kx .badge b{{font:{fw} 2.8cqw/1.05 {fh};color:{c["badgeb"]}}}
.kx .card{{position:absolute;right:5cqw;top:57%;transform:translateY(-50%) rotate(2deg);z-index:4;width:29cqw;background:#FFFDF8;border-radius:1.4cqw;box-shadow:0 1.2cqw 2.8cqw rgba(40,60,30,.2);overflow:hidden}}
.kx .card i{{display:block;height:11cqw;background:url({IMG}) center/cover}}
.kx .card div{{padding:1.8cqw 2.2cqw 2.2cqw}}
.kx .card .w{{font:{fw} 4.6cqw/1 {fh};color:#1A1A1A}}.kx .card .pr{{margin-top:.6cqw;font:500 1.5cqw/1.2 Georgia,serif;color:#7a6a50}}.kx .card .pr em{{color:{c["h"]};margin-left:.8cqw}}
.kx .card .zh{{margin-top:1cqw;font:{fw} 2.4cqw/1.2 {fh};color:{c["zh"]}}}.kx .card .df{{margin-top:.6cqw;font:500 1.35cqw/1.5 {fh};color:#555}}
@media(max-width:640px){{.kx{{aspect-ratio:4/5}}.kx .logo2{{height:7.5cqw;padding:0 3cqw;right:4cqw;top:4cqw}}.kx .logo2 .li{{height:4cqw}}.kx .logo2 .lt{{height:3.4cqw;margin-left:1.6cqw}}
 .kx .tb{{left:6cqw;right:6cqw;top:15cqw;transform:none;width:auto}}.kx .kick{{font-size:3.4cqw}}.kx .big{{font-size:10cqw}}.kx .sub{{font-size:7.4cqw}}.kx .pill{{font-size:3.2cqw;padding:1.8cqw 3.6cqw}}.kx .pill:before{{font-size:3cqw}}
 .kx .badge{{width:19cqw;height:19cqw;font-size:2.4cqw;right:5cqw;left:auto;top:auto;bottom:50%}}.kx .badge b{{font-size:4.8cqw}}.kx .dd{{display:none}}
 .kx .card{{left:8cqw;right:8cqw;width:auto;top:auto;bottom:5cqw;transform:rotate(1.5deg)}}.kx .card i{{height:20cqw}}.kx .card .w{{font-size:8cqw}}.kx .card .pr{{font-size:2.8cqw}}.kx .card .zh{{font-size:4.4cqw}}.kx .card .df{{font-size:2.6cqw}}}}
'''

def kv(c):
    r = random.Random(3)
    dd = ''.join(f'<i class="dd" style="left:{x}%;top:{y}%;width:{s}cqw;transform:translate(-50%,-50%) rotate({r.randint(-30,30)}deg);background-image:{line(NAMES[(i*3+3)%8], c["dd"])}"></i>'
                 for i, (x, y, s) in enumerate([(4,10,6),(30,88,5),(48,12,5),(58,86,6),(96,90,5),(12,92,5)]))
    return f'''<div class="kx">{dd}{LOGO}<div class="tb">
<span class="kick">素食英文速查 2026</span>
<div class="big">Vegan 中文是甚麼？</div>
<div class="sub">素食英文一表看清</div>
<span class="pill">附到外國餐廳的點餐英文</span></div>
<div class="badge">中英對照<b>25+</b>素食用語</div>
<div class="card"><i></i><div><div class="w">vegan</div><div class="pr">/ˈviːɡən/<em>noun · adj.</em></div><div class="zh">純素（全素）</div><div class="df">不吃任何動物來源食品，包括肉、蛋、奶及蜜糖</div></div></div></div>'''

secs = []
for t, q, fh, _, c, d in THEMES:
    fw = '700' if 'Huninn' in q else '800' if 'GoRound' in q or 'WenKai' in q else '900'
    doc = (f'<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">{gf(q)}'
           f'<style>body{{margin:0;padding:20px 14px;background:#fff}}{css(fh, fw, c)}</style></head><body>{kv(c)}</body></html>')
    secs.append(f'<section class="opt"><h3>{t}</h3><p>{d}</p><div class="pair"><div><small>桌面</small>'
                f'<iframe srcdoc="{html.escape(doc)}" style="width:880px;height:540px"></iframe></div>'
                f'<div><small>手機</small><iframe srcdoc="{html.escape(doc)}" style="width:390px;height:560px"></iframe></div></div></section>')
page = f'''<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>B6 KV 字體方案</title>
<style>body{{margin:0;background:#EEF1EA;color:#222;font:15px/1.6 -apple-system,"PingFang HK",sans-serif}}.wrap{{max-width:1340px;margin:0 auto;padding:24px 16px 60px}}
.opt{{margin:0 0 34px}}.opt h3{{margin:0 0 4px;font-size:18px}}.opt p{{margin:0 0 10px;color:#555;font-size:14px}}
.pair{{display:flex;gap:16px;flex-wrap:wrap;align-items:flex-start}}.pair small{{display:block;font-weight:700;color:#7a6a45;margin:0 0 4px}}iframe{{border:1px solid #ddd;background:#fff;border-radius:8px}}</style></head>
<body><div class="wrap"><h1 style="font-size:22px">B6 KV｜P1 海報＋字典詞條：5 款字體及素食配色</h1>
<p style="font-size:14px;color:#555">字體均為 Google Fonts 免費商用字體，只載入 KV 用到的字（子集），檔案很細。預覽要用瀏覽器打開及連線上網才看到字體。</p>{''.join(secs)}</div></body></html>'''
open(os.path.join(HERE, '..', 'kv-b6-fonts.html'), 'w', encoding='utf-8').write(page)
print('ok')
