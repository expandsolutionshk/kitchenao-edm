# Blog 1 KV 方案（5 款，1600×900）→ kv-options.html
# 參考香港媒體野餐文章 KV：真實相片背景＋粗體描邊大字＋色帶／圓章，並加入搜尋器視覺（地區色、地圖標記、tag、篩選掣、地點卡）
import importlib.util, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
s = importlib.util.spec_from_file_location('combo', os.path.join(HERE, 'combo.py')); C = importlib.util.module_from_spec(s); s.loader.exec_module(C)
P, RC, N = C.P, C.RC, C.N
cnt = {r: sum(1 for p in P if p['r'] == r) for r in RC}

L = 'https://www.lcsd.gov.hk/en/parks/'
D = 'https://www.discoverhongkong.com/content/dam/dhk/data/poi/media/'
IMG = {
 'tpwp': L + 'tpwp/common/graphics/gallery/05.jpg',          # 大埔海濱公園（新界）
 'velo': L + 'vdp/common/graphics/slideshow/01.jpg',          # 香港單車館公園（新界）
 'cwb': D + 'c/clearwater-bay-country-park/clearwater-bay-country-park-01.jpg',  # 清水灣（新界）
 'penfold': D + 'p/penfold-park/penfold-park-02.jpg',         # 彭福公園（新界）
 'db': D + 'c/central-park/central-park-02-en.jpg',           # 愉景灣中央公園（新界）一家人野餐
 'ktct': L + 'ktctp/images/2015/01/01.jpg',                   # 啟德郵輪碼頭公園（九龍）
 'ktp': L + 'ktp/common/graphics/fac/fac19.jpg',              # 觀塘海濱花園（九龍）
 'jvp': L + 'jvp/common/graphics/slideshow/01.jpg',           # 佐敦谷公園（九龍）
 'tamar': L + 'tp/common/graphics/fac/1.jpg',                 # 添馬公園（港島）
 'vp': L + 'vp/common/graphics/slideshow/09.jpg',             # 維多利亞公園（港島）
}
BOX = 'https://aoaodelivery.com/wp-content/uploads/2025/04/WhatsApp-Image-2025-04-12-at-4.08.18-PM-600x600.jpeg'
LOGO = 'https://aoaodelivery.com/wp-content/uploads/2023/08/kitchenAO_logo-1.png'
def img(k, cls='bg', extra=''):
    return f'<img class="{cls}" src="{IMG.get(k, k)}" alt="" referrerpolicy="no-referrer" {extra}>'

# ---- 搜尋器地圖（SVG）----
pins = ''
for p in P:
    x, y = C.xy(*C.GEO[p['id']])
    pins += (f'<g transform="translate({x:.1f},{y:.1f})"><path d="M0,0 C-6,-8 -11,-12 -11,-19 A11,11 0 1 1 11,-19 C11,-12 6,-8 0,0Z" '
             f'fill="#fff" stroke="{RC[p["r"]]}" stroke-width="2.6"/><text y="-15" font-size="11" text-anchor="middle">{C.IC(p)}</text></g>')
MAP = f'<svg viewBox="0 0 {C.W} {C.Hh}" class="hkmap"><rect width="{C.W}" height="{C.Hh}" fill="#BFE0F0"/><g fill="#E8F1DD" stroke="#B9CDA4" stroke-width="1.2">{C.land}</g>{pins}</svg>'

FEAT = '<p class="feat">可泊車、寵物友善野餐地點　一鍵搜尋</p>'
import base64
import io
from PIL import Image as _Im
_src = _Im.open(os.path.join(HERE, '..', 'halloween-edm-2026', 'img', 'logo-header-pill.png'))
def _crop(box):
    b = io.BytesIO(); _src.crop(box).save(b, 'PNG'); return 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode()
_LG_ICON = _crop((42, 23, 188, 97))     # ▲●
_LG_TEXT = _crop((218, 40, 506, 88))    # KITCHEN AO
LOGOH = f'<span class="logo2" aria-label="Kitchen AO"><img class="li" src="{_LG_ICON}" alt=""><img class="lt" src="{_LG_TEXT}" alt="Kitchen AO"></span>'
def rg(r, name):
    return f'<span class="rgp" style="--c:{RC[r]}"><i class="mpin" style="--c:{RC[r]}"><b>📍</b></i>{name} {cnt[r]} 個</span>'

