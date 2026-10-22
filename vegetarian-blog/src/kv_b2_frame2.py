# B2 KV 外框方案 v2（較豐富的素食餐牌設計，3 款）→ ../kv-b2-frame-options-v2.html
# 所有插圖均為自繪 SVG（原創），無使用素材
import os, html, urllib.parse, random
import kv_mag
HERE = os.path.dirname(os.path.abspath(__file__))
PX = 'https://images.pexels.com/photos/{0}/pexels-photo-{0}.jpeg?auto=compress&cs=tinysrgb&w=700'
COLS = [(PX.format(7118901), '蛋奶素', '吃蛋、奶'), (PX.format(36183642), '奶素', '吃奶、不吃蛋'),
        (PX.format(17140078), '五辛素', '可吃蔥、蒜、韭'), (PX.format(6157094), '純素', '只吃植物')]
TTL = '聚會有朋友吃素？<br>新手一表看懂<em>素食分類天書</em>'
U = lambda s: "url('data:image/svg+xml," + urllib.parse.quote(s) + "')"

# ---------- 自繪蔬菜 icon（彩色版／粉筆版） ----------
def veg(name, chalk=False):
    S = '#FFFFFF' if chalk else '#2B5B3C'
    f = (lambda c: 'none') if chalk else (lambda c: c)
    sw = 2.4 if chalk else 2
    g = {
     'carrot': f'<path d="M14 40 L30 18 Q34 14 38 18 Q42 22 38 26 Z" fill="{f("#F08A3C")}"/><path d="M22 30 l4 3 M26 25 l4 3 M18 35 l3 2"/><path d="M34 16 q-2 -8 -8 -10 M36 16 q2 -8 8 -10 M37 18 q6 -4 10 -2" fill="none"/>',
     'tomato': f'<circle cx="24" cy="27" r="13" fill="{f("#E5533D")}"/><path d="M24 14 l-5 -4 M24 14 l5 -4 M24 14 l-7 2 M24 14 l7 2 M24 14 v-6" fill="none"/><path d="M15 25 q2 -5 6 -6" fill="none" opacity=".6"/>',
     'mushroom': f'<path d="M8 24 Q10 8 24 8 Q38 8 40 24 Z" fill="{f("#C98B5A")}"/><path d="M18 24 L17 40 Q24 43 31 40 L30 24" fill="{f("#F3E3C7")}"/><circle cx="18" cy="16" r="2.2" fill="{f("#F3E3C7")}"/><circle cx="29" cy="14" r="2.6" fill="{f("#F3E3C7")}"/>',
     'broccoli': f'<path d="M20 28 L18 42 L30 42 L28 28" fill="{f("#8CC06B")}"/><circle cx="16" cy="22" r="7" fill="{f("#3F9D5A")}"/><circle cx="32" cy="22" r="7" fill="{f("#3F9D5A")}"/><circle cx="24" cy="15" r="8" fill="{f("#4FAE68")}"/>',
     'leaf': f'<path d="M8 40 Q8 10 40 8 Q40 38 8 40 Z" fill="{f("#7DBB6B")}"/><path d="M8 40 L32 16 M16 32 l-2 -8 M22 26 l-1 -8 M20 30 l8 1 M26 24 l8 0" fill="none"/>',
     'pea': f'<path d="M6 30 Q12 14 30 12 Q42 12 42 18 Q38 32 18 36 Q8 38 6 30 Z" fill="{f("#9CCB6E")}"/><circle cx="16" cy="27" r="3.4" fill="{f("#5FA14A")}"/><circle cx="24" cy="23" r="3.4" fill="{f("#5FA14A")}"/><circle cx="32" cy="19" r="3.4" fill="{f("#5FA14A")}"/><path d="M42 18 q4 -4 2 -10" fill="none"/>',
     'eggplant': f'<path d="M30 12 Q42 18 36 32 Q30 44 16 42 Q6 38 12 28 Q18 22 22 16 Q26 10 30 12 Z" fill="{f("#7C4E9E")}"/><path d="M28 12 q2 -6 8 -6 M27 13 q-6 0 -6 6 M30 12 q6 2 6 8" fill="{f("#5FA14A")}"/>',
     'corn': f'<path d="M24 6 Q34 14 32 30 Q30 40 24 42 Q18 40 16 30 Q14 14 24 6 Z" fill="{f("#F5C83A")}"/><path d="M18 18 h12 M17 24 h14 M18 30 h12 M24 8 v32" fill="none" opacity=".55"/><path d="M16 30 Q8 34 12 44 Q18 38 22 42 M32 30 Q40 34 36 44 Q30 38 26 42" fill="{f("#7DBB6B")}"/>',
    }[name]
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><g stroke="{S}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{g}</g></svg>'

