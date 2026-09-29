/* Kitchen AO 場景 Landing Page 共用邏輯：篩選、快速搜尋、套餐及單品、各 section */
(function(){
var D=AO_DATA, $=function(s,r){return (r||document).querySelector(s)}, $$=function(s,r){return [].slice.call((r||document).querySelectorAll(s))};
var cur=D.scenes[0];
function money(n){return n==null?'按人數計價':'$'+n.toLocaleString('en-US');}
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]});}
function ymd(d){return d.toISOString().slice(0,10);}
function addDays(n){var d=new Date();d.setHours(12,0,0,0);d.setDate(d.getDate()+n);return ymd(d);}

/* ---------- 篩選 tag ---------- */
function renderFilters(){
  $$('[data-ao="filters"]').forEach(function(box){
    box.innerHTML=D.scenes.map(function(s){return '<button type="button" class="ao-f'+(s.id===cur.id?' on':'')+'" data-id="'+s.id+'"><span class="ao-f-ic">'+s.icon+'</span><span class="ao-f-tx">'+s.label+'</span></button>';}).join('');
    $$('.ao-f',box).forEach(function(b){b.onclick=function(){setScene(b.dataset.id,true);};});
  });
}
function setScene(id,fromFilter){
  cur=D.scenes.filter(function(s){return s.id===id;})[0]||D.scenes[0];
  document.documentElement.style.setProperty('--sc',cur.color);
  document.body.setAttribute('data-scene',cur.id);
  $$('.ao-f').forEach(function(b){b.classList.toggle('on',b.dataset.id===cur.id);});
  var t=$('#qs-type'); if(t) t.value=cur.id;
  renderHero(); renderPkgs(); renderSingles(); resetQS(); startCountdown();
  if(fromFilter){var a=$('[data-ao="filters"] .ao-f.on'); if(a&&a.scrollIntoView) a.scrollIntoView({inline:'center',block:'nearest',behavior:'smooth'});}
}

/* ---------- Hero ---------- */
function renderHero(){
  $$('[data-ao="title"]').forEach(function(e){e.textContent=cur.title;});
  $$('[data-ao="sub"]').forEach(function(e){e.textContent=cur.sub;});
  $$('[data-ao="tag"]').forEach(function(e){e.textContent=cur.icon+' '+cur.label+'到會';});
  $$('[data-ao="hero-img"]').forEach(function(e){e.src=cur.hero;e.alt=cur.title;});
  $$('[data-ao="stats"]').forEach(function(e){e.innerHTML=cur.stats.map(function(s){return '<span class="ao-stat">'+esc(s)+'</span>';}).join('');});
  $$('[data-ao="promo-text"]').forEach(function(e){e.innerHTML='<b>'+esc(cur.promo.code)+'</b> '+esc(cur.promo.text);});
}

/* ---------- 優惠倒數 ---------- */
var cdT;
function startCountdown(){
  clearInterval(cdT);
  function tick(){
    var end=new Date(cur.promo.until+'T23:59:59+08:00').getTime(), s=Math.max(0,Math.floor((end-Date.now())/1000));
    var v=[Math.floor(s/86400),Math.floor(s%86400/3600),Math.floor(s%3600/60),s%60];
    $$('[data-ao="countdown"]').forEach(function(e){
      e.innerHTML=s?['天','時','分','秒'].map(function(u,i){return '<span class="ao-cd"><b>'+(v[i]<10?'0':'')+v[i]+'</b>'+u+'</span>';}).join(''):'<span class="ao-cd-end">優惠已結束</span>';
    });
  }
  tick(); cdT=setInterval(tick,1000);
}