KV = []
# 1 三區拼貼
KV.append(('A｜三區拼貼', '新界、九龍、港島三張實景並排，每區標上地區色及地點數目，一眼看出「多地區」。', f'''
<div class="kv k1">
  <div class="tri">
    <div>{img('tpwp')}{rg('nt','新界')}<em>大埔海濱公園</em></div>
    <div>{img('ktct')}{rg('kln','九龍')}<em>啟德郵輪碼頭公園</em></div>
    <div>{img('tamar')}{rg('hk','港島')}<em>添馬公園</em></div>
  </div>
  <div class="shade"></div>
  <div class="top"><span class="pill">2026 香港野餐好去處</span>
  <h2 class="ttl">香港野餐勝地大全</h2>
  <p class="rib">全港 {N} 個大草地／海景／隱世公園推介</p></div>
  {FEAT}{LOGOH}
</div>'''))

# 2 地圖主視覺
KV.append(('B｜搜尋器地圖', '左邊大字標題，右邊直接用搜尋器地圖（地區色標記），三個代表地點以圓形實景相片標示。', f'''
<div class="kv k2">
  {img('vp')}
  <div class="lpanel">
    <span class="pill">2026 香港野餐好去處</span>
    <h2 class="ttl y">全港野餐<br>地點搜尋器</h2>
    <p class="sub">{N} 個野餐地點 × 新界｜九龍｜港島</p>
    <p class="sub2">可泊車、寵物友善野餐地點一鍵搜尋</p>
  </div>
  <div class="mapcard">{MAP}
    <div class="callout c-nt"><span class="ph">{img('tpwp','')}</span><b style="--c:{RC['nt']}">大埔海濱公園</b></div>
    <div class="callout c-kln"><span class="ph">{img('ktct','')}</span><b style="--c:{RC['kln']}">啟德郵輪碼頭公園</b></div>
    <div class="callout c-hk"><span class="ph">{img('tamar','')}</span><b style="--c:{RC['hk']}">添馬公園</b></div>
    <div class="lg"><span><i style="background:{RC['nt']}"></i>新界</span><span><i style="background:{RC['kln']}"></i>九龍</span><span><i style="background:{RC['hk']}"></i>港島</span></div>
  </div>
  {LOGOH}
</div>'''))

# 3 搜尋器 UI
KV.append(('C｜搜尋器介面', '一家人野餐實景做背景，右邊放搜尋器篩選框及地點卡，直接展示「揀地區、可泊車、寵物友善」的功能。', f'''
<div class="kv k3">
  {img('db')}
  <div class="lshade"></div>
  <div class="left">
    <span class="pill">2026 香港野餐好去處</span>
    <h2 class="ttl">野餐好去處<br><span class="y">{N} 個推介</span></h2>
    <p class="sub">{N} 個大草地／海景／隱世公園<br>可泊車、寵物友善地點一鍵搜尋</p>
  </div>
  <div class="ui">
    <div class="flt">
      <p class="lab">① 地區</p>
      <div class="chips"><span class="ch">全部</span><span class="ch on"><i style="background:{RC['nt']}"></i>新界</span><span class="ch"><i style="background:{RC['kln']}"></i>九龍</span><span class="ch"><i style="background:{RC['hk']}"></i>港島</span></div>
      <p class="lab">② 條件及類別</p>
      <div class="chips"><span class="ch on">🚗 可泊車</span><span class="ch on">🐶 寵物友善</span><span class="ch">🌳 大草地</span><span class="ch">🌊 海景</span></div>
      <div class="act"><span class="go">🔍 確定搜尋</span><span class="cnt">符合條件的地點一覽</span></div>
    </div>
    <div class="card">
      <span class="th">{img('penfold','')}</span>
      <div><p class="nm">彭福公園 <small>Penfold Park</small></p>
      <div class="tgs"><span class="tg ok">🧺 適合野餐</span><span class="tg on">🌳 大草地</span><span class="tg pet">🐶 寵物友善</span></div>
      <p class="q">🅿️ 鄰近停車場　🚆 港鐵馬場站</p></div>
    </div>
  </div>
  {LOGOH}
</div>'''))

# 4 雜誌拼圖
KV.append(('D｜雜誌拼圖', '仿本地媒體常用的四格拼圖＋中間色帶大字，配圓形數字章及地圖標記，資訊量最大。', f'''
<div class="kv k4">
  <div class="grid">
    <div>{img('cwb')}<span class="tagp" style="--c:{RC['nt']}">📍 清水灣大坑墩</span></div>
    <div>{img('ktp')}<span class="tagp" style="--c:{RC['kln']}">📍 觀塘海濱花園</span></div>
    <div>{img('velo')}<span class="tagp" style="--c:{RC['nt']}">📍 香港單車館公園</span></div>
    <div>{img('tamar')}<span class="tagp" style="--c:{RC['hk']}">📍 添馬公園</span></div>
  </div>
  <div class="band">
    <h2 class="ttl y">香港野餐好去處大全</h2>
    <p class="rib2">新界｜九龍｜港島　可泊車、寵物友善地點一鍵搜尋</p>
  </div>
  <div class="badge"><b>{N}</b><span>個野餐地點</span></div>
  {LOGOH}
</div>'''))

