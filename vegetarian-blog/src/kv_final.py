# B1 KV 定稿：A1-e（提亮＋白霧＋Punch line＋關鍵字），去五辛相片，responsive（桌面 16:9／手機 4:5）
import os, html as H
from kv_fresh import LOGO, IMG, TAG, CSS as FRESH
TTL = '<h2 class="ttl">派對有<span class="y">素食朋友</span>點安排？<br>素食到會揀選全攻略</h2>'
HERE = os.path.dirname(os.path.abspath(__file__))
import base64
B64 = lambda f: 'data:image/jpeg;base64,' + base64.b64encode(open(os.path.join(HERE, '..', 'img', f), 'rb').read()).decode()
SET = 'https://aoaodelivery.com/wp-content/uploads/2025/05/9ee996d5-e50c-4745-b847-86d8e179c481.jpg'
KWS = '<p class="kw">' + ''.join(f'<span>#{w}</span>' for w in ['素食到會', '健康到會', '齋菜到會', '派對素食']) + '</p>'
CREDIT = ('<!-- 相片來源（Pexels 免費授權，可商用、毋須標示）：背景 https://www.pexels.com/photo/5418661/（保留原本食物，抹走青蔥、蒜頭換成番茄）；'
          '紫豆角 https://www.pexels.com/photo/5202092/；紫羽衣甘藍 https://www.pexels.com/photo/5755657/；'
          '套餐相為 Kitchen AO 自家產品相 -->')
def kv(src1600, src800):
  return (CREDIT + f'<div class="kv fr f1 vkv"><img class="bg" src="{src1600}" srcset="{src800} 800w, {src1600} 1600w" sizes="100vw" alt="派對素食到會：粟米、番茄、蘑菇、紫豆角等新鮮蔬菜"><div class="shade"></div>{LOGO}'
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
WP_DIR = 'https://aoaodelivery.com/wp-content/uploads/2026/10/'   # 上載後如路徑不同，請改這裡
def page(KV):
    return f'''<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>B1 KV 定稿</title><style>{CSS}
body{{background:transparent}}</style></head><body>{KV}</body></html>'''
def preview(KV, note):
    SRCDOC = H.escape(page(KV), quote=True)
    return f'''<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>B1 KV 定稿：桌面＋手機</title>
<style>body{{margin:0;background:#E9E5DC;font-family:-apple-system,"PingFang HK","Microsoft JhengHei",Arial,sans-serif;color:#3f3a33}}.w{{max-width:1240px;margin:0 auto;padding:24px 16px 60px}}h1{{font-size:22px;margin:0 0 4px}}p.d{{margin:0 0 18px;color:#7a6a45;font-size:14px}}h3{{margin:26px 0 8px;font-size:16px}}
iframe{{border:0;display:block;background:#fff}}.dkw{{width:100%;aspect-ratio:16/9;overflow:hidden;position:relative;box-shadow:0 6px 24px rgba(0,0,0,.15)}}.dk{{position:absolute;left:0;top:0;width:1200px;height:675px;transform-origin:0 0}}.mb{{width:390px;height:487.5px;box-shadow:0 6px 24px rgba(0,0,0,.15)}}</style></head><body><div class="w">
<h1>🥗 B1 KV 定稿</h1>
<p class="d">同一段 HTML，闊度 640px 或以下自動轉為手機版 4:5。背景已預先合成為 JPG（桌面載入 1600px、手機載入 800px），毋須即時運算。{note}</p>
<h3>桌面版（16:9）</h3><div class="dkw"><iframe class="dk" srcdoc="{SRCDOC}" title="B1 KV 桌面版（1200px 闊）" scrolling="no"></iframe></div>
<h3>手機版（390px 闊，4:5）</h3><iframe class="mb" srcdoc="{SRCDOC}" title="B1 KV 手機版" scrolling="no"></iframe>
</div><script>function fit(){{document.querySelectorAll('.dkw').forEach(w=>w.firstChild.style.transform='scale('+(w.clientWidth/1200)+')')}}fit();addEventListener('resize',fit)</script></body></html>'''
OUT = os.path.join(HERE, '..')
# 1) Repo / GitHub Pages：讀 img/ 資料夾
KV_REPO = kv('img/veg-b1-kv-bg-1600.jpg', 'img/veg-b1-kv-bg-800.jpg')
open(os.path.join(OUT, 'kv-b1.html'), 'w', encoding='utf-8').write(page(KV_REPO))
open(os.path.join(OUT, 'kv-b1-preview.html'), 'w', encoding='utf-8').write(preview(KV_REPO, ''))
# 2) 獨立預覽（圖片內嵌，離線及預覽面板都看到）
KV_STANDALONE = kv(B64('veg-b1-kv-bg-1600.jpg'), B64('veg-b1-kv-bg-800.jpg'))
open(os.path.join(OUT, 'kv-b1-preview-standalone.html'), 'w', encoding='utf-8').write(preview(KV_STANDALONE, '（此檔圖片已內嵌，可離線預覽）'))
# 3) WordPress 版：CSS 壓成一行（避免 WordPress 在 <style> 內插入 <br />），圖片讀 WP 媒體庫
KV_WP = kv(WP_DIR + 'veg-b1-kv-bg-1600.jpg', WP_DIR + 'veg-b1-kv-bg-800.jpg')
import re as _re
def scope(css, pre='.ao-vegkv '):
    css = _re.sub(r'/\*.*?\*/', '', css, flags=_re.S)
    out = []
    def rules(block):
        r = []
        for m in _re.finditer(r'([^{}]+)\{([^{}]*)\}', block):
            sel, body = m.group(1).strip(), m.group(2)
            if _re.match(r'^(\*|body|\.wrap|\.opt)', sel) or _re.search(r'\.(ka|kb|kc|pola|p1|p2|stamp|sub2|tks|f2|f3)\b', sel):
                continue
            sel = ','.join(pre + x.strip() for x in sel.split(','))
            r.append(sel + '{' + body + '}')
        return ''.join(r)
    i = 0
    for m in _re.finditer(r'@media[^{]+\{((?:[^{}]*\{[^{}]*\})*)\s*\}', css):
        out.append(rules(css[i:m.start()])); out.append(m.group(0)[:m.group(0).index('{')+1] + rules(m.group(1)) + '}'); i = m.end()
    out.append(rules(css[i:]))
    return ''.join(out).replace('\n', '')
css1 = '.ao-vegkv *{box-sizing:border-box}' + scope(CSS)
def block(src1600, src800, tag='div'):
    k = kv(src1600, src800).replace('<h2 class="ttl">', f'<{tag} class="ttl">').replace('</h2>', f'</{tag}>')
    return ('<div class="ao-vegkv"><style>.ao-vegkv{margin:0 0 22px;font-family:-apple-system,"PingFang HK","Microsoft JhengHei",Arial,sans-serif}.ao-vegkv h1.ttl{margin:0!important;padding:0!important;border:0!important}' + css1 + '</style>' + k + '</div>')
wp = ('<!-- B1 KV（WordPress Custom HTML／WPBakery Raw HTML）：先把 veg-b1-kv-bg-1600.jpg 及 veg-b1-kv-bg-800.jpg 上載到媒體庫，'
      '如網址不是 ' + WP_DIR + '…，請把下面兩個圖片網址改成媒體庫的網址 -->\n'
      + block(WP_DIR + 'veg-b1-kv-bg-1600.jpg', WP_DIR + 'veg-b1-kv-bg-800.jpg', 'div'))
open(os.path.join(OUT, 'kv-b1-WORDPRESS.html'), 'w', encoding='utf-8').write(wp)
print('final ok')
