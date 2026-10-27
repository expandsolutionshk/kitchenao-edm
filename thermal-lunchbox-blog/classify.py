import openpyxl,glob,re,json
f=glob.glob('/sessions/great-festive-darwin/mnt/uploads/*保溫 (1).xlsx')[0]
R=[r for r in openpyxl.load_workbook(f,read_only=True).worksheets[0].iter_rows(values_only=True) if r[0]][1:]
n=lambda k:re.sub(r'\s+','',k).lower()
rows={};
for r in R:
    k=n(r[0]); v=int(r[3] or 0)
    if k in rows: rows[k]['vol']=max(rows[k]['vol'],v); continue
    rows[k]=dict(kw=r[0].strip(),norm=k,vol=v,comp=r[6] or '',ci=r[7])
CATS={
 'C1':'保溫飯盒／保溫便當盒','C2':'燜燒壺／燜燒杯／保溫壺','C3':'加熱飯盒（USB／插電）',
 'C4':'保鮮盒／密實盒','C5':'保鮮紙／保鮮膜／保鮮貼','C6':'保鮮袋／密實袋','C7':'保溫袋／保冷袋／保溫箱','C8':'保溫碗／保溫盤／食物保溫方法'}
BR=[('象印','象印'),('虎牌','虎牌 Tiger'),('tiger','虎牌 Tiger'),('thermos','膳魔師 Thermos'),('膳魔師','膳魔師 Thermos'),('skater','Skater'),('muji','MUJI'),('三光','三光'),('仙德曼','仙德曼 Sadomain'),('sadomain','仙德曼 Sadomain'),('asvel','Asvel'),('luntus','Asvel'),('康寧','康寧 Corelle/Snapware'),('snapware','康寧 Corelle/Snapware'),('swanz','Swanz'),('monbento','Monbento'),('vaya','Vaya'),('mosh','Mosh'),('sabu','Sabu'),('omiebox','Omiebox'),('thanko','Thanko'),('bruno','Bruno'),('駱駝','駱駝牌'),('佳能','佳能 Glad'),('glad','佳能 Glad'),('pressnseal','佳能 Glad'),('woky','Woky'),('momo','momo（台灣網店）')]
def brand(k):
    for a,b in BR:
        if a in k: return b
    return ''
def cat(k):
    if re.search(r'usb|插電|加熱|thanko|bruno',k) and 'luntus' not in k: return 'C3'
    if re.search(r'保鮮紙|保鮮膜|保鲜膜|保鮮貼|pressnseal|神奇密封|神奇保鮮紙',k): return 'C5'
    if re.search(r'保鮮袋|保鲜袋|密實袋',k): return 'C6'
    if re.search(r'保鮮盒|密實盒|飯盒分隔',k) and '保溫' not in k: return 'C4'
    if k in ('glad保鮮','佳能保鮮','glad保鲜膜'): return 'C5'
    if re.search(r'袋|保溫箱',k): return 'C7'
    if re.search(r'壺|壶|燜燒|悶燒|保溫罐|提鍋|保溫杯',k): return 'C2'
    if re.search(r'保溫碗|保溫盤|食物保溫|飯菜保溫|保溫食物',k) and '盒' not in k: return 'C8'
    return 'C1'
def sub(k,c):
    b=brand(k)
    if re.search(r'打不開|缺點|評價|心得|開箱|ptt|殘膠|材質|用法|耐熱|微波|方法|門市|size',k): return '問題／評價（FAQ）'
    if b: return '品牌'
    if re.search(r'學生|小學|兒童',k): return '人群（學生／兒童）'
    if re.search(r'304|316|不銹鋼|不鏽鋼|陶瓷|玻璃|真空',k): return '材質／技術'
    if re.search(r'層|格|分隔|方形|長方形|單層',k): return '款式（分層／分格）'
    if re.search(r'推薦|推介|好用|效果好',k): return '推介'
    return '通用'
for r in rows.values():
    r['cat']=cat(r['norm']);r['catname']=CATS[r['cat']];r['brand']=brand(r['norm']);r['sub']=sub(r['norm'],r['cat'])
    r['intent']='Informational' if r['sub']=='問題／評價（FAQ）' or r['cat']=='C8' else ('Commercial' if r['sub'] in ('推介','品牌') else 'Commercial／Transactional')
json.dump(list(rows.values()),open('/tmp/kw_th.json','w'),ensure_ascii=False)
from collections import defaultdict
S=defaultdict(lambda:[0,0])
for r in rows.values(): S[r['cat']][0]+=1;S[r['cat']][1]+=r['vol']
print(len(rows));[print(c,CATS[c],S[c]) for c in sorted(S)]
for c in sorted(CATS):
  rs=sorted([r for r in rows.values() if r['cat']==c],key=lambda r:-r['vol'])
  print(c,' / '.join(f"{r['kw']}:{r['vol']}[{r['sub'][:2]}]" for r in rs[:25]))
