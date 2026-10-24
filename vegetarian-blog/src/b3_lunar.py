# -*- coding: utf-8 -*-
# 初一十五自動日子表
# 資料：香港天文台〈公曆與農曆日期對照表〉2026–2030，只記錄每個農曆月「初一」的公曆日期。
# 公式：十五 = 初一 + 14 日；農曆某日 = 初一 + (日數 − 1)。
# 每年天文台公布新一年對照表後，在 L 尾加上該年 12–13 個初一即可。
import json, datetime as dt

L = [('2026-01-19','十二月'),('2026-02-17','正月'),('2026-03-19','二月'),('2026-04-17','三月'),('2026-05-17','四月'),('2026-06-15','五月'),
('2026-07-14','六月'),('2026-08-13','七月'),('2026-09-11','八月'),('2026-10-10','九月'),('2026-11-09','十月'),('2026-12-09','十一月'),
('2027-01-08','十二月'),('2027-02-06','正月'),('2027-03-08','二月'),('2027-04-07','三月'),('2027-05-06','四月'),('2027-06-05','五月'),
('2027-07-04','六月'),('2027-08-02','七月'),('2027-09-01','八月'),('2027-09-30','九月'),('2027-10-29','十月'),('2027-11-28','十一月'),
('2027-12-28','十二月'),('2028-01-26','正月'),('2028-02-25','二月'),('2028-03-26','三月'),('2028-04-25','四月'),('2028-05-24','五月'),
('2028-06-23','閏五月'),('2028-07-22','六月'),('2028-08-20','七月'),('2028-09-19','八月'),('2028-10-18','九月'),('2028-11-16','十月'),
('2028-12-16','十一月'),('2029-01-15','十二月'),('2029-02-13','正月'),('2029-03-15','二月'),('2029-04-14','三月'),('2029-05-13','四月'),
('2029-06-12','五月'),('2029-07-11','六月'),('2029-08-10','七月'),('2029-09-08','八月'),('2029-10-08','九月'),('2029-11-06','十月'),
('2029-12-05','十一月'),('2030-01-04','十二月'),('2030-02-03','正月'),('2030-03-04','二月'),('2030-04-03','三月'),('2030-05-02','四月'),
('2030-06-01','五月'),('2030-07-01','六月'),('2030-07-30','七月'),('2030-08-29','八月'),('2030-09-27','九月'),('2030-10-27','十月'),
('2030-11-25','十一月'),('2030-12-25','十二月')]

# 食齋節日：(農曆月, 日, 名稱)
FEST = [('正月',1,'農曆新年年初一'),('二月',19,'觀音誕'),('四月',8,'佛誕（公眾假期）'),('六月',19,'觀音誕'),('七月',15,'盂蘭節'),('八月',15,'中秋節'),('九月',19,'觀音誕')]
DAYN = {1:'初一',8:'初八',15:'十五',19:'十九'}
WD = '一二三四五六日'

def _d(s): return dt.date.fromisoformat(s)
def lunar_year(d1, m):  # 十一月、十二月在公曆 1–2 月出現時屬上一個農曆年
    return d1.year - 1 if m in ('十一月','十二月') and d1.month <= 2 else d1.year
def fmt(d, ref_year):
    y = f'{d.year} 年 ' if d.year != ref_year else ''
    return f'{y}{d.month} 月 {d.day} 日（{WD[d.weekday()]}）'

def months(today, n=12):
    idx = max(i for i, (s, _) in enumerate(L) if _d(s) <= today)
    return [(_d(s), m) for s, m in L[idx:idx + n]]

def static_rows(today):
    out, nxt = [], None
    for d1, m in months(today):
        ly = lunar_year(d1, m); cells = []
        for d in (d1, d1 + dt.timedelta(days=14)):
            tag = ''
            if d < today: tag = ' <span class="b3-past">已過</span>'
            elif nxt is None: nxt = d; tag = ' <span class="b3-nx">下一個</span>'
            cls = ' class="b3-p"' if d < today else ''
            cells.append(f'<td{cls}>{fmt(d, ly)}{tag}</td>')
        out.append(f'<tr><td><b>農曆{m}</b><br><small class="b3-y">{ly} 年</small></td>{"".join(cells)}</tr>')
    return ''.join(out)

