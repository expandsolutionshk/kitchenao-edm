import re, os
D = os.path.dirname(os.path.abspath(__file__))
base = open(os.path.join(D, 'hero-rawhtml-no-halloween_backup_v4.html'), encoding='utf-8').read()
U = 'https://aoaodelivery.com/'
def bi(zh, en):
    return f'<span class="ao-zh" data-no-translation>{zh}</span><span class="ao-en" data-no-translation>{en}</span>'

ITEMS = [
    dict(lab='PARTY', zh='生日派對到會', en='Birthday Parties', szh='小型至百人派對', sen='Small to 100+ guests',
         href=U+'product-category/party/', img=U+'wp-content/uploads/2026/03/8-10_101-X-KITCHENAO-03-03-03-768x768.jpg',
         ic='<path d="M4 21h16M5 21v-7a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v7"/><path d="M5 16c1.2 0 1.2 1 2.3 1s1.2-1 2.4-1 1.2 1 2.3 1 1.2-1 2.3-1 1.2 1 2.4 1 1.1-1 2.3-1"/><path d="M8 12V9M12 12V9M16 12V9"/><path d="M8 6.5c0-.8.8-1.5 0-2.5-.8 1-0 1.7 0 2.5zM12 6.5c0-.8.8-1.5 0-2.5-.8 1 0 1.7 0 2.5zM16 6.5c0-.8.8-1.5 0-2.5-.8 1 0 1.7 0 2.5z"/>'),
    dict(lab='CORPORATE', zh='公司活動餐飲', en='Corporate Catering', szh='年會、會議活動', sen='Annual dinners, meetings',
         href=U+'corporate-catering-hk/', img=U+'wp-content/uploads/2023/11/IMG_2358.jpg',
         ic='<rect x="3" y="7.5" width="18" height="12.5" rx="1.5"/><path d="M9 7.5V5.5A1.5 1.5 0 0 1 10.5 4h3A1.5 1.5 0 0 1 15 5.5v2M3 12.5h18"/>'),
    dict(lab='STYLING', zh='精緻擺盤到會', en='Styled Platters', szh='擺盤送到現場', sen='Delivered to your venue',
         href=U+'product-category/商務活動/a-bit-of-cuisines-gourmet-in-a-box/', img=U+'wp-content/uploads/2025/04/WhatsApp-Image-2026-10-19-at-11.37.40-AM-768x542.jpeg',
         ic='<path d="M3 17h18M4.5 17a7.5 7.5 0 0 1 15 0"/><path d="M12 9.5V8M10.5 8h3M2.5 20h19"/>'),
]

OPTS = {}

# FS1: Four Seasons hero quick-link bar (thin line icons, spaced labels, white strip)
css1 = ('.ao-hf-fs1{display:grid;grid-template-columns:repeat(3,1fr);max-width:620px;margin:6px 0 0;background:rgba(255,255,255,.85);border-top:1px solid #1d1714;border-bottom:1px solid #1d1714}'
        '.ao-hf-fs1 .it{display:flex;flex-direction:column;align-items:center;text-align:center;padding:18px 8px 16px;}'
        '.ao-hf-fs1 .it+.it{border-left:1px solid #E6DDCB}'
                '.ao-hf-fs1 svg{width:30px;height:30px;fill:none;stroke:#9A7B2E;stroke-width:1.1;stroke-linecap:round;stroke-linejoin:round;margin:0 0 10px}'
        '.ao-hf-fs1 b{font-size:14.5px;color:#1d1714;font-weight:600;letter-spacing:.14em}'
        '.ao-hf-fs1 .sb{font-size:12px;color:#8A8378;margin-top:4px;letter-spacing:.06em}'
        'html[lang^="en"] .ao-hf-fs1 b{letter-spacing:.08em;text-transform:uppercase;font-size:12.5px}'
        '@media(max-width:640px){.ao-hf-fs1 .it{padding:14px 4px 12px}.ao-hf-fs1 svg{width:26px;height:26px}.ao-hf-fs1 b{font-size:12.5px;letter-spacing:.06em}.ao-hf-fs1 .sb{font-size:10.5px;letter-spacing:0}}')
