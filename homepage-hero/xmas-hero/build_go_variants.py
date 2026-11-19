from pathlib import Path
H=Path(__file__).parent
base=(H/'hero-xmas-option-c-rawhtml.html').read_text()
CH='<svg viewBox="0 0 10 10" aria-hidden="true"><path d="M3.5 1.5 7 5l-3.5 3.5"/></svg>'
V={}
V['1']=base
v2=base.replace(f'<span class="go">立即查看聖誕套餐{CH}</span>',f'<span class="go">探索聖誕套餐{CH}</span>').replace(f'<span class="go">View Christmas Sets{CH}</span>',f'<span class="go">Discover the Collection{CH}</span>')
v2=v2.replace('</style>','''/* V2 金線文字連結 */
.ao-hx .ao-xc-btn{animation:none}
.ao-hx .ao-xc-btn .go{margin-top:10px;padding:0 2px 5px;background:linear-gradient(#E4C77E,#E4C77E) left bottom/0 1px no-repeat,linear-gradient(rgba(200,162,74,.45),rgba(200,162,74,.45)) left bottom/100% 1px no-repeat;border-radius:0;color:#E4C77E;font-family:"Songti TC","Noto Serif TC",Baskerville,Georgia,serif;font-size:14.5px;font-weight:500;letter-spacing:.2em;gap:8px;animation:aoGoLine 3.6s ease-in-out infinite}
html[lang^="en"] .ao-hx .ao-xc-btn .go{font-family:Baskerville,"Baskerville Old Face",Georgia,serif;font-style:italic;font-size:16px;letter-spacing:.04em}
@keyframes aoGoLine{0%{background-size:0 1px,100% 1px}55%{background-size:100% 1px,100% 1px}100%{background-size:100% 1px,100% 1px;opacity:1}}
.ao-hx .ao-xc-btn .go svg{stroke:#E4C77E;stroke-width:1.3}
.ao-hx .ao-xc-btn:hover .go{background-color:transparent;color:#fff}.ao-hx .ao-xc-btn:hover .go svg{stroke:#fff}
@media (prefers-reduced-motion:reduce){.ao-hx .ao-xc-btn .go{animation:none;background-size:100% 1px,100% 1px}}
</style>''',1)
a=v2.index('/* V2');v2=v2[:a]+v2[a:].replace('.ao-hx .ao-xc-btn','.ao-hx.gv2 .ao-xc-btn');v2=v2.replace('class="ao-hero ao-hx ao-hx-c"','class="ao-hero ao-hx ao-hx-c gv2"',1)
V['2']=v2
v3=base.replace(f'<span class="go">立即查看聖誕套餐{CH}</span>',f'<span class="go">立即查看{CH}</span>').replace(f'<span class="go">View Christmas Sets{CH}</span>',f'<span class="go">View Sets{CH}</span>')
v3=v3.replace('</style>','''/* V3 左右分格 */
.ao-hx .ao-xc-btn{animation:none;display:grid!important;grid-template-columns:minmax(0,1fr) auto;grid-template-areas:"tt go" "sm go";align-items:center;justify-items:center;row-gap:4px;column-gap:0;min-height:80px;padding:12px 12px 12px 60px}
.ao-hx .ao-xc-btn .tt{grid-area:tt;align-self:end}.ao-hx .ao-xc-btn small{grid-area:sm;align-self:start}
.ao-hx .ao-xc-btn .go{grid-area:go;align-self:stretch;margin:0 0 0 18px;padding:0 20px 0 24px;background:transparent;border-left:1px solid rgba(200,162,74,.6);border-radius:0;color:#E4C77E;font-family:"Songti TC","Noto Serif TC",Baskerville,Georgia,serif;font-size:14.5px;font-weight:500;letter-spacing:.2em;gap:8px;transition:background .35s,color .35s}
html[lang^="en"] .ao-hx .ao-xc-btn .go{font-family:Baskerville,"Baskerville Old Face",Georgia,serif;font-style:italic;font-size:16px;letter-spacing:.04em}
.ao-hx .ao-xc-btn .go svg{stroke:#E4C77E;stroke-width:1.3}
.ao-hx .ao-xc-btn:hover .go{background:#C8A24A;color:#111}.ao-hx .ao-xc-btn:hover .go svg{stroke:#111}
.ao-hx .ao-xc-btn .hl.r{display:none}
@media(max-width:640px){.ao-hx .ao-xc-btn{min-height:84px;padding:10px 10px 10px 46px}.ao-hx .ao-xc-btn .go{margin-left:10px;padding:0 12px 0 14px;font-size:13px;letter-spacing:.1em}.ao-hx .ao-xc-btn .tt span{font-size:14.5px}.ao-hx .ao-xc-btn .tt .st{display:none}}
</style>''',1)
a=v3.index('/* V3');v3=v3[:a]+v3[a:].replace('.ao-hx .ao-xc-btn','.ao-hx.gv3 .ao-xc-btn');v3=v3.replace('class="ao-hero ao-hx ao-hx-c"','class="ao-hero ao-hx ao-hx-c gv3"',1)
V['3']=v3
for k,v in V.items(): (H/f'hero-C-go-v{k}-rawhtml.html').write_text(v,encoding='utf-8')
LB={'1':'V1｜金色膠囊按鈕（現有版本）','2':'V2｜金線文字連結：「探索聖誕套餐 ›」襯線字＋金色底線慢慢畫出，沒有外圍發光','3':'V3｜左右分格：左邊標題日期，右邊以金色細線分隔「立即查看 ›」，滑鼠移上去變金底'}
for lang,fn in (('zh-HK','Hero聖誕按鈕-三版本.html'),('en','Hero聖誕按鈕-三版本-EN.html')):
    body=''.join(f'<div style="position:sticky;top:0;z-index:9;padding:10px 20px;background:#1d1714;color:#E4C77E;font:600 13px -apple-system">{LB[k]}</div><div style="max-width:700px">{V[k]}</div>' for k in '123')
    (H/fn).write_text(f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>body{{margin:0;font-family:-apple-system,"PingFang HK",sans-serif}}.ao-hx-r,.ao-hf-fs1{{display:none!important}}.ao-hx{{padding:20px!important}}.ao-hx .ao-hero-grid{{grid-template-columns:1fr!important}}</style></head><body>{body}</body></html>',encoding='utf-8')
print('ok')
