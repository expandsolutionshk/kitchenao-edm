# B2 KV 外框 D（手繪蔬菜插畫餐牌框）：wrap(html) 把 kv_mag.block 的輸出包上外框
import urllib.parse, random
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


CSS_D = f'''
.ao-mkv.fd{{position:relative;padding:5.2% 5.6%;background:#FBF6EA;border-radius:14px;box-shadow:inset 0 0 0 2px #E2D6BB,0 6px 20px rgba(60,80,40,.12)}}
.ao-mkv.fd .kv{{border:0;border-radius:4px;box-shadow:0 0 0 3px #FBF6EA,0 0 0 4.5px #2F8F4E,0 0 0 8px #FBF6EA,0 0 0 9px #2F8F4E}}
.ao-mkv.fd .vg{{position:absolute;width:clamp(26px,4.6%,48px);aspect-ratio:1;background:no-repeat center/contain;z-index:3;pointer-events:none}}
.ao-mkv.fd .ttlbar{{position:absolute;left:50%;top:0;transform:translate(-50%,-50%);z-index:5;background:#2F8F4E;color:#fff;font:800 13px/1 -apple-system,"PingFang HK",Arial,sans-serif;letter-spacing:3px;padding:8px 22px;border-radius:30px;border:3px solid #FBF6EA;white-space:nowrap}}
@media(max-width:640px){{.ao-mkv.fd{{padding:9% 7%}}.ao-mkv.fd .vg{{width:26px}}.ao-mkv.fd .ttlbar{{font-size:11px;padding:6px 14px;letter-spacing:2px}}}}
'''
def wrap(block_html, seed=7, n_top=6, n_side=2):
    deco = scatter(seed, n_top=n_top, n_side=n_side, gap=(28, 72)) + '<span class="ttlbar">🌿 VEGETARIAN BIBLE · 素食天書 🌿</span>'
    h = block_html.replace('class="ao-mkv"', 'class="ao-mkv fd"', 1).replace('<div class="kv">', deco + '<div class="kv">', 1)
    return '<style>' + ' '.join(l.strip() for l in CSS_D.splitlines() if l.strip()) + '</style>' + h
