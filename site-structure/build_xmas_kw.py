# -*- coding: utf-8 -*-
"""聖誕 KW 分配頁（Seasonal › 聖誕節）
資料：xmas-kw-sources.json（GKP 香港 2025-10 至 2026-09）、core-kw-sources.json（Semrush 10-23、GSC 10-08）
輸出：xmas-kw.html
"""
import json, re, html, os
from diag_embed import section as DSEC, from_index, CSS as DCSS
HERE = os.path.dirname(os.path.abspath(__file__))
X = json.load(open(os.path.join(HERE, 'xmas-kw-sources.json'), encoding='utf-8'))
C = json.load(open(os.path.join(HERE, 'core-kw-sources.json'), encoding='utf-8'))
n = lambda k: re.sub(r'\s+', '', k).lower()
GKP = {n(r['kw']): r for r in X['rows']}
SEM, GSC = C['semrush'], C['gsc']
P = 'https://aoaodelivery.com'
E = html.escape

PAGES = {
 'LP':    ('聖誕到會 Landing page（中文）', '建議新增：/product-category/christmas-set/'),
 'LP-EN': ('聖誕到會 Landing page（英文）', '建議新增：/en/product-category/christmas-set/'),
 'BLOG':  ('聖誕 Blog（改寫）', '/blog/christmas-catering-hong-kong/'),
 'X':     ('不放', ''),
}

R = []
def add(pg, typ, kws, lang='中', use=''):
    for k in kws: R.append(dict(kw=k, pg=pg, typ=typ, lang=lang, use=use))

# ---------- Landing page（交易型）----------
add('LP', '主要', ['聖誕到會'], use='H1／Title／頁頂首段')
add('LP', '次要', ['聖誕到會套餐', '聖誕外賣', '聖誕派對食物', '公司聖誕派對到會', '聖誕到會餐單', '聖誕節到會', '聖誕大餐到會', '聖誕套餐 2026'], use='頁頂內容／H2／Meta')
add('LP', '長尾', ['火雞到會', '火雞訂購', '訂火雞', '火雞餐', '聖誕大餐外賣', '聖誕大餐外送', '聖誕素食餐'], use='產品名／FAQ（只寫真實有售的產品）')
add('LP-EN', '主要', ['christmas catering hong kong'], lang='EN', use='EN H1／Title')
add('LP-EN', '次要', ['christmas catering', 'xmas catering', 'xmas party catering', 'xmas lunch'], lang='EN', use='EN 頁頂內容／Meta')
add('LP-EN', '長尾', ['turkey hk', 'roast turkey hong kong', 'turkey catering hong kong', 'order turkey online', 'christmas bbq menu'], lang='EN', use='EN 產品名／FAQ')
# ---------- Blog（資訊型）----------
add('BLOG', '主要', ['聖誕大餐'], use='H1／Title／30 秒速覽')
add('BLOG', '次要', ['火雞', '薑餅人', '聖誕蛋糕', '聖誕曲奇', '聖誕小食', '聖誕甜品', '薑餅屋', '聖誕朱古力', '聖誕到會推介'], use='H2「經典聖誕食物一覽」／FAQ（火雞夠幾多人吃）')
add('BLOG', '長尾', ['聖誕食品', '聖誕節美食', '聖誕節菜式', '聖誕糖果', '拐杖糖', '聖誕布甸', '樹幹蛋糕', '聖誕冬甩', '聖誕馬卡龍', '聖誕杯子蛋糕', '聖誕泡芙', '聖誕可麗露', '聖誕布朗尼', '聖誕雪人蛋糕', '意大利聖誕麵包', '史多倫麵包', '肉餡餅', '簡單聖誕甜品', '糖霜曲奇', '薑餅曲奇', '聖誕軟餐'], use='H3／經典聖誕食物表')
add('BLOG', '長尾', ['panettone', 'gingerbread man', 'gingerbread house', 'christmas cake', 'candy cane', 'mince pie', 'christmas cookies', 'stollen', 'christmas dessert', 'yule log cake'], lang='EN', use='中文 Blog 內以括號寫英文名，例如「意大利聖誕麵包（Panettone）」（Blog 沒有英文版）')
PARTY = ['瑞士雞翼', '蜜汁雞翼', '烤雞翼', '水牛城雞翼', '薯角', '菠蘿腸仔', '迷你漢堡', '一口漢堡', 'sliders', '炸蝦多士', '一口多士', '沙嗲牛肉串', '沙嗲雞肉串', '照燒雞肉串',
         '凱撒沙律', '薯仔沙律', '雜果沙律', '蝦沙律', '蔬菜條沙律', 'popcorn chicken', '爆谷雞', '炸雞粒', '墨西哥脆片', '煙三文魚卷', '煙三文魚脆餅', '泡芙塔',
         '芝士條', '炸蟹鉗', '椒鹽蝦', '椒鹽魷魚', '炸魷魚圈', '炸洋蔥圈', '炸廣島蠔', '炸莫札瑞拉芝士', '笑臉薯餅', '芝士肉丸', '瑞典肉丸', '黑椒牛柳粒', '蒜蓉牛柳粒',
         '蛋沙律三文治', '吞拿魚三文治', '一口三文治', '碎蛋牛角包', '迷你牛角包', '迷你熱狗', '香腸卷', 'sausage rolls', 'pigs in blankets', '煙肉包腸仔', '迷你鹹批', 'quiche',
         '蜜瓜火腿', '風乾火腿拼盤', '冷肉拼盤', 'charcuterie board', '芝士拼盤', '忌廉芝士餅乾', 'bruschetta', '法式麵包脆片', '焗青口', 'prawn cocktail', '雞尾酒蝦', '鮮蝦杯',
         '煙肉卷帶子', 'bacon wrapped scallops', '水果串', '焗棉花糖', 'brownie', '布朗尼', '心太軟', '熔岩朱古力蛋糕', '松露朱古力', '蘋果批', '肉桂卷']
