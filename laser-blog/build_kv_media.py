# -*- coding: utf-8 -*-
# 激光打印食物 blog KV｜D 雙相頭條 × 野餐 blog 媒體 banner 風格（新假期式：白字黑描邊、黑底黃字膠囊、黃色色帶、圓章）
import pathlib, runpy, urllib.parse
HERE = pathlib.Path(__file__).parent
LOGO = runpy.run_path(str(HERE.parent / 'pitfalls-blog' / 'build_kv_ed.py'))['LOGO']
UP = 'https://aoaodelivery.com/wp-content/uploads'
BURGER = UP + '/2025/04/IMG_4266-e1788770926121.jpg'
MAC = UP + '/2025/05/DSC01522-768x577.jpeg'
FONT = ('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Chiron+Sung+HK:wght@900&display=swap&text='
        + urllib.parse.quote('激光打印食物雷射包・馬卡龍') + '">')
CSS = r'''
.ao-mkv2{container-type:inline-size;margin:0 0 26px;font-family:-apple-system,"PingFang HK","Microsoft JhengHei",Arial,sans-serif}
.ao-mkv2 *{box-sizing:border-box}
.ao-mkv2 .f{position:relative;aspect-ratio:16/9;overflow:hidden;border-radius:12px;background:#1A1A1A;box-shadow:0 6px 24px rgba(0,0,0,.15)}
.ao-mkv2 .ph{position:absolute;inset:0;display:grid;grid-template-columns:57% 43%;gap:.5cqw;background:#fff}
.ao-mkv2 .ph div{position:relative;overflow:hidden}
.ao-mkv2 .ph img{display:block;width:100%!important;height:100%!important;max-width:none!important;object-fit:cover;margin:0}
.ao-mkv2 .sh{position:absolute;left:0;right:0;bottom:0;height:62%;background:linear-gradient(180deg,rgba(0,0,0,0) 0%,rgba(0,0,0,.35) 45%,rgba(0,0,0,.72) 100%)}
.ao-mkv2 .lg{position:absolute;right:1.8cqw;top:1.8cqw;z-index:5;display:inline-flex;align-items:center;height:4cqw;background:#fff;border:.22cqw solid #1A1A1A;border-radius:3cqw;padding:0 1.6cqw}
.ao-mkv2 .lg .lo{height:2.3cqw!important;width:auto!important;max-width:none!important;display:block}
.ao-mkv2 .lab{position:absolute;z-index:3;background:#fff;color:#1A1A1A;font-weight:900;font-size:1.8cqw;padding:.5cqw 1.4cqw;border-radius:3cqw;border:.2cqw solid #1A1A1A;box-shadow:.3cqw .3cqw 0 #1A1A1A;white-space:nowrap}
.ao-mkv2 .l1{left:2cqw;top:2cqw;transform:rotate(-3deg)}
.ao-mkv2 .l2{left:59cqw;top:2.2cqw;transform:rotate(2deg)}
.ao-mkv2 .tb{position:absolute;left:3.6cqw;bottom:3.4cqw;z-index:4;display:flex;flex-direction:column;align-items:flex-start}
.ao-mkv2 .pill{display:inline-block;background:#1A1A1A;color:#F7CE46;font-weight:900;font-size:2cqw;padding:.6cqw 1.9cqw;border-radius:4cqw;margin-bottom:1.1cqw}
.ao-mkv2 .ttl{margin:0;font-family:"Chiron Sung HK","Noto Serif TC","Songti TC",serif;font-size:6.6cqw;font-weight:900;line-height:1.14;color:#fff;-webkit-text-stroke:.55cqw #1A1A1A;paint-order:stroke fill;text-shadow:0 .5cqw 0 #1A1A1A;letter-spacing:.2cqw;white-space:nowrap}
.ao-mkv2 .ttl .y{color:#F7CE46}
.ao-mkv2 .sub2{margin:1.4cqw 0 0;display:inline-block;background:#F7CE46;color:#1A1A1A;font-weight:900;font-size:2.1cqw;padding:.6cqw 1.6cqw;box-shadow:.4cqw .4cqw 0 #1A1A1A}
.ao-mkv2 .sub{margin:1.1cqw 0 0;font-size:1.9cqw;font-weight:900;color:#fff;text-shadow:0 .2cqw .5cqw rgba(0,0,0,.6)}
.ao-mkv2 .stamp{position:absolute;right:3.4cqw;bottom:3.4cqw;z-index:4;width:13cqw;height:13cqw;border-radius:50%;background:#F7CE46;border:.4cqw solid #1A1A1A;box-shadow:.5cqw .5cqw 0 #1A1A1A;display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(-10deg);color:#1A1A1A;font-weight:900;font-size:1.5cqw;line-height:1.15;text-align:center}
.ao-mkv2 .stamp b{font-size:3.4cqw;line-height:1}
@container (max-width:560px){
 .ao-mkv2 .f{aspect-ratio:auto;display:flex;flex-direction:column;background:#1A1A1A}
 .ao-mkv2 .ph{position:relative;inset:auto;grid-template-columns:1fr 1fr;gap:1cqw;aspect-ratio:2/1.15}
 .ao-mkv2 .sh{display:none}
 .ao-mkv2 .lg{right:3cqw;top:3cqw;height:7.6cqw;border-width:.45cqw;border-radius:6cqw;padding:0 3cqw}.ao-mkv2 .lg .lo{height:4.3cqw!important}
 .ao-mkv2 .lab{font-size:3.3cqw;padding:.9cqw 2.4cqw;border-width:.4cqw;box-shadow:.6cqw .6cqw 0 #1A1A1A}
 .ao-mkv2 .l1{left:3cqw;top:auto;bottom:calc(100% - 55cqw)}
 .ao-mkv2 .l2{left:53cqw;top:auto;bottom:calc(100% - 55cqw)}
 .ao-mkv2 .tb{position:relative;left:auto;bottom:auto;padding:7cqw 5cqw 6cqw}
 .ao-mkv2 .pill{font-size:3.6cqw;padding:1.2cqw 3.4cqw;margin-bottom:2.4cqw;border-radius:8cqw;background:#F7CE46;color:#1A1A1A}
 .ao-mkv2 .ttl{font-size:10.6cqw;-webkit-text-stroke:0;text-shadow:none;white-space:normal}
 .ao-mkv2 .sub2{font-size:3.9cqw;padding:1.2cqw 3cqw;margin-top:3cqw;box-shadow:.8cqw .8cqw 0 #fff}
 .ao-mkv2 .sub{font-size:3.6cqw;margin-top:2.6cqw;text-shadow:none;color:#E8E1D2}
 .ao-mkv2 .stamp{right:4cqw;bottom:auto;top:48cqw;width:21cqw;height:21cqw;border-width:.7cqw;box-shadow:.9cqw .9cqw 0 #000;font-size:2.5cqw}
 .ao-mkv2 .stamp b{font-size:5.4cqw}
}
'''
LOGO2 = LOGO.replace('class="lg"', 'class="lg" aria-label="Kitchen AO"')
KV = ('<div class="ao-mkv2"><div class="f">'
      f'<div class="ph"><div><img src="{BURGER}" alt="雷射包：漢堡刻上 Happy Birthday" fetchpriority="high" decoding="async"></div>'
      f'<div><img src="{MAC}" alt="馬卡龍刻字：印上名字及 Logo" decoding="async"></div></div>'
      '<div class="sh"></div>' + LOGO2 +
      '<span class="lab l1">🍔 雷射包</span><span class="lab l2">🌈 馬卡龍刻字</span>'
      '<div class="tb"><span class="pill">2026 香港到會新玩法</span>'
      '<div class="ttl">激光打印食物<br><span class="y">雷射包・馬卡龍</span></div>'
      '<span class="sub2">公司 Logo、名字、祝福語都刻得到</span>'
      '<span class="sub">$228 起｜最少 3 日前預訂</span></div>'
      '<div class="stamp">IG 觀看<b>21萬+</b>人氣之選</div>'
      '</div></div>')
(HERE / 'kv-media2.html').write_text(FONT + '<style>' + CSS + '</style>' + KV, encoding='utf-8')
page = ('<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>激光打印食物 KV｜媒體 banner 風格</title>' + FONT +
        '<style>body{margin:0;background:#E9E5DC;font-family:-apple-system,"PingFang HK",sans-serif}.w{max-width:1280px;margin:0 auto;padding:24px 18px 60px}h1{font-size:20px;margin:0 0 16px}'
        '.row{display:grid;grid-template-columns:minmax(0,1fr) 375px;gap:22px;align-items:start}.lab0{font-size:12px;color:#888;margin:0 0 6px}@media(max-width:900px){.row{grid-template-columns:1fr}}' + CSS + '</style></head><body><div class="w">'
        '<h1>激光打印食物｜Blog KV（D 雙相頭條 × 媒體 banner 風格）</h1><div class="row"><div><p class="lab0">桌面 16:9</p>' + KV + '</div><div><p class="lab0">手機 4:5</p>' + KV + '</div></div></div></body></html>')
(HERE / 'KV媒體banner-激光打印食物.html').write_text(page, encoding='utf-8')
print('ok')
