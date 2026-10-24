# 列表標題：D 活動海報風（文青配色）。把 <p class="t ao-tbt">列表N｜標題</p><div class="ao-tw">…</div> 包成卡片
import re, urllib.parse
CSS = '''.ao-article .ao-tbx{position:relative;background:#F4EFE6;border:2px solid #3B3A36;border-radius:18px;padding:16px 16px 18px;margin:24px 0 12px}
.ao-article .ao-tbh{display:flex;align-items:center;gap:12px;margin:0 0 14px}
.ao-article .ao-tbh .cal{flex:none;width:52px;border:2px solid #3B3A36;border-radius:8px;background:#FFFCF6;text-align:center;overflow:hidden;box-shadow:3px 3px 0 #3B3A36;position:relative}
.ao-article .ao-tbh .cal:before{content:"";position:absolute;top:-1px;left:12px;right:12px;height:6px;background:radial-gradient(circle,#3B3A36 2.5px,transparent 3px) 0 0/14px 6px repeat-x}
.ao-article .ao-tbh .cal b{display:block;background:#D8B4A0;border-bottom:2px solid #3B3A36;font-size:11px;font-weight:800;letter-spacing:1px;padding:7px 0 3px;color:#3B3A36;line-height:1.2}
.ao-article .ao-tbh .cal i{display:block;font-style:normal;font:900 24px/1.25 "Noto Serif TC",Georgia,serif;color:#3B3A36}
.ao-article .ao-tbh .t{font:900 23px/1.3 "Noto Serif TC","Songti TC",serif;color:#3B3A36;letter-spacing:1px}
.ao-article .ao-tbh .o{flex:none;margin-left:auto;border:2px solid #3B3A36;border-radius:30px;background:#D5DFD2;padding:4px 14px;font-weight:800;font-size:13px;color:#3B3A36;white-space:nowrap;line-height:1.4}
.ao-article .ao-tbx .ao-tw{margin:0!important;border:2px solid #3B3A36!important;border-radius:12px!important;background:#FFFCF6}
.ao-article .ao-tbx .ao-tbl{background:transparent}.ao-article .ao-tbl.ao-tblc{min-width:0!important;table-layout:fixed}.ao-article .ao-tblc th,.ao-article .ao-tblc td{white-space:normal!important;overflow-wrap:break-word}.ao-article .ao-tblc td.c,.ao-article .ao-tblc th.c{text-align:center}.ao-article .ao-tbl.ao-tbl4{table-layout:fixed}.ao-article .ao-tbl4 th:nth-child(1){width:15%}.ao-article .ao-tbl4 th:nth-child(2){width:23%}.ao-article .ao-tbl4 th:nth-child(3),.ao-article .ao-tbl4 th:nth-child(4){width:31%}.ao-article .ao-tbl4 th{white-space:normal!important}
.ao-article .ao-tbx .ao-tbl th{background:#3B3A36;color:#F4EFE6}
.ao-article .ao-tbx .ao-tbl td{border-top:1px solid rgba(59,58,54,.45)!important;color:#3B3A36}
.ao-article .ao-tbx .ao-tbl tbody tr:nth-child(4n+1) td{background:#F7F0DC}
.ao-article .ao-tbx .ao-tbl tbody tr:nth-child(4n+2) td{background:#F1E2DB}
.ao-article .ao-tbx .ao-tbl tbody tr:nth-child(4n+3) td{background:#E4E8DA}
.ao-article .ao-tbx .ao-tbl tbody tr:nth-child(4n) td{background:#DFE7EA}
.ao-article ol.ao-tix{list-style:none!important;margin:12px 0 26px!important;padding:0!important;display:grid;grid-template-columns:1fr 1fr;gap:10px}.ao-article ol.ao-tix li{margin:0!important;padding:0!important;list-style:none!important}.ao-article ol.ao-tix li:before{display:none!important}.ao-article ol.ao-tix a{display:flex;align-items:center;gap:10px;background:#F4EFE6;border:1.5px solid #3B3A36;border-radius:10px;padding:8px 12px;color:#3B3A36!important;text-decoration:none!important;font-size:15.5px!important;font-weight:700;line-height:1.4;box-shadow:2px 2px 0 #3B3A36;transition:transform .15s}.ao-article ol.ao-tix a:hover{transform:translate(-1px,-1px);box-shadow:3px 3px 0 #3B3A36}.ao-article ol.ao-tix .n{flex:none;width:26px;height:26px;border-radius:6px;background:#D8B4A0;border:1.5px solid #3B3A36;display:flex;align-items:center;justify-content:center;font:900 14px/1 "Noto Serif TC",Georgia,serif}.ao-article .ao-tbx{scroll-margin-top:110px}@media(max-width:640px){.ao-article ol.ao-tix{grid-template-columns:1fr}.ao-article .ao-tbl.ao-tbl3{min-width:0!important;font-size:14.5px!important}.ao-article .ao-tbl.ao-tbl3{table-layout:fixed}.ao-article .ao-tbl3 th,.ao-article .ao-tbl3 td{padding:9px 8px!important;white-space:normal!important;word-break:normal!important;overflow-wrap:break-word!important;writing-mode:horizontal-tb!important}.ao-article .ao-tbl3 th:nth-child(1){width:35%}.ao-article .ao-tbl3 th:nth-child(2){width:21%}.ao-article .ao-tbl3:not(.cmp) td:first-child{font-size:13px!important;overflow-wrap:normal!important;padding-right:4px!important}.ao-article .ao-tbl3.cmp th:nth-child(1){width:22%}.ao-article .ao-tbl3.cmp th:nth-child(2){width:39%}.ao-article .ao-tbx{padding:12px 10px 14px}.ao-article .ao-tbh .t{font-size:18px}.ao-article .ao-tbh .o{display:none}.ao-article .ao-tbh .cal{width:44px}.ao-article .ao-tbh .cal i{font-size:20px}}'''