for k in PARTY:
    add('BLOG', '派對食物清單', [k], lang='EN' if re.match(r'^[a-z ]+$', k) else '中', use='H2「聖誕派對食物推介」清單／表格，有售的連去產品頁')
# ---------- 不放 ----------
add('X', '不放', ['canapes'], lang='EN', use='已分配給商務活動頁（canapés）')
add('X', '不放', ['感恩節火雞訂購', '聖誕event'], use='和聖誕到會無關')
add('X', '不放', [r['kw'] for r in X['rows'] if r.get('brand')], use='對手品牌字，不寫品牌名、不放連結')

# Kitchen AO 有售的相關產品
PROD = {
 '瑞士雞翼': ('蜜蜜燒雞翼配脆薯角', '/product/a0500-honey-glazed-chicken-wings-w-potato-wedges/'),
 '蜜汁雞翼': ('蜜蜜燒雞翼配脆薯角', '/product/a0500-honey-glazed-chicken-wings-w-potato-wedges/'),
 '烤雞翼': ('蜜蜜燒雞翼配脆薯角', '/product/a0500-honey-glazed-chicken-wings-w-potato-wedges/'),
 '薯角': ('蜜蜜燒雞翼配脆薯角', '/product/a0500-honey-glazed-chicken-wings-w-potato-wedges/'),
 '菠蘿腸仔': ('甜甜鮮茄菠蘿焗芝士腸', '/product/a1120-baked-cheese-sausage-with-fresh-tomato-pineapple-sauce-2-pounds/'),
 '迷你漢堡': ('迷你芝士手打豬肉牛肉漢堡', '/product/a0700-handmade-mini-cheeseburger/'),
 '一口漢堡': ('迷你芝士手打豬肉牛肉漢堡', '/product/a0700-handmade-mini-cheeseburger/'),
 'sliders': ('迷你芝士手打豬肉牛肉漢堡', '/product/a0700-handmade-mini-cheeseburger/'),
 '炸蝦多士': ('懷舊芝麻蝦滑多士', '/product/a3400-deep-fried-sesame-shrimp-toast-with-thai-sauce/'),
 '一口多士': ('懷舊芝麻蝦滑多士', '/product/a3400-deep-fried-sesame-shrimp-toast-with-thai-sauce/'),
 '沙嗲牛肉串': ('香烤沙嗲串燒（豬雞）', '/product/a0200-grilled-satay-skewer-pork-and-chicken/'),
 '沙嗲雞肉串': ('香烤沙嗲串燒（豬雞）', '/product/a0200-grilled-satay-skewer-pork-and-chicken/'),
 '凱撒沙律': ('油香煙三文魚凱撒沙律', '/product/s0300-smoked-salmon-caesar-salad/'),
 '蝦沙律': ('千島汁大蝦蜜桃沙律', '/product/shrimp-and-peach-salad-in-thousand-island-dressing/'),
 'popcorn chicken': ('台式九層塔鹽酥雞', '/product/a2800-crispy-basil-chicken-dice/'),
 '爆谷雞': ('台式九層塔鹽酥雞', '/product/a2800-crispy-basil-chicken-dice/'),
 '炸雞粒': ('台式九層塔鹽酥雞', '/product/a2800-crispy-basil-chicken-dice/'),
 '墨西哥脆片': ('芝士粟米片配三色醬', '/product/a3100-cheese-nachos-with-flavorful-three-colour-salsa/'),
 '煙三文魚卷': ('煙三文魚卷牛油果醬法包多士', '/product/c1001-煙三文魚卷牛油果醬法包多士-1件/'),
 '泡芙塔': ('珍珠泡芙', '/product/d05-pearl-sugar-puffs-10pic/'),
 '聖誕泡芙': ('珍珠泡芙', '/product/d05-pearl-sugar-puffs-10pic/'),
 '聖誕馬卡龍': ('法式七彩馬卡龍', '/product/d01-french-colorful-macarons-10-pieces/'),
 '炸洋蔥圈': ('日式雞皮餃子配洋蔥圈', '/product/a1600-japanese-chicken-skin-dumplings-with-crispy-onion-rings/'),
}

