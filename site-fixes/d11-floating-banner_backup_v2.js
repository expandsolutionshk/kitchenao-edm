/* Kitchen AO 2026 Double 11 floating icon + promotion banner (zh / en auto)
   Install: WPCode > Add Snippet > JavaScript Snippet > Auto Insert > Site Wide Footer > Active
   - Floating "11.11" icon bottom-left (WhatsApp button stays bottom-right)
   - Banner opens only when the icon is clicked (no auto popup)
   - Hidden on cart / checkout / my-account; removes itself after 17 Nov 2026 23:59 HKT */
(function(){
  try{
    var END = Date.parse('2026-11-17T23:59:59+08:00');
    if (Date.now() > END) return;
    var p = location.pathname;
    if (/\/(cart|cart-3|checkout|my-account|my-account-2|wp-admin|wp-login)/.test(decodeURIComponent(p))) return;
    if (document.getElementById('ao-d11-fab')) return;
    var en = /^en/i.test(document.documentElement.lang || '') || /^\/en(\/|$)/.test(p);
    var T = en ? {
      fab: 'OFFER', title: '11.11 Four Rewards · 7 Days', lead: 'Spend HK$1,100, get 11% off sitewide',
      sub: 'Spend HK$1,500 or more for free snacks, up to 3 items.', code: 'PROMOTION CODE', copy: 'Copy', copied: 'Copied',
      date: 'Valid 11 to 17 November 2026', cta: 'Order Now', more: 'See all four rewards', close: 'Close',
      kv: 'https://aoaodelivery.com/wp-content/uploads/2026/11/d11-kv-en-768x787.jpg', home: '/en/#double11', menu: '/en/product-category/party/'
    } : {
      fab: '優惠', title: '一連七天　雙 11 四重賞', lead: '滿 HK$1,100 全網 11% OFF',
      sub: '滿 HK$1,500 起再送人氣小食，最多送 3 款。', code: 'PROMOTION CODE', copy: '複製', copied: '已複製',
      date: '優惠期　2026.11.11 至 11.17', cta: '立即預訂索取四重賞', more: '查看四重賞詳情', close: '關閉',
      kv: 'https://aoaodelivery.com/wp-content/uploads/2026/11/d11-kv-768x787.jpg', home: '/#double11', menu: '/product-category/party/'
    };
    function track(a){ try{ window.dataLayer = window.dataLayer || []; window.dataLayer.push({event:'d11_banner_' + a, promo_id:'double11_2026'}); }catch(e){} }

    var css = ''
    + '#ao-d11-fab{position:fixed;left:18px;bottom:22px;z-index:99990;width:68px;height:68px;border-radius:50%;border:0;padding:0;cursor:pointer;background:#1A1A1A;box-shadow:0 8px 22px rgba(0,0,0,.28);display:flex;flex-direction:column;align-items:center;justify-content:center;font-family:inherit;outline:2px solid #C8A24A;outline-offset:-6px;animation:aoD11In .5s ease both}'
    + '#ao-d11-fab b{font-family:"Arial Black",Arial,Helvetica,sans-serif;font-style:italic;font-size:17px;line-height:1;color:#E4C77E;letter-spacing:-.5px}'
    + '#ao-d11-fab small{font-size:11px;font-weight:800;color:#fff;margin-top:3px;letter-spacing:.08em}'
    + '#ao-d11-fab i{position:absolute;top:-14px;right:-22px;white-space:nowrap;background:#B03426;color:#fff;font-style:normal;font-size:10.5px;font-weight:800;border-radius:20px;padding:3px 6px;box-shadow:0 2px 6px rgba(0,0,0,.25)}'
    + '#ao-d11-fab:before{content:"";position:absolute;inset:-6px;border-radius:50%;border:2px solid rgba(200,162,74,.6);animation:aoD11Ring 2.2s ease-out infinite}'
    + '@keyframes aoD11Ring{0%{transform:scale(.9);opacity:1}100%{transform:scale(1.35);opacity:0}}'
    + '@keyframes aoD11In{from{transform:translateY(30px);opacity:0}to{transform:none;opacity:1}}'
    + '#ao-d11-ov{position:fixed;inset:0;z-index:99995;background:rgba(20,16,12,.62);display:none;align-items:center;justify-content:center;padding:16px}'
    + '#ao-d11-ov.on{display:flex}'
    + '#ao-d11-box{position:relative;width:100%;max-width:420px;max-height:calc(100vh - 32px);overflow-y:auto;background:#F3E7D2;border-radius:16px;box-shadow:0 20px 60px rgba(0,0,0,.4);font-family:inherit;color:#2B2622;animation:aoD11Pop .3s ease both}'
    + '@keyframes aoD11Pop{from{transform:scale(.94);opacity:0}to{transform:none;opacity:1}}'
    + '#ao-d11-box img{display:block;width:100%;height:auto;border-radius:16px 16px 0 0}'
    + '#ao-d11-x{position:absolute;top:10px;left:10px;width:34px;height:34px;border:0;border-radius:50%;background:rgba(0,0,0,.6);color:#fff;font-size:20px;line-height:1;cursor:pointer;z-index:2}'
    + '#ao-d11-box .bd{padding:16px 18px 20px;text-align:center}'
    + '#ao-d11-box .cd{background:#fff;border:1px solid #C8A24A;padding:5px;margin:0 0 14px}'
    + '#ao-d11-box .cd>div{border:1px solid #E6D3A6;padding:14px 10px}'
    + '#ao-d11-box .cd small{display:block;padding-left:.3em;font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;font-size:10.5px;letter-spacing:.3em;color:#9A7B2E}'
    + '#ao-d11-box .cd .r{display:flex;align-items:center;justify-content:center;gap:12px;margin:8px 0 0}'
    + '#ao-d11-box .cd strong{padding-left:.2em;font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;font-weight:300;font-size:26px;letter-spacing:.2em;color:#1A1A1A;user-select:all}'
    + '#ao-d11-box .cp{border:0;cursor:pointer;background:#1A1A1A;color:#E4C77E;border-radius:6px;padding:8px 14px;font:inherit;font-size:13px;font-weight:800}'
    + '#ao-d11-box .cp.ok{background:#C8A24A;color:#1A1A1A}'
    + '#ao-d11-box .dt{display:block;margin:10px 0 0;font-size:13px;color:#5d534d;letter-spacing:.05em}'
    + '#ao-d11-box a.b{display:flex;align-items:center;justify-content:center;min-height:48px;border-radius:40px;font-size:15px;font-weight:800;text-decoration:none!important;letter-spacing:.05em;margin:0 0 10px}'
    + '#ao-d11-box a.dk{background:#1A1A1A;color:#E4C77E!important}'
    + '#ao-d11-box a.ol{background:#fff;border:1.5px solid #1A1A1A;color:#1A1A1A!important;margin:0}'
    + '@media(max-width:640px){#ao-d11-fab{left:12px;bottom:14px;width:60px;height:60px}#ao-d11-fab b{font-size:15px}}'
    + '@media(prefers-reduced-motion:reduce){#ao-d11-fab,#ao-d11-fab:before,#ao-d11-box{animation:none}}';
    var st = document.createElement('style'); st.id = 'ao-d11-css'; st.textContent = css; document.head.appendChild(st);

    var fab = document.createElement('button');
    fab.id = 'ao-d11-fab'; fab.type = 'button'; fab.setAttribute('aria-label', T.title);
    fab.setAttribute('data-no-translation', '');
    fab.innerHTML = '<i>11% OFF</i><b>11.11</b><small>' + T.fab + '</small>';

    var ov = document.createElement('div');
    ov.id = 'ao-d11-ov'; ov.setAttribute('role', 'dialog'); ov.setAttribute('aria-modal', 'true'); ov.setAttribute('aria-label', T.title);
    ov.setAttribute('data-no-translation', '');
    ov.innerHTML = '<div id="ao-d11-box"><button type="button" id="ao-d11-x" aria-label="' + T.close + '">×</button>'
      + '<a href="' + T.menu + '"><img src="' + T.kv + '" alt="' + T.title + '：' + T.lead + '" width="768" height="787" loading="lazy"></a>'
      + '<div class="bd"><div class="cd"><div><small>' + T.code + '</small><div class="r"><strong>DOUBLE11</strong><button type="button" class="cp">' + T.copy + '</button></div>'
      + '<span class="dt">' + T.date + '</span></div></div>'
      + '<a class="b dk" href="' + T.menu + '">' + T.cta + '</a><a class="b ol" href="' + T.home + '">' + T.more + '</a></div></div>';

    function open(src){ ov.classList.add('on'); track('open_' + src); }
    function close(){ ov.classList.remove('on'); track('close'); }
    fab.addEventListener('click', function(){ open('icon'); });
    ov.addEventListener('click', function(e){ if (e.target === ov) close(); });
    document.addEventListener('keydown', function(e){ if (e.key === 'Escape' && ov.classList.contains('on')) close(); });

    function mount(){
      document.body.appendChild(fab); document.body.appendChild(ov);
      document.getElementById('ao-d11-x').addEventListener('click', close);
      [].forEach.call(ov.querySelectorAll('a'), function(a){ a.addEventListener('click', function(){ track('click_' + (a.className.indexOf('dk') > -1 ? 'order' : a.className.indexOf('ol') > -1 ? 'rewards' : 'kv')); }); });
      var cp = ov.querySelector('.cp');
      cp.addEventListener('click', function(){
        function done(){ cp.classList.add('ok'); cp.textContent = T.copied; track('copy_code'); setTimeout(function(){ cp.classList.remove('ok'); cp.textContent = T.copy; }, 2000); }
        if (navigator.clipboard && window.isSecureContext) { navigator.clipboard.writeText('DOUBLE11').then(done); }
        else { var t = document.createElement('textarea'); t.value = 'DOUBLE11'; t.style.position = 'fixed'; t.style.opacity = '0'; document.body.appendChild(t); t.select(); try{ document.execCommand('copy'); done(); }catch(e){} document.body.removeChild(t); }
      });
    }
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', mount); else mount();
  }catch(err){}
})();
