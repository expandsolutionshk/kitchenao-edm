# B3 KV 三個方案（日曆保留）→ ../kv-b3-options.html
# A：媒體封面風（左邊插畫視覺＋右邊紅底疊字）；B：節慶插畫風（紅底、圓月、祥雲、山巒、青海波）；C：直排編排（kv_b3_styles s2）
import os, html, urllib.parse
import kv_b3, kv_b3_styles
HERE = os.path.dirname(os.path.abspath(__file__))
SER, SAN, LOGO = kv_b3.SER, kv_b3.SAN, kv_b3.LOGO
TXT = '食齋日初一十五食齋懶人包原因禁忌日子表＋何時開始？破戒怎麼辦？未來12個月自動更新・一次看清每月農曆宜忌茹素祈福葷腥五辛望日朔日'
FONT = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@900&family=Noto+Sans+TC:wght@500;700;900'
        '&display=swap&text=' + urllib.parse.quote(''.join(sorted(set(TXT)))) + '">')
CAL = kv_b3.cal()

# ── 插畫：齋菜碗（自繪 SVG）
BOWL = '''<svg class="bowl" viewBox="0 0 320 230" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
<ellipse cx="160" cy="214" rx="118" ry="12" fill="rgba(60,30,10,.18)"/>
<g stroke="#5B3A1E" stroke-width="5" stroke-linecap="round"><line x1="208" y1="40" x2="300" y2="6"/><line x1="214" y1="52" x2="308" y2="26"/></g>
<path d="M28 108 Q160 120 292 108 Q284 196 160 206 Q36 196 28 108Z" fill="#F7F1E4" stroke="#2E2A26" stroke-width="3"/>
<path d="M42 140 Q160 156 278 140" fill="none" stroke="#B5382B" stroke-width="5"/>
<path d="M50 152 Q160 168 270 152" fill="none" stroke="#B5382B" stroke-width="2"/>
<ellipse cx="160" cy="108" rx="132" ry="26" fill="#EDE2CB" stroke="#2E2A26" stroke-width="3"/>
<g stroke="#2E2A26" stroke-width="2.4">
<path d="M64 104 q-10 -34 20 -44 q8 22 -6 48z" fill="#4E8A45"/><path d="M84 106 q4 -40 34 -40 q-2 26 -20 44z" fill="#6FAE5A"/>
<rect x="104" y="78" width="34" height="30" rx="5" fill="#FFF8E6"/><rect x="132" y="86" width="32" height="28" rx="5" fill="#FBF0D6"/>
<ellipse cx="190" cy="86" rx="24" ry="13" fill="#8A5A34"/><path d="M182 96 q8 14 16 0" fill="#E9D7B8"/>
<ellipse cx="226" cy="98" rx="20" ry="11" fill="#7A4E2D"/>
<circle cx="168" cy="110" r="9" fill="#E8833A"/><circle cx="246" cy="112" r="8" fill="#E8833A"/>
<path d="M200 112 q20 -30 46 -22 q-10 22 -46 22z" fill="#4E8A45"/>
<circle cx="92" cy="118" r="6" fill="#F2D06B"/><circle cx="214" cy="122" r="5" fill="#F2D06B"/>
</g></svg>'''

