# Blog 1 SEO 設定＋Keyword 部署頁 → seo-keywords.html
# 參考 qivation-mockup「逐段複製」頁的上半部（SEO 設定、Keyword 部署表、click 入了解更多），不含逐段 blog content
# Keyword 數據：kwdata.json（由「野餐keyword list (地點資料 v3).xlsx」GKP／Keyword Surfer／文章與keyword分配(blog1) 匯出）
import importlib.util, os, re, json, html as H
HERE = os.path.dirname(os.path.abspath(__file__))
s = importlib.util.spec_from_file_location('build', os.path.join(HERE, 'build.py')); B = importlib.util.module_from_spec(s); s.loader.exec_module(B)
D = json.load(open(os.path.join(HERE, 'kwdata.json')))
G, KS, BL = D['gkp'], D['ks'], D['blog1']
N = B.N

# ---------- SEO 設定 ----------
META_TITLE = f'香港野餐好去處2026｜{N}個大草地、海景、寵物友善野餐地點'
META_DESC = f'全港{N}個野餐好去處一鍵搜尋：按新界、九龍、港島篩選可泊車、寵物友善、大草地及海景地點，附鄰近停車場實時車位，野餐盒送到附近可停車位置。'
H1 = f'【香港野餐勝地大全】{N} 個大草地／海景／隱世公園推介｜野餐泊車、寵物友善地點一鍵搜尋'
SLUG = 'hong-kong-picnic-spots'
URL = f'https://aoaodelivery.com/blog/{SLUG}/'
KV_FILE = 'hong-kong-picnic-spots-2026-kv.webp'
KV_ALT = '香港野餐好去處 2026 全港野餐地點搜尋器'

# ---------- 文章內容（preview.html，抽出各位置文字）----------
h = open(os.path.join(HERE, 'preview.html')).read()
art = h[h.index('<div class="ao-article'):]
art = re.sub(r'<script.*?</script>|<style.*?</style>|<iframe.*?</iframe>', '', art, flags=re.S)
art = re.sub(r'<p class="pk-kw">.*?</p>|<p class="pk-h1note">.*?</p>', '', art, flags=re.S)   # 目標關鍵字標示及 H1 備註不計
txt = lambda x: re.sub(r'<[^>]+>', '', x)
faq_part = ''.join(re.findall(r'<details class="ao-faq">.*?</details>', art, flags=re.S))
h2s = ' '.join(re.findall(r'<h2[^>]*>(.*?)</h2>', art, flags=re.S))
h3s = ' '.join(re.findall(r'<h3[^>]*>(.*?)</h3>', art, flags=re.S))
body = re.sub(r'<details class="ao-faq">.*?</details>|<h2[^>]*>.*?</h2>|<h3[^>]*>.*?</h3>', '', art, flags=re.S)
ZONES = [('Title', META_TITLE), ('Description', META_DESC), ('H1', H1), ('H2', txt(h2s)), ('H3', txt(h3s)), ('內文', txt(body)), ('FAQ', txt(faq_part))]
marked = set(re.findall(r'<mark class="kw">([^<]*)</mark>', art))

def where(k):
    return [z for z, t in ZONES if k in t]

def vol(k, given=None):
    v = given if given not in (None, '', '--', 'None') else (G.get(k, {}) or {}).get('vol')
    try: return int(float(v))
    except Exception: return None

def yoy(k):
    y = (G.get(k) or {}).get('yoy')
    if y in (None, 'None', '--'): return '—'
    if y in ('∞', 'inf'): return '新出現'
    try:
        f = float(y); return f'{"+" if f > 0 else ("−" if f < 0 else "")}{abs(round(f * 100))}%'
    except Exception: return str(y)

# ---------- Keyword 清單（Excel blog1 分配 + 文章已用的主題字）----------
EXTRA = ['香港野餐好去處', '香港野餐地點', '隱世野餐地點', '野餐食物', '野餐小食', '野餐墊', '野餐泊車', '駕車野餐', '野餐食物哪裡買', '野餐注意事項']
SKIP = {'浩和街野餐'}   # 屯門浩和街已刪除
rows, seen = [], set()
for r in BL:
    k = r['kw']
    if k in seen or k in SKIP: continue
    seen.add(k); rows.append({'kw': k, 'vol': vol(k, r['vol']), 'src': 'Excel blog1 分配'})
for k in EXTRA:
    if k not in seen:
        seen.add(k); rows.append({'kw': k, 'vol': vol(k), 'src': '文章主題字'})
