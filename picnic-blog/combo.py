# 搜尋器整合版（篩選 + 地圖 + 一覽比較表 + B 款地點介紹）→ combo-mobile.html
# 2026-10-17：地點卡改用 B 款（列表＋詳情），加入官方資料（official.py）、野餐盒 pop up、資料來源
import importlib.util, json, os, re, html as H
from urllib.parse import quote
HERE = os.path.dirname(os.path.abspath(__file__))
def _load(n):
    s = importlib.util.spec_from_file_location(n, os.path.join(HERE, n + '.py')); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
_pk = _load('parks'); P = _pk.P; CATS = _pk.CATS
O = _load('official').O
def off(p):
    return O.get(p['name']) or O.get(p['name'].split(' / ')[0]) or {}
N = len(P)
GEO = {'tamar':(22.282,114.166),'sysmp':(22.290,114.142),'cyber':(22.261,114.130),'vpark':(22.282,114.188),'peak':(22.271,114.146),'mtdavis':(22.275,114.119),
'wkcd':(22.301,114.158),'ktct':(22.306,114.214),'shingfung':(22.318,114.206),'jvp':(22.323,114.219),'ktprom':(22.310,114.222),'ckl':(22.302,114.229),'namcheong':(22.326,114.155),'lokfu':(22.339,114.188),
'penfold':(22.401,114.204),'tpwp':(22.452,114.183),'velo':(22.316,114.263),'mospark':(22.426,114.231),'ngongping':(22.408,114.258),'taitamtun':(22.287,114.293),'tapmun':(22.471,114.360),'yuentun':(22.394,114.093),'tyipark':(22.358,114.106),'tyiwf':(22.350,114.098),'howo':(22.375,113.966),'tmpark':(22.392,113.976),'namsang':(22.465,114.030),'tswpark':(22.457,114.005),'ylpark':(22.440,114.017),
'inspire':(22.313,114.042),'db':(22.296,114.020),'ktsky':(22.3335,114.1960),'ktsq':(22.3300,114.1990),'csw':(22.3335,114.1505)}
LNG0, LNG1, LAT0, LAT1 = 113.86, 114.40, 22.19, 22.53
W, Hh = 540, 360
def xy(lat, lng): return ((lng-LNG0)/(LNG1-LNG0)*W, (LAT1-lat)/(LAT1-LAT0)*Hh)
LAND = {
 'mainland':[(113.90,22.36),(113.93,22.42),(113.98,22.48),(114.03,22.505),(114.10,22.525),(114.20,22.53),(114.30,22.50),(114.33,22.45),(114.29,22.41),(114.33,22.37),(114.30,22.28),(114.26,22.30),(114.22,22.302),(114.18,22.296),(114.16,22.297),(114.145,22.32),(114.10,22.35),(114.05,22.36),(113.99,22.368),(113.95,22.355)],
 'island':[(114.11,22.287),(114.15,22.292),(114.19,22.29),(114.23,22.287),(114.25,22.27),(114.24,22.23),(114.20,22.21),(114.15,22.22),(114.11,22.25)],
 'lantau':[(113.87,22.23),(113.91,22.28),(113.98,22.30),(114.05,22.322),(114.07,22.30),(114.03,22.245),(113.95,22.215),(113.89,22.215)],
 'tsingyi':[(114.085,22.34),(114.105,22.365),(114.12,22.35),(114.10,22.33)],
 'tapmun':[(114.352,22.465),(114.365,22.478),(114.37,22.466),(114.36,22.458)]}
land = ''.join(f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x,y in (xy(la,ln) for ln,la in pts))}"/>' for pts in LAND.values())
RN = {'hk':'港島','kln':'九龍','nt':'新界'}
RC = {'hk':'#E8743B','kln':'#3F9D5A','nt':'#1E5BD8'}
IC = lambda p: CATS[p['cats'][0]][0] if p['cats'] else '🧺'
VAC = 'https://resource.data.one.gov.hk/td/carpark/'
UTM = '?ao_ref=picnic_search'
def attrs(p): return f'data-id="{p["id"]}" data-r="{p["r"]}" data-car="{1 if p["car"] else 0}" data-pet="{p["pet"]}" data-cats="{" ".join(p["cats"])}"'
def unk(v): return (not v) or str(v).startswith('未能確認')
def esc(v): return H.escape(str(v))

# ---------- 地圖 pins ----------
pins = ''
for p in P:
    x, y = xy(*GEO[p['id']])
    pins += f'<a class="pin" href="#b-{p["id"]}" {attrs(p)} style="left:{x/W*100:.2f}%;top:{y/Hh*100:.2f}%;--c:{RC[p["r"]]}"><span><b>{IC(p)}</b></span><i>{p["name"]}</i></a>'

# ---------- 一覽比較表 ----------
ck = lambda v: '<b class="y">✓</b>' if v else '<span class="n">·</span>'
CK = list(CATS)
thead = '<tr><th class="st">地點</th><th title="可泊車">🚗<small>可泊車</small></th><th title="寵物">🐶<small>寵物</small></th>' + ''.join(f'<th title="{CATS[k][1]}">{CATS[k][0]}<small>{CATS[k][1]}</small></th>' for k in CK) + '</tr>'
trs = ''.join(f'<tr {attrs(p)}><td class="st"><a href="#b-{p["id"]}">{p["name"]}</a><small>{RN[p["r"]]}</small></td><td>{ck(p["car"])}</td><td>{"<b class=y>✓</b>" if p["pet"]=="Y" else ("<b class=p>指定</b>" if p["pet"]=="P" else "<span class=n>·</span>")}</td>' + ''.join(f'<td>{ck(k in p["cats"])}</td>' for k in CK) + '</tr>' for p in P)

