# -*- coding: utf-8 -*-
"""Blog 2 聖誕派對食物 KV：2 個方案（雜誌 Media style，桌面 16:9／手機 4:5）
用法：python3 kv_xmas.py <輸出 html>"""
import sys, urllib.parse
sys.path.insert(0, '/sessions/great-festive-darwin/mnt/kitchenao-edm/vegetarian-blog/src')
from brush import brush
from kv import LOGO
OUT = sys.argv[1]

def u(p, w=900, h=900): return f'https://images.unsplash.com/{p}?w={w}&h={h}&fit=crop&crop=entropy&q=80&auto=format'
TURKEY, BEEF, CAKE, MAC, GINGER = ('photo-1763689454945-4b0f3b151969', 'photo-1529692236671-f1f6cf9683ba',
    'photo-1766585449820-01a8fa6f1473', 'photo-1543921879-815164944436', 'photo-1771274023071-9d37360a6638')
TXT = '聖誕派對食物指南香港人吃甚麼？小食・主菜・甜品・蛋糕附份量公式及預算參考文：Kitchen AO 編輯部香烤火雞香草燒牛肉聖誕忌廉蛋糕聖誕馬卡龍薑餅人2026'
SUB = urllib.parse.quote(''.join(sorted(set(TXT))))
FONT = (f'<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Chiron+Sung+HK:wght@700;900&family=LXGW+WenKai+TC:wght@700'
        f'&display=swap&text={SUB}"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Pinyon+Script'
        f'&family=Playfair+Display:ital,wght@1,700&family=Cormorant+Garamond:wght@600&display=swap">')
SF = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2v20M3.3 7l17.4 10M3.3 17L20.7 7M12 5l-2-2M12 5l2-2M12 19l-2 2M12 19l2 2" '
      'stroke="currentColor" stroke-width="1.3" fill="none" stroke-linecap="round"/></svg>')
HOLLY = ('<svg viewBox="0 0 48 24" aria-hidden="true"><path d="M24 12c-6-8-14-8-20-4 4 1 6 4 6 7 4-3 9-4 14-3zM24 12c6-8 14-8 20-4-4 1-6 4-6 7-4-3-9-4-14-3z" fill="#2F5D3A"/>'
         '<circle cx="21" cy="13" r="3" fill="#B03426"/><circle cx="27" cy="13" r="3" fill="#B03426"/><circle cx="24" cy="9" r="3" fill="#C9372A"/></svg>')
SER1 = '"Chiron Sung HK","Noto Serif TC","Songti TC",serif'
SER2 = '"LXGW WenKai TC","Kaiti TC","STKaiti",serif'

