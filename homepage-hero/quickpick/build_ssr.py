# -*- coding: utf-8 -*-
"""派對分類頁快選區塊｜WAF 安全版（不在 WP 提交 <script>／<style>／onclick）
輸出：
  party-category-description-v2.html ：貼入分類描述（只有 HTML）
  party-quickpick.css                 ：加入「附加 CSS」
  party-quickpick.js                  ：GitHub Pages 檔（已由 WP 載入）；如頁面已有 .ao-qp 就只加功能，不再插入
"""
import re, json
exec(open('build_server.py', encoding='utf-8').read().split('php = """')[0])
sec2 = re.sub(r'''onclick="window\.dataLayer=window\.dataLayer\|\|\[\];dataLayer\.push\(\{event:'cta_click',cta_label:'([^']+)'\}\);"''', r'data-ga="\1"', sec)
assert 'onclick' not in sec2, re.findall(r'onclick="[^"]*"', sec2)[:2]
DESC = '<p>Kitchen AO <strong>香港派對到會套餐</strong>，適合生日派對、朋友聚會、公司活動及船河派對，2 人至 100 人以上均可選擇，全港送遞。想慢慢比較？可用下方<strong>價錢範圍</strong>及<strong>分類</strong>，瀏覽全部派對到會套餐。</p>'
html = sec2 + '<div class="ao-cat-seo">' + DESC + '</div>'
assert '<script' not in html and '<style' not in html
open('party-category-description-v2.html', 'w', encoding='utf-8').write(html)
open('party-quickpick.css', 'w', encoding='utf-8').write('/* Kitchen AO - party category quick-pick (server-rendered) */\n' + css + '\n' + seo_css + '\n')
old = open('party-quickpick_backup_v1.js', encoding='utf-8').read()
# 舊版插入邏輯（fallback）：取原檔第 2 個 IIFE 之前的部分
m = re.search(r"var st=document\.createElement\('style'\);st\.id='ao-qp-css';st\.textContent=(\".*?\");document\.head\.appendChild\(st\);", old, re.S)
css_json = m.group(1)
seo_js = re.search(r"/\* SEO 引導文字.*?\n  \}\)\(\);", old, re.S).group(0)
out = """/*! Kitchen AO｜/product-category/party/ 快速選擇派對套餐｜v2：支援伺服器輸出（分類描述已有 .ao-qp 時只加功能） */
(function(){
  if(window.__aoQP)return;window.__aoQP=1;
  var me=document.currentScript;
  var td=document.querySelector('.term-description');
  var __sec=document.querySelector('.ao-qp');
  if(!__sec){
    /* 後備：分類描述未有區塊時，沿用舊方法插入 */
    if(!document.getElementById('ao-qp-css')){var st=document.createElement('style');st.id='ao-qp-css';st.textContent=__CSS__;document.head.appendChild(st);}
    var box=document.createElement('div');box.innerHTML=__SEC__;
    __sec=box.firstElementChild;
    if(me&&td&&td.contains(me)){me.parentNode.insertBefore(__sec,me);}else if(td){td.insertBefore(__sec,td.firstChild);}else{var hd=document.querySelector('.woocommerce-products-header');if(hd){hd.appendChild(__sec);}else{return;}}
  __SEO__
  }
  /* GA：data-ga 點擊追蹤 */
  [].forEach.call(__sec.querySelectorAll('[data-ga]'),function(a){a.addEventListener('click',function(){window.dataLayer=window.dataLayer||[];window.dataLayer.push({event:'cta_click',cta_label:a.getAttribute('data-ga')});});});
  (function(){
__JS__
  })();
})();
"""
out = out.replace('__CSS__', css_json).replace('__SEC__', json.dumps(sec2, ensure_ascii=False)).replace('__SEO__', seo_js).replace('__JS__', js)
open('party-quickpick.js', 'w', encoding='utf-8').write(out)
print('desc', len(html), 'css', len(css) + len(seo_css), 'js', len(out), 'data-ga', html.count('data-ga='))