# ---------- B 款地點卡 ----------
def ktags(p):
    t = ['<span class="t ok">🧺 適合野餐</span>']
    t += [f'<span class="t on">{CATS[c][0]} {CATS[c][1]}</span>' for c in p['cats']]
    if p['pet'] == 'Y': t.append('<span class="t pet">🐶 寵物友善</span>')
    elif p['pet'] == 'P': t.append('<span class="t pet">🐾 寵物指定範圍</span>')
    return ''.join(t)
def card(p, kw=False):
    o = off(p); imgs = o.get('img', []) or []
    thumb = o.get('thumb') or (imgs[1] if len(imgs) > 1 else (imgs[0] if imgs else ''))
    thumb_h = f'<img src="{thumb}" alt="{esc(p["name"])}" loading="lazy">' if thumb else '<span class="noimg">📷</span>'
    opn = o.get('open', '') if not unk(o.get('open')) else ''
    quick = []
    if opn: quick.append(f'<span>🕒 {esc(opn.split("；")[0])}</span>')
    quick.append(f'<span>🚇 {esc(p["tr"])}</span>')
    quick.append(f'<span>🅿️ {len(p["car"])} 個鄰近停車場</span>' if p['car'] else f'<span>🅿️ {esc(p.get("carnote","沒有停車場資料"))}</span>')
    # gallery
    if imgs:
        figs = ''.join(f'<figure><img src="{u}" alt="{esc(p["name"])}" loading="lazy"></figure>' for u in imgs)
        nav = '<button class="nav p" type="button" aria-label="上一張">‹</button><button class="nav n" type="button" aria-label="下一張">›</button>' if len(imgs) > 1 else ''
        dots = '<div class="dots">' + ''.join('<i class="on"></i>' if i == 0 else '<i></i>' for i in range(len(imgs))) + '</div>' if len(imgs) > 1 else ''
        gal = f'<div class="gal"><div class="tr">{figs}</div><span class="src">圖片來源：{o.get("imgsrc","官方網頁")}</span>{nav}{dots}</div>'
    else:
        gal = '<div class="gal none"><span>📷 相片待補</span></div>'
    facts = []
    if not unk(o.get('addr')): facts.append(('📍 地址', o['addr']))
    if opn: facts.append(('🕒 開放時間', opn))
    facts.append(('🚇 交通', p['tr']))
    if not unk(o.get('mg')): facts.append(('🏛️ 管理機構', o['mg']))
    facts_h = ''.join(f'<div><b>{a}</b>{esc(v)}</div>' for a, v in facts)
    # car
    if p['car']:
        seen = set(); lis = ''
        for n, f in p['car']:
            btn = ''
            if f and f not in seen:
                seen.add(f); btn = f'<button class="vac" type="button" data-src="{VAC}{f}">查看實時車位</button><span class="vres"></span>'
            lis += f'<li>🅿️ {esc(n)}{btn}</li>'
        car = f'<div class="kcar"><ul>{lis}</ul></div>'
    else:
        car = f'<div class="kcar none">⚠️ {esc(p.get("carnote","暫無停車場資料"))}</div>'
    fac = '' if unk(o.get('fac')) else ''.join(f'<span>{esc(x.strip())}</span>' for x in str(o['fac']).replace('，','、').replace(',', '、').replace('；','、').split('、') if x.strip())
    # buttons
    g = 'https://www.google.com/maps/search/?api=1&amp;query=' + quote(p['name'].split(' / ')[0] + ' 香港')
    btns = [f'<a class="btn b1" href="{g}" target="_blank" rel="noopener">📍 Google Map</a>']
    mp = o.get('map', '')
    if mp:
        if mp.lower().endswith('.pdf'): btns.append(f'<a class="btn b2" href="{mp}" target="_blank" rel="noopener">🗺️ 平面圖（PDF）</a>')
        else: btns.append(f'<button class="btn b2" type="button" data-img="{mp}" data-t="{esc(p["name"])}｜平面圖">🗺️ 公園平面圖</button>')
    if p.get('petmap'): btns.append(f'<button class="btn b2" type="button" data-img="{p["petmap"]}" data-t="{esc(p["name"])}｜寵物共享公園範圍">🐾 寵物共享範圍</button>')
    if o.get('url'): btns.append(f'<a class="btn b2" href="{o["url"]}" target="_blank" rel="noopener">🏛️ 官方網頁</a>')
    btns.append('<button class="btn b3 openP" type="button">🧺 預訂Kitchen AO野餐盒・送到附近可停車位置</button>')
    intro = '' if unk(o.get('intro')) else f'<div class="dsec s-more"><details class="more"><summary>📖 官方簡介</summary><p>{esc(o["intro"])}</p></details></div>'
    return f'''<article class="prow" id="b-{p['id']}" {attrs(p)}>
  <div class="sum">
    <div class="thumb">{thumb_h}<span class="rg" style="background:{RC[p['r']]}">{RN[p['r']]}</span></div>
    <div class="info"><div class="ttl"><h3>{p['name']}</h3><small>{p['en']}</small></div><div class="tg">{ktags(p)}</div>{f'<p class="pk-kw">目標關鍵字：<mark class="kw">{p["kw"]}</mark></p>' if kw else ''}<p class="kin">{p['intro']}</p><p class="quick">{''.join(quick)}</p></div>
    <div class="act"><button class="dbtn" type="button" aria-expanded="false"><span class="lb">詳情</span> <span class="ar">▾</span></button></div>
  </div>
  <div class="det">
    <div class="lc">{gal}<div class="facts">{facts_h}</div><div class="dsec s-car"><h4>🅿️ 鄰近停車場</h4>{car}</div></div>
    <div class="rc">
      {f'<div class="dsec s-fac"><h4>🌿 主要設施</h4><div class="fac">{fac}</div></div>' if fac else ''}
      <div class="dsec s-pet"><h4>🐶 寵物</h4><div class="pet">{p['petnote']}</div></div>
      <div class="btns">{''.join(btns)}</div>
      {intro}
    </div>
  </div>
</article>'''
items = ''.join(card(p) for p in P)

