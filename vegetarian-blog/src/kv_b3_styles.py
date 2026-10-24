# B3 KV 三款設計風格（元素不變：撕日曆、標題、標籤、圓章、logo）→ ../kv-b3-styles.html
import os, html, urllib.parse
import kv_b3
HERE = os.path.dirname(os.path.abspath(__file__))
SER, SAN = kv_b3.SER, kv_b3.SAN
TXT = kv_b3.TXT + '齋初一十五每月農曆'
FONT = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@500;900&family=Noto+Sans+TC:wght@500;900'
        '&display=swap&text=' + urllib.parse.quote(''.join(sorted(set(TXT)))) + '">')

STYLES = {
# ───────── S1 港式柯式印刷（Riso 雙色套印）
's1': ('S1｜港式柯式印刷（雙色套印）',
 '只用朱紅＋墨綠兩色，配報紙底色及網點質感；標題及日曆數字有輕微「套印錯位」，似舊式街招／月曆印刷，平面、無立體陰影。',
 f'''
.kx3.s1{{background-color:#F2ECDD;background-image:radial-gradient(rgba(31,78,61,.16) .22cqw,transparent .26cqw);background-size:1.1cqw 1.1cqw}}
.kx3.s1:before{{inset:1.6cqw;border:.35cqw solid #1F4E3D;outline:0}}
.kx3.s1 .kick{{color:#1F4E3D;border:0;background:#E5533F;color:#F2ECDD;padding:.8cqw 1.4cqw;letter-spacing:.35cqw}}
.kx3.s1 .big{{color:#1F4E3D;text-shadow:.45cqw .35cqw 0 rgba(229,83,63,.9);font-size:7cqw}}
.kx3.s1 .sub{{color:#E5533F;text-shadow:.3cqw .25cqw 0 rgba(31,78,61,.55)}}
.kx3.s1 .pill{{background:transparent;border:.3cqw solid #1F4E3D;color:#1F4E3D;box-shadow:.5cqw .5cqw 0 #E5533F;border-radius:.4cqw}}
.kx3.s1 .pill:before{{content:"●";color:#E5533F;font-size:1.4cqw}}
.kx3.s1 .badge{{background:#E5533F;border:0;border-radius:0;box-shadow:none;clip-path:polygon(50% 0,61% 12%,76% 6%,79% 22%,94% 24%,88% 39%,100% 50%,88% 61%,94% 76%,79% 78%,76% 94%,61% 88%,50% 100%,39% 88%,24% 94%,21% 78%,6% 76%,12% 61%,0 50%,12% 39%,6% 24%,21% 22%,24% 6%,39% 12%);color:#F2ECDD}}
.kx3.s1 .badge b{{color:#F2ECDD}}
.kx3.s1 .cal:before{{content:"";position:absolute;left:50%;top:50%;width:31cqw;height:31cqw;transform:translate(-50%,-50%);border-radius:50%;background:radial-gradient(#E5533F .32cqw,transparent .36cqw) 0 0/1cqw 1cqw;opacity:.55;z-index:-1}}
.kx3.s1 .pg{{box-shadow:.9cqw .9cqw 0 #1F4E3D;border:.25cqw solid #1F4E3D;border-radius:.4cqw;background:#FBF7EC}}
.kx3.s1 .pg.back{{background:#EFE6D3}}
.kx3.s1 .pg .hd{{background:#E5533F;color:#F2ECDD;border-bottom:.25cqw solid #1F4E3D}}
.kx3.s1 .pg.front .num{{color:#1F4E3D;text-shadow:.5cqw .4cqw 0 rgba(229,83,63,.85)}}
.kx3.s1 .pg .yj{{border-top:.25cqw solid #1F4E3D}}.kx3.s1 .pg .yj div+div{{border-top:.2cqw solid #1F4E3D}}
.kx3.s1 .pg .yj b{{background:#1F4E3D;border-radius:.3cqw}}.kx3.s1 .pg .yj div+div b{{background:#E5533F}}
.kx3.s1 .ring{{background:#1F4E3D;box-shadow:none}}
@media(max-width:640px){{.kx3.s1{{background-size:2.2cqw 2.2cqw}}.kx3.s1 .big{{font-size:12.5cqw}}.kx3.s1 .cal:before{{width:56cqw;height:56cqw;background-size:1.9cqw 1.9cqw}}}}
'''),
# ───────── S2 直排書法編排（稿紙格＋印章）
's2': ('S2｜直排編排（稿紙格＋印章）',
 '標題改為中式直排，放在右邊；背景是淡紅原稿紙格線；圓章換成朱紅方印「齋」，墨黑＋朱砂兩色，留白多，似書籍封面。',
 f'''
.kx3.s2{{background-color:#F6F2E9;background-image:linear-gradient(rgba(192,57,43,.14) .12cqw,transparent .12cqw),linear-gradient(90deg,rgba(192,57,43,.14) .12cqw,transparent .12cqw);background-size:4cqw 4cqw;background-position:2cqw 2cqw}}
.kx3.s2:before{{inset:2cqw;border:.2cqw solid #C0392B;outline:0}}
.kx3.s2 .tb{{left:auto;right:6cqw;top:7.5cqw;transform:none;width:auto;height:44cqw;writing-mode:vertical-rl;display:flex;flex-direction:column;align-items:flex-start;gap:1.6cqw}}.kx3.s2 .pg.back .yj{{display:none}}
.kx3.s2 .kick{{white-space:nowrap;border:0;border-left:.2cqw solid #C0392B;padding:0 0 0 .8cqw;color:#C0392B;font:500 1.7cqw/1 {SER};letter-spacing:.6cqw}}
.kx3.s2 .big{{margin:0!important;font:900 6cqw/1.05 {SER}!important;color:#1C1C1C;letter-spacing:.4cqw;white-space:nowrap}}
.kx3.s2 .sub{{white-space:nowrap;margin:0;font:900 3.6cqw/1 {SER};color:#C0392B;letter-spacing:.6cqw}}
.kx3.s2 .pill{{white-space:nowrap;margin:0;writing-mode:vertical-rl;background:#1C1C1C;color:#F6F2E9;border:0;box-shadow:none;border-radius:0;padding:1.6cqw .9cqw;font:500 1.6cqw/1 {SAN};letter-spacing:.4cqw}}
.kx3.s2 .pill:before{{display:none}}
.kx3.s2 .badge{{left:auto;right:31cqw;top:auto;bottom:6cqw;width:9cqw;height:9cqw;border-radius:.6cqw;background:#C0392B;border:.3cqw solid #F6F2E9;outline:.2cqw solid #C0392B;box-shadow:none;transform:rotate(-6deg);font:500 1.2cqw/1.3 {SAN}}}
.kx3.s2 .badge:before{{content:"齋";display:block;font:900 3.6cqw/1 {SER};color:#F6F2E9;margin-bottom:.3cqw}}
.kx3.s2 .badge b{{display:none}}
.kx3.s2 .cal{{right:auto;left:12cqw;top:53%}}
.kx3.s2 .pg{{border-radius:.2cqw;box-shadow:0 .2cqw 0 rgba(0,0,0,.08),0 1.6cqw 2.4cqw -1cqw rgba(60,30,10,.25);background:#FFFDF7}}
.kx3.s2 .pg .hd{{background:#C0392B;font:500 1.6cqw/1 {SER};letter-spacing:.8cqw}}
.kx3.s2 .pg.front .num{{color:#1C1C1C;font-family:{SER}}}
.kx3.s2 .pg .yj{{border-top:.15cqw solid #1C1C1C}}.kx3.s2 .pg .yj div+div{{border-top:.15cqw solid #E5DCCB}}
.kx3.s2 .pg .yj b{{background:transparent;color:#1C1C1C;border:.15cqw solid #1C1C1C;border-radius:0}}.kx3.s2 .pg .yj div+div b{{color:#C0392B;border-color:#C0392B;background:transparent}}
.kx3.s2 .ring{{background:#1C1C1C}}
.kx3.s2 .logo2{{left:4cqw;right:auto;top:4cqw;border-color:#E5DCCB}}
@media(max-width:640px){{
 .kx3.s2{{background-size:7.5cqw 7.5cqw;background-position:3cqw 3cqw}}
 .kx3.s2 .tb{{right:6cqw;top:18cqw;height:94cqw;gap:2.2cqw}}
 .kx3.s2 .kick{{font-size:3cqw}}.kx3.s2 .big{{font-size:11cqw!important}}.kx3.s2 .sub{{font-size:6.4cqw}}.kx3.s2 .pill{{font-size:3cqw;padding:3cqw 1.6cqw}}
 .kx3.s2 .cal{{left:7cqw;bottom:auto;top:30cqw;transform:none;width:44cqw;height:52cqw}}
 .kx3.s2 .badge{{right:auto;left:30cqw;bottom:8cqw;width:16cqw;height:16cqw;font-size:2.2cqw}}.kx3.s2 .badge:before{{font-size:6.4cqw}}
 .kx3.s2 .logo2{{left:6cqw;top:6cqw}}
}}
'''),
# ───────── S3 現代分割版面（色塊＋超大字）
's3': ('S3｜現代分割版面（色塊＋超大字）',
 '左邊深綠色塊、右邊米色，日曆跨越兩邊；背景用超大鏤空「十五」字做紋理，芥末黃點綴，平面無陰影，最似雜誌／品牌海報。',
 f'''
.kx3.s3{{background:linear-gradient(90deg,#1E4A3B 0 57%,#F3EADB 57% 100%)}}
.kx3.s3:before{{display:none}}
.kx3.s3 .bgn{{position:absolute;z-index:1;left:-2cqw;bottom:-9cqw;font:900 34cqw/1 {SER};color:transparent;-webkit-text-stroke:.18cqw rgba(243,234,219,.16);letter-spacing:-1cqw;pointer-events:none;white-space:nowrap}}
.kx3.s3 .tb{{left:6cqw;width:46cqw}}
.kx3.s3 .kick{{color:#E8B04B;border-color:#E8B04B}}
.kx3.s3 .big{{color:#F3EADB}}
.kx3.s3 .sub{{color:#E8B04B}}
.kx3.s3 .pill{{background:#E8B04B;color:#1E4A3B;border:0;box-shadow:none;border-radius:0}}
.kx3.s3 .pill:before{{content:"→";font-size:2cqw}}
.kx3.s3 .badge{{left:auto;right:4.5cqw;top:auto;bottom:5cqw;background:#F3EADB;color:#1E4A3B;border:.3cqw solid #1E4A3B;box-shadow:none}}
.kx3.s3 .badge b{{color:#B5382B}}
.kx3.s3 .cal{{right:auto;left:51cqw;top:50%}}
.kx3.s3 .pg{{border-radius:0;box-shadow:1cqw 1cqw 0 rgba(0,0,0,.18)}}
.kx3.s3 .pg.back{{background:#E8B04B}}.kx3.s3 .pg.back .num{{color:rgba(30,74,59,.45)}}.kx3.s3 .pg.back .hd{{background:#1E4A3B}}
.kx3.s3 .pg .hd{{background:#B5382B}}
.kx3.s3 .pg .yj b{{border-radius:0}}
.kx3.s3 .ring{{background:#1E1E1E}}
.kx3.s3 .logo2{{border-color:#E5D9C4}}
@media(max-width:640px){{
 .kx3.s3{{background:linear-gradient(180deg,#1E4A3B 0 55%,#F3EADB 55% 100%)}}
 .kx3.s3 .bgn{{font-size:60cqw;left:-4cqw;bottom:auto;top:30cqw}}
 .kx3.s3 .tb{{left:8cqw;right:8cqw;width:auto}}
 .kx3.s3 .cal{{left:50%;bottom:6cqw;top:auto;transform:translateX(-50%)}}
 .kx3.s3 .badge{{right:6cqw;bottom:50cqw}}
}}
'''),
}

