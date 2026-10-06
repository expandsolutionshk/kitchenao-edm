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
  /* SEO 引導文字：分類「內容說明」嘅文字放喺快選區塊下面、price range／產品上面，做成細引導條 */
  (function(){{
    var tdesc=document.querySelector('.term-description');if(!tdesc)return;
    var nodes=[].filter.call(tdesc.childNodes,function(n){{return !(n.nodeType===1&&n.classList&&n.classList.contains('ao-qp'))&&(n.textContent||'').replace(/\s+/g,'')!=='';}});
    if(!nodes.length)return;
    var box=document.createElement('div');box.className='ao-cat-seo';
    nodes.forEach(function(n){{box.appendChild(n);}});
    var qp=tdesc.querySelector('.ao-qp');
    if(qp&&qp.nextSibling){{tdesc.insertBefore(box,qp.nextSibling);}}else{{tdesc.appendChild(box);}}
    var cs=document.createElement('style');cs.textContent='.ao-cat-seo{{max-width:1180px;margin:-12px auto 26px;padding:14px 20px 14px 66px;position:relative;border:0;border-radius:14px;background:linear-gradient(135deg,#f0d39a 0%,#d2a44e 100%);color:#241a12;font-size:14px;font-weight:600;line-height:1.75;text-align:left;box-shadow:0 8px 20px rgba(120,85,30,.18);}} .ao-cat-seo::before{{content:"↓";position:absolute;left:16px;top:50%;width:36px;height:36px;margin-top:-18px;border-radius:10px;background:rgba(255,255,255,.45);color:#7d5b27;font-size:18px;font-weight:900;line-height:36px;text-align:center;animation:aoSeoBob 1.6s ease-in-out infinite;}} .ao-cat-seo p{{margin:0 !important;color:#241a12 !important;}} .ao-cat-seo strong,.ao-cat-seo b{{color:#241a12;font-weight:900;}} @keyframes aoSeoBob{{0%,100%{{transform:translateY(0);}}50%{{transform:translateY(3px);}}}} @media (max-width:640px){{.ao-cat-seo{{margin:-8px 0 20px;padding:12px 14px 12px 58px;font-size:13px;}} .ao-cat-seo::before{{left:12px;width:32px;height:32px;margin-top:-16px;line-height:32px;font-size:16px;}}}} @media (prefers-reduced-motion:reduce){{.ao-cat-seo::before{{animation:none;}}}}';document.head.appendChild(cs);
  }})();
}})();
'''
open('party-quickpick.js','w',encoding='utf-8').write(out)
P='/sessions/great-festive-darwin/mnt/Desktop/cowork - aoao/pages/'
shutil.copy('party-quickpick.js',P+'party-quickpick.js')
print(len(out))
