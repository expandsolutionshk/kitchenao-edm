# -*- coding: utf-8 -*-
import json, os, re
from content import *
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_LINE_SPACING
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import docx.opc.constants

TARGET={'C1':'保溫飯盒（待 KP；現有清單以「保溫盒」140 最大）','C2':'燜燒壺（待 KP；「象印保温壺」1,900 多數是飲品保溫壺）','C3':'加熱飯盒（待 KP）','C4':'保鮮盒、密實盒（待 KP；現有清單幾乎沒有數據）','C5':'保鮮紙（待 KP；現有以品牌字「佳能保鮮紙」590 最大）','C6':'密實袋、保鮮袋（待 KP；現有以「佳能保鮮袋」260 最大）','C7':'保溫袋（1,000）','C8':'食物保溫方法（10）'}
HERE=os.path.dirname(os.path.abspath(__file__))
K=json.load(open(os.path.join(HERE,'kw_classified.json'),encoding='utf-8'))
n=lambda k:re.sub(r'\s+','',k).lower()
CJK='\u4e00-\u9fff'
for r in K:
    r['gkp']=r['kw']
    r['kw']=re.sub(r'(?<=['+CJK+r'0-9])\s+(?=['+CJK+r'])|(?<=['+CJK+r'])\s+(?=[0-9])','',r['kw'])
KV={r['norm']:r for r in K}
# roles
for c in CATS:
    rs=sorted([r for r in K if r['cat']==c],key=lambda r:-r['vol'])
    gen=[r for r in rs if r['sub'] in ('通用','推介','人群（學生／兒童）','材質／技術','款式（分層／分格）')]
    nf=[r for r in rs if r['sub']!='問題／評價（FAQ）']
    mainr=gen[0] if gen and gen[0]['vol']>=50 else nf[0]
    i=0
    for r in rs:
        if r['sub']=='問題／評價（FAQ）': r['role']='FAQ'; continue
        if r is mainr: r['role']='主要'; continue
        r['role']='次要' if i<6 and r['vol']>=20 else '長尾'; i+=1
H2OF={c:t for c,t,*_ in OUTLINE if c}
for r in K:
    r['h2']='H2 10｜常見問題（FAQ）' if r['role']=='FAQ' else H2OF[r['cat']].split('：')[0]
for k in ['保溫食物','食物保溫','保溫保冷袋','保溫保鮮盒']:
    if k in KV: KV[k]['h2']+='；亦用於 H2 1 總覽'

# ---------------- Excel ----------------
wb=Workbook();HF=PatternFill('solid',fgColor='1A1A1A');HFont=Font(name='Arial',bold=True,color='F7CE46')
def sheet(ws,head,rows,widths):
    ws.append(head)
    for r in rows: ws.append(r)
    for c in ws[1]: c.fill=HF;c.font=HFont;c.alignment=Alignment(wrap_text=True,vertical='center')
    for row in ws.iter_rows(min_row=2):
        for c in row: c.font=Font(name='Arial');c.alignment=Alignment(wrap_text=True,vertical='top')
    for i,w in enumerate(widths,1): ws.column_dimensions[get_column_letter(i)].width=w
    ws.freeze_panes='B2';ws.auto_filter.ref=f"A1:{get_column_letter(len(head))}{ws.max_row}"
ws=wb.active;ws.title='關鍵字分類'
rows=sorted(K,key=lambda r:(r['cat'],{'主要':0,'次要':1,'長尾':2,'FAQ':3}[r['role']],-r['vol']))
sheet(ws,['類別代號','產品類別','關鍵字','GKP 原文','Avg. monthly searches','角色','細分','品牌','搜尋意圖','放置位置','Competition'],
      [[r['cat'],r['catname'],r['kw'],r['gkp'],r['vol'],r['role'],r['sub'],r['brand'],r['intent'],r['h2'],r['comp']] for r in rows],[9,24,30,30,12,8,18,18,22,30,12])
Y=PatternFill('solid',fgColor='FFF2A8')
for row in ws.iter_rows(min_row=2):
    if row[5].value=='主要':
        for c in row: c.fill=Y; c.font=Font(name='Arial',bold=True)
ws2=wb.create_sheet('類別總覽')
summ=[]
for c,name in CATS.items():
    rs=sorted([r for r in K if r['cat']==c],key=lambda r:-r['vol'])
    summ.append([c,name,len(rs),sum(r['vol'] for r in rs),'、'.join(f"{r['kw']}（{r['vol']}）" for r in rs[:6]),SHOP_CAT[c],H2OF[c]])