/* ---------- 快速搜尋 ---------- */
function initQS(){
  var t=$('#qs-type'); if(!t) return;
  t.innerHTML=D.scenes.map(function(s){return '<option value="'+s.id+'">'+s.icon+' '+s.label+'</option>';}).join('');
  t.onchange=function(){setScene(t.value);};
  var d=$('#qs-date'); if(d){d.min=addDays(1);}
  var f=$('[data-ao="qs-form"]'); if(f) f.onsubmit=function(e){e.preventDefault();runQS();};
  $$('[data-ao="qs-again"]').forEach(function(b){b.onclick=resetQS;});
}
function resetQS(){
  var f=$('[data-ao="qs-form"]'), r=$('[data-ao="qs-result"]');
  if(f) f.hidden=false; if(r){r.hidden=true;}
  var m=$('[data-ao="qs-msg"]'); if(m) m.textContent='';
}
function recommend(n){
  var all=[];
  cur.series.forEach(function(se){se.items.forEach(function(it){all.push({s:se.name,n:it[0],min:it[1],max:it[2],p:it[3],img:it[4],url:it[5]});});});
  if(cur.perHead){return all.slice(0,3).map(function(x){x.note=x.p?('共約 $'+(x.p*n).toLocaleString('en-US')+'（'+n+' 份）'):'';x.fit='按份數訂購';return x;});}
  var fit=all.filter(function(x){return n>=x.min&&n<=x.max;});
  fit.forEach(function(x){x.fit='最合適';x.note=x.p?('人均約 $'+Math.round(x.p/Math.min(n,x.max))):'';});
  if(fit.length<3){
    var rest=all.filter(function(x){return fit.indexOf(x)<0;}).sort(function(a,b){return Math.abs(a.min-n)-Math.abs(b.min-n);});
    rest.slice(0,3-fit.length).forEach(function(x){x.fit=x.min>n?'份量較多':(x.max<n?'可加配':'參考');x.note=x.min>n?'適合 '+x.min+'–'+x.max+' 人':'可配搭其他套餐';fit.push(x);});
  }
  return fit.slice(0,3);
}
function runQS(){
  var n=parseInt(($('#qs-n')||{}).value,10), date=($('#qs-date')||{}).value, msg=$('[data-ao="qs-msg"]');
  if(!n||n<1){msg.textContent='請輸入活動人數';return;}
  if(!date){msg.textContent='請選擇活動日期';return;}
  var notes=[], ok=true;
  if(cur.window&&(date<cur.window[0]||date>cur.window[1])){ok=false;notes.push('<p class="ao-qs-warn">⚠️ '+esc(cur.label)+'套餐供應期為 '+cur.window[0]+' 至 '+cur.window[1]+'，所選日期未有供應。以下為參考，或可改選其他場景。</p>');}
  if(date<addDays(cur.lead)){notes.push('<p class="ao-qs-warn">⏱ 此類訂單建議最少提前 '+cur.lead+' 日預訂，急單請 <a href="'+WA+'" target="_blank" rel="noopener">WhatsApp</a> 查詢。</p>');}
  else if(ok){notes.push('<p class="ao-qs-ok">✅ '+date+' 可預訂'+esc(cur.label)+'餐單</p>');}
  if(date<=cur.promo.until&&ymd(new Date())<=cur.promo.until){notes.push('<p class="ao-qs-ok">🎟 優惠碼 <b>'+esc(cur.promo.code)+'</b> 適用：'+esc(cur.promo.text)+'</p>');}
  else{notes.push('<p class="ao-qs-muted">優惠碼 '+esc(cur.promo.code)+' 不適用於所選日期（有效期至 '+cur.promo.until+'）</p>');}
  var recs=recommend(n);
  var r=$('[data-ao="qs-result"]');
  $('[data-ao="qs-list"]',r).innerHTML='<p class="ao-qs-head">'+n+' 人・'+esc(cur.label)+'・'+date+'</p>'+notes.join('')+
    recs.map(function(x){return '<a class="ao-qs-item" href="'+x.url+'" target="_blank" rel="noopener"><img src="'+x.img+'" alt="'+esc(x.n)+'" loading="lazy"><span class="ao-qs-tx"><em>'+esc(x.fit)+'</em><b>'+esc(x.n)+'</b><span>'+money(x.p)+(x.note?'・'+esc(x.note):'')+'</span></span><span class="ao-qs-go">›</span></a>';}).join('')+
    '<a class="ao-qs-wa" href="'+WA+'?text='+encodeURIComponent('你好，我想查詢'+cur.label+'到會：'+n+' 人，日期 '+date)+'" target="_blank" rel="noopener">💬 WhatsApp 按此組合查詢</a>';
  $('[data-ao="qs-form"]').hidden=true; r.hidden=false;
}

/* ---------- 套餐（一個系列一行） ---------- */
function card(it,cls){
  return '<a class="'+(cls||'ao-pc')+'" href="'+it[5]+'" target="_blank" rel="noopener"><span class="ao-pc-img"><img src="'+it[4]+'" alt="'+esc(it[0])+'" loading="lazy"></span><span class="ao-pc-body"><b class="ao-pc-nm">'+esc(it[0])+'</b><span class="ao-pc-pax">'+(it[2]>=999?it[1]+' 人起':it[1]+'–'+it[2]+' 人')+'</span><span class="ao-pc-price">'+money(it[3])+(cur.perHead&&it[3]?' / 份':'')+'</span></span></a>';
}
function renderPkgs(){
  $$('[data-ao="pkgs"]').forEach(function(box){
    box.innerHTML=cur.series.map(function(se,i){
      return '<div class="ao-series"><div class="ao-series-hd"><div><h3>'+esc(se.name)+'</h3><p>'+esc(se.desc)+'</p></div><a class="ao-series-all" href="'+se.cat+'" target="_blank" rel="noopener">查看全部 ›</a></div>'+
      '<div class="ao-row"><button type="button" class="ao-rb prev" aria-label="向左">‹</button><div class="ao-track">'+se.items.map(function(it){return card(it);}).join('')+'</div><button type="button" class="ao-rb next" aria-label="向右">›</button></div></div>';
    }).join('');
    $$('.ao-row',box).forEach(function(row){
      var tr=$('.ao-track',row);
      $('.prev',row).onclick=function(){tr.scrollBy({left:-tr.clientWidth*0.8,behavior:'smooth'});};
      $('.next',row).onclick=function(){tr.scrollBy({left:tr.clientWidth*0.8,behavior:'smooth'});};
      function upd(){var o=tr.scrollWidth>tr.clientWidth+4;row.classList.toggle('ovf',o);}
      setTimeout(upd,60); window.addEventListener('resize',upd);
    });
  });
}
function renderSingles(){
  $$('[data-ao="singles"]').forEach(function(box){
    box.innerHTML=cur.singles.map(function(k){var s=D.singles[k];return '<a class="ao-sg" href="'+s[2]+'" target="_blank" rel="noopener"><img src="'+s[1]+'" alt="'+esc(s[0])+'" loading="lazy"><span><em>'+esc(s[3])+'</em><b>'+esc(s[0])+'</b></span></a>';}).join('');
  });
}

