# A｜蔬菜實景主角：清新版 3 款 → ../kv-a-fresh.html
import os
from kv import LOGO, PX, IMG, img, SETCARD, CSS as BASE
HERE = os.path.dirname(os.path.abspath(__file__))
IMG['white'] = PX.format(4887984)   # Pexels：白色木枱上的車厘茄、香草（俯拍）
IMG['slice'] = PX.format(7223295)   # Pexels：切片青瓜、甘筍、番茄（俯拍）
TAG = '<span class="pill">香港素食到會推介 2026</span>'
TTL = '<h2 class="ttl"><span class="y">「素」味人生</span>健康到會套餐，<br>派對有素食朋友點安排？</h2>'
TICKS = ('<ul class="tks"><li><i>✔</i>小食、沙律、意粉、主菜任選</li>'
         '<li><i>✔</i>6–26 人套餐　$1,388 起</li><li><i>✔</i>逢星期五落單 95 折</li></ul>')
KV = [
('A1｜同一張相，提亮＋白霧',
 '保留原本綠色蔬菜相，但相片提亮 15%、左邊改用奶白色霧化漸變；標題改深綠字，tag 改葉綠色，黃剔改綠剔。',
 f'<div class="kv fr f1">{img("veg")}<div class="shade"></div>{LOGO}<div class="tb">{TAG}{TTL}{TICKS}</div>{SETCARD}</div>'),
('A2｜換白底蔬菜相',
 '背景換成白色木枱上的車厘茄及香草，整體最光、最清新；文字直接放在留白位置，毋須霧化。',
 f'<div class="kv fr f2">{img("white")}<div class="shade"></div>{LOGO}<div class="tb">{TAG}{TTL}{TICKS}</div>{SETCARD}</div>'),
('A3｜薄荷綠色塊＋實景',
 '左邊約六成用淺薄荷綠色塊放標題，右邊蔬菜實景；顏色最統一，似健康飲食品牌的感覺。',
 f'<div class="kv fr f3"><div class="ph">{img("slice")}</div><div class="panel"></div>{LOGO}<div class="tb">{TAG}{TTL}{TICKS}</div>{SETCARD}</div>'),
]
CSS = BASE + '''
.fr{background:#F6FAF2}
.fr .ttl{font-size:4.4cqw;color:#1F5A3A;-webkit-text-stroke:.45cqw #fff!important;text-shadow:0 .35cqw 1.2cqw rgba(31,90,58,.25)}
.fr .ttl .y{color:#E8743B}
.fr .pill{background:#3F9D5A;color:#fff}
.fr .tks{box-shadow:0 .8cqw 2.4cqw rgba(31,90,58,.18);border:.15cqw solid #DCEFD6}
.fr .tks li{color:#24432F}.fr .tks i{color:#fff;-webkit-text-stroke:0!important;text-shadow:none;background:#3F9D5A;border-radius:50%;width:2.6cqw;height:2.6cqw;display:inline-flex;align-items:center;justify-content:center;font-size:1.5cqw}
.fr .logo2{border-color:#DCEFD6}
.fr .rib3{box-shadow:0 1cqw 2.6cqw rgba(31,90,58,.25)}.fr .rib3 span{background:#3F9D5A;color:#fff;border:3px solid #fff}
.fr .tb{position:absolute;left:4.5cqw;top:7cqw}
.f1 img.bg{filter:brightness(1.15) saturate(1.08)}
.f1 .shade{position:absolute;inset:0;background:linear-gradient(90deg,rgba(248,251,244,.93) 0%,rgba(248,251,244,.8) 42%,rgba(248,251,244,0) 66%)}
.f2 img.bg{filter:brightness(1.05)}
.f2 .shade{position:absolute;inset:0;background:linear-gradient(90deg,rgba(255,255,255,.75) 0%,rgba(255,255,255,.35) 50%,rgba(255,255,255,0) 70%)}
.f3 .ph{position:absolute;top:0;right:0;bottom:0;width:52%}.f3 .ph img{width:100%;height:100%;object-fit:cover;filter:brightness(1.05)}
.f3 .panel{position:absolute;top:0;left:0;bottom:0;width:62%;background:#EAF5E4;border-radius:0 50% 50% 0/0 100% 100% 0}
\n.f3 .ttl{font-size:4cqw}
'''
html = f'''<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>KV A 清新版（3 款）</title><style>{CSS}</style></head><body><div class="wrap">
<h1>🥗 KV A 清新版（3 款）</h1><p>改動方向：相片提亮、深色遮罩改奶白／薄荷綠、黑黃配色改葉綠＋白，標題深綠字白描邊。</p>
{''.join(f'<section class="opt"><h3>{t}</h3><p>{d}</p>{h}</section>' for t, d, h in KV)}
</div></body></html>'''
open(os.path.join(HERE, '..', 'kv-a-fresh.html'), 'w', encoding='utf-8').write(html); print('ok')
