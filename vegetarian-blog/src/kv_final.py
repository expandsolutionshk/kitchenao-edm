# B1 KV 定稿：A1-e（提亮＋白霧＋Punch line＋關鍵字），去五辛相片，responsive（桌面 16:9／手機 4:5）
import os, html as H
from kv_fresh import LOGO, IMG, TAG, CSS as FRESH
TTL = '<h2 class="ttl">派對有<span class="y">素食朋友</span>點安排？<br>素食到會揀選全攻略</h2>'
HERE = os.path.dirname(os.path.abspath(__file__))
JS = open(os.path.join(HERE, 'veg_bg.js'), encoding='utf-8').read()
SET = 'https://aoaodelivery.com/wp-content/uploads/2025/05/9ee996d5-e50c-4745-b847-86d8e179c481.jpg'
KWS = '<p class="kw">' + ''.join(f'<span>#{w}</span>' for w in ['素食到會', '健康到會', '齋菜到會', '派對素食']) + '</p>'
CREDIT = ('<!-- 相片來源（Pexels 免費授權，可商用、毋須標示）：背景 https://www.pexels.com/photo/5418661/（保留原本食物，抹走青蔥、蒜頭換成番茄）；'
          '紫豆角 https://www.pexels.com/photo/5202092/；紫羽衣甘藍 https://www.pexels.com/photo/5755657/；'
          '套餐相為 Kitchen AO 自家產品相 -->')
KV = (CREDIT + f'<div class="kv fr f1 vkv"><img class="bg" data-vegbg src="{IMG["veg"]}" alt="" style="opacity:0;transition:opacity .4s"><div class="shade"></div>{LOGO}'
      f'<div class="tb">{TAG}{TTL}<p class="pl2">素食，都可以豐富又滿足。</p>{KWS}</div>'
      f'<div class="rib3"><img src="{SET}" alt="Kitchen AO「素」味人生素食到會套餐"><span>⭐「素」味人生套餐</span></div></div>')
CSS = FRESH + '''
.pl2{margin:2.2cqw 0 0;font-size:2.6cqw;font-weight:800;color:#2C6E49;letter-spacing:.15cqw}
.kw{margin:1.6cqw 0 0;display:flex;flex-wrap:wrap;gap:.8cqw}.kw span{font-size:1.7cqw;font-weight:700;color:#2C6E49;background:rgba(255,255,255,.9);border:.15cqw solid #CFE8CD;border-radius:3cqw;padding:.35cqw 1.2cqw}
.fr .tb{top:50%;transform:translateY(-50%)}
.vkv{border-radius:0;box-shadow:none}
.vkv .shade{background:linear-gradient(90deg,rgba(248,251,244,.83) 0%,rgba(248,251,244,.70) 42%,rgba(248,251,244,0) 66%)}
@media(max-width:640px){
.vkv{aspect-ratio:4/5}
.vkv .shade{background:linear-gradient(180deg,rgba(248,251,244,.85) 0%,rgba(248,251,244,.78) 48%,rgba(248,251,244,0) 72%)}
.vkv .logo2{height:7.5cqw;padding:0 3cqw;right:4cqw;top:4cqw}.vkv .logo2 .li{height:4cqw}.vkv .logo2 .lt{height:3.4cqw;margin-left:1.6cqw}
.vkv .tb{left:6cqw;right:6cqw;top:15cqw;transform:none}
.vkv .pill{font-size:3.6cqw;padding:1cqw 3.2cqw;margin-bottom:2.4cqw}
.vkv .ttl{font-size:6.3cqw;-webkit-text-stroke:.8cqw #fff!important}
.vkv .pl2{font-size:4.4cqw;margin-top:3.4cqw}
.vkv .kw{gap:1.6cqw;margin-top:2.6cqw}.vkv .kw span{font-size:3.1cqw;padding:.7cqw 2.4cqw;border-width:.3cqw}
.vkv .rib3{width:44cqw;right:6cqw;bottom:6cqw;padding:.9cqw .9cqw 8.6cqw;border-radius:2.4cqw}
.vkv .rib3 span{font-size:3.3cqw;bottom:1.8cqw;left:-2.4cqw;right:-2.4cqw;padding:1.3cqw .6cqw}
}
'''
KV_PAGE = f'''<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>B1 KV 定稿（A1-e）</title><style>{CSS}
body{{background:transparent}}</style></head><body>{KV}<script>{JS}</script></body></html>'''
open(os.path.join(HERE, '..', 'kv-b1.html'), 'w', encoding='utf-8').write(KV_PAGE)
SRCDOC = H.escape(KV_PAGE, quote=True)
prev = f'''<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>B1 KV 定稿：桌面＋手機</title>
<style>body{{margin:0;background:#E9E5DC;font-family:-apple-system,"PingFang HK","Microsoft JhengHei",Arial,sans-serif;color:#3f3a33}}.w{{max-width:1240px;margin:0 auto;padding:24px 16px 60px}}h1{{font-size:22px;margin:0 0 4px}}p.d{{margin:0 0 18px;color:#7a6a45;font-size:14px}}h3{{margin:26px 0 8px;font-size:16px}}
iframe{{border:0;display:block;background:#fff}}.dkw{{width:100%;aspect-ratio:16/9;overflow:hidden;position:relative;box-shadow:0 6px 24px rgba(0,0,0,.15)}}.dk{{position:absolute;left:0;top:0;width:1200px;height:675px;transform-origin:0 0}}.mb{{width:390px;height:487.5px;box-shadow:0 6px 24px rgba(0,0,0,.15)}}</style></head><body><div class="w">
<h1>🥗 B1 KV 定稿：A1-e（Punch line＋關鍵字）</h1>
<p class="d">同一段 HTML，闊度 640px 或以下自動轉為手機版 4:5。背景：保留原本蔬菜（去五辛：抹走青蔥、蒜頭換成番茄），少量加入紫豆角及紫羽衣甘藍（頁面載入時以 Canvas 即時處理，約 1–2 秒）。</p>
<h3>桌面版（16:9）</h3><div class="dkw"><iframe class="dk" srcdoc="{SRCDOC}" title="B1 KV 桌面版（1200px 闊）" scrolling="no"></iframe></div>
<h3>手機版（390px 闊，4:5）</h3><iframe class="mb" srcdoc="{SRCDOC}" title="B1 KV 手機版" scrolling="no"></iframe>
</div><script>function fit(){{document.querySelectorAll('.dkw').forEach(w=>w.firstChild.style.transform='scale('+(w.clientWidth/1200)+')')}}fit();addEventListener('resize',fit)</script></body></html>'''
open(os.path.join(HERE, '..', 'kv-b1-preview.html'), 'w', encoding='utf-8').write(prev); print('final ok')
