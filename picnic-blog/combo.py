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
# 2026-10-18：改用官方座標（地政總署地名搜尋 HK1980 → WGS84；愉景灣用旅發局座標），來源見 geo_official.json
_GO = json.load(open(os.path.join(HERE, 'geo_official.json')))
GEO.update({k: (v['lat'], v['lng']) for k, v in _GO.items()})
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
RN = {'nt':'新界','kln':'九龍','hk':'港島'}
RC = {'hk':'#E8743B','kln':'#3F9D5A','nt':'#1E5BD8'}
IC = lambda p: CATS[p['cats'][0]][0] if p['cats'] else '🧺'
VAC = 'https://resource.data.one.gov.hk/td/carpark/'
UTM = '?ao_ref=picnic_search'
def attrs(p): return f'data-id="{p["id"]}" data-r="{p["r"]}" data-car="{1 if p["car"] else 0}" data-pet="{p["pet"]}" data-cats="{" ".join(p["cats"])}"'
AG = [('lcsd.gov.hk','康樂及文化事務署'),('afcd.gov.hk','漁農自然護理署'),('hiking.gov.hk','漁農自然護理署'),('info.gov.hk','政府新聞處'),
      ('discoverhongkong.com','香港旅遊發展局'),('westk.hk','西九文化區管理局'),('cyberport.hk','數碼港'),('disney.com','香港迪士尼樂園'),('ccidahk.gov.hk','文化創意產業發展處')]
def agency(u):
    for d, n in AG:
        if d in u: return n
    return ''
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
    if p['car']: t.append('<span class="t car">🚗 可泊車</span>')
    return ''.join(t)
def card(p, kw=False):
    o = off(p); imgs = o.get('img', []) or []
    thumb = o.get('thumb') or (imgs[1] if len(imgs) > 1 else (imgs[0] if imgs else ''))
    nm = esc(p['name'].split(' / ')[0])
    # 圖片載入失敗（斷 link）→ 凈色底＋地點名稱
    ERR = "onerror=\"this.onerror=null;this.parentNode.classList.add('ph');this.remove()\""
    thumb_h = f'<img src="{thumb}" alt="{esc(p["name"])}" loading="lazy" referrerpolicy="no-referrer" {ERR}>' if thumb else ''
    opn = o.get('open', '') if not unk(o.get('open')) else ''
    quick = []
    if opn: quick.append(f'<span>🕒 {esc(opn.split("；")[0])}</span>')
    quick.append(f'<span>🚇 {esc(p["tr"])}</span>')
    quick.append(f'<span>🅿️ {len(p["car"])} 個鄰近停車場</span>' if p['car'] else f'<span>🅿️ {esc(p.get("carnote","沒有停車場資料"))}</span>')
    # gallery
    if imgs:
        figs = ''.join(f'<figure data-n="{nm}"><span class="src">圖片來源：{agency(u)}</span><img src="{u}" alt="{esc(p["name"])}" loading="lazy" referrerpolicy="no-referrer" {ERR}></figure>' for u in imgs)
        nav = '<button class="nav p" type="button" aria-label="上一張">‹</button><button class="nav n" type="button" aria-label="下一張">›</button>' if len(imgs) > 1 else ''
        dots = '<div class="dots">' + ''.join('<i class="on"></i>' if i == 0 else '<i></i>' for i in range(len(imgs))) + '</div>' if len(imgs) > 1 else ''
        gal = f'<div class="gal"><div class="tr">{figs}</div>{nav}{dots}</div>'
    else:
        gal = f'<div class="gal ph" data-n="{nm}"></div>'
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
            elif not f:
                btn = '<span class="nodata">（運輸署未有提供實時車位數據）</span>'
            lis += f'<li>🅿️ {esc(n)}{btn}</li>'
        car = f'<div class="kcar"><ul>{lis}</ul></div>'
    else:
        car = f'<div class="kcar none">⚠️ {esc(p.get("carnote","暫無停車場資料"))}</div>'
    fac, facnote = '', ''
    if not unk(o.get('fac')):
        main, _, note = str(o['fac']).partition('；')          # 「；」後為補充說明
        items, buf, depth = [], '', 0
        for ch in main.replace('，', '、'):                       # 只拆括號以外的「、」
            depth += ch in '（(' ; depth -= ch in '）)'
            if ch == '、' and depth == 0: items.append(buf); buf = ''
            else: buf += ch
        items.append(buf)
        fac = ''.join(f'<span>{esc(x.strip())}</span>' for x in items if x.strip())
        facnote = f'<p class="facn">ℹ️ {esc(note.strip())}</p>' if note.strip() else ''
    # buttons
    g = 'https://www.google.com/maps/search/?api=1&amp;query=' + f"{GEO[p['id']][0]:.6f},{GEO[p['id']][1]:.6f}"  # 以官方座標開啟精確位置
    btns = [f'<a class="btn b1" href="{g}" target="_blank" rel="noopener">📍 Google Map</a>']
    mp = o.get('map', '')
    if mp:
        if mp.lower().endswith('.pdf'): btns.append(f'<a class="btn b2" href="{mp}" target="_blank" rel="noopener">🗺️ 平面圖（PDF）</a>')
        else: btns.append(f'<button class="btn b2" type="button" data-img="{mp}" data-s="{agency(mp)}" data-t="{esc(p["name"])}｜平面圖">🗺️ 公園平面圖</button>')
    if p.get('petmap'): btns.append(f'<button class="btn b2" type="button" data-img="{p["petmap"]}" data-s="{agency(p["petmap"])}" data-t="{esc(p["name"])}｜寵物共享公園範圍">🐾 寵物共享範圍</button>')
    btns.append('<button class="btn b3 openP" type="button">🧺 預訂Kitchen AO野餐盒・送到附近可停車位置</button>')
    intro = ''  # 2026-10-18：移除「官方簡介」（官方內容不會同步更新）
    return f'''<article class="prow" id="b-{p['id']}" {attrs(p)}>
  <div class="sum">
    <div class="thumb{'' if thumb else ' ph'}" data-n="{nm}">{thumb_h}<span class="rg" style="background:{RC[p['r']]}">{RN[p['r']]}</span></div>
    <div class="info"><div class="ttl"><h3>{p['name']}</h3><small>{p['en']}</small></div><div class="tg">{ktags(p)}</div>{f'<p class="pk-kw">目標關鍵字：<mark class="kw">{p["kw"]}</mark></p>' if kw else ''}<p class="kin">{p['intro']}</p><p class="quick">{''.join(quick)}</p></div>
    <div class="act"><button class="dbtn" type="button" aria-expanded="false"><span class="lb">詳情</span> <span class="ar">▾</span></button></div>
  </div>
  <div class="det">
    <div class="dhd">📋 {p['name'].split(' / ')[0]}詳情</div>
    <div class="lc">{gal}
      {f'<div class="dsec s-fac"><h4>🌿 主要設施</h4><div class="fac">{fac}</div>{facnote}</div>' if fac else ''}
      <div class="dsec s-pet"><h4>🐶 寵物</h4><div class="pet">{p['petnote']}</div></div>
    </div>
    <div class="rc">
      <div class="facts">{facts_h}</div>
      <div class="dsec s-car"><h4>🅿️ 鄰近停車場</h4>{car}</div>
      <div class="btns">{''.join(btns)}</div>
      {intro}
    </div>
    <button class="dclose" type="button">收起詳情 ▲</button>
  </div>
</article>'''
items = ''.join(card(p) for p in P)

