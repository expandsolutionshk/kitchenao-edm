# -*- coding: utf-8 -*-
"""整合新增 GKP（Keyword Stats 2026-10-28）到 KW 分類，並按 Blog 重新分配關鍵字"""
import json, os, re
from collections import Counter
from content import CATS as BASE, SHOP_CAT, PRODUCTS, PRICE_DATE, PROD_EXTRA
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

HERE = os.path.dirname(os.path.abspath(__file__))
fv = lambda v: '—' if v is None else f'{v:,}'
n = lambda k: re.sub(r'\s+', '', k).lower()
CJK = '一-鿿'
tidy = lambda k: re.sub(r'(?<=[' + CJK + r'0-9])\s+(?=[' + CJK + r'])|(?<=[' + CJK + r'])\s+(?=[0-9])', '', k.strip())

CATS = dict(BASE)
CATS['C2'] = '燜燒壺／燜燒杯／湯壺'
CATS.update({'C9': '飲品保溫壺／保溫杯／保溫瓶', 'C10': '冰袋／冰磚／露營冰箱',
             'C11': '錫紙／牛油紙／烘焙紙', 'C12': '暖包／自熱包'})
OLD = json.load(open(os.path.join(HERE, 'kw_classified.json'), encoding='utf-8'))
NEW = json.load(open(os.path.join(HERE, 'gkp_add_2026-10-28.json'), encoding='utf-8'))


def cat_new(k):
    if re.search(r'保溫壺|保溫杯|保溫瓶', k): return 'C9'
    if re.search(r'冰袋|冰磚|露營冰箱|野餐保冷袋', k): return 'C10'
    if re.search(r'錫紙|牛油紙|烘焙紙', k): return 'C11'
    if re.search(r'暖包|自熱包', k): return 'C12'
    if re.search(r'加熱|電熱|自熱', k): return 'C3'
    if re.search(r'燜燒|湯壺|食物罐|保溫提鍋', k): return 'C2'
    if re.search(r'保鮮紙|保鮮膜|保鮮布', k): return 'C5'
    if re.search(r'密實袋|保鮮袋|真空袋|ziploc|食物袋', k): return 'C6'
    if re.search(r'保鮮盒|密實盒|抽真空機|收納盒', k): return 'C4'
    if re.search(r'保溫箱|保溫袋|保冷袋|保暖袋|保溫手提袋|保溫背包', k): return 'C7'
    if re.search(r'保溫桶|保溫碟|保溫餐爐|布菲爐|保溫爐|暖碟', k): return 'C8'
    return 'C1'


rows = {}
for r in OLD:
    rows[r['norm']] = dict(kw=tidy(r['kw']), gkp=r['kw'], vol=r['vol'], comp=r['comp'], cat=r['cat'], brand=r['brand'],
                           sub=r['sub'], intent=r['intent'], src='原有清單（保溫.xlsx）', m3='', yoy='')
for x in NEW:
    k = n(x['kw'])
    if k in rows:
        rows[k].update(src='原有清單＋新增 GKP', m3=x['m3'], yoy=x['yoy'])
        continue
    rows[k] = dict(kw=tidy(x['kw']), gkp=x['kw'], vol=x['vol'], comp=x['comp'], cat=cat_new(k),
                   brand='Ziploc' if 'ziploc' in k else '',
                   sub='推介' if '推介' in k else ('問題／評價（FAQ）' if '食譜' in k else '通用'),
                   intent='Informational' if '食譜' in k else 'Commercial／Transactional',
                   src='新增 GKP（2026-10-28）', m3=x['m3'], yoy=x['yoy'])

