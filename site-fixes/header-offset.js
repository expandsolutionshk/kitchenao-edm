/* Kitchen AO v4: body top padding = real header height (incl. category menu and logo); mobile WhatsApp icon in gold bar */
(function(){
  function run(){
    var h=document.getElementById('header'),b=document.body;
    if(!h||!b||b.classList.contains('lafka_transparent_header')||b.classList.contains('lafka_boxed'))return;
    var top=document.getElementById('header_top');
    if(top&&!top.querySelector('.ao-hd-wa')){
      var a=document.createElement('a');
      a.className='ao-hd-wa';a.href='https://wa.me/85269011987';a.target='_blank';a.rel='noopener';a.setAttribute('aria-label','WhatsApp');
      a.innerHTML='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M17.47 14.38c-.3-.15-1.75-.86-2.02-.96-.27-.1-.47-.15-.67.15-.2.3-.77.96-.94 1.16-.17.2-.35.22-.64.07-.3-.15-1.25-.46-2.38-1.47-.88-.79-1.47-1.76-1.65-2.06-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.03-.52-.07-.15-.67-1.6-.92-2.2-.24-.58-.49-.5-.67-.5h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48 0 1.46 1.07 2.88 1.21 3.08.15.2 2.1 3.2 5.08 4.49.71.31 1.26.49 1.7.63.71.23 1.36.2 1.87.12.57-.08 1.75-.72 2-1.41.25-.69.25-1.29.17-1.41-.07-.12-.27-.2-.57-.35zM12.05 21.8h-.01a9.8 9.8 0 0 1-5-1.37l-.36-.21-3.72.98 1-3.63-.24-.37a9.79 9.79 0 0 1-1.5-5.22c0-5.4 4.4-9.8 9.83-9.8 2.62 0 5.09 1.03 6.94 2.88a9.75 9.75 0 0 1 2.87 6.93c0 5.41-4.4 9.81-9.81 9.81zm8.36-18.17A11.75 11.75 0 0 0 12.05.17C5.5.17.17 5.5.17 12.05c0 2.09.55 4.13 1.59 5.93L.07 24l6.17-1.62a11.83 11.83 0 0 0 5.8 1.48h.01c6.55 0 11.88-5.33 11.88-11.88 0-3.17-1.24-6.16-3.48-8.4z"/></svg>';
      top.appendChild(a);
    }
    /* language switcher: move into gold bar, show 中文 instead of ZH */
    function lang(){
      var sw=document.querySelector('.trp-language-switcher.trp-floating-switcher');
      if(sw&&top&&sw.parentNode!==top){top.appendChild(sw);}
      if(sw){sw.classList.add('ao-in-bar');var ns=sw.querySelectorAll('.trp-language-item-name');for(var j=0;j<ns.length;j++){if(/^\s*ZH\s*$/i.test(ns[j].textContent))ns[j].textContent='中文';}}
    }
    lang();window.addEventListener('load',lang);setTimeout(lang,800);setTimeout(lang,2000);
    function hh(){
      var r=h.getBoundingClientRect(),t=r.top,bot=r.bottom;
      var els=h.querySelectorAll('.main_menu_holder,#main-menu,#header_top,#logo');
      for(var i=0;i<els.length;i++){var e=els[i].getBoundingClientRect();if(e.height>0&&e.bottom>bot)bot=e.bottom;}
      return Math.ceil(bot-t);
    }
    function fit(){ if(window.scrollY>5)return; b.style.setProperty('padding-top',hh()+'px','important'); }
    fit();
    window.addEventListener('load',fit);
    window.addEventListener('resize',fit);
    if('ResizeObserver' in window){ new ResizeObserver(fit).observe(h); }
  }
  if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',run);}else{run();}
})();
