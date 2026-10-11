# Kitchen AO — Blog 1 野餐地點推介（Demo）
# python3 build.py  → preview.html（有 KW/PAA 黃色 highlight）＋ blog-picnic-WORDPRESS.html（無 highlight）
import json, re, html as H
from urllib.parse import quote
UTM = 'ao_ref=picnic_blog1'
CHILL = 'https://aoaodelivery.com/product-category/party/chill-box/?' + UTM
BIG = 'https://aoaodelivery.com/product/chill%e4%b8%80picnic-big-for-4-6-persons/?' + UTM
SMALL = 'https://aoaodelivery.com/product/chill%e4%b8%80picnic-small/?' + UTM
PLATTER = 'https://aoaodelivery.com/product/5-people-self-selected-platter/?' + UTM
WA = 'https://api.whatsapp.com/send?phone=85269011987&text=' + quote('你好，我想查詢 Chill一下野餐盒')
IMG_CHILL = 'https://aoaodelivery.com/wp-content/uploads/2025/04/WhatsApp-Image-2025-04-12-at-4.08.18-PM-600x400.jpeg'
IMG_PLATTER = 'https://aoaodelivery.com/wp-content/uploads/2023/10/KitchenAO_platter_thumbnail_%E5%B7%A5%E4%BD%9C%E5%8D%80%E5%9F%9F-1-600x600-1.png'
VAC = 'https://resource.data.one.gov.hk/td/carpark/'

# ---------- 分類 icon（之後可在 Excel 補資料）----------
CATS = {
 'sea':    ('🌊', '海景'),
 'lawn':   ('🌳', '大草地'),
 'hidden': ('🌿', '秘境'),
 'sky':    ('🏙️', '空中花園'),
 'shade':  ('⛱️', '有遮陰／雨天備案'),
 'euro':   ('🏛️', '特色園林'),
 'beach':  ('🏖️', '沙灘'),
}
REGIONS = [('hk', '港島', '港島野餐'), ('kln', '九龍', '九龍野餐'), ('nt', '新界', '新界野餐地點'), ('is', '離島', '離島野餐')]

