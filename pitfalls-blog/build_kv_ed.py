# -*- coding: utf-8 -*-
# 香港到會避伏指南 2026｜Blog KV 編輯風格兩款（A 雜誌封面／B 報章頭版）
import pathlib, io, base64, urllib.parse
from PIL import Image
HERE = pathlib.Path(__file__).parent
_src = Image.open(HERE.parent / 'halloween-edm-2026' / 'img' / 'logo-header-pill.png')
def _crop(box):
    b = io.BytesIO(); _src.crop(box).save(b, 'PNG'); return 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode()
LOGO = f'<span class="lg"><img class="lo" src="{_crop((40,21,508,99))}" alt="Kitchen AO" width="468" height="78"></span>'
PID = '1740047602722-b4993b79e4b7'
WPIMG = 'https://aoaodelivery.com/wp-content/uploads/2026/11/catering-pitfalls-kv-photo.jpg'
def ux(w, h): return WPIMG

ZH = '大常見｜香港到會避伏指南落單前先避開這五個陷阱照騙份量遲到隱藏收費服務附必問十條問題年版食物貨不對辦不足送貨結帳才知編輯部整理二〇二六第期'
FONT = ('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@500;900&family=Playfair+Display:ital,wght@1,700;1,900&display=swap&text='
        + urllib.parse.quote(''.join(sorted(set(ZH + '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.·,，、：｜—/ ')))) + '">')
SERIF = '"Noto Serif TC","Songti TC","PMingLiU",serif'
ITAL = '"Playfair Display",Georgia,serif'

