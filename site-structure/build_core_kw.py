# -*- coding: utf-8 -*-
"""核心頁面 KW 分配頁（公司到會、到會推介 + 其他待 review 頁面）
資料：core-kw-sources.json（Semrush HK 2026-10-23、GSC 2026-10-08 近 3 個月、Position Tracking 2026-10-24）
輸出：core-pages-kw.html
"""
import json, re, html, os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = json.load(open(os.path.join(HERE, 'core-kw-sources.json'), encoding='utf-8'))
K, G, PT = SRC['semrush'], SRC['gsc'], SRC['pt']
n = lambda k: re.sub(r'\s+', '', k).lower()

# ---------- 頁面 ----------
PAGES = {
 'CORP': ('公司到會（Annual Dinner）', '/corporate-catering-hk/'),
 'REC':  ('到會推介', '/hong-kong-catering-recommendation/'),
 'HOME': ('首頁', '/'),
 'BIZ':  ('商務活動', '/business-event/'),
 'BOX':  ('商務／員工餐盒分類', '/product-category/商務活動/commercial-lunch-box/'),
 'NB1':  ('新 Blog：Annual Dinner 籌備全攻略', '（建議新增）'),
 'OLD1': ('舊 Blog：到會邊間好', '/blog/hongkong-catering-2026-香港到會邊間好/'),
 'OLD2': ('舊 Blog：到會中伏', '/blog/catering-pitfalls-guide/'),
 'XMAS': ('舊 Blog：聖誕到會', '/blog/christmas-catering-hong-kong/'),
 'X':    ('不放（品牌／論壇／無關）', ''),
 'ABOUT': ('關於我們', '/about-kitchenao/'),
 'FAQ':  ('常見問題', '/常見問題/'),
 'GIFT': ('客製化紀念品', '/客製化紀念品訂製服務/'),
 'RCP':  ('Recipes 食譜', ''),
 'HOME-EN': ('首頁（英文）', '/en/'),
 'CORP-EN': ('公司到會（英文）', '/en/corporate-catering-hk/'),
 'REC-EN':  ('到會推介（英文）', '/en/hong-kong-catering-recommendation/'),
 'BIZ-EN':  ('商務活動（英文）', '/en/business-event/'),
 'BOX-EN':  ('商務／員工餐盒分類（英文）', '/en/product-category/商務活動/commercial-lunch-box/'),
 'PARTY':   ('派對到會套餐分類', '/product-category/party/'),
 'PARTY-EN':('派對到會套餐分類（英文）', '/en/product-category/party/'),
 'XMAS-LP':    ('聖誕到會 Landing page（建議新增）', '（建議新增：聖誕套餐分類）'),
 'XMAS-LP-EN': ('聖誕到會 Landing page（英文）', '（建議新增：/en/ 聖誕套餐分類）'),
}
# 英文字自動分配到英文頁（Blog 只有中文版，英文字改由其他英文頁負責）
EN_PAGE = {'HOME': 'HOME-EN', 'CORP': 'CORP-EN', 'REC': 'REC-EN', 'BIZ': 'BIZ-EN', 'BOX': 'BOX-EN', 'PARTY': 'PARTY-EN',
           'XMAS': 'XMAS-LP-EN', 'XMAS-LP': 'XMAS-LP-EN', 'NB1': 'CORP-EN'}
G30 = json.load(open(os.path.join(HERE, 'gsc-pages-2026-10-30.json'), encoding='utf-8'))
G30N = {pg: {n(k): v for k, v in d['q'].items()} for pg, d in G30.items()}
G30LAB = {'HOME': '中文首頁', 'HOME-EN': '英文首頁', 'CORP*': '公司到會', 'REC*': '到會推介'}
def now30(k):
    hits = [(G30LAB[pg], d[k][1], d[k][2]) for pg, d in G30N.items() if k in d and d[k][1] > 0]
    hits.sort(key=lambda x: -x[1])
    return '；'.join(f'{a} {b:,} 曝光 #{c:g}' for a, b, c in hits) or None

# kw, page, role, lang, src(額外來源), use
R = []
def add(page, role, kws, lang='中', src='', use=''):
    for k in kws: R.append(dict(kw=k, pg=page, typ=role, lang=lang, src=src, use=use))