# pet: Y / N / P(指定範圍)；car: [(停車場名, vacancy json 檔名 or None)]；kw = 呢個地點嘅目標 keyword
P = [
 # ---- 港島 ----
 dict(id='tamar', r='hk', name='添馬公園', en='Tamar Park', cats=['sea','lawn'], pet='N', kw='添馬公園野餐',
      car=[('金鐘道政府合署停車場','vacancy_tdc95p1.json')],
      intro='中環海旁標誌性大草坪，正對維港海景，設施完善，係市區<mark class="kw">中環野餐</mark>首選。',
      tr='金鐘站 A／E2 出口步行約 5–10 分鐘', petnote='主草坪唔可以帶狗野餐，旁邊海濱寵物空間另計。'),
 dict(id='sysmp', r='hk', name='中山紀念公園', en='Sun Yat Sen Memorial Park', cats=['lawn','shade'], pet='N', kw='中山紀念公園野餐',
      car=[('中山紀念公園停車場','vacancy_tdc114p1.json')],
      intro='西營盤海濱圓形大草坪，四周有蓋迴廊同樹蔭多，遮陰效果好。', tr='西營盤站 A2 出口步行約 5 分鐘',
      petnote='圓形野餐草坪唔屬准許寵物範圍。'),
 dict(id='cyber', r='hk', name='數碼港海濱公園', en='Cyberport Waterfront Park', cats=['sea','lawn'], pet='Y', kw='數碼港野餐',
      car=[('數碼港停車場（一＆二）','vacancy_tdc113p1.json'),('數碼港停車場（三）','vacancy_tdc113p2.json')],
      intro='港島南區臨海大草坪，視野開揚，有度假感。', tr='巴士 30X／970 到數碼港',
      petnote='草地可與寵物野餐，但唔屬康文署寵物共享公園名單。'),
 dict(id='vpark', r='hk', name='維多利亞公園', en='Victoria Park', cats=['lawn'], pet='P', kw='維園野餐',
      car=[('皇室堡停車場',None),('柏景臺停車場',None)],
      intro='銅鑼灣市中心大草坪，交通最方便。', tr='天后站 B 出口／銅鑼灣站 E 出口',
      petnote='寵物只可留喺指定位置，中央草坪野餐區不包括在內。'),
 dict(id='peak', r='hk', name='山頂公園', en='Victoria Peak Garden', cats=['hidden','euro'], pet='Y', kw='山頂野餐',
      car=[('山頂廣場停車場','vacancy_tdc21p1.json'),('山頂公園露天停車場',None)],
      intro='前港督別墅花園，保留古典涼亭同石階，英式莊園風格，人流相對少。', tr='山頂纜車或巴士到山頂，再步行約 15 分鐘',
      petnote='寵物共享場地，有可供野餐嘅草地。'),
 dict(id='hkpark', r='hk', name='香港公園', en='Hong Kong Park', cats=['shade'], pet='N', kw='港島野餐',
      car=[('太古廣場停車場',None),('花園道停車場',None)],
      intro='金鐘市區綠洲，樹蔭多，以石櫈、涼亭輕食為主。', tr='金鐘站 C1 出口經太古廣場', petnote='不設寵物野餐。'),
 dict(id='mtdavis', r='hk', name='摩星嶺配水庫臨時花園', en='Mount Davis Garden', cats=['hidden','sea'], pet='N', kw='港島野餐',
      car=[('堅尼地城停車場（再轉車或步行上山）','vacancy_tdcp7.json')],
      intro='半山隱世綠洲，人流少，遠眺南區海景。', tr='堅尼地城站轉乘小巴 54', petnote='未列寵物共享。'),
 # ---- 九龍 ----
 dict(id='wkcd', r='kln', name='西九藝術公園', en='Art Park, West Kowloon', cats=['lawn','sea'], pet='Y', kw='西九野餐',
      car=[('藝術公園停車場','vacancy_tdc17p2.json')],
      intro='維港海旁大草坪，海景同草地兼備，車位多，適合<mark class="kw">揸車野餐</mark>。', tr='九龍站／柯士甸站 E 出口步行',
      petnote='准許牽繩、受管束嘅寵物進入，可以喺草坪一齊野餐。'),
 dict(id='ktap', r='kln', name='啟德大道公園', en='Kai Tak Avenue Park', cats=['lawn'], pet='Y', kw='啟德野餐',
      car=[('AIRSIDE 停車場','vacancy_tdc121p1.json')],
      intro='啟德新發展區大型公園，草地寬敞，鄰近 AIRSIDE。', tr='啟德站出口即達', petnote='有大草坪，可攜寵物前往。'),
 dict(id='ktct', r='kln', name='啟德郵輪碼頭公園', en='Kai Tak Cruise Terminal Park', cats=['sky','sea','shade'], pet='Y', kw='郵輪碼頭野餐',
      car=[('郵輪碼頭停車場 1 號','vacancy_tdc347p1.json')],
      intro='全港最大空中花園之一，天台中央草坪，有上蓋位置，係雨天或暴曬天嘅後備選擇。', tr='小巴 86 到郵輪碼頭',
      petnote='天台公園現准攜寵物進入。'),
 dict(id='shingfung', r='kln', name='承豐道公園', en='Shing Fung Road Park', cats=['lawn','sea'], pet='Y', kw='啟德野餐',
      car=[('體藝館停車場',None),('啟德體育園停車場',None)],
      intro='啟德海濱寵物共享公園，設野餐草坪。', tr='啟德站步行', petnote='康文署寵物共享公園。'),
 dict(id='jvp', r='kln', name='佐敦谷公園', en='Jordan Valley Park', cats=['lawn'], pet='N', kw='佐敦谷野餐',
      car=[('佐敦谷公園停車場','vacancy_tdc357p1.json')],
      intro='九龍東中央低窪大草坪，環境舒適。', tr='彩虹站轉乘巴士', petnote='唔屬寵物共享公園。'),
 dict(id='ktprom', r='kln', name='觀塘海濱花園', en='Kwun Tong Promenade', cats=['sea'], pet='P', kw='觀塘海濱野餐',
      car=[('海濱匯停車場','vacancy_tdc14p8888.json')],
      intro='東九龍沿海草地長廊，遠眺維港同鯉魚門。', tr='牛頭角站 B6 出口步行約 10 分鐘', petnote='只限指定寵物共享區草地。'),
 dict(id='ckl', r='kln', name='茶果嶺海濱公園', en='Cha Kwo Ling Promenade', cats=['sea'], pet='P', kw='九龍野餐好去處',
      car=[('麗港城停車場',None)],
      intro='油塘、茶果嶺一帶新海濱，海景開揚。', tr='油塘站步行', petnote='只限海濱指定寵物共享範圍。'),
 dict(id='klnpark', r='kln', name='九龍公園', en='Kowloon Park', cats=['shade'], pet='N', kw='九龍公園野餐',
      car=[('九龍公園停車場','vacancy_tdc51p1.json')],
      intro='尖沙咀鬧市綠洲，以樹蔭、涼亭同石桌輕食為主，欠缺大草地。', tr='尖沙咀站 A1 出口', petnote='不設寵物野餐。'),
 dict(id='namcheong', r='kln', name='南昌公園', en='Nam Cheong Park', cats=['lawn'], pet='N', kw='南昌公園野餐',
      car=[('南昌停車場','vacancy_tdc14p5421.json'),('南昌薈停車場','vacancy_tdc14p5419.json')],
      intro='深水埗大型草坪，鄰近港鐵站。', tr='南昌站 A 出口', petnote='唔屬寵物共享公園。'),
 dict(id='lokfu', r='kln', name='樂富配水庫休憩花園', en='Lok Fu Service Reservoir Rest Garden', cats=['hidden','lawn'], pet='N', kw='樂富配水庫野餐',
      car=[('樂富邨停車場','vacancy_tdc14p4352.json')],
      intro='配水庫上蓋隱世大草地，人流少，適合打卡。', tr='樂富站步行', petnote='配水庫大草地暫未全面開放予寵物。'),
 # ---- 新界 ----
 dict(id='penfold', r='nt', name='彭福公園', en='Penfold Park', cats=['lawn'], pet='Y', kw='彭福公園野餐',
      car=[('彭福公園停車場',None)],
      intro='沙田馬場中央大草原，草質厚，係<mark class="kw">沙田野餐</mark>熱點。', tr='火炭站步行約 10 分鐘',
      petnote='少有准許狗狗喺指定範圍無繩奔跑；賽馬日暫停開放。'),
 dict(id='tpwp', r='nt', name='大埔海濱公園', en='Tai Po Waterfront Park', cats=['lawn','sea'], pet='N', kw='大埔海濱公園野餐',
      car=[('廣福停車場（大埔大華街）','vacancy_tdstt118.json')],
      intro='全港最大康文署公園之一，海景大草坪，可以放風箏。', tr='大埔墟站轉乘巴士', petnote='大草坪一般禁止寵物進入。'),
 dict(id='velo', r='nt', name='香港單車館公園', en='Velodrome Park', cats=['lawn'], pet='P', kw='將軍澳野餐',
      car=[('香港單車館停車場','vacancy_tdc374p1.json')],
      intro='將軍澳中央草坪，24 小時開放，有人工湖同遊樂場。', tr='坑口站 B 出口步行約 9 分鐘', petnote='只限指定位置。'),
 dict(id='mospark', r='nt', name='馬鞍山公園', en='Ma On Shan Park', cats=['lawn'], pet='N', kw='馬鞍山公園野餐',
      car=[('馬鞍山游泳池停車場','vacancy_tdc63p2.json')],
      intro='馬鞍山市中心公園，鄰近海濱長廊。', tr='馬鞍山站步行', petnote='不設寵物野餐。'),
 dict(id='saisha', r='nt', name='馬鞍山西沙路花園', en='Sai Sha Road Garden', cats=['sea'], pet='Y', kw='馬鞍山野餐',
      car=[('迎海停車場',None),('馬鞍山游泳池停車場','vacancy_tdc63p2.json')],
      intro='寵物共享公園，場地較細，適合帶狗散步加輕食。', tr='烏溪沙站步行', petnote='寵物共享公園，但未必有大草地。'),
 dict(id='ngongping', r='nt', name='馬鞍山昂坪高原', en='Ngong Ping Plateau, Ma On Shan', cats=['hidden','lawn','sea'], pet='Y', kw='昂坪野餐',
      car=[], carnote='無直達停車場，需由馬鞍山村或大水坑步行上山',
      intro='郊野高原大草地，遠眺西貢海，屬行山加野餐路線。', tr='由馬鞍山村步行上山', petnote='郊野公園範圍，可與寵物野餐。'),
 dict(id='taitamtun', r='nt', name='清水灣大坑墩草地', en='Tai Hom Tun, Clear Water Bay', cats=['lawn','sea'], pet='Y', kw='西貢野餐',
      car=[('大坑墩停車場',None)],
      intro='郊野公園山坡草地，海景開揚，適合放風箏。', tr='巴士到清水灣郊野公園', petnote='可攜犬前往，非康文署名單場地。'),
 dict(id='tapmun', r='nt', name='塔門', en='Tap Mun', cats=['hidden','sea','lawn'], pet='Y', kw='塔門野餐',
      car=[('黃石碼頭停車場（泊車後轉乘街渡）',None)],
      intro='離島高原草地，360 度海景，完全無遮擋，記得做足防曬。', tr='黃石碼頭或馬料水乘街渡', petnote='戶外草地，可與寵物野餐。'),
 dict(id='yuentun', r='nt', name='圓墩村草地', en='Yuen Tun Lawn', cats=['lawn','hidden'], pet='Y', kw='荃灣野餐',
      car=[('大欖郊野公園停車場',None)],
      intro='荃灣郊野草地，環境清幽。', tr='荃灣乘小巴往大欖', petnote='郊野公園範圍，可與寵物野餐。'),
 dict(id='tyipark', r='nt', name='青衣公園', en='Tsing Yi Park', cats=['euro'], pet='N', kw='青衣公園野餐',
      car=[('青衣運動場及游泳池停車場','vacancy_tdc81p5.json'),('港鐵青衣站停車場',None),('港鐵青衣城停車場',None)],
      intro='歐陸風人工湖，秋冬有落羽松轉紅。', tr='青衣站 C 出口步行約 3 分鐘', petnote='唔屬寵物共享公園。'),
 dict(id='tyiwf', r='nt', name='青衣海濱公園', en='Tsing Yi Promenade', cats=['sea'], pet='Y', kw='青衣野餐',
      car=[('青衣運動場及游泳池停車場','vacancy_tdc81p5.json'),('港鐵青衣站停車場',None),('港鐵青衣城停車場',None)],
      intro='青衣沿海長廊，可帶狗散步。', tr='青衣站步行', petnote='可與狗狗野餐嘅空間有限。'),
 dict(id='howo', r='nt', name='屯門浩和街', en='Ho Wo Street, Tuen Mun', cats=['sea'], pet='Y', kw='浩和街野餐',
      car=[('浩和街露天停車場／路邊咪錶',None)],
      intro='「港版邁阿密」海堤同棕櫚樹，視野開揚，可睇飛機。', tr='屯門站轉乘巴士 K52', petnote='戶外草地，可與寵物野餐。'),
 dict(id='tmpark', r='nt', name='屯門公園', en='Tuen Mun Park', cats=['lawn'], pet='N', kw='屯門公園野餐',
      car=[('屯門市廣場第二期停車場','vacancy_tdc25p43.json')],
      intro='屯門市中心大型公園。', tr='屯門站步行', petnote='不設寵物野餐。'),
 dict(id='namsang', r='nt', name='南生圍', en='Nam Sang Wai', cats=['hidden'], pet='Y', kw='南生圍野餐',
      car=[], carnote='附近空地，無正規停車場',
      intro='元朗濕地秘境，蘆葦同魚塘景色，日落特別靚。', tr='元朗乘小巴到南生圍', petnote='戶外空間，可與寵物野餐。'),
 dict(id='tswpark', r='nt', name='天水圍公園', en='Tin Shui Wai Park', cats=['lawn'], pet='N', kw='天水圍野餐',
      car=[('天水圍運動場停車場','vacancy_tdc359p1.json')],
      intro='天水圍社區大型公園。', tr='天水圍站步行', petnote='寵物只限指定位置，主要草地不包括在內。'),
 dict(id='ylpark', r='nt', name='元朗公園', en='Yuen Long Park', cats=['lawn','euro'], pet='N', kw='元朗公園野餐',
      car=[('元朗游泳池停車場','vacancy_tdc326p1.json')],
      intro='元朗市區公園，有觀鳥塔同草地。', tr='元朗站步行', petnote='不設寵物野餐。'),
 # ---- 離島 ----
 dict(id='inspire', r='is', name='迪欣湖', en='Inspiration Lake', cats=['lawn','euro'], pet='N', kw='迪欣湖野餐',
      car=[('迪欣湖活動中心停車場',None)],
      intro='全港最大人工湖之一，湖畔草地配歐陸風建築，可踩水上單車。', tr='欣澳站轉乘巴士 R8', petnote='未確認可帶寵物喺湖畔草地野餐。'),
 dict(id='db', r='is', name='愉景灣（大白灣／中央公園）', en='Discovery Bay', cats=['beach','sea','lawn'], pet='Y', kw='愉景灣野餐',
      car=[('欣澳露天停車場（愉景灣區內不准私家車駛入，需轉車）',None)],
      intro='沙灘加草地，度假氣氛重。', tr='中環 3 號碼頭乘船或欣澳轉巴士', petnote='區內草地及沙灘一般容許與寵物野餐。'),
]