rows, seen = [], set()
for r in R:
    k = n(r['kw'])
    if k in seen: continue
    seen.add(k)
    g = GKP.get(k) or {}
    s = SEM.get(k) or {}
    gs = GSC.get(k)
    pr = PROD.get(r['kw'])
    src = []
    if g: src.append('GKP' + ('（Ads 搜尋字新增）' if g.get('new') else ''))
    if s: src.append('Semrush')
    if gs: src.append('GSC')
    rows.append(dict(kw=r['kw'], pg=r['pg'], typ=r['typ'], lang=r['lang'], use=r['use'],
        vol=g.get('vol') if g.get('vol') is not None else (s.get('vol') or None),
        nov=g.get('nov'), dec=g.get('dec'), m3=round(g['m3'] * 100) if g.get('m3') is not None else None,
        gi=gs[1] if gs else None, gp=round(gs[2], 1) if gs and gs[2] else None,
        prod=pr[0] if pr else '', purl=P + pr[1] if pr else '', src='、'.join(src) or '—'))

def stats(pg):
    rs = [r for r in rows if r['pg'] == pg]
    return len(rs), sum(r['vol'] or 0 for r in rs), sum(r['dec'] or 0 for r in rs)

def kwli(pg, typs=None, lim=8):
    rs = sorted([r for r in rows if r['pg'] == pg and (not typs or r['typ'] in typs)], key=lambda r: -(r['dec'] or r['vol'] or 0))[:lim]
    out = ''.join(f"<li>{E(r['kw'])}<span>{'Vol ' + format(r['vol'], ',') if r['vol'] else '待 KP'}{' · 12 月 ' + format(r['dec'], ',') if r['dec'] else ''}</span></li>" for r in rs)
    return f'<ul class="kw">{out}</ul>'

def num(pg):
    c, v, d = stats(pg)
    return f'<div class="num"><div><b>{c}</b><small>關鍵字</small></div><div><b>{v:,}</b><small>平均月搜合計</small></div><div><b>{d:,}</b><small>2025 年 12 月搜尋合計</small></div></div>'

def card(pg, status, seo, outline, notes, links):
    name, url = PAGES[pg]
    u = f'<a href="{P}{url}" target="_blank">{E(url)}</a>' if url.startswith('/') else E(url)
    s = ''.join(f'<p><small>{a}</small>{b}</p>' for a, b in seo)
    o = ''.join(f'<li>{x}</li>' for x in outline)
    nt = ''.join(f'<li>{x}</li>' for x in notes)
    ln = ''.join(f'<span class="ln">{x}</span>' for x in links)
    return f'''<div class="pc big" id="{pg}" data-pg="{pg}"><div class="ph"><b>{pg}</b><span class="st">{status}</span><a class="anc" href="#{pg}" title="複製這頁的連結">🔗</a></div>
<h3>{name}</h3><p class="u">{u}</p>{num(pg)}
<div class="two"><div><h4>建議 SEO 設定</h4><div class="seo">{s}</div><h4>主攻字</h4>{kwli(pg, ('主要', '次要'))}</div>
<div><h4>建議內容架構</h4><ol class="out">{o}</ol><h4>注意</h4><ul class="iss">{nt}</ul></div></div>
<div class="lns">{ln}</div><button class="more" data-pg="{pg}">查看全部關鍵字 ↓</button></div>'''