# 公司到會
add('CORP','主要',['公司到會'],use='H1／Title／首段 100 字內')
add('CORP','次要',['企業到會','公司到會服務','到會服務 公司'],use='H2／首段／Meta')
add('CORP','次要',['annual dinner 到會','年會到會','午餐到會','office lunch 到會'],src='建議',use='H2（Annual Dinner／Office Lunch 段）')
add('CORP','長尾',['公司聚會到會','春茗到會','公司開年飯','公司團年飯','團年飯到會'],src='',use='H3／內文（節日公司活動段）')
add('CORP','FAQ',['公司到會價錢','公司到會要提前多少日預訂','公司到會有沒有素食','公司到會可否開發票'],src='建議',use='FAQ（FAQPage schema）')
add('CORP','主要',['corporate catering hong kong'],lang='EN',use='EN Title／H1（/en/ 版）')
add('CORP','次要',['corporate catering','corporate catering service','corporate catering hk','corporate catering events','office catering hong kong','office lunch delivery','office lunch catering','office lunch catering hong kong','corporate lunch catering hong kong','office party catering hk','office catering'],lang='EN',use='EN 內文／Meta')
add('CORP','長尾',['company annual dinner planning hk','annual dinner planner hk','annual lunch','department dinner'],lang='EN',src='GSC 10-30',use='EN Annual Dinner 段（Blog 只有中文版）')
# 到會推介
add('REC','主要',['到會推介','香港到會推介','到會推介2026'],use='H1／Title／首段 100 字內')
add('REC','次要',['公司到會推介','到會服務推介 2026'],src='GSC 10-30',use='H2「公司活動到會推介」（連去公司到會頁）')
add('REC','次要',['到會推薦','到會服務推介','高級到會推介','高級到會','到會推介評分最高','到會推介 好食','到會推介2022'],use='H2／內文／Meta')
add('REC','長尾',['派對到會推介','party到會推介','派對到會 推介','到會美食','到會專門店','小型到會'],use='H3／推介速覽表')
add('REC','主要',['catering company hong kong'],lang='EN',use='EN Title／H1（/en/ 版）')
add('REC','次要',['catering company hk','catering companies','celebrations catering','best catering hong kong'],lang='EN',use='EN 內文')
# 首頁
add('HOME','主要',['到會','香港到會','到會服務','到會食物'])
add('HOME','次要',['到會公司','到會服務 香港','美食到會','到會套餐','catering 香港'],src='GSC 10-30',use='首頁 H2／首段（首頁已排第 28 至 32 名）')
add('PARTY','主要',['派對到會','party 到會','派對到會套餐','派對食物到會','party food 到會','生日到會','生日到會服務','party到會'],src='GSC 10-30',use='派對分類頁 H1／頁頂內容（現由首頁排第 32 至 53 名）')
add('PARTY','主要',['party food delivery hk','party food delivery','party catering','party catering hk','party catering services','party food hk','food catering for birthday parties','catering party'],lang='EN',src='GSC 10-30',use='EN 派對分類頁')
add('XMAS-LP','主要',['聖誕到會','聖誕到會套餐','聖誕外賣','聖誕派對食物','公司聖誕派對到會','聖誕大餐外賣','聖誕大餐 外送'],src='聖誕策略 10-30',use='聖誕套餐分類 H1／頁頂內容（舊 Blog 改為主攻聖誕大餐）')
add('HOME','主要',['catering','catering hk','catering hong kong','catering service hong kong','catering services','catering 中文'],lang='EN')
add('HOME','次要',['catering service company','catering service provider','food catering services','catering service hk','catered meals','full service catering','affordable catering','food and beverage catering','food catering','catering service'],lang='EN',src='GSC 10-30',use='EN 首頁 H2／內文（現排第 37 至 59 名）')
# 商務活動
add('BIZ','主要',['商務到會','酒會到會','開張到會','宴會到會','酒會'])
add('BIZ','主要',['event catering','finger food catering','canapes catering hong kong'],lang='EN')
# 餐盒
add('BOX','主要',['商務飯盒','商務餐盒','公司飯盒','商務便當','飯盒到會','一人餐盒到會','lunch box 到會','員工餐盒','外賣飯盒','員工飯堂','員工餐廳'])
add('BOX','主要',['lunch set','catering box'],lang='EN')
# 新 blog
add('NB1','主要',['annual dinner'],src='Google 自動完成',use='H1（資訊型，公司到會頁不放）')
add('NB1','次要',['annual dinner 遊戲','公司annual dinner遊戲','annual dinner 抽獎 禮物','annual dinner抽獎禮物','annual dinner 場地','annual dinner 主題','annual dinner theme','annual dinner 表演','年度晚宴遊戲','年會遊戲','春茗遊戲','公司抽獎禮物','公司抽獎禮物推薦','公司派對遊戲','公司團體活動推薦'],use='H2／H3')
add('NB1','次要',['company annual dinner planning hk'],lang='EN',use='EN 版 H1')
# 相關 KW 擴充（2026-10-30 建議，待 KP 查搜尋量）
EXP = '建議擴充（待 KP）'
add('HOME','長尾',['到會外賣','外賣到會','到會食物外賣','香港到會服務','到會服務公司','到會網上訂購','即日到會','到會送貨','到會餐單','到會菜單'],src=EXP,use='首頁內文／FAQ')
add('HOME','長尾',['catering delivery hong kong','food catering hong kong','catering services hong kong','hong kong catering delivery','catering near me','catering company near me','catering menu hong kong'],lang='EN',src=EXP,use='EN 首頁內文')
add('CORP','長尾',['公司午餐到會','公司下午茶到會','辦公室到會','會議到會','公司活動到會','公司週年晚宴到會','公司派對到會','企業午餐','公司到會套餐','公司到會外賣'],src=EXP,use='H3／內文')
add('CORP','長尾',['corporate catering services hong kong','corporate lunch catering','meeting catering hong kong','business catering hong kong','corporate event catering hong kong','annual dinner catering','office lunch delivery hong kong','corporate lunch boxes'],lang='EN',src=EXP,use='EN H3／內文')
add('REC','長尾',['到會推介 香港','到會推薦 2026','高質到會','人氣到會','到會好評','到會比較','到會服務比較','邊間到會好'],src=EXP,use='推介速覽表／FAQ')
add('REC','長尾',['top catering companies hong kong','catering recommendations hong kong','best party catering hong kong','best corporate catering hong kong'],lang='EN',src=EXP,use='EN 內文')
add('PARTY','長尾',['派對到會推薦','派對食物外賣','生日派對到會','生日會到會','小朋友生日會到會','派對外賣','派對套餐'],src=EXP,use='派對分類頁頂內容')
add('PARTY','長尾',['birthday party catering hong kong','kids party catering hong kong','party food catering','party platters hong kong'],lang='EN',src=EXP,use='EN 派對分類頁')
# 舊 blog
add('OLD1','主要',['到會邊間好','平價到會','到會價錢','到會平'],use='重寫時 H1／H2')
add('OLD2','主要',['中伏','到會中伏','到會注意事項'],use='重寫時 H1／H2')
add('XMAS','主要',['聖誕大餐','聖誕到會推介','聖誕小食','聖誕食品','聖誕節到會','聖誕到會餐單','聖誕大餐到會'],use='重寫為「香港人聖誕餐吃甚麼」資訊型（主攻聖誕大餐）；交易字交給聖誕 Landing page')
add('XMAS','主要',['christmas catering hong kong','christmas catering','xmas catering','xmas party catering','new year catering'],lang='EN',use='Blog 沒有英文版 → 英文聖誕 Landing page')
# 不放
add('X','—',['到會推介lihkg','到會推介baby kingdom','到會推介 threads','大家樂到會','大快活到會','pizza hut到會','hku catering','asia pacific catering'],use='論壇／品牌／其他公司，不作目標')