# 5 拍立得＋野餐盒
KV.append(('E｜拍立得＋野餐盒', '三張拍立得代表三個地區，右邊配 Kitchen AO 野餐盒及「送到附近可停車位置」，連結內容與產品。', f'''
<div class="kv k5">
  {img('jvp')}
  <div class="veil"></div>
  <div class="pola">
    <figure class="p1"><i class="mpin big" style="--c:{RC['nt']}"><b>🌳</b></i>{img('cwb','')}<figcaption><b style="color:{RC['nt']}">新界</b>清水灣大坑墩</figcaption></figure>
    <figure class="p2"><i class="mpin big" style="--c:{RC['kln']}"><b>🌊</b></i>{img('ktct','')}<figcaption><b style="color:{RC['kln']}">九龍</b>啟德郵輪碼頭公園</figcaption></figure>
    <figure class="p3"><i class="mpin big" style="--c:{RC['hk']}"><b>🌳</b></i>{img('tamar','')}<figcaption><b style="color:{RC['hk']}">港島</b>添馬公園</figcaption></figure>
  </div>
  <div class="right">
    <span class="pill">2026 香港野餐好去處</span>
    <h2 class="ttl">懶人野餐<br><span class="y">全攻略</span></h2>
    <p class="sub">{N} 個大草地／海景／秘境</p>
    <div class="boxw"><img src="{BOX}" alt="Kitchen AO 野餐盒"><p><b>🧺 Kitchen AO 野餐盒</b>送到附近可停車位置</p></div>
    <p class="sub2">可泊車、寵物友善地點一鍵搜尋</p>
  </div>
  {LOGOH}
</div>'''))


# ---- F / G：以 E 為基礎（拍立得＋搜尋器篩選框＋右下角小地圖），背景光暗參考 C ----
FLT = f'''<div class="flt">
      <p class="lab">① 地區</p>
      <div class="chips"><span class="ch on">全部</span><span class="ch"><i style="background:{RC['nt']}"></i>新界</span><span class="ch"><i style="background:{RC['kln']}"></i>九龍</span><span class="ch"><i style="background:{RC['hk']}"></i>港島</span></div>
      <p class="lab">② 條件及類別（可多選）</p>
      <div class="chips"><span class="ch on">🚗 可泊車</span><span class="ch on">🐶 寵物友善</span><span class="ch on">🌳 大草地</span><span class="ch on">🌿 秘境</span><span class="ch on">🌊 海景</span><span class="ch on">🏛️ 特色園林</span></div>
      <div class="act"><span class="go">🔍 確定搜尋</span><span class="cnt">全部 {N} 個地點</span><span class="rst">重設</span></div>
    </div>'''
MINIMAP = f'''<div class="minimap">{MAP}
    <div class="mc c-nt"><span class="ph">{img('tpwp','')}</span><b style="--c:{RC['nt']}">大埔海濱公園</b></div>
    <div class="mc c-kln"><span class="ph">{img('ktct','')}</span><b style="--c:{RC['kln']}">啟德郵輪碼頭公園</b></div>
    <div class="mc c-hk"><span class="ph">{img('tamar','')}</span><b style="--c:{RC['hk']}">添馬公園</b></div>
    <div class="lg"><span><i style="background:{RC['nt']}"></i>新界</span><span><i style="background:{RC['kln']}"></i>九龍</span><span><i style="background:{RC['hk']}"></i>港島</span></div>
  </div>'''
TTL = f'''<span class="pill">2026 香港野餐好去處</span>
    <h2 class="ttl">全港野餐<span class="y">地點搜尋器</span></h2>
    <p class="sub">{N} 個野餐地點 × 新界｜九龍｜港島</p>
    <p class="sub2">可泊車、寵物友善野餐地點一鍵搜尋</p>'''
POLA = f'''<figure class="p1"><i class="mpin big" style="--c:{RC['nt']}"><b>🌳</b></i>{img('tpwp','')}<figcaption><b style="color:{RC['nt']}">新界</b>大埔海濱公園</figcaption></figure>
    <figure class="p2"><i class="mpin big" style="--c:{RC['kln']}"><b>🌊</b></i>{img('ktct','')}<figcaption><b style="color:{RC['kln']}">九龍</b>啟德郵輪碼頭公園</figcaption></figure>
    <figure class="p3"><i class="mpin big" style="--c:{RC['hk']}"><b>🌳</b></i>{img('tamar','')}<figcaption><b style="color:{RC['hk']}">港島</b>添馬公園</figcaption></figure>'''
