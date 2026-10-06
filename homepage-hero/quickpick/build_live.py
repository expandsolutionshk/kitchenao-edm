import re, json, shutil
c=open('option-b.html',encoding='utf-8').read()
c=re.sub(r'<!--.*?-->','',c,flags=re.S)
sec=re.search(r'<section class="ao-qp.*?</section>',c,re.S).group(0)
css=re.search(r'<style>(.*?)</style>',c,re.S).group(1)
scripts=re.findall(r'<script>(.*?)</script>',c,re.S)
# move inline header background into CSS
m=re.search(r' style="(background-image:[^"]*)"',sec)
hdr_css=''
if m:
    hdr_css='.ao-qp-head--photo{'+m.group(1).replace('&quot;','"')+'}'
    sec=sec.replace(m.group(0),'')
sec=re.sub(r'>\s+<','><',' '.join(l.strip() for l in sec.split('\n') if l.strip()))
css=' '.join(l.strip() for l in css.split('\n') if l.strip())+hdr_css
js='\n'.join(scripts).replace('document.currentScript&&document.currentScript.previousElementSibling','__sec')
out=f'''/*! Kitchen AO｜/product-category/party/ 快速選擇派對套餐（Option B）｜由 WordPress 分類描述載入 */
(function(){{
  var me=document.currentScript;
  if(document.getElementById('ao-qp-css'))return;
  var td=document.querySelector('.term-description');
  [].forEach.call(document.querySelectorAll('.term-description .ao-qp'),function(x){{x.parentNode.removeChild(x);}});
  var st=document.createElement('style');st.id='ao-qp-css';st.textContent={json.dumps(css,ensure_ascii=False)};document.head.appendChild(st);
  var box=document.createElement('div');box.innerHTML={json.dumps(sec,ensure_ascii=False)};
  var __sec=box.firstElementChild;
  if(me&&td&&td.contains(me)){{me.parentNode.insertBefore(__sec,me);}}else if(td){{td.insertBefore(__sec,td.firstChild);}}else{{var hd=document.querySelector('.woocommerce-products-header');if(hd){{hd.appendChild(__sec);}}else{{return;}}}}
  (function(){{
{js}
  }})();
}})();
'''
open('party-quickpick.js','w',encoding='utf-8').write(out)
P='/sessions/great-festive-darwin/mnt/Desktop/cowork - aoao/pages/'
shutil.copy('party-quickpick.js',P+'party-quickpick.js')
print(len(out))
