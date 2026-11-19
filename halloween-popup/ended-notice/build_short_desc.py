from pathlib import Path
H=Path(__file__).parent
LINK='https://aoaodelivery.com/product-category/party/'
SERIF='&quot;Songti TC&quot;,&quot;Noto Serif TC&quot;,Baskerville,Georgia,serif'
K='HALLOWEEN 2026'; T='2026 萬聖節狂嘩套餐已完滿結束'
P=f'多謝大家支持！以下餐單只供參考，2027 萬聖節再見。如正籌備其他聚會，歡迎查看<a href="{LINK}" style="color:#9A7B2E;text-decoration:none;border-bottom:1px solid #C8A24A;font-weight:600;">派對到會套餐分類</a>。'
PB=P.replace('color:#9A7B2E','color:#E4C77E')
OPT={
'A':('A｜米白金框卡','米白底、金色雙框，和聖誕頁及首頁 Hero 同一風格，最穩陣。',
f'<div style="margin:0 0 18px;padding:18px 20px;background:#fbf8f3;border:1px solid #C8A24A;box-shadow:inset 0 0 0 4px #fbf8f3,inset 0 0 0 5px rgba(200,162,74,.35);"><p style="margin:0 0 6px;font-size:11px;letter-spacing:.3em;color:#9A7B2E;">{K}</p><p style="margin:0 0 8px;font-family:{SERIF};font-size:19px;font-weight:600;letter-spacing:.04em;line-height:1.4;color:#1d1714;">{T}</p><p style="margin:0;font-size:14px;line-height:1.8;color:#5d534d;">{P}</p></div>'),
'B':('B｜黑底金字','黑底配金字，最搶眼，客人一入頁就知道套餐已結束。',
f'<div style="margin:0 0 18px;padding:18px 20px;background:#1d1714;border:1px solid #1d1714;box-shadow:inset 0 0 0 5px #1d1714,inset 0 0 0 6px rgba(200,162,74,.7);"><p style="margin:0 0 6px;font-size:11px;letter-spacing:.3em;color:#C8A24A;">{K}</p><p style="margin:0 0 8px;font-family:{SERIF};font-size:19px;font-weight:500;letter-spacing:.06em;line-height:1.4;color:#F3E3B8;">{T}</p><p style="margin:0;font-size:14px;line-height:1.8;color:#d8cfbf;">{PB}</p></div>'),
'C':('C｜極簡金線','沒有底色，只有上下兩條金線，最低調，和產品頁原本的版面最融合。',
f'<div style="margin:0 0 18px;padding:14px 0;border-top:1px solid #C8A24A;border-bottom:1px solid #C8A24A;"><p style="margin:0 0 6px;font-size:11px;letter-spacing:.3em;color:#9A7B2E;">✦ {K}</p><p style="margin:0 0 6px;font-family:{SERIF};font-size:18px;font-weight:600;letter-spacing:.04em;line-height:1.4;color:#1d1714;">{T}</p><p style="margin:0;font-size:14px;line-height:1.8;color:#5d534d;">{P}</p></div>'),
}
import html
mock='<div style="max-width:460px;font-family:-apple-system,\'PingFang HK\',sans-serif">{n}<h1 style="margin:0 0 12px;font-size:24px;font-weight:800;color:#1d1714">AO 12-16pax Halloween萬聖節狂嘩套餐</h1>{x}<p style="margin:0 0 6px;font-size:14px;color:#333">美味度 ★★★★★<br>豪華度 ★★★★★</p><p style="margin:10px 0;font-size:22px;font-weight:700">$3,138.00 <span style="font-size:12px;background:#f3e3d0;color:#a0522d;padding:3px 8px;border-radius:12px;vertical-align:middle">已售完</span></p></div>'
body=''
for k,(n,d,c) in OPT.items():
    (H/f'short-desc-option-{k}.html').write_text(c,encoding='utf-8')
    body+=f'<section style="padding:28px 24px;border-bottom:8px solid #eee"><p style="margin:0 0 4px;font:600 15px -apple-system;color:#9A7B2E">{n}</p><p style="margin:0 0 16px;font:13px -apple-system;color:#666">{d}</p>'+mock.format(n='',x=c)+f'<details style="margin-top:16px"><summary style="cursor:pointer;font:13px -apple-system">顯示代碼</summary><textarea style="width:100%;height:120px;font:12px monospace">{html.escape(c)}</textarea></details></section>'
(H/'萬聖節簡短描述公告-三款.html').write_text('<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>萬聖節公告 3 款</title></head><body style="margin:0;background:#fff">'+body+'</body></html>',encoding='utf-8')
print('ok')
