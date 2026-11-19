/* Kitchen AO 萬聖節套餐已結束公告（2026-11-19）
   - 只喺萬聖節分類頁及 6 個萬聖節套餐產品頁顯示（product_cat-halloween-set）
   - 中英文自動切換；WPCode 用 JavaScript Snippet，位置選 Site Wide Footer */
(function(){
  try{
    var body = document.body;
    var isCat = body.classList.contains('term-halloween-set');
    var prod = document.querySelector('.single-product div.product.product_cat-halloween-set');
    if (!isCat && !prod) return;
    if (document.getElementById('ao-hw-end')) return;
    var en = /^en/i.test(document.documentElement.lang || '') || /^\/en(\/|$)/.test(location.pathname);
    var P = en ? '/en' : '';
    var T = en ? {
      k: 'HALLOWEEN 2026',
      h: 'Our Halloween sets have ended for 2026',
      p: 'Thank you for celebrating with us. The menus below are for reference only, and we look forward to seeing you again next Halloween. Planning another gathering? Take a look at:',
      l: [['Christmas Catering 2026', '12 to 27 Dec', P + '/catering/christmas/', 1],
          ['Party Catering Sets', 'Gourmet, kids, vegetarian and more', P + '/product-category/party/'],
          ['Sets by Group Size', '2 to 100+ guests', P + '/product-category/party-set-by-people/'],
          ['Corporate Catering', 'Office lunch and company events', P + '/corporate-catering-hk/'],
          ['Get a Quote', 'Tailor-made menu for your event', P + '/catering-quote-enquiry/']]
    } : {
      k: 'HALLOWEEN 2026',
      h: '2026 萬聖節狂嘩套餐已完滿結束',
      p: '多謝大家支持！以下餐單只供參考，明年萬聖節再見。如正籌備其他聚會，歡迎查看：',
      l: [['聖誕到會套餐 2026', '12 月 12 日至 27 日供應', '/catering/christmas/', 1],
          ['派對到會套餐', '美食派對、兒童、素食及更多', '/product-category/party/'],
          ['按人數揀套餐', '2 至 100 人以上', '/product-category/party-set-by-people/'],
          ['公司到會', '員工午餐及公司活動', '/corporate-catering-hk/'],
          ['專人活動報價', '按活動需要度身配搭', '/catering-quote-enquiry/']]
    };
    var css = ''
      + '#ao-hw-end{box-sizing:border-box;width:100%;margin:0 0 28px;padding:22px 24px;background:#fbf8f3;border:1px solid #C8A24A;box-shadow:inset 0 0 0 4px #fbf8f3,inset 0 0 0 5px rgba(200,162,74,.35);font-family:inherit;color:#1d1714;clear:both}'
      + '#ao-hw-end *{box-sizing:border-box}'
      + '#ao-hw-end .k{display:block;font-size:11px;letter-spacing:.3em;color:#9A7B2E;margin:0 0 6px}'
      + '#ao-hw-end .h{margin:0 0 6px;font-family:"Songti TC","Noto Serif TC",Baskerville,Georgia,serif;font-size:21px;font-weight:600;letter-spacing:.04em;line-height:1.35;color:#1d1714}'
      + '#ao-hw-end .p{margin:0 0 16px;font-size:14px;line-height:1.8;color:#5d534d}'
      + '#ao-hw-end .g{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:10px}'
      + '#ao-hw-end a{display:flex;flex-direction:column;justify-content:center;min-height:68px;padding:10px 12px;background:#fff;border:1px solid #E6DDCB;text-decoration:none!important;color:#1d1714!important;transition:border-color .25s,background .25s,color .25s}'
      + '#ao-hw-end a b{font-size:14px;font-weight:600;letter-spacing:.06em;line-height:1.35}'
      + '#ao-hw-end a small{margin-top:3px;font-size:11.5px;color:#8A8378;letter-spacing:.03em;line-height:1.4}'
      + '#ao-hw-end a:hover{border-color:#1d1714}'
      + '#ao-hw-end a.x{background:#1d1714;border-color:#1d1714;color:#F3E3B8!important}#ao-hw-end a.x small{color:#C8A24A}#ao-hw-end a.x:hover{background:#000}'
      + '@media(max-width:1024px){#ao-hw-end .g{grid-template-columns:repeat(3,minmax(0,1fr))}}'
      + '@media(max-width:640px){#ao-hw-end{padding:18px 16px;margin:0 0 20px}#ao-hw-end .h{font-size:18px}#ao-hw-end .p{font-size:13.5px}#ao-hw-end .g{grid-template-columns:1fr 1fr;gap:8px}#ao-hw-end a{min-height:62px;padding:9px 10px}#ao-hw-end a b{font-size:13px;letter-spacing:.03em}#ao-hw-end a small{font-size:11px}#ao-hw-end a.x{grid-column:1/-1}}';
    var st = document.createElement('style'); st.id = 'ao-hw-end-css'; st.textContent = css; document.head.appendChild(st);
    var box = document.createElement('div'); box.id = 'ao-hw-end'; box.setAttribute('data-no-translation', '');
    var links = T.l.map(function(x){ return '<a' + (x[3] ? ' class="x"' : '') + ' href="' + x[2] + '" data-lb="' + x[2] + '"><b>' + x[0] + '</b><small>' + x[1] + '</small></a>'; }).join('');
    box.innerHTML = '<span class="k">' + T.k + '</span><p class="h">' + T.h + '</p><p class="p">' + T.p + '</p><div class="g">' + links + '</div>';
    [].forEach.call(box.querySelectorAll('a'), function(a){ a.addEventListener('click', function(){ try{ window.dataLayer = window.dataLayer || []; window.dataLayer.push({event:'cta_click', cta_label:'halloween_ended', link_url:a.getAttribute('data-lb')}); }catch(e){} }); });
    if (prod) { prod.parentNode.insertBefore(box, prod); }
    else {
      var holder = document.querySelector('#products-wrapper .content_holder') || document.querySelector('.content_holder');
      var list = document.querySelector('.box-product-list, ul.products');
      if (holder) holder.insertBefore(box, holder.firstChild);
      else if (list) list.parentNode.insertBefore(box, list);
      else (document.querySelector('#main') || body).prepend(box);
    }
  }catch(err){}
})();