LP = card('LP', '交易型｜11 月 10 日前上線', [
  ('H1', '聖誕到會套餐 2026｜公司聖誕派對及家庭聚會到會'),
  ('SEO Title', '聖誕到會 2026｜聖誕派對套餐・聖誕外賣全港送貨｜Kitchen AO'),
  ('Meta Description', 'Kitchen AO 2026 聖誕到會套餐，適合公司聖誕派對及家庭聚會，按人數選擇，全港送貨。平安夜及聖誕節送貨時段有限，建議提早預訂。'),
  ('Focus Keyword', '<mark>聖誕到會</mark>（副：聖誕到會套餐、聖誕外賣、聖誕派對食物）')], [
  '頁頂 150 至 300 字：聖誕到會套餐、適合人數、截單及送貨時段',
  '聖誕套餐列表（產品分類本身）',
  '公司聖誕派對到會：連去公司到會頁',
  '平安夜及聖誕節送貨安排：連去送貨需知',
  '常見問題（FAQPage schema）：要提早幾多預訂、可否指定時間、有沒有素食'], [
  '類似現有的 Halloween 萬聖節狂嘩套餐分類，用產品分類頁做 Landing page，網址建議不帶年份，每年沿用。',
  '只寫真實資料：2026 聖誕套餐、價錢、截單日期及早鳥優惠（如有）。',
  '「聖誕到會」Semrush 1,000 搜尋量，GSC 265 曝光、第 16.7 名；Kama 第 9 名、Bear 第 4 名。'],
  ['← 聖誕 Blog', '→ 公司到會', '→ 送貨需知', '→ 報價查詢'])
LPEN = card('LP-EN', '交易型｜英文版', [
  ('H1', 'Christmas Catering Hong Kong 2026: Party Sets for Offices and Families'),
  ('SEO Title', 'Christmas Catering Hong Kong 2026 | Xmas Party Sets | Kitchen AO'),
  ('Meta Description', 'Kitchen AO Christmas catering sets for office parties and family gatherings, by number of guests, with delivery across Hong Kong. Book early for Christmas Eve and Christmas Day.'),
  ('Focus Keyword', '<mark>christmas catering hong kong</mark>（副：xmas catering、xmas party catering）')], [
  '英文頁頂介紹（用 English SEO 方格及 English H1 欄）',
  '聖誕套餐列表',
  'Office Christmas party catering：連去 /en/corporate-catering-hk/',
  'Christmas Eve and Christmas Day delivery：連去 /en/delivery/',
  'FAQ'], [
  'Blog 只有中文版，所有英文聖誕字由這頁負責。',
  '「christmas catering」12 月 590 搜尋量；Kama 第 11 名、Bear 第 18 名。'],
  ['→ /en/corporate-catering-hk/', '→ /en/delivery/'])
BLOG = card('BLOG', '資訊型｜11 月中前改寫', [
  ('H1', '香港人聖誕餐吃甚麼？2026 聖誕大餐、到會及派對食物全攻略'),
  ('SEO Title', '聖誕大餐吃甚麼？2026 香港聖誕餐、聖誕到會及派對食物推介｜Kitchen AO'),
  ('Meta Description', '2026 香港聖誕大餐怎樣選？按到會派對、快餐套餐、酒店聖誕大餐、火鍋及自家煮整理預算及人數，附經典聖誕食物、派對食物清單及預訂貼士。'),
  ('Focus Keyword', '<mark>聖誕大餐</mark>（副：聖誕小食、火雞、聖誕食品）')], [
  '30 秒速覽：50 字直接答案＋表（場景／人數／預算／提早幾多預訂）',
  '聖誕到會派對套餐：連去聖誕 Landing page',
  '快餐聖誕套餐：只寫類別，不寫品牌',
  '西餐廳及酒店聖誕大餐：外出或外帶',
  '冬日火鍋及打邊爐',
  '自家煮聖誕餐：火雞、焗豬手、烤牛肉',
  '經典聖誕食物一覽：火雞、薑餅人、樹幹蛋糕、聖誕布甸（中英對照）',
  '聖誕派對食物推介：派對食物清單，有售的連去產品頁',
  '香港人訂聖誕餐的習慣：提早預訂、平安夜送貨時段',
  '常見問題（FAQPage schema）：聖誕大餐幾錢、火雞夠幾多人吃、幾時要訂'], [
  '沿用現有網址，保留舊有排名；標題由「聖誕到會2025」改為主攻「聖誕大餐」，交易字交給 Landing page。',
  '「聖誕大餐」平均月搜 1,300，2025 年 11 月 2,400、12 月 12,100；「聖誕小食」12 月 3,600。',
  '派對食物字（瑞士雞翼、迷你漢堡等）放在清單或表格，不逐個寫段落；下表「Kitchen AO 有售」一欄列出可連去的產品。',
  '對手品牌字（快餐、連鎖店）不寫品牌名、不放連結。'],
  ['→ 聖誕 Landing page', '→ 單點小食', '→ 甜品', '→ 公司到會'])
