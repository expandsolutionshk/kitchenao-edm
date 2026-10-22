# B2 KV 外框：媒體／雜誌風格（2 款）→ ../kv-b2-frame-options-v3.html
import os, html, urllib.parse
import kv_mag
HERE = os.path.dirname(os.path.abspath(__file__))
U = lambda s: "url('data:image/svg+xml," + urllib.parse.quote(s) + "')"
SPRIG = U('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><g stroke="#2B5B3C" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round">'
          '<path d="M10 40 Q22 26 38 10" fill="none"/><path d="M22 28 q-12 -2 -14 -12 q12 0 14 12z" fill="#7DBB6B"/>'
          '<path d="M28 22 q10 4 12 14 q-12 -2 -12 -14z" fill="#3F9D5A"/><path d="M33 16 q-8 -6 -6 -14 q8 4 6 14z" fill="#9CCB6E"/></g></svg>')

CSS = {
'g': f'''
/* G｜雜誌封面框 */
.ao-mkv.fg{{position:relative;padding:2.4% 3.2% 3.2%;background:#FBF8F1;border-radius:4px;box-shadow:0 0 0 1px #E4DCC8,0 8px 24px rgba(40,50,30,.12)}}
.ao-mkv.fg .mh{{position:relative;margin:0 0 2.2%;display:flex;align-items:flex-end;justify-content:space-between;border-bottom:3px solid #1A1A1A;padding-bottom:.6%}}
.ao-mkv.fg .mh b{{font:900 clamp(20px,4.2vw,40px)/.9 "Playfair Display","Didot","Bodoni 72","Times New Roman",serif;letter-spacing:.06em;color:#1F5A3A;display:flex;align-items:center;gap:.25em}}
.ao-mkv.fg .mh b i{{display:inline-block;width:.75em;height:.75em;background:{SPRIG} no-repeat center/contain}}
.ao-mkv.fg .mh b em{{font-style:normal;font:800 .42em/1 -apple-system,"PingFang HK",sans-serif;letter-spacing:.3em;color:#1A1A1A;margin-left:.4em}}
.ao-mkv.fg .mh span{{font:700 clamp(9px,1.1vw,12px)/1.4 -apple-system,"PingFang HK",sans-serif;letter-spacing:.18em;color:#6b6250;text-align:right}}
.ao-mkv.fg .mh:after{{content:"";position:absolute;left:0;right:0;bottom:-7px;border-bottom:1px solid #1A1A1A}}
.ao-mkv.fg .kv{{border:0;border-radius:0}}
@media(max-width:640px){{.ao-mkv.fg{{padding:4% 4% 4%}}.ao-mkv.fg .mh{{margin-bottom:4%}}.ao-mkv.fg .mh b{{font-size:17px;white-space:nowrap}}.ao-mkv.fg .mh b em{{font-size:.5em;letter-spacing:.15em}}.ao-mkv.fg .mh span{{font-size:7.5px;letter-spacing:.06em}}}}
''',
'h': f'''
/* H｜專題書脊框 */
.ao-mkv.fh{{position:relative;padding:2.4% 2.4% 2.4% 8.5%;background:#fff;border:1px solid #D9E7D2;border-radius:4px;box-shadow:0 8px 24px rgba(31,90,58,.12)}}
.ao-mkv.fh .sp{{position:absolute;left:0;top:0;bottom:0;width:6.2%;background:#2F8F4E;display:flex;align-items:center;justify-content:center}}
.ao-mkv.fh .sp b{{writing-mode:vertical-rl;color:#fff;font:900 clamp(12px,1.9vw,20px)/1 -apple-system,"PingFang HK",sans-serif;letter-spacing:.35em;white-space:nowrap}}
.ao-mkv.fh .sp b small{{font:700 .62em/1 -apple-system,Arial,sans-serif;letter-spacing:.25em;color:#CFE8CD;margin-top:.8em}}
.ao-mkv.fh .sp:before,.ao-mkv.fh .sp:after{{content:"";position:absolute;left:50%;width:42%;aspect-ratio:1;transform:translateX(-50%);background:{SPRIG} no-repeat center/contain;filter:brightness(0) invert(1);opacity:.9}}
.ao-mkv.fh .sp:before{{top:3%}}.ao-mkv.fh .sp:after{{bottom:3%;transform:translateX(-50%) scaleY(-1)}}
.ao-mkv.fh .is{{position:absolute;right:2.4%;top:0;transform:translateY(-50%);background:#F7CE46;color:#1A1A1A;font:900 clamp(9px,1.1vw,12px)/1 -apple-system,"PingFang HK",sans-serif;letter-spacing:.15em;padding:7px 12px;border-radius:2px;z-index:8}}
.ao-mkv.fh .kv{{border:0;border-radius:0;box-shadow:inset 0 0 0 1px #E4ECE0}}
@media(max-width:640px){{.ao-mkv.fh{{padding:3% 3% 3% 12%}}.ao-mkv.fh .sp{{width:9.5%}}.ao-mkv.fh .sp b{{font-size:12px;letter-spacing:.25em}}}}
''',
}
DECO = {
 'g': '<div class="mh"><b><i></i>VEGETARIAN BIBLE<em>素食天書</em></b><span>KITCHEN AO<br>2026 · 新手特刊</span></div>',
 'h': '<div class="sp"><b>素食天書<small>VEGETARIAN BIBLE</small></b></div><span class="is">ISSUE 2026 · 素食特輯</span>',
}