sheet(ws2,['類別代號','產品類別','關鍵字數','搜尋量合計','代表關鍵字（月搜）','網店分類參考','文章 H2'],summ,[9,24,9,11,60,50,50])
ws3=wb.create_sheet('產品對照表')
sheet(ws3,['類別','品牌','型號','容量／尺寸','重點規格','價錢（HKD）','網店','產品連結','備註'],
      [[CATS[p[0]]]+list(p[1:]) for p in PRODUCTS],[22,18,30,20,36,18,22,60,20])
for row in ws3.iter_rows(min_row=2):
    row[7].hyperlink=row[7].value;row[7].font=Font(name='Arial',color='0563C1',underline='single')
ws4=wb.create_sheet('建議新增KW（待KP）')
sheet(ws4,['類別代號','產品類別','建議關鍵字','原因'],
      [[c,CATS[c],k,'原有 GKP 清單沒有此字，需在 Keyword Planner 查詢搜尋量'] for c in SUGGEST for k in SUGGEST[c]],[9,24,24,50])
ws5=wb.create_sheet('說明')
for line in [['資料來源','Google Keyword Planner（保溫.xlsx，287 行，去除重複後 273 個字）'],['價錢日期',PRICE_DATE+'，於各網店產品頁記錄，以網店實時價錢為準'],['分類參考','HKTVmall、友和 YOHO、惠康、Thermos HK 官網的產品分類'],['黃色','每個產品類別的主要關鍵字'],['建議新增 KW','不在原有清單內，未有搜尋量數據，例如保暖袋、燜燒杯、保鮮盒']]:
    ws5.append(line)
ws5.column_dimensions['A'].width=14;ws5.column_dimensions['B'].width=90
for row in ws5.iter_rows():
    for c in row: c.font=Font(name='Arial',bold=(c.column==1))
xl=os.path.join(HERE,'保溫保鮮餐具_KW分類_2026-10-28.xlsx');wb.save(xl)

# ---------------- Word ----------------
doc=Document()
for s in doc.sections: s.left_margin=s.right_margin=Cm(2.2);s.top_margin=s.bottom_margin=Cm(2)
FONT='Microsoft JhengHei'
def setfont(style,size,bold=False,color=None):
    style.font.name=FONT;style.font.size=Pt(size);style.font.bold=bold
    style.element.rPr.rFonts.set(qn('w:eastAsia'),FONT)
    if color: style.font.color.rgb=RGBColor.from_string(color)
setfont(doc.styles['Normal'],11)
pf=doc.styles['Normal'].paragraph_format;pf.line_spacing=1.5;pf.space_after=Pt(8)
for lv,sz,co in [(1,18,'1A1A1A'),(2,15,'9A7B2E'),(3,12.5,'1A1A1A')]:
    st=doc.styles[f'Heading {lv}'];setfont(st,sz,True,co);st.paragraph_format.space_before=Pt(18 if lv<3 else 12);st.paragraph_format.space_after=Pt(8);st.paragraph_format.line_spacing=1.3
def P(t,bold_prefix=None,style=None):
    p=doc.add_paragraph(style=style)
    if bold_prefix: r=p.add_run(bold_prefix);r.bold=True
    p.add_run(t);return p
def B(t,bp=None): return P(t,bp,'List Bullet')
def shade(cell,fill):
    tcPr=cell._tc.get_or_add_tcPr();s=OxmlElement('w:shd');s.set(qn('w:val'),'clear');s.set(qn('w:color'),'auto');s.set(qn('w:fill'),fill);tcPr.append(s)
def link(par,url,text):
    rid=par.part.relate_to(url,docx.opc.constants.RELATIONSHIP_TYPE.HYPERLINK,is_external=True)
    h=OxmlElement('w:hyperlink');h.set(qn('r:id'),rid);r=OxmlElement('w:r');rp=OxmlElement('w:rPr')
    c=OxmlElement('w:color');c.set(qn('w:val'),'0563C1');u=OxmlElement('w:u');u.set(qn('w:val'),'single');rp.append(c);rp.append(u)
    t=OxmlElement('w:t');t.text=text;r.append(rp);r.append(t);h.append(r);par._p.append(h)
