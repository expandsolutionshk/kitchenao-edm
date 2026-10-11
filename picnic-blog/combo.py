# 搜尋器整合版（D 比較表 + E 地圖 + B 列表）— Mobile Demo → combo-mobile.html
import importlib.util, json
spec = importlib.util.spec_from_file_location('b', 'build.py'); b = importlib.util.module_from_spec(spec); spec.loader.exec_module(b)
P = b.P; CATS = b.CATS
GEO = {'tamar':(22.282,114.166),'sysmp':(22.290,114.142),'cyber':(22.261,114.130),'vpark':(22.282,114.188),'peak':(22.271,114.146),'hkpark':(22.277,114.161),'mtdavis':(22.275,114.119),
'wkcd':(22.301,114.158),'ktap':(22.330,114.200),'ktct':(22.306,114.214),'shingfung':(22.318,114.206),'jvp':(22.323,114.219),'ktprom':(22.310,114.222),'ckl':(22.302,114.229),'klnpark':(22.300,114.170),'namcheong':(22.326,114.155),'lokfu':(22.339,114.188),
'penfold':(22.401,114.204),'tpwp':(22.452,114.183),'velo':(22.316,114.263),'mospark':(22.426,114.231),'saisha':(22.432,114.241),'ngongping':(22.408,114.258),'taitamtun':(22.287,114.293),'tapmun':(22.471,114.360),'yuentun':(22.394,114.093),'tyipark':(22.358,114.106),'tyiwf':(22.350,114.098),'howo':(22.375,113.966),'tmpark':(22.392,113.976),'namsang':(22.465,114.030),'tswpark':(22.457,114.005),'ylpark':(22.440,114.017),
'inspire':(22.313,114.042),'db':(22.296,114.020)}
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
RN = {'hk':'港島','kln':'九龍','nt':'新界','is':'離島'}
RC = {'hk':'#E8743B','kln':'#3F9D5A','nt':'#1E5BD8','is':'#8E44AD'}
def attrs(p): return f'data-id="{p["id"]}" data-r="{p["r"]}" data-car="{1 if p["car"] else 0}" data-pet="{p["pet"]}" data-cats="{" ".join(p["cats"])}"'
def cars(p): return '、'.join(n for n,_ in p['car']) or p.get('carnote','—')
# E map pins
pins = ''
for p in P:
    x, y = xy(*GEO[p['id']])
    pins += f'<a class="pin" href="#b-{p["id"]}" {attrs(p)} style="left:{x/W*100:.2f}%;top:{y/Hh*100:.2f}%;--c:{RC[p["r"]]}"><span><b>{CATS[p["cats"][0]][0]}</b></span><i>{p["name"]}</i></a>'