CSS = '''
.k{position:relative;width:100%;aspect-ratio:16/9;container-type:inline-size;overflow:hidden;font-family:-apple-system,"PingFang HK",sans-serif}
.k *{box-sizing:border-box}.k p{margin:0}
.k .logo2{position:absolute;right:1.8cqw;top:1.8cqw;z-index:6;display:inline-flex;align-items:center;height:4.3cqw;background:#fff;border-radius:3cqw;padding:0 1.8cqw;line-height:0}
.k .logo2 img{display:block;width:auto}.k .logo2 .li{height:2.3cqw}.k .logo2 .lt{height:2cqw;margin-left:1cqw}
/* ===== Option 1 黑金雜誌 ===== */
.k1{background:radial-gradient(90% 120% at 15% 0%,#3a2c18 0,#141414 60%)}
.k1:before{content:"";position:absolute;inset:0;background-image:radial-gradient(#ffffff1f 1.1px,transparent 1.5px),radial-gradient(#F7CE462a 1px,transparent 1.4px);background-size:2.6cqw 2.6cqw,1.6cqw 1.6cqw;background-position:0 0,.8cqw 1.1cqw}
.k1 .g{position:absolute;top:0;right:0;bottom:0;width:46%;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:.45cqw;background:#C8A24A}
.k1 .g>div{position:relative;background-size:cover;background-position:center}
.k1 .g span{position:absolute;left:.6cqw;bottom:1.4cqw;transform:rotate(-2deg);white-space:nowrap;background:none no-repeat center/100% 100%;padding:.8cqw 3.4cqw .9cqw 3cqw;color:#fff;font:900 1.9cqw/1.2 ''' + SER1 + ''';letter-spacing:.15cqw;filter:drop-shadow(0 .3cqw .5cqw rgba(0,0,0,.25))}
.k1 .g span.gd{color:#1A1A1A}
.k1 .tb{position:absolute;left:5cqw;top:50%;transform:translateY(-50%);width:44cqw;z-index:2}
.k1 .kick{display:flex;align-items:center;gap:1.2cqw;font-size:1.5cqw;letter-spacing:.3cqw;color:#C8A24A}
.k1 .kick b{color:#fff;background:none no-repeat center/100% 100%;padding:.5cqw 2.8cqw .6cqw;font-weight:800}
.k1 .kick i{flex:0 0 5cqw;height:.15cqw;background:#C8A24A}
.k1 .scr{font:4.6cqw/1 "Pinyon Script",cursive;color:#C8A24A;margin:2cqw 0 .4cqw -.3cqw}
.k1 .ttl{font:900 5.2cqw/1.22 ''' + SER1 + ''';color:#fff;letter-spacing:.15cqw;white-space:nowrap}
.k1 .ttl em{position:relative;display:inline-block;font-style:normal;color:#fff;background:linear-gradient(180deg,#D0402F,#9E2A20);padding:.5cqw 4.4cqw .75cqw;margin:.8cqw 0 0 -.4cqw;line-height:1.15;clip-path:polygon(0 0,100% 0,95.5% 50%,100% 100%,0 100%,4.5% 50%);text-shadow:0 .2cqw .4cqw rgba(0,0,0,.25)}
.k1 .ttl em:before{content:"";position:absolute;left:3cqw;right:3cqw;top:.45cqw;bottom:.45cqw;border-top:.14cqw dashed #F7CE46;border-bottom:.14cqw dashed #F7CE46;pointer-events:none}
.k1 .rib{position:relative;display:inline-block}
.k1 .rib .hl{position:absolute;right:-3.2cqw;top:-.6cqw;width:5.4cqw;z-index:2;transform:rotate(12deg)}.k1 .rib .hl svg{display:block;width:100%}
.k1 .rib .sp{position:absolute;color:#F7CE46;font-size:1.5cqw;line-height:1}
.k1 .dek{margin-top:2.2cqw;font-size:1.75cqw;line-height:1.7;color:#E8DFCC;letter-spacing:.08cqw}
.k1 .dek b{color:#F7CE46;font-weight:700}
.k1 .by{margin-top:2cqw;font-size:1.2cqw;color:#9A8f7e;letter-spacing:.15cqw}
.k1 .sf{position:absolute;color:#C8A24A;opacity:.55;z-index:1}.k1 .sf svg{display:block;width:100%}
/* ===== Option 2 象牙餐牌雜誌 ===== */
.k2{background:#FBF6EA}
.k2 .fr{position:absolute;inset:1.6cqw;border:.12cqw solid #C8A24A;outline:.35cqw double #C8A24A;outline-offset:.6cqw;pointer-events:none;z-index:4}
.k2 .arch{position:absolute;right:7cqw;top:5.5cqw;bottom:5.5cqw;width:33cqw;border-radius:16.5cqw 16.5cqw 1cqw 1cqw;background-size:cover;background-position:center;box-shadow:0 1.2cqw 3cqw rgba(60,40,15,.18)}
.k2 .dot{position:absolute;width:15cqw;height:15cqw;border-radius:50%;background-size:cover;background-position:center;border:.6cqw solid #FBF6EA;box-shadow:0 .8cqw 2cqw rgba(60,40,15,.2);z-index:3}
.k2 .d1{right:34cqw;bottom:6cqw}.k2 .d2{right:2.6cqw;top:6.5cqw;width:11cqw;height:11cqw}
.k2 .cap{position:absolute;z-index:5;font:700 1.35cqw/1 ''' + SER2 + ''';color:#fff;background:#B03426;padding:.6cqw 1.4cqw;border-radius:2cqw;letter-spacing:.15cqw}
.k2 .c1{right:37cqw;bottom:5.4cqw}.k2 .c2{right:9cqw;bottom:7.5cqw;background:#1A1A1A;color:#F7CE46}
.k2 .tb{position:absolute;left:6.5cqw;top:50%;transform:translateY(-50%);width:44cqw;z-index:2}
.k2 .holly{width:5.6cqw;margin:0 0 1cqw}.k2 .holly svg{display:block;width:100%}
.k2 .kick{font:600 1.45cqw/1 "Cormorant Garamond",serif;letter-spacing:.55cqw;color:#9A7B2E}
.k2 .scr{font:italic 700 5.6cqw/1 "Playfair Display",serif;color:#B03426;margin:1.6cqw 0 .6cqw -.2cqw;letter-spacing:-.1cqw}
.k2 .ttl{font:700 4.5cqw/1.25 ''' + SER2 + ''';color:#1A1A1A;letter-spacing:.2cqw;white-space:nowrap}
.k2 .orn{color:#C8A24A;margin:1.6cqw 0 1.2cqw;font-size:1.6cqw;letter-spacing:.6cqw}
.k2 .dek{font-size:1.75cqw;line-height:1.7;color:#4A4238}
.k2 .by{margin-top:1.6cqw;font-size:1.2cqw;color:#9A8f7e;letter-spacing:.15cqw}
.k2 .logo2{right:auto;left:50%;transform:translateX(-50%);top:auto;bottom:.6cqw;border:.2cqw solid #E6D3A6;height:3.4cqw}
.k2 .logo2 .li{height:1.8cqw}.k2 .logo2 .lt{height:1.6cqw}
/* ===== 手機 4:5 ===== */
.m .k{aspect-ratio:4/5}
.m .k .logo2{height:7.5cqw;padding:0 3cqw;right:4cqw;top:4cqw}.m .k .logo2 .li{height:4cqw}.m .k .logo2 .lt{height:3.4cqw;margin-left:1.6cqw}
.m .k1 .g{top:auto;left:0;width:100%;height:39%;gap:.6cqw;grid-template-columns:repeat(4,1fr);grid-template-rows:1fr}
.m .k1 .g span{font-size:2.5cqw;padding:1cqw 2.6cqw 1.1cqw 2.4cqw;left:50%;bottom:2.4cqw;transform:translateX(-50%) rotate(-2deg);letter-spacing:0}
.m .k1 .tb{left:6cqw;right:6cqw;width:auto;top:11.5cqw;transform:none}
.m .k1 .kick{font-size:3cqw}.m .k1 .kick b{padding:.9cqw 4.4cqw 1cqw}.m .k1 .kick i{flex-basis:8cqw;height:.3cqw}
.m .k1 .scr{font-size:8.2cqw;margin-top:2.6cqw}.m .k1 .ttl{font-size:9.6cqw}.m .k1 .ttl em{padding:1cqw 7cqw 1.4cqw}.m .k1 .ttl em:before{left:5cqw;right:5cqw;top:.8cqw;bottom:.8cqw;border-width:.28cqw}.m .k1 .rib .hl{width:9cqw;right:-5cqw;top:-1.4cqw}.m .k1 .rib .sp{font-size:2.6cqw}.m .k1 .dek{font-size:3.6cqw;line-height:1.6;margin-top:2.6cqw}.m .k1 .by{display:none}
.m .k2 .fr{inset:3cqw;outline-width:.6cqw;outline-offset:1cqw;border-width:.25cqw}
.m .k2 .arch{right:auto;left:22cqw;top:auto;bottom:7cqw;width:56cqw;height:46cqw;border-radius:28cqw 28cqw 2cqw 2cqw}
.m .k2 .dot{width:24cqw;height:24cqw;border-width:1cqw}.m .k2 .d1{right:auto;left:7cqw;bottom:9cqw}.m .k2 .d2{right:7cqw;top:auto;bottom:34cqw;width:20cqw;height:20cqw}
.m .k2 .cap{font-size:2.6cqw;padding:1.1cqw 2.6cqw}.m .k2 .c1{right:auto;left:8cqw;bottom:7cqw}.m .k2 .c2{right:9cqw;bottom:9cqw}
.m .k2 .tb{left:9cqw;right:9cqw;width:auto;top:9cqw;transform:none;text-align:center}
.m .k2 .holly{width:10cqw;margin:0 auto 1.6cqw}.m .k2 .kick{font-size:2.6cqw;letter-spacing:.8cqw}.m .k2 .scr{font-size:10cqw;margin:2.4cqw 0 1cqw}
.m .k2 .ttl{font-size:7.6cqw}.m .k2 .orn{display:none}.m .k2 .dek{font-size:3.3cqw;margin-top:2cqw}.m .k2 .by{display:none}
.m .k2 .logo2{bottom:auto;top:auto;left:50%;bottom:1.2cqw;height:6cqw}.m .k2 .logo2 .li{height:3.2cqw}.m .k2 .logo2 .lt{height:2.8cqw}
'''
def k1():
    tags = [(TURKEY, '香烤火雞', '#B03426', ''), (BEEF, '香草燒牛肉', '#C8A24A', 'gd'), (CAKE, '聖誕忌廉蛋糕', '#C8A24A', 'gd'), (MAC, '聖誕馬卡龍', '#B03426', '')]
    g = '<div class="g">' + ''.join(f'<div style="background-image:url({u(p)})"><span class="{c}" style="background-image:{brush(col, seed=k + 7, opacity=.95)}">{n}</span></div>'
                                    for k, (p, n, col, c) in enumerate(tags)) + '</div>'
    sfs = ''.join(f'<span class="sf" style="{s}">{SF}</span>' for s in ('left:2.4cqw;top:3cqw;width:2.6cqw', 'left:46cqw;bottom:4cqw;width:1.8cqw', 'left:40cqw;top:5cqw;width:1.4cqw'))
    return (f'<div class="k k1">{g}{sfs}{LOGO}<div class="tb">'
            f'<p class="kick"><b style="background-image:{brush("#B03426", seed=3, opacity=.95)}">聖誕派對食物指南</b><i></i>2026</p>'
            f'<p class="scr">Christmas Feast</p>'
            f'<p class="ttl">香港人聖誕派對<br><span class="rib"><em>吃甚麼？</em><span class="hl">{HOLLY}</span><span class="sp" style="left:-2cqw;top:.4cqw">✦</span><span class="sp" style="right:-4.6cqw;bottom:.2cqw;font-size:1cqw">✦</span></span></p>'
            f'<p class="dek"><b>小食・主菜・甜品・蛋糕</b><br>附份量公式及預算參考</p><p class="by">文：Kitchen AO 編輯部</p></div></div>')
