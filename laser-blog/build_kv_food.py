# -*- coding: utf-8 -*-
# 激光打印食物 blog KV｜飲食媒體風格兩款（C 拱形相片／D 雙相頭條）
import pathlib, runpy
HERE = pathlib.Path(__file__).parent
LOGO = runpy.run_path(str(HERE.parent / 'pitfalls-blog' / 'build_kv_ed.py'))['LOGO']
UP = 'https://aoaodelivery.com/wp-content/uploads'
BURGER = UP + '/2025/04/IMG_4266-e1788770926121.jpg'
MAC = UP + '/2025/05/DSC01522-768x577.jpeg'
SANS = '-apple-system,"PingFang HK","Noto Sans TC","Microsoft JhengHei",sans-serif'

CSS = r'''
.ao-fkv{container-type:inline-size;margin:0 0 26px;font-family:SANS}
.ao-fkv *{box-sizing:border-box}
.ao-fkv img{display:block;width:100%;height:100%;object-fit:cover;margin:0}
.ao-fkv .lg{display:inline-flex;align-items:center;background:#fff}
.ao-fkv .lg .lo{height:max(18px,2.6cqw);width:auto}

/* ===== C｜拱形相片（雜誌食譜頁感覺） ===== */
.ao-fkv.c .f{position:relative;aspect-ratio:16/9;background:#F1E6D2;overflow:hidden;color:#1A1A1A}
.ao-fkv.c .tx{position:absolute;left:5cqw;top:4.6cqw;bottom:4.6cqw;width:50cqw;display:flex;flex-direction:column}
.ao-fkv.c .top{display:flex;align-items:center;gap:1.6cqw}
.ao-fkv.c .lg{background:transparent}
.ao-fkv.c .tag{background:#C2452D;color:#fff;font-weight:800;font-size:max(10px,1.25cqw);letter-spacing:.18em;padding:.5cqw 1.2cqw}
.ao-fkv.c .k{margin:auto 0 0;font-size:max(12px,2cqw);font-weight:700;color:#C2452D;letter-spacing:.06em}
.ao-fkv.c .h{margin:.8cqw 0 0;font-size:8.8cqw;line-height:1.02;font-weight:900;letter-spacing:-.01em}
.ao-fkv.c .d{margin:1.6cqw 0 0;font-size:max(12px,1.75cqw);line-height:1.55;font-weight:500;color:#4a3f33;max-width:40cqw}
.ao-fkv.c .pr{display:flex;gap:2.4cqw;margin:2.4cqw 0 0;padding-top:1.6cqw;border-top:2px solid #1A1A1A}
.ao-fkv.c .pr div{font-size:max(11px,1.35cqw);font-weight:600;color:#4a3f33;line-height:1.4}
.ao-fkv.c .pr b{display:block;font-size:max(14px,2.3cqw);font-weight:900;color:#1A1A1A}
.ao-fkv.c .arch{position:absolute;right:5cqw;top:4.6cqw;width:30cqw;height:calc(100% - 9.2cqw);border-radius:15cqw 15cqw 0 0;overflow:hidden}
.ao-fkv.c .dot{position:absolute;right:30cqw;bottom:4.6cqw;width:17cqw;height:17cqw;border-radius:50%;overflow:hidden;border:.7cqw solid #F1E6D2}
.ao-fkv.c .cap{position:absolute;right:5cqw;bottom:1.4cqw;font-size:max(9px,1cqw);letter-spacing:.14em;font-weight:700;color:#7a6a55}
@container (max-width:560px){
 .ao-fkv.c .f{aspect-ratio:4/5}
 .ao-fkv.c .arch{right:6cqw;top:6cqw;width:50cqw;height:54cqw;border-radius:25cqw 25cqw 0 0}
 .ao-fkv.c .dot{right:auto;left:10cqw;top:28cqw;bottom:auto;width:28cqw;height:28cqw;border-width:1.4cqw}
 .ao-fkv.c .tx{left:6cqw;right:6cqw;width:auto;top:6cqw;bottom:6cqw}
 .ao-fkv.c .top{flex-direction:column;align-items:flex-start;gap:2cqw}
 .ao-fkv.c .lg .lo{height:6cqw}
 .ao-fkv.c .tag{font-size:2.8cqw;padding:1cqw 2.4cqw}
 .ao-fkv.c .k{font-size:4.2cqw}
 .ao-fkv.c .h{font-size:12.6cqw}
 .ao-fkv.c .d{display:none}
 .ao-fkv.c .pr{gap:6cqw;margin-top:3.6cqw;padding-top:3cqw}
 .ao-fkv.c .pr div{font-size:3cqw}.ao-fkv.c .pr b{font-size:5.2cqw}
 .ao-fkv.c .cap{display:none}
}

/* ===== D｜雙相頭條（飲食網站頭條感覺） ===== */
.ao-fkv.d .f{position:relative;aspect-ratio:16/9;overflow:hidden;background:#111;color:#fff}
.ao-fkv.d .ph{position:absolute;inset:0 0 34% 0;display:grid;grid-template-columns:58% 42%;gap:3px;background:#111}
.ao-fkv.d .ph div{position:relative;overflow:hidden}
.ao-fkv.d .ph span{position:absolute;left:1.6cqw;bottom:1.4cqw;background:#fff;color:#111;font-weight:800;font-size:max(10px,1.25cqw);padding:.4cqw 1cqw}
.ao-fkv.d .lg{position:absolute;right:2cqw;top:2cqw;padding:.7cqw 1.2cqw}
.ao-fkv.d .bar{position:absolute;left:0;right:0;bottom:0;height:34%;padding:2.4cqw 4cqw;display:flex;flex-direction:column;justify-content:center;background:#111}
.ao-fkv.d .tag{display:inline-block;align-self:flex-start;background:#E8B634;color:#111;font-weight:900;font-size:max(10px,1.2cqw);letter-spacing:.16em;padding:.4cqw 1.1cqw;margin-bottom:1.2cqw}
.ao-fkv.d .h{margin:0;font-size:4.6cqw;line-height:1.12;font-weight:900}
.ao-fkv.d .h em{font-style:normal;color:#E8B634}
.ao-fkv.d .d{margin:1cqw 0 0;font-size:max(12px,1.6cqw);color:#cfc7b8;font-weight:500}
@container (max-width:560px){
 .ao-fkv.d .f{aspect-ratio:4/5}
 .ao-fkv.d .ph{inset:0 0 44% 0;grid-template-columns:1fr;grid-template-rows:62% 38%}
 .ao-fkv.d .ph span{font-size:3cqw;padding:1cqw 2.2cqw;left:3.4cqw;bottom:3cqw}
 .ao-fkv.d .lg{right:4cqw;top:4cqw;padding:1.4cqw 2.4cqw}.ao-fkv.d .lg .lo{height:5.6cqw}
 .ao-fkv.d .bar{height:44%;padding:5cqw 6cqw}
 .ao-fkv.d .tag{font-size:2.8cqw;padding:1cqw 2.4cqw;margin-bottom:3cqw}
 .ao-fkv.d .h{font-size:9.4cqw}
 .ao-fkv.d .d{font-size:3.6cqw;margin-top:2.4cqw}
}
'''.replace('SANS', SANS)