def static_fest(today):
    out = []
    for d1, m in months(today):
        ly = lunar_year(d1, m)
        for fm, day, name in FEST:
            if fm == m:
                d = d1 + dt.timedelta(days=day - 1)
                if d >= today:
                    out.append(f'<tr><td><b>{name}</b></td><td>農曆{m}{DAYN[day]}</td><td>{fmt(d, 0)}</td></tr>')
    return ''.join(out)

# 瀏覽器端：按讀者「今日」（香港時間）重新計算
JS = r'''<script>(function(){
var L=__L__,F=__F__,DN={1:'初一',8:'初八',15:'十五',19:'十九'},WD='日一二三四五六';
function P(s){var a=s.split('-');return Date.UTC(+a[0],a[1]-1,+a[2]);}
function A(t,n){return t+n*864e5;}
var hk=new Intl.DateTimeFormat('en-CA',{timeZone:'Asia/Hong_Kong',year:'numeric',month:'2-digit',day:'2-digit'}).format(new Date());
var T=P(hk);
function ly(t,m){var d=new Date(t);return (m=='十一月'||m=='十二月')&&d.getUTCMonth()<2?d.getUTCFullYear()-1:d.getUTCFullYear();}
function f(t,ry){var d=new Date(t);return (d.getUTCFullYear()!=ry?d.getUTCFullYear()+' 年 ':'')+(d.getUTCMonth()+1)+' 月 '+d.getUTCDate()+' 日（'+WD[d.getUTCDay()]+'）';}
var i=-1;for(var k=0;k<L.length;k++){if(P(L[k][0])<=T)i=k;}
if(i<0)return;var M=L.slice(i,i+12);if(!M.length)return;
var rows='',fr='',nx=null,nxl='';
M.forEach(function(x){var t1=P(x[0]),m=x[1],y=ly(t1,m),c='';
 [[t1,'初一'],[A(t1,14),'十五']].forEach(function(p){var t=p[0],tag='';
  if(t<T)tag=' <span class="b3-past">已過</span>';else if(nx===null){nx=t;nxl=y+' 年農曆'+m+p[1];tag=' <span class="b3-nx">下一個</span>';}
  c+='<td'+(t<T?' class="b3-p"':'')+'>'+f(t,y)+tag+'</td>';});
 rows+='<tr><td><b>農曆'+m+'</b><br><small class="b3-y">'+y+' 年</small></td>'+c+'</tr>';
 F.forEach(function(e){if(e[0]==m){var t=A(t1,e[1]-1);if(t>=T)fr+='<tr><td><b>'+e[2]+'</b></td><td>農曆'+m+DN[e[1]]+'</td><td>'+f(t,0)+'</td></tr>';}});});
var a=document.querySelector('#b3-dates tbody');if(a)a.innerHTML=rows;
var b=document.querySelector('#b3-fest tbody');if(b&&fr)b.innerHTML=fr;
var n=document.getElementById('b3-next');
if(n&&nx!==null){var dd=Math.round((nx-T)/864e5);n.innerHTML='<b>'+f(nx,0)+'</b>，即'+nxl+(dd===0?'（就是今日）':'，還有 <b>'+dd+'</b> 日');}
})();</script>'''

def js():
    return (JS.replace('__L__', json.dumps(L, ensure_ascii=False))
              .replace('__F__', json.dumps(FEST, ensure_ascii=False)).replace('\n', ''))

def next_text(today):
    for d1, m in months(today):
        for d, nm in ((d1, '初一'), (d1 + dt.timedelta(days=14), '十五')):
            if d >= today:
                dd = (d - today).days
                return f'<b>{fmt(d, 0)}</b>，即{lunar_year(d1, m)} 年農曆{m}{nm}' + ('（就是今日）' if dd == 0 else f'，還有 <b>{dd}</b> 日')
