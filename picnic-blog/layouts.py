# 搜尋結果顯示方式 A–F 比較 Demo → layouts.html
import importlib.util, html as H
spec = importlib.util.spec_from_file_location('b', 'build.py'); b = importlib.util.module_from_spec(spec); spec.loader.exec_module(b)
IDS = ['tamar', 'cyber', 'wkcd', 'ktct', 'penfold', 'tapmun', 'inspire', 'howo']
PS = [next(p for p in b.P if p['id'] == i) for i in IDS]
GEO = {'tamar': (22.282, 114.166), 'cyber': (22.261, 114.130), 'wkcd': (22.301, 114.158), 'ktct': (22.306, 114.214),
       'penfold': (22.398, 114.205), 'tapmun': (22.471, 114.360), 'inspire': (22.313, 114.042), 'howo': (22.375, 113.966)}
RN = {'hk': '港島', 'kln': '九龍', 'nt': '新界', 'is': '離島'}
def tags(p, small=False): return b.tags(p)
def icons(p):
    s = ('🚗' if p['car'] else '') + ('🐶' if p['pet'] == 'Y' else ('🐾' if p['pet'] == 'P' else ''))
    return s + ''.join(b.CATS[c][0] for c in p['cats'])
def cars(p): return '、'.join(n for n, _ in p['car']) or p.get('carnote', '—')
PH = '<div class="ph">📷</div>'

# A 雙欄卡片
A = ''.join(f'<div class="a-card">{PH}<div class="bd"><h4>{p["name"]}</h4><div class="tg">{tags(p)}</div><p>{p["intro"]}</p><p class="s">🚇 {p["tr"]}</p><p class="s">🐶 {p["petnote"]}</p><div class="car">🅿️ {cars(p)}</div></div></div>' for p in PS[:4])
# B 橫向列表
B = ''.join(f'<details class="b-row"><summary><div class="ph sm">📷</div><div class="bd"><h4>{p["name"]} <span class="rg">{RN[p["r"]]}</span></h4><div class="tg">{tags(p)}</div><p>{p["intro"]}</p><p class="car">🅿️ {cars(p)}</p></div><span class="more">詳情 ▾</span></summary><div class="b-more">🚇 {p["tr"]}<br>🐶 {p["petnote"]}</div></details>' for p in PS)
# C 精簡卡＋展開
C = ''.join(f'<details class="c-card"><summary>{PH}<h4>{p["name"]}</h4><div class="ic">{icons(p)}</div><span class="more">撳睇詳情 ▾</span></summary><div class="c-more"><p>{p["intro"]}</p><p class="s">🚇 {p["tr"]}</p><p class="s">🐶 {p["petnote"]}</p><div class="car">🅿️ {cars(p)}</div></div></details>' for p in PS[:6])
# D 比較表
yes = lambda x: '<b class="y">✓</b>' if x else '<span class="n">—</span>'
D = '<div class="d-wrap"><table class="d-tb"><thead><tr><th>地點</th><th>地區</th><th>🚗</th><th>🐶</th>' + ''.join(f'<th>{v[0]}</th>' for k, v in list(b.CATS.items())[:4]) + '<th>鄰近停車場</th></tr></thead><tbody>'
for p in PS:
    D += f'<tr><td><a href="#">{p["name"]}</a></td><td>{RN[p["r"]]}</td><td>{yes(p["car"])}</td><td>{"<b class=y>✓</b>" if p["pet"]=="Y" else ("<b class=p>指定</b>" if p["pet"]=="P" else "<span class=n>—</span>")}</td>' + ''.join(f'<td>{yes(k in p["cats"])}</td>' for k in list(b.CATS)[:4]) + f'<td class="cp">{cars(p)}</td></tr>'
D += '</tbody></table></div>'
# E 地圖＋列表
lat0, lat1, lng0, lng1 = 22.20, 22.52, 113.90, 114.42
pins = ''.join(f'<a class="pin" href="#e-{p["id"]}" style="left:{(GEO[p["id"]][1]-lng0)/(lng1-lng0)*100:.1f}%;top:{(lat1-GEO[p["id"]][0])/(lat1-lat0)*100:.1f}%"><span>{b.CATS[p["cats"][0]][0]}</span><i>{p["name"]}</i></a>' for p in PS)
E = f'<div class="e-map"><div class="sea">香港（示意地圖，非真實比例）</div>{pins}</div><div class="e-list">' + ''.join(f'<div class="e-item" id="e-{p["id"]}"><b>{p["name"]}</b><span>{icons(p)}</span><small>🅿️ {cars(p)}</small></div>' for p in PS) + '</div>'
# F 每區左右滑
F = ''
for rid, rn in [('hk', '港島'), ('kln', '九龍'), ('nt', '新界')]:
    rp = [p for p in b.P if p['r'] == rid][:6]
    F += f'<p class="f-t">📍 {rn}（左右滑動）</p><div class="f-row">' + ''.join(f'<div class="f-card">{PH}<h4>{p["name"]}</h4><div class="ic">{icons(p)}</div></div>' for p in rp) + '</div>'