# ── 插畫：祥雲、山巒、青海波
CLOUD = '''<svg class="cloud" viewBox="0 0 200 90" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><g fill="#FFF3E2" stroke="#E7A93B" stroke-width="3">
<path d="M20 70 q-18 -2 -14 -20 q4 -16 22 -12 q2 -22 26 -22 q20 0 26 18 q10 -14 28 -8 q18 6 14 26 q16 2 14 18 z"/></g>
<g fill="none" stroke="#E7A93B" stroke-width="3" stroke-linecap="round"><path d="M50 52 q0 -14 14 -14 q12 0 12 12 q0 9 -9 9 q-7 0 -7 -7"/><path d="M104 56 q0 -12 12 -12 q10 0 10 10 q0 7 -7 7"/></g>
<path d="M118 76 h70" stroke="#FFF3E2" stroke-width="4" stroke-linecap="round"/></svg>'''
MTN = '''<svg class="mtn" viewBox="0 0 1600 300" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
<path d="M0 170 L180 70 L330 150 L520 40 L700 160 L860 90 L1020 170 L1200 60 L1380 150 L1600 80 V300 H0Z" fill="#3C7A5A" stroke="#E7B95A" stroke-width="5"/>
<path d="M0 230 L220 120 L420 220 L640 110 L860 230 L1080 130 L1300 230 L1480 140 L1600 200 V300 H0Z" fill="#245541" stroke="#E7B95A" stroke-width="5"/>
<g stroke="rgba(231,185,90,.6)" stroke-width="3" fill="none"><path d="M520 40 L560 110 M1200 60 L1240 130 M180 70 L210 120"/></g></svg>'''
WAVE = '''<svg class="wave {cls}" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><defs>
<pattern id="sg{cls}" width="40" height="20" patternUnits="userSpaceOnUse"><g fill="none" stroke="{c}" stroke-width="2.2">
<circle cx="20" cy="20" r="18"/><circle cx="20" cy="20" r="12"/><circle cx="20" cy="20" r="6"/>
<circle cx="0" cy="10" r="18"/><circle cx="0" cy="10" r="12"/><circle cx="0" cy="10" r="6"/>
<circle cx="40" cy="10" r="18"/><circle cx="40" cy="10" r="12"/><circle cx="40" cy="10" r="6"/></g></pattern>
<clipPath id="cp{cls}"><circle cx="100" cy="100" r="100"/></clipPath></defs>
<rect width="200" height="200" fill="url(#sg{cls})" clip-path="url(#cp{cls})"/></svg>'''

PHOTO = 'https://images.pexels.com/photos/5848480/pexels-photo-5848480.jpeg?auto=compress&cs=tinysrgb&w=1200'
BASE = '.kx3 .pg.back .yj{display:none}.kx3 *{box-sizing:border-box}.kx3 .logo2 img{display:block!important;width:auto!important;max-width:none!important;margin:0!important;padding:0!important;border:0!important;box-shadow:none!important}'
CALCSS = kv_b3.CSS + kv_b3.CALCSS2  # 沿用日曆及 logo 樣式

