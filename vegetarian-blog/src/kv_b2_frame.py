# B2 KV 外框方案（3 款）：似素食餐牌的邊線 → ../kv-b2-frame-options.html
import os, html, urllib.parse
import kv_mag
HERE = os.path.dirname(os.path.abspath(__file__))
PX = 'https://images.pexels.com/photos/{0}/pexels-photo-{0}.jpeg?auto=compress&cs=tinysrgb&w=700'
COLS = [(PX.format(7118901), '蛋奶素', '吃蛋、奶'), (PX.format(36183642), '奶素', '吃奶、不吃蛋'),
        (PX.format(17140078), '五辛素', '可吃蔥、蒜、韭'), (PX.format(6157094), '純素', '只吃植物')]
TTL = '聚會有朋友吃素？<br>新手一表看懂<em>素食分類天書</em>'
svg = lambda s: "url(\"data:image/svg+xml," + urllib.parse.quote(s) + "\")"

# 葉仔角花（左上角方向，其餘三角用 transform 翻轉）
LEAF = svg('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120"><g fill="none" stroke="#2F8F4E" stroke-width="3" stroke-linecap="round">'
           '<path d="M10 70 Q10 10 70 10"/><path d="M18 64 Q20 22 64 18" stroke-width="1.6" opacity=".7"/></g>'
           '<g fill="#3F9D5A"><path d="M70 10 q14 -10 30 -4 q-12 14 -30 4z"/><path d="M10 70 q-10 14 -4 30 q14 -12 4 -30z"/>'
           '<path d="M34 26 q4 -16 20 -20 q-2 16 -20 20z" fill="#7DBB6B"/><path d="M26 34 q-16 4 -20 20 q16 -2 20 -20z" fill="#7DBB6B"/></g>'
           '<circle cx="22" cy="22" r="5" fill="#E8743B"/></svg>')
# 葉仔圖案（花邊用）
VINE = svg('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 60 60"><g fill="#3F9D5A" opacity=".85">'
           '<path d="M8 30 q8 -14 22 -10 q-8 12 -22 10z"/><path d="M52 30 q-8 14 -22 10 q8 -12 22 -10z" fill="#7DBB6B"/></g>'
           '<circle cx="30" cy="30" r="2.6" fill="#E9A400"/></svg>')

