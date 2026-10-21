# KV A1（提亮＋白霧）：三個剔改為文章重點（簡單細字）→ ../kv-a1-toc.html
import os
from kv_fresh import LOGO, img, SETCARD, CSS as FRESH, TAG, TTL
HERE = os.path.dirname(os.path.abspath(__file__))
PTS = ['派對有素食朋友，食物應該怎樣安排？', '揀素食到會要注意甚麼？', '「素」味人生套餐價目、份量及菜式', '預訂流程、送貨及免運費']
L1 = '<ol class="pt1">' + ''.join(f'<li><i>{i:02d}</i>{t}</li>' for i, t in enumerate(PTS, 1)) + '</ol>'
L2 = '<ul class="pt2"><li class="h">本文重點</li>' + ''.join(f'<li>{t}</li>' for t in PTS) + '</ul>'
PUNCH = '<p class="pl">一份套餐，照顧每位素食賓客</p>'
KWS = '<p class="kw">' + ''.join(f'<span>#{w}</span>' for w in ['素食到會', '健康到會', '齋菜到會', '派對素食']) + '</p>'
PUNCH2 = '<p class="pl2">素食，都可以豐富又滿足。</p>'
def kv(x): return f'<div class="kv fr f1">{img("veg")}<div class="shade"></div>{LOGO}<div class="tb">{TAG}{TTL}{x}</div>{SETCARD}</div>'
KV = [
('A1-c｜Punch line', '標題下加一句短句，綠色細字配左邊綠線，突出「照顧素食賓客」的賣點。', kv(PUNCH)),
('A1-d｜關鍵字標籤', '用 4 個 # 關鍵字細標籤（素食到會、健康到會、齋菜到會、派對素食），似社交媒體 hashtag，同時帶出 SEO 關鍵字。', kv(KWS)),
('A1-e｜Punch line＋關鍵字', '短句配關鍵字標籤；句子帶出感覺，標籤帶出搜尋字眼。', kv(PUNCH2 + KWS)),
]
CSS = FRESH + '''
.pl{margin:2.4cqw 0 0;padding:.2cqw 0 .2cqw 1.5cqw;border-left:.4cqw solid #3F9D5A;font-size:2.6cqw;font-weight:800;color:#2C6E49;letter-spacing:.1cqw}
.pl2{margin:2.2cqw 0 0;font-size:2.6cqw;font-weight:800;color:#2C6E49;letter-spacing:.15cqw}
.kw{margin:1.6cqw 0 0;display:flex;flex-wrap:wrap;gap:.8cqw}.kw span{font-size:1.7cqw;font-weight:700;color:#2C6E49;background:rgba(255,255,255,.9);border:.15cqw solid #CFE8CD;border-radius:3cqw;padding:.35cqw 1.2cqw}
.pl+.kw{margin-top:1.4cqw}
.fr .tb{top:50%;transform:translateY(-50%)}
'''
html = f'''<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>KV A1：Punch line／關鍵字版（3 款）</title><style>{CSS}</style></head><body><div class="wrap">
<h1>🥗 KV A1：三個剔改為 Punch line／關鍵字（3 款）</h1><p>標題下改為一句短句或關鍵字標籤；關鍵字取自 B1 主攻字眼。</p>
{''.join(f'<section class="opt"><h3>{t}</h3><p>{d}</p>{h}</section>' for t, d, h in KV)}
</div></body></html>'''
open(os.path.join(HERE, '..', 'kv-a1-toc.html'), 'w', encoding='utf-8').write(html); print('ok')
