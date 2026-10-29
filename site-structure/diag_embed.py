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
