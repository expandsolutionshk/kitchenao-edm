import urllib.parse, html, shutil
B='https://aoaodelivery.com'; U=B+'/wp-content/uploads/'
def dl(l): return f" onclick=\"window.dataLayer=window.dataLayer||[];dataLayer.push({{event:'cta_click',cta_label:'{l}'}});\""
PPL=[('2 - 6','小型聚會','2-6人','qp_ppl_2_6'),('7 - 11','家庭派對','7-11人','qp_ppl_7_11'),('12 - 16','生日派對','12-16人','qp_ppl_12_16'),('18 - 25','公司／朋友聚餐','18-25人','qp_ppl_18_25'),('30+','大型活動','30人以上','qp_ppl_30'),('100+','企業活動','100人以上','qp_ppl_100')]
SER=[('🎃','Halloween 萬聖節狂嘩套餐','期間限定・10月23日至11月1日送貨','/product-category/halloween-set/?ao_ref=hw26_party_qp','qp_s_halloween','期間限定','hw'),
('⭐','美食派對 Gourmet','人氣之選・熱食主菜','/product-category/party/foot-party/','qp_s_gourmet','人氣','hot'),
('🥂','輕食宴會 Refreshment','會議茶點・開幕酒會','/product-category/party/refreshment-set/','qp_s_refreshment','',''),
('🚤','船河派對套餐','碼頭交收・方便分發','/product-category/party/boat-party-set/','qp_s_boat','',''),
('🧸','兒童派對套餐','兒童生日派對','/product-category/party/children/','qp_s_kids','',''),
('💑','雙人套餐','二人慶祝・紀念日','/product-category/party/set-for-two/','qp_s_couple','',''),
('🥗','「素」味人生','素食派對套餐','/product-category/party/vegetarians-set/','qp_s_veg','',''),
('🍖','肉食獸套餐','上將海港之選','/product-category/party/meat-monster/','qp_s_meat','',''),
('🧺','Chill 一下野餐盒','野餐・戶外活動','/product-category/party/chill-box/','qp_s_chill','',''),
('🍢','手指食物拼盤','Finger Food・Platter','/product-category/party/platter/','qp_s_platter','','')]
# (id, name, desc, price, regular, suffix, img, url, cls)
TOP=[(21622,'AO 18 - 22 人 Halloween 萬聖節狂嘩套餐','期間限定・5 大狂嘩主打菜式',3758,4088,'',U+'2026/10/2026-Halloween-18-22_set-photo-600x600.jpg','/product/ao-18-22pax-halloween萬聖節狂嘩套餐/','hw'),
(6262,'AO 12 - 16 人美食派對 Gourmet Set','人氣之選・熱食主菜',2988,2988,'',U+'2026/03/12-16_101-X-KITCHENAO-03-03-03-03-600x600.jpg','/product/ao-12-16pax-gourmet-set/',''),
(6394,'派對大快樂兒童餐（5 人起）','兒童生日派對・自選人數',600,600,'起',U+'2023/10/202308-KIDS-thumbnail_工作區域-1-600x600.jpg','/product/party-big-happy-kids-meal-select-the-number-of-people-5-people-or-more/',''),
(6407,'AO 18 - 22 人輕食宴會套餐 Refreshment','會議茶點・開幕酒會',3488,3488,'',U+'2023/11/refreshmentparty-04-600x600.jpg','/product/ao-18-22pax-refreshment-set/',''),
(14314,'AO 36 - 40 人狂歡派對船河套餐','Boat Party Set・碼頭交收',6332,6332,'',U+'2025/04/WhatsApp-Image-2025-04-12-at-4.08.26-PM-600x600.jpeg','/product/ao-36-40pax-狂歡派對船河套餐-boat-party-set/','')]
WA='https://wa.me/85269011987?text='+urllib.parse.quote('你好，我已在 Kitchen AO 網站瀏覽過派對到會餐單，但仍未決定選擇哪一款，想查詢以下問題：')
def ppl_url(k): return B+'/product-category/party-set-by-people/'+k+'分享選項/'
def price_html(p,r,suf):
    s=f'<strong data-price>HK${p:,}{suf}</strong>'
    if r>p: s+=f'<del data-reg>HK${r:,}</del>'
    return s