# ---------- 野餐盒 pop up ----------
PROD = [('2 人','二人小確幸套餐','$438','https://aoaodelivery.com/product/small-but-special-package-for-two/','https://aoaodelivery.com/wp-content/uploads/2023/10/202308-2pax-thumbnail_%E5%B7%A5%E4%BD%9C%E5%8D%80%E5%9F%9F-1-600x600.jpg','二人享樂拼盤＋清新沙律＋意大利麵＋惹味主食'),
('2 人','二人豪華儀式感UP!套餐','$588','https://aoaodelivery.com/product/luxury-ceremony-up-package-for-two/','https://aoaodelivery.com/wp-content/uploads/2023/10/202308-2pax-thumbnail-02-600x600.jpg','升級版：二人享樂拼盤＋清新沙律＋意大利麵＋惹味主食'),
('2 人','Chill一下野餐盒（小）','$258','https://aoaodelivery.com/product/chill%e4%b8%80picnic-small/','https://aoaodelivery.com/wp-content/uploads/2025/04/WhatsApp-Image-2025-04-12-at-4.08.18-PM-600x600.jpeg','主食 2 選 1＋小食 7 選 4＋甜品 4 選 2'),
('4–6 人','Chill一下野餐盒（大）','$628','https://aoaodelivery.com/product/chill%e4%b8%80picnic-big-for-4-6-persons/','https://aoaodelivery.com/wp-content/uploads/2025/04/WhatsApp-Image-2025-04-12-at-4.08.18-PM-600x600.jpeg','沙律＋主食 3 選 1＋小食 8 選 6＋甜品 4 選 3'),
('5 人','5 人自選拼盤','$498','https://aoaodelivery.com/product/5-people-self-selected-platter/','https://aoaodelivery.com/wp-content/uploads/2023/10/KitchenAO_platter_thumbnail_%E5%B7%A5%E4%BD%9C%E5%8D%80%E5%9F%9F-1-600x600-1.png','20 款小食自選 6 款')]
pcards = ''.join(f'<div class="pc"><div class="pim"><img src="{im}" alt="{n}" loading="lazy"><span class="ppl">👥 {ppl}</span></div><div class="pbd"><p class="pn">{n}</p><p class="pmenu">{menu}</p><div class="pft"><b class="pp">{pr}</b><a class="atc" href="{u}{UTM}" target="_blank" rel="noopener">🍱 揀選心水餐單</a></div></div></div>' for ppl,n,pr,u,im,menu in PROD)

# ---------- 資料來源（每行一個）----------
srcs = [('康樂及文化事務署 — 公園及動植物公園','https://www.lcsd.gov.hk/tc/facilities/facilitieslist/parks.html'),
        ('康樂及文化事務署 — 「寵物共享公園」及寵物共享範圍地圖','https://www.lcsd.gov.hk/tc/facilities/otherinfo/petpark.html'),
        ('運輸署 — 實時停車場空位資料（資料一線通）','https://data.gov.hk/tc-data/dataset/hk-td-tis_5-real-time-parking-vacancy-data'),
        ('漁農自然護理署 — 郊野公園','https://www.afcd.gov.hk/tc_chi/country/cou_lea/the_facts.html'),
        ('香港旅遊發展局 — 摩星嶺、愉景灣中央公園及彭福公園相片','https://www.discoverhongkong.com/tc/place-to-go/travel.guide-penfold-park.html')]
srcs_h = ''.join(f'<li><a href="{u}" target="_blank" rel="noopener">{esc(n)}</a></li>' for n, u in srcs) + '<li>各地點的官方資料，請參閱地點卡內「🏛️ 官方網頁」按鈕</li><li>地圖：地政總署地圖 API（香港地理空間數據共享平台）；相片：各官方網頁</li><li>核對日期：2026-10-17</li>'

chips_r = '<button class="ch on" data-f="r" data-v="all">全部</button>' + ''.join(f'<button class="ch" data-f="r" data-v="{k}"><i style="background:{RC[k]}"></i>{v}</button>' for k,v in RN.items())
chips_c = ''.join(f'<button class="ch" data-f="cat" data-v="{k}">{v[0]} {v[1]}</button>' for k,v in CATS.items())