# ---------- 野餐盒 pop up ----------
PROD = [('2 人','二人小確幸套餐','$438','https://aoaodelivery.com/product/small-but-special-package-for-two/','https://aoaodelivery.com/wp-content/uploads/2023/10/202308-2pax-thumbnail_%E5%B7%A5%E4%BD%9C%E5%8D%80%E5%9F%9F-1-600x600.jpg','二人享樂拼盤＋清新沙律＋意大利麵＋惹味主食'),
('2 人','二人豪華儀式感UP!套餐','$588','https://aoaodelivery.com/product/luxury-ceremony-up-package-for-two/','https://aoaodelivery.com/wp-content/uploads/2023/10/202308-2pax-thumbnail-02-600x600.jpg','升級版：二人享樂拼盤＋清新沙律＋意大利麵＋惹味主食'),
('2 人','Chill一下野餐盒（小）','$258','https://aoaodelivery.com/product/chill%e4%b8%80picnic-small/','https://aoaodelivery.com/wp-content/uploads/2025/04/WhatsApp-Image-2025-04-12-at-4.08.18-PM-600x600.jpeg','主食 2 選 1＋小食 7 選 4＋甜品 4 選 2'),
('4–6 人','Chill一下野餐盒（大）','$628','https://aoaodelivery.com/product/chill%e4%b8%80picnic-big-for-4-6-persons/','https://aoaodelivery.com/wp-content/uploads/2025/04/WhatsApp-Image-2025-04-12-at-4.08.18-PM-600x600.jpeg','沙律＋主食 3 選 1＋小食 8 選 6＋甜品 4 選 3'),
('5 人','5 人自選拼盤','$498','https://aoaodelivery.com/product/5-people-self-selected-platter/','https://aoaodelivery.com/wp-content/uploads/2023/10/KitchenAO_platter_thumbnail_%E5%B7%A5%E4%BD%9C%E5%8D%80%E5%9F%9F-1-600x600-1.png','20 款小食自選 6 款')]
def pcards_for(utm):
    return ''.join(f'<div class="pc"><div class="pim"><img src="{im}" alt="{n}" loading="lazy"><span class="ppl">👥 {ppl}</span></div><div class="pbd"><p class="pn">{n}</p><p class="pmenu">{menu}</p><div class="pft"><b class="pp">{pr}</b><a class="atc" href="{u}{utm}" target="_blank" rel="noopener">🍱 揀選心水餐單</a></div></div></div>' for ppl,n,pr,u,im,menu in PROD)
pcards = pcards_for(UTM)

# ---------- 資料來源（每行一個）----------
srcs = [('康樂及文化事務署 — 公園及動植物公園','https://www.lcsd.gov.hk/tc/facilities/facilitieslist/parks.html'),
        ('康樂及文化事務署 — 「寵物共享公園」及寵物共享範圍地圖','https://www.lcsd.gov.hk/tc/facilities/otherinfo/petpark.html'),
        ('運輸署 — 實時停車場空位資料（資料一線通）','https://data.gov.hk/tc-data/dataset/hk-td-tis_5-real-time-parking-vacancy-data'),
        ('漁農自然護理署 — 郊野公園','https://www.afcd.gov.hk/tc_chi/country/cou_lea/the_facts.html'),
        ('香港旅遊發展局 — 摩星嶺、愉景灣中央公園、彭福公園及清水灣郊野公園相片','https://www.discoverhongkong.com/tc/place-to-go/travel.guide-penfold-park.html'),
        ('文化創意產業發展處 — 樂富配水庫休憩花園相片','https://fpf.ccidahk.gov.hk/tc/location/detail.php?id=1792')]
srcs_h = ''.join(f'<li><a href="{u}" target="_blank" rel="noopener">{esc(n)}</a></li>' for n, u in srcs) + '<li>地圖：地政總署地圖 API（香港地理空間數據共享平台）；相片：康樂及文化事務署、漁農自然護理署、香港旅遊發展局等機構</li><li>核對日期：2026-10-17</li>'

chips_r = '<button class="ch on" data-f="r" data-v="all">全部</button>' + ''.join(f'<button class="ch" data-f="r" data-v="{k}"><i style="background:{RC[k]}"></i>{v}</button>' for k,v in RN.items())
chips_c = ''.join(f'<button class="ch" data-f="cat" data-v="{k}">{v[0]} {v[1]}</button>' for k,v in CATS.items())