ppl=''.join(f'<a href="{ppl_url(k)}"{dl(t)}><b>{n}<small>人</small></b><em>{d}</em></a>' for n,d,k,t in PPL)
ser=''.join(f'<a class="{"is-"+c if c else ""}" href="{B+u}"{dl(t)}><i>{e}</i><span><b>{n}</b><small>{s}</small></span>{f"<em>{bd}</em>" if bd else ""}</a>' for e,n,s,u,t,bd,c in SER)
top=''.join(f'''<a class="{"is-"+c if c else ""}" href="{B+u}" data-pid="{pid}" data-suffix="{suf}"{dl("qp_top_"+str(pid))}><span class="ao-qp-ph"><img src="{img}" alt="{html.escape(n)}" width="600" height="600" loading="lazy" decoding="async"><span class="ao-qp-rank">TOP {i+1}</span></span><span class="ao-qp-pi"><b>{n}</b><em>{d}</em><span class="ao-qp-pr">{price_html(p,r,suf)}</span><span class="ao-qp-btn">查看詳情</span></span></a>''' for i,(pid,n,d,p,r,suf,img,u,c) in enumerate(TOP))
MARK=f'''<!-- ===== Kitchen AO｜/product-category/party/ 快速選擇派對套餐｜Option A 黑金（Raw HTML）===== -->
<section class="ao-qp ao-qp--a" aria-labelledby="ao-qp-title">
  <div class="ao-qp-head">
    <p class="ao-qp-eyebrow">Kitchen AO Party Catering</p>
    <h2 id="ao-qp-title" class="ao-qp-title">快速選擇派對套餐</h2>
    <p class="ao-qp-sub">先按人數或系列選擇合適套餐，再直接網上下單。</p>
  </div>
  <div class="ao-qp-sec"><div class="ao-qp-lbl"><span>1</span>按人數選擇</div><div class="ao-qp-ppl">{ppl}</div></div>
  <div class="ao-qp-sec"><div class="ao-qp-lbl"><span>2</span>按系列選擇</div><div class="ao-qp-series">{ser}</div></div>
  <div class="ao-qp-sec ao-qp-sec--top">
    <div class="ao-qp-tophead"><span class="ao-qp-toptag"><i>3</i>🔥 本週 <b>TOP 5</b> 人氣推介</span></div>
    <div class="ao-qp-pop">{top}</div>
  </div>
  <div class="ao-qp-help"><p>仍未決定選擇哪一款？</p><a href="{WA}" target="_blank" rel="noopener noreferrer"{dl('qp_whatsapp')}>WhatsApp 專人為你配搭餐單</a></div>
</section>'''
JS='''<script>
(function(){
  /* 自動更新「本週 TOP 5 人氣推介」價錢（讀取 WooCommerce 現價；失敗則保留原價） */
  var box=document.currentScript&&document.currentScript.previousElementSibling;
  if(!box||!window.fetch)return;
  var cards=box.querySelectorAll('[data-pid]');var ids=[].map.call(cards,function(a){return a.getAttribute('data-pid')}).join(',');
  fetch('/wp-json/wc/store/v1/products?include='+ids+'&per_page=10').then(function(r){return r.json()}).then(function(list){
    list.forEach(function(p){
      var card=box.querySelector('[data-pid="'+p.id+'"]');if(!card||!p.prices)return;
      var m=Math.pow(10,p.prices.currency_minor_unit||0),now=Math.round(p.prices.price/m),reg=Math.round(p.prices.regular_price/m),suf=card.getAttribute('data-suffix')||'';
      var pr=card.querySelector('.ao-qp-pr');if(!pr)return;
      pr.innerHTML='<strong data-price>HK$'+now.toLocaleString('en-US')+suf+'</strong>'+(reg>now?'<del data-reg>HK$'+reg.toLocaleString('en-US')+'</del>':'');
    });
  }).catch(function(){});
})();
</script>'''
CSS='''<style>
.ao-qp{max-width:1180px;margin:16px auto 32px;padding:40px 36px 34px;border-radius:24px;background:radial-gradient(120% 140% at 0% 0%,#3a2a20 0%,#211812 55%,#15100c 100%);color:#efe5d6;box-shadow:inset 0 0 0 1px rgba(214,180,104,.25);font-family:inherit;}
.ao-qp *{box-sizing:border-box;font-family:inherit;}
.ao-qp a{text-decoration:none !important;}
.ao-qp-head{text-align:center;margin:0 0 28px;}
.ao-qp-eyebrow{margin:0 0 8px !important;color:#c9a45c;font-size:11px;font-weight:700;letter-spacing:2px;line-height:1.3;text-transform:uppercase;}
.ao-qp .ao-qp-title{margin:0 0 6px !important;color:#f8f1e7 !important;font-size:28px;font-weight:800;line-height:1.35;letter-spacing:1px;}
.ao-qp-sub{margin:0 !important;color:#cbbca6;font-size:15px;line-height:1.7;}
.ao-qp-sec{margin:0 0 28px;}
.ao-qp-lbl{display:flex;align-items:center;gap:10px;margin:0 0 12px;color:#e3c98f;font-size:16px;font-weight:800;letter-spacing:.5px;}
.ao-qp-lbl span{display:inline-flex;align-items:center;justify-content:center;width:24px;height:24px;border-radius:50%;background:#d6b468;color:#241a12;font-size:13px;font-weight:800;}
.ao-qp-lbl::after{content:"";flex:1;height:1px;background:linear-gradient(90deg,rgba(214,180,104,.5),rgba(214,180,104,0));}

/* ===== 本週 TOP 5：大字 + 金色標籤 + 疊層卡 ===== */
.ao-qp-sec--top{position:relative;margin-top:44px;padding:34px 20px 22px;border-radius:20px;background:linear-gradient(180deg,rgba(214,180,104,.14) 0%,rgba(214,180,104,.04) 100%);border:1px solid rgba(214,180,104,.35);box-shadow:0 18px 40px rgba(0,0,0,.35),0 0 0 6px rgba(214,180,104,.06);}
.ao-qp-tophead{position:absolute;left:50%;top:0;transform:translate(-50%,-50%);z-index:2;white-space:nowrap;}
.ao-qp-toptag{display:inline-flex;align-items:center;gap:6px;padding:10px 26px;border-radius:999px;background:linear-gradient(135deg,#f0d39a 0%,#d2a44e 100%);color:#241a12;font-size:21px;font-weight:800;letter-spacing:1px;line-height:1.2;box-shadow:0 8px 20px rgba(0,0,0,.45),0 0 0 4px #211812,0 0 0 5px rgba(214,180,104,.6);}
.ao-qp-toptag i{display:inline-flex;align-items:center;justify-content:center;width:24px;height:24px;margin-right:2px;border-radius:50%;background:#241a12;color:#f0d39a;font-style:normal;font-size:13px;}
.ao-qp-toptag b{padding:2px 9px;border-radius:8px;background:#241a12;color:#f0d39a;font-weight:800;}
.ao-qp-pop{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:14px;margin-top:6px;}
.ao-qp-pop a{position:relative;display:flex;flex-direction:column;overflow:hidden;border-radius:16px;border:1px solid rgba(214,180,104,.25);background:#1b140f;color:#f6eddf !important;box-shadow:0 10px 24px rgba(0,0,0,.35);transition:transform .25s ease,border-color .25s ease;}
.ao-qp-pop a:hover{transform:translateY(-4px);border-color:#c9a45c;}
.ao-qp-ph{position:relative;display:block;aspect-ratio:1/1;overflow:hidden;}
.ao-qp-ph img{display:block;width:100% !important;height:100% !important;object-fit:cover;transition:transform .5s ease;}
.ao-qp-pop a:hover .ao-qp-ph img{transform:scale(1.05);}
.ao-qp-rank{position:absolute;left:10px;top:10px;padding:4px 10px;border-radius:8px;background:rgba(21,16,12,.85);color:#f0d39a;font-size:12px;font-weight:800;letter-spacing:1px;border:1px solid rgba(214,180,104,.6);}
.ao-qp-pi{display:flex;flex-direction:column;flex:1;padding:12px 12px 14px;}
.ao-qp-pi b{font-size:14.5px;font-weight:700;line-height:1.45;}
.ao-qp-pi em{margin-top:3px;font-style:normal;font-size:12px;color:#a99880;line-height:1.5;}
.ao-qp-pr{display:flex;align-items:baseline;flex-wrap:wrap;gap:4px 8px;margin-top:auto;padding-top:10px;}
.ao-qp-pr strong{font-size:18px;font-weight:800;color:#e7c98b;}
.ao-qp-pr del{font-size:12px;color:#8d7f6c;}
.ao-qp-btn{display:block;margin-top:10px;padding:9px 10px;border-radius:999px;background:linear-gradient(135deg,#e3c482,#b8893f);color:#1d150f;font-size:13.5px;font-weight:800;text-align:center;line-height:1.2;transition:filter .2s ease;}
.ao-qp-pop a:hover .ao-qp-btn{filter:brightness(1.1);}
/* Halloween 卡（跟 Pop up 紫橙色調） */
.ao-qp-pop a.is-hw{background:linear-gradient(180deg,#2c1f3b 0%,#1c1426 100%);border-color:#ff7a1a;box-shadow:0 10px 26px rgba(255,90,0,.25);}
.ao-qp-pop a.is-hw .ao-qp-rank{background:#ff7a1a;color:#1c1426;border-color:#ff7a1a;}
.ao-qp-pop a.is-hw em{color:#cdb8e6;}
.ao-qp-pop a.is-hw .ao-qp-pr strong{color:#ffb347;}
.ao-qp-pop a.is-hw .ao-qp-btn{background:linear-gradient(135deg,#ff8a1f,#ff5a00);color:#1c1426;}

/* ===== 按人數（白卡） ===== */
.ao-qp-ppl{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:10px;}
.ao-qp-ppl a{position:relative;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:5px;min-height:78px;padding:12px 6px;border:2px solid transparent;border-radius:14px;background:#fff;color:#2b211b !important;text-align:center;line-height:1.2;box-shadow:0 6px 16px rgba(0,0,0,.28);transition:all .25s ease;}
.ao-qp-ppl a::before{content:"";position:absolute;left:50%;top:0;width:28px;height:3px;border-radius:0 0 3px 3px;background:#d2a44e;transform:translateX(-50%);transition:width .25s ease;}
.ao-qp-ppl b{display:flex;align-items:baseline;gap:4px;font-size:21px;font-weight:800;white-space:nowrap;color:#2b211b;letter-spacing:.3px;}
.ao-qp-ppl small{font-size:13px;font-weight:700;color:#9a7230;}
.ao-qp-ppl em{font-style:normal;font-size:12px;color:#7d6e60;white-space:nowrap;}
.ao-qp-ppl a:hover,.ao-qp-ppl a:focus-visible{border-color:#d6b468;background:#fbf3e3;}
.ao-qp-ppl a:hover::before{width:60%;}

/* ===== 按系列 ===== */
.ao-qp-series{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;}
.ao-qp-series a{position:relative;display:flex;align-items:center;gap:14px;padding:13px 16px;border-radius:14px;border:1px solid rgba(214,180,104,.2);background:rgba(255,255,255,.035);color:#f6eddf !important;transition:all .25s ease;}
.ao-qp-series a:hover{border-color:#c9a45c;background:rgba(201,164,92,.1);}
.ao-qp-series i{flex:0 0 40px;height:40px;display:flex;align-items:center;justify-content:center;border-radius:12px;background:rgba(214,180,104,.16);font-style:normal;font-size:19px;}
.ao-qp-series span{display:flex;flex-direction:column;min-width:0;}
.ao-qp-series b{font-size:15px;font-weight:800;line-height:1.35;}
.ao-qp-series small{margin-top:2px;font-size:12.5px;color:#a99880;line-height:1.4;}
.ao-qp-series em{margin-left:auto;flex:0 0 auto;padding:3px 10px;border-radius:999px;font-style:normal;font-size:11px;font-weight:800;white-space:nowrap;}
/* 美食派對：金色 highlight */
.ao-qp-series a.is-hot{background:linear-gradient(135deg,#f0d39a 0%,#d2a44e 100%);border-color:transparent;color:#241a12 !important;}
.ao-qp-series a.is-hot small{color:#5a4320;}
.ao-qp-series a.is-hot i{background:rgba(255,255,255,.45);}
.ao-qp-series a.is-hot em{background:#c0392b;color:#fff;}
.ao-qp-series a.is-hot:hover{filter:brightness(1.05);}
/* Halloween：跟 Pop up 紫橙色調 */
.ao-qp-series a.is-hw{background:linear-gradient(135deg,#2c1f3b 0%,#1c1426 100%);border:1.5px solid #ff7a1a;box-shadow:0 6px 18px rgba(255,90,0,.22);}
.ao-qp-series a.is-hw b{color:#fff;}
.ao-qp-series a.is-hw small{color:#cdb8e6;}
.ao-qp-series a.is-hw i{background:rgba(255,122,26,.18);}
.ao-qp-series a.is-hw em{background:linear-gradient(135deg,#ff8a1f,#ff5a00);color:#1c1426;}
.ao-qp-series a.is-hw:hover{background:linear-gradient(135deg,#3a2850 0%,#22182e 100%);}

/* ===== WhatsApp ===== */
.ao-qp-help{display:flex;align-items:center;justify-content:center;flex-wrap:wrap;gap:10px 18px;padding-top:22px;border-top:1px solid rgba(214,180,104,.22);}
.ao-qp-help p{margin:0 !important;font-size:15px;color:#cbbca6;}
.ao-qp-help a{display:inline-block;padding:13px 28px;border-radius:999px;background:linear-gradient(135deg,#e3c482,#b8893f);color:#1d150f !important;font-size:15px;font-weight:800;line-height:1.2;}
.ao-qp-help a:hover{filter:brightness(1.08);}
.ao-qp img.emoji{display:inline !important;width:1em !important;height:1em !important;margin:0 !important;vertical-align:-0.12em !important;}

@media (max-width:1080px){.ao-qp-pop{grid-template-columns:repeat(3,minmax(0,1fr));}}
@media (max-width:960px){.ao-qp-ppl{grid-template-columns:repeat(3,minmax(0,1fr));}}
@media (max-width:640px){
  .ao-qp{padding:26px 14px 22px;border-radius:18px;}
  .ao-qp .ao-qp-title{font-size:23px;}
  .ao-qp-sub{font-size:14px;}
  .ao-qp-sec{margin-bottom:24px;}
  .ao-qp-sec--top{margin-top:36px;padding:30px 0 14px 12px;border-radius:16px;}
  .ao-qp-toptag{font-size:17px;padding:8px 18px;}
  .ao-qp-pop{display:flex;gap:10px;overflow-x:auto;scroll-snap-type:x mandatory;padding:4px 12px 8px 0;scrollbar-width:none;}
  .ao-qp-pop::-webkit-scrollbar{display:none;}
  .ao-qp-pop a{flex:0 0 62%;scroll-snap-align:start;}
  .ao-qp-ppl{gap:8px;}
  .ao-qp-ppl a{min-height:66px;padding:10px 4px;border-radius:12px;}
  .ao-qp-ppl b{font-size:17px;}
  .ao-qp-ppl em{font-size:11px;}
  .ao-qp-series{gap:8px;}
  .ao-qp-series a{gap:9px;padding:10px 10px;}
  .ao-qp-series i{flex-basis:30px;height:30px;font-size:16px;border-radius:9px;}
  .ao-qp-series b{font-size:13px;}
  .ao-qp-series small{display:none;}
  .ao-qp-series em{position:absolute;top:-8px;right:6px;padding:2px 7px;font-size:10px;}
  .ao-qp-help{flex-direction:column;}
  .ao-qp-help a{width:100%;text-align:center;}
}
@media (prefers-reduced-motion:reduce){.ao-qp a,.ao-qp img{transition:none !important;}}
</style>'''
code=MARK+'\n'+JS+'\n'+CSS+'\n'
open('option-a.html','w',encoding='utf-8').write(code)
head='<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>*,*::before,*::after{box-sizing:border-box}html,body{overflow-x:hidden}body{margin:0;font-family:"Rubik","Noto Sans TC","PingFang TC",sans-serif;background:#fff;color:#333}.hd{height:60px;background:#a98a52}.wpcol{padding:20px 15px}@media(min-width:768px){.wpcol{padding:30px 30px}}</style></head><body><div class="hd"></div><div class="wpcol">'
open('preview-a.html','w',encoding='utf-8').write(head+code+'</div></body></html>')
P='/sessions/great-festive-darwin/mnt/Desktop/cowork - aoao/pages/'
shutil.copy('option-a.html',P+'party-quickpick-option-A.html'); shutil.copy('preview-a.html',P+'party-quickpick-option-A-preview.html')
import re
idx=open('index.html',encoding='utf-8').read()
idx=re.sub(r'(<textarea id="ca"[^>]*>).*?(</textarea>)',lambda m:m.group(1)+html.escape(code)+m.group(2),idx,flags=re.S)
open('index.html','w',encoding='utf-8').write(idx)
print(len(code), code.count('–'), code.count('→'))
fr=lambda w,h,s: f'<div style="display:inline-block;vertical-align:top;width:{int(w*s)}px;height:{int(h*s)}px;overflow:hidden;margin:3px"><iframe style="width:{w}px;height:{h}px;border:0;transform:scale({s});transform-origin:0 0" srcdoc="{html.escape(head+code+"</div></body></html>",quote=True)}"></iframe></div>'
open('/sessions/great-festive-darwin/mnt/outputs/qpa.html','w',encoding='utf-8').write('<!doctype html><meta charset="utf-8"><body style="margin:0;background:#222;white-space:nowrap">'+fr(1300,1500,0.5)+fr(390,1600,0.47)+'</body>')
