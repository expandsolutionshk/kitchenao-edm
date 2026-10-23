# B6 KV 方案 v2：參考展覽海報風格（淺木紋底、粗體大字、紅色副題、圓形徽章、淡線條蔬菜插畫）→ ../kv-b6-options.html
import os, html, random
from kv_fresh import LOGO
from kv_frame_d import veg, U as SVGU, NAMES
HERE = os.path.dirname(os.path.abspath(__file__))
W = 'https://aoaodelivery.com/wp-content/uploads/2026/10/'
IMG = {'vegan': W + 'veg-b2-kv-vegan.jpg', 'egg': W + 'veg-b2-kv-egg.jpg', 'milk': W + 'veg-b2-kv-milk.jpg', 'wx': W + 'veg-b2-kv-wuxin.jpg'}
FONT = '-apple-system,"PingFang HK","Microsoft JhengHei",Arial,sans-serif'
SERIF = '"Noto Serif TC","Songti TC","PMingLiU",Georgia,serif'

def line(name):   # 淡啡色線條版蔬菜
    return SVGU(veg(name, chalk=True).replace('#FFFFFF', '#B9976A').replace('stroke-width="2.4"', 'stroke-width="1.6"'))
def doodles(seed, spots):
    r = random.Random(seed)
    return ''.join(f'<i class="dd" style="left:{x}%;top:{y}%;width:{s}cqw;transform:translate(-50%,-50%) rotate({r.randint(-30,30)}deg);background-image:{line(NAMES[(i*3+seed)%8])}"></i>'
                   for i, (x, y, s) in enumerate(spots))

BASE = f'''
.kx{{position:relative;width:100%;aspect-ratio:16/9;container-type:inline-size;overflow:hidden;font-family:{FONT};border:4px solid #CFE8CD;border-radius:6px;box-sizing:border-box;
 background-color:#F6EFE3;background-image:repeating-linear-gradient(90deg,rgba(160,120,70,.05) 0 .2cqw,transparent .2cqw 2.6cqw),repeating-linear-gradient(90deg,rgba(160,120,70,.04) 0 .1cqw,transparent .1cqw 7.3cqw),radial-gradient(ellipse at 70% 30%,rgba(255,255,255,.7),transparent 60%)}}
.kx *{{box-sizing:border-box}}
.kx .dd{{position:absolute;aspect-ratio:1;background:no-repeat center/contain;opacity:.55;pointer-events:none;z-index:1}}
.kx .logo2{{position:absolute;right:2cqw;top:2cqw;z-index:9;display:inline-flex;align-items:center;height:4.3cqw;background:#fff;border:.25cqw solid #E7DCC8;border-radius:3cqw;padding:0 1.8cqw}}.kx .logo2 img{{display:block;width:auto}}.kx .logo2 .li{{height:2.3cqw}}.kx .logo2 .lt{{height:2cqw;margin-left:1cqw}}
.kx .tb{{position:absolute;z-index:3}}
.kx .kick{{display:inline-block;font:900 1.9cqw/1 {FONT};color:#2F8F4E;letter-spacing:.2cqw}}
.kx .big{{margin:1cqw 0 0;font:900 5.2cqw/1.12 {FONT};color:#9A5A2B;letter-spacing:.1cqw;-webkit-text-stroke:.25cqw #fff;paint-order:stroke fill;text-shadow:.3cqw .35cqw 0 rgba(120,70,30,.25);white-space:nowrap}}
.kx .red{{margin:1cqw 0 0;font:900 3.9cqw/1.1 {FONT};color:#D7262E;letter-spacing:.15cqw;white-space:nowrap}}
.kx .pill{{display:inline-flex;align-items:center;gap:.8cqw;margin:2cqw 0 0;font:800 1.8cqw/1 {FONT};color:#fff;background:#3C6FD1;padding:1cqw 2.2cqw;border-radius:3cqw;box-shadow:0 .4cqw 0 #27519F}}
.kx .pill:before{{content:"";width:1.6cqw;height:1.6cqw;border-radius:50%;background:#fff;box-shadow:inset 0 0 0 .45cqw #D7262E}}
.kx .badge{{position:absolute;z-index:6;width:11cqw;height:11cqw;border-radius:50%;background:#9A5A2B;color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;transform:rotate(10deg);box-shadow:0 .5cqw 1.2cqw rgba(90,50,20,.3);border:.35cqw solid #fff;font:800 1.35cqw/1.25 {FONT}}}
.kx .badge b{{font:900 2.8cqw/1.05 {FONT};color:#FFE08A}}
@media(max-width:640px){{.kx{{aspect-ratio:4/5}}.kx .logo2{{height:7.5cqw;padding:0 3cqw;right:4cqw;top:4cqw}}.kx .logo2 .li{{height:4cqw}}.kx .logo2 .lt{{height:3.4cqw;margin-left:1.6cqw}}
 .kx .tb{{left:6cqw!important;right:6cqw;top:15cqw!important;transform:none!important;width:auto!important}}.kx .kick{{font-size:3.4cqw}}.kx .big{{font-size:10cqw}}.kx .red{{font-size:7.4cqw}}.kx .pill{{font-size:3.2cqw;padding:1.8cqw 3.6cqw}}.kx .pill:before{{width:2.8cqw;height:2.8cqw}}
 .kx .badge{{width:19cqw;height:19cqw;font-size:2.4cqw;right:5cqw!important;left:auto!important;top:auto!important;bottom:50%!important}}.kx .badge b{{font-size:4.8cqw}}.kx .dd{{display:none}}}}
'''
TB = '''<div class="tb" style="left:5cqw;top:50%;transform:translateY(-50%);width:50cqw">
<span class="kick">🌱 素食英文速查 2026</span>
<div class="big">Vegan 中文是甚麼？</div>
<div class="red">素食英文一表看清</div>
<span class="pill">附到外國餐廳的點餐英文</span></div>'''