CSS = '''
*{box-sizing:border-box}body{margin:0;background:#E9E5DC;font-family:-apple-system,"PingFang HK","Microsoft JhengHei",Arial,sans-serif;color:#3f3a33}
.vt{position:sticky;top:0;z-index:30;display:flex;justify-content:center;gap:6px;padding:10px;background:#E9E5DC}
.vt button{border:0;border-radius:30px;padding:9px 22px;font-size:14px;font-weight:800;background:#fff;color:#7a6a45;cursor:pointer;box-shadow:0 1px 4px rgba(0,0,0,.08)}.vt button.on{background:#1A1A1A;color:#fff}
.phone{container-type:inline-size;max-width:430px;margin:0 auto;background:#fff;min-height:100vh;box-shadow:0 0 30px rgba(0,0,0,.12);transition:max-width .25s;padding-bottom:30px}
.phone.d{max-width:1080px}
.hd{padding:16px 16px 12px;background:linear-gradient(135deg,#3F9D5A,#2C6E49);color:#fff}.hd p{margin:0;font-size:12px;opacity:.85}.hd h1{margin:4px 0 0;font-size:21px}
.flt{margin:12px;padding:12px;border:2px solid #3F9D5A;border-radius:16px;background:#fff}.frow{display:flex;flex-wrap:wrap;align-items:center;gap:6px;margin:0 0 8px}.lab{flex:0 0 100%;font-size:12px;font-weight:800;color:#2C6E49}
.ch{flex:0 0 auto;border:1.5px solid #CFE8CD;background:#F4FBF3;color:#2C6E49;border-radius:20px;padding:5px 11px;font-size:13px;font-weight:700;display:flex;align-items:center;gap:5px;cursor:pointer}
.ch i{width:9px;height:9px;border-radius:5px;display:inline-block}.ch.on{background:#3F9D5A;border-color:#3F9D5A;color:#fff}
.go{display:block;width:100%;margin:6px 0 10px;border:0;border-radius:30px;padding:12px;font-size:15px;font-weight:800;background:#1A1A1A;color:#fff;cursor:pointer}.go.pd{background:#3F9D5A;box-shadow:0 0 0 4px rgba(63,157,90,.25)}
.cnt{display:flex;justify-content:space-between;font-size:12.5px;font-weight:700;padding-top:2px}.cnt button{border:0;background:none;color:#9A7B2E;font-weight:700;text-decoration:underline;padding:0;cursor:pointer}
.sec{padding:14px 12px 4px}.sec h2{margin:0 0 8px;font-size:16px;color:#1A1A1A}.sec h2 small{font-weight:600;color:#9A8f7e;font-size:12px;margin-left:4px}
#lmap{height:340px;border-radius:14px;display:none}#lmap.on{display:block}.lpin{display:flex;align-items:center;justify-content:center;width:28px;height:28px;border-radius:14px;background:#fff;border:2.5px solid var(--c);box-shadow:0 2px 6px rgba(0,0,0,.3);font-size:14px}.leaflet-tooltip{font-weight:800;font-size:12px}
.map{position:relative;width:100%;aspect-ratio:540/360;border-radius:14px;overflow:hidden;background:#BFE0F0}
.map svg{position:absolute;inset:0;width:100%;height:100%}.map polygon{fill:#E8F1DD;stroke:#B9CDA4;stroke-width:1.2}.map .note{position:absolute;left:8px;bottom:6px;font-size:10.5px;color:#4d7b93;font-weight:700}
.pin{position:absolute;transform:translate(-50%,-100%);text-decoration:none;z-index:2}
.pin span{display:flex;align-items:center;justify-content:center;width:24px;height:24px;border-radius:12px 12px 12px 0;transform:rotate(-45deg);background:#fff;border:2px solid var(--c);box-shadow:0 2px 5px rgba(0,0,0,.25);font-size:12px}
.pin span b{display:block;transform:rotate(45deg);font-weight:400;line-height:1}
.pin i{position:absolute;left:50%;top:-20px;transform:translateX(-50%);display:none;font-style:normal;font-size:11px;font-weight:800;color:#1A1A1A;background:#fff;border-radius:6px;padding:1px 6px;white-space:nowrap;box-shadow:0 1px 4px rgba(0,0,0,.2)}
.pin:hover i,.pin.lbl i{display:block}
.lg{display:flex;flex-wrap:wrap;gap:4px 10px;margin-top:6px;font-size:11px;color:#7A7268}
.sec .sh{margin:0 0 8px;font-size:16px;color:#1A1A1A}.sec .sh small{font-weight:600;color:#9A8f7e;font-size:12px;margin-left:4px}
.tseo{margin:0 0 10px;font-size:14px;line-height:1.85;color:#5a5348}
.cmp{border:1.5px solid #3F9D5A;border-radius:14px;background:#fff;overflow:hidden}
.cmp summary{list-style:none;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:8px;padding:12px 14px;font-weight:800;font-size:14.5px;color:#2C6E49;background:#F4FBF3}.cmp summary::-webkit-details-marker{display:none}
.cmp .ar{transition:transform .2s}.cmp[open] .ar{transform:rotate(180deg)}
.thint{margin:0;padding:8px 12px;font-size:12px;color:#9A8f7e}
.cmp .tw{border:0;border-top:1px solid #EFE8DA;border-radius:0}
.tw{overflow-x:auto;border-radius:12px;border:1px solid #EFE8DA;max-height:520px;overflow-y:auto}
table{border-collapse:collapse;width:100%;table-layout:fixed;font-size:12px}
th{position:sticky;top:0;z-index:1;background:#1A1A1A;color:#fff;padding:6px 0;font-weight:700;font-size:13px}th small{display:block;font-size:9.5px;font-weight:600;opacity:.8}
td{padding:6px 0;text-align:center;border-bottom:1px solid #F2ECE0}
.st{text-align:left;width:34%;padding-left:6px!important;background:#fff}th.st{background:#1A1A1A}
td.st a{color:#1A1A1A;font-weight:800;text-decoration:none;font-size:12px;line-height:1.3;display:block}td.st small{display:block;color:#9A8f7e;font-size:10.5px}
tbody tr:nth-child(even) td{background:#FBF8F2}
.y{color:#2C6E49;font-size:14px}.p{color:#B07A3A;font-size:10px}.n{color:#d3cbbb}
.empty{display:none;padding:14px;text-align:center;background:#FFF4F2;border-radius:12px;font-size:13px}
.off{display:none!important}
/* ===== B 款地點卡 ===== */
.prow{border:1px solid #E7E0D2;border-radius:18px;background:#fff;box-shadow:0 3px 12px rgba(0,0,0,.05);overflow:hidden;margin:0 0 14px;scroll-margin-top:60px;transition:box-shadow .3s,border-color .3s}
.prow.hit{border-color:#3F9D5A;box-shadow:0 0 0 4px rgba(63,157,90,.25)}
.sum{display:grid;grid-template-columns:200px minmax(0,1fr) auto;gap:18px;padding:14px}
.thumb{position:relative;border-radius:14px;overflow:hidden;background:#DDEBD9;aspect-ratio:4/3;display:flex;align-items:center;justify-content:center}
.thumb img{width:100%;height:100%;object-fit:cover;display:block}.noimg{font-size:26px}
.thumb .rg{position:absolute;left:8px;top:8px;color:#fff;font-size:12px;font-weight:800;border-radius:20px;padding:3px 10px}
.info{min-width:0;display:flex;flex-direction:column;gap:9px}
.ttl{display:flex;align-items:baseline;flex-wrap:wrap;gap:3px 10px}.ttl h3{margin:0;font-size:20px;color:#1A1A1A;line-height:1.3}.ttl small{font-size:12.5px;color:#9A8f7e;font-weight:600}
.tg{display:flex;flex-wrap:wrap;gap:7px}
.t{display:inline-flex;align-items:center;gap:4px;font-size:12.5px;font-weight:700;padding:4px 11px;border-radius:20px;border:1.5px solid transparent}
.t.ok{background:#1A1A1A;color:#F7CE46}.t.on{background:#F4FBF3;color:#2C6E49;border-color:#CFE8CD}.t.pet{background:#FFF0E0;color:#C24E00;border-color:#F7D3AE}
.kin{margin:0;font-size:14.5px;line-height:1.8;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.quick{display:flex;flex-wrap:wrap;gap:4px 14px;margin:0;font-size:13px;color:#5a5348}
.act{display:flex;align-items:center}
.dbtn{border:0;border-radius:30px;padding:11px 20px;font-size:14px;font-weight:800;background:#1A1A1A;color:#fff;cursor:pointer;white-space:nowrap}
.dbtn .ar{display:inline-block;transition:transform .2s}.prow.open .dbtn .ar{transform:rotate(180deg)}
.det{display:none;border-top:1px dashed #E4D9C2;padding:18px 14px 20px}
.prow.open .det{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:24px;align-items:start}
.gal{position:relative;border-radius:14px;overflow:hidden;aspect-ratio:4/3;background:#DDEBD9}
.gal.none{display:flex;align-items:center;justify-content:center;color:#7FA27D;font-weight:700}
.gal .tr{display:flex;height:100%;overflow-x:auto;scroll-snap-type:x mandatory;scrollbar-width:none}.gal .tr::-webkit-scrollbar{display:none}
.gal figure{flex:0 0 100%;margin:0;scroll-snap-align:start}.gal img{width:100%;height:100%;object-fit:cover;display:block}
.gal .src{position:absolute;right:8px;top:8px;background:rgba(255,255,255,.88);font-size:11px;border-radius:6px;padding:2px 7px;color:#555}
.dots{position:absolute;left:0;right:0;bottom:12px;display:flex;justify-content:center;gap:6px}
.dots i{width:7px;height:7px;border-radius:4px;background:rgba(255,255,255,.6);box-shadow:0 1px 3px rgba(0,0,0,.25)}.dots i.on{background:#fff;width:16px}
.nav{position:absolute;top:50%;transform:translateY(-50%);width:34px;height:34px;border-radius:17px;border:0;background:rgba(255,255,255,.9);font-size:18px;font-weight:900;cursor:pointer;box-shadow:0 2px 6px rgba(0,0,0,.2)}.nav.p{left:8px}.nav.n{right:8px}
.facts{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:14px}
.facts div{background:#FAF7F1;border-radius:12px;padding:10px 12px;font-size:13px;line-height:1.6}.facts b{display:block;font-size:12px;color:#7a6a45;margin-bottom:3px}
.dsec{padding:14px 0}.dsec h4{margin:0 0 9px;font-size:14px;color:#1A1A1A}
.lc .s-car{padding-bottom:0}
.rc{display:flex;flex-direction:column}.rc .dsec{border-top:1px dashed #E4D9C2}.rc>.dsec:first-child{border-top:0;padding-top:0}
.fac{display:flex;flex-wrap:wrap;gap:7px}.fac span{font-size:12.5px;background:#F4FBF3;border:1px solid #CFE8CD;color:#2C6E49;border-radius:16px;padding:3px 10px}
.pet{background:#FFF8EC;border:1px solid #F3E2BF;border-radius:12px;padding:11px 13px;font-size:14px;line-height:1.75}
.kcar{background:#F6F8FB;border:1px solid #E2E8F2;border-radius:12px;padding:10px 13px;font-size:13.5px}.kcar.none{background:#FFF8EC;border-color:#F3E2BF}
.kcar ul{margin:0;padding:0}.kcar li{list-style:none;display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin:3px 0}
.vac{border:1px solid #1E5BD8;background:#fff;color:#1E5BD8;border-radius:20px;padding:3px 11px;font-size:12px;font-weight:700;cursor:pointer}.vres{font-weight:800;color:#2C6E49;font-size:12.5px}
.more summary{cursor:pointer;font-weight:800;font-size:14px;color:#1A1A1A;list-style:none}.more summary::-webkit-details-marker{display:none}
.more summary::after{content:" ▾";color:#3F9D5A}.more[open] summary::after{content:" ▴"}.more p{margin:10px 0 0;font-size:14px;line-height:1.85;color:#5a5348}
.btns{display:flex;flex-wrap:wrap;gap:10px;margin:14px 0 0}
.btn{flex:1 1 auto;display:flex;align-items:center;justify-content:center;gap:6px;text-decoration:none;border:0;border-radius:30px;padding:11px 14px;min-height:44px;font-size:13.5px;font-weight:800;cursor:pointer;white-space:nowrap}
.b1{background:#1A1A1A;color:#fff}.b2{background:#F4FBF3;color:#2C6E49;border:1.5px solid #3F9D5A}.b3{flex:1 1 100%;background:#3F9D5A;color:#fff}
.rc .s-more{margin-top:14px}
@container (max-width:640px){
  .sum{grid-template-columns:96px minmax(0,1fr);gap:12px;padding:12px}
  .thumb{aspect-ratio:1/1;align-self:start}
  .ttl h3{font-size:17px}.ttl small{font-size:11.5px;width:100%}
  .tg{gap:5px}.t{font-size:11.5px;padding:3px 8px}
  .kin{font-size:13.5px;line-height:1.7}.quick{font-size:12px;gap:3px 10px}
  .act{grid-column:1/-1}.dbtn{flex:1}
  .prow.open .det{grid-template-columns:1fr;gap:14px;padding:14px 12px 16px}
  .facts{gap:8px}.facts div{padding:9px 10px;font-size:12.5px}
  .btns{display:grid;grid-template-columns:1fr 1fr}.b3{grid-column:1/-1}.btn{white-space:normal;text-align:center}
  .rc .btns{order:1;margin-top:0}.rc .s-more{order:2;margin-top:12px;border-top:0}.rc .s-fac{order:3;border-top:1px dashed #E4D9C2!important;padding-top:14px!important}.rc .s-pet{order:4}
}
/* pop up */
.mdl{position:fixed;inset:0;z-index:99;background:rgba(20,20,20,.6);display:flex;align-items:center;justify-content:center;padding:14px}.mdl[hidden]{display:none}
.mbox{position:relative;background:#fff;border-radius:14px;padding:16px;max-width:860px;width:100%;max-height:90vh;overflow:auto}.mbox img{width:100%;height:auto;border-radius:8px;display:block}
.mt{margin:0 36px 8px 0;font-weight:800;font-size:14.5px}.msrc{margin:6px 0 0;font-size:12px;color:#7A7268;text-align:right}.mx{position:absolute;right:10px;top:8px;border:0;background:#F1EBDF;width:30px;height:30px;border-radius:15px;cursor:pointer}
.psub{margin:0 0 14px;font-size:13.5px;color:#5a5348;line-height:1.7}
.pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(190px,1fr));gap:14px}
.pc{border:1px solid #E7E0D2;border-radius:14px;overflow:hidden;display:flex;flex-direction:column}
.pim{position:relative;aspect-ratio:1/1;background:#F4FBF3}.pim img{width:100%;height:100%;object-fit:cover;display:block;border-radius:0}
.ppl{position:absolute;left:8px;top:8px;background:#1A1A1A;color:#F7CE46;font-size:12.5px;font-weight:800;border-radius:20px;padding:3px 10px}
.pbd{padding:12px;display:flex;flex-direction:column;flex:1;gap:6px}.pn{margin:0;font-weight:800;color:#1A1A1A;font-size:15px;line-height:1.4}
.pmenu{margin:0;font-size:12.5px;color:#7a6a45;line-height:1.6;flex:1}
.pft{display:flex;align-items:center;justify-content:space-between;gap:8px}.pp{font-size:18px;color:#C24E00}
.atc{background:#3F9D5A;color:#fff;text-decoration:none;font-weight:800;font-size:13px;border-radius:30px;padding:8px 12px;white-space:nowrap}
.pall{display:block;margin-top:14px;text-align:center;font-weight:800;color:#9A7B2E;text-decoration:none}
@media(max-width:520px){.pgrid{grid-template-columns:1fr 1fr}.pft{flex-direction:column;align-items:stretch}.atc{text-align:center}}
.srcs{margin:18px 12px 0;padding-top:14px;border-top:1px solid #E7E0D2;font-size:12.5px;color:#7a6a45}
.srcs h2{margin:0 0 8px;font-size:15px;color:#1A1A1A}.srcs ul{margin:0;padding-left:18px;line-height:1.9}.srcs a{color:#9A7B2E;word-break:break-all}
'''
JS = '''
var LM=null,LMK={};
(function(){if(!window.L)return;var m=document.getElementById('lmap');m.classList.add('on');document.getElementById('svgmap').style.display='none';LM=L.map(m,{scrollWheelZoom:false}).setView([22.36,114.13],10);var GB='https://mapapi.geodata.gov.hk/gs/api/v1.0.0/xyz/';L.tileLayer(GB+'basemap/WGS84/{z}/{x}/{y}.png',{maxZoom:19,minZoom:9,attribution:'<a href="https://api.portal.hkmapservice.gov.hk/disclaimer" target="_blank" rel="noopener">© 地政總署地圖</a>'}).addTo(LM);L.tileLayer(GB+'label/hk/tc/WGS84/{z}/{x}/{y}.png',{maxZoom:19,minZoom:9}).addTo(LM);PTS.forEach(function(p){var mk=L.marker([p.lat,p.lng],{icon:L.divIcon({className:'',html:'<div class="lpin" style="--c:'+p.c+'">'+p.ic+'</div>',iconSize:[28,28],iconAnchor:[14,14]})}).addTo(LM).bindTooltip(p.n);mk.on('click',function(){go('#b-'+p.id)});LMK[p.id]=mk;});})();
function go(h){var t=document.querySelector(h);if(!t)return;t.scrollIntoView({behavior:'smooth',block:'start'});t.classList.add('hit');setTimeout(function(){t.classList.remove('hit')},1800);}
(function(){
var ph=document.getElementById('phone');
document.querySelectorAll('.vt button').forEach(function(b){b.onclick=function(){document.querySelectorAll('.vt button').forEach(function(x){x.classList.toggle('on',x===b)});ph.classList.toggle('d',b.dataset.v==='d');if(LM)setTimeout(function(){LM.invalidateSize()},300);}});
var TOTAL=document.querySelectorAll('.prow').length;
var st={r:'all',car:0,pet:0,cats:[]};var els=document.querySelectorAll('[data-id]');
function ok(e){if(st.r!=='all'&&e.dataset.r!==st.r)return false;if(st.car&&e.dataset.car!=='1')return false;if(st.pet&&e.dataset.pet!=='Y')return false;var c=e.dataset.cats.split(' ');return st.cats.every(function(x){return c.indexOf(x)>-1})}
function apply(){var n=0;els.forEach(function(e){var o=ok(e);e.classList.toggle('off',!o);if(o&&e.classList.contains('prow'))n++;});
document.getElementById('cnt').textContent=(n===TOTAL?'全部 ':'符合：')+n+' 個地點';document.getElementById('empty').style.display=n?'none':'block';
if(LM){var vis=[];document.querySelectorAll('.prow').forEach(function(e){var mk=LMK[e.dataset.id];if(!mk)return;if(e.classList.contains('off')){LM.removeLayer(mk)}else{mk.addTo(LM);vis.push(mk.getLatLng())}});if(vis.length&&vis.length<PTS.length)LM.fitBounds(L.latLngBounds(vis).pad(0.3),{maxZoom:14});else LM.setView([22.36,114.13],10);}
document.querySelectorAll('.pk-region').forEach(function(g){g.style.display=g.querySelector('.prow:not(.off)')?'':'none'});var pins=document.querySelectorAll('.pin:not(.off)');pins.forEach(function(p){p.classList.toggle('lbl',pins.length<=6)});}
document.querySelectorAll('.ch').forEach(function(b){b.onclick=function(){var f=b.dataset.f,v=b.dataset.v;
if(f==='r'){st.r=v;document.querySelectorAll('.ch[data-f=r]').forEach(function(x){x.classList.toggle('on',x===b)})}
else if(f==='car'){st.car=!st.car;b.classList.toggle('on')}else if(f==='pet'){st.pet=!st.pet;b.classList.toggle('on')}
else{var i=st.cats.indexOf(v);if(i>-1)st.cats.splice(i,1);else st.cats.push(v);b.classList.toggle('on')}pend(true);}});
function pend(x){var g=document.getElementById('go');g.classList.toggle('pd',x);if(x)document.getElementById('cnt').textContent='已更改條件，請按「確定搜尋」';}
document.getElementById('go').onclick=function(){apply();pend(false);var t=document.getElementById('hk-map');if(t)t.scrollIntoView({behavior:'smooth',block:'start'});};
document.getElementById('rst').onclick=function(){st={r:'all',car:0,pet:0,cats:[]};document.querySelectorAll('.ch').forEach(function(x){x.classList.toggle('on',x.dataset.v==='all')});apply();pend(false);};
document.querySelectorAll('a[href^="#b-"]').forEach(function(a){a.onclick=function(ev){ev.preventDefault();go(a.getAttribute('href'));}});
document.querySelectorAll('.prow').forEach(function(r){
  var d=r.querySelector('.dbtn'),lb=d.querySelector('.lb');d.onclick=function(){var o=r.classList.toggle('open');d.setAttribute('aria-expanded',o);lb.textContent=o?'收起':'詳情';};
  var tr=r.querySelector('.tr');if(!tr)return;var ds=r.querySelectorAll('.dots i');
  tr.addEventListener('scroll',function(){var i=Math.round(tr.scrollLeft/tr.clientWidth);ds.forEach(function(x,k){x.classList.toggle('on',k===i)})});
  var p=r.querySelector('.nav.p'),n=r.querySelector('.nav.n');if(p)p.onclick=function(){tr.scrollBy({left:-tr.clientWidth,behavior:'smooth'})};if(n)n.onclick=function(){tr.scrollBy({left:tr.clientWidth,behavior:'smooth'})};
});
var md=document.getElementById('mdl'),mi=md.querySelector('img'),mt=md.querySelector('.mt');
document.querySelectorAll('[data-img]').forEach(function(b){b.onclick=function(){mi.src=b.dataset.img;mi.alt=b.dataset.t;mt.textContent=b.dataset.t;md.hidden=false;}});
function mcl(){md.hidden=true;mi.removeAttribute('src');}md.querySelector('.mx').onclick=mcl;md.onclick=function(e){if(e.target===md)mcl();};
var pm=document.getElementById('pmdl');document.querySelectorAll('.openP').forEach(function(b){b.onclick=function(){pm.hidden=false}});
function pcl(){pm.hidden=true}pm.querySelector('.mx').onclick=pcl;pm.onclick=function(e){if(e.target===pm)pcl()};
document.addEventListener('keydown',function(e){if(e.key==='Escape'){mcl();pcl()}});
document.querySelectorAll('.vac').forEach(function(b){b.onclick=function(){var o=b.nextElementSibling;o.textContent='讀取中…';
fetch(b.dataset.src).then(function(r){return r.json()}).then(function(j){var v=null;try{j.car_park[0].vehicle_type.forEach(function(t){if(t.type==='P')v=t.service_category[0].vacancy})}catch(e){}o.textContent=(v==null||v<0)?'暫無數據':'空位：'+v})
.catch(function(){o.innerHTML='<a href="'+b.dataset.src+'" target="_blank" rel="noopener">開啟數據</a>'})}});
apply();})();
'''

