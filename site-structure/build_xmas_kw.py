# -*- coding: utf-8 -*-
"""聖誕 KW 分配頁（Seasonal › 聖誕節）
資料：xmas-kw-sources.json（GKP 香港 2025-10 至 2026-09）、core-kw-sources.json（Semrush 10-23、GSC 10-08）
輸出：xmas-kw.html
"""
import json, re, html, os
from diag_embed import section as DSEC, from_index, CSS as DCSS, nav_html, NAV_CSS, NAV_JS, top_html, TOP_CSS
HERE = os.path.dirname(os.path.abspath(__file__))
X = json.load(open(os.path.join(HERE, 'xmas-kw-sources.json'), encoding='utf-8'))
C = json.load(open(os.path.join(HERE, 'core-kw-sources.json'), encoding='utf-8'))
n = lambda k: re.sub(r'\s+', '', k).lower()
GKP = {n(r['kw']): r for r in X['rows']}
NEW = json.load(open(os.path.join(HERE, 'xmas-gkp-2026-10-31.json'), encoding='utf-8'))   # Xmas (2).xlsx，GKP 2026-10-31
for _k, _v in NEW.items():
    GKP[_k] = dict(kw=_v['kw'], vol=_v['vol'], m3=_v['m3'], nov=_v['nov'], dec=_v['dec'], new=False, gsc=_v.get('src') == 'GSC')
SEM, GSC = C['semrush'], C['gsc']
P = 'https://aoaodelivery.com'
E = html.escape

PAGES = {
 'LP':    ('聖誕到會 Landing page（中文）', '建議新增：/product-category/christmas-set/'),
 'LP-EN': ('聖誕到會 Landing page（英文）', '建議新增：/en/product-category/christmas-set/'),
 'OLD':   ('舊 Blog：聖誕到會（Landing page 上線當日 301）', '/blog/christmas-catering-hong-kong/'),
 'B2':    ('Blog 2｜香港人聖誕餐吃甚麼？聖誕小食及派對食物（新文章＋搵食工具）', '建議新增：/blog/christmas-food-hong-kong/'),
 'X':     ('不放', ''),
}

R = []
def add(pg, typ, kws, lang='中', use=''):
    for k in kws: R.append(dict(kw=k, pg=pg, typ=typ, lang=lang, use=use))

