# B1 素食到會 blog KV（3 款，1600×900）→ ../kv-options.html
# 參考野餐 blog KV：真實相片背景＋黑底黃字 tag＋白字黑描邊大標題＋白卡／拍立得＋Kitchen AO logo pill
import os, io, base64
from PIL import Image as _Im
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..', '..')

_src = _Im.open(os.path.join(ROOT, 'halloween-edm-2026', 'img', 'logo-header-pill.png'))
def _crop(box):
    b = io.BytesIO(); _src.crop(box).save(b, 'PNG'); return 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode()
LOGO = f'<span class="logo2" aria-label="Kitchen AO"><img class="li" src="{_crop((42,23,188,97))}" alt=""><img class="lt" src="{_crop((218,40,506,88))}" alt="Kitchen AO"></span>'

PX = 'https://images.pexels.com/photos/{0}/pexels-photo-{0}.jpeg?auto=compress&cs=tinysrgb&w=1600'
IMG = {
 'veg':   PX.format(5418661),   # Pexels：綠色背景上的番茄、粟米、蘑菇（俯拍）
 'bowl':  PX.format(7660437),   # Pexels：三碗蔬菜沙律（俯拍）
 'set':   'https://aoaodelivery.com/wp-content/uploads/2025/05/9ee996d5-e50c-4745-b847-86d8e179c481.jpg',  # Kitchen AO「素」味人生九宮格實拍
}
def img(k, cls='bg', alt=''):
    return f'<img class="{cls}" src="{IMG[k]}" alt="{alt}" referrerpolicy="no-referrer">'

TAG = '<span class="pill">香港素食到會推介 2026</span>'
TTL = '<h2 class="ttl"><span class="y">「素」味人生</span>健康到會套餐，<br>派對有素食朋友點安排？</h2>'
TICKS = ('<ul class="tks"><li><i>✔</i>小食、沙律、意粉、主菜任選</li>'
         '<li><i>✔</i>6–26 人套餐　$1,388 起</li>'
         '<li><i>✔</i>逢星期五落單 95 折</li></ul>')
SETCARD = f'<div class="rib3">{img("set","","Kitchen AO「素」味人生套餐")}<span>⭐「素」味人生套餐</span></div>'

KV = [
('A｜蔬菜實景主角',
 '綠色背景蔬菜俯拍做全幅背景，左邊 tag＋標題＋三個黃色剔，右下「素」味人生實拍白卡；最似野餐 KV 的版面。',
 f'''<div class="kv ka">{img('veg')}<div class="shade"></div>{LOGO}
  <div class="tb">{TAG}{TTL}{TICKS}</div>{SETCARD}</div>'''),
('B｜三圖拼貼',
 '三張實景並排（蔬菜、沙律、套餐），底部深色漸變，標題置中；三張相分別標上「新鮮蔬菜／清新沙律／素食套餐」。',
 f'''<div class="kv kb"><div class="tri">
   <div>{img('veg')}<span class="rl">🥕 新鮮蔬菜</span></div>
   <div>{img('bowl')}<span class="rl">🥗 清新沙律</span></div>
   <div>{img('set')}<span class="rl">🍝 素食套餐</span></div></div>
  <div class="shade"></div>{LOGO}
  <div class="tb">{TAG}{TTL}<p class="sub2">小食・沙律・意粉・主菜任選｜逢星期五落單 95 折</p></div></div>'''),
('C｜拍立得＋圓章',
 '沙律俯拍做背景，左邊標題，右邊兩張傾斜拍立得（蔬菜、套餐實拍），加黃色「星期五落單 95 折」圓章，較活潑。',
 f'''<div class="kv kc">{img('bowl')}<div class="shade"></div>{LOGO}
  <div class="tb">{TAG}{TTL}{TICKS}</div>
  <div class="pola"><figure class="p1">{img('veg','')}<figcaption>🥕 新鮮蔬菜</figcaption></figure>
   <figure class="p2">{img('set','')}<figcaption>🍝「素」味人生套餐</figcaption></figure></div>
  <div class="stamp"><b>星期五</b>落單<em>95折</em></div></div>'''),
]

