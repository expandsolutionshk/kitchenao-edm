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
}

# kw, page, role, lang, src(額外來源), use
R = []
def add(page, role, kws, lang='中', src='', use=''):
    for k in kws: R.append(dict(kw=k, pg=page, typ=role, lang=lang, src=src, use=use))

# 公司到會
add('CORP','主要',['公司到會'],use='H1／Title／首段 100 字內')
add('CORP','次要',['企業到會','公司到會服務','公司到會推介','到會服務 公司','到會公司'],use='H2／首段／Meta')
add('CORP','次要',['annual dinner 到會','年會到會','午餐到會','office lunch 到會'],src='建議',use='H2（Annual Dinner／Office Lunch 段）')
add('CORP','長尾',['公司聚會到會','春茗到會','公司開年飯','公司團年飯','團年飯到會'],src='',use='H3／內文（節日公司活動段）')
add('CORP','FAQ',['公司到會價錢','公司到會要提前多少日預訂','公司到會有沒有素食','公司到會可否開發票'],src='建議',use='FAQ（FAQPage schema）')
add('CORP','主要',['corporate catering hong kong'],lang='EN',use='EN Title／H1（/en/ 版）')
add('CORP','次要',['corporate catering','corporate catering service','corporate catering hk','corporate catering events','office catering hong kong','office lunch delivery','office lunch catering','catering service company'],lang='EN',use='EN 內文／Meta')
# 到會推介
add('REC','主要',['到會推介','香港到會推介','到會推介2026'],use='H1／Title／首段 100 字內')
add('REC','次要',['到會推薦','到會服務推介','到會服務推介 2026','到會服務 香港','高級到會推介','高級到會','到會推介評分最高','到會推介 好食','到會推介2022'],use='H2／內文／Meta')
add('REC','長尾',['派對到會推介','party到會推介','派對到會 推介','美食到會','到會美食','到會專門店','小型到會'],use='H3／推介速覽表')
add('REC','主要',['catering company hong kong'],lang='EN',use='EN Title／H1（/en/ 版）')
add('REC','次要',['catering company hk','catering companies','party catering','party catering hk','catering party','food catering'],lang='EN',use='EN 內文')
# 首頁
add('HOME','主要',['到會','香港到會','到會服務','到會食物'])
add('HOME','主要',['catering','catering hk','catering hong kong','catering service hong kong','catering services','catering 中文'],lang='EN')
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
# 舊 blog
add('OLD1','主要',['到會邊間好','平價到會','到會價錢','到會平'],use='重寫時 H1／H2')
add('OLD2','主要',['中伏','到會中伏','到會注意事項'],use='重寫時 H1／H2')
add('XMAS','主要',['聖誕到會','聖誕到會推介','聖誕節到會','聖誕到會餐單','聖誕大餐到會','公司聖誕派對到會'],use='重寫時 H1／H2（12 月旺季前上線）')
add('XMAS','主要',['christmas catering hong kong','christmas catering','xmas party catering'],lang='EN')
# 不放
add('X','—',['到會推介lihkg','到會推介baby kingdom','到會推介 threads','大家樂到會','大快活到會','pizza hut到會','hku catering','asia pacific catering'],use='論壇／品牌／其他公司，不作目標')

AUTOC = {n(x) for x in ['公司到會推介','到會推介2026','到會推介評分最高','到會推介 好食','到會推介lihkg','到會推介baby kingdom','到會推介 threads',
         'annual dinner','annual dinner 遊戲','annual dinner 抽獎 禮物','annual dinner 場地','annual dinner 主題','annual dinner theme','annual dinner 表演','office lunch catering','到會邊間好']}

def pos(v):
    return v[0] if v else None

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
    if r['src'] == '建議' and not srcs: srcs.append('建議（待 KP）')
    rows.append(dict(kw=r['kw'], pg=r['pg'], typ=r['typ'], lang=r['lang'], use=r['use'],
        vol=s.get('vol') or None, kd=s.get('kd'), gi=g[1] if g else None, gp=round(g[2],1) if g and g[2] else None,
        pt=pt if isinstance(pt,(int,float)) else None, ao=pos(s.get('ao')), km=pos(s.get('km')), br=pos(s.get('br')),
        src='、'.join(srcs) or '—'))