NAMES = ['carrot', 'tomato', 'leaf', 'mushroom', 'broccoli', 'pea', 'corn', 'eggplant']

def scatter(seed, chalk=False, n_top=9, n_side=3, gap=(0,0), ty=4.2, sx=3.0):
    """沿邊框擺放 icon：回傳 (left%, top%, size, rot, svg) 清單"""
    r = random.Random(seed); out = []; k = 0
    for i in range(n_top):          # 上、下兩行
        x = 3 + i * (94 / (n_top - 1))
        for y in (ty, 100 - ty):
            if y < 50 and gap[0] < x < gap[1]: continue
            out.append((x + r.uniform(-1.5, 1.5), y, r.uniform(.85, 1.15), r.uniform(-28, 28), NAMES[k % 8])); k += 3
    for j in range(n_side):         # 左、右兩邊
        y = 22 + j * (56 / max(1, n_side - 1))
        for x in (sx, 100 - sx):
            out.append((x, y + r.uniform(-3, 3), r.uniform(.85, 1.1), r.uniform(-30, 30), NAMES[k % 8])); k += 5
    return ''.join(f'<i class="vg" style="left:{x:.1f}%;top:{y:.1f}%;--s:{s:.2f};transform:translate(-50%,-50%) rotate({a:.0f}deg) scale(var(--s));background-image:{U(veg(nm, chalk))}"></i>' for x, y, s, a, nm in out)

LEAFC = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200"><g stroke="#2B5B3C" stroke-width="1.6" stroke-linejoin="round">' + ''.join(
    f'<path transform="rotate({a} 100 100) translate({dx} 0)" d="M100 100 Q118 70 150 66 Q140 98 100 100 Z" fill="{c}"/>'
    for a, dx, c in [(-10, 0, '#3F9D5A'), (25, 6, '#7DBB6B'), (60, 0, '#4FAE68'), (95, 8, '#9CCB6E'), (130, 0, '#3F9D5A'),
                     (165, 4, '#7DBB6B'), (200, 0, '#5FA14A'), (235, 10, '#9CCB6E'), (-45, 12, '#4FAE68')]) + \
    '</g><circle cx="100" cy="100" r="9" fill="#E5533D" stroke="#2B5B3C" stroke-width="1.6"/><circle cx="122" cy="118" r="6" fill="#F5C83A" stroke="#2B5B3C" stroke-width="1.6"/></svg>'