PAT = re.compile(r'<p class="t ao-tbt">列表(\d+)｜(.*?)</p>\s*(<div class="ao-tw">.*?</table></div>)', re.S)

def apply(body, head='{n} 個素食英文中英對照表速查'):
    titles = []
    def rep(m):
        n, t, tw = m.group(1), m.group(2), m.group(3)
        tag0 = None
        if '｜' in t:
            t, tag0 = t.split('｜', 1)
        titles.append(t)
        rows = tw.count('<tr>') - 1
        head = tw.split('</tr>')[0]
        if head.count('<th>') == 3:
            cls = 'ao-tbl ao-tbl3' + (' cmp' if '<th>項目</th>' in head else '')
            tw = tw.replace('<table class="ao-tbl">', f'<table class="{cls}">', 1)
        elif head.count('<th>') == 4:
            tw = tw.replace('<table class="ao-tbl">', '<table class="ao-tbl ao-tbl4">', 1)
        tag = tag0 or ('比較表' if '比較' in t else f'{rows} 個用語')
        return (f'<div class="ao-tbx" id="t{n}">'
                f'<div class="ao-tbh"><span class="cal"><b>列表</b><i>{n}</i></span><span class="t">{t}</span><span class="o">{tag}</span></div>{tw}</div>')
    body = PAT.sub(rep, body)
    items = ''.join(f'<li><a href="#t{i}"><span class="n">{i}</span>{t}</a></li>' for i, t in enumerate(titles, 1))
    idx = (f'<h2 class="ao-h2" id="tables">{head.format(n=len(titles))}</h2>\n'
           f'<p>全文整理了以下 {len(titles)} 個列表，按一下即可跳到相關列表：</p>\n<ol class="ao-tix">{items}</ol>\n')
    body = body.replace('<!--TBL_INDEX-->', idx, 1)
    txt = '列表0123456789' + ''.join(titles)
    font = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@900&display=swap&text='
            + urllib.parse.quote(''.join(sorted(set(txt)))) + '">')
    return font + '<style>' + CSS.replace('\n', '') + '</style>\n' + body