AC = [('保溫飯盒推薦', 'C1', '長尾'), ('保溫飯盒推薦香港', 'C1', '長尾'), ('保溫飯盒邊隻好', 'C1', '長尾'), ('保溫飯盒消委會', 'C1', 'FAQ'),
      ('保溫飯盒袋', 'C7', '長尾'), ('燜燒壺保溫壺分別', 'C2', 'FAQ'), ('燜燒壺推介', 'C2', '長尾'), ('燜燒壺用法', 'C2', 'FAQ'),
      ('燜燒壺帶飯', 'C2', '長尾'), ('燜燒壺食譜', 'C2', '長尾'), ('燜燒壺消委會', 'C2', 'FAQ'), ('保溫袋推薦', 'C7', '長尾'),
      ('保溫袋可以撐多久', 'C7', 'FAQ'), ('加熱飯盒推薦', 'C3', '長尾'), ('加熱飯盒消委會', 'C3', 'FAQ'), ('usb 加熱飯盒', 'C3', '長尾'),
      ('保鮮紙可以入微波爐嗎', 'C5', 'FAQ'), ('保鮮紙可以蒸嗎', 'C5', 'FAQ'), ('保鮮紙品牌', 'C5', '長尾'),
      ('密實袋尺寸', 'C6', '長尾'), ('密實袋微波爐', 'C6', 'FAQ'), ('密實袋慢煮', 'C6', '長尾'), ('密實袋耐熱', 'C6', 'FAQ')]
for kw, c, role in AC:
    k = n(kw)
    if k in rows: continue
    rows[k] = dict(kw=kw, gkp='', vol=None, comp='', cat=c, brand='', sub='問題／評價（FAQ）' if role == 'FAQ' else '推介',
                   intent='Informational' if role == 'FAQ' else 'Commercial', src='Google 自動建議（2026-10-28）', m3='', yoy='', ac_role=role)
for k, r in rows.items():
    # 原有清單中屬飲品保溫壺／保溫杯的字，移去 C9
    if r['cat'] == 'C2' and re.search(r'保[溫温]壺|保[溫温]壶|保溫杯', k) and not re.search(r'燜|悶|飯壺|罐', k):
        r['cat'] = 'C9'
    r['catname'] = CATS[r['cat']]
    r['variant'] = bool(re.search(r'[温饭壶鲜实]', r['gkp'] or ''))

BLOG = {
    'C1': ('Blog 1｜食物保暖用品篇', 'H2｜保溫飯盒／保溫便當盒推介'),
    'C2': ('Blog 1｜食物保暖用品篇', 'H2｜燜燒壺、燜燒杯與湯壺'),
    'C3': ('Blog 1｜食物保暖用品篇', 'H2｜加熱飯盒、電熱飯盒與自熱飯盒'),
    'C7': ('Blog 1｜食物保暖用品篇', 'H2｜保溫袋、保冷袋與保溫箱'),
    'C8': ('Blog 1｜食物保暖用品篇', 'H2｜派對及到會食物怎樣保溫？（Kitchen AO 轉化段）'),
    'C9': ('只作承接（不作目標）', 'Blog 1 的 H3「燜燒壺與保溫壺有甚麼分別？」'),
    'C4': ('Blog 2｜保鮮用品篇（建議另寫）', 'H2｜保鮮盒、密實盒與真空保鮮'),
    'C5': ('Blog 2｜保鮮用品篇（建議另寫）', 'H2｜保鮮紙、保鮮膜與保鮮貼'),
    'C6': ('Blog 2｜保鮮用品篇（建議另寫）', 'H2｜保鮮袋、密實袋與真空袋'),
    'C10': ('暫不使用（冰袋、冰磚）', ''),
    'C11': ('不建議（另一主題：烘焙）', ''),
    'C12': ('不建議（暖包多指暖手包）', ''),
}
for r in rows.values():
    r['blog'], r['h2'] = BLOG[r['cat']]

# 角色：每個 H2 主要 1 個、次要最多 6 個（月搜 50 以上）、長尾（20 至 40）、FAQ，其餘自然涵蓋
MAIN = {'C1': '保溫飯盒', 'C2': '燜燒壺', 'C3': '加熱飯盒', 'C7': '保溫袋', 'C8': '保溫碗',
        'C4': '保鮮盒', 'C5': '保鮮紙', 'C6': '密實袋'}
for c in CATS:
    i = 0
    for r in sorted([r for r in rows.values() if r['cat'] == c], key=lambda r: -(r['vol'] or 0)):
        if not r['blog'].startswith('Blog'): r['role'] = '不作目標'; continue
        if r.get('ac_role'): r['role'] = r['ac_role']; continue
        if r['sub'] == '問題／評價（FAQ）': r['role'] = 'FAQ'; continue
        if n(r['kw']) == n(MAIN.get(c, '')): r['role'] = '主要'; continue
        if r['variant']: r['role'] = '自然涵蓋（簡體／異寫）'; continue
        if r['vol'] >= 50 and i < (9 if c == 'C1' else 6): r['role'] = '次要'; i += 1; continue
        r['role'] = '長尾' if r['vol'] >= 20 else '自然涵蓋（月搜 10 或以下）'