AUTOC = {n(x) for x in ['公司到會推介','到會推介2026','到會推介評分最高','到會推介 好食','到會推介lihkg','到會推介baby kingdom','到會推介 threads',
         'annual dinner','annual dinner 遊戲','annual dinner 抽獎 禮物','annual dinner 場地','annual dinner 主題','annual dinner theme','annual dinner 表演','office lunch catering','到會邊間好']}

def pos(v):
    return v[0] if v else None

XMAS_PG = {'XMAS', 'XMAS-LP', 'XMAS-LP-EN'}
R = [r for r in R if r['pg'] not in XMAS_PG]
rows = []
seen = set()
for r in R:
    k = n(r['kw'])
    if k in seen: continue
    seen.add(k)
    s = K.get(k) or {}
    g = G.get(k)
    pt = PT.get(k)
    srcs = []
    if s: srcs.append('Semrush')
    if g: srcs.append('GSC')
    if k in AUTOC: srcs.append('Google 自動完成')
    if now30(k) and 'GSC' not in srcs: srcs.append('GSC 10-30')
    if r['src'] == '建議' and not srcs: srcs.append('建議（待 KP）')
    if r['src'].startswith('建議擴充'): srcs.insert(0, '建議擴充（待 KP）')
    pgv = EN_PAGE.get(r['pg'], r['pg']) if r['lang'] == 'EN' else r['pg']
    rows.append(dict(kw=r['kw'], pg=pgv, typ=r['typ'], lang=r['lang'], use=r['use'], now=now30(k),
        vol=s.get('vol') or None, kd=s.get('kd'), gi=g[1] if g else None, gp=round(g[2],1) if g and g[2] else None,
        pt=pt if isinstance(pt,(int,float)) else None, ao=pos(s.get('ao')), km=pos(s.get('km')), br=pos(s.get('br')),
        src='、'.join(srcs) or '—'))

# KP 種子字：沒有 Semrush 搜尋量、而且不是「不放」
SEED_PAGES = ['HOME', 'HOME-EN', 'CORP', 'CORP-EN', 'REC', 'REC-EN', 'PARTY', 'PARTY-EN', 'BIZ', 'BIZ-EN', 'BOX', 'BOX-EN', 'NB1', 'OLD1', 'OLD2']
SEEDS = {pg: [r['kw'] for r in rows if r['pg'] == pg] for pg in SEED_PAGES}
SEEDS = {k: v for k, v in SEEDS.items() if v}
seed = [k for v in SEEDS.values() for k in v]

def stats(pg):
    rs = [r for r in rows if r['pg'] == pg]
    return len(rs), sum(r['vol'] or 0 for r in rs), sum(r['gi'] or 0 for r in rs)

E = html.escape
def kwli(pg, lim=8):
    rs = sorted([r for r in rows if r['pg'] == pg], key=lambda r: (-(r['vol'] or 0), -(r['gi'] or 0)))[:lim]
    out = []
    for r in rs:
        m = []
        if r['vol']: m.append(f"Vol {r['vol']:,}")
        if r['gi']: m.append(f"GSC {r['gi']:,}／{r['gp']}")
        if r['pt']: m.append(f"PT {int(r['pt'])}")
        out.append(f"<li>{E(r['kw'])}<span>{' · '.join(m) or '待 KP'}</span></li>")
    return '<ul class="kw">' + ''.join(out) + '</ul>'

def num(pg):
    c, v, g = stats(pg)
    return f'<div class="num"><div><b>{c}</b><small>關鍵字</small></div><div><b>{v:,}</b><small>Semrush Vol 合計</small></div><div><b>{g:,}</b><small>GSC 曝光（3 個月）</small></div></div>'

