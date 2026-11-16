/* Kitchen AO：場景頁及產品頁預載（WPCode → JavaScript Snippet → 全站頁尾 Site Wide Footer）
   滑鼠停留連結約 0.2 秒或手機按下時，瀏覽器在背後預先載入下一頁，撳落去差不多即時顯示。
   只支援 Chrome / Edge / Android Chrome；Safari、Firefox 會自動略過，不影響正常瀏覽。 */
(function () {
  if (!(window.HTMLScriptElement && HTMLScriptElement.supports && HTMLScriptElement.supports('speculationrules'))) return;
  var no = [
    { href_matches: '/wp-admin/*' }, { href_matches: '/*/wp-admin/*' }, { href_matches: '/wp-login.php*' },
    { href_matches: '/cart/*' }, { href_matches: '/checkout/*' }, { href_matches: '/my-account/*' },
    { href_matches: '/*/cart/*' }, { href_matches: '/*/checkout/*' }, { href_matches: '/*/my-account/*' },
    { href_matches: '/*?*add-to-cart=*' }, { href_matches: '/*?*remove_item=*' }, { href_matches: '/*?*logout*' },
    { selector_matches: '[rel~="nofollow"]' }, { selector_matches: '.no-prerender, .no-prerender a' }
  ];
  var rules = {
    // 到會場景頁（中英）：完整預先渲染
    prerender: [{ source: 'document', eagerness: 'moderate',
      where: { and: [{ or: [{ href_matches: '/catering/*' }, { href_matches: '/en/catering/*' }] }, { not: { or: no } }] } }],
    // 產品及分類頁：只預先下載 HTML（較輕）
    prefetch: [{ source: 'document', eagerness: 'moderate',
      where: { and: [{ or: [{ href_matches: '/product/*' }, { href_matches: '/en/product/*' }, { href_matches: '/product-category/*' }, { href_matches: '/en/product-category/*' }] }, { not: { or: no } }] } }]
  };
  var s = document.createElement('script');
  s.type = 'speculationrules';
  s.textContent = JSON.stringify(rules);
  document.head.appendChild(s);
})();