OPTS = [
('A｜餐牌雙線框＋葉仔角花',
 '外層淺綠粗框，內層深綠細線，四角加葉仔角花及小番茄點綴，似西式餐廳的素食餐牌，最簡潔。',
 'fa', f'''
.ao-mkv.fa .kv{{border:0;border-radius:4px;box-shadow:0 0 0 6px #E3F1DC}}
.ao-mkv.fa .kv:after{{content:"";position:absolute;inset:1.1cqw;border:.22cqw solid #2F8F4E;outline:.12cqw solid #2F8F4E;outline-offset:-.7cqw;pointer-events:none;z-index:6}}
.ao-mkv.fa .kv .cn{{position:absolute;width:7cqw;height:7cqw;background:{LEAF} no-repeat center/contain;z-index:7;pointer-events:none}}
.ao-mkv.fa .kv .cn.tl{{left:.4cqw;top:.4cqw}}.ao-mkv.fa .kv .cn.tr{{right:.4cqw;top:.4cqw;transform:scaleX(-1)}}
.ao-mkv.fa .kv .cn.bl{{left:.4cqw;bottom:.4cqw;transform:scaleY(-1)}}.ao-mkv.fa .kv .cn.br{{right:.4cqw;bottom:.4cqw;transform:scale(-1)}}
.ao-mkv.fa .kv .logo2{{right:3cqw;top:3cqw}}.ao-mkv.fa .kv .tb{{left:6cqw}}
'''),
('B｜葉仔花邊框',
 '外框是一圈葉仔圖案（淺綠底＋綠葉＋黃點），好似素食餐牌的花邊，在白色 blog 首頁上最突出。',
 'fb', f'''
.ao-mkv.fb{{padding:24px;border-radius:14px;background:#E6F3DF {VINE} repeat;background-size:28px 28px;box-shadow:inset 0 0 0 2px #BFE0B3}}
.ao-mkv.fb .kv{{border:0;border-radius:6px;box-shadow:0 0 0 3px #fff,0 4px 14px rgba(31,90,58,.18)}}
@media(max-width:640px){{.ao-mkv.fb{{padding:16px;background-size:22px 22px}}}}
'''),
('C｜牛皮紙餐牌＋「VEGETARIAN MENU」頂牌',
 '牛皮紙色外框配綠色虛線車邊，頂部中間掛一塊「VEGETARIAN MENU · 素食餐牌」小牌，似咖啡店手寫餐牌，最有主題感。',
 'fc', '''
.ao-mkv.fc{position:relative;padding:22px 14px 14px;border-radius:12px;background:#EBDDBF;background-image:radial-gradient(rgba(120,90,40,.10) 1px,transparent 1.2px);background-size:7px 7px;box-shadow:inset 0 0 0 2px #D4C09A}
.ao-mkv.fc:before{content:"";position:absolute;inset:7px;border:2px dashed #3F9D5A;border-radius:9px;pointer-events:none}
.ao-mkv.fc .tag{position:absolute;left:50%;top:-12px;transform:translateX(-50%);z-index:8;background:#2F8F4E;color:#fff;font:800 12px/1 -apple-system,"PingFang HK",Arial,sans-serif;letter-spacing:2px;padding:7px 16px;border-radius:4px;box-shadow:0 2px 0 #1F5A3A;white-space:nowrap}
.ao-mkv.fc .tag:before,.fc .tag:after{content:"🌿";margin:0 6px;letter-spacing:0}
.ao-mkv.fc .kv{border:0;border-radius:6px;box-shadow:0 3px 10px rgba(90,60,20,.18)}
@media(max-width:640px){.ao-mkv.fc{padding:20px 10px 10px}.ao-mkv.fc .tag{font-size:10.5px;padding:6px 10px}}
'''),
]

def build(cls, css):
    h = kv_mag.block(COLS, 'div', ttl=TTL).replace('class="ao-mkv"', f'class="ao-mkv {cls}"', 1)
    if cls == 'fa':
        h = h.replace('<div class="kv">', '<div class="kv"><i class="cn tl"></i><i class="cn tr"></i><i class="cn bl"></i><i class="cn br"></i>', 1)
    if cls == 'fc':
        h = h.replace('<div class="kv">', '<span class="tag">VEGETARIAN MENU · 素食餐牌</span><div class="kv">', 1)
    return f'<style>{css}</style>' + h

secs = []
for t, d, cls, css in OPTS:
    blk = build(cls, css)
    doc = f'<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body style="margin:0;padding:18px 12px;background:#fff">{blk}</body></html>'
    secs.append(f'<section class="opt"><h3>{t}</h3><p>{d}</p><div class="pair"><div><small>桌面（白色 blog 背景）</small>'
                f'<iframe srcdoc="{html.escape(doc)}" style="width:860px;height:580px"></iframe></div>'
                f'<div><small>手機</small><iframe srcdoc="{html.escape(doc)}" style="width:390px;height:600px"></iframe></div></div></section>')

page = f'''<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>B2 KV 外框方案</title>
<style>body{{margin:0;background:#EEF1EA;color:#222;font:15px/1.6 -apple-system,"PingFang HK",Arial,sans-serif}}.wrap{{max-width:1320px;margin:0 auto;padding:24px 16px 60px}}
.opt{{margin:0 0 34px}}.opt h3{{margin:0 0 4px;font-size:18px}}.opt p{{margin:0 0 10px;color:#555;font-size:14px}}
.pair{{display:flex;gap:16px;flex-wrap:wrap;align-items:flex-start}}.pair small{{display:block;font-weight:700;color:#7a6a45;margin:0 0 4px}}iframe{{border:1px solid #ddd;background:#fff;border-radius:8px}}</style></head>
<body><div class="wrap"><h1 style="font-size:22px">B2 KV｜素食餐牌外框 3 款</h1>{''.join(secs)}</div></body></html>'''
open(os.path.join(HERE, '..', 'kv-b2-frame-options.html'), 'w', encoding='utf-8').write(page)
print('ok')
