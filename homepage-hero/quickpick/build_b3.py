import html, shutil, re
a=open('option-a.html',encoding='utf-8').read()
U='https://aoaodelivery.com/wp-content/uploads/'
FEAST=U+'2025/04/WhatsApp-Image-2025-04-14-at-6.13.46-PM-600x600.jpeg'
b=a.replace('Option A 黑金（Raw HTML）','Option B 黑金・餐廳質感版（Raw HTML）')
# header: food photo band + ornament
old_head='''  <div class="ao-qp-head">
    <p class="ao-qp-eyebrow">Kitchen AO Party Catering</p>
    <h2 id="ao-qp-title" class="ao-qp-title">快速選擇派對套餐</h2>
    <p class="ao-qp-sub">先按人數或系列選擇合適套餐，再直接網上下單。</p>
  </div>'''
assert old_head in b
b=b.replace(old_head,f'''  <div class="ao-qp-head ao-qp-head--photo" style="background-image:linear-gradient(180deg,rgba(18,13,10,.35) 0%,rgba(18,13,10,.78) 70%,#1d150f 100%),url('{FEAST}');">
    <p class="ao-qp-eyebrow">Kitchen AO Party Catering</p>
    <h2 id="ao-qp-title" class="ao-qp-title">快速選擇派對套餐</h2>
    <span class="ao-qp-orn" aria-hidden="true"><i></i>◆<i></i></span>
    <p class="ao-qp-sub">先按人數或系列選擇合適套餐，再直接網上下單。</p>
  </div>''')
# english kickers on tags
b=b.replace('<i>1</i>👥 按人數選擇</span>','<i>1</i>👥 按人數選擇<small>BY GUESTS</small></span>')
b=b.replace('<i>2</i>🍽️ 按系列選擇</span>','<i>2</i>🍽️ 按系列選擇<small>OUR MENU</small></span>')
b=b.replace('<i>3</i>🔥 本週 <b>TOP 5</b> 人氣推介</span>','<i>3</i>🔥 本週 <b>TOP 5</b> 人氣推介<small>CHEF\'S PICKS</small></span>')

# ===== 商務到會 TIPS 區（按人數選擇 與 按系列選擇 之間）=====
LOGO='https://aoaodelivery.com/wp-content/uploads/2023/08/kitchenAO_logo-1.png'
ITEMS=[('🍱','商務飯盒'),('🤝','Team Building'),('🥂','酒會 Finger Food 及 Canapé'),('🎀','簡易開張套餐'),('🎪','Event 活動'),('🏆','Annual Dinner'),('🍸','Cocktail 服務（Free Flow、Cocktail Bar）'),('🤵','服務生安排'),('📝','訂製食譜 Customised Recipe')]
rows=''.join(f'<li><span class="ao-biz-tick">✓</span><span class="ao-biz-ic">{e}</span><span>{t}</span></li>' for e,t in ITEMS)
BIZ=f"""<div class="ao-biz" data-biz>
    <div class="ao-biz-wrap">
      <button type="button" class="ao-biz-btn" aria-expanded="false" aria-controls="ao-biz-panel"><span class="ao-biz-bi">💼</span><span class="ao-biz-tx">商務到會 TIPS</span><span class="ao-biz-car">▾</span></button>
      <div class="ao-biz-panel" id="ao-biz-panel" role="region" aria-label="商務到會服務">
        <button type="button" class="ao-biz-x" aria-label="關閉">×</button>
        <div class="ao-biz-ph"><span>FOR BUSINESS</span><b>企業及商務到會服務</b></div>
        <ul class="ao-biz-list">{rows}</ul>
        <a class="ao-biz-wa" href="https://api.whatsapp.com/send?phone=85269011987&text=%E4%BC%81%E6%A5%AD%E5%8F%8A%E5%95%86%E5%8B%99%E5%88%B0%E6%9C%83%E6%9C%8D%E5%8B%99%E6%9F%A5%E8%A9%A2" target="_blank" rel="noopener" onclick="window.dataLayer=window.dataLayer||[];dataLayer.push({{event:'cta_click',cta_label:'qp_biz_whatsapp'}});">WhatsApp 聯絡企業客戶專員</a>
        <a class="ao-biz-more" href="https://aoaodelivery.com/business-event/" target="_blank" rel="noopener" onclick="window.dataLayer=window.dataLayer||[];dataLayer.push({{event:'cta_click',cta_label:'qp_biz_intro'}});">商務活動簡介</a>
      </div>
    </div>
    <div class="ao-biz-cursor" aria-hidden="true"><span class="ao-biz-logo"><img src="{LOGO}" alt="" width="194" height="121"></span><span>We Serve, We WOW</span></div>
  </div>
  """
