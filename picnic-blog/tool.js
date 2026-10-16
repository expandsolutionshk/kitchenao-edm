(function(){
  var root=document.querySelector('.ao-picnic'); if(!root) return;
  var st={r:'all',car:false,pet:false,cats:[]};
  var chips=root.querySelectorAll('.pk-chip'), cards=root.querySelectorAll('.pk-card'), regs=root.querySelectorAll('.pk-region');
  function apply(){
    var shown=0;
    cards.forEach(function(c){
      var ok=(st.r==='all'||c.dataset.r===st.r)&&(!st.car||c.dataset.car==='1')&&(!st.pet||c.dataset.pet==='Y');
      if(ok&&st.cats.length){var cs=c.dataset.cats.split(' ');ok=st.cats.every(function(x){return cs.indexOf(x)>-1;});}
      c.style.display=ok?'':'none'; if(ok) shown++;
    });
    regs.forEach(function(r){var any=[].some.call(r.querySelectorAll('.pk-card'),function(c){return c.style.display!=='none';});r.style.display=any?'':'none';});
    var cnt=root.querySelector('#pkCount'); if(cnt) cnt.textContent=(shown===cards.length?'顯示全部 ':'符合條件：')+shown+' 個地點';
    var em=root.querySelector('#pkEmpty'); if(em) em.hidden=shown>0;
  }
  chips.forEach(function(b){b.addEventListener('click',function(){
    var f=b.dataset.f,v=b.dataset.v;
    if(f==='r'){st.r=v;root.querySelectorAll('.pk-chip[data-f="r"]').forEach(function(x){x.classList.toggle('on',x===b);});}
    else if(f==='car'){st.car=!st.car;b.classList.toggle('on',st.car);}
    else if(f==='pet'){st.pet=!st.pet;b.classList.toggle('on',st.pet);}
    else if(f==='cat'){var i=st.cats.indexOf(v);if(i>-1)st.cats.splice(i,1);else st.cats.push(v);b.classList.toggle('on',i<0);}
    apply();
  });});
  var rs=root.querySelector('#pkReset'); if(rs) rs.addEventListener('click',function(){st={r:'all',car:false,pet:false,cats:[]};chips.forEach(function(x){x.classList.toggle('on',x.dataset.f==='r'&&x.dataset.v==='all');});apply();});
  // 實時車位（運輸署開放數據；如瀏覽器封鎖跨域，則開新分頁顯示原始數據）
  root.querySelectorAll('.pk-vac').forEach(function(b){b.addEventListener('click',function(){
    var out=b.nextElementSibling; out.textContent='讀取中…';
    fetch(b.dataset.src).then(function(r){return r.json();}).then(function(j){
      var v=null;try{var cp=j.car_park[0];cp.vehicle_type.forEach(function(t){if(t.type==='P'){v=t.service_category[0].vacancy;}});}catch(e){}
      out.textContent=(v===null||v===undefined)?'暫無數據':(v<0?'暫無數據':'空位：'+v);
    }).catch(function(){out.innerHTML='<a href="'+b.dataset.src+'" target="_blank" rel="noopener">開啟數據</a>';});
  });});
  // 寵物共享範圍地圖 pop up
  var md=root.querySelector('#pkModal');
  if(md){var img=md.querySelector('img'),tt=md.querySelector('.pk-mt');
    root.querySelectorAll('.pk-mapbtn').forEach(function(b){b.addEventListener('click',function(){img.src=b.dataset.img;tt.textContent=b.dataset.t;md.hidden=false;});});
    function cl(){md.hidden=true;img.removeAttribute('src');}
    md.querySelector('.pk-mx').addEventListener('click',cl);md.addEventListener('click',function(e){if(e.target===md)cl();});
    document.addEventListener('keydown',function(e){if(e.key==='Escape'&&!md.hidden)cl();});}
  apply();
})();