def k2():
    return (f'<div class="k k2"><div class="arch" style="background-image:url({u(TURKEY, 900, 1100)})"></div>'
            f'<div class="dot d1" style="background-image:url({u(CAKE, 500, 500)})"></div><div class="dot d2" style="background-image:url({u(GINGER, 500, 500)})"></div>'
            f'<span class="cap c1">聖誕忌廉蛋糕</span><span class="cap c2">香烤火雞</span>'
            f'<div class="fr"></div>{LOGO}<div class="tb"><div class="holly">{HOLLY}</div>'
            f'<p class="kick">CHRISTMAS PARTY FOOD · 2026</p><p class="scr">Merry Feast</p>'
            f'<p class="ttl">香港人聖誕派對<br>吃甚麼？</p><p class="orn">— ✧ —</p>'
            f'<p class="dek">小食・主菜・甜品・蛋糕<br>附份量公式及預算參考</p><p class="by">文：Kitchen AO 編輯部</p></div></div>')
def pair(fn, name, note):
    return (f'<section><h2>{name}</h2><p class="nt">{note}</p><div class="row"><div class="d"><small>桌面 16:9（1600×900）</small>{fn()}</div>'
            f'<div class="m"><small>手機 4:5（1080×1350）</small>{fn()}</div></div></section>')
