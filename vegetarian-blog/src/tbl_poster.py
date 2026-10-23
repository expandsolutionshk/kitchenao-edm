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
@media(max-width:640px){.ao-article .ao-tbx{padding:12px 10px 14px}.ao-article .ao-tbh .t{font-size:18px}.ao-article .ao-tbh .o{display:none}.ao-article .ao-tbh .cal{width:44px}.ao-article .ao-tbh .cal i{font-size:20px}}'''

PAT = re.compile(r'<p class="t ao-tbt">列表(\d+)｜(.*?)</p>\s*(<div class="ao-tw">.*?</table></div>)', re.S)

def apply(body):
    titles = []
    def rep(m):
        n, t, tw = m.group(1), m.group(2), m.group(3)
        titles.append(t)
        rows = tw.count('<tr>') - 1
        tag = '比較表' if '比較' in t else f'{rows} 個用語'
        return (f'<div class="ao-tbx">'
                f'<div class="ao-tbh"><span class="cal"><b>列表</b><i>{n}</i></span><span class="t">{t}</span><span class="o">{tag}</span></div>{tw}</div>')
    body = PAT.sub(rep, body)
    txt = '列表0123456789' + ''.join(titles)
    font = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@900&display=swap&text='
            + urllib.parse.quote(''.join(sorted(set(txt)))) + '">')
    return font + '<style>' + CSS.replace('\n', '') + '</style>\n' + body