# ---------- Landing page（交易型）----------
add('LP', '主要', ['聖誕到會'], use='H1／Title／頁頂首段')
add('LP', '次要', ['聖誕外賣', '聖誕套餐', '聖誕大餐到會', '聖誕到會套餐', '聖誕派對到會', '公司聖誕派對到會'], use='頁頂內容／H2／Meta')
add('LP', '長尾', ['聖誕到會4人', '聖誕到會6人', '聖誕到會2人', '聖誕二人餐外賣', '一人聖誕餐'], use='按人數的套餐名稱及篩選（例如「4 人聖誕到會套餐」）')
add('LP', '長尾', ['聖誕外賣到會', '聖誕餐到會', '聖誕到會外賣', '聖誕套餐到會', '聖誕party到會', 'christmas到會', 'christmasparty到會', 'xmas到會', '到會聖誕', '聖誕小食到會', '聖誕美食到會', '聖誕食物到會', '聖誕到會餐盒', '聖誕便當到會', '聖誕外賣下午茶', '聖誕海鮮到會', '聖誕套餐 2026'], use='頁頂內容／產品描述／FAQ 自然出現')
add('LP', '長尾', ['聖誕火雞到會', '聖誕到會火雞', '聖誕火雞套餐', '火雞到會', '火雞訂購', '訂火雞', '火雞餐', '聖誕大餐外賣', '聖誕大餐外送', '聖誕素食餐'], use='只在有真實產品時使用（例如有火雞套餐才寫火雞字）')
add('LP-EN', '主要', ['christmas catering hong kong'], lang='EN', use='EN H1／Title')
add('LP-EN', '次要', ['christmas catering', 'xmas catering', 'xmas party catering', 'xmas lunch'], lang='EN', use='EN 頁頂內容／Meta')
add('LP-EN', '長尾', ['turkey hk', 'roast turkey hong kong', 'turkey catering hong kong', 'order turkey online', 'christmas bbq menu'], lang='EN', use='EN 產品名／FAQ')
# ---------- 舊 Blog 1 已併入 Landing page（301）----------
add('LP', '次要', ['聖誕節到會', '聖誕到會推介', '聖誕到會餐單'], use='H2「聖誕到會推介：按場合揀套餐」／套餐餐單（由舊 Blog 1 併入）')
add('B2', '長尾', ['聖誕到會酒店', '酒店聖誕到會', '聖誕酒店到會', '酒店聖誕外賣', '聖誕酒店外賣', '聖誕外賣酒店', '酒店火雞'], use='H2「香港人聖誕餐的 5 個場景」酒店一節（只寫類別，不寫酒店名）')
# ---------- Blog 2（新文章：資訊型）----------
add('B2', '主要', ['聖誕小食'], use='Title／H1／首段（H1 以「香港人聖誕餐吃甚麼？」開頭）')
add('B2', '次要', ['聖誕餐', '聖誕派對食物', '聖誕派對小食', '聖誕party小食', 'christmasparty食物', '聖誕晚餐', '聖誕大餐', '聖誕大餐吃什麼'], use='H1／30 秒速覽／H2「香港人聖誕餐的 5 個場景」')
add('B2', '次要', ['聖誕大餐食譜', '聖誕火雞', '聖誕小食diy', '簡易聖誕小食'], use='H2「在家吃聖誕大餐：自己煮還是訂到會？」／H2「簡易聖誕小食」')
add('B2', '長尾', ['聖誕大餐自己煮', '聖誕小食食譜', '聖誕派對小食食譜', '聖誕簡易小食', '聖誕健康小食', '聖誕大餐食物', '港式聖誕大餐', '茶餐廳聖誕大餐', '聖誕節火雞', '火雞聖誕', '聖誕火雞餐', '聖誕食火雞', '火雞聖誕大餐', '聖誕火雞大餐', '聖誕大餐火雞', '聖誕節火雞大餐', '火雞自助餐', '聖誕火雞餐廳'], use='H3／FAQ（火雞夠幾多人吃、自家煮還是訂到會）')
add('B2', '次要', ['火雞', '薑餅人', '聖誕蛋糕', '聖誕曲奇', '聖誕甜品', '薑餅屋', '聖誕朱古力'], use='H2「聖誕主菜」／H2「聖誕甜品」／FAQ（火雞夠幾多人吃）')
add('B2', '長尾', ['聖誕食品', '聖誕節美食', '聖誕節菜式', '聖誕糖果', '拐杖糖', '聖誕布甸', '樹幹蛋糕', '聖誕冬甩', '聖誕馬卡龍', '聖誕杯子蛋糕', '聖誕泡芙', '聖誕可麗露', '聖誕布朗尼', '聖誕雪人蛋糕', '意大利聖誕麵包', '史多倫麵包', '肉餡餅', '簡單聖誕甜品', '糖霜曲奇', '薑餅曲奇', '聖誕軟餐'], use='H3／經典聖誕食物表')
add('B2', '長尾', ['panettone', 'gingerbread man', 'gingerbread house', 'christmas cake', 'candy cane', 'mince pie', 'christmas cookies', 'stollen', 'christmas dessert', 'yule log cake'], lang='EN', use='中文 Blog 內以括號寫英文名，例如「意大利聖誕麵包（Panettone）」（Blog 沒有英文版）')
PARTY = ['瑞士雞翼', '蜜汁雞翼', '烤雞翼', '水牛城雞翼', '薯角', '菠蘿腸仔', '迷你漢堡', '一口漢堡', 'sliders', '炸蝦多士', '一口多士', '沙嗲牛肉串', '沙嗲雞肉串', '照燒雞肉串',
         '凱撒沙律', '薯仔沙律', '雜果沙律', '蝦沙律', '蔬菜條沙律', 'popcorn chicken', '爆谷雞', '炸雞粒', '墨西哥脆片', '煙三文魚卷', '煙三文魚脆餅', '泡芙塔',
         '芝士條', '炸蟹鉗', '椒鹽蝦', '椒鹽魷魚', '炸魷魚圈', '炸洋蔥圈', '炸廣島蠔', '炸莫札瑞拉芝士', '笑臉薯餅', '芝士肉丸', '瑞典肉丸', '黑椒牛柳粒', '蒜蓉牛柳粒',
         '蛋沙律三文治', '吞拿魚三文治', '一口三文治', '碎蛋牛角包', '迷你牛角包', '迷你熱狗', '香腸卷', 'sausage rolls', 'pigs in blankets', '煙肉包腸仔', '迷你鹹批', 'quiche',
         '蜜瓜火腿', '風乾火腿拼盤', '冷肉拼盤', 'charcuterie board', '芝士拼盤', '忌廉芝士餅乾', 'bruschetta', '法式麵包脆片', '焗青口', 'prawn cocktail', '雞尾酒蝦', '鮮蝦杯',
         '煙肉卷帶子', 'bacon wrapped scallops', '水果串', '焗棉花糖', 'brownie', '布朗尼', '心太軟', '熔岩朱古力蛋糕', '松露朱古力', '蘋果批', '肉桂卷']