TOPIC = {'野餐好去處', '香港野餐好去處', '香港野餐地點', '野餐小食', '野餐食物', '野餐墊'}
SECOND = {'港島野餐', '九龍野餐', '九龍野餐好去處', '新界野餐地點', '狗狗野餐好去處', '狗狗野餐', '狗狗寵物公園', '野餐泊車', '野餐盒', '隱世野餐地點', '野餐食物哪裡買', '駕車野餐', '野餐注意事項'}
for r in rows:
    k = r['kw']; ks = KS.get(k)
    r['ks'] = int(float(ks)) if ks not in (None, 'None', '') else None
    r['tier'] = '主' if (k in TOPIC or (r['vol'] or 0) >= 500) else ('次' if k in SECOND else ('長尾' if not r['vol'] else '地點'))
    r['where'] = where(k); r['yoy'] = yoy(k)
    r['ok'] = '✓' if r['where'] else '✗'
    r['hl'] = any(k in m for m in marked)
ORDER = {'主': 0, '次': 1, '地點': 2, '長尾': 3}
rows.sort(key=lambda r: (ORDER[r['tier']], -(r['vol'] or 0), -(r['ks'] or 0)))
covered = sum(r['vol'] or 0 for r in rows if r['ok'] == '✓'); total = sum(r['vol'] or 0 for r in rows)
fmt = lambda v: f'{v:,}' if v else '—'

trs = ''.join(f'''<tr><td class="c">{r["tier"]}</td><td><b>{r["kw"]}</b>{'' if r['hl'] else ' <span class="nohl">未 highlight</span>'}</td><td class="n">{fmt(r["vol"])}</td><td class="n">{fmt(r["ks"])}</td><td class="n">{r["yoy"]}</td><td>{"、".join(r["where"]) or "—"}</td><td class="c st{'' if r['ok']=='✓' else ' bad'}">{r["ok"]}</td></tr>''' for r in rows)

# ---------- click 入了解更多：層級總覽＋按用家問題分類 ----------
by = {t: [r for r in rows if r['tier'] == t] for t in ORDER}
lv = lambda rs: '、'.join(f'<b>{r["kw"]}</b>（{fmt(r["vol"])}）' if r['vol'] else r['kw'] for r in rs)
FAQQ = [q for q, a in B.FAQ]
GROUPS = [
 ('A', '搵地點：邊度可以野餐？', 'Where（搵地點）', '香港有咩野餐好去處？邊區有大草地、海景？',
  ['野餐好去處', '香港野餐好去處', '香港野餐地點', '隱世野餐地點', '港島野餐', '九龍野餐', '九龍野餐好去處', '新界野餐地點', '西九野餐', '啟德野餐', '迪欣湖野餐'],
  ['香港的公園可以野餐嗎？', '下雨天可以去哪裡野餐？', '公眾假期去野餐要注意甚麼？'], '搜尋器、一覽比較表、一／二／三 地區段落（地點卡）'),
 ('B', '帶狗狗：邊度准帶寵物？', 'Where ＋ 是非題', '可唔可以帶狗？邊度係寵物共享公園？',
  ['狗狗野餐好去處', '狗狗野餐', '狗狗寵物公園'], ['可以帶狗去野餐嗎？'], '搜尋器「寵物友善」篩選、地點卡寵物資料及寵物共享範圍地圖、帶狗狗野餐須知'),
 ('C', '泊車：揸車去邊度方便？', 'How-to（交通）', '邊個地點有停車場？有冇實時車位？',
  ['野餐泊車', '駕車野餐'], ['哪個野餐地點有停車場？'], '搜尋器「可泊車」篩選、地點卡鄰近停車場及實時車位'),
 ('D', '食物：帶咩食物、去邊度買？', '推薦／準備買', '野餐食物點揀？邊度訂野餐盒？',
  ['野餐食物', '野餐小食', '野餐盒', '野餐食物哪裡買'], ['野餐食物哪裡買？', '野餐食物如何保鮮？', '野餐盒可以送到公園嗎？'], '野餐食物段、Kitchen AO 野餐盒、單點小食推介'),
 ('E', '用品及注意事項', 'How-to ＋ 是非題', '要帶咩用品？有咩規矩？',
  ['野餐墊', '野餐注意事項'], ['野餐幾點到達最容易找到位置？', '公園野餐可以燒烤嗎？'], '野餐用品清單、編輯總結'),
]
rmap = {r['kw']: r for r in rows}
def gblock(code, name, typ, need, kws, faqs, pos):
    tot = sum((rmap.get(k) or {}).get('vol') or 0 for k in kws)
    kk = '、'.join(f'{k} {fmt((rmap.get(k) or {}).get("vol"))}' for k in kws)
    ff = '<br>'.join(('✓ ' if q in FAQQ else '✗ ') + q for q in faqs)
    return f'''<table class="grp"><thead><tr><th colspan="2">{code}. {name}<small>合計 {tot:,}／月 · {typ}</small></th></tr></thead><tbody>
<tr><td class="k">用家想解決</td><td>{need}</td></tr><tr><td class="k">Keyword</td><td>{kk}</td></tr>
<tr><td class="k">本文已答問題（FAQ）</td><td>{ff}</td></tr><tr><td class="k">文章位置</td><td>{pos}</td></tr></tbody></table>'''
groups = ''.join(gblock(*g) for g in GROUPS)
place_rows = by['地點']