XC = f'''<div class="pc" id="X" data-pg="X"><div class="ph"><b>X</b><span class="st">不放</span><a class="anc" href="#X" title="複製這頁的連結">🔗</a></div>
<h3>不放：對手品牌字及無關字</h3>{num('X')}<ul class="iss"><li>對手品牌字（快餐及連鎖店聖誕套餐）搜尋量大多只有每月 10 至 170，而且會幫對手做 SEO。</li><li>canapes 已分配給商務活動頁；感恩節、聖誕 event 和聖誕到會無關。</li></ul>{kwli('X', None, 6)}<button class="more" data-pg="X">查看全部 ↓</button></div>'''

CSS = open(os.path.join(HERE, 'core-kw.css'), encoding='utf-8').read() + DCSS + '''
.pc{scroll-margin-top:16px}.pc .anc{margin-left:auto;text-decoration:none;font-size:15px;opacity:.55}.pc .anc:hover{opacity:1}.pc.hit{outline:3px solid #C8A24A;outline-offset:2px}
.copied{position:fixed;bottom:20px;left:50%;transform:translateX(-50%);background:#1A1A1A;color:#F7CE46;padding:8px 16px;border-radius:20px;font-size:14px;z-index:9}'''
JS = r'''const sel=document.getElementById('pg'),typ=document.getElementById('typ');
Object.entries(D.pages).forEach(([k,v])=>{const o=document.createElement('option');o.value=k;o.textContent=k+' '+v;sel.appendChild(o)});
[...new Set(D.rows.map(r=>r.typ))].forEach(t=>{const o=document.createElement('option');o.value=t;o.textContent=t;typ.appendChild(o)});
const f=x=>x==null||x===''?'':Number(x).toLocaleString();
const C=[['kw','關鍵字'],['pg','頁面'],['typ','角色'],['lang','語言'],['vol','平均月搜'],['nov','2025 年 11 月'],['dec','2025 年 12 月'],['m3','3 個月變化 %'],['gi','GSC 曝光'],['gp','GSC 排名'],['prod','Kitchen AO 有售'],['src','來源'],['use','用法']];
const NUM=['vol','nov','dec','m3','gi','gp'];let sk='dec',sd=-1,cur=[];
function draw(){const pg=sel.value,tp=typ.value,q=document.getElementById('q').value.trim().toLowerCase();
let rs=D.rows.filter(r=>(!pg||r.pg===pg)&&(!tp||r.typ===tp)&&(!q||r.kw.toLowerCase().includes(q)));
rs.sort((a,b)=>{let x=a[sk],y=b[sk];if(NUM.includes(sk)){if(x==null&&y==null)return 0;if(x==null)return 1;if(y==null)return -1;return (x-y)*sd}return String(x||'').localeCompare(String(y||''),'zh-HK')*sd});cur=rs;
document.getElementById('tb').innerHTML='<tr>'+C.map(([k,t])=>`<th class="s${sk===k?' on':''}" data-k="${k}">${t} <i>${sk===k?(sd>0?'▲':'▼'):'⇅'}</i></th>`).join('')+'</tr>'+
rs.map(r=>'<tr>'+C.map(([k])=>NUM.includes(k)?`<td class=n>${f(r[k])}</td>`:k==='kw'&&(r.typ==='主要')?`<td><mark>${r.kw}</mark></td>`:k==='prod'&&r.purl?`<td><a href="${r.purl}" target="_blank">${r.prod}</a></td>`:`<td>${r[k]??''}</td>`).join('')+'</tr>').join('');
document.querySelectorAll('#tb th.s').forEach(t=>t.onclick=()=>{const k=t.dataset.k;if(sk===k)sd=-sd;else{sk=k;sd=NUM.includes(k)?-1:1}draw()});
document.getElementById('cnt').textContent=rs.length+' 項';}
['pg','typ'].forEach(i=>document.getElementById(i).onchange=draw);document.getElementById('q').oninput=draw;
document.getElementById('dl').onclick=()=>{const esc=v=>{v=v==null?'':String(v);return /[",\n]/.test(v)?'"'+v.replace(/"/g,'""')+'"':v};const L=[C.map(c=>c[1]).map(esc).join(',')].concat(cur.map(r=>C.map(([k])=>r[k]).map(esc).join(',')));const b=new Blob(['﻿'+L.join('\n')],{type:'text/csv'});const a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='xmas-kw.csv';a.click();};
document.querySelectorAll('.more').forEach(b=>b.onclick=()=>{sel.value=b.dataset.pg;draw();document.getElementById('all').scrollIntoView({behavior:'smooth'})});
function goHash(){const id=decodeURIComponent(location.hash.slice(1));if(!id)return;const c=document.getElementById(id);if(c&&c.classList.contains('pc')){document.querySelectorAll('.pc.hit').forEach(x=>x.classList.remove('hit'));c.classList.add('hit');c.scrollIntoView({behavior:'smooth'});}if([...sel.options].some(o=>o.value===id)){sel.value=id;draw();}}
document.querySelectorAll('.pc .anc').forEach(a=>a.onclick=e=>{e.preventDefault();history.replaceState(null,'',a.getAttribute('href'));goHash();(navigator.clipboard?navigator.clipboard.writeText(location.href):Promise.reject()).then(()=>{const d=document.createElement('div');d.className='copied';d.textContent='已複製連結';document.body.appendChild(d);setTimeout(()=>d.remove(),1500);}).catch(()=>{});});
window.addEventListener('hashchange',goHash);draw();setTimeout(goHash,200);'''