OPTS = [
('D｜手繪蔬菜插畫邊框',
 '米白餐牌紙，四邊圍滿自繪蔬菜插畫（紅蘿蔔、番茄、西蘭花、蘑菇、豆莢、粟米、茄子、葉），內框雙線，似精緻的插畫素食餐牌。',
 'fd', f'''
.ao-mkv.fd{{position:relative;padding:5.2% 5.6%;background:#FBF6EA;border-radius:14px;box-shadow:inset 0 0 0 2px #E2D6BB,0 6px 20px rgba(60,80,40,.12)}}
.ao-mkv.fd .kv{{border:0;border-radius:4px;box-shadow:0 0 0 3px #FBF6EA,0 0 0 4.5px #2F8F4E,0 0 0 8px #FBF6EA,0 0 0 9px #2F8F4E}}
.ao-mkv.fd .vg{{position:absolute;width:clamp(26px,4.6%,48px);aspect-ratio:1;background:no-repeat center/contain;z-index:3;pointer-events:none}}
.ao-mkv.fd .ttlbar{{position:absolute;left:50%;top:0;transform:translate(-50%,-50%);z-index:5;background:#2F8F4E;color:#fff;font:800 13px/1 -apple-system,"PingFang HK",Arial,sans-serif;letter-spacing:3px;padding:8px 22px;border-radius:30px;border:3px solid #FBF6EA;white-space:nowrap}}
@media(max-width:640px){{.ao-mkv.fd{{padding:9% 7%}}.ao-mkv.fd .vg{{width:26px}}.ao-mkv.fd .ttlbar{{font-size:11px;padding:6px 14px;letter-spacing:2px}}}}
''', lambda: scatter(7, gap=(28, 72)) + '<span class="ttlbar">🌿 VEGETARIAN MENU · 素食餐牌 🌿</span>'),
('E｜黑板餐牌＋粉筆插畫',
 '木框黑板（深綠），四周粉筆手繪蔬菜，上方粉筆字「Today\'s Veggie Menu」，KV 好似用膠紙貼在黑板上的餐牌，最有咖啡店感覺。',
 'fe', '''
.ao-mkv.fe{position:relative;padding:8.5% 6% 5.5%;border-radius:10px;background:#2F4A3B;background-image:radial-gradient(rgba(255,255,255,.05) 1px,transparent 1.5px),radial-gradient(ellipse at 30% 20%,rgba(255,255,255,.08),transparent 60%);background-size:5px 5px,100% 100%;border:12px solid #8A5A32;box-shadow:inset 0 0 0 2px #6E4523,inset 0 0 30px rgba(0,0,0,.35),0 8px 22px rgba(0,0,0,.25)}
.ao-mkv.fe .vg{position:absolute;width:clamp(24px,4.4%,46px);aspect-ratio:1;background:no-repeat center/contain;z-index:1;opacity:.82;pointer-events:none}
.ao-mkv.fe .chalk{position:absolute;left:50%;top:4.2%;transform:translate(-50%,-50%) rotate(-2deg);z-index:2;color:#F6F1E3;font:400 clamp(16px,3.2vw,30px)/1 "Chalkboard SE","Marker Felt","Comic Sans MS",cursive;white-space:nowrap;text-shadow:0 0 1px rgba(255,255,255,.6)}
.ao-mkv.fe .chalk small{font:700 .55em/1 -apple-system,"PingFang HK",sans-serif;letter-spacing:3px;margin-left:10px;color:#F5C83A}
.ao-mkv.fe .kv{border:0;border-radius:3px;transform:rotate(-.6deg);box-shadow:0 10px 24px rgba(0,0,0,.4);z-index:2}
.ao-mkv.fe .tape{position:absolute;z-index:6;width:11%;height:4.2%;background:rgba(240,228,190,.85);box-shadow:0 1px 2px rgba(0,0,0,.2)}
.ao-mkv.fe .tape.a{left:3.4%;top:7.4%;transform:rotate(-32deg)}.ao-mkv.fe .tape.b{right:3.4%;top:7.4%;transform:rotate(30deg)}
.ao-mkv.fe .tape.c{left:3.4%;bottom:2.6%;transform:rotate(28deg)}.ao-mkv.fe .tape.d{right:3.4%;bottom:2.6%;transform:rotate(-30deg)}
@media(max-width:640px){.ao-mkv.fe{padding:15% 6% 7%;border-width:8px}.ao-mkv.fe .vg{width:24px}.ao-mkv.fe .chalk{top:5.5%}.ao-mkv.fe .tape{width:16%;height:3%}.ao-mkv.fe .tape.a,.ao-mkv.fe .tape.b{top:10%}}
''', lambda: scatter(11, chalk=True, n_top=8, n_side=3, gap=(22, 78), ty=4.6, sx=3.2) + '<span class="chalk">Today\'s Veggie Menu<small>素食餐牌</small></span><i class="tape a"></i><i class="tape b"></i><i class="tape c"></i><i class="tape d"></i>'),
('F｜花環絲帶餐牌',
 '綠色卡紙配白色虛線車邊，左上及右下角有一大束手繪葉仔花環（配番茄、粟米點綴），頂部是摺邊絲帶「素食餐牌 VEGETARIAN MENU」，似節慶餐牌，最搶眼。',
 'ff', f'''
.ao-mkv.ff{{position:relative;padding:7% 4.5% 4.5%;--sc:#3F9D5A;background:radial-gradient(circle at 10px 10px,var(--sc) 10px,transparent 10.5px) -10px -10px/20px 20px,var(--sc);border-radius:6px;-webkit-mask:radial-gradient(circle 9px at 50% 0,#0000 98%,#000) 50% -9px/18px 100% repeat-x,radial-gradient(circle 9px at 50% 100%,#0000 98%,#000) 50% calc(100% + 9px)/18px 100% repeat-x;-webkit-mask-composite:source-in;mask-composite:intersect}}
.ao-mkv.ff:before{{content:"";position:absolute;inset:2.4% 1.8%;border:2px dashed rgba(255,255,255,.7);border-radius:6px;pointer-events:none}}
.ao-mkv.ff .kv{{border:0;border-radius:6px;box-shadow:0 0 0 5px #FBF6EA,0 10px 24px rgba(0,0,0,.25)}}
.ao-mkv.ff .wr{{position:absolute;width:24%;aspect-ratio:1;background:{U(LEAFC)} no-repeat center/contain;z-index:6;pointer-events:none;filter:drop-shadow(0 4px 6px rgba(0,0,0,.2))}}
.ao-mkv.ff .wr.a{{left:0;top:0;transform:rotate(-15deg)}}.ao-mkv.ff .wr.b{{right:0;bottom:0;transform:rotate(160deg);width:20%}}
.ao-mkv.ff .rb{{position:absolute;left:50%;top:3.4%;transform:translateX(-50%);z-index:7;background:#F5C83A;color:#1F5A3A;font:900 clamp(12px,1.7vw,16px)/1 -apple-system,"PingFang HK",Arial,sans-serif;letter-spacing:2px;padding:10px 26px;white-space:nowrap;box-shadow:0 3px 0 #C99A1E}}
.ao-mkv.ff .rb:before,.ao-mkv.ff .rb:after{{content:"";position:absolute;top:8px;width:22px;height:100%;background:#E2B229;z-index:-1}}
.ao-mkv.ff .rb:before{{left:-16px;clip-path:polygon(0 0,100% 0,100% 100%,0 100%,30% 50%)}}.ao-mkv.ff .rb:after{{right:-16px;clip-path:polygon(0 0,100% 0,70% 50%,100% 100%,0 100%)}}
@media(max-width:640px){{.ao-mkv.ff{{padding:13% 5% 6%}}.ao-mkv.ff .wr{{width:30%}}.ao-mkv.ff .wr.b{{width:24%}}.ao-mkv.ff .rb{{top:3%;font-size:11px;padding:8px 16px}}}}
''', lambda: '<i class="wr a"></i><i class="wr b"></i><span class="rb">🌿 素食餐牌 VEGETARIAN MENU</span>'),
]