KV.append(('F｜拍立得＋搜尋器（拍立得在左）', '以 E 為基礎：左邊三張拍立得代表三區；右邊標題下改放搜尋器篩選框；搜尋器地圖縮細放右下角。背景改用清水灣郊野公園實景，不加暗化效果。', f'''
<div class="kv kf k6">
  {img('cwb')}
  <div class="pola">{POLA}</div>
  <div class="tblock">{TTL}</div>
  <div class="ui">{FLT}</div>
  {MINIMAP}
  {LOGOH}
</div>'''))
KV.append(('G｜搜尋器＋拍立得（拍立得在右）', '同一 brief 的另一排法：標題及篩選框放左邊（背景同樣不加暗化）；三張拍立得在右上方展開；小地圖放右下角。', f'''
<div class="kv kf k7">
  {img('cwb')}
  <div class="tblock">{TTL}</div>
  <div class="ui">{FLT}</div>
  <div class="pola">{POLA}</div>
  {MINIMAP}
  {LOGOH}
</div>'''))

CSS = '''
*{box-sizing:border-box}body{margin:0;background:#E9E5DC;font-family:-apple-system,"PingFang HK","Microsoft JhengHei",Arial,sans-serif;color:#3f3a33}
.wrap{max-width:1240px;margin:0 auto;padding:24px 16px 60px}.wrap>h1{font-size:22px;margin:0 0 4px}.wrap>p{margin:0 0 20px;color:#7a6a45;font-size:14px}
.opt{margin:0 0 34px}.opt h3{margin:0 0 4px;font-size:18px}.opt p{margin:0 0 10px;font-size:14px;color:#5a5348}
.kv{position:relative;width:100%;aspect-ratio:16/9;container-type:inline-size;overflow:hidden;border-radius:12px;background:#2C6E49;box-shadow:0 6px 24px rgba(0,0,0,.15)}
.kv img{display:block}.kv img.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.ttl{margin:0;font-weight:900;line-height:1.1;color:#fff;-webkit-text-stroke:.55cqw #1A1A1A;paint-order:stroke fill;text-shadow:0 .5cqw 0 #1A1A1A;letter-spacing:.2cqw}
.y{color:#F7CE46}
.pill{display:inline-block;background:#1A1A1A;color:#F7CE46;font-weight:900;font-size:1.9cqw;padding:.6cqw 1.8cqw;border-radius:4cqw;margin-bottom:1.2cqw}
.tg{display:inline-flex;align-items:center;gap:.4cqw;font-weight:800;font-size:1.7cqw;padding:.55cqw 1.4cqw;border-radius:4cqw;border:.18cqw solid transparent;white-space:nowrap;line-height:1.3}
.tg.ok{background:#1A1A1A;color:#F7CE46}.tg.on{background:#F4FBF3;color:#2C6E49;border-color:#CFE8CD}.tg.pet{background:#FFF0E0;color:#C24E00;border-color:#F7D3AE}.tg.car{background:#E6F0FF;color:#1E5BD8;border-color:#C7DAFB}
.feat{position:absolute;left:0;right:0;bottom:3cqw;margin:0;text-align:center;color:#fff;font-weight:900;font-size:3cqw;-webkit-text-stroke:.3cqw #1A1A1A;paint-order:stroke fill;text-shadow:0 .3cqw 0 #1A1A1A}
.sub2{margin:1.4cqw 0 0;display:inline-block;background:#F7CE46;color:#1A1A1A;font-weight:900;font-size:2cqw;padding:.6cqw 1.6cqw;box-shadow:.4cqw .4cqw 0 #1A1A1A}
.feat2{display:flex;flex-wrap:wrap;gap:.8cqw;margin-top:1.6cqw}
.logo{position:absolute;right:1.8cqw;top:1.8cqw;background:#fff;border-radius:1cqw;padding:.6cqw 1cqw;box-shadow:0 .3cqw 1cqw rgba(0,0,0,.2)}.logo img{height:3cqw;width:auto}
.mpin{display:inline-flex;align-items:center;justify-content:center;width:2.4cqw;height:2.4cqw;border-radius:50% 50% 50% 0;transform:rotate(-45deg);background:#fff;border:.25cqw solid var(--c)}.mpin b{transform:rotate(45deg);font-size:1.1cqw;font-weight:400}
.mpin.big{width:4.4cqw;height:4.4cqw;border-width:.4cqw}.mpin.big b{font-size:2.1cqw}
/* 1 */
.k1 .tri{position:absolute;inset:0;display:flex;gap:.5cqw;background:#fff}.k1 .tri>div{position:relative;flex:1;overflow:hidden}.k1 .tri img{width:100%;height:100%;object-fit:cover}
.k1 .shade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.55) 0%,rgba(0,0,0,.05) 50%,rgba(0,0,0,.45) 100%)}
.k1 .rgp{position:absolute;left:1.4cqw;bottom:12.6cqw;display:inline-flex;align-items:center;gap:.6cqw;background:var(--c);color:#fff;font-weight:900;font-size:2cqw;padding:.5cqw 1.4cqw .5cqw .7cqw;border-radius:4cqw;box-shadow:0 .3cqw .8cqw rgba(0,0,0,.3)}
.k1 em{position:absolute;left:1.6cqw;bottom:10.4cqw;color:#fff;font-style:normal;font-weight:800;font-size:1.5cqw;text-shadow:0 .15cqw .4cqw rgba(0,0,0,.7)}
.k1 .top{position:absolute;left:0;right:0;top:3.4cqw;text-align:center}.k1 .ttl{font-size:8cqw}
.rib{display:inline-block;margin:1.6cqw 0 0;background:#F7CE46;color:#1A1A1A;font-weight:900;font-size:2.6cqw;padding:.8cqw 2.4cqw;transform:rotate(-1.5deg);box-shadow:.5cqw .5cqw 0 #1A1A1A}
/* 2 */
.k2 .lpanel{position:absolute;left:0;top:0;bottom:0;width:46%;padding:5cqw 3.5cqw;background:linear-gradient(90deg,rgba(28,72,46,.95) 0%,rgba(28,72,46,.88) 75%,rgba(28,72,46,0) 100%);color:#fff}
.k2 .ttl{font-size:6.6cqw}.sub{margin:1.6cqw 0 0;font-size:2.3cqw;font-weight:900;color:#fff;text-shadow:0 .2cqw .5cqw rgba(0,0,0,.5);line-height:1.35}
.k2 .mapcard{position:absolute;right:3cqw;top:8cqw;width:50%;background:#fff;border-radius:2cqw;padding:1cqw;box-shadow:0 1cqw 3cqw rgba(0,0,0,.35);transform:rotate(1.2deg)}
.hkmap{display:block;width:100%;height:auto;border-radius:1.2cqw}
.callout{position:absolute;display:flex;align-items:center;gap:.6cqw}.callout .ph{width:7cqw;height:7cqw;border-radius:50%;overflow:hidden;border:.45cqw solid #fff;box-shadow:0 .4cqw 1cqw rgba(0,0,0,.35)}.callout .ph img{width:100%;height:100%;object-fit:cover}
.callout b{background:var(--c);color:#fff;font-size:1.5cqw;font-weight:900;padding:.4cqw 1cqw;border-radius:3cqw;white-space:nowrap}
.c-nt{left:28%;top:-3cqw}.c-kln{left:52%;top:15cqw}.c-hk{left:4%;top:24cqw}
.k2 .lg{position:absolute;left:2cqw;bottom:2cqw;display:flex;gap:1cqw;background:rgba(255,255,255,.92);padding:.5cqw 1cqw;border-radius:2cqw;font-size:1.3cqw;font-weight:800}.k2 .lg i{display:inline-block;width:1cqw;height:1cqw;border-radius:50%;margin-right:.4cqw}
/* 3 */
.k3 .lshade{position:absolute;inset:0;background:linear-gradient(90deg,rgba(0,0,0,.6) 0%,rgba(0,0,0,.25) 45%,rgba(0,0,0,0) 70%)}
.k3 .left{position:absolute;left:4cqw;top:6cqw;width:42%}.k3 .ttl{font-size:7cqw}
.k3 .ui{position:absolute;right:3.5cqw;top:6cqw;width:40%;display:flex;flex-direction:column;gap:1.4cqw}
.k3 .flt{background:#fff;border-radius:1.8cqw;padding:1.8cqw 2cqw;box-shadow:0 1cqw 3cqw rgba(0,0,0,.3)}
.k3 .lab{margin:0 0 .6cqw;font-size:1.3cqw;font-weight:800;color:#7a6a45}.chips{display:flex;flex-wrap:wrap;gap:.6cqw;margin-bottom:1.2cqw}
.ch{display:inline-flex;align-items:center;gap:.4cqw;border:.15cqw solid #CFE8CD;background:#F4FBF3;color:#2C6E49;border-radius:3cqw;padding:.45cqw 1.1cqw;font-size:1.4cqw;font-weight:700}.ch i{width:.8cqw;height:.8cqw;border-radius:50%}
.ch.on{background:#3F9D5A;border-color:#3F9D5A;color:#fff}
.k3 .act{display:flex;align-items:center;gap:1.2cqw;border-top:.1cqw solid #EFE8DA;padding-top:1.2cqw}.go{background:#1A1A1A;color:#fff;font-weight:800;font-size:1.4cqw;padding:.6cqw 1.6cqw;border-radius:3cqw}.k3 .cnt{font-size:1.3cqw;font-weight:700;color:#5a5348}
.k3 .card{display:flex;gap:1.2cqw;background:#fff;border-radius:1.8cqw;padding:1.2cqw;box-shadow:0 1cqw 3cqw rgba(0,0,0,.3);transform:translateX(-3cqw) rotate(-1.5deg)}
.k3 .th{flex:0 0 9cqw;height:9cqw;border-radius:1.2cqw;overflow:hidden}.k3 .th img{width:100%;height:100%;object-fit:cover}
.k3 .nm{margin:0 0 .6cqw;font-size:2cqw;font-weight:900;color:#1A1A1A}.k3 .nm small{font-size:1.1cqw;color:#9A8f7e;font-weight:600}
.k3 .tgs{display:flex;flex-wrap:wrap;gap:.5cqw}.k3 .tgs .tg{font-size:1.2cqw;padding:.35cqw .9cqw}.k3 .q{margin:.7cqw 0 0;font-size:1.25cqw;color:#5a5348}
/* 4 */
.k4{background:#fff}.k4 .grid{position:absolute;inset:0;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:.6cqw}
.k4 .grid>div{position:relative;overflow:hidden}.k4 .grid img{width:100%;height:100%;object-fit:cover}
.tagp{position:absolute;left:1.4cqw;top:1.4cqw;background:#fff;color:var(--c);border:.25cqw solid var(--c);font-weight:900;font-size:1.6cqw;padding:.35cqw 1.1cqw;border-radius:3cqw}
.k4 .grid>div:nth-child(2) .tagp,.k4 .grid>div:nth-child(4) .tagp{left:auto;right:1.4cqw}
.k4 .grid>div:nth-child(3) .tagp,.k4 .grid>div:nth-child(4) .tagp{top:auto;bottom:1.4cqw}
.k4 .grid>div:nth-child(2) .tagp{top:7cqw}
.k4 .band{position:absolute;left:0;right:0;top:50%;transform:translateY(-50%);background:rgba(26,26,26,.9);padding:1.6cqw 0 1.4cqw 17cqw;text-align:left}
.k4 .ttl{font-size:6.2cqw;-webkit-text-stroke:.35cqw #1A1A1A;text-shadow:none}
.rib2{margin:.8cqw 0 0;color:#fff;font-weight:800;font-size:2cqw}
.badge{position:absolute;left:2.5cqw;top:50%;transform:translateY(-50%) rotate(-8deg);width:13cqw;height:13cqw;border-radius:50%;background:#F7CE46;border:.6cqw solid #1A1A1A;display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:0 .6cqw 0 #1A1A1A}
.badge b{font-size:6cqw;font-weight:900;line-height:1;color:#1A1A1A}.badge span{font-size:1.5cqw;font-weight:900;color:#1A1A1A}
/* 5 */
.k5 .veil{position:absolute;inset:0;background:linear-gradient(90deg,rgba(255,255,255,.1) 0%,rgba(20,60,38,.55) 55%,rgba(20,60,38,.9) 100%)}
.pola{position:absolute;left:3cqw;top:4cqw;width:52%;height:88%}
.pola figure{position:absolute;margin:0;background:#fff;padding:1cqw 1cqw 0;box-shadow:0 .8cqw 2cqw rgba(0,0,0,.35);width:22cqw}
.pola figure img{width:100%;aspect-ratio:4/3;object-fit:cover}.pola figcaption{padding:.8cqw 0 1cqw;font-size:1.7cqw;font-weight:900;color:#1A1A1A;text-align:center}.pola figcaption b{margin-right:.6cqw}
.pola .mpin{position:absolute;left:50%;top:-2.6cqw;margin-left:-2.2cqw;z-index:2}
.p1{left:0;top:2cqw;transform:rotate(-7deg)}.p2{left:17cqw;top:10cqw;transform:rotate(4deg);z-index:1}.p3{left:4cqw;top:27cqw;transform:rotate(3deg)}
.k5 .right{position:absolute;right:4cqw;top:5cqw;width:38%;color:#fff}.k5 .ttl{font-size:7.4cqw}
.boxw{display:flex;align-items:center;gap:1.2cqw;margin-top:1.8cqw;background:#fff;border-radius:1.6cqw;padding:1cqw;color:#1A1A1A;box-shadow:0 .8cqw 2cqw rgba(0,0,0,.3)}
.boxw img{width:10cqw;height:10cqw;object-fit:cover;border-radius:1cqw}.boxw p{margin:0;font-size:1.6cqw;font-weight:700;line-height:1.5}.boxw b{display:block;font-size:2cqw;color:#2C6E49}

.logo2{position:absolute;right:1.8cqw;top:1.8cqw;z-index:5;box-sizing:border-box;display:inline-flex;align-items:center;height:3.6cqw;background:#fff;border:.22cqw solid #1A1A1A;border-radius:3cqw;padding:0 1.5cqw}.logo2 img{display:block;width:auto}.logo2 .li{height:1.9cqw}.logo2 .lt{height:1.7cqw;margin-left:.85cqw}
.logo2 .tri{width:0;height:0;border-left:1.05cqw solid transparent;border-right:1.05cqw solid transparent;border-bottom:1.8cqw solid #1A1A1A}
.logo2 .dot{width:1.8cqw;height:1.8cqw;border-radius:50%;background:#F39A2B;margin-left:-.35cqw}
.logo2 b{margin-left:.6cqw;font-family:"Avenir Next Condensed","DIN Condensed","Arial Narrow",sans-serif;font-weight:500;font-size:2.2cqw;letter-spacing:.05cqw;color:#1A1A1A;line-height:1}
/* F / G */
.kf .shadeR{position:absolute;inset:0;background:linear-gradient(270deg,rgba(0,0,0,.62) 0%,rgba(0,0,0,.3) 45%,rgba(0,0,0,0) 72%)}
.kf .shadeL{position:absolute;inset:0;background:linear-gradient(90deg,rgba(0,0,0,.62) 0%,rgba(0,0,0,.3) 45%,rgba(0,0,0,0) 72%)}
.kf .ttl{font-size:4.8cqw;white-space:nowrap}.kf .sub{font-size:2.3cqw;margin-top:1.2cqw;color:#1A1A1A;font-weight:900;-webkit-text-stroke:.45cqw #fff;paint-order:stroke fill;text-shadow:none}.kf .sub2{font-size:1.9cqw;margin-top:1cqw}
.kf .flt{background:#fff;border-radius:1.8cqw;padding:1.4cqw 1.6cqw;box-shadow:0 1cqw 3cqw rgba(0,0,0,.3)}
.kf .ch{font-size:1.25cqw;padding:.35cqw .9cqw}.kf .lab{margin:0 0 .5cqw;font-size:1.2cqw;font-weight:800;color:#7a6a45}.kf .chips{margin-bottom:1cqw}
.kf .rst{margin-left:auto;font-size:1.25cqw;font-weight:700;color:#9A7B2E;text-decoration:underline}.kf .act{display:flex;align-items:center;gap:1.2cqw;border-top:.1cqw solid #EFE8DA;padding-top:1cqw}.kf .cnt{font-size:1.25cqw;font-weight:700;color:#5a5348}
.kf .ui{position:absolute;width:36cqw}
.kf .pola{position:absolute}.kf .pola figure{width:17cqw;padding:.8cqw .8cqw 0}.kf .pola figcaption{font-size:1.35cqw;padding:.6cqw 0 .8cqw}
.kf .pola .mpin.big{width:3.6cqw;height:3.6cqw;margin-left:-1.8cqw;top:-2.2cqw}.kf .pola .mpin.big b{font-size:1.7cqw}
.minimap{position:absolute;right:2.2cqw;bottom:2.2cqw;width:22cqw;background:#fff;border-radius:1.2cqw;padding:.6cqw;box-shadow:0 .8cqw 2.4cqw rgba(0,0,0,.4);transform:rotate(2deg);z-index:3}
.minimap .hkmap{border-radius:.8cqw}
.mc{position:absolute;display:flex;align-items:center;gap:.3cqw}.mc .ph{width:3.4cqw;height:3.4cqw;border-radius:50%;overflow:hidden;border:.25cqw solid #fff;box-shadow:0 .2cqw .6cqw rgba(0,0,0,.35)}.mc .ph img{width:100%;height:100%;object-fit:cover}
.mc b{background:var(--c);color:#fff;font-size:.85cqw;font-weight:900;padding:.2cqw .6cqw;border-radius:2cqw;white-space:nowrap}
.minimap .c-nt{left:30%;top:-1.6cqw}.minimap .c-kln{left:50%;top:6.4cqw}.minimap .c-hk{left:3%;top:10cqw}
.minimap .lg{position:absolute;left:1cqw;bottom:1cqw;display:flex;gap:.5cqw;background:rgba(255,255,255,.92);padding:.25cqw .6cqw;border-radius:1cqw;font-size:.75cqw;font-weight:800}.minimap .lg i{display:inline-block;width:.6cqw;height:.6cqw;border-radius:50%;margin-right:.25cqw}
/* F：拍立得在左，標題及篩選框在右 */
.k6 .pola{left:3cqw;top:4cqw;width:46%;height:50cqw}
.k6 .p1{left:0;top:1cqw;transform:rotate(-7deg)}.k6 .p2{left:14cqw;top:9cqw;transform:rotate(4deg);z-index:1}.k6 .p3{left:3cqw;top:25cqw;transform:rotate(3deg)}
.k6 .tblock{position:absolute;left:47%;top:3.5cqw;color:#fff}
.k6 .ui{left:47%;top:27cqw;width:32cqw}
/* G：標題及篩選框在左，拍立得在右上 */
.k7 .tblock{position:absolute;left:4cqw;top:2.6cqw;color:#fff}
.k7 .ui{left:4cqw;top:27cqw;width:34cqw}
.k7 .pola{left:54.5%;top:10cqw;width:46%;height:30cqw}
.k7 .pola figure{width:14.5cqw}.k7 .pola figcaption{font-size:1.2cqw;white-space:nowrap}
.k7 .p1{left:0;top:2.5cqw;transform:rotate(-5deg)}.k7 .p2{left:14.8cqw;top:0;transform:rotate(2deg);z-index:1}.k7 .p3{left:29.4cqw;top:3cqw;transform:rotate(6deg)}

/* G：除標題外放大 20%，地圖放大 30% */
.k7 .logo2{transform:scale(1.2);transform-origin:top right}
.k7 .pill{font-size:2.28cqw;padding:.6cqw 2cqw;margin-bottom:1cqw}
.k7 .sub{font-size:2.76cqw}.k7 .sub2{font-size:2.28cqw;padding:.72cqw 1.92cqw}
.k7 .ui{top:28.6cqw;width:37cqw;transform:scale(1.2);transform-origin:top left}.k7 .flt{padding:1.1cqw 1.4cqw}.k7 .chips{margin-bottom:.7cqw}.k7 .lab{margin-bottom:.35cqw}.k7 .act{padding-top:.8cqw}
.k7 .pola{left:51.5%;top:9cqw}
.k7 .pola figure{width:16.2cqw;padding:.96cqw .96cqw 0}.k7 .pola figcaption{font-size:1.44cqw;padding:.72cqw 0 .96cqw}
.k7 .pola .mpin.big{width:4.3cqw;height:4.3cqw;margin-left:-2.15cqw;top:-2.6cqw}.k7 .pola .mpin.big b{font-size:2cqw}
.k7 .p1{left:0}.k7 .p2{left:15.3cqw}.k7 .p3{left:30.6cqw}
.k7 .minimap{transform:rotate(2deg) scale(1.3);transform-origin:bottom right}
'''
html = f'''<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>Blog 1 KV 方案（7 款）</title><style>{CSS}</style></head><body><div class="wrap">
<h1>🧺 Blog 1 KV 方案（7 款，1600 × 900）</h1>
<p>背景為官方實景相片（康文署／旅發局，僅作概念示意）；正式製作建議改用自家拍攝或已取得授權的高解像度相片。</p>
{''.join(f'<section class="opt"><h3>{t}</h3><p>{d}</p>{h}</section>' for t, d, h in KV)}
</div></body></html>'''
# 選定方案 G → 單獨 KV 頁（供 blog mockup 以 iframe 嵌入）
KV_G = [h for t, d, h in KV if t.startswith('G')][0]
KV_G_HTML = f'''<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>Blog 1 KV（G）</title><style>{CSS}
html,body{{margin:0;background:transparent}}.kv{{border-radius:0;box-shadow:none}}</style></head><body>{KV_G}</body></html>'''
if __name__ == '__main__':
    open(os.path.join(HERE, 'kv-options.html'), 'w').write(html)
    open(os.path.join(HERE, 'kv-g.html'), 'w').write(KV_G_HTML); print('ok', len(KV))