DATA = json.dumps(dict(rows=rows, pages={k: v[0] for k, v in PAGES.items()}), ensure_ascii=False)
page = f'''<!DOCTYPE html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>聖誕 KW 分配｜Kitchen AO</title><style>{CSS}</style></head><body>
<header><h1>🎄 聖誕 KW 分配（Seasonal › 聖誕節）</h1>
<p>資料：Google Keyword Planner 香港（2025-10 至 2026-09，匯出 10-27）、Semrush HK（10-23）、GSC（10-08）｜2026-10-30 更新｜<a href="./index.html#%E8%81%96%E8%AA%95%E7%AF%80">← 返回聖誕節架構圖</a>｜<a href="./core-pages-kw.html">🏢 核心頁面 KW 分配</a></p></header>
<div class="wrap">
{DSEC(from_index("聖誕節"), "架構圖（聖誕節）", "Landing page 用聖誕套餐分類（類似萬聖節狂嘩套餐分類），原本計劃的 /catering/christmas/ 場景頁暫不做。")}
<div class="rule"><b>分工：</b>交易字（聖誕到會、聖誕外賣、聖誕派對食物）由<b>聖誕到會 Landing page</b>負責，11 月 10 日前上線；資訊字（聖誕大餐、聖誕小食、火雞）由<b>改寫後的聖誕 Blog</b>負責，11 月中前完成，再連去 Landing page。英文聖誕字全部交給英文 Landing page（Blog 只有中文版）。對手品牌字不做。<br><b>連結：</b>每張卡右上角 🔗 可複製該頁的獨立網址（例如 <code>xmas-kw.html#BLOG</code>），打開後會自動跳到該頁及篩選關鍵字。</div>
<h2>頁面分配</h2><div class="grid1">{LP}{BLOG}{LPEN}</div>
<div class="grid">{XC}</div>
<h2 id="all">全部關鍵字</h2><div class="card">
<div class="tools"><select id="pg"><option value="">全部頁面</option></select><select id="typ"><option value="">全部角色</option></select><input id="q" placeholder="搜尋關鍵字"><span id="cnt"></span><button class="dl" id="dl">⬇ 下載 CSV</button></div>
<div class="tw"><table id="tb"></table></div>
<p class="foot">平均月搜、11 月、12 月＝GKP（2025 年）；沒有 GKP 數字的用 Semrush；GSC＝曝光／平均排名（近 3 個月，10-08）；Kitchen AO 有售＝可在 Blog 派對食物清單連去的產品頁。</p></div>
</div>
<script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script>
<script>try{{mermaid.initialize({{startOnLoad:true,securityLevel:'loose',flowchart:{{htmlLabels:true,curve:'basis'}}}});}}catch(e){{}}const D={DATA};{JS}</script></body></html>'''
open(os.path.join(HERE, 'xmas-kw.html'), 'w', encoding='utf-8').write(page)
print('rows', len(rows))
for pg in PAGES: print(pg, stats(pg))
