# -*- coding: utf-8 -*-
# 香港到會避伏指南 2026｜Blog KV（媒體風格：參考野餐／素食 blog KV）
import pathlib, io, base64
from PIL import Image
HERE = pathlib.Path(__file__).parent
_src = Image.open(HERE.parent / 'halloween-edm-2026' / 'img' / 'logo-header-pill.png')
def _crop(box):
    b = io.BytesIO(); _src.crop(box).save(b, 'PNG'); return 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode()
LOGO = f'<span class="lg" aria-label="Kitchen AO"><img class="li" src="{_crop((42,23,188,97))}" alt=""><img class="lt" src="{_crop((218,40,506,88))}" alt="Kitchen AO"></span>'
PID = '1740047602722-b4993b79e4b7'   # Unsplash dHeKcZ0a-xY
def ux(w, h): return f'https://images.unsplash.com/photo-{PID}?w={w}&h={h}&fit=crop&crop=entropy&q=78&auto=format'

CSS = r'''
.ao-mkv{container-type:inline-size;margin:0 0 24px;font-family:-apple-system,"PingFang HK","Microsoft JhengHei",Arial,sans-serif}
.ao-mkv *{box-sizing:border-box}
.ao-mkv .f{position:relative;aspect-ratio:16/9;overflow:hidden;border-radius:12px;background:#2a1f16;box-shadow:0 6px 24px rgba(0,0,0,.15)}
.ao-mkv picture,.ao-mkv .bg{position:absolute;inset:0;display:block;width:100%;height:100%}
.ao-mkv .bg{object-fit:cover}
.ao-mkv .sh{position:absolute;inset:0;background:linear-gradient(90deg,rgba(20,14,8,.86) 0%,rgba(20,14,8,.62) 42%,rgba(20,14,8,.1) 72%,rgba(0,0,0,0) 100%)}
.ao-mkv .lg{position:absolute;right:1.8cqw;top:1.8cqw;z-index:5;display:inline-flex;align-items:center;height:4.3cqw;background:#fff;border:.25cqw solid #1A1A1A;border-radius:3cqw;padding:0 1.8cqw}
.ao-mkv .lg .li{height:2.3cqw;width:auto}.ao-mkv .lg .lt{height:2cqw;width:auto;margin-left:1cqw}
.ao-mkv .tb{position:absolute;left:4.5cqw;top:6.5cqw;z-index:3;display:flex;flex-direction:column;align-items:flex-start}
.ao-mkv .pill{display:inline-block;background:#1A1A1A;color:#F7CE46;font-weight:900;font-size:2.1cqw;padding:.6cqw 2cqw;border-radius:4cqw;margin:0 0 1.4cqw;letter-spacing:.05em}
.ao-mkv .ttl{margin:0;font-size:5.4cqw;font-weight:900;line-height:1.22;color:#fff;-webkit-text-stroke:.55cqw #1A1A1A;paint-order:stroke fill;text-shadow:0 .5cqw 0 #1A1A1A;letter-spacing:.15cqw;white-space:nowrap}
.ao-mkv .ttl .y{color:#F7CE46}
.ao-mkv .sub{display:inline-block;margin:1.6cqw 0 0;background:#F7CE46;color:#1A1A1A;font-weight:900;font-size:1.9cqw;padding:.7cqw 1.8cqw;box-shadow:.4cqw .4cqw 0 #1A1A1A}
.ao-mkv .tks{list-style:none;margin:2cqw 0 0;padding:1.2cqw 2cqw;background:#fff;border-radius:1.6cqw;box-shadow:0 1cqw 3cqw rgba(0,0,0,.3);display:inline-block}
.ao-mkv .tks li{display:flex;align-items:center;gap:1cqw;font-size:1.85cqw;font-weight:900;color:#1A1A1A;padding:.55cqw 0;margin:0;line-height:1.3}
.ao-mkv .tks li+li{border-top:.12cqw dashed #E4D9C2}
.ao-mkv .tks i{font-style:normal;font-size:2.4cqw;line-height:1;color:#F7CE46;-webkit-text-stroke:.22cqw #1A1A1A;paint-order:stroke fill;text-shadow:.2cqw .2cqw 0 #1A1A1A}
.ao-mkv .stamp{position:absolute;right:5cqw;bottom:5cqw;z-index:4;width:14cqw;height:14cqw;border-radius:50%;background:#F7CE46;border:.4cqw solid #1A1A1A;box-shadow:.5cqw .5cqw 0 #1A1A1A;display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(-10deg);color:#1A1A1A;font-weight:900;font-size:1.7cqw;line-height:1.15;text-align:center}
.ao-mkv .stamp b{font-size:3.4cqw;line-height:1}.ao-mkv .stamp em{font-style:normal;font-size:2cqw;color:#C0392B;margin-top:.3cqw}
@container (max-width:640px){
 .ao-mkv .f{aspect-ratio:4/5}
 .ao-mkv .sh{background:linear-gradient(0deg,rgba(20,14,8,.92) 0%,rgba(20,14,8,.78) 46%,rgba(20,14,8,.2) 75%,rgba(0,0,0,0) 100%)}
 .ao-mkv .lg{right:auto;left:5cqw;top:5cqw;height:9.4cqw;border-width:.5cqw;border-radius:6cqw;padding:0 3.6cqw}
 .ao-mkv .lg .li{height:5cqw}.ao-mkv .lg .lt{height:4.3cqw;margin-left:2cqw}
 .ao-mkv .tb{left:5cqw;right:5cqw;top:auto;bottom:6cqw}
 .ao-mkv .pill{font-size:4.2cqw;padding:1.2cqw 4cqw;border-radius:8cqw;margin-bottom:3cqw}
 .ao-mkv .ttl{font-size:10.4cqw;-webkit-text-stroke:1cqw #1A1A1A;text-shadow:0 1cqw 0 #1A1A1A;white-space:normal}
 .ao-mkv .sub{font-size:4cqw;padding:1.4cqw 3.4cqw;margin-top:3.4cqw;box-shadow:.8cqw .8cqw 0 #1A1A1A}
 .ao-mkv .tks{margin-top:4cqw;padding:2.4cqw 4cqw;border-radius:3cqw}
 .ao-mkv .tks li{font-size:3.9cqw;gap:2cqw;padding:1.1cqw 0}
 .ao-mkv .tks i{font-size:5cqw;-webkit-text-stroke:.4cqw #1A1A1A}
 .ao-mkv .stamp{right:5cqw;top:5cqw;bottom:auto;width:24cqw;height:24cqw;border-width:.7cqw;box-shadow:.9cqw .9cqw 0 #1A1A1A;font-size:3cqw}
 .ao-mkv .stamp b{font-size:6cqw}.ao-mkv .stamp em{font-size:3.6cqw}
}
'''