CSS = r'''
.ao-ekv{container-type:inline-size;margin:0 0 26px}
.ao-ekv *{box-sizing:border-box}
.ao-ekv img{display:block}
.ao-ekv picture,.ao-ekv .bg{display:block;width:100%;height:100%}
.ao-ekv .bg{object-fit:cover;width:100%!important;height:100%!important;max-width:none!important}
.ao-ekv .lg{display:inline-flex;align-items:center;background:#fff}
.ao-ekv .lg .lo{height:2.1cqw!important;width:auto!important;max-width:none!important}

/* ===== A 雜誌封面：白紙欄＋相片（按文章欄闊度 560–900px 設計） ===== */
.ao-ekv.a .f{display:grid;grid-template-columns:46% 54%;aspect-ratio:16/9;background:#fff;border:1px solid #141414}
.ao-ekv.a .pp{position:relative;padding:4.2cqw 4.4cqw 3.6cqw;display:flex;flex-direction:column;color:#141414;min-width:0}
.ao-ekv.a .mh{display:flex;justify-content:space-between;align-items:center;gap:2cqw;border-bottom:2px solid #141414;padding-bottom:1.6cqw;font-family:-apple-system,"Helvetica Neue",Arial,sans-serif;font-size:max(10.5px,1.35cqw);letter-spacing:.22em;font-weight:700;white-space:nowrap}
.ao-ekv.a .mh .lg .lo{height:max(20px,3cqw)!important;width:auto!important;max-width:none!important}
.ao-ekv.a .k{margin:auto 0 0;line-height:1.3;font-family:SERIF;font-weight:500;font-size:2.7cqw;letter-spacing:.3em;color:#141414}
.ao-ekv.a .h{margin:.8cqw 0 0;font-family:SERIF;font-weight:900;font-size:9cqw;line-height:1.02;letter-spacing:.02em}
.ao-ekv.a .n{display:flex;align-items:baseline;gap:1.4cqw;margin:2.2cqw 0 0;padding-top:1.8cqw;border-top:1px solid #141414}
.ao-ekv.a .n b{font-family:ITAL;font-style:italic;font-weight:900;font-size:8cqw;line-height:.9;color:#A8322A}
.ao-ekv.a .n span{font-family:SERIF;font-weight:900;font-size:3.6cqw;line-height:1}
.ao-ekv.a .tg{margin:1.2cqw 0 0;font-family:SERIF;font-weight:500;font-size:max(12px,1.9cqw);color:#4a443d;letter-spacing:.04em}
.ao-ekv.a .ft{margin-top:2.4cqw;display:flex;justify-content:space-between;gap:2cqw;font-family:-apple-system,"Helvetica Neue",Arial,sans-serif;font-size:max(10.5px,1.3cqw);letter-spacing:.14em;color:#6b645c;font-weight:600}
.ao-ekv.a .ph{position:relative;overflow:hidden;min-width:0}
@container (max-width:540px){
 .ao-ekv.a .f{grid-template-columns:1fr;aspect-ratio:auto}
 .ao-ekv.a .ph{order:-1;aspect-ratio:4/3}
 .ao-ekv.a .pp{padding:5cqw 5.6cqw 5cqw}
 .ao-ekv.a .mh{font-size:2.4cqw;padding-bottom:2.6cqw}
 .ao-ekv.a .mh .lg .lo{height:5.2cqw!important;width:auto!important;max-width:none!important}
 .ao-ekv.a .k{margin-top:6cqw;font-size:5cqw}
 .ao-ekv.a .h{font-size:17cqw;margin-top:1.6cqw}
 .ao-ekv.a .n{gap:2.4cqw;margin-top:4cqw;padding-top:3.4cqw}
 .ao-ekv.a .n b{font-size:15cqw}
 .ao-ekv.a .n span{font-size:6.6cqw}
 .ao-ekv.a .tg{font-size:3.3cqw;margin-top:2.4cqw}
 .ao-ekv.a .ft{font-size:2.3cqw;margin-top:4.4cqw}
}

/* ===== B 報章頭版：全幅相片＋襯線大標題 ===== */
.ao-ekv.b .f{position:relative;aspect-ratio:16/9;overflow:hidden;background:#1b1612}
.ao-ekv.b .bgw{position:absolute;inset:0}
.ao-ekv.b .sh{position:absolute;inset:0;background:linear-gradient(180deg,rgba(14,11,8,.55) 0%,rgba(14,11,8,.05) 28%,rgba(14,11,8,.15) 45%,rgba(14,11,8,.9) 100%)}
.ao-ekv.b .top{position:absolute;left:3.6cqw;right:3.6cqw;top:2.6cqw;display:flex;justify-content:space-between;align-items:center;color:#fff;font-family:-apple-system,"Helvetica Neue",Arial,sans-serif;font-size:.95cqw;letter-spacing:.26em;font-weight:700;border-bottom:1px solid rgba(255,255,255,.55);padding-bottom:1.2cqw}
.ao-ekv.b .lg{padding:.6cqw 1cqw}
.ao-ekv.b .bt{position:absolute;left:3.6cqw;right:3.6cqw;bottom:3cqw;color:#fff}
.ao-ekv.b .k{font-family:ITAL;font-style:italic;font-weight:700;font-size:2cqw;color:#E9C46A;margin:0 0 .6cqw}
.ao-ekv.b .h{margin:0;font-family:SERIF;font-weight:900;font-size:5.8cqw;line-height:1.12;letter-spacing:.02em;max-width:70cqw}
.ao-ekv.b .d{margin:1.4cqw 0 0;font-family:SERIF;font-weight:500;font-size:1.6cqw;line-height:1.7;max-width:56cqw;color:#EDE6D8}
.ao-ekv.b .mb{display:none}
.ao-ekv.b .ix{display:grid;grid-template-columns:repeat(5,1fr);margin:2.2cqw 0 0;border-top:1px solid rgba(255,255,255,.55)}
.ao-ekv.b .ix span{padding:1cqw 0 0;font-family:SERIF;font-weight:500;font-size:1.45cqw;color:#fff;border-left:1px solid rgba(255,255,255,.3);padding-left:1.2cqw}
.ao-ekv.b .ix span:first-child{border-left:0;padding-left:0}
.ao-ekv.b .ix i{display:block;font-family:ITAL;font-style:italic;font-weight:700;font-size:1.3cqw;color:#E9C46A;margin-bottom:.2cqw}
@container (max-width:640px){
 .ao-ekv.b .f{aspect-ratio:4/5}
 .ao-ekv.b .sh{background:linear-gradient(180deg,rgba(14,11,8,.55) 0%,rgba(14,11,8,0) 22%,rgba(14,11,8,.35) 42%,rgba(14,11,8,.94) 70%)}
 .ao-ekv.b .top{left:5cqw;right:5cqw;top:5cqw;font-size:2.3cqw;padding-bottom:2.6cqw}
 .ao-ekv.b .lg{padding:1.4cqw 2.4cqw}.ao-ekv.b .lg .lo{height:4.6cqw!important;width:auto!important;max-width:none!important}
 .ao-ekv.b .bt{left:5cqw;right:5cqw;bottom:5cqw}
 .ao-ekv.b .k{font-size:4.6cqw}
 .ao-ekv.b .h{font-size:9.4cqw;max-width:none;line-height:1.18}
 .ao-ekv.b .mb{display:inline}
 .ao-ekv.b .d{font-size:3.7cqw;max-width:none;margin-top:3cqw}
 .ao-ekv.b .ix{grid-template-columns:repeat(5,1fr);margin-top:4.4cqw}
 .ao-ekv.b .ix span{font-size:3.3cqw;padding:2cqw 0 0 2cqw}
 .ao-ekv.b .ix i{font-size:3cqw}
}
'''.replace('SERIF', SERIF).replace('ITAL', ITAL)