C = ('<div class="ao-fkv c"><div class="f">'
     '<div class="tx"><div class="top">' + LOGO + '<span class="tag">PARTY FOOD</span></div>'
     '<div class="k">香港到會新玩法</div><div class="h">激光<br>打印食物</div>'
     '<div class="d">公司 Logo、名字、祝福語，刻在雷射包和馬卡龍上。</div>'
     '<div class="pr"><div><b>$228</b>雷射包 8 個起</div><div><b>$198</b>馬卡龍 10 個</div><div><b>3 日</b>前預訂</div></div></div>'
     f'<div class="arch"><img src="{BURGER}" alt="雷射包：漢堡刻上 Happy Birthday" loading="eager" decoding="async"></div>'
     f'<div class="dot"><img src="{MAC}" alt="馬卡龍刻字" loading="eager" decoding="async"></div>'
     '<span class="cap">KITCHEN AO · 2026</span></div></div>')

D = ('<div class="ao-fkv d"><div class="f">'
     f'<div class="ph"><div><img src="{BURGER}" alt="雷射包：漢堡刻上 Happy Birthday" decoding="async"><span>雷射包</span></div>'
     f'<div><img src="{MAC}" alt="馬卡龍刻字：印上 Logo" decoding="async"><span>馬卡龍刻字</span></div></div>' + LOGO +
     '<div class="bar"><span class="tag">PARTY FOOD · 2026</span>'
     '<div class="h">激光打印食物：<em>雷射包、馬卡龍</em>刻上你的字</div>'
     '<div class="d">公司 Logo、名字、祝福語皆可｜$228 起｜最少 3 日前預訂</div></div></div></div>')

(HERE / 'kv-food-c.html').write_text('<style>' + CSS + '</style>' + C, encoding='utf-8')
(HERE / 'kv-food-d.html').write_text('<style>' + CSS + '</style>' + D, encoding='utf-8')
page = ('<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>激光打印食物 KV｜飲食媒體風格兩款</title>'
        '<style>body{margin:0;background:#E9E5DC;font-family:-apple-system,"PingFang HK",sans-serif;color:#222}.w{max-width:1280px;margin:0 auto;padding:24px 18px 60px}h1{font-size:20px;margin:0 0 4px}.nt{font-size:13px;color:#777;margin:0 0 20px}h2{font-size:16px;margin:30px 0 10px}'
        '.row{display:grid;grid-template-columns:minmax(0,1fr) 375px;gap:22px;align-items:start}.lab{font-size:12px;color:#888;margin:0 0 6px}@media(max-width:900px){.row{grid-template-columns:1fr}}' + CSS + '</style></head><body><div class="w">'
        '<h1>激光打印食物｜Blog KV 飲食媒體風格兩款</h1><p class="nt">相片：Kitchen AO 實拍（雷射包、馬卡龍）。請用瀏覽器開啟以載入相片。</p>'
        '<h2>C｜拱形相片（食譜雜誌頁）</h2><div class="row"><div><p class="lab">桌面 16:9</p>' + C + '</div><div><p class="lab">手機 4:5</p>' + C + '</div></div>'
        '<h2>D｜雙相頭條（飲食網站頭條）</h2><div class="row"><div><p class="lab">桌面 16:9</p>' + D + '</div><div><p class="lab">手機 4:5</p>' + D + '</div></div>'
        '</div></body></html>')
(HERE / 'KV飲食媒體風格兩款-激光打印食物.html').write_text(page, encoding='utf-8')
print('ok')