KV = ('<div class="ao-mkv"><div class="f">'
      f'<picture><source media="(max-width:640px)" srcset="{ux(900,1125)}"><img class="bg" src="{ux(1600,900)}" alt="香港到會避伏指南 2026：派對到會美食擺滿木枱" width="1600" height="900" fetchpriority="high" decoding="async"></picture>'
      '<div class="sh"></div>' + LOGO +
      '<div class="tb"><span class="pill">香港到會避伏指南 2026</span>'
      '<p class="ttl">叫到會前必看！<br><span class="y">5 大到會陷阱</span></p>'
      '<span class="sub">附落單前必問 10 條問題</span>'
      '<ul class="tks"><li><i>✔</i>照騙：食物貨不對辦</li><li><i>✔</i>份量不足、送貨遲到</li><li><i>✔</i>結帳才知的隱藏收費</li></ul></div>'
      '<div class="stamp"><b>2026</b>最新版<em>避伏攻略</em></div>'
      '</div></div>')

(HERE / 'kv-media.html').write_text('<style>' + CSS + '</style>' + KV, encoding='utf-8')
page = ('<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>KV 媒體風格｜香港到會避伏指南 2026</title>'
        '<style>body{margin:0;background:#E9E5DC;font-family:-apple-system,"PingFang HK",sans-serif}.w{max-width:1280px;margin:0 auto;padding:24px 18px 60px}h1{font-size:20px;margin:0 0 16px}'
        '.row{display:grid;grid-template-columns:minmax(0,1fr) 375px;gap:22px;align-items:start}.lab{font-size:12px;color:#888;margin:0 0 6px}@media(max-width:900px){.row{grid-template-columns:1fr}}' + CSS + '</style></head><body><div class="w">'
        '<h1>香港到會避伏指南 2026｜Blog KV（媒體風格）</h1><div class="row"><div><p class="lab">桌面 16:9</p>' + KV + '</div><div><p class="lab">手機 4:5</p>' + KV + '</div></div></div></body></html>')
(HERE / 'KV媒體風格-香港到會避伏指南.html').write_text(page, encoding='utf-8')
print('ok')