# ---------- 共用片段（combo-mobile.html 及 blog preview 共用）----------
from collections import Counter
_cc = Counter(c for p in P for c in p['cats']); _rc = Counter(p['r'] for p in P)
NCAR = sum(1 for p in P if p['car']); NPET = sum(1 for p in P if p['pet'] == 'Y'); NPETP = sum(1 for p in P if p['pet'] == 'P')
TBL_SEO = (f'全港 {N} 個野餐地點一覽：港島 {_rc["hk"]} 個、九龍 {_rc["kln"]} 個、新界 {_rc["nt"]} 個。'
           f'當中 {NCAR} 個鄰近設有停車場，適合駕車野餐；{NPET} 個屬寵物友善地點，另有 {NPETP} 個設寵物指定範圍，方便帶狗狗野餐。'
           f'按地點類別劃分，大草地 {_cc["lawn"]} 個、海景 {_cc["sea"]} 個、秘境 {_cc["hidden"]} 個及特色園林 {_cc["euro"]} 個。'
           '展開下表，即可一次比較各地點的泊車、寵物及類別資料。')
FILTER = f"""<div class="flt">
<div class="frow"><span class="lab">① 地區</span>{chips_r}</div>
<div class="frow"><span class="lab">② 條件及類別（可多選）</span><button class="ch" data-f="car" data-v="1">🚗 可泊車</button><button class="ch" data-f="pet" data-v="Y">🐶 寵物友善</button>{chips_c}</div>
<button class="go" id="go" type="button">🔍 確定搜尋</button>
<div class="cnt"><span id="cnt"></span><button id="rst">重設</button></div></div>"""
def MAP(hx='h2'):
    return f"""<div class="sec" id="hk-map"><{hx} class="sh">📍 地圖<small>點擊地圖標記查看地點介紹</small></{hx}><div id="lmap"></div><div class="map" id="svgmap"><svg viewBox="0 0 {W} {Hh}" preserveAspectRatio="none">{land}</svg>{pins}<span class="note">示意地圖，並非真實比例</span></div>
<div class="lg">{''.join(f'<span><b style="color:{RC[k]}">●</b> {v}</span>' for k,v in RN.items())}<span>標記內圖示＝主要類別</span></div></div>"""
def TABLE(hx='h2'):
    return f"""<div class="sec" id="hk-table"><{hx} class="sh">📊 全港野餐地點一覽比較表</{hx}><p class="tseo">{TBL_SEO}</p>
<details class="cmp"><summary><span>📊 展開一覽比較表（{N} 個地點）</span><b class="ar">▾</b></summary><p class="thint">點擊地點名稱，即可查看該地點介紹。</p><div class="tw"><table><thead>{thead}</thead><tbody>{trs}</tbody></table></div></details></div>"""
POPUPS = f"""<div class="mdl" id="pmdl" hidden><div class="mbox"><button class="mx" type="button" aria-label="關閉">✕</button><p class="mt">🧺 Kitchen AO 野餐盒｜送到附近可停車位置</p><p class="psub">選擇人數及套餐，按「揀選心水餐單」後於網站揀選菜式並完成訂購。消費滿 $1,450 免運費，於地面可停車位置車邊交收。</p><div class="pgrid">{pcards}</div><a class="pall" href="https://aoaodelivery.com/product-category/party/chill-box/{UTM}" target="_blank" rel="noopener">瀏覽全部野餐盒 →</a></div></div>
<div class="mdl" id="mdl" hidden><div class="mbox"><button class="mx" type="button" aria-label="關閉">✕</button><p class="mt"></p><img alt=""><p class="msrc">圖片來源︰官方網頁</p></div></div>"""
SRCS = f'<section class="srcs"><h2>資料來源</h2><ul>{srcs_h}</ul></section>'
LEAF_CSS = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.css">'
SCRIPTS = '<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.js"></script><script>var PTS=' + json.dumps([dict(id=p["id"],n=p["name"],lat=GEO[p["id"]][0],lng=GEO[p["id"]][1],c=RC[p["r"]],ic=IC(p)) for p in P],ensure_ascii=False) + ';</script><script>' + JS + '</script>'
PAGE_ONLY = ('*{', 'body{', '.vt', '.phone', '.hd')
def scope_css(css, pre):
    """將元件 CSS 加上前綴（供 WordPress 文章使用），略過 demo 頁面專用規則"""
    out = []; i = 0; n = len(css)
    def rules(block):
        res = []
        for m in re.finditer(r'([^{}]+)\{([^{}]*)\}', block):
            sel, body = m.group(1).strip(), m.group(2)
            parts = [x.strip() for x in sel.split(',')]
            if any(x.startswith(PAGE_ONLY) for x in parts): continue
            res.append(','.join(f'{pre} {x}' for x in parts) + '{' + body + '}')
        return '\n'.join(res)
    while i < n:
        j = css.find('@', i)
        if j < 0: out.append(rules(css[i:])); break
        out.append(rules(css[i:j]))
        k = css.index('{', j); depth = 1; e = k + 1
        while depth:
            depth += {'{': 1, '}': -1}.get(css[e], 0); e += 1
        out.append(css[j:k] + '{' + rules(css[k+1:e-1]) + '}')
        i = e
    return '\n'.join(x for x in out if x)
html = f'''<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>全港野餐地點搜尋器 Demo（{N} 個地點）</title>{LEAF_CSS}<style>{CSS}</style></head><body>
<div class="vt" role="tablist"><button class="on" data-v="m" role="tab">📱 手機版</button><button data-v="d" role="tab">💻 電腦版</button></div>
<div class="phone" id="phone">
<div class="hd"><p>Kitchen AO・Blog 1 搜尋器 Demo</p><h1>🧺 全港野餐地點搜尋器（{N} 個地點）</h1></div>
{FILTER}
{MAP()}
{TABLE()}
<div class="sec"><h2>📝 地點介紹</h2><p class="empty" id="empty">沒有符合條件的地點，請嘗試減少篩選條件。</p>{items}</div>
{SRCS}
{POPUPS}
</div>{SCRIPTS}</body></html>'''
if __name__ == '__main__':
    open(os.path.join(HERE, 'combo-mobile.html'), 'w').write(html); print(len(html), N)