# 句子小抄：筆記紙風（不當列表）
NB_CSS = '''.ao-article .ao-nb{position:relative;margin:16px 0 22px;padding:32px 18px 32px 76px;background-color:#F7FBF6;background-image:linear-gradient(90deg,transparent 58px,#E7A9A0 58px,#E7A9A0 60px,transparent 60px),repeating-linear-gradient(180deg,transparent 0 31px,#D6E2EA 31px 32px);border:0;border-radius:2px;box-shadow:6px 6px 0 rgba(59,58,54,.16);transform:rotate(-.4deg)}.ao-article .ao-nb.t2{transform:rotate(.4deg)}.ao-article .ao-nb:after{content:"";position:absolute;top:-13px;left:50%;width:120px;height:28px;margin-left:-60px;background:rgba(216,160,170,.62);transform:rotate(-3deg);clip-path:polygon(3% 0,97% 0,100% 20%,97% 40%,100% 60%,97% 80%,100% 100%,3% 100%,0 80%,3% 60%,0 40%,3% 20%)}.ao-article .ao-nb.t2:after{background:rgba(222,200,120,.62);transform:rotate(4deg);left:auto;right:40px;margin:0}
.ao-article .ao-nb:before{content:"";position:absolute;left:18px;top:32px;bottom:32px;width:16px;background:radial-gradient(circle at 8px 16px,#3B3A36 4px,transparent 4.6px) 0 0/16px 96px repeat-y}
.ao-article .ao-nb .hd{position:absolute;top:4px;left:76px;font-size:12px!important;font-weight:800;letter-spacing:2px;color:#B48A7A;line-height:24px}
.ao-article .ao-nb .r{position:relative}
.ao-article .ao-nb .no{position:absolute;left:-54px;top:0;width:34px;text-align:right;font:900 17px/32px "Noto Serif TC",Georgia,serif;color:#C59C8A}
.ao-article .ao-nb p.zh{margin:0!important;font-size:13px!important;line-height:32px!important;font-weight:800;color:#8A7F70;letter-spacing:1px}
.ao-article .ao-nb p.en{margin:0!important;font:600 17px/32px Georgia,"Times New Roman",serif!important;color:#3B3A36}
.ao-article .ao-nb p.en i{font-style:normal;color:#B5A998;margin:0 6px}

.ao-article .ao-nb.dl p.en b{font-family:-apple-system,"PingFang HK",sans-serif;font-size:14px;color:#2C6E49;margin-right:4px}.ao-article .ao-nb.dl p.zh{font-weight:500;letter-spacing:0;color:#7a7266;font-size:14px!important}.ao-article .ao-nb.dl .r+.r{margin-top:0}.ao-article .ao-nb.dl{margin:18px 0 52px!important}.ao-article .ao-nb.dl p.en .cn{font:500 14px/32px -apple-system,"PingFang HK",sans-serif;color:#7a7266;margin-left:4px}
@media(max-width:640px){.ao-article .ao-nb.dl{padding-left:54px}.ao-article .ao-nb{padding:32px 12px 32px 54px;background-image:linear-gradient(90deg,transparent 42px,#E7A9A0 42px,#E7A9A0 44px,transparent 44px),repeating-linear-gradient(180deg,transparent 0 31px,#D6E2EA 31px 32px)}.ao-article .ao-nb:before{left:10px;width:14px;background-size:14px 96px;background-position:-1px 0}.ao-article .ao-nb .hd{left:54px}.ao-article .ao-nb .no{left:-40px;width:26px;font-size:14px}.ao-article .ao-nb p.en{font-size:15.5px!important}}'''

def notebook(ul_html, head):
    items = re.findall(r'<li>(.*?)</li>', ul_html, re.S)
    rows = []
    for i, it in enumerate(items, 1):
        z, e = it.split('：', 1)
        rows.append(f'<div class="r"><span class="no">{i:02d}</span><p class="t zh">{z}</p><p class="t en">{e.replace("／", "<i>／</i>")}</p></div>')
    return f'<div class="ao-nb"><span class="hd">{head}</span>{"".join(rows)}</div>'

EMO = {'Waiter': '🤵', 'You': '🙋', 'Colleague': '🧑‍💼', 'Friend': '🧑‍🍳'}

def apply_nb(body):
    for aid, head, cls in (('say', 'MEMO · 自我介紹', ''), ('order', 'MEMO · 點餐', ' t2')):
        m = re.search(r'(id="%s">.*?)(<ul class="ao-ck">.*?</ul>)' % aid, body, re.S)
        body = body[:m.start(2)] + notebook(m.group(2), head).replace('class="ao-nb"', 'class="ao-nb' + cls + '"', 1) + body[m.end(2):]
    tapes = [' t2', '', ' t2']
    def dlg(m):
        k = len(dlg.n); dlg.n.append(1)
        rows = ''.join(f'<div class="r"><p class="t en"><b>{EMO.get(sp, "")} {sp}：</b>{en}<span class="cn">（{zh}）</span></p></div>'
                       for sp, en, zh in re.findall(r'<p><b>(.*?)：</b>(.*?)<small>(.*?)</small></p>', m.group(1)))
        return f'<div class="ao-nb dl{tapes[k % 3]}">{rows}</div>'
    dlg.n = []
    body = re.sub(r'<div class="ao-dlg">(.*?)</div>', dlg, body, flags=re.S)
    return '<style>' + NB_CSS.replace('\n', '') + '</style>\n' + body