CSS = '''
*{box-sizing:border-box}body{margin:0;background:#E9E5DC;font-family:-apple-system,"PingFang HK","Microsoft JhengHei",Arial,sans-serif;color:#3f3a33}
.vt{position:sticky;top:0;z-index:30;display:flex;justify-content:center;gap:6px;padding:10px;background:#E9E5DC}
.vt button{border:0;border-radius:30px;padding:9px 22px;font-size:14px;font-weight:800;background:#fff;color:#7a6a45;cursor:pointer;box-shadow:0 1px 4px rgba(0,0,0,.08)}.vt button.on{background:#1A1A1A;color:#fff}
.phone{container-type:inline-size;max-width:430px;margin:0 auto;background:#fff;min-height:100vh;box-shadow:0 0 30px rgba(0,0,0,.12);transition:max-width .25s;padding-bottom:30px}
.phone.d{max-width:1080px}
.hd{padding:16px 16px 12px;background:linear-gradient(135deg,#3F9D5A,#2C6E49);color:#fff}.hd p{margin:0;font-size:12px;opacity:.85}.hd h1{margin:4px 0 0;font-size:21px}
.flt{margin:12px;padding:18px 20px 16px;border:1.5px solid #CFE8CD;border-radius:18px;background:#fff;box-shadow:0 4px 16px rgba(44,110,73,.08)}.frow{display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin:0 0 16px}.frow.f1{}.lab{flex:0 0 100%;display:flex;align-items:center;gap:10px;margin-bottom:4px;font-size:14.5px;font-weight:800;color:#1A1A1A;letter-spacing:.3px}.fhd{margin:0 0 12px;font-size:15.5px;font-weight:900;color:#2C6E49}.flt .frow+.frow,.flt .fhd+.frow{border-top:1px dashed #E4D9C2;padding-top:14px}.no{position:relative;flex:0 0 auto;display:inline-flex;align-items:center;justify-content:center;width:28px;height:28px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#FFE58A,#F7CE46 55%,#D9A21B);color:#1A1A1A;font-style:normal;font-weight:900;font-size:14px;border:2px solid #1A1A1A;box-shadow:2px 2px 0 #1A1A1A}.go .no{width:24px;height:24px;font-size:13px;margin-right:6px;border-color:#F7CE46;box-shadow:none}
.ch{flex:0 0 auto;border:1.5px solid #CFE8CD;background:#F4FBF3;color:#2C6E49;border-radius:22px;padding:7px 14px;font-size:14px;font-weight:700;display:flex;align-items:center;gap:5px;cursor:pointer;transition:background .15s,border-color .15s}.ch:hover{border-color:#3F9D5A}
.ch i{width:9px;height:9px;border-radius:5px;display:inline-block}.ch.on{background:#3F9D5A;border-color:#3F9D5A;color:#fff}
.cnt #rst{margin-left:auto}.go{display:inline-flex;align-items:center;gap:4px;width:auto;margin:0;border:0;border-radius:30px;padding:8px 20px;font-size:14px;font-weight:800;background:#1A1A1A;color:#fff;cursor:pointer}.go.pd{background:#3F9D5A;box-shadow:0 0 0 4px rgba(63,157,90,.25)}
.cnt{display:flex;align-items:center;gap:14px;flex-wrap:wrap;font-size:13.5px;font-weight:700;color:#5a5348;margin-top:2px;padding-top:14px;border-top:1px solid #EFE8DA}.cnt #rst{border:0;background:none;color:#9A7B2E;font-weight:700;text-decoration:underline;padding:0;cursor:pointer}
.sec{padding:14px 12px 4px}.sec h2{margin:0 0 8px;font-size:18px;color:#1A1A1A}.sec h2 small{font-weight:600;color:#9A8f7e;font-size:12px;margin-left:4px}
#lmap{height:360px;border-radius:14px;display:none}.leaflet-touch .leaflet-bar a{width:40px;height:40px;line-height:40px;font-size:22px}.mhint{display:none}.fbar,.shd{display:none}.msheet .fbar{display:flex;align-items:center;gap:10px;margin:12px}.fbtn{display:inline-flex;align-items:center;gap:6px;border:1.5px solid #3F9D5A;background:#fff;color:#2C6E49;border-radius:24px;padding:8px 16px;font-weight:800;font-size:14.5px;cursor:pointer;font-family:inherit}.fbd{background:#3F9D5A;color:#fff;border-radius:10px;padding:0 7px;font-size:12px}.fsum{font-size:13.5px;font-weight:700;color:#5a5348}.msheet .flt:not(.sheet){display:none}.flt.sheet{position:fixed;left:0;right:0;bottom:0;margin:0;z-index:10001;border:0;border-radius:20px 20px 0 0;max-height:85vh;overflow-y:auto;padding:8px 16px 18px;box-shadow:0 -6px 24px rgba(0,0,0,.2);transform:translateY(100%);transition:transform .25s}.flt.sheet.on{transform:none}.flt.sheet .shd{display:flex;align-items:center;justify-content:space-between;position:relative;padding:14px 0 12px;font-size:16px;color:#1A1A1A}.shd .grab{position:absolute;left:50%;top:2px;margin-left:-20px;width:40px;height:4px;border-radius:2px;background:#DDD}.shd .sx{border:0;background:none;font-size:20px;cursor:pointer;color:#1A1A1A}.flt.sheet .go{flex:1 1 auto;justify-content:center;padding:11px 16px;font-size:15px}.fbg{position:fixed;inset:0;background:rgba(0,0,0,.45);z-index:10000;opacity:0;transition:opacity .2s}.fbg.on{opacity:1}.leaflet-tile-container img.leaflet-tile{width:256.6px!important;height:256.6px!important;max-width:none!important}.lclu{display:flex;align-items:center;justify-content:center;width:36px;height:36px;border-radius:18px;background:#3F9D5A;color:#fff;font-weight:900;font-size:14px;border:3px solid #fff;box-shadow:0 2px 8px rgba(0,0,0,.35)}.mpop{display:flex;flex-direction:column;gap:6px;font-family:inherit}.mpop img{width:100%;height:110px;object-fit:cover;border-radius:8px}.mpop b{font-size:15px;color:#1A1A1A}.mpop .mt{font-size:12px;color:#5a5348;line-height:1.6}.mpbtn{border:0;border-radius:20px;background:#1A1A1A;color:#fff;font-weight:800;font-size:13px;padding:7px 12px;cursor:pointer}.mf{display:none}#lmap.on{display:block}.lpin{display:flex;align-items:center;justify-content:center;width:28px;height:28px;border-radius:14px;background:#fff;border:2.5px solid var(--c);box-shadow:0 2px 6px rgba(0,0,0,.3);font-size:14px}.leaflet-tooltip{font-weight:800;font-size:12px}
.map{position:relative;width:100%;aspect-ratio:540/360;border-radius:14px;overflow:hidden;background:#BFE0F0}
.map svg{position:absolute;inset:0;width:100%;height:100%}.map polygon{fill:#E8F1DD;stroke:#B9CDA4;stroke-width:1.2}.map .note{position:absolute;left:8px;bottom:6px;font-size:11px;color:#4d7b93;font-weight:700}
.pin{position:absolute;transform:translate(-50%,-100%);text-decoration:none;z-index:2}
.pin span{display:flex;align-items:center;justify-content:center;width:24px;height:24px;border-radius:12px 12px 12px 0;transform:rotate(-45deg);background:#fff;border:2px solid var(--c);box-shadow:0 2px 5px rgba(0,0,0,.25);font-size:12px}
.pin span b{display:block;transform:rotate(45deg);font-weight:400;line-height:1}
.pin i{position:absolute;left:50%;top:-20px;transform:translateX(-50%);display:none;font-style:normal;font-size:11px;font-weight:800;color:#1A1A1A;background:#fff;border-radius:6px;padding:1px 6px;white-space:nowrap;box-shadow:0 1px 4px rgba(0,0,0,.2)}
.pin:hover i,.pin.lbl i{display:block}
.lg{display:flex;flex-wrap:wrap;gap:4px 10px;margin-top:6px;font-size:12px;color:#7A7268}
.sec .sh{margin:0 0 8px;font-size:18px;color:#1A1A1A}.sec .sh small{font-weight:600;color:#9A8f7e;font-size:12px;margin-left:4px}
.tseo{margin:0 0 10px;font-size:15px;line-height:1.85;color:#5a5348}
#hk-table{padding-bottom:22px;margin-bottom:8px;border-bottom:2px solid #EFE8DA}
.cmp{border:0;background:none}
.cmp summary{list-style:none;cursor:pointer;display:inline-flex;align-items:center;gap:6px;padding:9px 20px;border-radius:30px;background:#3F9D5A;color:#fff;font-weight:800;font-size:14px;box-shadow:0 2px 6px rgba(63,157,90,.3)}.cmp summary::-webkit-details-marker{display:none}.cmp summary:hover{background:#2C6E49}
.cmp .ar{transition:transform .2s}.cmp[open] .ar{transform:rotate(180deg)}.cmp .c{display:none}.cmp[open] .c{display:inline}.cmp[open] .o{display:none}
.cmp[open] .tw{margin-top:10px;border:1.5px solid #3F9D5A}
.thint{margin:0;padding:8px 12px;font-size:12px;color:#9A8f7e}
.cmp .tw{border-radius:12px}
.tw{overflow-x:auto;border-radius:12px;border:1px solid #EFE8DA}
table{border-collapse:collapse;width:100%;table-layout:fixed;font-size:13px}
th{position:sticky;top:0;z-index:1;background:#1A1A1A;color:#fff;padding:10px 2px;font-weight:700;font-size:13px}th small{display:block;margin-top:3px;font-size:11.5px;font-weight:600;opacity:.85}
td{padding:11px 2px;text-align:center;vertical-align:middle;border-bottom:1px solid #F2ECE0}
.st{text-align:left;width:34%;padding-left:14px!important;padding-right:8px!important;background:#fff}th.st{background:#1A1A1A}
td.st a{color:#1A1A1A;font-weight:800;text-decoration:none;font-size:14px;line-height:1.4;display:block}td.st small{display:block;margin-top:3px;color:#9A8f7e;font-size:12px}
tbody tr:nth-child(even) td{background:#FBF8F2}
.y{color:#2C6E49;font-size:14px}.p{color:#B07A3A;font-size:11px}.n{color:#d3cbbb}
.empty{display:none;padding:14px;text-align:center;background:#FFF4F2;border-radius:12px;font-size:13px}
.off{display:none!important}
/* ===== B 款地點卡 ===== */
.prow{border:1px solid #E7E0D2;border-radius:18px;background:#fff;box-shadow:0 3px 12px rgba(0,0,0,.05);overflow:hidden;margin:0 0 14px;scroll-margin-top:60px;transition:box-shadow .3s,border-color .3s}
.prow.hit{border-color:#3F9D5A;box-shadow:0 0 0 4px rgba(63,157,90,.25)}.prow.open{border:2px solid #3F9D5A;box-shadow:0 8px 26px rgba(44,110,73,.18)}.dhd{grid-column:1/-1;display:flex;align-items:center;gap:6px;margin:0 0 2px;padding:9px 14px;border-radius:10px;background:#F4FBF3;color:#2C6E49;font-weight:800;font-size:15px}.tclose{display:block;width:100%;margin-top:12px;border:1.5px solid #3F9D5A;background:#fff;color:#2C6E49;border-radius:30px;padding:10px;font-size:14px;font-weight:800;cursor:pointer;font-family:inherit}.dclose{grid-column:1/-1;display:block;width:100%;margin-top:4px;border:1.5px solid #3F9D5A;background:#fff;color:#2C6E49;border-radius:30px;padding:10px;font-size:14px;font-weight:800;cursor:pointer;font-family:inherit}
.sum{display:grid;grid-template-columns:200px minmax(0,1fr) auto;gap:18px;padding:14px}
.thumb{position:relative;border-radius:14px;overflow:hidden;background:#DDEBD9;aspect-ratio:4/3;display:flex;align-items:center;justify-content:center}
.thumb img{width:100%;height:100%;object-fit:cover;display:block}
.ph{background:#E3EFDF!important;display:flex;align-items:center;justify-content:center}.ph::after{content:attr(data-n);color:#2C6E49;font-weight:800;font-size:15px;text-align:center;padding:8px;line-height:1.4}
.gal figure.ph,.gal.ph{display:flex}.gal.ph::after{font-size:20px}
.thumb .rg{position:absolute;left:8px;top:8px;color:#fff;font-size:12px;font-weight:800;border-radius:20px;padding:3px 10px}
.info{min-width:0;display:flex;flex-direction:column;gap:9px}
.ttl{display:flex;align-items:baseline;flex-wrap:wrap;gap:3px 10px}.ttl h3{margin:0;font-size:20px;color:#1A1A1A;line-height:1.3}.ttl small{font-size:13px;color:#9A8f7e;font-weight:600}
.tg{display:flex;flex-wrap:wrap;gap:6px}
.t{display:inline-flex;align-items:center;gap:3px;font-size:12px;line-height:1.35;white-space:nowrap;font-weight:700;padding:2px 9px;border-radius:20px;border:1px solid transparent}
.t.ok{background:#FFF6D6;color:#8A6A00;border-color:#F0DC9A}.t.on{background:#F4FBF3;color:#2C6E49;border-color:#CFE8CD}.t.car{background:#E6F0FF;color:#1E5BD8;border-color:#C7DAFB}.t.pet{background:#FFF0E0;color:#C24E00;border-color:#F7D3AE}
.kin{margin:0;font-size:15.5px;line-height:1.8;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.quick{display:flex;flex-wrap:wrap;gap:4px 14px;margin:0;font-size:13.5px;color:#5a5348}
.act{display:flex;align-items:center}
.dbtn{border:0;border-radius:30px;padding:11px 20px;font-size:14px;font-weight:800;background:#1A1A1A;color:#fff;cursor:pointer;white-space:nowrap}
.dbtn .ar{display:inline-block;transition:transform .2s}.prow.open .dbtn .ar{transform:rotate(180deg)}
.det{display:none;border-top:1px dashed #E4D9C2;padding:18px 14px 20px}
.prow.open .det{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:24px;align-items:start}
.gal{position:relative;border-radius:14px;overflow:hidden;aspect-ratio:4/3;background:#DDEBD9}
.gal.none{display:flex;align-items:center;justify-content:center;color:#7FA27D;font-weight:700}
.gal .tr{display:flex;height:100%;overflow-x:auto;scroll-snap-type:x mandatory;scrollbar-width:none}.gal .tr::-webkit-scrollbar{display:none}
.gal figure{position:relative;flex:0 0 100%;margin:0;scroll-snap-align:start}.gal img{width:100%;height:100%;object-fit:cover;display:block}
.gal .src{position:absolute;right:8px;top:8px;background:rgba(255,255,255,.88);font-size:11px;border-radius:6px;padding:2px 7px;color:#555}
.dots{position:absolute;left:0;right:0;bottom:12px;display:flex;justify-content:center;gap:6px}
.dots i{width:7px;height:7px;border-radius:4px;background:rgba(255,255,255,.6);box-shadow:0 1px 3px rgba(0,0,0,.25)}.dots i.on{background:#fff;width:16px}
.nav{position:absolute;top:50%;transform:translateY(-50%);width:34px;height:34px;border-radius:17px;border:0;background:rgba(255,255,255,.9);font-size:18px;font-weight:900;cursor:pointer;box-shadow:0 2px 6px rgba(0,0,0,.2)}.nav.p{left:8px}.nav.n{right:8px}
.facts{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:14px}
.facts div{background:#FAF7F1;border-radius:12px;padding:10px 12px;font-size:14px;line-height:1.6}.facts b{display:block;font-size:12.5px;color:#7a6a45;margin-bottom:3px}
.dsec{padding:14px 0}.dsec h4{margin:0 0 9px;font-size:15px;color:#1A1A1A}
.lc .dsec{border-top:1px dashed #E4D9C2;margin-top:14px}.lc .s-pet{padding-bottom:0}.rc .facts{margin-top:0}.rc .s-car{padding-bottom:0}
.rc{display:flex;flex-direction:column}.rc .dsec{border-top:1px dashed #E4D9C2;margin-top:14px}
.facn{margin:8px 0 0;font-size:13px;color:#7a6a45;line-height:1.6}.fac{display:flex;flex-wrap:wrap;gap:7px}.fac span{font-size:13px;background:#F4FBF3;border:1px solid #CFE8CD;color:#2C6E49;border-radius:16px;padding:3px 10px}
.s-pet .pet{background:#FFF8EC;border:1px solid #F3E2BF;border-radius:12px;padding:11px 13px;font-size:15px;line-height:1.75}
.kcar{background:#F6F8FB;border:1px solid #E2E8F2;border-radius:12px;padding:10px 13px;font-size:14px}.kcar.none{background:#FFF8EC;border-color:#F3E2BF}
.kcar ul{margin:0;padding:0}.kcar li{list-style:none;display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin:3px 0}
.vac{border:1px solid #1E5BD8;background:#fff;color:#1E5BD8;border-radius:20px;padding:3px 11px;font-size:12.5px;font-weight:700;cursor:pointer}.nodata{font-size:12px;color:#9A8f7e;font-weight:600}.vres{font-weight:800;color:#2C6E49;font-size:12.5px}
.more summary{cursor:pointer;font-weight:800;font-size:15px;color:#1A1A1A;list-style:none}.more summary::-webkit-details-marker{display:none}
.more summary::after{content:" ▾";color:#3F9D5A}.more[open] summary::after{content:" ▴"}.more p{margin:10px 0 0;font-size:15px;line-height:1.85;color:#5a5348}
.btns{display:flex;flex-wrap:wrap;gap:10px;margin:14px 0 0}
.btn{flex:1 1 auto;display:flex;align-items:center;justify-content:center;gap:6px;text-decoration:none;border:0;border-radius:30px;padding:11px 14px;min-height:44px;font-size:14px;font-weight:800;cursor:pointer;white-space:nowrap}
.b1{background:#1A1A1A;color:#fff}.b2{background:#F4FBF3;color:#2C6E49;border:1.5px solid #3F9D5A}.b3{flex:1 1 100%;background:#3F9D5A;color:#fff}
.rc .s-more{margin-top:14px}
@container (min-width:641px){#lmap{height:480px}}
@container (max-width:640px){
  .flt{padding:14px 12px 12px}.frow{display:grid;gap:8px;margin-bottom:14px}.frow .lab{grid-column:1/-1;margin:0}.f1{grid-template-columns:repeat(4,1fr)}.f2{grid-template-columns:repeat(3,1fr)}.frow .ch{justify-content:center;padding:9px 4px;font-size:13.5px;border-radius:12px;min-height:42px;white-space:nowrap}.f1 .ch{border-radius:22px}.cnt{display:flex;flex-wrap:wrap;gap:10px 12px;padding-top:12px}.cnt #cnt{order:1}.cnt #rst{order:2;margin-left:auto}.cnt .go{order:3;flex:1 1 100%;justify-content:center;padding:12px 16px;font-size:15px}
  .mhint{display:inline-block;margin-left:10px;color:#2C6E49;font-weight:700;font-size:14.5px;vertical-align:middle}

  .ch{font-size:13.5px;padding:6px 12px}.flt{padding:14px 14px 12px}.frow{gap:7px;margin-bottom:14px}.tseo{font-size:14.5px}
  .sum{grid-template-columns:96px minmax(0,1fr);gap:12px;padding:12px}
  .thumb{aspect-ratio:1/1;align-self:start}
  .ttl h3{font-size:17px}.ttl small{font-size:12px;width:100%}
  .tg{gap:5px}.t{font-size:11.5px;padding:2px 8px}
  .kin{font-size:14.5px;line-height:1.7}.quick{font-size:13px;gap:3px 10px}
  .act{grid-column:1/-1}.dbtn{flex:1}
  .prow.open .det{grid-template-columns:1fr;gap:14px;padding:14px 12px 16px}
  .facts{gap:8px}.facts div{padding:9px 10px;font-size:13.5px}
  .btns{display:grid;grid-template-columns:1fr 1fr}.b3{grid-column:1/-1}.btn{white-space:normal;text-align:center}
  .lc,.rc{display:contents}.det .dhd{order:0}.det .dclose{order:99}.det .gal{order:1}.det .facts{order:2;margin-top:0}.det .s-car{order:3}.det .btns{order:4}.det .s-fac{order:5}.det .s-pet{order:6}.det .dsec{margin-top:0}
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
.pmenu{margin:0;font-size:13px;color:#7a6a45;line-height:1.6;flex:1}
.pft{display:flex;align-items:center;justify-content:space-between;gap:8px}.pp{font-size:18px;color:#C24E00}
.atc{background:#3F9D5A;color:#fff;text-decoration:none;font-weight:800;font-size:13px;border-radius:30px;padding:8px 12px;white-space:nowrap}
.pall{display:block;margin-top:14px;text-align:center;font-weight:800;color:#9A7B2E;text-decoration:none}
.swh{display:none}
@media(max-width:600px){#pmdl .mbox{padding:14px 0 16px}#pmdl .mt,#pmdl .psub,#pmdl .swh,#pmdl .pall{padding:0 14px}#pmdl .psub{margin-bottom:6px;font-size:13px}#pmdl .swh{display:block;margin:0 0 8px;font-size:12.5px;color:#9A7B2E;font-weight:700}#pmdl .pgrid{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;gap:12px;padding:0 14px 6px;scroll-padding:0 14px;scrollbar-width:none}#pmdl .pgrid::-webkit-scrollbar{display:none}#pmdl .pc{flex:0 0 74%;scroll-snap-align:start}#pmdl .pft{flex-direction:row;align-items:center}#pmdl .pall{display:block}}
@media(max-width:520px){.pgrid{grid-template-columns:1fr 1fr}.pft{flex-direction:column;align-items:stretch}.atc{text-align:center}}
.srcs{margin:18px 12px 0;padding-top:14px;border-top:1px solid #E7E0D2;font-size:13px;color:#7a6a45}
.srcs h2{margin:0 0 8px;font-size:15px;color:#1A1A1A}.srcs ul{margin:0;padding-left:18px;line-height:1.9}.srcs a{color:#9A7B2E;word-break:break-all}
'''
JS = '''
var LM=null,LY=null,LMK={};function fitAll(){if(!LM)return;LM.fitBounds(L.latLngBounds(PTS.map(function(p){return [p.lat,p.lng]})),{padding:[24,24]});}
(function(){if(!window.L)return;var m=document.getElementById('lmap');m.classList.add('on');document.getElementById('svgmap').style.display='none';var MOB=L.Browser.mobile;LM=L.map(m,{scrollWheelZoom:false,dragging:!MOB,tap:false,zoomSnap:1}).setView([22.36,114.13],10);var GB='https://mapapi.geodata.gov.hk/gs/api/v1.0.0/xyz/';L.tileLayer(GB+'basemap/WGS84/{z}/{x}/{y}.png',{maxZoom:19,minZoom:9,attribution:'<a href="https://api.portal.hkmapservice.gov.hk/disclaimer" target="_blank" rel="noopener">© 地政總署地圖</a>'}).addTo(LM);L.tileLayer(GB+'label/hk/tc/WGS84/{z}/{x}/{y}.png',{maxZoom:19,minZoom:9}).addTo(LM);LY=L.markerClusterGroup?L.markerClusterGroup({maxClusterRadius:38,disableClusteringAtZoom:13,showCoverageOnHover:false,spiderfyOnMaxZoom:true,iconCreateFunction:function(c){return L.divIcon({className:'',html:'<div class="lclu">'+c.getChildCount()+'</div>',iconSize:[36,36],iconAnchor:[18,18]})}}).addTo(LM):LM;PTS.forEach(function(p){var mk=L.marker([p.lat,p.lng],{icon:L.divIcon({className:'',html:'<div class="lpin" style="--c:'+p.c+'">'+p.ic+'</div>',iconSize:[28,28],iconAnchor:[14,14]})});mk.bindPopup('<div class="mpop">'+(p.img?'<img src="'+p.img+'" alt="" referrerpolicy="no-referrer" onerror="this.remove()">':'')+'<b>'+p.n+'</b><span class="mt">'+p.tg+'</span><button type="button" class="mpbtn" data-id="'+p.id+'">查看詳情 ↓</button></div>',{maxWidth:220,minWidth:200,autoPanPadding:[20,20]});if(!MOB)mk.bindTooltip(p.n);LY.addLayer(mk);LMK[p.id]=mk;});LM.on('popupopen',function(e){var b=e.popup.getElement().querySelector('.mpbtn');if(b)b.onclick=function(){openCard(b.dataset.id)}});})();
function openCard(id){var r=document.getElementById('b-'+id);if(!r)return;if(LM)LM.closePopup();if(!r.classList.contains('open')){var d=r.querySelector('.dbtn');if(d)d.click();}go('#b-'+id);}
function go(h){var t=document.querySelector(h);if(!t)return;t.scrollIntoView({behavior:'smooth',block:'start'});t.classList.add('hit');setTimeout(function(){t.classList.remove('hit')},1800);}
(function(){
var ph=document.getElementById('phone');
document.querySelectorAll('.vt button').forEach(function(b){b.onclick=function(){document.querySelectorAll('.vt button').forEach(function(x){x.classList.toggle('on',x===b)});ph.classList.toggle('d',b.dataset.v==='d');if(LM)setTimeout(function(){LM.invalidateSize()},300);}});
var TOTAL=document.querySelectorAll('.prow').length;
var st={r:'all',car:0,pet:0,cats:[]};var els=document.querySelectorAll('[data-id]');
function ok(e){if(st.r!=='all'&&e.dataset.r!==st.r)return false;if(st.car&&e.dataset.car!=='1')return false;if(st.pet&&e.dataset.pet!=='Y')return false;var c=e.dataset.cats.split(' ');return st.cats.every(function(x){return c.indexOf(x)>-1})}
function apply(){var n=0;els.forEach(function(e){var o=ok(e);e.classList.toggle('off',!o);if(o&&e.classList.contains('prow'))n++;});
document.getElementById('cnt').textContent=(n===TOTAL?'全部 ':'符合：')+n+' 個地點';var fs=document.querySelector('.fsum');if(fs)fs.textContent=(n===TOTAL?'全部 ':'符合：')+n+' 個地點';var k=(st.r!=='all'?1:0)+(st.car?1:0)+(st.pet?1:0)+st.cats.length,bd=document.querySelector('.fbd');if(bd){bd.hidden=!k;bd.textContent=k;}document.getElementById('empty').style.display=n?'none':'block';
if(LM){var vis=[];document.querySelectorAll('.prow').forEach(function(e){var mk=LMK[e.dataset.id];if(!mk)return;if(e.classList.contains('off')){LY.removeLayer(mk)}else{if(!LY.hasLayer(mk))LY.addLayer(mk);vis.push(mk.getLatLng())}});if(vis.length&&vis.length<PTS.length)LM.fitBounds(L.latLngBounds(vis).pad(0.3),{maxZoom:14});else fitAll();}
document.querySelectorAll('.pk-region').forEach(function(g){g.style.display=g.querySelector('.prow:not(.off)')?'':'none'});var pins=document.querySelectorAll('.pin:not(.off)');pins.forEach(function(p){p.classList.toggle('lbl',pins.length<=6)});}
document.querySelectorAll('.ch').forEach(function(b){b.onclick=function(){var f=b.dataset.f,v=b.dataset.v;
if(f==='r'){st.r=v;document.querySelectorAll('.ch[data-f=r]').forEach(function(x){x.classList.toggle('on',x===b)})}
else if(f==='car'){st.car=!st.car;b.classList.toggle('on')}else if(f==='pet'){st.pet=!st.pet;b.classList.toggle('on')}
else{var i=st.cats.indexOf(v);if(i>-1)st.cats.splice(i,1);else st.cats.push(v);b.classList.toggle('on')}pend(true);}});
function pend(x){var g=document.getElementById('go');g.classList.toggle('pd',x);if(x)document.getElementById('cnt').textContent='已更改條件，請按「確定搜尋」';}
var FL=document.querySelector('.flt'),FH=FL.parentNode,FN=FL.nextSibling,FB=document.querySelector('.fbar'),BG=document.createElement('div');BG.className='fbg';
function CT(){return document.querySelector('.pk-cmb')||document.getElementById('phone')}
function mode(){var c=CT(),m=false;/* 2026-10-18：手機版改回直接顯示篩選框（底部彈出面板停用，改 m 條件即可恢復） */if(c)c.classList.toggle('msheet',m);if(!m)closeS();}
function openS(){var h=document.querySelector('.ao-picnic')||document.body;h.appendChild(BG);h.appendChild(FL);FL.classList.add('sheet');document.body.style.overflow='hidden';requestAnimationFrame(function(){requestAnimationFrame(function(){BG.classList.add('on');FL.classList.add('on')})})}
function closeS(){if(!FL.classList.contains('sheet'))return;FL.classList.remove('on','sheet');BG.classList.remove('on');FH.insertBefore(FL,FN);if(BG.parentNode)BG.parentNode.removeChild(BG);document.body.style.overflow=''}
FB.querySelector('.fbtn').onclick=openS;BG.onclick=closeS;FL.querySelector('.sx').onclick=closeS;window.addEventListener('resize',mode);mode();
document.querySelectorAll('.vt button').forEach(function(b){b.addEventListener('click',function(){setTimeout(mode,320)})});
document.getElementById('go').onclick=function(){closeS();apply();pend(false);var t=document.getElementById('hk-map');if(t)t.scrollIntoView({behavior:'smooth',block:'start'});};
document.getElementById('rst').onclick=function(){st={r:'all',car:0,pet:0,cats:[]};document.querySelectorAll('.ch').forEach(function(x){x.classList.toggle('on',x.dataset.v==='all')});apply();pend(false);};
document.querySelectorAll('a[href^="#b-"]').forEach(function(a){a.onclick=function(ev){ev.preventDefault();go(a.getAttribute('href'));}});
document.querySelectorAll('.tclose').forEach(function(b){b.onclick=function(){var dt=b.closest('details');dt.open=false;var t=document.getElementById('hk-table');if(t)t.scrollIntoView({behavior:'smooth',block:'start'})}});
document.querySelectorAll('.prow').forEach(function(r){
  var d=r.querySelector('.dbtn'),lb=d.querySelector('.lb');d.onclick=function(){var o=r.classList.toggle('open');d.setAttribute('aria-expanded',o);lb.textContent=o?'收起':'詳情';};var dc=r.querySelector('.dclose');if(dc)dc.onclick=function(){d.click();r.scrollIntoView({behavior:'smooth',block:'start'})};
  var tr=r.querySelector('.tr');if(!tr)return;var ds=r.querySelectorAll('.dots i');
  tr.addEventListener('scroll',function(){var i=Math.round(tr.scrollLeft/tr.clientWidth);ds.forEach(function(x,k){x.classList.toggle('on',k===i)})});
  var p=r.querySelector('.nav.p'),n=r.querySelector('.nav.n');if(p)p.onclick=function(){tr.scrollBy({left:-tr.clientWidth,behavior:'smooth'})};if(n)n.onclick=function(){tr.scrollBy({left:tr.clientWidth,behavior:'smooth'})};
});
var md=document.getElementById('mdl'),mi=md.querySelector('img'),mt=md.querySelector('.mt');
document.querySelectorAll('[data-img]').forEach(function(b){b.onclick=function(){mi.src=b.dataset.img;mi.alt=b.dataset.t;mt.textContent=b.dataset.t;md.querySelector('.msrc').textContent=b.dataset.s?'圖片來源︰'+b.dataset.s:'';md.hidden=false;}});
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
TBL_SEO = (f'想找香港野餐好去處？下表整理了全港 {N} 個野餐地點：新界有大埔海濱公園及清水灣大坑墩等大草地，九龍有西九文化區等海濱草地，港島則有添馬公園。展開下表，即可按泊車、寵物及類別逐一比較。')
FILTER = f"""<div class="fbar"><button class="fbtn" type="button">⚙️ 篩選 <span class="fbd" hidden></span></button><span class="fsum"></span></div>
<div class="flt"><div class="shd"><i class="grab"></i><b>篩選野餐地點</b><button class="sx" type="button" aria-label="關閉">✕</button></div>
<p class="fhd">✨ 三步找到心水野餐地點</p>
<div class="frow f1"><span class="lab"><i class="no">1</i>揀選地區</span>{chips_r}</div>
<div class="frow f2"><span class="lab"><i class="no">2</i>揀選條件及類別（可多選）</span><button class="ch" data-f="car" data-v="1">🚗 可泊車</button><button class="ch" data-f="pet" data-v="Y">🐶 寵物友善</button>{chips_c}</div>
<div class="cnt"><button class="go" id="go" type="button"><i class="no">3</i>🔍 確定搜尋</button><span id="cnt"></span><button id="rst">重設</button></div></div>"""
def MAP(hx='h2'):
    return f"""<div class="sec" id="hk-map"><{hx} class="sh">📍 地圖<span class="mhint">🤏 用兩隻手指移動及縮放地圖</span></{hx}><div id="lmap"></div><div class="map" id="svgmap"><svg viewBox="0 0 {W} {Hh}" preserveAspectRatio="none">{land}</svg>{pins}<span class="note">示意地圖，並非真實比例</span></div>
</div>"""
def TABLE(hx='h2', hcls='sh'):
    return f"""<div class="sec" id="hk-table"><{hx} class="{hcls}">📊 全港野餐地點一覽比較表</{hx}><p class="tseo">{TBL_SEO}</p>
<details class="cmp"><summary><span class="o">📊 展開比較表（{N} 個地點）</span><span class="c">📊 收起比較表</span><b class="ar">▾</b></summary><div class="tw"><table><thead>{thead}</thead><tbody>{trs}</tbody></table></div><button class="tclose" type="button">收起比較表 ▲</button></details></div>"""
POPUPS = f"""<div class="mdl" id="pmdl" hidden><div class="mbox"><button class="mx" type="button" aria-label="關閉">✕</button><p class="mt">🧺 Kitchen AO 野餐盒｜送到附近可停車位置</p><p class="psub">選擇人數及套餐，按「揀選心水餐單」後於網站揀選菜式並完成訂購。滿 $1,450 全港免運費；滿 $700 九龍指定區域免運費，港島及新界區運費半價，於地面可停車位置車邊交收。</p><p class="swh">← 左右滑動查看 5 款套餐 →</p><div class="pgrid">{pcards}</div><a class="pall" href="https://aoaodelivery.com/product-category/party/chill-box/{UTM}" target="_blank" rel="noopener">瀏覽全部野餐盒 →</a></div></div>
<div class="mdl" id="mdl" hidden><div class="mbox"><button class="mx" type="button" aria-label="關閉">✕</button><p class="mt"></p><img alt=""><p class="msrc"></p></div></div>"""
SRCS = f'<section class="srcs"><h2>資料來源</h2><ul>{srcs_h}</ul></section>'
LEAF_CSS = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.css"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet.markercluster/1.5.3/MarkerCluster.min.css">'
SCRIPTS = '<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.js"></script><script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet.markercluster/1.5.3/leaflet.markercluster.min.js"></script><script>var PTS=' + json.dumps([dict(id=p["id"],n=p["name"],lat=GEO[p["id"]][0],lng=GEO[p["id"]][1],c=RC[p["r"]],ic=IC(p),img=(off(p).get("thumb") or ((off(p).get("img") or [""])[0])),tg="　".join([CATS[c][0]+" "+CATS[c][1] for c in p["cats"]]+(["🐶 寵物友善"] if p["pet"]=="Y" else (["🐾 寵物指定範圍"] if p["pet"]=="P" else []))+(["🅿️ 可泊車"] if p["car"] else []))) for p in P],ensure_ascii=False) + ';</script><script>' + JS + '</script>'
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
<div class="sec"><h2>📝 港島、九龍、新界野餐地點介紹</h2><p class="empty" id="empty">沒有符合條件的地點，請嘗試減少篩選條件。</p>{items}</div>
{SRCS}
{POPUPS}
</div>{SCRIPTS}</body></html>'''
if __name__ == '__main__':
    open(os.path.join(HERE, 'combo-mobile.html'), 'w').write(html); print(len(html), N)
