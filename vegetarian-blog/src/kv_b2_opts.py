# B2 KV 標題設計方案（媒體文章風格，3 款）→ ../kv-b2-options.html
import os
from kv_fresh import LOGO
from brush import brush
HERE = os.path.dirname(os.path.abspath(__file__))
PX = 'https://images.pexels.com/photos/{0}/pexels-photo-{0}.jpeg?auto=compress&cs=tinysrgb&w=700'
COLS = [(7118901, '🥚 蛋奶素', '吃蛋、奶'), (36183642, '🥛 奶素', '吃奶、不吃蛋'),
        (17140078, '🧄 五辛素', '可吃蔥、蒜、韭'), (6157094, '🌱 純素', '只吃植物')]
GRID = '<div class="g">' + ''.join(f'<div style="background-image:url({PX.format(i)})"><span>{a}<small>{b}</small></span></div>' for i, a, b in COLS) + '</div>'
import re as _re
_NAME = lambda a: _re.sub(r'^\S+\s', '', a)
GRID_B = '<div class="g gb">' + ''.join(f'<div style="background-image:url({PX.format(i)})"><span><i>0{n+1}</i><b>{_NAME(a)}</b><small>{b}</small></span></div>' for n, (i, a, b) in enumerate(COLS)) + '</div>'
GRID_C = '<div class="g gc">' + ''.join(f'<div style="background-image:url({PX.format(i)})"><span><b>{_NAME(a)}</b><small>{b}</small></span></div>' for i, a, b in COLS) + '</div>'

CLR = ['#E9A400', '#3C8FCB', '#E8743B', '#2F8F4E']   # 蛋奶素 黃／奶素 藍／五辛素 橙／純素 綠
def GRID_BR(cls, styles):
    return f'<div class="g {cls}">' + ''.join(f'<div style="background-image:url({PX.format(i)})"><span style="background-image:{styles[n]}"><b>{_NAME(a)}</b><small>{b}</small></span></div>' for n, (i, a, b) in enumerate(COLS)) + '</div>'
GRID_D = GRID_BR('gd', [brush(c, seed=n+3, opacity=.93) for n, c in enumerate(CLR)])
GRID_E = GRID_BR('ge', [brush('#1F5A3A', seed=n+11, dry=True) for n in range(4)])
GRID_F = GRID_BR('gf', [brush('#F7CE46', seed=n+21, opacity=.95) for n in range(4)])
KICK_D = brush('#2F8F4E', seed=40, opacity=.95); EM_D = brush('#F7CE46', seed=41, opacity=.75)
KICK_E = brush('#1F5A3A', seed=42, dry=True); EM_E = brush('#E8743B', seed=43, dry=True, opacity=.85)
KICK_F = brush('#F7CE46', seed=44); EM_F = brush('#F7CE46', seed=45, opacity=.7)
def M1B(grid, kick, em, k):
    return f'''<div class="kv m1 {k}"><style>.{k} .kick b{{background-image:{kick}}}.{k} h2 em{{background-image:{em}}}</style>{grid}{LOGO}<div class="tb">
 <p class="kick"><b>素食新手入門</b><i></i>2026</p>
 <h2>聚會有朋友吃素？<br>新手一表看懂<em>素食種類</em></h2>
 <p class="dek">蛋奶素、奶素、五辛素、純素……<br>10 種吃法一次看清！</p>
 <p class="by">文：Kitchen AO 編輯部</p></div></div>'''

KW = '<p class="kw">' + ''.join(f'<span>#{w}</span>' for w in ['素食種類', '蛋奶素', '奶素', '五辛素', '純素']) + '</p>'

OPTS = [
('M1-D｜水彩筆刷・四色分類', '每類一種顏色的筆刷底（蛋奶素黃、奶素藍、五辛素橙、純素綠），白字；「素食新手入門」及「素食種類」亦加筆刷，活潑易分辨。', M1B(GRID_D, KICK_D, EM_D, 'kd')),
('M1-E｜乾筆粗刷・品牌深綠', '統一深綠色乾筆刷（有飛白紋理），白字；「素食種類」用橙色乾筆刷襯底，較有手作質感、整體統一。', M1B(GRID_E, KICK_E, EM_E, 'ke')),
('M1-F｜黃色螢光筆刷', '黃色筆刷似螢光筆劃過，深綠字；與標題「素食種類」的黃色筆刷呼應，清新、最似雜誌重點標記。', M1B(GRID_F, KICK_F, EM_F, 'kf')),
]

