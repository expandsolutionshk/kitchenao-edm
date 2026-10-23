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
.ao-article .ao-tbx .ao-tbl{background:transparent}
.ao-article .ao-tbx .ao-tbl th{background:#3B3A36;color:#F4EFE6}
.ao-article .ao-tbx .ao-tbl td{border-top:1px solid rgba(59,58,54,.45)!important;color:#3B3A36}
.ao-article .ao-tbx .ao-tbl tbody tr:nth-child(4n+1) td{background:#F7F0DC}
.ao-article .ao-tbx .ao-tbl tbody tr:nth-child(4n+2) td{background:#F1E2DB}
.ao-article .ao-tbx .ao-tbl tbody tr:nth-child(4n+3) td{background:#E4E8DA}
.ao-article .ao-tbx .ao-tbl tbody tr:nth-child(4n) td{background:#DFE7EA}
@media(max-width:640px){.ao-article .ao-tbl.ao-tbl3{min-width:0!important;font-size:14.5px!important}.ao-article .ao-tbl3 th,.ao-article .ao-tbl3 td{padding:9px 8px!important;white-space:normal!important;overflow-wrap:anywhere}.ao-article .ao-tbl3 td:first-child{width:34%}.ao-article .ao-tbx{padding:12px 10px 14px}.ao-article .ao-tbh .t{font-size:18px}.ao-article .ao-tbh .o{display:none}.ao-article .ao-tbh .cal{width:44px}.ao-article .ao-tbh .cal i{font-size:20px}}'''

PAT = re.compile(r'<p class="t ao-tbt">列表(\d+)｜(.*?)</p>\s*(<div class="ao-tw">.*?</table></div>)', re.S)

def apply(body):
    titles = []
    def rep(m):
        n, t, tw = m.group(1), m.group(2), m.group(3)
        titles.append(t)
        rows = tw.count('<tr>') - 1
        if tw.split('</tr>')[0].count('<th>') == 3:
            tw = tw.replace('<table class="ao-tbl">', '<table class="ao-tbl ao-tbl3">', 1)
        tag = '比較表' if '比較' in t else f'{rows} 個用語'
        return (f'<div class="ao-tbx">'
                f'<div class="ao-tbh"><span class="cal"><b>列表</b><i>{n}</i></span><span class="t">{t}</span><span class="o">{tag}</span></div>{tw}</div>')
    body = PAT.sub(rep, body)
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

.ao-article .ao-nb.dl p.en b{font-family:-apple-system,"PingFang HK",sans-serif;font-size:14px;color:#2C6E49;margin-right:4px}.ao-article .ao-nb.dl p.zh{font-weight:500;letter-spacing:0;color:#7a7266;font-size:14px!important}.ao-article .ao-nb.dl .r+.r{margin-top:0}
@media(max-width:640px){.ao-article .ao-nb.dl{padding-left:54px}.ao-article .ao-nb{padding:32px 12px 32px 54px;background-image:linear-gradient(90deg,transparent 42px,#E7A9A0 42px,#E7A9A0 44px,transparent 44px),repeating-linear-gradient(180deg,transparent 0 31px,#D6E2EA 31px 32px)}.ao-article .ao-nb:before{left:10px;width:14px;background-size:14px 96px;background-position:-1px 0}.ao-article .ao-nb .hd{left:54px}.ao-article .ao-nb .no{left:-40px;width:26px;font-size:14px}.ao-article .ao-nb p.en{font-size:15.5px!important}}'''

def notebook(ul_html, head):
    items = re.findall(r'<li>(.*?)</li>', ul_html, re.S)
    rows = []
    for i, it in enumerate(items, 1):
        z, e = it.split('：', 1)
        rows.append(f'<div class="r"><span class="no">{i:02d}</span><p class="t zh">{z}</p><p class="t en">{e.replace("／", "<i>／</i>")}</p></div>')
    return f'<div class="ao-nb"><span class="hd">{head}</span>{"".join(rows)}</div>'

def apply_nb(body):
    for aid, head, cls in (('say', 'MEMO · 自我介紹', ''), ('order', 'MEMO · 點餐', ' t2')):
        m = re.search(r'(id="%s">.*?)(<ul class="ao-ck">.*?</ul>)' % aid, body, re.S)
        body = body[:m.start(2)] + notebook(m.group(2), head).replace('class="ao-nb"', 'class="ao-nb' + cls + '"', 1) + body[m.end(2):]
    tapes = [' t2', '', ' t2']
    def dlg(m):
        k = len(dlg.n); dlg.n.append(1)
        rows = ''.join(f'<div class="r"><p class="t en"><b>{sp}：</b>{en}</p><p class="t zh">{zh}</p></div>'
                       for sp, en, zh in re.findall(r'<p><b>(.*?)：</b>(.*?)<small>(.*?)</small></p>', m.group(1)))
        return f'<div class="ao-nb dl{tapes[k % 3]}">{rows}</div>'
    dlg.n = []
    body = re.sub(r'<div class="ao-dlg">(.*?)</div>', dlg, body, flags=re.S)
    return '<style>' + NB_CSS.replace('\n', '') + '</style>\n' + body
