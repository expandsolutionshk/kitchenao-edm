<script>
window.AO_VOTE_ENDPOINT = "https://script.google.com/macros/s/AKfycbys2loW9LmKPHALbYjBiM11jtbQTD2r6vaI6GCJydA-IBQgzhRsyzufKeiZSMwE6z2R/exec";
window._aoUp=0; window._aoDown=0;
function aoRender(){var up=window._aoUp||0,down=window._aoDown||0,total=up+down;var r=document.getElementById('aoRate');if(!r)return;if(total>0){var p=Math.round(up/total*100);document.getElementById('aoRateFill').style.width=p+'%';document.getElementById('aoRatePct').textContent=p+'%';document.getElementById('aoRateTotal').textContent='共 '+total+' 票';r.style.display='block';}else{r.style.display='none';}}
window.aoCounts=function(res){if(!res||!res.ok)return;window._aoUp=res.up||0;window._aoDown=res.down||0;aoRender();};
(function(){var s=document.createElement('script');s.src=window.AO_VOTE_ENDPOINT+'?callback=aoCounts&url='+encodeURIComponent(location.href);document.body.appendChild(s);})();
function aoThanks(){var q=document.getElementById('aoQ');if(q)q.textContent='🙏 感謝你的回饋！';['aoUp','aoDown'].forEach(function(id){var b=document.getElementById(id);if(b){b.disabled=true;b.style.opacity='.55';b.style.cursor='default';}});}
function aoVote(v){var k='ao_voted_'+location.pathname;if(localStorage.getItem(k)){aoThanks();aoRender();return;}try{localStorage.setItem(k,v);}catch(e){}if(v==='up')window._aoUp++;else window._aoDown++;var vb=document.getElementById(v==='up'?'aoUp':'aoDown');if(vb)vb.classList.add('voted');try{fetch(window.AO_VOTE_ENDPOINT,{method:'POST',headers:{'Content-Type':'text/plain;charset=utf-8'},body:JSON.stringify({vote:v,url:location.href,title:document.title,ref:document.referrer})}).catch(function(){});}catch(e){}aoThanks();aoRender();}
</script>
