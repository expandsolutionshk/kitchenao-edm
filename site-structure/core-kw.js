try{mermaid.initialize({startOnLoad:true,securityLevel:'loose',flowchart:{htmlLabels:true}});}catch(e){console.warn('mermaid not loaded')}
const sel=document.getElementById('pg'),lang=document.getElementById('lang');
Object.entries(D.pages).forEach(([k,v])=>{if(!D.rows.some(r=>r.pg===k))return;const o=document.createElement('option');o.value=k;o.textContent=k+' '+v;sel.appendChild(o)});
const f=x=>x==null||x===''?'':Number(x).toLocaleString();
const C=[['kw','關鍵字',1],['pg','頁面'],['typ','類型'],['lang','語言'],['vol','Vol'],['kd','KD'],['gi','GSC 曝光'],['gp','GSC 排名'],['pt','PT 10-24'],['ao','AO'],['km','Kama'],['br','Bear'],['now','現時排名頁（GSC 10-30）'],['src','來源'],['use','用法']];
const NUM=['vol','kd','gi','gp','pt','ao','km','br'];let sk=null,sd=-1,cur=[];
function draw(){const pg=sel.value,lg=lang.value,q=document.getElementById('q').value.trim().toLowerCase();
let rs=D.rows.filter(r=>(!pg||r.pg===pg)&&(!lg||r.lang===lg)&&(!q||r.kw.toLowerCase().includes(q)));
if(sk)rs.sort((a,b)=>{let x=a[sk],y=b[sk];if(NUM.includes(sk)){if(x==null&&y==null)return 0;if(x==null)return 1;if(y==null)return -1;return (x-y)*sd}return String(x||'').localeCompare(String(y||''),'zh-HK')*sd});
else rs.sort((a,b)=>((a.pg==='X')-(b.pg==='X'))||(b.vol||0)-(a.vol||0)||(b.gi||0)-(a.gi||0));
cur=rs;
document.getElementById('tb').innerHTML='<tr>'+C.map(([k,t])=>`<th class="s${sk===k?' on':''}" data-k="${k}">${t} <i>${sk===k?(sd>0?'▲':'▼'):'⇅'}</i></th>`).join('')+'</tr>'+
rs.map(r=>'<tr>'+C.map(([k,t,mk])=>NUM.includes(k)?`<td class=n>${f(r[k])}</td>`:(k==='pg'?`<td title="${D.pages[r.pg]||''}">${r.pg}</td>`:`<td>${mk&&r.typ==='主要'?'<mark>'+r[k]+'</mark>':(r[k]??'')}</td>`)).join('')+'</tr>').join('');
document.querySelectorAll('#tb th.s').forEach(t=>t.onclick=()=>{const k=t.dataset.k;if(sk===k)sd=-sd;else{sk=k;sd=NUM.includes(k)?(['gp','pt','ao','km','br','kd'].includes(k)?1:-1):1}draw()});
document.getElementById('cnt').textContent=rs.length+' 項';}
function csv(){const esc=v=>{v=v==null?'':String(v);return /[",\n]/.test(v)?'"'+v.replace(/"/g,'""')+'"':v};
const head=C.map(c=>c[1]);head.splice(2,0,'頁面名稱');
const lines=[head.map(esc).join(',')].concat(cur.map(r=>{const v=C.map(([k])=>r[k]);v.splice(2,0,D.pages[r.pg]||'');return v.map(esc).join(',')}));
const b=new Blob(['﻿'+lines.join('\n')],{type:'text/csv;charset=utf-8'});const a=document.createElement('a');
a.href=URL.createObjectURL(b);a.download=`核心頁面KW${sel.value?'_'+sel.value:''}.csv`;document.body.appendChild(a);a.click();a.remove();}
sel.onchange=draw;lang.onchange=draw;document.getElementById('q').oninput=draw;document.getElementById('dl').onclick=csv;
document.getElementById('cp').onclick=()=>{const t=document.getElementById('seed');t.select();navigator.clipboard?navigator.clipboard.writeText(t.value):document.execCommand('copy')};
document.querySelectorAll('.more').forEach(b=>b.onclick=()=>{sel.value=b.dataset.pg;draw();document.getElementById('all').scrollIntoView({behavior:'smooth'})});
draw();