for k in PARTY:
    add('B2', '搵食工具食物', [k], lang='EN' if re.match(r'^[a-z ]+$', k) else '中', use='搵食工具卡片及「聖誕小食推介」清單，有售的連去產品頁')
# ---------- 不放 ----------
add('X', '不放', ['canapes'], lang='EN', use='已分配給商務活動頁（canapés）')
add('X', '不放', ['感恩節火雞訂購', '聖誕event'], use='和聖誕到會無關')
add('X', '不放', ['聖誕禮物公司', '公司聖誕禮物', '聖誕party遊戲', '聖誕partygame', '聖誕派對遊戲', '公司聖誕抽獎禮物', '聖誕禮物公司抽獎', '聖誕公司禮物', '公司聖誕交換禮物', '聖誕派對禮物'], use='另一主題（禮物／遊戲），可留作日後 Blog')
add('X', '不放', ['大快活聖誕到會', '聖誕到會大快活', 'delifrance聖誕到會', 'delifrance聖誕套餐', '意粉屋聖誕到會', '銀杏館聖誕到會', 'spaghettihouse聖誕到會', '一田聖誕到會', '太興聖誕到會', '大家樂聖誕火雞', '大快活聖誕火雞'], use='對手品牌字，不寫品牌名、不放連結')
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
    if g: src.append('GKP' + ('（Ads 搜尋字新增）' if g.get('new') else '') + ('（GSC 有曝光）' if g.get('gsc') else ''))
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
  '頁頂 150 至 300 字：聖誕到會套餐 2026、適合人數、截單日期及送貨時段（「聖誕到會」放在首段 100 字內）',
  '聖誕到會推介：按場合揀套餐（公司、家庭、小朋友、素食），承接舊 Blog 1 的「聖誕到會推介」「聖誕節到會」',
  '按人數揀聖誕套餐：2 人、4 人、6 人、10 人、20 人以上（承接「聖誕到會4人」12 月 480 搜尋）',
  '聖誕套餐列表（產品分類本身），每個套餐寫明人數、每位價錢及菜式',
  '聖誕小食加配：連去單點小食、甜品及 Blog 2 搵食工具',
  '公司聖誕派對到會：連去公司到會頁',
  '平安夜及聖誕節送貨安排、截單日期：連去送貨需知',
  '常見問題（FAQPage schema）：要提早幾多預訂、平安夜可否送貨、有沒有火雞、可否加素食'], [
  '用產品分類頁做 Landing page（類似萬聖節狂嘩套餐分類），網址不帶年份，每年沿用。上線當日把舊 Blog「聖誕到會」301 轉到這頁。',
  'GKP 10-31：「聖誕到會」平均月搜 1,000，2025 年 11 月 3,600、12 月 8,100；「聖誕外賣」及「聖誕派對食物」12 月各 1,300；「聖誕套餐」12 月 880。11 月起急升，所以要 11 月 10 日前上線。',
  '對手做法（只作參考，頁面不寫品牌）：連鎖快餐及餐廳聖誕套餐約每位 HK$70 至 200，套餐按人數由 2 至 35 人；常見賣點是早鳥折扣（12 月中前預訂）、原隻燒火雞、滿額送贈品及熱食送到樓下。Kitchen AO 可突出食物質素、按人數配搭及全港送貨。',
  '只寫真實資料：2026 聖誕套餐、價錢、截單日期、早鳥優惠及火雞（如有）。'],
  ['← Blog 2 搵食工具', '← 舊 Blog 301', '→ 公司到會', '→ 送貨需知', '→ 報價查詢'])
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
B2 = card('B2', '資訊型＋搵食工具｜新文章｜11 月中前上線', [
  ('H1', '香港人聖誕餐吃甚麼？2026 聖誕小食、派對食物及聖誕大餐推介（附搵食工具）'),
  ('SEO Title', '聖誕小食推介 2026｜香港人聖誕餐吃甚麼？派對食物搵食工具｜Kitchen AO'),
  ('Meta Description', '香港人聖誕餐吃甚麼？2026 聖誕小食、派對食物、火雞及聖誕甜品一次看，用搵食工具按人數、預算及口味篩選，附在家吃聖誕大餐及預訂貼士。'),
  ('Focus Keyword', '<mark>聖誕小食</mark>（副：聖誕餐、聖誕派對食物、聖誕大餐）')], [
  '30 秒速覽：香港人聖誕餐吃甚麼？50 字直接答案＋表（場景／常見食物／人數／預算／提早幾多預訂）',
  '🔍 聖誕食物搵食工具：按類別（小食／主菜／甜品／飲品）、人數、預算、素食、小朋友篩選，有售的連去產品頁',
  '聖誕小食推介：鹹點及 Finger Food（瑞士雞翼、迷你漢堡、蝦多士等）',
  '聖誕主菜：火雞、燒牛肉、焗豬手（附「火雞夠幾多人吃」）',
  '聖誕甜品：薑餅人、樹幹蛋糕、聖誕布甸、Panettone（中英對照）',
  '香港人聖誕餐的 5 個場景：到會派對、快餐套餐、酒店及餐廳、火鍋打邊爐、自己煮（只寫類別，不寫品牌）',
  '在家吃聖誕大餐：自己煮還是訂到會？（承接聖誕大餐、聖誕大餐食譜）',
  '簡易聖誕小食 DIY：3 至 5 款簡單做法',
  '香港人訂聖誕餐的習慣：提早預訂、平安夜送貨時段 → CTA 聖誕到會套餐',
  '常見問題（FAQPage schema）：聖誕小食有甚麼、火雞夠幾多人吃、聖誕大餐在家吃甚麼、幾時要訂'], [
  '整合原本「香港人聖誕餐吃甚麼」及「聖誕小食＋搵食工具」兩個方向：保留場景分類及在家吃聖誕大餐，主攻字改為「聖誕小食」（12 月 3,600，競爭低，首頁沒有專門清單）。',
  '「聖誕大餐」（12 月 12,100）搜尋結果以媒體的酒店及餐廳清單為主，所以只作次要字，放在場景及「在家吃聖誕大餐」兩節。',
  '「聖誕派對食物」（12 月 1,300，競爭低）及約 70 個派對食物字由 Landing page 及舊 Blog 1 移到這篇，成為搵食工具的食物清單。',
  '對手品牌字（快餐、連鎖店）只寫類別，不寫品牌名、不放連結。'],
  ['→ 聖誕 Landing page', '→ 單點小食', '→ 甜品', '→ 公司到會'])