# D table
ck = lambda v: '<b class="y">✓</b>' if v else '<span class="n">·</span>'
CK = list(CATS)
thead = '<tr><th class="st">地點</th><th>🚗</th><th>🐶</th>' + ''.join(f'<th>{CATS[k][0]}</th>' for k in CK) + '</tr>'
trs = ''.join(f'<tr {attrs(p)}><td class="st"><a href="#b-{p["id"]}">{p["name"]}</a><small>{RN[p["r"]]}</small></td><td>{ck(p["car"])}</td><td>{"<b class=y>✓</b>" if p["pet"]=="Y" else ("<b class=p>指定</b>" if p["pet"]=="P" else "<span class=n>·</span>")}</td>' + ''.join(f'<td>{ck(k in p["cats"])}</td>' for k in CK) + '</tr>' for p in P)
# B list (all info shown)
items = ''
for p in P:
    carl = ''.join(f'<li>🅿️ {n}</li>' for n,_ in p['car']) or f'<li>⚠️ {p.get("carnote","暫無停車場資料")}</li>'
    items += f'''<article class="b-row" id="b-{p['id']}" {attrs(p)}>
  <div class="b-top"><div class="ph">📷</div><div class="b-hd"><h3>{p['name']}</h3><span class="rg" style="background:{RC[p['r']]}">{RN[p['r']]}</span><div class="tg">{b.tags(p)}</div></div></div>
  <p class="in">{p['intro']}</p>
  <p class="s">🚇 {p['tr']}</p><p class="s">🐶 {p['petnote']}</p>
  <div class="car"><b>鄰近停車場</b><ul>{carl}</ul></div>
  <a class="back" href="#hk-map">↑ 返回地圖</a>
</article>'''
chips_r = '<button class="ch on" data-f="r" data-v="all">全部</button>' + ''.join(f'<button class="ch" data-f="r" data-v="{k}"><i style="background:{RC[k]}"></i>{v}</button>' for k,v in RN.items())
chips_c = ''.join(f'<button class="ch" data-f="cat" data-v="{k}">{v[0]} {v[1]}</button>' for k,v in CATS.items())
CSS = '''
#lmap{height:340px;border-radius:14px;display:none}#lmap.on{display:block}.lpin{display:flex;align-items:center;justify-content:center;width:28px;height:28px;border-radius:14px;background:#fff;border:2.5px solid var(--c);box-shadow:0 2px 6px rgba(0,0,0,.3);font-size:14px}.leaflet-tooltip{font-weight:800;font-size:12px}
*{box-sizing:border-box}body{margin:0;background:#E9E5DC;font-family:-apple-system,"PingFang HK","Microsoft JhengHei",Arial,sans-serif;color:#3f3a33;}
.phone{max-width:430px;margin:0 auto;background:#fff;min-height:100vh;box-shadow:0 0 30px rgba(0,0,0,.12);}
.hd{padding:16px 16px 10px;background:linear-gradient(135deg,#3F9D5A,#2C6E49);color:#fff;}
.hd p{margin:0;font-size:12px;opacity:.85}.hd h1{margin:4px 0 0;font-size:21px;}
.flt{margin:12px;padding:12px;border:2px solid #3F9D5A;border-radius:16px;background:#fff;}.frow{display:flex;flex-wrap:wrap;align-items:center;gap:6px;margin:0 0 8px;}.lab{flex:0 0 100%;font-size:12px;font-weight:800;color:#2C6E49;}
.row{display:flex;gap:6px;overflow-x:auto;padding-bottom:6px;scrollbar-width:none;}.row::-webkit-scrollbar{display:none}
.ch{flex:0 0 auto;border:1.5px solid #CFE8CD;background:#F4FBF3;color:#2C6E49;border-radius:20px;padding:5px 11px;font-size:13px;font-weight:700;display:flex;align-items:center;gap:5px;}
.ch i{width:9px;height:9px;border-radius:5px;display:inline-block}.ch.on{background:#3F9D5A;border-color:#3F9D5A;color:#fff;}
.cnt{display:flex;justify-content:space-between;font-size:12.5px;font-weight:700;padding-top:2px}.cnt button{border:0;background:none;color:#9A7B2E;font-weight:700;text-decoration:underline;padding:0}
.sec{padding:14px 12px 4px}.sec h2{margin:0 0 8px;font-size:16px;color:#1A1A1A}.sec h2 small{font-weight:600;color:#9A8f7e;font-size:12px;margin-left:4px}
/* map */
.map{position:relative;width:100%;aspect-ratio:540/360;border-radius:14px;overflow:hidden;background:#BFE0F0;}
.map svg{position:absolute;inset:0;width:100%;height:100%}.map polygon{fill:#E8F1DD;stroke:#B9CDA4;stroke-width:1.2}
.map .note{position:absolute;left:8px;bottom:6px;font-size:10.5px;color:#4d7b93;font-weight:700}
.pin{position:absolute;transform:translate(-50%,-100%);text-decoration:none;z-index:2}
.pin span{display:flex;align-items:center;justify-content:center;width:24px;height:24px;border-radius:12px 12px 12px 0;transform:rotate(-45deg);background:#fff;border:2px solid var(--c);box-shadow:0 2px 5px rgba(0,0,0,.25);font-size:12px}
.pin span b{display:block;transform:rotate(45deg);font-weight:400;line-height:1}
.pin i{position:absolute;left:50%;top:-20px;transform:translateX(-50%);display:none;font-style:normal;font-size:11px;font-weight:800;color:#1A1A1A;background:#fff;border-radius:6px;padding:1px 6px;white-space:nowrap;box-shadow:0 1px 4px rgba(0,0,0,.2)}
.pin:hover i,.pin.lbl i{display:block}.pin.off{display:none}
.lg{display:flex;flex-wrap:wrap;gap:4px 10px;margin-top:6px;font-size:11px;color:#7A7268}
/* table */
.tw{overflow-x:auto;border-radius:12px;border:1px solid #EFE8DA}
table{border-collapse:collapse;width:100%;table-layout:fixed;font-size:12px}
th{background:#1A1A1A;color:#fff;padding:6px 0;font-weight:700;font-size:13px}td{padding:6px 0;text-align:center;border-bottom:1px solid #F2ECE0}
.st{text-align:left;width:31%;padding-left:6px!important;background:#fff}th.st{background:#1A1A1A}
td.st a{color:#1A1A1A;font-weight:800;text-decoration:none;font-size:12px;line-height:1.3;display:block}td.st small{display:block;color:#9A8f7e;font-size:10.5px}
tr:nth-child(even) td{background:#FBF8F2}tr:nth-child(even) td.st{background:#FBF8F2}
.y{color:#2C6E49;font-size:14px}.p{color:#B07A3A;font-size:10px}.n{color:#d3cbbb}
/* list */
.b-row{border:1px solid #EBE3D2;border-radius:14px;padding:12px;margin:0 0 12px;scroll-margin-top:12px;transition:box-shadow .3s,border-color .3s}
.b-row.hit{border-color:#3F9D5A;box-shadow:0 0 0 4px rgba(63,157,90,.25)}
.b-top{display:flex;gap:10px}.ph{flex:0 0 92px;height:92px;border-radius:10px;background:repeating-linear-gradient(45deg,#EEF6ED,#EEF6ED 8px,#E3F0E1 8px,#E3F0E1 16px);display:flex;align-items:center;justify-content:center;font-size:20px}
.b-hd{min-width:0}.b-hd h3{margin:0 0 4px;font-size:16px;color:#1A1A1A;display:inline}
.rg{display:inline-block;margin-left:6px;color:#fff;font-size:10.5px;font-weight:700;border-radius:10px;padding:1px 7px;vertical-align:2px}
.tg{display:flex;flex-wrap:wrap;gap:4px;margin-top:6px}.pk-tag{font-size:11px;font-weight:700;padding:2px 8px;border-radius:20px}
.t-car{background:#E6F0FF;color:#1E5BD8}.t-pet{background:#FFF0E0;color:#C24E00}.t-pet2{background:#FFF7EC;color:#B07A3A}.t-cat{background:#F4FBF3;color:#2C6E49}
.in{margin:10px 0 6px;font-size:14px;line-height:1.65}.s{margin:0 0 4px;font-size:13px;color:#5d534d;line-height:1.6}
mark{background:none;color:inherit}
.car{margin-top:8px;padding:8px 10px;border-radius:10px;background:#F6F8FB;font-size:12.5px}.car b{color:#1E5BD8;font-size:11.5px;letter-spacing:1px}.car ul{margin:3px 0 0;padding:0;list-style:none}
.back{display:inline-block;margin-top:8px;font-size:12px;font-weight:700;color:#9A7B2E;text-decoration:none}
.empty{display:none;padding:14px;text-align:center;background:#FFF4F2;border-radius:12px;font-size:13px}
.off{display:none!important}
'''
JS = '''
var LM=null,LMK={};
(function(){if(!window.L)return;var m=document.getElementById('lmap');m.classList.add('on');document.getElementById('svgmap').style.display='none';LM=L.map(m,{scrollWheelZoom:false}).setView([22.36,114.13],10);L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{maxZoom:18,attribution:'© OpenStreetMap'}).addTo(LM);PTS.forEach(function(p){var mk=L.marker([p.lat,p.lng],{icon:L.divIcon({className:'',html:'<div class="lpin" style="--c:'+p.c+'">'+p.ic+'</div>',iconSize:[28,28],iconAnchor:[14,14]})}).addTo(LM).bindTooltip(p.n);mk.on('click',function(){go('#b-'+p.id)});LMK[p.id]=mk;});})();
function go(h){var t=document.querySelector(h);if(!t)return;t.scrollIntoView({behavior:'smooth',block:'start'});t.classList.add('hit');setTimeout(function(){t.classList.remove('hit')},1800);}

(function(){var st={r:'all',car:0,pet:0,cats:[]};var els=document.querySelectorAll('[data-id]');
function ok(e){if(st.r!=='all'&&e.dataset.r!==st.r)return false;if(st.car&&e.dataset.car!=='1')return false;if(st.pet&&e.dataset.pet!=='Y')return false;var c=e.dataset.cats.split(' ');return st.cats.every(function(x){return c.indexOf(x)>-1})}
function apply(){var n=0;els.forEach(function(e){var o=ok(e);e.classList.toggle('off',!o);if(o&&e.classList.contains('b-row'))n++;});
document.getElementById('cnt').textContent=(n===35?'全部 ':'符合：')+n+' 個地點';document.getElementById('empty').style.display=n?'none':'block';
if(LM){var vis=[];document.querySelectorAll('.b-row').forEach(function(e){var mk=LMK[e.dataset.id];if(!mk)return;if(e.classList.contains('off')){LM.removeLayer(mk)}else{mk.addTo(LM);vis.push(mk.getLatLng())}});if(vis.length&&vis.length<35)LM.fitBounds(L.latLngBounds(vis).pad(0.3),{maxZoom:14});}var pins=document.querySelectorAll('.pin:not(.off)');pins.forEach(function(p){p.classList.toggle('lbl',pins.length<=6)});}
document.querySelectorAll('.ch').forEach(function(b){b.onclick=function(){var f=b.dataset.f,v=b.dataset.v;
if(f==='r'){st.r=v;document.querySelectorAll('.ch[data-f=r]').forEach(function(x){x.classList.toggle('on',x===b)})}
else if(f==='car'){st.car=!st.car;b.classList.toggle('on')}else if(f==='pet'){st.pet=!st.pet;b.classList.toggle('on')}
else{var i=st.cats.indexOf(v);if(i>-1)st.cats.splice(i,1);else st.cats.push(v);b.classList.toggle('on')}apply();}});
document.getElementById('rst').onclick=function(){st={r:'all',car:0,pet:0,cats:[]};document.querySelectorAll('.ch').forEach(function(x){x.classList.toggle('on',x.dataset.v==='all')});apply();};
document.querySelectorAll('a[href^="#b-"]').forEach(function(a){a.onclick=function(ev){ev.preventDefault();go(a.getAttribute('href'));}});
apply();})();
'''
html = f'''<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>野餐地點搜尋器 Mobile Demo（D＋E＋B）</title><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.css"><style>{CSS}</style></head><body><div class="phone">
<div class="hd"><p>Kitchen AO・Blog 1 搜尋器 Demo（Mobile）</p><h1>🧺 全港野餐地點搜尋器</h1></div>
<div class="flt">
<div class="frow"><span class="lab">① 地區</span>{chips_r}</div>
<div class="frow"><span class="lab">② 條件</span><button class="ch" data-f="car" data-v="1">🚗 可泊車</button><button class="ch" data-f="pet" data-v="Y">🐶 寵物友善</button></div>
<div class="frow"><span class="lab">③ 類別</span>{chips_c}</div>
<div class="cnt"><span id="cnt"></span><button id="rst">重設</button></div></div>
<div class="sec" id="hk-map"><h2>📍 地圖<small>撳 pin 跳去地點介紹</small></h2><div id="lmap"></div><div class="map" id="svgmap"><svg viewBox="0 0 {W} {Hh}" preserveAspectRatio="none">{land}</svg>{pins}<span class="note">示意地圖，非真實比例</span></div>
<div class="lg">{''.join(f'<span><b style="color:{RC[k]}">●</b> {v}</span>' for k,v in RN.items())}<span>pin 內 icon＝主要類別</span></div></div>
<div class="sec"><h2>📊 一覽比較表<small>撳地點名跳去介紹</small></h2><div class="tw"><table><thead>{thead}</thead><tbody>{trs}</tbody></table></div></div>
<div class="sec"><h2>📝 地點介紹</h2><p class="empty" id="empty">冇符合條件嘅地點，試吓減少篩選條件。</p>{items}</div>
</div><script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.js"></script><script>var PTS={json.dumps([dict(id=p["id"],n=p["name"],lat=GEO[p["id"]][0],lng=GEO[p["id"]][1],c=RC[p["r"]],ic=CATS[p["cats"][0]][0]) for p in P],ensure_ascii=False)};</script><script>{JS}</script></body></html>'''
open('combo-mobile.html','w').write(html); print(len(html))