def field(lbl, val, cnt=True, note=''):
    c = f'<span class="cnt">{len(val)} 字</span>' if cnt else ''
    return f'<div class="fld"><div class="fl">{lbl}</div><div class="fv"><span class="v">{H.escape(val)}</span>{c}<button type="button" class="cp" data-v="{H.escape(val, quote=True)}">複製</button>{note}</div></div>'

PAGE = f'''<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>SEO 設定及 Keyword 部署 — {H.escape(H1)}</title>
<style>
*{{box-sizing:border-box}}body{{margin:0;background:#F6F4EF;font-family:-apple-system,"PingFang HK","Microsoft JhengHei",Arial,sans-serif;color:#2b2a27;line-height:1.7;font-size:15px}}
.wrap{{max-width:1080px;margin:0 auto;padding:28px 18px 70px}}h1{{font-size:22px;margin:0 0 6px}}.lead{{margin:0 0 26px;color:#6b6457}}
.card{{background:#fff;border:1px solid #E7E1D4;border-radius:14px;padding:20px 22px;margin:0 0 22px}}.card h2{{margin:0 0 6px;font-size:18px}}.card .hint{{margin:0 0 14px;color:#7a6a45;font-size:13.5px}}
.fld{{display:grid;grid-template-columns:150px 1fr;gap:12px;padding:12px 0;border-top:1px solid #F0EBE0}}.fld:first-of-type{{border-top:0}}.fl{{font-weight:800;color:#2C6E49}}
.fv{{display:flex;flex-wrap:wrap;align-items:center;gap:8px}}.v{{flex:1 1 420px}}.cnt{{font-size:12.5px;color:#3F9D5A;font-weight:700}}
.cp{{border:1px solid #CFE8CD;background:#F4FBF3;color:#2C6E49;border-radius:20px;padding:3px 12px;font-size:12.5px;font-weight:700;cursor:pointer}}.cp.done{{background:#3F9D5A;color:#fff}}
.note{{flex:1 1 100%;font-size:13px;color:#7a6a45}}.v{{min-width:0;overflow-wrap:anywhere}}
@media(max-width:640px){{.fld{{grid-template-columns:1fr;gap:4px}}.v{{flex-basis:100%}}}}
.legend{{font-size:13px;color:#6b6457;margin:0 0 10px}}.legend b{{color:#2b2a27}}
.tw{{overflow-x:auto;border:1px solid #E7E1D4;border-radius:10px}}table{{border-collapse:collapse;width:100%;font-size:14px}}
th{{background:#2C6E49;color:#fff;text-align:left;padding:9px 10px;white-space:nowrap}}td{{padding:8px 10px;border-top:1px solid #F0EBE0;vertical-align:top}}
td.c{{text-align:center;white-space:nowrap}}td.n{{text-align:right;white-space:nowrap;font-variant-numeric:tabular-nums}}.st{{color:#2C6E49;font-weight:900}}.st.bad{{color:#C0392B}}
.nohl{{font-size:11.5px;color:#C24E00;background:#FFF0E0;border-radius:8px;padding:1px 6px}}
.src{{margin:10px 0 0;font-size:12.5px;color:#7a6a45}}
details.more{{margin:18px 0 0;border:1.5px solid #3F9D5A;border-radius:12px;background:#fff}}details.more>summary{{list-style:none;cursor:pointer;padding:12px 16px;font-weight:800;color:#2C6E49;display:flex;justify-content:space-between;gap:10px}}details.more>summary::-webkit-details-marker{{display:none}}
details.more>summary .ar{{transition:transform .2s}}details.more[open]>summary .ar{{transform:rotate(180deg)}}.mbody{{padding:4px 16px 18px}}.mbody h3{{font-size:16px;margin:16px 0 8px}}
table.lv td:first-child,table.grp td.k{{width:150px;font-weight:800;color:#2C6E49;white-space:nowrap}}table.grp{{margin:0 0 14px;border:1px solid #E7E1D4;border-radius:10px;overflow:hidden}}table.grp th small{{margin-left:10px;font-weight:600;opacity:.85}}
</style></head><body><div class="wrap">
<h1>SEO 設定及 Keyword 部署 — Blog 1 香港野餐好去處</h1>
<p class="lead">填入 WordPress 文章 → Rank Math（或 Yoast）SEO 設定。撳「複製」即可抄入相應欄位。</p>

<section class="card"><h2>SEO 設定</h2><p class="hint">字數以中文字計（全形符號計 1 字）；Meta Title 建議約 30 字內，Meta Description 約 80 字內。</p>
{field('Meta Title', META_TITLE)}
{field('Meta Description', META_DESC)}
{field('文章標題（H1）', H1)}
{field('封面圖（KV）', KV_FILE, False, '<span class="note">1600 × 900 webp；alt：' + KV_ALT + '（採用 KV 方案 G）</span>')}
{field('URL Slug', SLUG, False)}
{field('完整網址', URL, False)}
{field('分類', '香港到會資訊', False, '<span class="note">與船P篇相同分類；如另設「生活／活動」分類可再調整。</span>')}
{field('Focus Keyword', '野餐好去處', False, '<span class="note">次要：香港野餐好去處、香港野餐地點、狗狗野餐好去處、野餐泊車</span>')}
</section>

<section class="card"><h2>本篇 Keyword 部署</h2>
<p class="legend"><b>✓</b> 原字出現於文章　<b>✗</b> 未覆蓋　｜　<span class="nohl">未 highlight</span> ＝ 文章有出現但未加黃色標示　｜　已覆蓋月搜尋 {covered:,}／{total:,}</p>
<div class="tw"><table><thead><tr><th>層級</th><th>Keyword</th><th>月搜尋（GKP）</th><th>Keyword Surfer</th><th>按年</th><th>放喺邊</th><th>狀態</th></tr></thead><tbody>{trs}</tbody></table></div>
<p class="src">數據：{D["file"]}（GKP、Keyword Surfer 及「文章與keyword分配(blog1)」工作表）。GKP 月搜尋為 Keyword Planner 區間數值；「—」表示 Excel 未有數據。「放喺邊」按 preview.html 實際內容自動檢查（不計「目標關鍵字」標示行）。屯門浩和街已刪除，相關字詞不列入。</p>

<details class="more"><summary><span>click 入了解更多　層級總覽 ＋ 按「用家想解決咩問題」分類</span><b class="ar">▾</b></summary><div class="mbody">
<h3>1. 層級總覽</h3>
<div class="tw"><table class="lv"><tbody>
<tr><td>主字</td><td>{lv(by['主'])}</td></tr>
<tr><td>次字</td><td>{lv(by['次'])}</td></tr>
<tr><td>地點字</td><td>{'、'.join(f'{r["kw"]} {fmt(r["vol"])}' for r in place_rows)}</td></tr>
<tr><td>長尾</td><td>{'、'.join(r['kw'] for r in by['長尾']) or '—'}</td></tr>
<tr><td>產品</td><td>Chill一下野餐盒（小／大）、二人小確幸套餐、二人豪華儀式感UP!套餐、5 人自選拼盤、單點小食 6 款</td></tr>
</tbody></table></div>
<h3>2. 按「用家想解決咩問題」分類</h3>
{groups}
<p class="src">「本文已答問題」為文章 FAQ 及內文已回答的問題（✓ 已答、✗ 未答）；未有 Google PAA 實際抓取數據，如需要可再補充。</p>
</div></details>
</section>
</div>
<script>document.querySelectorAll('.cp').forEach(function(b){{b.onclick=function(){{(navigator.clipboard?navigator.clipboard.writeText(b.dataset.v):Promise.reject()).then(function(){{b.textContent='已複製';b.classList.add('done');setTimeout(function(){{b.textContent='複製';b.classList.remove('done')}},1500)}}).catch(function(){{prompt('複製以下內容',b.dataset.v)}})}}}});</script>
</body></html>'''
if __name__ == '__main__':
    open(os.path.join(HERE, 'seo-keywords.html'), 'w').write(PAGE)
    print('rows', len(rows), 'covered', covered, total, 'missing', [r['kw'] for r in rows if r['ok'] != '✓'], 'nohl', [r['kw'] for r in rows if r['ok'] == '✓' and not r['hl']])
    print(len(META_TITLE), len(META_DESC), len(H1))
