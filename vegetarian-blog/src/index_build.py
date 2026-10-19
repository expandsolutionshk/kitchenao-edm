# -*- coding: utf-8 -*-
from common import *
F={'B1':'b1-vegetarian-catering.html','B2':'b2-vegetarian-types-guide.html','B3':'b3-chu-yat-sap-ng-guide.html','B4':'b4-vegetarian-nutrition.html','B5':'b5-weekly-vegetarian-menu.html','B6':'b6-vegan-vegetarian-meaning.html'}
cards=''.join(f'<a class="c" href="{F[p]}"><b>{p}</b><span>{BLOGS[p][0]}</span><small>{BLOGS[p][1].replace(B,"")}</small></a>' for p in F)
html_=f'''<!DOCTYPE html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>素食 Blog Mockups｜Kitchen AO</title>
<style>body{{margin:0;font-family:-apple-system,"PingFang HK",sans-serif;background:#FBF6EC;color:#2a2620}}header{{background:#1A1A1A;color:#F7CE46;padding:18px 24px}}header h1{{margin:0;font-size:20px}}header a{{color:#F7CE46}}
.w{{max-width:1000px;margin:0 auto;padding:20px}}.g{{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px}}
.c{{display:block;background:#fff;border-radius:14px;padding:16px;text-decoration:none;color:inherit;box-shadow:0 2px 10px rgba(0,0,0,.06);border-top:5px solid #3F9D5A}}.c b{{background:#1A1A1A;color:#F7CE46;border-radius:8px;padding:2px 8px;font-size:13px}}.c span{{display:block;font-weight:800;margin:8px 0 4px;line-height:1.4}}.c small{{color:#7a6a45}}</style></head><body>
<header><h1>🥦 素食 Blog Mockups（6 篇）</h1><p><a href="../site-structure/vegetarian-kw.html">→ 素食 KW 分配架構</a>　｜　<a href="../site-structure/">網站架構圖</a></p></header>
<div class="w"><p>黃色＝已分配關鍵字（每頁頂部可隱藏）；每篇底部附資料來源（以香港政府機構為主）。</p><div class="g">{cards}</div></div></body></html>'''
open(HERE.parent/'index.html','w',encoding='utf-8').write(html_);print('ok')
