/* Kitchen AO: auto switch to English (/en/) for visitors whose browser language is English.
   - Only on first visit; remembers the choice for 30 days (cookie ao_lang).
   - If the visitor clicks the language switcher, their choice is kept (no loop).
   - Skips search engine bots, logged-in admin, checkout/cart/my-account and wp-admin.
   Install: WPCode > Add Snippet > JavaScript Snippet > Location: Site Wide Header > Active */
(function(){
  try{
    var ua=navigator.userAgent||'';
    if(/bot|crawl|spider|slurp|lighthouse|google|bing|baidu|yandex|facebookexternalhit|preview/i.test(ua)||navigator.webdriver)return;
    if(document.documentElement.className.indexOf('wp-toolbar')>-1||/(^|\s)logged-in(\s|$)/.test(document.body?document.body.className:''))return;
    var p=location.pathname;
    if(/^\/(wp-admin|wp-login|checkout|cart|my-account|cart-3|my-account-2)/.test(p))return;
    function getC(n){var m=document.cookie.match('(?:^|; )'+n+'=([^;]*)');return m?m[1]:''}
    function setC(n,v){document.cookie=n+'='+v+';path=/;max-age='+(60*60*24*30)+';SameSite=Lax'}
    var isEn=/^\/en(\/|$)/.test(p);
    // remember manual choice: any click on the language switcher
    document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('.trp-language-switcher a, a[href*="/en/"], .trp-ls-language-name');if(!a)return;var h=a.getAttribute('href')||'';setC('ao_lang',/\/en(\/|$)/.test(h)?'en':'zh')},true);
    var saved=getC('ao_lang');
    if(saved){return;}                       // already decided (auto or manual)
    var langs=(navigator.languages&&navigator.languages.length?navigator.languages:[navigator.language||'']).join(',').toLowerCase();
    var prefersEn=/^en/.test(langs) && !/zh|yue/.test(langs.split(',')[0]);
    setC('ao_lang',prefersEn?'en':'zh');
    if(prefersEn&&!isEn){location.replace('/en'+(p==='/'?'/':p)+location.search+location.hash);}
  }catch(err){}
})();