A_CSS = f'''
.kx3.oa{{background:#F4E9D6}}.kx3.oa:before{{display:none}}
.kx3.oa .vis{{position:absolute;left:0;top:0;bottom:0;width:50%;background:#EDE3D2 url('{PHOTO}') 40% 50%/cover no-repeat;overflow:hidden}}
.kx3.oa .vis:after{{content:"";position:absolute;inset:0;background:linear-gradient(90deg,transparent 72%,rgba(142,27,23,.55)),linear-gradient(0deg,rgba(40,20,10,.25),transparent 35%)}}
.kx3.oa .rp{{position:absolute;right:0;top:0;bottom:0;width:50%;background:linear-gradient(160deg,#C2302A,#8E1B17);overflow:hidden}}
.kx3.oa .rp:before{{content:"";position:absolute;inset:0;background:radial-gradient(circle at 90% 10%,rgba(255,215,140,.18),transparent 45%),repeating-radial-gradient(circle at 100% 100%,rgba(255,255,255,.04) 0 .4cqw,transparent .4cqw 2cqw)}}
.kx3.oa .moon{{position:absolute;z-index:3;left:3.5cqw;bottom:3.5cqw;width:27cqw;height:27cqw;border-radius:50%;background:#FFF7EA;box-shadow:0 0 0 1cqw rgba(255,247,234,.35),0 1cqw 2.4cqw rgba(60,20,10,.25)}}.kx3.oa .cal{{left:8.6cqw;right:auto;top:auto;bottom:5.4cqw;width:16.8cqw;height:20.5cqw;transform:rotate(-5deg)}}.kx3.oa .cal .pg.back{{transform:rotate(-10deg) translate(-3.6cqw,.6cqw)}}.kx3.oa .cal .pg .hd{{font-size:1.3cqw;padding:2cqw 0 .9cqw}}.kx3.oa .cal .pg .num{{font-size:6cqw}}.kx3.oa .cal .pg.back .num{{font-size:4.4cqw}}.kx3.oa .cal .pg .yj div{{font-size:1.15cqw;padding:.6cqw 1.2cqw}}.kx3.oa .cal .pg .yj b{{width:2cqw;height:2cqw;font-size:1.1cqw}}.kx3.oa .cal .ring{{width:1.4cqw;height:2.6cqw;top:-1cqw}}.kx3.oa .cal .ring.a{{left:4cqw}}.kx3.oa .cal .ring.b{{right:4cqw}}
.kx3.oa .bowl{{position:absolute;z-index:7;left:19cqw;bottom:1.4cqw;width:25cqw}}
.kx3.oa .logo2{{left:2.6cqw;right:auto;top:2.6cqw}}
.kx3.oa .st{{position:absolute;z-index:6;left:53cqw;top:31cqw;display:flex;flex-direction:column;align-items:flex-start;gap:.8cqw}}
.kx3.oa .st span{{background:#fff;color:#B5382B;font:900 2.1cqw/1 {SAN};padding:.9cqw 1.4cqw;border:.3cqw solid #B5382B;box-shadow:.5cqw .5cqw 0 rgba(0,0,0,.25);transform:rotate(-6deg)}}
.kx3.oa .st span+span{{margin-left:3cqw;transform:rotate(-3deg)}}
.kx3.oa .ttl{{position:absolute;z-index:6;right:4.5cqw;top:5cqw;text-align:right}}
.kx3.oa .t1,.kx3.oa .t2{{display:block;font:900 7.6cqw/1.12 {SER};color:#fff;letter-spacing:.4cqw;text-shadow:0 .4cqw 0 rgba(0,0,0,.25);margin:0!important;padding:0!important;border:0!important;text-transform:none!important}}
.kx3.oa .t2{{font-size:6.2cqw}}
.kx3.oa .boxes{{display:flex;justify-content:flex-end;align-items:center;gap:.8cqw;margin-top:1.8cqw}}
.kx3.oa .boxes b{{background:#fff;color:#B5382B;font:900 5cqw/1 {SER};padding:.8cqw 1.2cqw;letter-spacing:.3cqw}}
.kx3.oa .boxes i{{font:900 4cqw/1 {SAN};color:#FFD98A;font-style:normal}}
.kx3.oa .t3{{display:block;margin-top:1.4cqw;font:900 6cqw/1.1 {SER};color:#fff;letter-spacing:.4cqw}}
.kx3.oa .ft{{position:absolute;z-index:6;right:4.5cqw;bottom:3.6cqw;font:900 2.4cqw/1 {SAN};color:#FFD98A;letter-spacing:.2cqw}}
@media(max-width:640px){{
 .kx3.oa .vis{{width:100%;bottom:auto;height:48%;background-position:70% 55%}}.kx3.oa .vis:after{{background:linear-gradient(0deg,rgba(142,27,23,.6),transparent 30%)}}.kx3.oa .rp{{width:100%;top:auto;height:52%}}
 .kx3.oa .moon{{left:5cqw;bottom:auto;top:20cqw;width:42cqw;height:42cqw}}.kx3.oa .cal{{left:14cqw;right:auto;top:24cqw;bottom:auto;width:24cqw;height:32cqw;transform:rotate(-5deg)}}.kx3.oa .cal .pg.back{{transform:rotate(-10deg) translate(-5.5cqw,1cqw)}}.kx3.oa .cal .pg .hd{{font-size:2.2cqw;padding:3.2cqw 0 1.4cqw}}.kx3.oa .cal .pg .num{{font-size:10.5cqw}}.kx3.oa .cal .pg.back .num{{font-size:8cqw}}.kx3.oa .cal .pg .yj div{{font-size:1.9cqw;padding:1cqw 2cqw}}.kx3.oa .cal .pg .yj b{{width:3.2cqw;height:3.2cqw;font-size:1.8cqw}}.kx3.oa .cal .ring{{width:2.2cqw;height:4cqw;top:-1.6cqw}}.kx3.oa .cal .ring.a{{left:6cqw}}.kx3.oa .cal .ring.b{{right:6cqw}}
 .kx3.oa .bowl{{left:auto;right:3cqw;bottom:auto;top:20cqw;width:46cqw}}
 .kx3.oa .logo2{{left:5cqw;top:5cqw}}
 .kx3.oa .st{{left:6cqw;top:62cqw}}.kx3.oa .st span{{font-size:3.4cqw;padding:1.4cqw 2.2cqw}}
 .kx3.oa .ttl{{right:6cqw;top:62cqw}}.kx3.oa .t1{{font-size:11cqw}}.kx3.oa .t2{{font-size:9cqw}}
 .kx3.oa .boxes{{margin-top:2.6cqw}}.kx3.oa .boxes b{{font-size:7cqw}}.kx3.oa .boxes i{{font-size:6cqw}}.kx3.oa .t3{{display:none}}
 .kx3.oa .ft{{right:6cqw;bottom:5cqw;font-size:3.6cqw}}
}}'''