b=b.replace('<div class="ao-qp-sec ao-qp-box ao-qp-box--ser">',BIZ+'<div class="ao-qp-sec ao-qp-box ao-qp-box--ser">',1)
assert 'data-biz' in b
BIZJS="""<script>
(function(){
  /* 商務到會 TIPS：mouse over 展開、手機撳一下展開；自訂滑鼠游標 */
  var biz=document.querySelector('.ao-qp [data-biz]');if(!biz)return;
  var wrap=biz.querySelector('.ao-biz-wrap'),btn=biz.querySelector('.ao-biz-btn'),cur=biz.querySelector('.ao-biz-cursor');
  function set(o){biz.classList.toggle('is-open',o);btn.setAttribute('aria-expanded',o?'true':'false');}
  var fine=window.matchMedia&&window.matchMedia('(hover:hover) and (pointer:fine)').matches;
  if(fine){
    wrap.addEventListener('mouseenter',function(){set(true);});
    wrap.addEventListener('mouseleave',function(){set(false);});
    biz.addEventListener('mousemove',function(e){var r=biz.getBoundingClientRect();cur.style.transform='translate('+(e.clientX-r.left)+'px,'+(e.clientY-r.top)+'px)';biz.classList.add('has-cursor');});
    biz.addEventListener('mouseleave',function(){biz.classList.remove('has-cursor');});
  }
  biz.querySelector('.ao-biz-x').addEventListener('click',function(e){e.stopPropagation();set(false);btn.blur();});
  btn.addEventListener('click',function(){set(!biz.classList.contains('is-open'));if(biz.classList.contains('is-open')){window.dataLayer=window.dataLayer||[];window.dataLayer.push({event:'cta_click',cta_label:'qp_biz_open'});}});
  document.addEventListener('click',function(e){if(!biz.contains(e.target))set(false);});
  document.addEventListener('keydown',function(e){if(e.key==='Escape')set(false);});
  /* 捲過此區後：按鈕變成浮動 icon（只喺快選區域範圍內顯示） */
  var sec=document.querySelector('.ao-qp');
  if('IntersectionObserver' in window&&sec){
    var areaGone=false,secIn=false,helpIn=false;
    var upd=function(){var f=areaGone&&secIn&&!helpIn,was=biz.classList.contains('is-float');if(f!==was)set(false);biz.classList.toggle('is-float',f);};
    var help=sec.querySelector('.ao-qp-help');if(help)new IntersectionObserver(function(en){helpIn=en[0].isIntersecting;upd();}).observe(help);
    new IntersectionObserver(function(en){var e=en[0];areaGone=!e.isIntersecting&&e.boundingClientRect.top<0;upd();}).observe(biz);
    new IntersectionObserver(function(en){secIn=en[0].isIntersecting;upd();},{rootMargin:'0px 0px -120px 0px'}).observe(sec);
  }
})();
</script>"""
b=b.replace('</script>','</script>\n'+BIZJS,1)