rows[n('保溫飯盒')]['role'] = '全文主關鍵字'
rows[n('保鮮紙')]['role'] = '全文主關鍵字'
for k in ('保溫飯盒推介', '學生保溫飯盒', '象印保溫飯盒', '燜燒壺保溫壺分別'): rows[n(k)]['focus'] = True
R = list(rows.values())
json.dump(R, open(os.path.join(HERE, 'kw_classified_v2.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)

# ---------------- Excel ----------------
wb = Workbook()
HF = PatternFill('solid', fgColor='1A1A1A'); HFont = Font(name='Arial', bold=True, color='F7CE46')


def sheet(ws, head, data, widths):
    ws.append(head)
    for d in data: ws.append(d)
    for c in ws[1]: c.fill = HF; c.font = HFont; c.alignment = Alignment(wrap_text=True, vertical='center')
    for row in ws.iter_rows(min_row=2):
        for c in row: c.font = Font(name='Arial'); c.alignment = Alignment(wrap_text=True, vertical='top')
    for i, w in enumerate(widths, 1): ws.column_dimensions[get_column_letter(i)].width = w
    ws.freeze_panes = 'B2'; ws.auto_filter.ref = f"A1:{get_column_letter(len(head))}{ws.max_row}"


ORD = {'全文主關鍵字': 0, '主要': 1, '次要': 2, '長尾': 3, 'FAQ': 4, '自然涵蓋（簡體／異寫）': 5,
       '自然涵蓋（月搜 10 或以下）': 6, '不作目標': 7}
BORD = lambda b: 0 if b.startswith('Blog 1') else 1 if b.startswith('Blog 2') else 2

ws = wb.active; ws.title = '關鍵字分類'
data = sorted(R, key=lambda r: (BORD(r['blog']), int(r['cat'][1:]), ORD[r['role']], -(r['vol'] or 0)))
sheet(ws, ['Blog 分配', '類別代號', '產品類別', '關鍵字', 'GKP 原文', 'Avg. monthly searches', '3 個月變化', '按年變化',
           '角色', '細分', '品牌', '搜尋意圖', '放置位置', 'Competition（廣告）', '資料來源'],
      [[r['blog'], r['cat'], r['catname'], r['kw'], r['gkp'], r['vol'], r['m3'], r['yoy'], r['role'], r['sub'],
        r['brand'], r['intent'], r['h2'], r['comp'], r['src']] for r in data],
      [22, 8, 22, 26, 26, 11, 9, 9, 18, 16, 14, 20, 34, 12, 20])
FILL = {'全文主關鍵字': 'F7CE46', '主要': 'FFF2A8', '次要': 'FFF9DB', '不作目標': 'EEEEEE'}
for row in ws.iter_rows(min_row=2):
    f = FILL.get(row[8].value)
    if f:
        for c in row: c.fill = PatternFill('solid', fgColor=f)
    bold = row[8].value in ('全文主關鍵字', '主要')
    for c in row: c.font = Font(name='Arial', bold=bold)
    if row[14].value.startswith('新增') or row[14].value.endswith('新增 GKP'):
        row[3].font = Font(name='Arial', bold=bold, color='2C6E49')

ws2 = wb.create_sheet('Blog KW 重整')
summ = []
TGT = ('全文主關鍵字', '主要', '次要', '長尾', 'FAQ')
for b in ['Blog 1｜食物保暖用品篇', 'Blog 2｜保鮮用品篇（建議另寫）', '只作承接（不作目標）', '暫不使用（冰袋、冰磚）',
          '不建議（另一主題：烘焙）', '不建議（暖包多指暖手包）']:
    rs = [r for r in R if r['blog'] == b]
    pick = lambda role: '、'.join(f"{r['kw']}（{fv(r['vol'])}）" for r in sorted([x for x in rs if x['role'] == role], key=lambda r: -(r['vol'] or 0)))
    tgt = [r for r in rs if r['role'] in TGT]
    summ.append([b, len(rs), sum((r['vol'] or 0) for r in rs), len(tgt), pick('全文主關鍵字'), pick('主要'), pick('次要'), pick('長尾'),
                 '' if tgt else '、'.join(f"{r['kw']}（{fv(r['vol'])}）" for r in sorted(rs, key=lambda r: -(r['vol'] or 0))[:8])])
sheet(ws2, ['分配', '關鍵字數', '月搜合計', '實際要佈局的字數', '全文主關鍵字', '各 H2 主要關鍵字', '次要關鍵字', '長尾關鍵字', '代表字（不作目標）'],
      summ, [26, 9, 11, 12, 18, 36, 60, 70, 60])

ws3 = wb.create_sheet('類別總覽')
cs = []
for c, name in CATS.items():
    rs = sorted([r for r in R if r['cat'] == c], key=lambda r: -(r['vol'] or 0))
    cs.append([c, name, rs[0]['blog'], len(rs), sum((r['vol'] or 0) for r in rs),
               '、'.join(f"{r['kw']}（{fv(r['vol'])}）" for r in rs[:6]), SHOP_CAT.get(c, '')])
sheet(ws3, ['類別代號', '產品類別', 'Blog 分配', '關鍵字數', '月搜合計', '代表關鍵字（月搜）', '網店分類參考'], cs, [9, 24, 26, 9, 10, 60, 50])

ws4 = wb.create_sheet('新增KW（GKP 已查）')
nk = sorted([r for r in R if r['src'] != '原有清單（保溫.xlsx）'], key=lambda r: -(r['vol'] or 0))
sheet(ws4, ['關鍵字', 'Avg. monthly searches', '3 個月變化', '按年變化', 'Competition（廣告）', '類別', 'Blog 分配', '角色'],
      [[r['kw'], r['vol'], r['m3'], r['yoy'], r['comp'], r['catname'], r['blog'], r['role']] for r in nk],
      [20, 12, 10, 10, 12, 24, 28, 22])

ws5 = wb.create_sheet('產品對照表')
sheet(ws5, ['類別', '品牌', '產品名稱（網店官方原文）', '型號／貨號', '容量／尺寸', '重點規格', '價錢（HKD）', '網店', '產品連結', '產品圖片網址', '備註'],
      [[CATS[p[0]], p[1], p[2], PROD_EXTRA[p[7]][0]] + list(p[3:8]) + [PROD_EXTRA[p[7]][1], p[8]] for p in PRODUCTS], [22, 18, 40, 16, 20, 36, 18, 22, 50, 50, 20])
for row in ws5.iter_rows(min_row=2):
    for i in (8, 9):
        row[i].hyperlink = row[i].value; row[i].font = Font(name='Arial', color='0563C1', underline='single')

ws6 = wb.create_sheet('說明')
for line in [
    ['資料來源', f'Google Keyword Planner（香港）：原有清單「保溫.xlsx」273 個字，加上 2026-10-28 新增查詢 60 個字（1 個與原有重複），合共 {len(R)} 個字'],
    ['月搜', 'Avg. monthly searches 為 2025 年 10 月至 2026 年 9 月平均；3 個月及按年變化只限新增查詢的字'],
    ['Competition', 'Google 廣告的競爭程度，不等於 SEO 排名難度'],
    ['角色', '全文主關鍵字／主要：放 H1、Title 及 H2；次要：H2、H3 或內文；長尾：H3、FAQ 或內文一次；自然涵蓋：不用刻意寫入，Google 會視作同義或變體；不作目標：不寫入此 blog'],
    ['顏色', '深黃＝全文主關鍵字；黃＝各 H2 主要關鍵字；淺黃＝次要；灰＝不作目標；綠字＝新增 GKP 字'],
    ['價錢日期', PRICE_DATE + '，於各網店產品頁記錄，以網店實時價錢為準'],
]:
    ws6.append(line)
ws6.column_dimensions['A'].width = 14; ws6.column_dimensions['B'].width = 100
for row in ws6.iter_rows():
    for c in row:
        c.font = Font(name='Arial', bold=(c.column == 1)); c.alignment = Alignment(wrap_text=True, vertical='top')
wb.save(os.path.join(HERE, '保溫保鮮餐具_KW分類_2026-10-28.xlsx'))

for s in summ: print(s[0], s[1], s[2], s[3], '|', s[4], '|', s[5], '|', s[6][:300])
print(Counter(r['role'] for r in R if r['blog'].startswith('Blog 1')))
print(len(R))