OPTS = [
('P1｜海報＋字典詞條',
 '淺木紋底、啡色粗體大字、紅色副題、藍色資料牌及圓形徽章，參考展覽海報的排版；右邊一張字典詞條卡（vegan /ˈviːɡən/ 純素），背景淡淡畫上線條蔬菜。',
 '''
.p1 .card{position:absolute;right:5cqw;top:57%;transform:translateY(-50%) rotate(2deg);z-index:4;width:29cqw;background:#FFFDF8;border-radius:1.4cqw;box-shadow:0 1.2cqw 2.8cqw rgba(90,60,30,.22);overflow:hidden}
.p1 .card i{display:block;height:11cqw;background:center/cover}
.p1 .card div{padding:1.8cqw 2.2cqw 2.2cqw}
.p1 .card .w{font:700 4.6cqw/1 "Noto Serif TC",Georgia,serif;color:#1A1A1A}.p1 .card .pr{margin-top:.6cqw;font:500 1.5cqw/1.2 Georgia,serif;color:#7a6a50}.p1 .card .pr em{color:#2F8F4E;margin-left:.8cqw}
.p1 .card .zh{margin-top:1cqw;font:900 2.4cqw/1.2 -apple-system,"PingFang HK",sans-serif;color:#D7262E}.p1 .card .df{margin-top:.6cqw;font:600 1.35cqw/1.5 -apple-system,"PingFang HK",sans-serif;color:#555}
.p1 .badge{left:33cqw;top:6cqw}
@media(max-width:640px){.p1 .card{left:8cqw;right:8cqw;width:auto;top:auto;bottom:5cqw;transform:rotate(1.5deg)}.p1 .card i{height:20cqw}.p1 .card .w{font-size:8cqw}.p1 .card .pr{font-size:2.8cqw}.p1 .card .zh{font-size:4.4cqw}.p1 .card .df{font-size:2.6cqw}}
''',
 lambda: f'''<div class="kx p1">{doodles(3, [(4,10,6),(30,88,5),(48,12,5),(58,86,6),(96,90,5),(12,92,5)])}{LOGO}{TB}
<div class="badge">中英對照<b>25+</b>素食用語</div>
<div class="card"><i style="background-image:url({IMG['vegan']})"></i><div><div class="w">vegan</div><div class="pr">/ˈviːɡən/<em>noun · adj.</em></div><div class="zh">純素（全素）</div><div class="df">不吃任何動物來源食品，包括肉、蛋、奶及蜜糖</div></div></div></div>'''),

('P2｜海報＋中英字卡',
 '同一海報排版，右邊改為 4 張微傾斜的中英字卡（Vegetarian 素食者、Vegan 純素、Flexitarian 彈性素食者、Pescatarian 海鮮素者），一眼看到「中英對照」。',
 '''
.p2 .cards{position:absolute;right:3.5cqw;top:55%;transform:translateY(-50%);z-index:4;width:34cqw;display:grid;grid-template-columns:1fr 1fr;gap:1.4cqw}
.p2 .cd{background:#FFFDF8;border-radius:1.2cqw;overflow:hidden;box-shadow:0 1cqw 2.2cqw rgba(90,60,30,.22)}
.p2 .cd:nth-child(1){transform:rotate(-3deg)}.p2 .cd:nth-child(2){transform:rotate(2.5deg) translateY(1.2cqw)}.p2 .cd:nth-child(3){transform:rotate(2deg)}.p2 .cd:nth-child(4){transform:rotate(-2.5deg) translateY(1.2cqw)}
.p2 .cd i{display:block;height:5.6cqw;background:center/cover}.p2 .cd div{padding:1cqw 1.4cqw 1.3cqw}
.p2 .cd b{display:block;font:700 2.2cqw/1.1 "Noto Serif TC",Georgia,serif;color:#1A1A1A}.p2 .cd span{display:block;margin-top:.4cqw;font:900 1.8cqw/1.2 -apple-system,"PingFang HK",sans-serif;color:#2F8F4E}.p2 .cd.no span{color:#D7262E}
.p2 .badge{left:36cqw;top:5cqw}
@media(max-width:640px){.p2 .cards{left:6cqw;right:6cqw;width:auto;top:auto;bottom:5cqw;transform:none;gap:3cqw}.p2 .cd i{height:8cqw}.p2 .cd div{padding:1.8cqw 2.4cqw}.p2 .cd b{font-size:4cqw}.p2 .cd span{font-size:3.2cqw}}
''',
 lambda: f'''<div class="kx p2">{doodles(5, [(4,10,6),(30,88,5),(46,10,5),(54,90,6),(12,92,5)])}{LOGO}{TB}
<div class="badge">中英對照<b>25+</b>素食用語</div>
<div class="cards">
<div class="cd"><i style="background-image:url({IMG['egg']})"></i><div><b>Vegetarian</b><span>素食者</span></div></div>
<div class="cd"><i style="background-image:url({IMG['vegan']})"></i><div><b>Vegan</b><span>純素（全素）</span></div></div>
<div class="cd"><i style="background-image:url({IMG['wx']})"></i><div><b>Flexitarian</b><span>彈性素食者</span></div></div>
<div class="cd no"><i style="background-image:url({IMG['milk']})"></i><div><b>Pescatarian</b><span>海鮮素者（非素食）</span></div></div>
</div></div>'''),

('P3｜海報＋點餐對話',
 '同一海報排版，右邊是餐廳點餐的對話氣泡（英文＋中文），配一個圓形相片，突出「點餐英文」的實用賣點，最活潑。',
 '''
.p3 .chat{position:absolute;right:4cqw;top:12cqw;z-index:4;width:36cqw;display:flex;flex-direction:column;gap:1.6cqw}
.p3 .bb{max-width:33cqw;padding:1.3cqw 1.9cqw;border-radius:2.2cqw;box-shadow:0 .8cqw 1.8cqw rgba(90,60,30,.2)}
.p3 .bb b{display:block;font:700 1.9cqw/1.3 Georgia,serif;color:#1A1A1A}.p3 .bb small{display:block;margin-top:.3cqw;font:700 1.3cqw/1.3 -apple-system,"PingFang HK",sans-serif;color:#7a6a50}
.p3 .bb.you{align-self:flex-start;background:#fff;border-bottom-left-radius:.4cqw}.p3 .bb.me{align-self:flex-end;background:#FFE08A;border-bottom-right-radius:.4cqw}
.p3 .ph{position:absolute;right:30cqw;bottom:-4cqw;z-index:2;width:17cqw;height:17cqw;border-radius:50%;background:center/cover;border:.6cqw solid #fff;box-shadow:0 1cqw 2cqw rgba(90,60,30,.2)}
.p3 .badge{left:35cqw;top:5cqw}
@media(max-width:640px){.p3 .chat{left:6cqw;right:6cqw;width:auto;top:auto;bottom:5cqw;gap:2.4cqw}.p3 .bb{max-width:74cqw;padding:2cqw 3cqw}.p3 .bb b{font-size:3.6cqw}.p3 .bb small{font-size:2.5cqw}.p3 .ph{display:none}}
''',
 lambda: f'''<div class="kx p3">{doodles(7, [(4,10,6),(30,88,5),(46,10,5),(12,92,5)])}{LOGO}{TB}
<div class="badge">中英對照<b>25+</b>素食用語</div>
<i class="ph" style="background-image:url({IMG['vegan']})"></i>
<div class="chat">
<div class="bb you"><b>Do you have any vegetarian options?</b><small>有素食選擇嗎？</small></div>
<div class="bb me"><b>I'm vegan — no egg or dairy, please.</b><small>我吃純素，請不要蛋奶。</small></div>
<div class="bb you"><b>Could you make it without garlic?</b><small>可以走蒜嗎？</small></div>
</div></div>'''),
]