def tags(p):
    t = []
    if p['car']: t.append('<span class="pk-tag t-car">🚗 可泊車</span>')
    if p['pet'] == 'Y': t.append('<span class="pk-tag t-pet">🐶 寵物友善</span>')
    elif p['pet'] == 'P': t.append('<span class="pk-tag t-pet2">🐾 寵物指定範圍</span>')
    for c in p['cats']: t.append(f'<span class="pk-tag t-cat">{CATS[c][0]} {CATS[c][1]}</span>')
    return ''.join(t)

def card(i, p):
    if p['car']:
        lis = ''.join(f'<li><span class="nm">🅿️ {H.escape(n)}</span>' + (f'<button type="button" class="pk-vac" data-src="{VAC}{f}">查實時車位</button><span class="pk-vres"></span>' if f else '') + '</li>' for n, f in p['car'])
        carhtml = f'<div class="pk-car"><p class="lbl">鄰近停車場</p><ul>{lis}</ul></div>'
    else:
        carhtml = f'<div class="pk-car pk-car--none"><p class="lbl">鄰近停車場</p><p>⚠️ {p.get("carnote","暫無停車場資料")}</p></div>'
    data = f'data-r="{p["r"]}" data-car="{1 if p["car"] else 0}" data-pet="{p["pet"]}" data-cats="{" ".join(p["cats"])}"'
    return f'''<article class="pk-card" id="pk-{p['id']}" {data}>
  <div class="pk-ph"><span>📷 相片待補</span></div>
  <div class="pk-body">
    <h3 class="pk-h3">{p['name']} <small>{p['en']}</small></h3>
    <div class="pk-tags">{tags(p)}</div>
    <p class="pk-kw">目標關鍵字：<mark class="kw">{p['kw']}</mark></p>
    <p class="pk-intro">{p['intro']}</p>
    <p class="pk-tr"><b>🚇 交通：</b>{p['tr']}</p>
    <p class="pk-pet"><b>🐶 寵物：</b>{p['petnote']}</p>
    {carhtml}
  </div>
</article>'''