# ---------- 詳細卡 ----------
CORP_CARD = f'''
<div class="pc big" id="CORP" data-pg="CORP"><div class="ph"><b>CORP</b><a class="anc" href="#CORP" title="複製這頁的連結">🔗</a><span class="st">第一輪｜要重寫</span></div>
<h3>公司到會（Annual Dinner、Office Lunch）</h3>
<p class="u"><a href="https://aoaodelivery.com/corporate-catering-hk/" target="_blank">/corporate-catering-hk/</a>（頁面 ID 18404）</p>
{num('CORP')}
<div class="two"><div><h4>中文版主攻字</h4>{kwli('CORP', 6)}</div><div><h4>英文版（<a href="https://aoaodelivery.com/en/corporate-catering-hk/" target="_blank">/en/corporate-catering-hk/</a>）主攻字</h4>{kwli('CORP-EN', 6)}</div></div>
<div class="two"><div>
<h4>現況（2026-10-27 檢查）</h4>
<ul class="iss">
<li><b>內容太薄</b>：正文約 1,490 字，只有 1 張圖、3 條站內連結。</li>
<li><b>兩個 H1</b>：主題自動輸出的頁面標題，加上內文再寫一個 H1。</li>
<li><b>口語太多</b>：揀、定、搞掂、唔、冇、點樣，要改為書面語。</li>
<li><b>未能核實的宣稱</b>：「星級酒店大廚主理」「專利三重保溫技術」「24 小時內出報價」，以及蟹皇煲仔飯、煙燻牛肋等菜式和 $150／$200／$248／$300 每位價錢。要向營運確認，不能確認的要刪走。</li>
<li><b>內鏈不足</b>：沒有連去商務餐盒、員工餐盒、高級餐盒、九宮格 Canapés、商務活動、報價查詢、合作夥伴。<code>/delivery-info</code> 是轉址連結，要改為 <code>/delivery/</code>。</li>
<li><b>Schema</b>：只有 Article，沒有 Service 和 FAQPage。</li>
<li><b>排名</b>：GSC「公司到會」510 曝光、平均第 29 名；「到會公司」697 曝光、第 31 名；「商務到會」301 曝光、第 32 名。全部在第三頁，零點擊。</li>
</ul></div><div>
<h4>建議 SEO 設定</h4>
<div class="seo"><p><small>H1（內文只留一個）</small>香港公司到會｜Annual Dinner、Office Lunch 及公司聚會到會套餐</p>
<p><small>SEO Title（10-25 已更新）</small>香港公司到會2026｜Annual Dinner、Office Lunch 到會套餐</p>
<p><small>Meta Description（10-25 已更新）</small>Kitchen AO 提供香港公司到會服務，適合 Annual Dinner、Office Lunch、開張及週年活動。按人數及預算安排餐單，全港送貨，歡迎查詢報價。</p>
<p><small>Focus Keyword</small><mark>公司到會</mark>（副：企業到會、annual dinner 到會）</p></div>
<h4>建議 H2 架構</h4>
<ol class="out">
<li>公司到會速覽：一段 40 至 60 字的直接答案，加一個表（活動類型／人數／建議套餐／每位預算／提前預訂日數）。<em>AI Overview 最常引用這類段落</em></li>
<li>Annual Dinner 到會：人數、菜單配搭及時間安排</li>
<li>Office Lunch 及會議午餐：連去商務餐盒、員工餐盒</li>
<li>公司聚會及節日活動：聖誕派對、春茗、團年飯（連去聖誕 Blog）</li>
<li>商務活動及酒會：連去商務活動頁</li>
<li>公司到會價錢怎樣計算？</li>
<li>預訂流程（5 步）及報價查詢 CTA</li>
<li>合作機構及真實案例：連去合作夥伴頁</li>
<li>常見問題（FAQPage schema）</li>
</ol></div></div>
<h4>AI search（GEO）建議</h4>
<ul class="iss g">
<li>每個 H2 開頭先用 1 至 2 句直接回答，再補充細節。</li>
<li>價錢、人數、預訂日數用表格呈現，方便 AI 摘錄。</li>
<li>加入可核實的事實：服務年份、合作機構類別、真實活動照片及日期；頁底寫明「最後更新：2026 年 X 月」。</li>
<li>Annual Dinner 遊戲、抽獎禮物、場地等資訊字（合共約 1,000 搜尋量）不放在這頁，改放新 Blog（NB1），再互相連結。</li>
</ul>
<div class="lns"><span class="ln">→ 商務／員工餐盒分類</span><span class="ln">→ 商務活動</span><span class="ln">→ 報價查詢</span><span class="ln">→ 合作夥伴</span><span class="ln">↔ NB1 Annual Dinner Blog</span><span class="ln">→ 聖誕 Blog</span></div>
<button class="more" data-pg="CORP">查看全部關鍵字 ↓</button></div>'''

REC_CARD = f'''
<div class="pc big" id="REC" data-pg="REC"><div class="ph"><b>REC</b><a class="anc" href="#REC" title="複製這頁的連結">🔗</a><span class="st">第一輪｜要改寫</span></div>
<h3>到會推介</h3>
<p class="u"><a href="https://aoaodelivery.com/hong-kong-catering-recommendation/" target="_blank">/hong-kong-catering-recommendation/</a>（頁面 ID 18621）</p>
{num('REC')}
<div class="two"><div><h4>中文版主攻字</h4>{kwli('REC', 6)}</div><div><h4>英文版（<a href="https://aoaodelivery.com/en/hong-kong-catering-recommendation/" target="_blank">/en/hong-kong-catering-recommendation/</a>）主攻字</h4>{kwli('REC-EN', 6)}</div></div>
<div class="two"><div>
<h4>現況（2026-10-27 檢查）</h4>
<ul class="iss">
<li><b>主字沒有排名</b>：「到會推介」（Semrush 2,400）Kitchen AO 在 100 名以外，Kama 和 Bear 都排第 1。</li>
<li><b>排名分散</b>：「到會推介2022」由派對分類頁排第 38；「到會邊間好」由舊 Blog 爭奪。要按下面的分配表分清楚每頁負責的字。</li>
<li><b>兩個 H1</b>：主題輸出「到會推介」，內文再有一個 H1。</li>
<li><b>HTML 錯誤</b>：「先看活動性質……」這句清單項目被標成 H2，而且開頭有多餘的「&gt;」。</li>
<li><b>轉址連結</b>：<code>/product-category/busines-event/</code> 要改為 <code>/business-event/</code>。</li>
<li><b>口語</b>：「幾多日前」改為「多少日前」。</li>
<li><b>Schema</b>：只有 Article；FAQ 未加 FAQPage schema。</li>
<li>正文約 2,400 字，10-25 已更新 Meta。</li>
</ul></div><div>
<h4>建議 SEO 設定</h4>
<div class="seo"><p><small>H1</small>香港到會推介2026｜按公司活動、生日派對及船河選擇到會套餐</p>
<p><small>SEO Title</small>香港到會推介2026｜公司活動・生日派對・船河到會｜Kitchen AO</p>
<p><small>Meta Description</small>2026 香港到會推介：按公司活動、生日派對、船河及素食需要，比較 Kitchen AO 熱門到會套餐的人數、價錢及預訂時間，附揀選清單及常見問題。</p>
<p><small>Focus Keyword</small><mark>到會推介</mark>（副：香港到會推介、到會推薦）</p></div>
<h4>建議 H2 架構</h4>
<ol class="out">
<li>香港到會推介速覽：一個表（場合／推介套餐／人數／價錢起／連結）。<em>「推介」搜尋意圖要求清單式比較</em></li>
<li>公司活動到會推介：連去公司到會頁</li>
<li>生日派對及兒童到會推介：連去兒童套餐</li>
<li>船河到會推介：連去船河套餐</li>
<li>素食到會推介：連去素食 B1</li>
<li>小型聚會到會推介（2 至 10 人）：連去人數選餐</li>
<li>揀選到會的 5 個準則：連去「到會邊間好」及「到會中伏」舊 Blog</li>
<li>客人評價及真實活動</li>
<li>預訂流程</li>
<li>常見問題（FAQPage schema）</li>
</ol></div></div>
<h4>AI search（GEO）建議</h4>
<ul class="iss g">
<li>速覽表的價錢及人數要和產品頁一致（由產品頁抄，不要估算）。</li>
<li>每個推介段落寫明「適合誰、多少人、預算、需要提前多少日預訂」，AI 回答「到會推介」時較易引用。</li>
<li>加入 Google 評價分數及數量（要真實），並在頁面寫明更新月份。</li>
<li>論壇字（到會推介 lihkg、baby kingdom）不作目標，但可在 FAQ 回應論壇常見疑問。</li>
</ul>
<div class="lns"><span class="ln">→ 公司到會</span><span class="ln">→ 兒童套餐</span><span class="ln">→ 船河套餐</span><span class="ln">→ 素食 B1</span><span class="ln">→ 人數選餐</span><span class="ln">↔ 舊 Blog 到會邊間好</span><span class="ln">↔ 舊 Blog 到會中伏</span></div>
<button class="more" data-pg="REC">查看全部關鍵字 ↓</button></div>'''