# KP 種子字：沒有 Semrush 搜尋量、而且不是「不放」
seed = [r['kw'] for r in rows if r['vol'] is None and r['pg'] not in ('X',)]

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
<div class="pc big" data-pg="CORP"><div class="ph"><b>CORP</b><span class="st">第一輪｜要重寫</span></div>
<h3>公司到會（Annual Dinner、Office Lunch）</h3>
<p class="u"><a href="https://aoaodelivery.com/corporate-catering-hk/" target="_blank">/corporate-catering-hk/</a>（頁面 ID 18404）</p>
{num('CORP')}
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
<div class="pc big" data-pg="REC"><div class="ph"><b>REC</b><span class="st">第一輪｜要改寫</span></div>
<h3>到會推介</h3>
<p class="u"><a href="https://aoaodelivery.com/hong-kong-catering-recommendation/" target="_blank">/hong-kong-catering-recommendation/</a>（頁面 ID 18621）</p>
{num('REC')}
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
    return f'''<div class="pc {cls}" data-pg="{pg}"><div class="ph"><b>{pg}</b><span class="st">{status}</span></div>
<h3>{title}</h3><p class="u">{link}</p><ul class="iss">{lis}</ul>{kws}{more}</div>'''

OTHERS = [
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
 small('XMAS','舊 Blog：聖誕到會','/blog/christmas-catering-hong-kong/','重寫｜11 月中前上線',[
   '「聖誕到會」Semrush 1,000 搜尋量，GSC 265 曝光、第 16.7 名。12 月旺季前要更新 2026 套餐。',
   '負責所有「聖誕到會」字，包括公司聖誕派對；公司到會頁只簡單提及並連過來。']),
 small('NB1','新 Blog：Annual Dinner 籌備全攻略','（建議新增）','建議新增',[
   '承接 annual dinner 遊戲、抽獎禮物、場地、主題等資訊字，Kama 已用 Blog 排名（annual dinner 遊戲第 9 名）。',
   '文內 CTA 連去公司到會頁。']),
 small('RCP','Recipes 食譜','（未有 URL）','未開始',[
   '要先決定方向：素食食譜已分配給素食 B5；其他食譜（派對小食、節日菜式）要另做 KW list。',
   '建議用 Recipe schema，每篇連去對應的單點或套餐產品。']),
]

# ---------- 擁有權表 ----------
OWN = [
 ('到會、香港到會、到會服務、到會食物、catering','首頁','整站最大字，只由首頁主攻'),
 ('到會推介、香港到會推介、到會推薦、到會推介2026','到會推介','套餐推介清單'),
 ('到會邊間好、平價到會、到會價錢','舊 Blog：到會邊間好','比較及揀選準則'),
 ('中伏、到會注意事項','舊 Blog：到會中伏','避雷清單'),
 ('公司到會、企業到會、annual dinner 到會、office lunch','公司到會','交易型服務頁'),
 ('商務到會、酒會、開張、宴會到會、canapés','商務活動','活動型服務頁'),
 ('商務餐盒、員工餐盒、公司飯盒、商務便當','商務／員工餐盒分類','產品分類'),
 ('annual dinner 遊戲、抽獎禮物、場地、主題','新 Blog：Annual Dinner','資訊型'),
 ('聖誕到會、公司聖誕派對','舊 Blog：聖誕到會','季節性'),
]
own_html = '<table class="own"><tr><th>關鍵字群</th><th>負責頁面</th><th>頁面角色</th></tr>' + ''.join(f'<tr><td>{E(a)}</td><td><b>{E(b)}</b></td><td>{E(c)}</td></tr>' for a,b,c in OWN) + '</table>'