regions = ''
n = 0
for rid, rname, rkw in REGIONS:
    ps = [p for p in P if p['r'] == rid]
    cards = ''
    for p in ps:
        n += 1; cards += card(n, p)
    regions += f'''<section class="pk-region" data-region="{rid}">
  <h2 class="ao-h2" id="r-{rid}">📍 {rname}野餐地點推介（{len(ps)} 個）</h2>
  <p class="ao-aio">【AIO 直接解答｜待寫 50–80 字】<mark class="kw">{rkw}</mark>可以去邊？以下 {len(ps)} 個地點已按可泊車、寵物友善同地點類別標示。</p>
  <div class="pk-grid">{cards}</div>
</section>'''

chips_r = ''.join(f'<button type="button" class="pk-chip" data-f="r" data-v="{rid}">{rn}</button>' for rid, rn, _ in REGIONS)
chips_c = ''.join(f'<button type="button" class="pk-chip" data-f="cat" data-v="{k}">{v[0]} {v[1]}</button>' for k, v in CATS.items())
legend = ''.join(f'<span>{v[0]} {v[1]}</span>' for v in CATS.values())

CSS = open('style.css').read()
JS = open('tool.js').read()
FAQ = [
 ('野餐幾點去到搵位最合適？', '建議上午 11:30 前或下午 3:30 後到達：早到可以霸樹蔭位，下晝去避開正午暴曬，仲可以睇日落。'),
 ('香港公園可以野餐嗎？', '大部分康文署公園嘅草地都可以野餐，但部分草坪會輪流開放或維修，出發前建議查閱康文署網頁。'),
 ('可以帶狗去野餐嗎？', '可以，但要揀寵物共享公園或准許寵物嘅草地，並以狗帶牽引。本文每個地點都有「🐶 寵物友善」標示。'),
 ('哪個野餐地點有停車場？', '用上面搜尋器揀「🚗 可泊車」，每個地點底部都列出鄰近停車場，部分可以即時查實時車位。'),
 ('下雨天可以去哪裡野餐？', '可以考慮有上蓋嘅空中花園，例如啟德郵輪碼頭公園，或樹蔭較多嘅中山紀念公園、九龍公園。'),
 ('野餐食物哪裡買？', '唔想自己準備，可以預訂 Kitchen AO「Chill一下野餐盒」，乾爽一口食，直送到公園入口交收。'),
]
faq_html = ''.join(f'<details class="ao-faq"><summary><mark class="paa">{q}</mark></summary><div class="a">{a}</div></details>' for q, a in FAQ)
faq_ld = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}, ensure_ascii=False)