def small(pg, title, url, status, notes, cls=''):
    lis = ''.join(f'<li>{x}</li>' for x in notes)
    link = f'<a href="https://aoaodelivery.com{url}" target="_blank">{E(url)}</a>' if url.startswith('/') else E(url)
    kws = kwli(pg, 6) if any(r['pg'] == pg for r in rows) else ''
    more = f'<button class="more" data-pg="{pg}">查看關鍵字 ↓</button>' if kws else ''
    return f'''<div class="pc {cls}" id="{pg}" data-pg="{pg}"><div class="ph"><b>{pg}</b><a class="anc" href="#{pg}" title="複製這頁的連結">🔗</a><span class="st">{status}</span></div>
<h3>{title}</h3><p class="u">{link}</p><ul class="iss">{lis}</ul>{kws}{more}</div>'''

OTHERS = [
 small('HOME','首頁（中文）','/','10-30 新增分配',[
   'GSC 10-30：13,142 曝光、平均第 27 名，近 30 日升 11%。「到會」第 19 名最接近首頁；「到會服務」940 曝光、第 28 名。',
   '新增負責「到會公司」（602 曝光、第 30 名）、「到會服務 香港」「到會套餐」「美食到會」。',
   '首頁不再主攻公司到會、推介及派對字：加內鏈區塊，用「公司到會」「到會推介」「派對到會」作連結文字。']),
 small('HOME-EN','首頁（英文）','/en/','10-30 新增分配',[
   'GSC 10-30：2,046 曝光，128 點擊幾乎全部來自品牌字（kitchen ao 第 1 名）。',
   '負責 catering、catering hong kong、catering services、catering service company／provider（現第 46 至 59 名）。',
   'corporate catering 類字交給英文公司到會頁；英文首頁加內鏈連去 /en/corporate-catering-hk/。']),
 small('PARTY','派對到會套餐分類（中英）','/product-category/party/','10-30 新增',[
   '「派對到會」465 曝光、「生日到會」295 曝光、「party 到會」202 曝光，現時全部由首頁排第 32 至 53 名。',
   '分類頁頂加 150 至 300 字介紹及 FAQ，H1 用「派對到會套餐」。英文版主攻 party food delivery hk、party catering。']),
 small('BIZ','商務活動','/business-event/','下一輪',[
   '和公司到會頁重疊：兩頁都寫「公司到會推介」。建議這頁改為主攻商務活動、酒會、開張、發佈會及 Canapés。',
   '有兩個完全相同的 H2「公司到會推介 開胃菜 Finger Food 和 Canapé\'s 的魅力」。',
   '錯字：「Whastapp」「活動性質及而求」「訂購公司到會時否需要」。',
   'GSC「商務到會」301 曝光、第 32 名；「宴會到會」169 曝光、第 26 名。']),
 small('ABOUT','關於我們（Authority）','/about-kitchenao/','下一輪',[
   '目的：建立 E-E-A-T 及 AI 搜尋信任。加入成立年份、團隊及廚師背景（真實資料）、食物製造廠牌照號碼、合作機構、媒體報道。',
   '加入 Organization schema（logo、地址、電話、sameAs：Facebook、Instagram、Google 商家）。',
   '有兩個 H1（「「關於 Kitchen AO」」及「關於 Kitchen AO」）。',
   '每篇 Blog 加作者簡介並連回這頁。']),
 small('FAQ','常見問題（由 CS 起草）','/常見問題/','下一輪',[
   '建議由 CS 按 5 類收集真實問題：訂購及付款、送貨及運費、餐單及飲食要求、改期及取消、發票及公司客。',
   '每題答案 40 至 80 字，先直接回答；整頁加 FAQPage schema。',
   '和送貨需知、報價查詢頁互相連結；避免和公司到會頁的 FAQ 完全重複。']),
 small('GIFT','客製化紀念品訂製服務','/客製化紀念品訂製服務/','下一輪｜有錯要即改',[
   '<b>現有錯誤</b>：FAQ 2 仍有佔位字「提前 [例如：2-3週] 預訂」，要即時改為實際日數。',
   '網站架構計劃把這頁合併到 /catering/custom-printed-food/，改寫前先決定是否合併。',
   '目標字待做 KW list（客製化紀念品 GSC 有曝光，Semrush 第 29 名）。']),
 small('OLD1','舊 Blog：到會邊間好','/blog/hongkong-catering-2026-香港到會邊間好/','重寫（第二輪）',[
   '負責「到會邊間好、平價到會、到會價錢」，和到會推介頁分工：這篇做比較及揀選準則，到會推介頁做套餐推介。',
   'Kama 和 Bear「到會邊間好」都排第 1。']),
 small('OLD2','舊 Blog：到會中伏','/blog/catering-pitfalls-guide/','重寫（第二輪）',[
   '負責「中伏、到會注意事項」。Semrush「中伏」（320）排第 15 名，GSC 第 12 名，接近第一頁。',
   '連去到會推介及報價查詢。']),
 small('NB1','新 Blog：Annual Dinner 籌備全攻略','（建議新增）','建議新增',[
   '承接 annual dinner 遊戲、抽獎禮物、場地、主題等資訊字，Kama 已用 Blog 排名（annual dinner 遊戲第 9 名）。',
   '文內 CTA 連去公司到會頁。']),
 small('RCP','Recipes 食譜','（未有 URL）','未開始',[
   '要先決定方向：素食食譜已分配給素食 B5；其他食譜（派對小食、節日菜式）要另做 KW list。',
   '建議用 Recipe schema，每篇連去對應的單點或套餐產品。']),
]