page = f'''<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>B2 聖誕派對食物 KV｜2 個方案</title>{FONT}
<style>body{{margin:0;background:#EFEBE2;font:15px/1.6 -apple-system,"PingFang HK",sans-serif;color:#222}}.wrap{{max-width:1320px;margin:0 auto;padding:22px 16px 60px}}
h1{{font-size:22px}}h2{{font-size:18px;margin:34px 0 2px}}.nt{{margin:0 0 10px;color:#5d534d}}.row{{display:flex;gap:18px;align-items:flex-start;flex-wrap:wrap}}.row .d{{flex:1 1 760px;min-width:300px}}.row .m{{flex:0 0 380px}}
.row small{{display:block;font-weight:700;color:#7a6a45;margin:0 0 6px}}{CSS}</style></head><body><div class="wrap">
<h1>Blog 2 聖誕派對食物｜KV 2 個方案（雜誌 Media style）</h1>
<p class="nt">沿用素食 Blog 雜誌式 KV 結構：左邊 kicker、標題、副題、作者；右邊食物相片。食物相片暫用 Unsplash，正式版建議換成 Kitchen AO 寶箱牛及原隻燒雞實拍。設計參考 Four Seasons Sydney（https://www.fourseasons.com/sydney/）：留白、細金線。</p>
{pair(k1, 'Option 1｜黑金雜誌（港式明體＋英文花體）', '字體：標題「Chiron Sung HK」港式明體 900、英文「Pinyon Script」花體；右邊 2×2 食物格配金色間線及紅金筆刷標籤，「吃甚麼？」用紅色聖誕絲帶（燕尾兩端、金色虛線車邊、冬青果及金星點綴）。同 Blog 黑金 CTA 一致。')}
{pair(k2, 'Option 2｜象牙餐牌雜誌（楷書＋Playfair 斜體）', '字體：標題「LXGW WenKai TC」霞鶩文楷（手寫楷書感）、英文「Playfair Display」斜體紅字；雙金框同 Kitchen AO 精選餐牌卡一致，拱形主相＋兩個圓形小相，冬青果點綴。')}
</div></body></html>'''
open(OUT, 'w', encoding='utf-8').write(page)
print('ok', len(page))