def opt_a(tag='div'):
    return (f'<div class="kx3 oa"><div class="vis"></div><div class="rp"></div><div class="moon"></div>{LOGO}{CAL}'
            '<div class="st"><span>何時開始？</span><span>破戒怎麼辦？</span></div>'
            f'<div class="ttl"><{tag} class="t1">初一十五</{tag}><span class="t2">食齋懶人包</span>'
            '<div class="boxes"><b>原因</b><i>＋</i><b>禁忌</b></div><span class="t3">日子表</span></div>'
            '<div class="ft">未來 12 個月日子自動更新</div></div>')

B_CSS = f'''
.kx3.ob{{background:#D63A2F}}.kx3.ob:before{{display:none}}
.kx3.ob .wave{{position:absolute;z-index:1;opacity:.9}}
.kx3.ob .wave.w1{{left:-8cqw;top:-10cqw;width:26cqw}}.kx3.ob .wave.w2{{right:-6cqw;top:16cqw;width:20cqw}}
.kx3.ob .moon{{position:absolute;z-index:2;left:6cqw;top:7cqw;width:36cqw;height:36cqw;border-radius:50%;background:#FFF7EA;box-shadow:0 0 0 1.2cqw rgba(255,247,234,.18)}}
.kx3.ob .cal{{left:11cqw;right:auto;top:8.5cqw;transform:rotate(-5deg);width:24cqw;height:32cqw}}
.kx3.ob .cloud{{position:absolute;z-index:7;left:1.5cqw;top:38cqw;width:14cqw}}
.kx3.ob .mtn{{position:absolute;z-index:3;left:0;right:0;bottom:0;width:100%;height:13cqw}}
.kx3.ob .tb{{left:auto;right:5cqw;top:9cqw;transform:none;width:48cqw;text-align:center}}
.kx3.ob .kick{{border:0;color:#FFE2B8;font:700 2cqw/1 {SAN};letter-spacing:.5cqw}}
.kx3.ob .big{{color:#fff;font:900 7.4cqw/1.1 {SAN}!important;letter-spacing:.5cqw;margin-top:1.4cqw!important}}
.kx3.ob .rule{{display:flex;align-items:center;gap:1cqw;margin:1.6cqw 3cqw}}.kx3.ob .rule:before,.kx3.ob .rule:after{{content:"";flex:1;height:.2cqw;background:#F2C46B}}
.kx3.ob .rule i{{width:1.2cqw;height:1.2cqw;background:#F2C46B;transform:rotate(45deg)}}
.kx3.ob .sub{{color:#fff;font:900 4.4cqw/1.25 {SAN};letter-spacing:.3cqw;white-space:normal}}
.kx3.ob .pill{{display:none}}
.kx3.ob .badge{{left:auto;right:4cqw;top:auto;bottom:10cqw;background:#F2C46B;color:#7A2A14;border:.3cqw solid #fff;z-index:8}}.kx3.ob .badge b{{color:#B5382B}}
.kx3.ob .dot{{position:absolute;z-index:2;border-radius:50%;background:#F2C46B}}
.kx3.ob .logo2{{border-color:#F2C46B}}
@media(max-width:640px){{
 .kx3.ob .moon{{left:50%;top:13cqw;width:62cqw;height:62cqw;transform:translateX(-50%)}}
 .kx3.ob .cal{{left:50%;top:15cqw;width:40cqw;height:52cqw;transform:translateX(-50%) rotate(-5deg)}}
 .kx3.ob .cloud{{left:2cqw;top:60cqw;width:22cqw}}.kx3.ob .wave.w1{{width:40cqw;left:-14cqw;top:-14cqw}}.kx3.ob .wave.w2{{width:30cqw;top:40cqw;right:-12cqw}}
 .kx3.ob .tb{{left:6cqw;right:6cqw;width:auto;top:79cqw}}.kx3.ob .kick{{display:none}}.kx3.ob .big{{font-size:11cqw!important;margin:0!important}}
 .kx3.ob .rule{{margin:2cqw 8cqw}}.kx3.ob .sub{{font-size:5.6cqw}}
 .kx3.ob .mtn{{height:16cqw}}.kx3.ob .badge{{right:5cqw;bottom:auto;top:52cqw;width:20cqw;height:20cqw;font-size:2.5cqw}}.kx3.ob .badge b{{font-size:5.2cqw}}
}}'''