# ---------- 擁有權表 ----------
OWN = [
 ('到會、香港到會、到會服務、到會公司、到會套餐、美食到會', '首頁 /', 'catering、catering hong kong、catering services、catering service company／provider', '首頁 /en/', '整站最大字，只由首頁主攻'),
 ('公司到會、企業到會、公司到會服務、annual dinner 到會、年會到會、午餐到會', '公司到會', 'corporate catering hong kong、corporate catering (service)、office catering hong kong、office lunch catering、company annual dinner planning hk', '公司到會 /en/', '交易型服務頁；英文版同時承接 Annual Dinner 英文字'),
 ('到會推介、香港到會推介、到會推薦、公司到會推介、到會服務推介 2026', '到會推介', 'catering company hong kong、catering companies、celebrations catering', '到會推介 /en/', '推介清單；公司字只留一段並連去公司到會'),
 ('派對到會、party 到會、派對到會套餐、生日到會', '派對到會套餐分類', 'party food delivery hk、party catering (services)、food catering for birthday parties', '派對分類 /en/', '產品分類頁；現由首頁排第 32 至 53 名'),
 ('商務到會、酒會、開張、宴會到會、canapés', '商務活動', 'event catering、finger food catering、canapes catering hong kong', '商務活動 /en/', '活動型服務頁'),
 ('商務餐盒、員工餐盒、公司飯盒、商務便當', '商務／員工餐盒分類', 'lunch set、catering box', '餐盒分類 /en/', '產品分類'),
 ('聖誕到會、聖誕大餐等所有聖誕字', '見 🎄 聖誕 KW 分配頁', 'christmas catering 等', '見 🎄 聖誕 KW 分配頁', '已拆到 Seasonal › 聖誕節（xmas-kw.html）'),
 ('到會邊間好、平價到會、到會價錢', '舊 Blog：到會邊間好', '（Blog 只有中文版）', '—', '比較及揀選準則'),
 ('中伏、到會注意事項', '舊 Blog：到會中伏', '（Blog 只有中文版）', '—', '避雷清單'),
 ('annual dinner 遊戲、抽獎禮物、場地、主題', '新 Blog：Annual Dinner', '（Blog 只有中文版，英文字由公司到會 /en/ 負責）', '—', '資訊型'),
]
own_html = '<table class="own"><tr><th>中文關鍵字群</th><th>中文頁</th><th>英文關鍵字群</th><th>英文頁</th><th>頁面角色</th></tr>' + ''.join(f'<tr><td>{E(a)}</td><td><b>{E(b)}</b></td><td>{E(c)}</td><td><b>{E(d)}</b></td><td>{E(e)}</td></tr>' for a,b,c,d,e in OWN) + '</table>'

# ---------- GSC 2026-10-30 對位分析 ----------
def gsc30_html():
    lab = [('HOME','中文首頁 /'),('HOME-EN','英文首頁 /en/'),('CORP*','公司到會（中＋英）'),('REC*','到會推介（中＋英）')]
    tr = ''
    for k, name in lab:
        d = G30[k]['tot']; ch = (d['last30'] - d['prev30']) / d['prev30'] * 100 if d['prev30'] else 0
        tr += f"<tr><td><b>{name}</b></td><td>{d['impr']:,}</td><td>{d['clicks']:,}</td><td>{d['pos']}</td><td>{d['last30']:,} vs {d['prev30']:,}（{ch:+.0f}%）</td></tr>"
    t1 = '<table class="own"><tr><th>頁面</th><th>曝光</th><th>點擊</th><th>平均排名</th><th>近 30 日曝光 vs 前 30 日</th></tr>' + tr + '</table>'
    kws = ['到會公司','公司到會','商務到會','公司到會服務','企業到會','公司到會推介','香港到會推介','派對到會','生日到會','corporate catering','corporate catering service','catering service company','company annual dinner planning hk']
    want = {r['kw']: (PAGES[r['pg']][0]) for r in rows}
    tr = ''
    for kw in kws:
        k = n(kw); cells = []
        for pg in ['HOME','HOME-EN','CORP*','REC*']:
            v = G30N[pg].get(k); cells.append(f"{v[1]:,}／#{v[2]:g}" if v else '—')
        tr += f"<tr><td><b>{E(kw)}</b></td>" + ''.join(f'<td>{c}</td>' for c in cells) + f"<td>{E(want.get(kw,'—'))}</td></tr>"
    t2 = '<table class="own"><tr><th>關鍵字</th><th>中文首頁</th><th>英文首頁</th><th>公司到會</th><th>到會推介</th><th>分配到</th></tr>' + tr + '</table>'
    return f"""<p class="note">GSC 2026-07-28 至 10-27（匯出 10-30）。公司到會及到會推介的數字包括中英文版；曝光／平均排名。</p>{t1}
<h4>自家頁面互搶：公司到會及推介字主要由首頁排名</h4>{t2}
<ul class="iss"><li><b>公司到會頁差不多沒有排名</b>：「公司到會」「到會公司」「企業到會」都由首頁（第 29 至 44 名）及到會推介頁（第 74 至 86 名）排名，公司到會頁沒有出現。新版內文上線後曝光已升 67%。</li>
<li><b>到會推介頁搶錯字</b>：3 個月零點擊，主要排名的是公司到會字（第 75 至 86 名）；「香港到會推介」反而由首頁排第 31 名。改寫時要刪減公司內容，主攻推介、推薦、邊間好。</li>
<li><b>派對字由首頁排名</b>：「派對到會」465 曝光、「生日到會」295 曝光，應交給派對到會套餐分類頁。</li>
<li><b>英文首頁只有品牌字有點擊</b>：catering service company（第 52 名）、corporate catering service（第 37 名）等，要用英文公司到會頁及首頁內鏈分流。</li>
<li><b>行動</b>：首頁加內鏈區塊（「公司到會」「到會推介」「派對到會」作連結文字），英文首頁同樣用 corporate catering、party catering 連去英文頁。</li></ul>"""