OLDC = f'''<div class="pc" id="OLD" data-pg="OLD"><div class="ph"><b>OLD</b><span class="st">301 轉址｜Landing page 上線當日</span><a class="anc" href="#OLD" title="複製這頁的連結">🔗</a></div>
<h3>舊 Blog：聖誕到會（併入 Landing page）</h3><p class="u"><a href="{P}/blog/christmas-catering-hong-kong/" target="_blank">/blog/christmas-catering-hong-kong/</a></p>
<ul class="iss"><li><b>原因</b>：「聖誕到會推介」首頁全是傳媒的多品牌推介清單（HK01、星島），不寫對手就排不上；只寫自家套餐又和 Landing page 重疊，兩頁會互搶「聖誕到會」。</li>
<li><b>現況</b>：這篇現時為「聖誕到會」排名（GSC 265 曝光、第 16.7 名），301 後排名及連結價值交給 Landing page。</li>
<li><b>Rank Math › Redirections</b>：Source <code>blog/christmas-catering-hong-kong</code>（Exact）→ Destination Landing page 網址 → 301 Permanent Move。</li>
<li><b>時間</b>：Landing page 上線當日才做；之前不要轉址，舊文章繼續保留排名。轉址後到 GSC 用「網址審查」提交 Landing page。</li>
<li>它的關鍵字（聖誕節到會、聖誕到會推介、聖誕到會餐單）已移到 Landing page；酒店聖誕到會比較字移到 Blog 2。</li></ul></div>
'''
XC = f'''<div class="pc" id="X" data-pg="X"><div class="ph"><b>X</b><span class="st">不放</span><a class="anc" href="#X" title="複製這頁的連結">🔗</a></div>
<h3>不放：對手品牌字及無關字</h3>{num('X')}<ul class="iss"><li>對手品牌字（快餐及連鎖店聖誕套餐）搜尋量大多只有每月 10 至 170，而且會幫對手做 SEO。</li><li>canapes 已分配給商務活動頁；感恩節、聖誕 event 和聖誕到會無關。</li></ul>{kwli('X', None, 6)}<button class="more" data-pg="X">查看全部 ↓</button></div>'''