SEC = [('A', '雙欄卡片（而家用緊）', '資料最齊，但頁面最長。', f'<div class="a-grid">{A}</div>'),
       ('B', '橫向列表 List view（建議）', '一行一個地點，手機最易睇；交通、寵物說明撳「詳情」先展開。', B),
       ('C', '精簡卡＋展開詳情', '只顯示相、名、icon，撳卡先展開。最整齊，但大部分文字收埋。', f'<div class="c-grid">{C}</div>'),
       ('D', '比較表（建議放搜尋器上面做總覽）', '一眼比較邊個有泊車、寵物友善、海景；手機要左右滑。', D),
       ('E', '地圖＋列表', '最有「工具」感；正式版要用 Google Maps／Leaflet 同補經緯度。', E),
       ('F', '每區左右滑動', '版面最短，但篩選結果唔夠一目了然。', F)]
body = ''.join(f'<section class="lay" id="lay-{k}"><div class="lh"><span class="lk">{k}</span><div><h2>{t}</h2><p>{d}</p></div></div>{c}</section>' for k, t, d, c in SEC)
nav = ''.join(f'<a href="#lay-{k}">{k}</a>' for k, *_ in SEC)
CSS = '''
body{margin:0;background:#F4F1EA;font-family:-apple-system,"PingFang HK","Microsoft JhengHei",Arial,sans-serif;color:#3f3a33;}
.top{position:sticky;top:0;z-index:9;background:#1A1A1A;color:#fff;padding:10px 16px;display:flex;gap:10px;align-items:center;flex-wrap:wrap;font-weight:700;font-size:14px;}
.top a{color:#1A1A1A;background:#F7CE46;border-radius:20px;padding:3px 12px;text-decoration:none;}
.wrap{max-width:900px;margin:0 auto;padding:18px 14px 60px;}
.lay{background:#fff;border-radius:18px;padding:20px;margin:0 0 26px;box-shadow:0 4px 16px rgba(0,0,0,.06);}
.lh{display:flex;gap:14px;align-items:flex-start;margin:0 0 16px;}
.lk{flex:0 0 46px;height:46px;border-radius:23px;background:#3F9D5A;color:#fff;font:900 22px/46px sans-serif;text-align:center;}
.lh h2{margin:0 0 4px;font-size:20px;color:#1A1A1A;}.lh p{margin:0;font-size:14px;color:#7A7268;}
h4{margin:0 0 6px;font-size:16px;color:#1A1A1A;}
p{margin:0 0 6px;font-size:14px;line-height:1.65;}.s{font-size:13px;color:#5d534d;}
.ph{aspect-ratio:16/10;background:repeating-linear-gradient(45deg,#EEF6ED,#EEF6ED 10px,#E3F0E1 10px,#E3F0E1 20px);display:flex;align-items:center;justify-content:center;font-size:22px;}
.tg{display:flex;flex-wrap:wrap;gap:5px;margin:0 0 8px;}
.pk-tag{font-size:11.5px;font-weight:700;padding:2px 9px;border-radius:20px;}
.t-car{background:#E6F0FF;color:#1E5BD8;}.t-pet{background:#FFF0E0;color:#C24E00;}.t-pet2{background:#FFF7EC;color:#B07A3A;}.t-cat{background:#F4FBF3;color:#2C6E49;}
.car{margin-top:6px;padding:7px 10px;border-radius:10px;background:#F6F8FB;font-size:12.5px;color:#1E5BD8;}
/* A */.a-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px;}.a-card{border:1px solid #EBE3D2;border-radius:14px;overflow:hidden;}.a-card .bd{padding:12px;}
/* B */.b-row{border:1px solid #EBE3D2;border-radius:14px;margin:0 0 10px;overflow:hidden;}
.b-row summary{list-style:none;display:flex;gap:12px;padding:10px;cursor:pointer;align-items:flex-start;}.b-row summary::-webkit-details-marker{display:none;}
.ph.sm{flex:0 0 110px;aspect-ratio:1/1;border-radius:10px;}.b-row .bd{flex:1;min-width:0;}.b-row .car{display:inline-block;margin:0;padding:3px 8px;}
.rg{font-size:11.5px;color:#fff;background:#9A8f7e;border-radius:10px;padding:1px 8px;margin-left:4px;vertical-align:2px;}
.more{flex:0 0 auto;font-size:12.5px;font-weight:700;color:#9A7B2E;}.b-more{padding:0 14px 12px 132px;font-size:13px;line-height:1.7;}
/* C */.c-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;align-items:start;}
.c-card{border:1px solid #EBE3D2;border-radius:14px;overflow:hidden;}.c-card summary{list-style:none;cursor:pointer;padding:0 0 10px;text-align:center;}.c-card summary::-webkit-details-marker{display:none;}
.c-card h4{margin:8px 8px 4px;}.ic{font-size:18px;letter-spacing:2px;}.c-card .more{display:block;margin-top:4px;}.c-more{padding:0 12px 12px;}
/* D */.d-wrap{overflow-x:auto;}.d-tb{width:100%;min-width:640px;border-collapse:collapse;font-size:13.5px;}
.d-tb th{background:#1A1A1A;color:#fff;padding:8px 6px;font-size:13px;}.d-tb th:first-child{text-align:left;border-radius:10px 0 0 0;}.d-tb th:last-child{border-radius:0 10px 0 0;}
.d-tb td{padding:8px 6px;border-bottom:1px solid #EFE8DA;text-align:center;}.d-tb td:first-child{text-align:left;font-weight:700;}.d-tb tr:nth-child(even) td{background:#FBF8F2;}
.y{color:#2C6E49;font-size:16px;}.p{color:#B07A3A;font-size:12px;}.n{color:#c9c1b2;}.cp{text-align:left!important;font-size:12px;color:#1E5BD8;}
.d-tb a{color:#1A1A1A;}
/* E */.e-map{position:relative;height:340px;border-radius:14px;background:linear-gradient(160deg,#CFE8F5,#A9D4EC);overflow:hidden;margin:0 0 12px;}
.sea{position:absolute;left:12px;top:10px;font-size:12px;color:#3d6c86;font-weight:700;}
.pin{position:absolute;transform:translate(-50%,-100%);text-decoration:none;text-align:center;}
.pin span{display:block;width:34px;height:34px;line-height:34px;margin:0 auto;border-radius:17px 17px 17px 0;transform:rotate(-45deg);background:#fff;border:2px solid #3F9D5A;box-shadow:0 3px 8px rgba(0,0,0,.2);}
.pin span:first-letter{}.pin i{display:block;margin-top:4px;font-style:normal;font-size:11px;font-weight:800;color:#1A1A1A;background:rgba(255,255,255,.85);border-radius:6px;padding:0 4px;white-space:nowrap;}
.e-list{display:grid;grid-template-columns:repeat(2,1fr);gap:8px;}.e-item{display:flex;flex-direction:column;padding:8px 10px;border:1px solid #EBE3D2;border-radius:10px;font-size:13px;}.e-item small{color:#1E5BD8;}
/* F */.f-t{font-weight:800;color:#1A1A1A;margin:10px 0 6px;}.f-row{display:flex;gap:10px;overflow-x:auto;padding-bottom:6px;scroll-snap-type:x mandatory;}
.f-card{flex:0 0 160px;scroll-snap-align:start;border:1px solid #EBE3D2;border-radius:12px;overflow:hidden;text-align:center;padding-bottom:8px;}.f-card h4{font-size:14px;margin:6px 6px 2px;}
@media(max-width:640px){.a-grid,.e-list{grid-template-columns:1fr;}.c-grid{grid-template-columns:1fr 1fr;}.ph.sm{flex-basis:84px;}.b-more{padding-left:14px;}.b-row p:not(.car){display:none;}}
'''
out = f'''<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>野餐搜尋結果顯示方式 A–F</title><style>{CSS}</style></head><body>
<div class="top">搜尋結果顯示方式比較（示範用 {len(PS)} 個地點）：{nav}</div><div class="wrap">{body}</div></body></html>'''
open('layouts.html', 'w').write(out); print(len(out))