extra='''

/* ===== 商務到會 TIPS ===== */
.ao-biz{position:relative;z-index:20;display:flex;align-items:center;justify-content:center;min-height:80px;margin:8px -36px 0;padding:15px 20px;background:linear-gradient(90deg,rgba(30,42,74,0) 0%,rgba(30,42,74,.55) 20%,rgba(30,42,74,.55) 80%,rgba(30,42,74,0) 100%);border-top:1px solid rgba(120,150,210,.25);border-bottom:1px solid rgba(120,150,210,.25);}
.ao-biz-wrap{position:relative;}
.ao-biz-btn{display:inline-flex;align-items:center;gap:10px;height:50px;padding:0 26px 0 10px;border:0;border-radius:999px;background:linear-gradient(135deg,#2c4a86 0%,#1e2a4a 100%);color:#fff;font:inherit;font-size:17px;font-weight:800;letter-spacing:2px;cursor:pointer;box-shadow:0 10px 24px rgba(10,20,50,.55),0 0 0 2px rgba(140,170,230,.35);animation:aoBizFloat 1.3s ease-in-out infinite;}
.ao-biz-bi{display:inline-flex;align-items:center;justify-content:center;width:34px;height:34px;border-radius:50%;background:#fff;font-size:17px;}
.ao-biz-car{font-size:12px;transition:transform .25s ease;opacity:.85;}
.ao-biz.is-open .ao-biz-car{transform:rotate(180deg);}
.ao-biz.is-open .ao-biz-btn{animation:none;}
@keyframes aoBizFloat{0%,100%{transform:translateY(0);}50%{transform:translateY(-6px);}}
.ao-biz-panel{position:absolute;left:50%;top:calc(100% + 12px);width:min(420px,88vw);padding:18px 18px 16px;border-radius:16px;background:#fff;color:#1e2a4a;box-shadow:0 24px 50px rgba(0,0,0,.45);transform:translate(-50%,-8px);opacity:0;visibility:hidden;transition:opacity .22s ease,transform .22s ease,visibility .22s;}
.ao-biz-panel::before{content:"";position:absolute;left:50%;top:-14px;width:100%;height:14px;transform:translateX(-50%);}
.ao-biz-panel::after{content:"";position:absolute;left:50%;top:-7px;width:14px;height:14px;background:#fff;transform:translateX(-50%) rotate(45deg);border-radius:2px;}
.ao-biz.is-open .ao-biz-panel{opacity:1;visibility:visible;transform:translate(-50%,0);}
.ao-biz-x{position:absolute;top:10px;right:10px;z-index:2;width:32px;height:32px;display:flex;align-items:center;justify-content:center;padding:0;border:0;border-radius:50%;background:#1e2a4a;color:#fff;font:inherit;font-size:20px;line-height:1;cursor:pointer;box-shadow:0 4px 10px rgba(0,0,0,.25);transition:background .2s ease,transform .2s ease;}
.ao-biz-x:hover{background:#b8893f;transform:rotate(90deg);}
.ao-biz-ph{margin:0 0 12px;padding-right:30px;padding-left:30px;padding:0 0 10px;border-bottom:2px solid #e3e9f5;text-align:center;}
.ao-biz-ph span{display:block;font-size:10.5px;font-weight:800;letter-spacing:3px;color:#5b77b3;}
.ao-biz-ph b{display:block;margin-top:2px;font-size:17px;font-weight:800;color:#1e2a4a;}
.ao-biz-list{list-style:none !important;margin:0 0 14px !important;padding:0 !important;border:1px solid #e3e9f5;border-radius:12px;overflow:hidden;}
.ao-biz-list li{display:flex;align-items:center;gap:10px;margin:0 !important;padding:9px 12px !important;font-size:14px;font-weight:700;line-height:1.4;list-style:none !important;}
.ao-biz-list li:nth-child(odd){background:#f5f8fd;}
.ao-biz-list li + li{border-top:1px solid #edf1f8;}
.ao-biz-tick{flex:0 0 22px;height:22px;display:inline-flex;align-items:center;justify-content:center;border-radius:50%;background:linear-gradient(135deg,#f0d39a 0%,#c99a45 100%);color:#241a12;font-size:12px;font-weight:900;box-shadow:0 2px 6px rgba(185,137,63,.45);}
.ao-biz-ic{flex:0 0 22px;text-align:center;font-size:16px;}
.ao-biz-wa{display:block;padding:13px 16px;border-radius:999px;background:linear-gradient(135deg,#e3c482,#b8893f);color:#1d150f !important;text-align:center;font-size:15px;font-weight:800;line-height:1.2;letter-spacing:1px;box-shadow:0 8px 18px rgba(185,137,63,.35);transition:filter .2s ease;}
.ao-biz-wa:hover{filter:brightness(1.08);}
.ao-biz-more{display:block;margin-top:8px;padding:11px 16px;border-radius:999px;border:1.5px solid #1e2a4a;background:#fff;color:#1e2a4a !important;text-align:center;font-size:14.5px;font-weight:800;line-height:1.2;letter-spacing:1px;transition:background .2s ease,color .2s ease;}
.ao-biz-more:hover{background:#1e2a4a;color:#fff !important;}
/* 自訂游標：AO logo + We Serve, We WOW */
.ao-biz-cursor{position:absolute;left:0;top:0;z-index:40;display:inline-flex;align-items:center;gap:8px;padding:6px 14px 6px 6px;border-radius:999px;background:#1e2a4a;color:#fff;font-size:14px;font-weight:800;white-space:nowrap;pointer-events:none;opacity:0;margin:22px 0 0 14px;box-shadow:0 8px 20px rgba(0,0,0,.4);transition:opacity .15s ease;}
.ao-biz-cursor::before{content:"";position:absolute;left:4px;top:-6px;border:6px solid transparent;border-bottom-color:#1e2a4a;border-left-color:#1e2a4a;}
.ao-biz.has-cursor .ao-biz-cursor{opacity:1;}
.ao-biz-logo{display:inline-block;width:52px;height:30px;border-radius:999px;background:#fff;position:relative;overflow:hidden;}
.ao-biz-logo img{position:absolute;left:50%;top:5px;width:59px !important;height:auto !important;max-width:none !important;margin-left:-29.5px;clip-path:inset(0 0 41% 0);}
.ao-biz-wrap .ao-biz-panel, .ao-biz-wrap .ao-biz-btn{position:relative;}
.ao-biz-wrap .ao-biz-panel{position:absolute;}

/* 浮動 icon 模式 */
.ao-biz.is-float .ao-biz-wrap{position:fixed;left:18px;bottom:96px;z-index:99990;animation:aoBizIn .3s ease;}
.ao-biz.is-float .ao-biz-btn{width:58px;height:58px;padding:0;justify-content:center;border-radius:50%;animation:aoBizPulse 1.3s ease-in-out infinite;}
.ao-biz.is-float .ao-biz-tx,.ao-biz.is-float .ao-biz-car{display:none;}
.ao-biz.is-float .ao-biz-bi{width:42px;height:42px;font-size:21px;}
.ao-biz.is-float .ao-biz-btn::after{content:"商務到會";position:absolute;left:calc(100% + 10px);top:50%;transform:translateY(-50%);padding:6px 12px;border-radius:999px;background:#1e2a4a;color:#fff;font-size:13px;font-weight:800;letter-spacing:1px;white-space:nowrap;box-shadow:0 6px 14px rgba(0,0,0,.35);}
.ao-biz.is-float .ao-biz-panel{left:0;top:auto;bottom:calc(100% + 14px);transform:translate(0,8px);}
.ao-biz.is-float.is-open .ao-biz-panel{transform:translate(0,0);}
.ao-biz.is-float .ao-biz-panel::after{left:28px;top:auto;bottom:-7px;}
.ao-biz.is-float .ao-biz-panel::before{top:auto;bottom:-14px;}
@keyframes aoBizIn{from{opacity:0;transform:translateY(16px);}to{opacity:1;transform:none;}}
@keyframes aoBizPulse{0%,100%{box-shadow:0 10px 24px rgba(10,20,50,.55),0 0 0 2px rgba(140,170,230,.35);}50%{box-shadow:0 10px 24px rgba(10,20,50,.55),0 0 0 9px rgba(140,170,230,0);}}
@media (max-width:640px){
  .ao-biz.is-float .ao-biz-wrap{left:12px;bottom:84px;}
  .ao-biz{margin:6px -14px 0;min-height:76px;padding:13px 12px;}
  .ao-biz-btn{height:48px;font-size:15px;letter-spacing:1px;padding-right:20px;}
  .ao-biz-cursor{display:none;}
  .ao-biz-list li{font-size:13.5px;padding:8px 10px !important;}
}
@media (prefers-reduced-motion:reduce){.ao-biz-btn{animation:none;}}
/* ===== Option B 微調：餐廳質感（參考 Dina / Steak In / Black Truffle） ===== */
.ao-qp{padding:0 36px 34px;overflow:hidden;background:#1d150f radial-gradient(120% 90% at 50% 0%,#2e2219 0%,#1d150f 60%,#140e0a 100%);box-shadow:inset 0 0 0 1px rgba(214,180,104,.3),0 30px 60px rgba(20,12,6,.25);border-radius:20px;}
.ao-qp-head--photo{margin:0 -36px 34px;padding:58px 24px 34px;background-size:cover;background-position:center 40%;}
.ao-qp-head--photo .ao-qp-eyebrow{color:#e2c48a;letter-spacing:4px;}
.ao-qp-head--photo .ao-qp-title{font-size:32px !important;letter-spacing:4px !important;text-shadow:0 2px 14px rgba(0,0,0,.55);}
.ao-qp-orn{display:inline-flex;align-items:center;gap:10px;margin:2px 0 10px;color:#d6b468;font-size:9px;}
.ao-qp-orn i{display:block;width:54px;height:1px;background:linear-gradient(90deg,rgba(214,180,104,0),#d6b468);}
.ao-qp-orn i:last-child{background:linear-gradient(90deg,#d6b468,rgba(214,180,104,0));}
.ao-qp-head--photo .ao-qp-sub{color:#efe2cc;text-shadow:0 1px 8px rgba(0,0,0,.5);}
/* 標籤：加英文小字，較精緻 */
.ao-qp-tag,.ao-qp-toptag{position:relative;padding:9px 24px 9px 20px;font-size:18px;letter-spacing:2px;}
.ao-qp-tag small,.ao-qp-toptag small{display:inline-block;margin-left:8px;padding-left:10px;border-left:1px solid currentColor;font-size:10.5px;font-weight:800;letter-spacing:2.5px;opacity:.7;}
/* 區塊框：更細嘅金線 + 內框 */
.ao-qp-box,.ao-qp-sec--top{box-shadow:0 18px 40px rgba(0,0,0,.3),inset 0 0 0 4px rgba(20,14,10,.6),inset 0 0 0 5px rgba(214,180,104,.14);}
/* 人數卡：底部細金線分隔 */
.ao-qp-ppl a{border-radius:12px;}
.ao-qp-ppl em{background:transparent;border-top:1px solid #e3d3b5;border-radius:0;padding:5px 2px 0;}
.ao-qp-ppl a:hover em{background:transparent;color:#7d5b27;}
/* 系列卡：hover 時金色內框 */
.ao-qp-series a{border-radius:12px;}
.ao-qp-series a:hover{box-shadow:inset 0 0 0 1px rgba(214,180,104,.55);}
/* TOP 5：相下金線 + 價錢襯托 */
.ao-qp-pop a{border-radius:12px;}
.ao-qp-ph{border-bottom:3px solid #d6b468;}
.ao-qp-pop a.is-hw .ao-qp-ph{border-bottom-color:#ff7a1a;}
.ao-qp-pi b{font-size:14.5px;}
/* WhatsApp：深色帶 */
.ao-qp-help{margin:6px -36px -34px;padding:26px 24px 30px;background:#140e0a;border-top:1px solid rgba(214,180,104,.3);}
@media (max-width:640px){
  .ao-qp{padding:0 14px 22px;border-radius:16px;max-width:none;margin-left:calc(50% - 50vw + 8px) !important;margin-right:calc(50% - 50vw + 8px) !important;}
  .ao-qp-box{padding-left:8px !important;padding-right:8px !important;}
  .ao-qp-head--photo{margin:0 -14px 26px;padding:40px 14px 26px;}
  .ao-qp-head--photo .ao-qp-title{font-size:24px !important;letter-spacing:2px !important;}
  .ao-qp-tag,.ao-qp-toptag{display:inline-block;white-space:nowrap;text-align:center;font-size:15px;padding:7px 18px 6px;letter-spacing:1px;border-radius:20px;line-height:1.35;}
  .ao-qp-tag i,.ao-qp-toptag i{display:inline-flex;vertical-align:1px;width:20px;height:20px;font-size:11px;margin-right:4px;}
  .ao-qp-toptag b{padding:1px 6px;}
  .ao-qp-tag small,.ao-qp-toptag small{display:block;margin:2px 0 0;padding:0;border:0;text-align:center;font-size:15px;letter-spacing:1.5px;opacity:.75;}
  .ao-qp-box,.ao-qp-sec--top{padding-top:44px;}
  /* 系列卡（手機）：上排 icon＋標籤，下排名稱 */
  .ao-qp-series a{display:grid;grid-template-columns:auto 1fr;grid-template-areas:"ic tag" "nm nm";align-items:center;gap:7px 8px;padding:11px 12px 12px;min-height:84px;}
  .ao-qp-series a > i{grid-area:ic;width:32px;height:32px;flex:none;font-size:16px;}
  .ao-qp-series a > span:not(.ao-qp-bats){display:contents;}
  .ao-qp-series a > span b{grid-area:nm;font-size:13.5px;line-height:1.35;}
  .ao-qp-series a > span small{display:none;}
  .ao-qp-series a > em,.ao-qp-series a.is-hot em{grid-area:tag;position:static;justify-self:start;margin:0;padding:3px 9px;font-size:10.5px;}
  .ao-qp-limit{grid-area:tag;justify-self:start;margin:0;padding:3px 10px;font-size:11px;}
  .ao-qp-series a.is-hw b{font-size:13.5px;}
  .ao-qp-help{margin:6px -14px -22px;}
}
'''
b=b.replace('</style>',extra+'</style>',1)
open('option-b.html','w',encoding='utf-8').write(b)
hd='<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>*,*::before,*::after{box-sizing:border-box}html,body{overflow-x:hidden}body{margin:0;font-family:"Rubik","Noto Sans TC","PingFang TC",sans-serif;background:#fff;color:#333}.hd{height:60px;background:#a98a52}.wpcol{padding:20px 15px}@media(min-width:768px){.wpcol{padding:30px 30px}}</style></head><body><div class="hd"></div><div class="wpcol">'
open('preview-b.html','w',encoding='utf-8').write(hd+b+'</div></body></html>')
P='/sessions/great-festive-darwin/mnt/Desktop/cowork - aoao/pages/'
shutil.copy('option-b.html',P+'party-quickpick-option-B.html'); shutil.copy('preview-b.html',P+'party-quickpick-option-B-preview.html')
idx=open('index.html',encoding='utf-8').read()
idx=re.sub(r'(<textarea id="cb"[^>]*>).*?(</textarea>)',lambda m:m.group(1)+html.escape(b)+m.group(2),idx,flags=re.S)
idx=idx.replace('Option B｜餐廳雜誌風（Dina／Steak In 風格）','Option B｜黑金・餐廳質感版（A 微調）').replace('B｜餐廳雜誌風','B｜黑金餐廳質感')
open('index.html','w',encoding='utf-8').write(idx)
pv=hd+b+'</div></body></html>'
fr=lambda w,h,s: f'<div style="display:inline-block;vertical-align:top;width:{int(w*s)}px;height:{int(h*s)}px;overflow:hidden;margin:3px"><iframe style="width:{w}px;height:{h}px;border:0;transform:scale({s});transform-origin:0 0" srcdoc="{html.escape(pv,quote=True)}"></iframe></div>'
open('/sessions/great-festive-darwin/mnt/outputs/qpb3.html','w',encoding='utf-8').write('<!doctype html><meta charset="utf-8"><body style="margin:0;background:#222;white-space:nowrap">'+fr(1300,1750,0.42)+fr(390,1500,0.42)+'</body>')
print(len(b))