CSS = open(os.path.join(HERE, 'core-kw.css'), encoding='utf-8').read() + DCSS + NAV_CSS + TOP_CSS + '''
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
{top_html('聖誕節')}
<header><h1>🎄 聖誕節：架構圖＋KW 分配</h1>
<p>資料：Google Keyword Planner 香港（2025-10 至 2026-09，10-27 及 10-31 匯出）、Semrush HK（10-23）、GSC（10-08）｜2026-10-31 更新</p></header>
<div class="wrap">
{DSEC(from_index("聖誕節"), "架構圖（聖誕節）", "Landing page 用聖誕套餐分類（類似萬聖節狂嘩套餐分類），原本計劃的 /catering/christmas/ 場景頁暫不做。")}
<div class="rule"><b>分工（10-31 更新）：</b>只有兩頁。<b>聖誕到會 Landing page</b>負責所有訂購及揀套餐字（聖誕到會、聖誕節到會、聖誕到會推介、聖誕外賣、聖誕套餐、聖誕大餐到會），11 月 10 日前上線；<b>Blog 2（新文章＋搵食工具）</b>負責資訊字（聖誕小食、聖誕餐、聖誕派對食物、聖誕大餐、火雞），11 月中前上線，再連去 Landing page。舊 Blog「聖誕到會」在 Landing page 上線當日 301 轉到 Landing page。英文聖誕字全部交給英文 Landing page。對手品牌字不做。<br><b>連結：</b>每張卡右上角 🔗 可複製該頁的獨立網址（例如 <code>xmas-kw.html#B2</code>），打開後會自動跳到該頁及篩選關鍵字。</div>
<h2>頁面分配</h2><div class="grid1">{LP}{B2}{LPEN}</div>
<div class="grid">{OLDC}{XC}</div>
<h2 id="all">全部關鍵字</h2><div class="card">
<div class="tools"><select id="pg"><option value="">全部頁面</option></select><select id="typ"><option value="">全部角色</option></select><input id="q" placeholder="搜尋關鍵字"><span id="cnt"></span><button class="dl" id="dl">⬇ 下載 CSV</button></div>
<div class="tw"><table id="tb"></table></div>
<p class="foot">平均月搜、11 月、12 月＝GKP（2025 年）；沒有 GKP 數字的用 Semrush；GSC＝曝光／平均排名（近 3 個月，10-08）；Kitchen AO 有售＝可在 Blog 派對食物清單連去的產品頁。</p></div>
</div>
<script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script>
<script>try{{mermaid.initialize({{startOnLoad:true,securityLevel:'loose',flowchart:{{htmlLabels:true,curve:'basis'}}}});}}catch(e){{}}const D={DATA};{JS}</script>{NAV_JS}</body></html>'''
open(os.path.join(HERE, 'xmas-kw.html'), 'w', encoding='utf-8').write(page)
print('rows', len(rows))
for pg in PAGES: print(pg, stats(pg))
