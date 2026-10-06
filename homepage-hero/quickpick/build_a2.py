import urllib.parse, html, shutil
B='https://aoaodelivery.com'; U=B+'/wp-content/uploads/'
def dl(l): return f" onclick=\"window.dataLayer=window.dataLayer||[];dataLayer.push({{event:'cta_click',cta_label:'{l}'}});\""
PPL=[('2 - 6','小型聚會','2-6人','qp_ppl_2_6'),('7 - 11','家庭派對','7-11人','qp_ppl_7_11'),('12 - 16','生日派對','12-16人','qp_ppl_12_16'),('18 - 25','公司／朋友聚餐','18-25人','qp_ppl_18_25'),('30+','大型活動','30人以上','qp_ppl_30'),('100+','企業活動','100人以上','qp_ppl_100')]
SER=[('🎃','Halloween|萬聖節狂嘩套餐','','/product-category/halloween-set/?ao_ref=hw26_party_qp','qp_s_halloween','期間限定','hw'),
('⭐','美食派對|Gourmet Set','人氣之選・熱食主菜','/product-category/party/foot-party/','qp_s_gourmet','人氣','hot'),
('🥂','輕食宴會 Refreshment','會議茶點・開幕酒會','/product-category/party/refreshment-set/','qp_s_refreshment','',''),
('🍖','肉食獸套餐','上將海港之選','/product-category/party/meat-monster/','qp_s_meat','',''),
('🧸','兒童派對套餐','兒童生日派對','/product-category/party/children/','qp_s_kids','',''),
('💑','雙人套餐','二人慶祝・紀念日','/product-category/party/set-for-two/','qp_s_couple','',''),
('🥗','「素」味人生','素食派對套餐','/product-category/party/vegetarians-set/','qp_s_veg','',''),
('🚤','船河派對套餐','碼頭交收・方便分發','/product-category/party/boat-party-set/','qp_s_boat','',''),
('🧺','Chill 一下野餐盒','野餐・戶外活動','/product-category/party/chill-box/','qp_s_chill','',''),
('🍢','手指食物拼盤','Finger Food・Platter','/product-category/party/platter/','qp_s_platter','',''),
('🍽️','單品|À la carte','小食・主菜・甜品自由配搭','/product-category/a-la-carte/','qp_s_alacarte','',''),
('🎉','派對用品|Party Supplies','餐具・食物架・派對配件','/product-category/party-supplies/','qp_s_supplies','','')]
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
BAT='<svg viewBox="0 0 100 44"><path d="M50 18 L53 9 L55.5 17 C62 12 78 6 97 10 C89 14 85 20 87 27 C81 22 75 22 71 29 C67 24 61 24 57.5 31 C55 29 52.5 33 50 38 C47.5 33 45 29 42.5 31 C39 24 33 24 29 29 C25 22 19 22 13 27 C15 20 11 14 3 10 C22 6 38 12 44.5 17 L47 9 Z" fill="#2a0d3d"/><circle cx="47.6" cy="20" r="1.6" fill="#FFE14D"/><circle cx="52.4" cy="20" r="1.6" fill="#FFE14D"/></svg>'
BATS='<span class="ao-qp-bats" aria-hidden="true"><i class="b1">'+BAT+'</i><i class="b2">'+BAT+'</i><i class="b3">'+BAT+'</i></span>'
ppl=''.join(f'<a href="{ppl_url(k)}" target="_blank" rel="noopener"{dl(t)}><b>{n}<small>人</small></b><em>{d}</em></a>' for n,d,k,t in PPL)
def nm(n): return n.replace('|','<span class="ao-qp-l2"> ',1)+'</span>' if '|' in n else n
ser=''.join((f'<a class="is-hw" href="{B+u}" target="_blank" rel="noopener"{dl(t)}>{BATS}<i>{e}</i><span><mark class="ao-qp-limit">{bd}</mark><b>{nm(n)}</b></span></a>' if c=="hw" else f'<a class="{"is-"+c if c else ""}" href="{B+u}" target="_blank" rel="noopener"{dl(t)}><i>{e}</i><span><b>{nm(n)}</b>{f"<small>{s}</small>" if s else ""}</span>{f"<em>{bd}</em>" if bd else ""}</a>') for e,n,s,u,t,bd,c in SER)
top=''.join(f'''<a class="{"is-"+c if c else ""}" href="{B+u}" target="_blank" rel="noopener" data-pid="{pid}" data-suffix="{suf}"{dl("qp_top_"+str(pid))}><span class="ao-qp-ph"><img src="{img}" alt="{html.escape(n)}" width="600" height="600" loading="lazy" decoding="async"><span class="ao-qp-rank">TOP {i+1}</span></span><span class="ao-qp-pi"><b>{n}</b><em>{d}</em><span class="ao-qp-pr">{price_html(p,r,suf)}</span><span class="ao-qp-btn"><span>查看詳情</span></span></span></a>''' for i,(pid,n,d,p,r,suf,img,u,c) in enumerate(TOP))
MARK=f'''<!-- ===== Kitchen AO｜/product-category/party/ 快速選擇派對套餐｜Option A 黑金（Raw HTML）===== -->
<section class="ao-qp ao-qp--a" aria-labelledby="ao-qp-title">
  <div class="ao-qp-head">
    <p class="ao-qp-eyebrow">Kitchen AO Party Catering</p>
    <h2 id="ao-qp-title" class="ao-qp-title">快速選擇派對套餐</h2>
    <p class="ao-qp-sub">先按人數或系列選擇合適套餐，再直接網上下單。</p>
  </div>
  <div class="ao-qp-sec ao-qp-box ao-qp-box--ppl"><div class="ao-qp-tophead"><span class="ao-qp-tag ao-qp-tag--ppl"><i>1</i>👥 按人數選擇</span></div><div class="ao-qp-ppl">{ppl}</div></div>
  <div class="ao-qp-sec ao-qp-box ao-qp-box--ser"><div class="ao-qp-tophead"><span class="ao-qp-tag ao-qp-tag--ser"><i>2</i>🍽️ 按系列選擇</span></div><div class="ao-qp-series">{ser}</div></div>
  <div class="ao-qp-sec ao-qp-sec--top">
    <div class="ao-qp-tophead"><span class="ao-qp-toptag"><i>3</i>🔥 本週 <b>TOP 5</b> 人氣推介</span></div>
    <div class="ao-qp-slider"><button type="button" class="ao-qp-nav ao-qp-prev" aria-label="上一個">‹</button><div class="ao-qp-pop">{top}</div><button type="button" class="ao-qp-nav ao-qp-next" aria-label="下一個">›</button></div>
    <div class="ao-qp-dots" aria-hidden="true"></div>
  </div>
  <div class="ao-qp-help"><p>仍未決定選擇哪一款？</p><a href="{WA}" target="_blank" rel="noopener noreferrer"{dl('qp_whatsapp')}>WhatsApp 專人為你配搭餐單</a></div>
</section>'''
JS='''<script>
(function(){
  /* TOP 5 slider：箭咀＋圓點（≤1080px） */
  var sec=document.currentScript&&document.currentScript.previousElementSibling;if(!sec)return;
  var sl=sec.querySelector('.ao-qp-slider');if(!sl)return;
  var track=sl.querySelector('.ao-qp-pop'),prev=sl.querySelector('.ao-qp-prev'),next=sl.querySelector('.ao-qp-next'),dots=sec.querySelector('.ao-qp-dots');
  var cards=track.children;for(var i=0;i<cards.length;i++){dots.appendChild(document.createElement('i'));}
  function step(){return cards.length>1?cards[1].offsetLeft-cards[0].offsetLeft:track.clientWidth;}
  function upd(){var max=track.scrollWidth-track.clientWidth-2;prev.disabled=track.scrollLeft<=2;next.disabled=track.scrollLeft>=max;
    var idx=Math.round(track.scrollLeft/step());if(track.scrollLeft>=max)idx=cards.length-1;[].forEach.call(dots.children,function(d,k){d.classList.toggle('on',k===idx);});}
  prev.addEventListener('click',function(){track.scrollBy({left:-step(),behavior:'smooth'});});
  next.addEventListener('click',function(){track.scrollBy({left:step(),behavior:'smooth'});});
  track.addEventListener('scroll',function(){window.requestAnimationFrame(upd);},{passive:true});
  window.addEventListener('resize',upd);upd();
})();
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
.ao-qp-eyebrow{text-align:center !important;margin:0 0 8px !important;color:#c9a45c;font-size:11px;font-weight:700;letter-spacing:2px;line-height:1.3;text-transform:uppercase;}
.ao-qp .ao-qp-title{margin:0 0 6px !important;color:#f8f1e7 !important;font-size:28px;font-weight:800;line-height:1.35;letter-spacing:1px;}
.ao-qp-sub{text-align:center !important;margin:0 !important;color:#cbbca6;font-size:15px;line-height:1.7;}
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
.ao-qp-pop a{position:relative;display:flex;flex-direction:column;overflow:hidden;border-radius:16px;border:1px solid #fff;background:#fff;color:#2b211b !important;box-shadow:0 10px 24px rgba(0,0,0,.35);transition:transform .25s ease,border-color .25s ease;}
@media (hover:hover){.ao-qp-pop a:hover{transform:translateY(-4px);border-color:#c9a45c;}}
.ao-qp-ph{position:relative;display:block;aspect-ratio:1/1;overflow:hidden;}
.ao-qp-ph img{display:block;width:100% !important;height:100% !important;object-fit:cover;transition:transform .5s ease;}
.ao-qp-pop a:hover .ao-qp-ph img{transform:scale(1.05);}
.ao-qp-rank{position:absolute;left:10px;top:10px;padding:5px 11px;border-radius:8px;background:#ffd23f;color:#1d150f;font-size:12.5px;font-weight:900;letter-spacing:1px;box-shadow:0 4px 12px rgba(0,0,0,.35),0 0 0 2px #1d150f;}
.ao-qp-pi{display:flex;flex-direction:column;flex:1;padding:12px 12px 14px;}
.ao-qp-pi b{font-size:14.5px;font-weight:700;line-height:1.45;}
.ao-qp-pi em{margin-top:3px;font-style:normal;font-size:12px;color:#8a7b6e;line-height:1.5;}
.ao-qp-pr{display:flex;align-items:baseline;flex-wrap:wrap;gap:4px 8px;margin-top:auto;padding-top:10px;}
.ao-qp-pr strong{font-size:18px;font-weight:800;color:#9a6b1f;}
.ao-qp-pr del{font-size:12px;color:#a39686;}
.ao-qp-btn{display:block;margin-top:10px;padding:9px 10px;border-radius:999px;background:linear-gradient(135deg,#e3c482,#b8893f);color:#1d150f;font-size:13.5px;font-weight:800;text-align:center;line-height:1.2;transition:filter .2s ease;}
.ao-qp-pop a:hover .ao-qp-btn{filter:brightness(1.1);}
/* Halloween 卡（跟 Pop up 紫橙色調） */
.ao-qp-pop a.is-hw{background:linear-gradient(180deg,#2c1f3b 0%,#1c1426 100%);border-color:#ff7a1a;color:#f6eddf !important;box-shadow:0 10px 26px rgba(255,90,0,.25);}

.ao-qp-pop a.is-hw em{color:#cdb8e6;}
.ao-qp-pop a.is-hw .ao-qp-pr strong{color:#ffb347;}
.ao-qp-pop a.is-hw .ao-qp-pr del{color:#9c8bb3;}
.ao-qp-pop a.is-hw .ao-qp-btn{background:linear-gradient(135deg,#ff8a1f,#ff5a00);color:#1c1426;}


/* ===== 1・2 區塊：同 TOP 5 一樣疊層標籤，但用唔同顏色 ===== */
.ao-qp-box{position:relative;margin-top:44px;padding:34px 20px 22px;border-radius:20px;box-shadow:0 18px 40px rgba(0,0,0,.3);}
.ao-qp-tag{display:inline-flex;align-items:center;gap:6px;padding:10px 26px;border-radius:999px;font-size:19px;font-weight:800;letter-spacing:1px;line-height:1.2;}
.ao-qp-tag i{display:inline-flex;align-items:center;justify-content:center;width:24px;height:24px;margin-right:2px;border-radius:50%;font-style:normal;font-size:13px;}
/* 1 按人數：象牙白 */
.ao-qp-box--ppl{background:linear-gradient(180deg,rgba(246,237,223,.10) 0%,rgba(246,237,223,.03) 100%);border:1px solid rgba(246,237,223,.35);}
.ao-qp-tag--ppl{background:linear-gradient(135deg,#fffaf1 0%,#eadcc4 100%);color:#2b211b;box-shadow:0 8px 20px rgba(0,0,0,.45),0 0 0 4px #211812,0 0 0 5px rgba(246,237,223,.55);}
.ao-qp-tag--ppl i{background:#2b211b;color:#f6eddf;}
/* 2 按系列：玫瑰銅 */
.ao-qp-box--ser{background:linear-gradient(180deg,rgba(196,120,84,.14) 0%,rgba(196,120,84,.04) 100%);border:1px solid rgba(214,140,104,.45);}
.ao-qp-tag--ser{background:linear-gradient(135deg,#e6a37f 0%,#a95c3b 100%);color:#fff;box-shadow:0 8px 20px rgba(0,0,0,.45),0 0 0 4px #211812,0 0 0 5px rgba(214,140,104,.6);}
.ao-qp-tag--ser i{background:#fff;color:#8f4a2d;}

/* ===== 按人數（白卡） ===== */
.ao-qp-ppl{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:10px;}
.ao-qp-ppl a{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:7px;min-height:84px;padding:12px 6px;border:1.5px solid #fff;border-radius:16px;background:linear-gradient(180deg,#ffffff 0%,#f8f2e8 100%);color:#2b211b !important;text-align:center;line-height:1.2;box-shadow:0 6px 16px rgba(0,0,0,.28);transition:all .25s ease;}
.ao-qp-ppl b{display:flex;align-items:baseline;gap:4px;font-size:22px;font-weight:800;white-space:nowrap;color:#2b211b;letter-spacing:.3px;}
.ao-qp-ppl small{font-size:13px;font-weight:700;color:#9a7230;}
.ao-qp-ppl em{display:inline-block;padding:3px 10px;border-radius:999px;background:#f1e6d2;font-style:normal;font-size:11.5px;font-weight:600;color:#7d5b27;white-space:nowrap;}
.ao-qp-ppl a:hover,.ao-qp-ppl a:focus-visible{border-color:#d6b468;transform:translateY(-2px);box-shadow:0 10px 22px rgba(0,0,0,.35),0 0 0 3px rgba(214,180,104,.35);}
.ao-qp-ppl a:hover em{background:#2b211b;color:#f0d39a;}

/* ===== 按系列 ===== */
.ao-qp-series{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;}
.ao-qp-series a{position:relative;display:flex;text-align:left;align-items:center;gap:14px;padding:13px 16px;border-radius:14px;border:1px solid rgba(214,180,104,.2);background:rgba(255,255,255,.035);color:#f6eddf !important;transition:all .25s ease;}
.ao-qp-series a:hover{border-color:#c9a45c;background:rgba(201,164,92,.1);}
.ao-qp-series i{flex:0 0 40px;height:40px;display:flex;align-items:center;justify-content:center;border-radius:12px;background:rgba(214,180,104,.16);font-style:normal;font-size:19px;}
.ao-qp-series a > span:not(.ao-qp-bats){display:flex;flex-direction:column;align-items:flex-start;min-width:0;text-align:left;}
.ao-qp-l2{display:inline;}
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
.ao-qp-series a.is-hw b{font-size:16px;}
.ao-qp-series a.is-hw em{padding:6px 14px;font-size:13.5px;letter-spacing:1px;background:linear-gradient(135deg,#ffb347,#ff5a00);color:#1c1426;box-shadow:0 0 0 2px rgba(255,179,71,.35),0 4px 14px rgba(255,90,0,.55);animation:aoQpGlow 1.8s ease-in-out infinite;}

.ao-qp-limit{align-self:flex-start;display:inline-block;margin:0 0 5px;padding:4px 12px;border-radius:999px;background:linear-gradient(135deg,#ffd23f 0%,#ff8a1f 55%,#ff5a00 100%);color:#1c1426;font-size:12.5px;font-weight:900;letter-spacing:1.5px;line-height:1.3;box-shadow:0 0 0 2px rgba(255,179,71,.35),0 4px 14px rgba(255,90,0,.55);animation:aoQpGlow 1.8s ease-in-out infinite;}
@keyframes aoQpGlow{0%,100%{box-shadow:0 0 0 2px rgba(255,179,71,.35),0 4px 14px rgba(255,90,0,.45);}50%{box-shadow:0 0 0 4px rgba(255,179,71,.55),0 4px 22px rgba(255,90,0,.85);}}
.ao-qp-series a.is-hw:hover{background:linear-gradient(135deg,#3a2850 0%,#22182e 100%);}


/* ===== Halloween 蝙蝠動畫（同 Pop up） ===== */
.ao-qp-bats{position:absolute;inset:0;z-index:0;overflow:hidden;border-radius:inherit;pointer-events:none;}
.ao-qp-bats i{position:absolute;top:50%;left:-12%;width:30px;margin-top:-7px;animation:aoQpBat 5s linear infinite;}
.ao-qp-bats i.b2{width:22px;margin-top:-14px;animation-duration:6s;animation-delay:1.6s;}
.ao-qp-bats i.b3{width:26px;margin-top:1px;animation-duration:5.5s;animation-delay:3.2s;}
.ao-qp-bats svg{display:block;width:100%;height:auto;transform-origin:50% 40%;animation:aoQpFlap .16s ease-in-out infinite alternate;}
.ao-qp-series a.is-hw .ao-qp-bats svg path{fill:#ff8a1f;}
.ao-qp-series a.is-hw .ao-qp-bats i{width:34px;}
.ao-qp-series a.is-hw .ao-qp-bats i.b2{width:26px;}
.ao-qp-series a.is-hw .ao-qp-bats i.b3{width:30px;}
.ao-qp-series a.is-hw > i,.ao-qp-series a.is-hw > span{position:relative;z-index:1;}
.ao-qp-series a.is-hw > em{z-index:2;}
.ao-qp-btn{position:relative;overflow:hidden;}
.ao-qp-btn > span{position:relative;z-index:1;}
.ao-qp-pop a.is-hw .ao-qp-btn::after{content:"";position:absolute;top:0;left:-60%;width:40%;height:100%;background:linear-gradient(100deg,rgba(255,255,255,0),rgba(255,255,255,.6),rgba(255,255,255,0));transform:skewX(-20deg);animation:aoQpShine 2.8s ease-in-out infinite;z-index:2;}
@keyframes aoQpBat{0%{left:-12%;transform:translateY(4px);}25%{transform:translateY(-6px);}50%{transform:translateY(5px);}75%{transform:translateY(-5px);}100%{left:108%;transform:translateY(3px);}}
@keyframes aoQpFlap{from{transform:scaleY(1);}to{transform:scaleY(.55) scaleX(.92);}}
@keyframes aoQpShine{0%{left:-60%;}55%,100%{left:130%;}}


/* ===== WhatsApp ===== */
.ao-qp-help{display:flex;align-items:center;justify-content:center;flex-wrap:wrap;gap:10px 18px;padding-top:22px;border-top:1px solid rgba(214,180,104,.22);}
.ao-qp-help p{margin:0 !important;font-size:15px;color:#cbbca6;}
.ao-qp-help a{display:inline-block;padding:13px 28px;border-radius:999px;background:linear-gradient(135deg,#e3c482,#b8893f);color:#1d150f !important;font-size:15px;font-weight:800;line-height:1.2;}
.ao-qp-help a:hover{filter:brightness(1.08);}
.ao-qp img.emoji{display:inline !important;width:1em !important;height:1em !important;margin:0 !important;vertical-align:-0.12em !important;}

.ao-qp-slider{position:relative;}
.ao-qp-nav{display:none;}
.ao-qp-dots{display:none;}
/* ≤1080px：TOP 5 變成可左右滑動 */
@media (max-width:1080px){
  .ao-qp-pop{display:flex;gap:12px;overflow-x:auto;overflow-y:hidden;scroll-snap-type:x proximity;-webkit-overflow-scrolling:touch;overscroll-behavior-x:contain;touch-action:pan-x pan-y;padding:6px 2px 10px;scrollbar-width:none;}
  .ao-qp-pop::-webkit-scrollbar{display:none;}
  .ao-qp-pop a{flex:0 0 31%;scroll-snap-align:start;}
  .ao-qp-nav{position:absolute;top:38%;z-index:5;display:flex;align-items:center;justify-content:center;width:38px;height:38px;padding:0;border:0;border-radius:50%;background:rgba(255,210,63,.95);color:#1d150f;font:inherit;font-size:24px;font-weight:900;line-height:1;cursor:pointer;box-shadow:0 6px 14px rgba(0,0,0,.4);transition:opacity .2s ease;}
  .ao-qp-prev{left:-8px;}
  .ao-qp-next{right:-8px;}
  .ao-qp-nav[disabled]{opacity:0;pointer-events:none;}
  .ao-qp-dots{display:flex;justify-content:center;gap:6px;margin-top:6px;}
  .ao-qp-dots i{width:7px;height:7px;border-radius:50%;background:rgba(255,255,255,.3);transition:all .2s ease;}
  .ao-qp-dots i.on{width:20px;border-radius:4px;background:#ffd23f;}
}
@media (max-width:960px){.ao-qp-ppl{grid-template-columns:repeat(3,minmax(0,1fr));}
  .ao-qp-series a.is-hot em{position:absolute;top:-10px;right:8px;margin:0;}
  .ao-qp-series a.is-hw b{font-size:15px;}
}
@media (max-width:640px){
  .ao-qp{padding:26px 14px 22px;border-radius:18px;}
  .ao-qp .ao-qp-title{font-size:23px;}
  .ao-qp-sub{font-size:14px;}
  .ao-qp-sec{margin-bottom:24px;}
  .ao-qp-sec--top{margin-top:36px;padding:30px 0 14px 12px;border-radius:16px;}
  .ao-qp-toptag,.ao-qp-tag{font-size:16px;padding:8px 16px;}
  .ao-qp-box{margin-top:36px;padding:30px 10px 14px;border-radius:16px;}
  .ao-qp-pop{gap:10px;padding:6px 2px 10px;}
  .ao-qp-pop a{flex:0 0 66%;}
  .ao-qp-nav{width:34px;height:34px;font-size:22px;}
  .ao-qp-prev{left:-6px;}
  .ao-qp-next{right:-2px;}
  .ao-qp-ppl{gap:8px;}
  .ao-qp-ppl a{min-height:70px;padding:9px 3px;gap:5px;border-radius:12px;}
  .ao-qp-ppl em{padding:2px 7px;}
  .ao-qp-ppl b{font-size:17px;}
  .ao-qp-ppl em{font-size:11px;}
  .ao-qp-series{gap:8px;}
  .ao-qp-series a{gap:9px;padding:10px 10px;}
  .ao-qp-series i{flex-basis:30px;height:30px;font-size:16px;border-radius:9px;}
  .ao-qp-series b{font-size:13px;}
  .ao-qp-series small{display:none;}
  .ao-qp-series em{position:absolute;top:-8px;right:6px;padding:2px 7px;font-size:10px;}
  .ao-qp-l2{display:block;}
  .ao-qp-limit{padding:3px 9px;font-size:11px;letter-spacing:1px;margin-bottom:4px;}
  .ao-qp-series a.is-hw b{font-size:13.5px;}
  .ao-qp-help{flex-direction:column;}
  .ao-qp-help a{width:100%;text-align:center;}
}
@media (prefers-reduced-motion:reduce){.ao-qp a,.ao-qp img{transition:none !important;}.ao-qp-bats{display:none;}.ao-qp-limit{animation:none !important;}.ao-qp-btn::after{animation:none !important;}}
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