def opt_b(tag='div'):
    dots = ''.join(f'<span class="dot" style="left:{x}cqw;top:{y}cqw;width:{s}cqw;height:{s}cqw"></span>' for x, y, s in ((46, 6, .9), (52, 30, .6), (90, 8, .7), (44, 38, .5)))
    return (f'<div class="kx3 ob">{WAVE.format(cls="w1", c="#F07A5E")}{WAVE.format(cls="w2", c="#F2C46B")}{dots}<div class="moon"></div>{LOGO}{CAL}{CLOUD}{MTN}'
            f'<div class="tb"><span class="kick">每月農曆初一・十五</span><{tag} class="big">初一十五食齋</{tag}><div class="rule"><i></i></div>'
            '<div class="sub">原因・禁忌・日子表<br>一次看清</div></div><div class="badge">12 個月<b>日子</b>自動更新</div></div>')

def block(opt, tag='div'):
    if opt == 'c':
        return kv_b3_styles.block('s2', tag)
    h, css = (opt_a(tag), A_CSS) if opt == 'a' else (opt_b(tag), B_CSS)
    return f'<div class="ao-b3kv" style="margin:0 0 22px">{FONT}<style>{(CALCSS + BASE + css).replace(chr(10), "")}</style>{h}</div>'

OPTS = [('a', 'A｜媒體封面風（參考圖 1）', '左邊換成真實齋菜相片（雲耳炒豆腐配筷子），撕日曆縮細放在相片左下，下面墊一個米白色圓形底，右邊深紅底配白色粗宋體疊字、白底紅字方格及斜貼「何時開始？」「破戒怎麼辦？」貼紙，底部金色一行「未來 12 個月日子自動更新」。'),
        ('b', 'B｜節慶插畫風（參考圖 2）', '朱紅底，左邊大白色圓月托住撕日曆，旁邊一朵祥雲；角落用青海波紋，底部綠色山巒配金邊，右邊白色粗黑體標題、金色分隔線，圓章改金色放右下。'),
        ('c', 'C｜直排編排（稿紙格＋印章）', '標題改中式直排放右邊，淡紅稿紙格線做背景，圓章換成朱紅方印「齋」，墨黑＋朱砂兩色，留白多，似書籍封面。')]

if __name__ == '__main__':
    secs = []
    for k, t, d in OPTS:
        doc = f'<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body style="margin:0;padding:10px;background:#fff">{block(k)}</body></html>'
        secs.append(f'<section><h3>{t}</h3><p>{d}</p><div class="pair"><div><small>桌面</small><iframe srcdoc="{html.escape(doc)}" style="width:860px;height:510px"></iframe></div>'
                    f'<div><small>手機</small><iframe srcdoc="{html.escape(doc)}" style="width:390px;height:510px"></iframe></div></div></section>')
    page = f'''<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="robots" content="noindex"><title>B3 KV 三個方案</title><style>body{{margin:0;background:#EEF1EA;font:15px/1.6 -apple-system,"PingFang HK",sans-serif;color:#222}}.wrap{{max-width:1300px;margin:0 auto;padding:20px 16px 50px}}section{{margin:0 0 30px}}h3{{margin:0 0 4px}}section>p{{margin:0 0 8px;color:#555}}.pair{{display:flex;gap:14px;flex-wrap:wrap}}small{{display:block;font-weight:700;color:#7a6a45}}iframe{{border:1px solid #ddd;border-radius:8px;background:#fff}}</style></head><body><div class="wrap"><h1 style="font-size:21px">B3 KV｜三個方案（日曆保留）</h1>{"".join(secs)}</div></body></html>'''
    open(os.path.join(HERE, '..', 'kv-b3-options.html'), 'w', encoding='utf-8').write(page)
    print('ok')