def wrap(block_html, style):
    h = block_html.replace('class="ao-mkv"', f'class="ao-mkv f{style}"', 1).replace('<div class="kv">', DECO[style] + '<div class="kv">', 1)
    return '<style>' + ' '.join(l.strip() for l in CSS[style].splitlines() if l.strip() and not l.strip().startswith('/*')) + '</style>' + h

if __name__ == '__main__':
    PX = 'https://images.pexels.com/photos/{0}/pexels-photo-{0}.jpeg?auto=compress&cs=tinysrgb&w=700'
    COLS = [(PX.format(7118901), '蛋奶素', '吃蛋、奶'), (PX.format(36183642), '奶素', '吃奶、不吃蛋'),
            (PX.format(17140078), '五辛素', '可吃蔥、蒜、韭'), (PX.format(6157094), '純素', '只吃植物')]
    TTL = '聚會有朋友吃素？<br>新手一表看懂<em>素食分類天書</em>'
    OPTS = [('G｜雜誌封面框', '仿雜誌封面：頂部大字刊頭「VEGETARIAN BIBLE 素食天書」配粗細雙線，右邊「KITCHEN AO 2026 · 素食新手特刊」期號，只用一枝小葉仔做點綴，視線集中在標題。', 'g'),
            ('H｜專題書脊框', '仿網媒／雜誌專題：左邊一條綠色書脊直排「素食天書 VEGETARIAN BIBLE」，右上角黃色「ISSUE 2026 · 素食特輯」標籤，外框只得一條幼線，最簡潔、最有媒體感。', 'h')]
    secs = []
    for t, d, st in OPTS:
        blk = wrap(kv_mag.block(COLS, 'div', ttl=TTL), st)
        doc = f'<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body style="margin:0;padding:26px 14px;background:#fff">{blk}</body></html>'
        secs.append(f'<section class="opt"><h3>{t}</h3><p>{d}</p><div class="pair"><div><small>桌面（白色 blog 背景）</small>'
                    f'<iframe srcdoc="{html.escape(doc)}" style="width:860px;height:600px"></iframe></div>'
                    f'<div><small>手機</small><iframe srcdoc="{html.escape(doc)}" style="width:390px;height:640px"></iframe></div></div></section>')
    page = f'''<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>B2 KV 外框方案 v3</title>
<style>body{{margin:0;background:#EEF1EA;color:#222;font:15px/1.6 -apple-system,"PingFang HK",Arial,sans-serif}}.wrap{{max-width:1320px;margin:0 auto;padding:24px 16px 60px}}
.opt{{margin:0 0 34px}}.opt h3{{margin:0 0 4px;font-size:18px}}.opt p{{margin:0 0 10px;color:#555;font-size:14px}}
.pair{{display:flex;gap:16px;flex-wrap:wrap;align-items:flex-start}}.pair small{{display:block;font-weight:700;color:#7a6a45;margin:0 0 4px}}iframe{{border:1px solid #ddd;background:#fff;border-radius:8px}}</style></head>
<body><div class="wrap"><h1 style="font-size:22px">B2 KV｜媒體風格外框（2 款）</h1>{''.join(secs)}</div></body></html>'''
    open(os.path.join(HERE, '..', 'kv-b2-frame-options-v3.html'), 'w', encoding='utf-8').write(page)
    print('ok')