def table(head,rows,widths=None,links=None):
    t=doc.add_table(rows=1,cols=len(head));t.style='Table Grid'
    for i,h in enumerate(head):
        c=t.rows[0].cells[i];c.text='';rr=c.paragraphs[0].add_run(h);rr.bold=True;shade(c,'F3EFE6')
    for row in rows:
        cells=t.add_row().cells
        for i,v in enumerate(row):
            cells[i].text=''
            if links and i in links and v: link(cells[i].paragraphs[0],v[1],v[0])
            else: cells[i].paragraphs[0].add_run(str(v))
    for r in t.rows:
        for c in r.cells:
            for p in c.paragraphs:
                p.paragraph_format.line_spacing=1.25;p.paragraph_format.space_after=Pt(2)
                for run in p.runs: run.font.size=Pt(9.5)
    if widths:
        for r in t.rows:
            for i,w in enumerate(widths): r.cells[i].width=Cm(w)
    doc.add_paragraph()
def kwline(r): return f"{r['kw']}（{r['vol']:,}）"

doc.add_heading('保溫、保鮮及燜燒餐具 Blog：大綱及關鍵字規劃',1)
P(f'Kitchen AO Blog｜關鍵字資料：Google Keyword Planner（香港）｜產品價錢記錄日期：{PRICE_DATE}')
doc.add_heading('一、整頁 SEO 設定',2)
table(['項目','建議'],[
 ['H1','保溫飯盒、燜燒壺及保鮮用品選購全攻略（2026）'],
 ['SEO Title','【2026】保溫飯盒推介｜保溫便當盒、燜燒壺、保鮮盒及保溫袋選購指南'],
 ['Meta Description','比較象印、虎牌、膳魔師等保溫飯盒及燜燒壺，整理保鮮盒、佳能保鮮紙、保溫袋及保溫箱的價錢與選購重點，附學生及上班族帶飯建議。'],
 ['建議網址','/blog/thermal-lunch-box-guide/'],
 ['全文主關鍵字','保溫飯盒（原有清單沒有這個字的搜尋量，要先在 Keyword Planner 查詢）'],
 ['全文次關鍵字（月搜）','保溫袋（1,000）、保溫箱（480）、象印保溫飯盒（320）、佳能保鮮紙（590）、保溫盒（140）、學生保溫飯盒（110）、保溫便當盒（90）'],
],[4,13])
P('「象印保温壺」（1,900）是清單中最大的字，但大部分搜尋者想找的是飲品保溫壺，所以只放在 H2 3 的 H3 承接，不作全文主關鍵字。',bold_prefix='注意：')

doc.add_heading('二、產品類別及關鍵字分配',2)
P('參考 HKTVmall、友和 YOHO、惠康及 Thermos HK 的分類方式，把 273 個關鍵字（原清單 287 行，去除重複）分為 8 個產品類別，每個類別由一個 H2 負責，避免同一篇文章內的段落重複搶字。')
table(['類別','關鍵字數','月搜合計','網店分類參考','負責段落'],
 [[f"{c} {CATS[c]}",s[2],f"{s[3]:,}",SHOP_CAT[c],H2OF[c].split('｜')[0]] for c,s in zip(CATS,summ)],[4,1.6,1.8,6.5,3])

doc.add_heading('三、文章大綱',2)
for cat,h2,kws,desc,h3s in OUTLINE:
    doc.add_heading(h2,3)
    P(desc,bold_prefix='目的：')
    if cat:
        rs=[r for r in K if r['cat']==cat]
        main=[r for r in rs if r['role']=='主要'];sec=sorted([r for r in rs if r['role']=='次要'],key=lambda r:-r['vol'])
        lt=[r for r in rs if r['role']=='長尾'];fq=[r for r in rs if r['role']=='FAQ']
        B(TARGET[cat],'建議主攻字：')
        B('、'.join(kwline(r) for r in main),'主關鍵字（現有數據）：')
        if sec: B('、'.join(kwline(r) for r in sec),'次關鍵字：')
        if lt: B(f"{len(lt)} 個，月搜合計 {sum(r['vol'] for r in lt):,}（例如："+'、'.join(r['kw'] for r in sorted(lt,key=lambda r:-r['vol'])[:5])+'）','長尾關鍵字：')
        if fq:
            fv=sorted([r for r in fq if r['vol']>0],key=lambda r:-r['vol']);f0=len(fq)-len(fv)
            B('、'.join(kwline(r) for r in fv)+(f'；另有 {f0} 個暫時沒有搜尋量' if f0 else '')+'（放入 H2 10 FAQ）','問題字：')
        B('、'.join(SUGGEST[cat]),'建議補查（待 KP）：')
    else:
        B('、'.join(kwline(KV[n(k)]) if n(k) in KV else f'{k}（待 KP）' for k in kws),'使用關鍵字：')
    for h in h3s: B(h)
    if cat:
        ps=[p for p in PRODUCTS if p[0]==cat]
        if ps:
            p=doc.add_paragraph();r=p.add_run(f'產品選購快速對照表：{CATS[cat]}');r.bold=True
            table(['品牌','型號','容量','重點規格','價錢（HKD）','購買連結'],[[x[1],x[2],x[3],x[4],x[5],(x[6],x[7])] for x in ps],[2.3,3.4,2.2,4.2,2.3,2.4],links={5:None})