MERMAID = '''flowchart LR
H["首頁<br/>到會・catering"] --> REC["到會推介<br/>/hong-kong-catering-recommendation/"]
H --> CORP["公司到會<br/>/corporate-catering-hk/"]
REC --> CORP
REC <--> OLD1["舊 Blog<br/>到會邊間好"]
REC <--> OLD2["舊 Blog<br/>到會中伏"]
CORP --> BOX["商務／員工餐盒分類"]
CORP <--> BIZ["商務活動<br/>/business-event/"]
CORP <--> NB1["新 Blog<br/>Annual Dinner 籌備"]
CORP <--> XMAS["舊 Blog<br/>聖誕到會"]
CORP --> Q["報價查詢"]
BIZ --> Q
CORP --> P["合作夥伴"]
ABOUT["關於我們"] -.authority.-> CORP & REC
classDef main fill:#1A1A1A,color:#F7CE46,stroke:#1A1A1A
classDef blog fill:#E3F4E8,stroke:#6FAE82
classDef cat fill:#E3F1FB,stroke:#7AA7CF
class CORP,REC main
class OLD1,OLD2,XMAS,NB1 blog
class BOX,BIZ,Q,P,ABOUT cat'''

DATA = json.dumps(dict(rows=rows, pages={k: v[0] for k, v in PAGES.items()}), ensure_ascii=False)
SEED = '\n'.join(seed)

CSS = open(os.path.join(HERE, 'core-kw.css'), encoding='utf-8').read()
JS = open(os.path.join(HERE, 'core-kw.js'), encoding='utf-8').read()

page = f'''<!DOCTYPE html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>核心頁面 KW 分配｜Kitchen AO</title><style>{CSS}</style></head><body>
<header><h1>🏢 核心頁面 KW 分配（公司到會、到會推介＋其他待 review 頁面）</h1>
<p>資料：Semrush Organic Positions HK（2026-10-23，Kitchen AO／Kama／Bear）、GSC 近 3 個月（2026-10-08）、Position Tracking（2026-10-24）、Google 自動完成｜<a href="./index.html">← 返回網站架構圖</a></p></header>
<div class="wrap">
<div class="rule"><b>分配原則：</b>一個關鍵字只分配到一頁。整站大字（到會、catering）只由首頁主攻；「推介」字由到會推介頁負責；公司及 Annual Dinner 交易字由公司到會頁負責；資訊字（遊戲、抽獎、場地）放 Blog；餐盒字留在產品分類。<br><b>注意：</b>公司到會類大部分字在 Semrush 沒有搜尋量，標示「待 KP」，請用下面的種子字清單在 Keyword Planner 查詢後再更新。</div>
<h2>內鏈架構</h2><div class="card"><pre class="mermaid">{E(MERMAID)}</pre></div>
<h2>關鍵字擁有權（防止自家頁面互搶）</h2><div class="card">{own_html}</div>
<h2>第一輪：公司到會＋到會推介</h2><div class="grid1">{CORP_CARD}{REC_CARD}</div>
<h2>其他待 review 頁面</h2><div class="grid">{''.join(OTHERS)}</div>
<h2 id="all">全部關鍵字</h2><div class="card">
<div class="tools"><select id="pg"><option value="">全部頁面</option></select><select id="lang"><option value="">中＋EN</option><option>中</option><option>EN</option></select><input id="q" placeholder="搜尋關鍵字"><span id="cnt"></span><button class="dl" id="dl">⬇ 下載 CSV</button></div>
<div class="tw"><table id="tb"></table></div>
<p class="foot">Vol／KD＝Semrush HK；GSC＝曝光／平均排名（近 3 個月）；PT＝Position Tracking 10-24 排名（Desktop）；AO／Kama／Bear＝Semrush 排名。空白代表沒有數據。</p></div>
<h2>Keyword Planner 種子字（{len(seed)} 個，沒有 Semrush 搜尋量）</h2><div class="card">
<p class="note">複製後貼入 Google Keyword Planner ›「取得搜尋量和預測」，地區選香港，匯出 csv 給我更新。</p>
<textarea id="seed" readonly>{E(SEED)}</textarea><button class="dl" id="cp">📋 複製</button></div>
</div>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<script>const D={DATA};{JS}</script></body></html>'''

open(os.path.join(HERE, 'core-pages-kw.html'), 'w', encoding='utf-8').write(page)
print('rows', len(rows), 'seed', len(seed))
for pg in PAGES: print(pg, stats(pg))