CSS = '''
*{box-sizing:border-box}body{margin:0;background:#E9E5DC;font-family:-apple-system,"PingFang HK","Microsoft JhengHei",Arial,sans-serif;color:#3f3a33}
.wrap{max-width:1240px;margin:0 auto;padding:24px 16px 60px}.wrap>h1{font-size:22px;margin:0 0 4px}.wrap>p{margin:0 0 20px;color:#7a6a45;font-size:14px}
.opt{margin:0 0 34px}.opt h3{margin:0 0 4px;font-size:18px}.opt p{margin:0 0 10px;font-size:14px;color:#5a5348}
.kv{position:relative;width:100%;aspect-ratio:16/9;container-type:inline-size;overflow:hidden;border-radius:12px;background:#2C6E49;box-shadow:0 6px 24px rgba(0,0,0,.15)}
.kv img{display:block}.kv img.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.ttl{margin:0;font-size:4.9cqw;font-weight:900;line-height:1.22;color:#fff;-webkit-text-stroke:.55cqw #1A1A1A!important;paint-order:stroke fill;text-shadow:0 .5cqw 0 #1A1A1A;letter-spacing:.15cqw;white-space:nowrap}
.y{color:#F7CE46}
.pill{display:inline-block;background:#1A1A1A;color:#F7CE46;font-weight:900;font-size:2.2cqw;padding:.6cqw 2cqw;border-radius:4cqw;margin-bottom:1.4cqw}
.sub2{margin:1.6cqw 0 0;display:inline-block;background:#F7CE46;color:#1A1A1A;font-weight:900;font-size:1.9cqw;padding:.7cqw 1.8cqw;box-shadow:.4cqw .4cqw 0 #1A1A1A}
.tks{list-style:none;margin:2cqw 0 0;padding:1.2cqw 2cqw;background:#fff;border-radius:1.6cqw;box-shadow:0 1cqw 3cqw rgba(0,0,0,.3);display:inline-block}
.tks li{display:flex;align-items:center;gap:1cqw;font-size:1.9cqw;font-weight:900;color:#1A1A1A;padding:.55cqw 0}.tks li+li{border-top:.12cqw dashed #E4D9C2}
.tks i{font-style:normal;font-size:2.6cqw;line-height:1;color:#F7CE46;-webkit-text-stroke:.22cqw #1A1A1A!important;paint-order:stroke fill;text-shadow:.2cqw .2cqw 0 #1A1A1A}
.logo2{position:absolute;right:1.8cqw;top:1.8cqw;z-index:5;display:inline-flex;align-items:center;height:4.3cqw;background:#fff;border:.25cqw solid #1A1A1A;border-radius:3cqw;padding:0 1.8cqw}.logo2 .li{height:2.3cqw;width:auto}.logo2 .lt{height:2cqw;width:auto;margin-left:1cqw}
.rib3{position:absolute;right:4cqw;bottom:4.5cqw;width:27cqw;background:#fff;border-radius:1.4cqw;padding:.5cqw .5cqw 5cqw;box-shadow:0 1.2cqw 2.8cqw rgba(0,0,0,.4);transform:rotate(-3deg);z-index:3}
.rib3 img{display:block;width:100%;aspect-ratio:1/1;object-fit:cover;border-radius:1cqw}
.rib3 span{position:absolute;left:-1.4cqw;right:-1.4cqw;bottom:1cqw;padding:.8cqw .4cqw;text-align:center;font-size:1.9cqw;font-weight:900;color:#1A1A1A;background:#F7CE46;box-shadow:0 .4cqw 1cqw rgba(0,0,0,.3)}
/* A */
.ka .shade{position:absolute;inset:0;background:linear-gradient(90deg,rgba(18,40,26,.78) 0%,rgba(18,40,26,.45) 45%,rgba(0,0,0,0) 70%)}
.ka .tb{position:absolute;left:4.5cqw;top:7cqw}
.ka .ttl{font-size:4.5cqw}
/* B */
.kb .tri{position:absolute;inset:0;display:flex;gap:.5cqw;background:#fff}.kb .tri>div{position:relative;flex:1;overflow:hidden}.kb .tri img{width:100%;height:100%;object-fit:cover}
.kb .rl{position:absolute;left:1.6cqw;top:7.2cqw;z-index:2;background:#fff;color:#1A1A1A;font-weight:900;font-size:1.7cqw;padding:.5cqw 1.4cqw;border-radius:3cqw;border:.2cqw solid #1A1A1A;box-shadow:.25cqw .25cqw 0 #1A1A1A}
.kb .shade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 30%,rgba(10,30,18,.55) 55%,rgba(10,30,18,.9) 100%)}
.kb .tb{position:absolute;left:0;right:0;bottom:4cqw;text-align:center}
.kb .ttl{font-size:5cqw}
/* C */
.kc .shade{position:absolute;inset:0;background:linear-gradient(90deg,rgba(20,45,28,.85) 0%,rgba(20,45,28,.6) 50%,rgba(20,45,28,.15) 100%)}
.kc .tb{position:absolute;left:4.5cqw;top:7cqw}
.kc .ttl{font-size:4.2cqw}
.pola{position:absolute;right:3cqw;top:9cqw;width:32cqw;height:44cqw}
.pola figure{position:absolute;margin:0;width:19.5cqw;background:#fff;padding:1cqw 1cqw 0;box-shadow:0 1cqw 2.4cqw rgba(0,0,0,.45)}
.pola img{display:block;width:100%;aspect-ratio:1/1;object-fit:cover}
.pola figcaption{padding:.8cqw 0 1cqw;font-size:1.6cqw;font-weight:900;color:#1A1A1A;text-align:center;white-space:nowrap}
.pola .p1{left:0;top:0;transform:rotate(-6deg)}.pola .p2{right:0;top:15cqw;transform:rotate(5deg);z-index:1}
.stamp{position:absolute;right:26.5cqw;bottom:3.5cqw;z-index:4;width:13cqw;height:13cqw;border-radius:50%;background:#F7CE46;border:.4cqw solid #1A1A1A;box-shadow:.5cqw .5cqw 0 #1A1A1A;display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(-10deg);color:#1A1A1A;font-weight:900;font-size:1.7cqw;line-height:1.15;text-align:center}
.stamp b{font-size:2.1cqw}.stamp em{font-style:normal;font-size:3.6cqw;color:#C0392B}
'''

html = f'''<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>B1 素食到會 KV 方案（3 款）</title><style>{CSS}</style></head><body><div class="wrap">
<h1>🥗 B1 素食到會 Blog KV 方案（3 款，16:9）</h1>
<p>背景：Kitchen AO「素」味人生九宮格實拍＋Pexels 免費授權蔬菜／沙律相（可商用、毋須標示出處）。正式版建議換成自家拍攝的素食菜式。</p>
{''.join(f'<section class="opt"><h3>{t}</h3><p>{d}</p>{h}</section>' for t, d, h in KV)}
</div></body></html>'''
open(os.path.join(HERE, '..', 'kv-options.html'), 'w', encoding='utf-8').write(html)
print('ok')