PIC = (f'<picture><source media="(max-width:640px)" srcset="{ux(900,1125)}"><img class="bg" src="{ux(1600,900)}" '
       'alt="香港到會避伏指南 2026：派對到會美食擺滿木枱" width="1600" height="900" fetchpriority="high" decoding="async"></picture>')
PIC_A = (f'<picture><img class="bg" src="{ux(1000,1000)}" '
         'alt="香港到會避伏指南 2026：派對到會美食擺滿木枱" width="1000" height="1000" fetchpriority="high" decoding="async"></picture>')

A = ('<div class="ao-ekv a"><div class="f"><div class="pp">'
     '<div class="mh"><span>CATERING GUIDE · 2026</span>' + LOGO + '</div>'
     '<div class="k">香港到會</div><div class="h">避伏<br>指南</div>'
     '<div class="n"><b>5</b><span>大常見陷阱</span></div><div class="tg">照騙｜份量｜遲到｜隱藏收費｜服務</div>'
     '<div class="ft"><span>附落單前必問 10 條問題</span><span>2026 年版</span></div></div>'
     '<div class="ph">' + PIC_A + '</div></div></div>')

B = ('<div class="ao-ekv b"><div class="f"><div class="bgw">' + PIC + '</div><div class="sh"></div>'
     '<div class="top"><span>THE CATERING GUIDE · 2026</span>' + LOGO + '</div>'
     '<div class="bt"><div class="k">Before you order</div>'
     '<div class="h">香港到會避伏指南：<br>落單前先避開<br class="mb">這五個陷阱</div>'
     '<div class="d">由照騙、份量不足、送貨遲到到結帳才知的隱藏收費，附落單前必問十條問題。</div>'
     '<div class="ix"><span><i>01</i>照騙</span><span><i>02</i>份量</span><span><i>03</i>遲到</span><span><i>04</i>隱藏收費</span><span><i>05</i>服務</span></div>'
     '</div></div></div>')

for nm, kv in (('kv-ed-a.html', A), ('kv-ed-b.html', B)):
    (HERE / nm).write_text(FONT + '<style>' + CSS + '</style>' + kv, encoding='utf-8')
page = ('<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>KV 編輯風格兩款｜香港到會避伏指南 2026</title>' + FONT +
        '<style>body{margin:0;background:#E9E5DC;font-family:-apple-system,"PingFang HK",sans-serif;color:#222}.w{max-width:1280px;margin:0 auto;padding:24px 18px 60px}h1{font-size:20px;margin:0 0 4px}.nt{font-size:13px;color:#777;margin:0 0 20px}h2{font-size:16px;margin:30px 0 10px}'
        '.row{display:grid;grid-template-columns:minmax(0,1fr) 375px;gap:22px;align-items:start}.lab{font-size:12px;color:#888;margin:0 0 6px}@media(max-width:900px){.row{grid-template-columns:1fr}}' + CSS + '</style></head><body><div class="w">'
        '<h1>香港到會避伏指南 2026｜Blog KV（A 雜誌封面）</h1><div class="nt">字體：Noto Serif TC（中文襯線）＋ Playfair Display Italic（英文及數字）。無圓角、無陰影、無 emoji，以幼線、刊頭及大字排版。請用瀏覽器開啟以載入相片及字體。</p>'
        '<h2>A｜雜誌封面（白紙欄＋相片）</h2><div class="row"><div><div class="lab">桌面 16:9</p>' + A + '</div><div><div class="lab">手機</p>' + A + '</div></div>'
        '</div></body></html>')
(HERE / 'KV編輯風格兩款-香港到會避伏指南.html').write_text(page, encoding='utf-8')
print('ok')