BODY = f'''<div class="ao-article ao-picnic">
<style>
{CSS}
</style>

<div class="pk-kv"><div><p class="pk-kv-pill">香港野餐好去處 2026</p><p class="pk-kv-t">全港野餐地點<br>搜尋器</p><p class="pk-kv-s">{n} 個大草地／海景／隱世公園・可泊車・寵物友善</p></div><span class="pk-kv-note">KV 待製作（1600 × 900）</span></div>

<div class="ao-introcard">
<p class="ao-q">🧺 想搵<mark class="kw">香港野餐好去處</mark>？</p>
<p class="ao-intro">香港地方細，但都有唔少靚景<mark class="kw">野餐好去處</mark>：無敵海景、大片真草地、<mark class="kw">隱世野餐地點</mark>同空中花園應有盡有，仲可以同狗狗一齊野餐。Kitchen AO 整合咗全港 {n} 個<mark class="kw">香港野餐地點</mark>，按地區分類，再用「可泊車」「寵物友善」同地點類別三個條件篩選，每個地點都列出鄰近停車場，方便你<mark class="kw">揸車野餐</mark>。</p>
</div>

<div class="ao-tagsec"><span class="lbl">此文章相關 Tag</span><div class="ao-tags"><span>野餐好去處</span><span>香港野餐</span><span>狗狗野餐</span><span>野餐泊車</span><span>野餐盒</span></div></div>

<nav class="ao-toc"><div class="t">目錄</div><ul>
<li><a href="#pk-tool">全港野餐地點搜尋器</a></li>
{''.join(f'<li><a href="#r-{rid}">{rn}野餐地點推介</a></li>' for rid, rn, _ in REGIONS)}
<li><a href="#dog">帶狗狗野餐須知</a></li>
<li><a href="#food">野餐食物帶咩好？</a></li>
<li><a href="#faq">野餐常見問題</a></li>
<li><a href="#chill">Kitchen AO 野餐盒推介</a></li>
</ul></nav>

<h2 class="ao-h2" id="pk-tool">🔍 全港野餐地點搜尋器</h2>
<p class="ao-aio">【AIO 直接解答｜待寫 50–80 字】揀地區，再用 3 個條件篩選：<mark class="kw">野餐泊車</mark>、<mark class="kw">狗狗野餐好去處</mark>，同埋海景、<mark class="kw">大草地野餐</mark>、秘境等地點類別。</p>
<div class="pk-tool" id="pkTool">
  <div class="pk-row"><span class="pk-lab">① 地區</span><button type="button" class="pk-chip on" data-f="r" data-v="all">全部</button>{chips_r}</div>
  <div class="pk-row"><span class="pk-lab">② 條件</span><button type="button" class="pk-chip" data-f="car" data-v="1">🚗 可泊車</button><button type="button" class="pk-chip" data-f="pet" data-v="Y">🐶 寵物友善</button></div>
  <div class="pk-row"><span class="pk-lab">③ 類別</span>{chips_c}</div>
  <div class="pk-foot"><span id="pkCount">顯示全部 {n} 個地點</span><button type="button" class="pk-reset" id="pkReset">重設</button></div>
  <div class="pk-legend">{legend}<span>🚗 可泊車</span><span>🐶 寵物友善</span><span>🐾 寵物指定範圍</span></div>
</div>
<p class="pk-empty" id="pkEmpty" hidden>冇符合條件嘅地點，試吓減少篩選條件。</p>

{regions}

<h2 class="ao-h2" id="dog">🐶 帶狗狗野餐須知</h2>
<p class="ao-aio">【AIO 直接解答｜待寫】<mark class="kw">狗狗野餐</mark>前，記得揀准許寵物嘅草地，並遵守以下守則：</p>
<div class="ao-why"><ul>
<li><b>全程用狗帶：</b>根據漁護署及康文署守則，絕大部分公眾地方及寵物共享公園，狗隻必須以狗帶（2 米內為佳）牽引。</li>
<li><b>唔好離開視線：</b>留意狗狗動向，同其他狗狗互動時要看管。</li>
<li><b>自備糧水：</b>帶足食水同狗糧，炎熱天氣注意中暑。</li>
<li><b>清理排泄物：</b>帶備狗袋，保持草地清潔。</li>
</ul></div>

<h2 class="ao-h2" id="food">🥪 戶外<mark class="kw">野餐食物</mark>帶咩好？物資清單與保存須知</h2>
<p class="ao-aio">【AIO 直接解答｜待寫】<mark class="kw">野餐小食</mark>最好揀一口份量、乾爽唔漏汁；海鮮、沙律要用保冷袋，2 小時內食完。</p>
<div class="pk-check"><p><b>🧺 野餐用品清單</b></p><ul><li><mark class="kw">野餐墊</mark>（防水底）</li><li>保冷袋＋冰種</li><li>濕紙巾、垃圾袋</li><li>防曬、驅蚊用品</li><li>寵物糧水（如帶狗）</li></ul></div>

<h2 class="ao-h2" id="faq">❓ 野餐常見問題 FAQ</h2>
{faq_html}

<!-- ===== 產品（最後先介紹）===== -->
<h2 class="ao-h2" id="chill">🍱 懶人之選：Kitchen AO <mark class="kw">野餐盒</mark>推介</h2>
<p class="ao-aio">唔想花 4 個鐘備料再搬去公園？Chill一下野餐盒乾爽一口食、免餐具，送到公園入口交收，<mark class="kw">野餐食物哪裡買</mark>一次解決。</p>
<div class="pk-prod">
  <a class="pk-pcard" href="{BIG}"><img src="{IMG_CHILL}" alt="Chill一下野餐盒（大）4–6 人" loading="lazy"><div><p class="pn">Chill一下野餐盒（大）</p><p class="pp">4–6 人份　<b>$628</b></p><p class="pd">9 款小食：迷你芝士手打牛肉漢堡、千島汁蜜桃大蝦沙律杯、九層塔香酥雞等</p></div></a>
  <a class="pk-pcard" href="{SMALL}"><img src="{IMG_CHILL}" alt="Chill一下野餐盒（小）2–3 人" loading="lazy"><div><p class="pn">Chill一下野餐盒（小）</p><p class="pp">2–3 人份　<b>$258</b></p><p class="pd">7 款小食：煙鴨胸青瓜蛋三文治、酥皮腸仔卷、焦糖葡撻等</p></div></a>
  <a class="pk-pcard" href="{PLATTER}"><img src="{IMG_PLATTER}" alt="5 人自選拼盤" loading="lazy"><div><p class="pn">5 人自選拼盤</p><p class="pp">5 人份　<b>$498（待核實）</b></p><p class="pd">自選小食組合，適合人多野餐</p></div></a>
</div>
<div class="ao-cta ao-cta--2"><a class="pk-btn" href="{CHILL}">🧺 睇全部野餐盒</a><a class="pk-btn pk-btn--wa" href="{WA}" target="_blank" rel="noopener">WhatsApp 查詢</a></div>
<p class="pk-note">※ 公園入口交收安排（TBC）：滿 $1,450 免運費，交收點待確認。</p>

<div class="ao-related"><p class="ao-related-t">📖 延伸閱讀</p>
<a href="#">【揸車野餐好去處】香港野餐泊車地圖（Blog 2，待寫）→</a>
<a href="https://aoaodelivery.com/blog/kids-birthday-party-catering/">【香港家長必讀】小朋友生日會到會挑選指南 →</a>
</div>
</div>
<script type="application/ld+json">{faq_ld}</script>
<script>{JS}</script>
'''

prev = '''<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>Blog 1 野餐地點推介 Demo</title></head><body style="margin:0;padding:24px 14px;background:#fff">
<div class="pk-demo-bar">DEMO｜<mark class="kw">黃色</mark>＝目標關鍵字／PAA　<label><input type="checkbox" id="hlToggle" checked> 顯示 highlight</label></div>
''' + BODY + '''<script>document.getElementById('hlToggle').onchange=function(){document.body.classList.toggle('no-hl',!this.checked)};</script></body></html>'''
open('preview.html', 'w').write(prev)
open('index.html', 'w').write(prev)
wp = re.sub(r'<mark class="(?:kw|paa)">(.*?)</mark>', r'\1', BODY)
wp = re.sub(r'<p class="pk-kw">.*?</p>', '', wp)
open('blog-picnic-WORDPRESS.html', 'w').write(wp)
print('parks', n, 'car', sum(1 for p in P if p['car']), 'pet', sum(1 for p in P if p['pet'] == 'Y'))