from diag_embed import N as DN, mm as DMM, section as DSEC, CSS as DCSS
_old1 = '/blog/hongkong-catering-2026-e9-a6-99-e6-b8-af-e5-88-b0-e6-9c-83-e9-82-8a-e9-96-93-e5-a5-bd/'
MERMAID = DMM('LR', [
 DN('H', '首頁（HOME／HOME-EN）', '/', 'ok', '首頁'),
 DN('CORP', 'CORP｜公司到會（Annual Dinner）', '/corporate-catering-hk/', 'old', '服務頁'),
 DN('REC', 'REC｜到會推介', '/hong-kong-catering-recommendation/', 'old', '服務頁'),
 DN('PARTY', 'PARTY｜派對到會套餐分類', '/product-category/party/', 'ok', '產品分類頁'),
 DN('BIZ', 'BIZ｜商務活動', '/business-event/', 'old', '服務頁'),
 DN('BOX', 'BOX｜商務餐盒', '/product-category/商務活動/commercial-lunch-box/', 'ok', '產品分類頁'),
 DN('EXE', '高級餐盒', '/product-category/商務活動/executive-premium-meal-box/', 'ok', '產品分類頁'),
 DN('Q', '報價查詢', '/catering-quote-enquiry/', 'ok', '支援頁（報價）'),
 DN('P', '合作夥伴與服務實績', '/合作伙伴/', 'ok', '信任頁'),
 DN('ABOUT', 'ABOUT｜關於我們（Authority）', '/about-kitchenao/', 'old', '信任頁'),
 DN('FAQ', 'FAQ｜常見問題（CS 起草）', '/常見問題/', 'old', '支援頁'),
 DN('GIFT', 'GIFT｜客製化紀念品訂製服務', '/客製化紀念品訂製服務/', 'old', '服務頁'),
 DN('OLD1', 'OLD1｜舊 Blog：到會邊間好', _old1, 'old', 'Blog 文章'),
 DN('OLD2', 'OLD2｜舊 Blog：到會中伏', '/blog/catering-pitfalls-guide/', 'old', 'Blog 文章'),
 DN('NB1', 'NB1｜新 Blog：Annual Dinner 籌備', '', 'new', '計劃中'),
 DN('DL', '送貨需知', '/delivery/', 'ok', '支援頁'),
], ['H -- "內鏈區塊：公司到會" --> CORP', 'H -- "內鏈區塊：到會推介" --> REC', 'H -- "內鏈區塊：派對到會" --> PARTY',
 'REC -. "CTA：公司活動到會推介" .-> CORP', 'REC -. "CTA：派對套餐" .-> PARTY', 'REC <--> OLD1', 'REC <--> OLD2',
 'CORP -. "卡片：Office Lunch" .-> BOX', 'CORP -. "卡片：Meeting Lunch" .-> EXE', 'CORP -. "卡片：酒會開張" .-> BIZ',
 'CORP -. "CTA：到會報價查詢" .-> Q', 'CORP -. "合作夥伴與服務實績" .-> P', 'CORP -. "運費及免運費" .-> DL',
 'NB1 -. "CTA：公司到會" .-> CORP', 'BIZ -. "CTA：報價" .-> Q', 'GIFT -. "CTA：報價" .-> Q',
 'FAQ -. "送貨問題" .-> DL', 'FAQ -. "公司客問題" .-> CORP', 'ABOUT -. authority .-> CORP & REC'])

DATA = json.dumps(dict(rows=rows, pages={k: v[0] for k, v in PAGES.items()}), ensure_ascii=False)
SEED = '\n'.join(seed)
def seed_html():
    tabs = ''.join(f'<button class="sd" data-k="{k}">{E(PAGES[k][0])}（{len(v)}）</button>' for k, v in SEEDS.items())
    areas = ''.join(f'<textarea class="seedt" id="seed-{k}" readonly hidden>{E(chr(10).join(v))}</textarea>' for k, v in SEEDS.items())
    return f'<div class="seedtabs"><button class="sd on" data-k="ALL">全部核心頁面（{len(seed)}）</button>{tabs}</div><textarea class="seedt" id="seed-ALL" readonly>{E(SEED)}</textarea>{areas}'