def build(cls, css, deco):
    h = kv_mag.block(COLS, 'div', ttl=TTL).replace('class="ao-mkv"', f'class="ao-mkv {cls}"', 1)
    h = h.replace('<div class="kv">', deco() + '<div class="kv">', 1)
    return f'<style>{css}</style>' + h

secs = []
for t, d, cls, css, deco in OPTS:
    blk = build(cls, css, deco)
    doc = f'<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body style="margin:0;padding:26px 14px;background:#fff">{blk}</body></html>'
    secs.append(f'<section class="opt"><h3>{t}</h3><p>{d}</p><div class="pair"><div><small>桌面（白色 blog 背景）</small>'
                f'<iframe srcdoc="{html.escape(doc)}" style="width:860px;height:600px"></iframe></div>'
                f'<div><small>手機</small><iframe srcdoc="{html.escape(doc)}" style="width:390px;height:640px"></iframe></div></div></section>')

page = f'''<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>B2 KV 外框方案 v2</title>
<style>body{{margin:0;background:#EEF1EA;color:#222;font:15px/1.6 -apple-system,"PingFang HK",Arial,sans-serif}}.wrap{{max-width:1320px;margin:0 auto;padding:24px 16px 60px}}
.opt{{margin:0 0 34px}}.opt h3{{margin:0 0 4px;font-size:18px}}.opt p{{margin:0 0 10px;color:#555;font-size:14px}}
.pair{{display:flex;gap:16px;flex-wrap:wrap;align-items:flex-start}}.pair small{{display:block;font-weight:700;color:#7a6a45;margin:0 0 4px}}iframe{{border:1px solid #ddd;background:#fff;border-radius:8px}}</style></head>
<body><div class="wrap"><h1 style="font-size:22px">B2 KV｜素食餐牌外框 v2（3 款）</h1>{''.join(secs)}</div></body></html>'''
open(os.path.join(HERE, '..', 'kv-b2-frame-options-v2.html'), 'w', encoding='utf-8').write(page)
print('ok')