CSS = '''
*{box-sizing:border-box}body{margin:0;background:#EEF1EA;font-family:-apple-system,"PingFang HK","Microsoft JhengHei",Arial,sans-serif;color:#2b2b2b}
.wrap{max-width:1100px;margin:0 auto;padding:24px 16px 60px}.wrap>h1{font-size:22px;margin:0 0 6px}
.opt{margin:0 0 34px}.opt h3{margin:0 0 4px;font-size:18px}.opt>p{margin:0 0 10px;font-size:14px;color:#555}
.kv{position:relative;width:100%;aspect-ratio:16/9;container-type:inline-size;overflow:hidden;background:#fff}
.g{position:absolute;top:0;right:0;bottom:0;width:45%;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:.5cqw;background:#fff}
.g>div{position:relative;background-size:cover;background-position:center}
.g span{position:absolute;left:50%;bottom:2cqw;transform:translateX(-50%);white-space:nowrap;background:#fff;color:#1F5A3A;font-weight:900;font-size:1.7cqw;line-height:1.3;padding:.45cqw 1.4cqw;border-radius:3cqw;border:.25cqw solid #3F9D5A;box-shadow:0 .6cqw 1.4cqw rgba(0,0,0,.25);text-align:center}
.g span small{display:block;font-size:1.05cqw;font-weight:700;color:#5a7a63}
.logo2{position:absolute;right:1.8cqw;top:1.8cqw;z-index:5;display:inline-flex;align-items:center;height:4.3cqw;background:#fff;border:.25cqw solid #DCEFD6;border-radius:3cqw;padding:0 1.8cqw}.logo2 .li{height:2.3cqw;width:auto}.logo2 .lt{height:2cqw;width:auto;margin-left:1cqw}
.tb{position:absolute;left:4.5cqw;top:50%;transform:translateY(-50%);width:46cqw}
.tb h2{margin:0;font-weight:900;white-space:nowrap}
.kw{margin:1.8cqw 0 0;display:flex;flex-wrap:wrap;gap:.8cqw}.kw span{font-size:1.5cqw;font-weight:700;border-radius:3cqw;padding:.3cqw 1.1cqw}
/* M1 雜誌 */
.m1{background:#FBFAF6}
.m1 .kick{display:flex;align-items:center;gap:1.2cqw;margin:0 0 1.8cqw;font-size:1.5cqw;letter-spacing:.3cqw;color:#7a7a7a}.m1 .kick b{color:#2C6E49}.m1 .kick i{flex:0 0 6cqw;height:.15cqw;background:#2C6E49}
.m1 h2{font-family:"Noto Serif TC","Songti TC","PMingLiU",serif;font-size:3.7cqw;line-height:1.3;color:#1A1A1A;letter-spacing:.1cqw}
.m1 h2 em{font-style:normal;color:#2C6E49;border-bottom:.35cqw solid #F7CE46}
.m1 .dek{margin:2cqw 0 0;padding-left:1.4cqw;border-left:.35cqw solid #3F9D5A;font-size:1.9cqw;line-height:1.6;color:#4a4a4a}
.m1 .by{margin:2.4cqw 0 0;font-size:1.3cqw;color:#8a8a8a;letter-spacing:.15cqw}
/* M2 色塊 */
.m2{background:#1F5A3A}.m2 .tb{color:#fff}
.m2 .lab{display:inline-flex;align-items:center;margin:0 0 2cqw;font-size:1.6cqw;font-weight:700;background:#fff;color:#1F5A3A;border-radius:.4cqw;overflow:hidden}.m2 .lab b{background:#F7CE46;color:#1A1A1A;padding:.4cqw 1.2cqw;margin-right:1.2cqw}.m2 .lab{padding-right:1.4cqw}
.m2 h2{font-size:3.7cqw;line-height:1.32}
.m2 h2 em{font-style:normal;background:linear-gradient(transparent 62%,rgba(247,206,70,.85) 62%);color:#fff;padding:0 .3cqw}
.m2 .dek{margin:2cqw 0 0;font-size:1.8cqw;line-height:1.6;color:#D7EBDD}
.m2 .kw span{color:#fff;border:.15cqw solid rgba(255,255,255,.55)}
/* M3 大數字 */
.m3{background:#F6FAF2}
.m3 .kick{margin:0 0 1.6cqw;padding-bottom:1cqw;border-bottom:.15cqw solid #1F5A3A;font-size:1.5cqw;color:#2C6E49;letter-spacing:.2cqw}
.m3 h2{font-size:3.4cqw;line-height:1.3;color:#1F5A3A}.m3 h2 em{font-style:normal;color:#E8743B}
.m3 .big{display:flex;align-items:center;gap:1.4cqw;margin:1.6cqw 0 0;padding:.6cqw 0 1cqw;border-bottom:.15cqw solid #1F5A3A}
.m3 .big b{font-size:9cqw;line-height:.9;font-weight:900;color:#E8743B;letter-spacing:-.3cqw}
.m3 .big span{font-size:2.6cqw;font-weight:900;color:#1F5A3A;line-height:1.3}.m3 .big small{display:block;font-size:1.4cqw;font-weight:700;color:#5a7a63;margin-top:.4cqw}
.m3 .kw span{color:#2C6E49;background:#fff;border:.15cqw solid #CFE8CD}
.m1 .kw span{color:#2C6E49;border:.15cqw solid #CFE8CD;background:#fff}

/* 標籤 B：雜誌圖說條 */
.gb span{left:0;right:0;bottom:0;transform:none;border:0;border-radius:0;box-shadow:none;background:rgba(255,255,255,.88);backdrop-filter:blur(2px);display:flex;align-items:baseline;gap:.8cqw;padding:.8cqw 1.4cqw;text-align:left;color:#1A1A1A}
.gb span i{font-style:normal;font-family:Georgia,serif;font-size:1.5cqw;color:#3F9D5A;font-weight:700}
.gb span b{font-family:"Noto Serif TC","Songti TC","PMingLiU",serif;font-size:1.8cqw}
.gb span small{display:inline;font-size:1.05cqw;color:#666;font-weight:500;margin-left:auto}
/* 標籤 C：左上角色塊 */
.gc span{left:1.2cqw;top:auto;bottom:1.2cqw;transform:none;border:0;border-radius:.3cqw;background:#1F5A3A;color:#fff;box-shadow:0 .4cqw 1cqw rgba(0,0,0,.2);text-align:left;padding:.6cqw 1.2cqw}
.gc span b{font-size:1.7cqw;letter-spacing:.1cqw}
.gc span small{color:#CFE8CD;font-size:1.05cqw;margin-top:.2cqw}

/* 筆刷標籤共用 */
.gd span,.ge span,.gf span{left:.6cqw;bottom:1.4cqw;transform:rotate(-2deg);border:0;border-radius:0;box-shadow:none;background:none no-repeat center/100% 100%;padding:.9cqw 3.6cqw 1cqw 3.2cqw;text-align:left;filter:drop-shadow(0 .3cqw .5cqw rgba(0,0,0,.18))}
.gd span b,.ge span b,.gf span b{display:block;font-size:2.2cqw;letter-spacing:.15cqw}
.gd span small,.ge span small,.gf span small{font-size:1.2cqw;margin-top:.1cqw}
.gd span,.ge span{color:#fff}.gd span small,.ge span small{color:rgba(255,255,255,.92)}
.gf span{color:#1F5A3A}.gf span small{color:#3d5a45}
.m1 .kick b{background:none no-repeat center/100% 100%}
.kd .kick b,.ke .kick b{color:#fff;padding:.5cqw 2.8cqw .6cqw}
.kf .kick b{color:#1F5A3A;padding:.5cqw 2.8cqw .6cqw}
.kd h2 em,.ke h2 em,.kf h2 em{border:0;background:none no-repeat center 70%/104% 62%;padding:0 1.6cqw;margin:0 -1.2cqw}
.ke h2 em{color:#1F5A3A}
'''
html = f'''<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>B2 KV 標題設計方案</title><style>{CSS}</style></head><body><div class="wrap">
<h1>B2 KV｜M1 雜誌專題式：筆刷標籤 3 款</h1>
{''.join(f'<section class="opt"><h3>{t}</h3><p>{d}</p>{h}</section>' for t, d, h in OPTS)}
</div></body></html>'''
open(os.path.join(HERE, '..', 'kv-b2-options.html'), 'w', encoding='utf-8').write(html)
print('ok')