# fix link text per row (shop name)
doc.add_heading('四、FAQ 建議答案（書面語）',2)
FAQ=[('保溫飯盒可以直接放入微波爐嗎？','不可以。不銹鋼保溫飯盒會反射微波，可能產生火花並損壞微波爐。如需加熱，應把食物移到耐熱玻璃或標明可微波的 PP 容器，並在加熱前打開排氣孔或鬆開蓋子。部分品牌的內盒可以微波（例如象印 SL-NC09 的內盒，蓋除外），使用前要先看說明書。'),
 ('燜燒壺可以保冷或裝凍飲嗎？','可以。燜燒壺是雙層真空不銹鋼容器，同樣可以隔絕外界熱力。以膳魔師 JBT-400 為例，官方標示 6 小時後仍保持 11°C 以下，適合裝水果、乳酪或凍甜品。'),
 ('保溫飯盒為甚麼會有倒汗水？怎樣避免飯菜變爛？','熱飯菜密封後，蒸氣遇冷會在蓋底凝結成水滴，滴回飯菜令米飯變糊。方法：裝盒後先讓食物散熱 1 至 2 分鐘才蓋上；選用飯、餸分層的保溫便當盒；在最上層鋪一張廚房紙吸收水氣。'),
 ('便當盒有異味或膠圈發霉，應該怎樣清洗？','去異味：用溫水加少許梳打粉或白醋浸 30 分鐘，再沖洗晾乾。膠圈發霉：拆出矽膠圈，用稀釋的檸檬酸或白醋浸泡，再用軟毛牙刷輕刷。不要用鋼絲刷或強力清潔劑，以免損壞密封圈。'),
 ('保溫便當盒打不開怎麼辦？','熱食物冷卻後，盒內氣壓降低，蓋子會被吸緊。可以把飯盒放入溫水浸 1 至 2 分鐘，或按下排氣掣再打開。裝盒時不要裝得太滿，可以減少這個情況。'),
 ('保鮮紙可以放入微波爐嗎？','要選標明「微波爐適用」的保鮮紙（例如佳能微波爐保鮮紙），而且不要直接貼着食物表面，並留一個缺口排氣。高油高糖的食物溫度較高，最好改用微波爐專用蓋。')]
for q,a in FAQ:
    p=doc.add_paragraph();r=p.add_run('Q：'+q);r.bold=True;p.paragraph_format.space_after=Pt(2)
    P(a)
doc.add_heading('五、內鏈及 CTA',2)
for t in ['H2 8「保溫箱」→ Kitchen AO Chill 野餐盒 /product-category/party/chill-box/',
          'H2 9「派對食物保溫」→ 餐具及暖貼加配 /product-category/party-supplies/thin-crust-pizza/ 及 送貨需知 /delivery/',
          'H2 2「學生保溫飯盒」→ 日後的學校飯盒 Landing Page（網站架構圖已規劃）',
          '文末 CTA：「不想自己帶飯？公司午餐及派對可以選擇 Kitchen AO 到會」→ 公司到會 /corporate-catering-hk/']: B(t)
doc.add_heading('六、資料說明',2)
for t in [f'產品價錢於 {PRICE_DATE} 在網店產品頁記錄，網店價錢經常變動，上線前要再核對一次，並在對照表下方寫明「價錢更新日期」。',
          '部分價錢來自網店搜尋結果卡，未能打開完整產品頁核對，已在 Excel「產品對照表」備註欄註明。',
          'Lock & Lock、Ziploc、iwaki、Snapware、Thanko、Bruno 等品牌未能在香港網店確認現售價錢，所以未放入對照表。',
          '「保溫飯盒」「保鮮盒」「燜燒杯」「保暖袋」等大字不在原有清單內，已列在 Excel「建議新增KW（待KP）」分頁。']: B(t)
out=os.path.join(HERE,'保溫保鮮餐具_Blog大綱及KW規劃_2026-10-28.docx');doc.save(out)
print('ok',xl,out)
