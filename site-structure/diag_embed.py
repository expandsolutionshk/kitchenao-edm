# -*- coding: utf-8 -*-
"""KW 分配頁頂的架構圖（和 index.html 同一款：每格顯示頁面類型、名稱及完整 URL，按格子打開頁面；虛線＝CTA 連結）"""
import json, html, os
HERE = os.path.dirname(os.path.abspath(__file__))
B = 'https://aoaodelivery.com'

CSS = '''
.diag h2{margin-top:6px}.diag .card{overflow:auto}
.diag .legend{font-size:13px;color:#6b6252;margin:0 0 10px}.diag .legend span{display:inline-block;padding:2px 10px;border-radius:8px;margin-right:6px}
.diag .legend .new{background:#E3F4E8}.diag .legend .old{background:#FFF4D6}.diag .legend .ok{background:#E3F1FB}.diag .legend .cta{background:#fff;border:1px dashed #8a8172}
.diag .mermaid .nodeLabel,.diag .mermaid .nodeLabel *{font-size:15px!important;line-height:1.35}.diag .mermaid .nodeLabel b{font-size:16px!important}
.diag .mermaid .u{font-size:12px!important;color:#444;word-break:break-all}.diag .mermaid .node{cursor:pointer}
.diag .mermaid .t{display:inline-block;font-size:12px!important;font-weight:700;color:#fff!important;background:#1A1A1A;border-radius:10px;padding:2px 9px;margin-bottom:4px}
.diag .mermaid .edgeLabel,.diag .mermaid .edgeLabel *{font-size:13px!important;color:#7a5c12!important;background:#FFF8E6!important}
'''
LEGEND = '<p class="legend"><span class="new">綠＝新建／建議新增</span><span class="old">黃＝要整理</span><span class="ok">藍＝已有</span><span class="cta">虛線＋文字＝CTA 連結（要在該頁加入的按鈕或連結）</span>按格子可打開該頁</p>'

def section(code, title='架構圖', note=''):
    n = f'<p class="note">{note}</p>' if note else ''
    return f'<div class="diag"><h2 id="map">{title}</h2>{LEGEND}{n}<div class="card"><pre class="mermaid">{html.escape(code)}</pre></div></div>'

def from_index(key):
    return json.load(open(os.path.join(HERE, 'diagrams.json'), encoding='utf-8'))[key]

# 簡化版（給沒有在 index.html 的圖用）
def N(i, name, path='', cls='ok', tag='頁面'):
    return dict(id=i, name=name, url=(B + path) if path else '', cls=cls, tag=tag)

CLS = ['classDef new fill:#E3F4E8,stroke:#3BAA5C', 'classDef old fill:#FFF4D6,stroke:#C8A24A', 'classDef bad fill:#FDE2E1,stroke:#E2574C',
       'classDef ok fill:#E3F1FB,stroke:#2B7BD0']

def mm(direction, nodes, edges):
    L = [f'flowchart {direction}']
    for n in nodes:
        url = n['url'] or '（未有 URL）'
        lab = f"<span class='t'>{n['tag']}</span><br/><b>{n['name']}</b><br/><span class='u'>{url}</span>".replace('"', "'")
        L.append(f'{n["id"]}["{lab}"]:::{n["cls"]}')
    L += edges
    L += [f'click {n["id"]} "{n["url"]}" _blank' for n in nodes if n['url']]
    L += CLS
    return '\n'.join(L)

# ---------- 共用頂部選單（index.html 及各 KW 頁）----------
ORDER = ['全站總覽', '船河', '素食', '生日會', '公司午餐', '學校飯盒', '中秋節', '萬聖節', '聖誕節', '野餐', '訂製食物', '地區頁']
GROUP = {'Seasonal': ['中秋節', '萬聖節', '聖誕節']}
KWPAGE = {'素食': 'vegetarian-kw.html', '聖誕節': 'xmas-kw.html'}   # 這些分頁＝架構圖＋KW 分配，同一頁
LABEL = {'素食': '🥦 素食', '聖誕節': '🎄 聖誕節'}
CORE = ('🏢 核心頁面 KW 分配', 'core-pages-kw.html')
import urllib.parse as _u
def href(k):
    return KWPAGE.get(k) or 'index.html#' + _u.quote(k)
NAV_CSS = '''
.snav{display:flex;gap:8px;flex-wrap:wrap;padding:12px 24px;background:#fff;border-bottom:1px solid #eee;position:sticky;top:0;z-index:20;font-family:-apple-system,"PingFang HK","Noto Sans HK",sans-serif}
.snav a,.snav .dt{border:1.5px solid #1A1A1A;background:#fff;color:#1A1A1A;border-radius:30px;padding:6px 14px;font-size:14px;text-decoration:none;cursor:pointer;line-height:1.4}
.snav a.on,.snav .dt.on{background:#C8A24A;border-color:#C8A24A;font-weight:800}
.snav .dd{position:relative}.snav .dt:after{content:' ▾'}
.snav .menu{display:none;position:absolute;top:115%;left:0;background:#fff;border:1.5px solid #1A1A1A;border-radius:14px;padding:6px;min-width:150px;box-shadow:0 8px 24px rgba(0,0,0,.12)}
.snav .dd.open .menu{display:block}.snav .menu a{display:block;border:0;border-radius:10px;margin:2px 0}
'''
NAV_JS = '''<script>document.querySelectorAll('.snav .dt').forEach(t=>t.onclick=e=>{e.stopPropagation();t.parentNode.classList.toggle('open')});document.addEventListener('click',()=>document.querySelectorAll('.snav .dd').forEach(d=>d.classList.remove('open')));</script>'''
def nav_html(current):
    ing = {k: g for g, ks in GROUP.items() for k in ks}
    out, done = [], set()
    for k in ORDER:
        g = ing.get(k)
        if g:
            if g in done: continue
            done.add(g)
            on = ' on' if current in GROUP[g] else ''
            items = ''.join(f'<a href="{href(x)}"{" class=on" if x == current else ""}>{LABEL.get(x, x)}</a>' for x in GROUP[g])
            out.append(f'<div class="dd"><span class="dt{on}">{g}</span><div class="menu">{items}</div></div>')
        else:
            out.append(f'<a href="{href(k)}"{" class=on" if k == current else ""}>{LABEL.get(k, k)}</a>')
    out.append(f'<a href="{CORE[1]}"{" class=on" if current == "核心" else ""}>{CORE[0]}</a>')
    return '<nav class="snav">' + ''.join(out) + '</nav>'

# 最頂：和 index.html 一樣的網站架構圖標題＋選單
TOP_CSS = '''.stop{background:#1A1A1A;padding:14px 24px;border-bottom:1px solid #333}.stop a{color:#F7CE46;text-decoration:none;font-size:20px;font-weight:800;font-family:-apple-system,"PingFang HK","Noto Sans HK",sans-serif}.stop span{display:block;color:#C9BFA8;font-size:13px;margin-top:2px}
.stop + .snav + header{background:#2a2620}'''
def top_html(current):
    return '<div class="stop"><a href="index.html">Kitchen AO 網站架構圖（Site Structure）</a><span>每個格子顯示完整 URL，按一下可打開該頁</span></div>' + nav_html(current)