/* ---------- 靜態 sections ---------- */
var BOSS='data:image/svg+xml;utf8,'+encodeURIComponent('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 260"><rect width="200" height="260" fill="none"/><circle cx="100" cy="70" r="42" fill="#cfc6b3"/><path d="M20 260c0-70 36-110 80-110s80 40 80 110z" fill="#cfc6b3"/><text x="100" y="215" font-size="16" text-anchor="middle" fill="#8a7f6b" font-family="sans-serif">老闆相片</text></svg>');
function renderStatic(){
  $$('[data-ao="trust"]').forEach(function(b){b.innerHTML=
    '<div class="ao-tc"><p class="ao-tc-k">服務人數超過</p><p class="ao-tc-v">XX 萬+</p><p class="ao-tc-note">（數字待提供）</p><div class="ao-tc-foot">🍽 全港公司、學校、家庭派對</div></div>'+
    '<div class="ao-tc"><p class="ao-tc-k">餐飲團隊經驗</p><p class="ao-tc-v">10 年+</p><div class="ao-tc-boss"><img src="'+BOSS+'" alt="創辦人（相片待提供）"><img src="'+BOSS+'" alt="主廚（相片待提供）"></div><div class="ao-tc-foot">👨‍🍳 創辦人及主廚（姓名待提供）</div></div>'+
    '<div class="ao-tc"><p class="ao-tc-k">每月最高賣出</p><p class="ao-tc-v">1,000+ 單</p><div class="ao-tc-foot">🏆 全港到會訂單</div></div>';});
  $$('[data-ao="photos"]').forEach(function(b){b.innerHTML=D.photos.map(function(p){return '<figure class="ao-ph"><img src="'+p+'" alt="Kitchen AO 客人到會回圖" loading="lazy"><figcaption>示例相片</figcaption></figure>';}).join('');});
  $$('[data-ao="reviews"]').forEach(function(b){b.innerHTML='<div class="ao-rv-sum"><b>4.9</b><span>★★★★★</span><p>Google 評分（示例，請換上實際評分及評論數）</p></div>'+
    [1,2,3].map(function(i){return '<div class="ao-rv"><div class="ao-rv-top"><span class="ao-rv-av">G</span><div><b>Google 用戶（示例 '+i+'）</b><span>★★★★★</span></div></div><p>此處放入真實 Google 評論內容。建議挑選提及準時送達、份量及味道的評論，並附上評論日期。</p></div>';}).join('');});
  $$('[data-ao="kol"]').forEach(function(b){b.innerHTML=[1,2,3].map(function(i){return '<div class="ao-kol"><div class="ao-kol-img">KOL 相片 '+i+'</div><b>@KOL 帳號（示例）</b><p>KOL 分享內容摘要，附原帖連結。</p></div>';}).join('');});
  $$('[data-ao="services"]').forEach(function(b){b.innerHTML=D.services.map(function(s){return '<a class="ao-sv" href="'+s[3]+'" target="_blank" rel="noopener"><span class="ao-sv-ic">'+s[0]+'</span><b>'+esc(s[1])+'</b><span>'+esc(s[2])+'</span></a>';}).join('');});
  $$('[data-ao="clients"]').forEach(function(b){b.innerHTML='<img src="'+D.clients+'" alt="Kitchen AO 合作夥伴及服務機構展示 — 企業、醫療、教育及公共機構" loading="lazy">';});
  $$('[data-ao="reels"]').forEach(function(b){
    b.innerHTML=D.reels.map(function(u,i){return u?'<div class="ao-reel"><blockquote class="instagram-media" data-instgrm-permalink="'+u+'" data-instgrm-version="14" style="margin:0;width:100%;min-width:0;"></blockquote></div>':'<div class="ao-reel ao-reel-ph">Instagram Reel '+(i+1)+'<br><small>（請提供 Reel 連結）</small></div>';}).join('');
    var s=document.createElement('script');s.async=true;s.src='https://www.instagram.com/embed.js';document.body.appendChild(s);
  });
}

document.addEventListener('DOMContentLoaded',function(){
  renderFilters(); initQS(); renderStatic(); setScene(cur.id);
});
})();