html1 = '<div class="ao-hf ao-hf-fs1">' + ''.join(
    f'<div class="it"><svg viewBox="0 0 24 24" aria-hidden="true">{i["ic"]}</svg><b>{bi(i["zh"], i["en"])}</b><span class="sb">{bi(i["szh"], i["sen"])}</span></div>'
    for i in ITEMS) + '</div>'
OPTS['FS1'] = (css1, html1, 'Four Seasons Hero 快速連結列：幼線 icon、字距較闊、上下黑幼線白底條')

# FS2: Four Seasons "Discover" image tiles with title overlay and VIEW link
css2 = ('.ao-hf-fs2{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;max-width:620px;margin:6px 0 0}'
        '.ao-hf-fs2 .it{position:relative;display:block;aspect-ratio:3/4;overflow:hidden;background:#1d1714;text-decoration:none !important}'
        '.ao-hf-fs2 img{position:absolute;inset:0;width:100% !important;height:100% !important;object-fit:cover;margin:0 !important;transition:transform .7s}'
        '.ao-hf-fs2 .it:hover img{transform:scale(1.05)}'
        '.ao-hf-fs2 .it:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 35%,rgba(0,0,0,.72) 100%)}'
        '.ao-hf-fs2 .tx{position:absolute;left:0;right:0;bottom:0;z-index:2;padding:14px 12px;color:#fff;text-align:left}'
        '.ao-hf-fs2 small{display:block;font-size:9.5px;letter-spacing:.3em;color:#E4C77E;margin:0 0 6px}'
        '.ao-hf-fs2 b{display:block;font-size:15px;font-weight:500;letter-spacing:.08em;line-height:1.35;color:#fff}'
        '.ao-hf-fs2 .v{display:inline-block;margin-top:8px;font-size:10.5px;letter-spacing:.22em;border-bottom:1px solid rgba(255,255,255,.7);padding-bottom:2px}'
        '@media(max-width:640px){.ao-hf-fs2{gap:6px}.ao-hf-fs2 .tx{padding:10px 8px}.ao-hf-fs2 small{font-size:8.5px;letter-spacing:.16em}.ao-hf-fs2 b{font-size:12.5px;letter-spacing:.02em}.ao-hf-fs2 .v{font-size:9px;letter-spacing:.12em}}')
html2 = '<div class="ao-hf ao-hf-fs2">' + ''.join(
    f'<a class="it" href="{i["href"]}"><img src="{i["img"]}" alt="{i["zh"]}" loading="lazy" decoding="async"><span class="tx"><small>{i["lab"]}</small><b>{bi(i["zh"], i["en"])}</b><span class="v">{bi("查看", "VIEW")}</span></span></a>'
    for i in ITEMS) + '</div>'
OPTS['FS2'] = (css2, html2, 'Four Seasons「Discover Sydney」圖片磚：直身相、底部漸黑、金色英文小標＋白字＋「查看」底線')

pat = re.compile(r'<ul class="ao-hero-feats">.*?</ul>', re.S)
blocks = []
for k, (css, h, desc) in OPTS.items():
    out = pat.sub(lambda m: h, base, count=1).replace('<style>\n', '<style>\n' + css + '\n', 1)
    open(os.path.join(D, f'hero-rawhtml-feats-{k}.html'), 'w', encoding='utf-8').write(out)
    blocks.append(f'<div class="lab"><b>方案 {k}</b>{desc}</div>' + out)
head = ('<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>首頁 Hero Mockup：Four Seasons 方案</title><style>body{margin:0;font-family:-apple-system,"PingFang HK","Noto Sans TC",sans-serif;background:#fff}'
        '.lab{max-width:1240px;margin:34px auto 0;padding:12px 20px;background:#141414;color:#F4ECDD;border-radius:10px;font-size:14px}.lab b{color:#E4C77E;margin-right:8px}</style></head><body>')
open(os.path.join(D, 'hero-mockup-zh-FS.html'), 'w', encoding='utf-8').write(head + ''.join(blocks) + '</body></html>')
print('ok')