def block(style, tag='div'):
    h = kv_b3.kv(tag).replace('class="kx3"', f'class="kx3 {style}"', 1)
    if style == 's3':
        h = h.replace(kv_b3.LOGO, kv_b3.LOGO + '<span class="bgn">十五</span>', 1)
    css = (kv_b3.CSS + kv_b3.CALCSS2 + STYLES[style][2]).replace('\n', '')
    return f'<div class="ao-b3kv" style="margin:0 0 22px">{FONT}<style>{css}</style>{h}</div>'

if __name__ == '__main__':
    secs = []
    for k, (t, d, _) in STYLES.items():
        doc = f'<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body style="margin:0;padding:10px;background:#fff">{block(k)}</body></html>'
        secs.append(f'<section><h3>{t}</h3><p>{d}</p><div class="pair"><div><small>桌面</small><iframe srcdoc="{html.escape(doc)}" style="width:860px;height:510px"></iframe></div>'
                    f'<div><small>手機</small><iframe srcdoc="{html.escape(doc)}" style="width:390px;height:510px"></iframe></div></div></section>')
    page = f'''<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="robots" content="noindex"><title>B3 KV 三款風格</title><style>body{{margin:0;background:#EEF1EA;font:15px/1.6 -apple-system,"PingFang HK",sans-serif;color:#222}}.wrap{{max-width:1300px;margin:0 auto;padding:20px 16px 50px}}section{{margin:0 0 30px}}h3{{margin:0 0 4px}}section>p{{margin:0 0 8px;color:#555}}.pair{{display:flex;gap:14px;flex-wrap:wrap}}small{{display:block;font-weight:700;color:#7a6a45}}iframe{{border:1px solid #ddd;border-radius:8px;background:#fff}}</style></head><body><div class="wrap"><h1 style="font-size:21px">B3 KV｜同一組元素、三款設計風格</h1>{"".join(secs)}</div></body></html>'''
    open(os.path.join(HERE, '..', 'kv-b3-styles.html'), 'w', encoding='utf-8').write(page)
    print('ok')