secs = []
for t, d, css, mk in OPTS:
    doc = (f'<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
           f'<style>body{{margin:0;padding:20px 14px;background:#fff}}{BASE}{css}</style></head><body>{mk()}</body></html>')
    secs.append(f'<section class="opt"><h3>{t}</h3><p>{d}</p><div class="pair"><div><small>桌面</small>'
                f'<iframe srcdoc="{html.escape(doc)}" style="width:880px;height:540px"></iframe></div>'
                f'<div><small>手機</small><iframe srcdoc="{html.escape(doc)}" style="width:390px;height:560px"></iframe></div></div></section>')
page = f'''<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>B6 KV 方案</title>
<style>body{{margin:0;background:#EEF1EA;color:#222;font:15px/1.6 {FONT}}}.wrap{{max-width:1340px;margin:0 auto;padding:24px 16px 60px}}
.opt{{margin:0 0 34px}}.opt h3{{margin:0 0 4px;font-size:18px}}.opt p{{margin:0 0 10px;color:#555;font-size:14px}}
.pair{{display:flex;gap:16px;flex-wrap:wrap;align-items:flex-start}}.pair small{{display:block;font-weight:700;color:#7a6a45;margin:0 0 4px}}iframe{{border:1px solid #ddd;background:#fff;border-radius:8px}}</style></head>
<body><div class="wrap"><h1 style="font-size:22px">B6 KV 方案（參考展覽海報風格，3 款）</h1>{''.join(secs)}</div></body></html>'''
open(os.path.join(HERE, '..', 'kv-b6-options.html'), 'w', encoding='utf-8').write(page)
print('ok')