CSS = open(os.path.join(HERE, 'core-kw.css'), encoding='utf-8').read() + DCSS + '\n.seedtabs{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0}.seedtabs .sd{border:1px solid #E3D9C4;background:#fff;border-radius:16px;padding:4px 12px;font-size:13px;cursor:pointer}.seedtabs .sd.on{background:#1A1A1A;color:#F7CE46;border-color:#1A1A1A}textarea.seedt{width:100%;height:220px;box-sizing:border-box}\n.pc{scroll-margin-top:16px}.pc .anc{margin-left:auto;text-decoration:none;font-size:15px;opacity:.55}.pc .anc:hover{opacity:1}.pc.hit{outline:3px solid #C8A24A;outline-offset:2px}.copied{position:fixed;bottom:20px;left:50%;transform:translateX(-50%);background:#1A1A1A;color:#F7CE46;padding:8px 16px;border-radius:20px;font-size:14px;z-index:9}'
JS = open(os.path.join(HERE, 'core-kw.js'), encoding='utf-8').read().replace("document.getElementById('seed')","document.querySelector('textarea.seedt:not([hidden])')") + '''
document.querySelectorAll('.seedtabs .sd').forEach(b=>b.onclick=()=>{document.querySelectorAll('.seedtabs .sd').forEach(x=>x.classList.toggle('on',x===b));document.querySelectorAll('textarea.seedt').forEach(a=>a.hidden=a.id!=='seed-'+b.dataset.k);});
function goHash(){const id=decodeURIComponent(location.hash.slice(1));if(!id)return;const c=document.getElementById(id);const opt=[...sel.options].some(o=>o.value===id);if(!(c&&c.classList.contains('pc'))){if(opt){sel.value=id;draw();document.getElementById('all').scrollIntoView({behavior:'smooth'});}return;}document.querySelectorAll('.pc.hit').forEach(x=>x.classList.remove('hit'));c.classList.add('hit');c.scrollIntoView({behavior:'smooth'});if([...sel.options].some(o=>o.value===id)){sel.value=id;draw();}}
document.querySelectorAll('.pc .anc').forEach(a=>a.onclick=e=>{e.preventDefault();history.replaceState(null,'',a.getAttribute('href'));goHash();const u=location.href;(navigator.clipboard?navigator.clipboard.writeText(u):Promise.reject()).then(()=>{const d=document.createElement('div');d.className='copied';d.textContent='已複製連結';document.body.appendChild(d);setTimeout(()=>d.remove(),1500);}).catch(()=>{});});
window.addEventListener('hashchange',goHash);setTimeout(goHash,300);'''

page = f'''<!DOCTYPE html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>核心頁面 KW 分配｜Kitchen AO</title><style>{CSS}</style></head><body>
<header><h1>🏢 核心頁面 KW 分配（公司到會、到會推介＋其他待 review 頁面）</h1>
<p>資料：Semrush Organic Positions HK（2026-10-23，Kitchen AO／Kama／Bear）、GSC 近 3 個月（2026-10-08；首頁、公司到會、到會推介 2026-10-30）、Position Tracking（2026-10-24）、Google 自動完成｜<a href="./index.html">← 返回網站架構圖</a>｜<a href="./xmas-kw.html">🎄 聖誕 KW 分配</a></p></header>
<div class="wrap">
{DSEC(MERMAID, "架構圖（中文版；英文版 /en/ 結構相同）", "包括公司到會、到會推介、商務活動、關於我們、常見問題、客製化紀念品及相關 Blog。")}
<div class="rule"><b>分配原則：</b>一個關鍵字只分配到一頁。整站大字（到會、catering）只由首頁主攻；「推介」字由到會推介頁負責；公司及 Annual Dinner 交易字由公司到會頁負責；資訊字（遊戲、抽獎、場地）放 Blog；餐盒字留在產品分類；派對字由派對到會套餐分類負責。<br><b>中英文分工（10-30）：</b>每個中文頁有對應的 /en/ 英文頁，英文字分配到英文頁（例如 corporate catering → /en/corporate-catering-hk/）；Blog 只有中文版，所以英文的 Annual Dinner 字交給英文公司到會頁。所有聖誕字（中英）已拆到 <a href="./xmas-kw.html">🎄 聖誕 KW 分配頁</a>（Seasonal › 聖誕節）。架構圖中英文版相同。<br><b>注意：</b>公司到會類大部分字在 Semrush 沒有搜尋量，標示「待 KP」，請用下面的種子字清單在 Keyword Planner 查詢後再更新。</div>

<h2>GSC 對位分析（2026-10-30）</h2><div class="card">{gsc30_html()}</div>
<h2>關鍵字擁有權：中英文頁分工（2026-10-30 更新）</h2><div class="card">{own_html}</div>
<h2>第一輪：公司到會＋到會推介</h2><div class="grid1">{CORP_CARD}{REC_CARD}</div>
<h2>其他待 review 頁面</h2><div class="grid">{''.join(OTHERS)}</div>
<h2 id="all">全部關鍵字</h2><div class="card">
<div class="tools"><select id="pg"><option value="">全部頁面</option></select><select id="lang"><option value="">中＋EN</option><option>中</option><option>EN</option></select><input id="q" placeholder="搜尋關鍵字"><span id="cnt"></span><button class="dl" id="dl">⬇ 下載 CSV</button></div>
<div class="tw"><table id="tb"></table></div>
<p class="foot">現時排名頁＝GSC 10-30 哪一頁有曝光（曝光 #平均排名）；Vol／KD＝Semrush HK；GSC＝曝光／平均排名（近 3 個月）；PT＝Position Tracking 10-24 排名（Desktop）；AO／Kama／Bear＝Semrush 排名。空白代表沒有數據。</p></div>
<h2 id="kp">Keyword Planner 查詢清單（{len(seed)} 個，全部核心頁面，不含聖誕字）</h2><div class="card">
<p class="note">複製後貼入 Google Keyword Planner ›「取得搜尋量和預測」，地區選香港，匯出 csv 給我更新。</p>
<p class="note">包括首頁、公司到會、到會推介（中英文）、派對分類、商務活動、餐盒分類及相關 Blog 的全部關鍵字，另加 {sum(1 for r in rows if r['src'].startswith('建議擴充'))} 個建議擴充字（來源欄標示「建議擴充」）。聖誕字已移到 🎄 聖誕 KW 分配頁。GKP 每次最多可貼 10,000 個字，可以一次過貼「全部」，或按頁面分開查。</p>
{seed_html()}<button class="dl" id="cp">📋 複製目前清單</button></div>
</div>
<script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script>
<script>const D={DATA};{JS}</script></body></html>'''

open(os.path.join(HERE, 'core-pages-kw.html'), 'w', encoding='utf-8').write(page)
print('rows', len(rows), 'seed', len(seed))
for pg in PAGES: print(pg, stats(pg))
