import urllib.parse, html, os
B='https://aoaodelivery.com'
U=B+'/wp-content/uploads/'
def dl(label): return f" onclick=\"window.dataLayer=window.dataLayer||[];dataLayer.push({{event:'cta_click',cta_label:'{label}'}});\""
PPL=[('2–6','小型聚會','2-6','qp_ppl_2_6'),('7–11','家庭派對','7-11','qp_ppl_7_11'),('12–16','生日派對','12-16','qp_ppl_12_16'),('18–25','公司／朋友聚餐','18-25','qp_ppl_18_25'),('30+','大型活動','30人以上','qp_ppl_30'),('100+','企業活動','100人以上','qp_ppl_100')]
def ppl_url(k):
    k = k if '以上' in k else k+'人'
    return B+'/product-category/party-set-by-people/'+k+'分享選項/'
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
POP=[(6130,'5人自選拼盤','自選拼盤・適合 5 人小聚',498,U+'2023/10/KitchenAO_platter_thumbnail_工作區域-1-600x600-1.png','/product/5-people-self-selected-platter/'),
(6242,'AO 8–10 人美食派對 Gourmet Set','8–10 人・熱食主菜',1988,U+'2026/03/8-10_101-X-KITCHENAO-03-03-03-600x600.jpg','/product/ao-8-10pax-gourmet-set/'),
(5359,'AO 12–16 人輕食宴會套餐 Refreshment','12–16 人・會議茶點',2688,U+'2023/11/refreshmentparty-03-600x600.jpg','/product/ao-12-16pax-refreshment-set/')]
WA='https://wa.me/85269011987?text='+urllib.parse.quote('你好，我已在 Kitchen AO 網站瀏覽過派對到會餐單，但仍未決定選擇哪一款，想查詢以下問題：')

def markup(theme, labels):
    l1,l2,l3=labels
    ppl=''.join(f'<a href="{ppl_url(k)}"{dl(t)}><b>{n}<small>人</small></b><em>{d}</em></a>' for n,d,k,t in PPL)
    ser=''.join(f'<a class="{"is-"+c if c else ""}" href="{B+u}"{dl(t)}><i>{e}</i><span><b>{n}</b><small>{s}</small></span>{f"<em>{bd}</em>" if bd else ""}</a>' for e,n,s,u,t,bd,c in SER)
    pop=''.join(f'<a href="{B+u}" data-pid="{pid}"{dl("qp_pop_"+str(pid))}><span class="ao-qp-ph"><img src="{img}" alt="{html.escape(n)}" width="600" height="600" loading="lazy" decoding="async"></span><span class="ao-qp-pi"><small>人氣推介</small><b>{n}</b><em>{d}</em><span class="ao-qp-pr"><strong data-price>HK${p:,}</strong><span>查看詳情 →</span></span></span></a>' for pid,n,d,p,img,u in POP)
    return f'''<section class="ao-qp ao-qp--{theme}" aria-labelledby="ao-qp-title-{theme}">
  <div class="ao-qp-head">
    <p class="ao-qp-eyebrow">Kitchen AO Party Catering</p>
    <h2 id="ao-qp-title-{theme}" class="ao-qp-title">快速選擇派對套餐</h2>
    <p class="ao-qp-sub">先按人數或系列選擇合適套餐，再直接網上下單。</p>
  </div>
  <div class="ao-qp-sec"><div class="ao-qp-lbl">{l1}按人數選擇</div><div class="ao-qp-ppl">{ppl}</div></div>
  <div class="ao-qp-sec"><div class="ao-qp-lbl">{l2}按系列選擇</div><div class="ao-qp-series">{ser}</div></div>
  <div class="ao-qp-sec"><div class="ao-qp-lbl">{l3}本週人氣推介</div><div class="ao-qp-pop">{pop}</div></div>
  <div class="ao-qp-help"><p>仍未決定選擇哪一款？</p><a href="{WA}" target="_blank" rel="noopener noreferrer"{dl('qp_whatsapp')}>WhatsApp 專人為你配搭餐單</a></div>
</section>'''

BASE='''.ao-qp{max-width:1180px;margin:16px auto 32px;font-family:inherit;}
.ao-qp *{box-sizing:border-box;}
.ao-qp a{text-decoration:none !important;}
.ao-qp-head{text-align:center;margin:0 0 26px;}
.ao-qp-eyebrow{margin:0 0 8px !important;font-size:11px;font-weight:700;letter-spacing:2px;line-height:1.3;text-transform:uppercase;}
.ao-qp .ao-qp-title{margin:0 0 6px !important;font-size:28px;font-weight:800;line-height:1.35;}
.ao-qp-sub{margin:0 !important;font-size:15px;line-height:1.7;}
.ao-qp-sec{margin:0 0 26px;}
.ao-qp-lbl{display:flex;align-items:center;gap:10px;margin:0 0 12px;font-size:14px;font-weight:800;letter-spacing:.5px;}
.ao-qp-lbl::after{content:"";flex:1;height:1px;}
.ao-qp-ppl{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:10px;}
.ao-qp-ppl a{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;min-height:76px;padding:12px 6px;text-align:center;line-height:1.2;transition:all .25s ease;}
.ao-qp-ppl b{display:flex;align-items:baseline;gap:3px;font-size:22px;font-weight:700;white-space:nowrap;}
.ao-qp-ppl small{font-size:12.5px;font-weight:700;}
.ao-qp-ppl em{font-style:normal;font-size:12px;}
.ao-qp-series{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;}
.ao-qp-series a{position:relative;display:flex;align-items:center;gap:14px;padding:13px 16px;transition:all .25s ease;}
.ao-qp-series i{flex:0 0 40px;height:40px;display:flex;align-items:center;justify-content:center;font-style:normal;font-size:19px;}
.ao-qp-series span{display:flex;flex-direction:column;min-width:0;}
.ao-qp-series b{font-size:15px;font-weight:700;line-height:1.35;}
.ao-qp-series small{margin-top:2px;font-size:12.5px;line-height:1.4;}
.ao-qp-series em{margin-left:auto;flex:0 0 auto;padding:3px 10px;font-style:normal;font-size:11px;font-weight:800;letter-spacing:.5px;white-space:nowrap;}
.ao-qp-pop{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;}
.ao-qp-pop a{display:flex;flex-direction:column;overflow:hidden;transition:all .25s ease;}
.ao-qp-ph{display:block;aspect-ratio:16/10;overflow:hidden;}
.ao-qp-ph img{display:block;width:100% !important;height:100% !important;object-fit:cover;transition:transform .5s ease;}
.ao-qp-pop a:hover .ao-qp-ph img{transform:scale(1.05);}
.ao-qp-pi{display:flex;flex-direction:column;flex:1;padding:14px 16px 16px;}
.ao-qp-pi small{font-size:11px;font-weight:800;letter-spacing:1px;}
.ao-qp-pi b{margin:4px 0 2px;font-size:16px;font-weight:700;line-height:1.4;}
.ao-qp-pi em{font-style:normal;font-size:13px;}
.ao-qp-pr{display:flex;align-items:center;justify-content:space-between;gap:8px;margin-top:auto;padding-top:12px;}
.ao-qp-pr strong{font-size:18px;font-weight:800;}
.ao-qp-pr span{font-size:13px;font-weight:700;white-space:nowrap;}
.ao-qp-help{display:flex;align-items:center;justify-content:center;flex-wrap:wrap;gap:10px 18px;padding-top:22px;}
.ao-qp-help p{margin:0 !important;font-size:15px;}
.ao-qp-help a{display:inline-block;padding:13px 28px;font-size:15px;font-weight:800;line-height:1.2;transition:all .25s ease;}
.ao-qp img.emoji{display:inline !important;width:1em !important;height:1em !important;margin:0 !important;vertical-align:-0.12em !important;}
@media (max-width:960px){
  .ao-qp-ppl{grid-template-columns:repeat(3,minmax(0,1fr));}
}
@media (max-width:640px){
  .ao-qp .ao-qp-title{font-size:23px;}
  .ao-qp-sub{font-size:14px;}
  .ao-qp-sec{margin-bottom:22px;}
  .ao-qp-ppl{gap:8px;}
  .ao-qp-ppl a{min-height:64px;padding:9px 4px;}
  .ao-qp-ppl b{font-size:18px;}
  .ao-qp-ppl em{font-size:11px;}
  .ao-qp-series{gap:8px;}
  .ao-qp-series a{gap:9px;padding:10px 10px;}
  .ao-qp-series i{flex-basis:30px;height:30px;font-size:16px;}
  .ao-qp-series b{font-size:13px;}
  .ao-qp-series small{display:none;}
  .ao-qp-series em{position:absolute;top:-8px;right:6px;padding:2px 7px;font-size:10px;}
  .ao-qp-pop{display:flex;gap:12px;overflow-x:auto;scroll-snap-type:x mandatory;margin:0 -4px;padding:2px 4px 8px;scrollbar-width:none;}
  .ao-qp-pop::-webkit-scrollbar{display:none;}
  .ao-qp-pop a{flex:0 0 74%;scroll-snap-align:start;}
  .ao-qp-help{flex-direction:column;}
  .ao-qp-help a{width:100%;text-align:center;}
}
@media (prefers-reduced-motion:reduce){.ao-qp a,.ao-qp img{transition:none !important;}}
'''

SERIF="'Noto Serif TC','Songti TC','Source Han Serif TC','PMingLiU',serif"
THEMES={
'a':('Option A｜Noir 黑金（深色奢華）',('','',''),f'''
.ao-qp--a{{padding:40px 36px 34px;border-radius:24px;background:radial-gradient(120% 140% at 0% 0%,#3a2a20 0%,#211812 55%,#15100c 100%);color:#efe5d6;box-shadow:inset 0 0 0 1px rgba(214,180,104,.25);}}
.ao-qp--a .ao-qp-eyebrow{{color:#c9a45c;}}
.ao-qp--a .ao-qp-title{{font-family:{SERIF};color:#f6eddf !important;letter-spacing:2px;}}
.ao-qp--a .ao-qp-sub{{color:#cbbca6;}}
.ao-qp--a .ao-qp-lbl{{color:#d9bd84;}}
.ao-qp--a .ao-qp-lbl::after{{background:linear-gradient(90deg,rgba(214,180,104,.5),rgba(214,180,104,0));}}
.ao-qp--a .ao-qp-ppl a{{border:1px solid rgba(214,180,104,.35);border-radius:14px;background:rgba(255,255,255,.03);color:#f6eddf !important;}}
.ao-qp--a .ao-qp-ppl b{{font-family:{SERIF};color:#f6eddf;}}
.ao-qp--a .ao-qp-ppl small{{color:#c9a45c;}}
.ao-qp--a .ao-qp-ppl em{{color:#a99880;}}
.ao-qp--a .ao-qp-ppl a:hover{{background:#c9a45c;border-color:#c9a45c;}}
.ao-qp--a .ao-qp-ppl a:hover b,.ao-qp--a .ao-qp-ppl a:hover small,.ao-qp--a .ao-qp-ppl a:hover em{{color:#1d150f;}}
.ao-qp--a .ao-qp-series a{{border-radius:14px;border:1px solid rgba(214,180,104,.2);background:rgba(255,255,255,.035);color:#f6eddf !important;}}
.ao-qp--a .ao-qp-series a:hover{{border-color:#c9a45c;background:rgba(201,164,92,.1);}}
.ao-qp--a .ao-qp-series i{{border-radius:50%;border:1px solid rgba(214,180,104,.4);}}
.ao-qp--a .ao-qp-series small{{color:#a99880;}}
.ao-qp--a .ao-qp-series em{{border-radius:999px;background:#c9a45c;color:#1d150f;}}
.ao-qp--a .ao-qp-series a.is-hw{{border-color:rgba(255,122,26,.55);background:linear-gradient(90deg,rgba(255,122,26,.16),rgba(255,122,26,.03));}}
.ao-qp--a .ao-qp-series a.is-hw em{{background:#ff7a1a;color:#1d150f;}}
.ao-qp--a .ao-qp-pop a{{border-radius:16px;border:1px solid rgba(214,180,104,.22);background:#1b140f;color:#f6eddf !important;}}
.ao-qp--a .ao-qp-pop a:hover{{border-color:#c9a45c;}}
.ao-qp--a .ao-qp-pi small{{color:#c9a45c;}}
.ao-qp--a .ao-qp-pi em{{color:#a99880;}}
.ao-qp--a .ao-qp-pr strong{{font-family:{SERIF};color:#e7c98b;}}
.ao-qp--a .ao-qp-pr span{{color:#cbbca6;}}
.ao-qp--a .ao-qp-help{{border-top:1px solid rgba(214,180,104,.22);}}
.ao-qp--a .ao-qp-help p{{color:#cbbca6;}}
.ao-qp--a .ao-qp-help a{{border-radius:999px;background:linear-gradient(135deg,#e3c482,#b8893f);color:#1d150f !important;}}
.ao-qp--a .ao-qp-help a:hover{{filter:brightness(1.08);}}
@media (max-width:640px){{.ao-qp--a{{padding:26px 14px 22px;border-radius:18px;}}}}
'''),
'b':('Option B｜Ivory 象牙（淺色雜誌風）',('<span>01</span>','<span>02</span>','<span>03</span>'),f'''
.ao-qp--b{{padding:44px 40px 36px;border-radius:4px;background:#faf6ef;color:#2b211b;border:1px solid #e9dfcf;box-shadow:0 1px 0 #fff inset,0 18px 40px rgba(60,40,20,.06);}}
.ao-qp--b .ao-qp-eyebrow{{color:#a07c3b;}}
.ao-qp--b .ao-qp-title{{font-family:{SERIF};color:#201814 !important;font-weight:700;letter-spacing:3px;}}
.ao-qp--b .ao-qp-title::after{{content:"";display:block;width:44px;height:2px;margin:14px auto 0;background:#b8955a;}}
.ao-qp--b .ao-qp-sub{{color:#6a5f58;}}
.ao-qp--b .ao-qp-lbl{{color:#201814;font-family:{SERIF};font-weight:700;font-size:16px;letter-spacing:1px;}}
.ao-qp--b .ao-qp-lbl span{{font-family:inherit;color:#b8955a;font-size:13px;letter-spacing:1px;}}
.ao-qp--b .ao-qp-lbl::after{{background:#e3d6c1;}}
.ao-qp--b .ao-qp-ppl a{{border-radius:2px;background:#fff;border:1px solid #e9dfcf;color:#201814 !important;}}
.ao-qp--b .ao-qp-ppl b{{font-family:{SERIF};}}
.ao-qp--b .ao-qp-ppl small{{color:#a07c3b;}}
.ao-qp--b .ao-qp-ppl em{{color:#8a7b6e;}}
.ao-qp--b .ao-qp-ppl a:hover{{border-color:#201814;background:#201814;}}
.ao-qp--b .ao-qp-ppl a:hover b,.ao-qp--b .ao-qp-ppl a:hover em{{color:#fff;}}
.ao-qp--b .ao-qp-ppl a:hover small{{color:#d9bd84;}}
.ao-qp--b .ao-qp-series{{gap:0 28px;}}
.ao-qp--b .ao-qp-series a{{padding:14px 4px;border-bottom:1px solid #e3d6c1;color:#201814 !important;}}
.ao-qp--b .ao-qp-series a::after{{content:"→";margin-left:auto;padding-left:8px;color:#b8955a;transition:transform .25s ease;}}
.ao-qp--b .ao-qp-series a:hover::after{{transform:translateX(4px);}}
.ao-qp--b .ao-qp-series a:hover b{{color:#a07c3b;}}
.ao-qp--b .ao-qp-series i{{border-radius:50%;background:#f1e8da;}}
.ao-qp--b .ao-qp-series small{{color:#8a7b6e;}}
.ao-qp--b .ao-qp-series em{{margin-left:10px;border:1px solid #b8955a;color:#a07c3b;border-radius:2px;}}
.ao-qp--b .ao-qp-series em + *{{}}
.ao-qp--b .ao-qp-series a.is-hw i{{background:#fde7d3;}}
.ao-qp--b .ao-qp-series a.is-hw em{{border-color:#e06a10;color:#e06a10;}}
.ao-qp--b .ao-qp-pop a{{background:#fff;border:1px solid #e9dfcf;color:#201814 !important;}}
.ao-qp--b .ao-qp-pop a:hover{{box-shadow:0 14px 30px rgba(60,40,20,.12);}}
.ao-qp--b .ao-qp-pi small{{color:#a07c3b;}}
.ao-qp--b .ao-qp-pi b{{font-family:{SERIF};}}
.ao-qp--b .ao-qp-pi em{{color:#8a7b6e;}}
.ao-qp--b .ao-qp-pr{{border-top:1px solid #efe6d8;margin-top:auto;}}
.ao-qp--b .ao-qp-pr strong{{font-family:{SERIF};color:#201814;}}
.ao-qp--b .ao-qp-pr span{{color:#a07c3b;}}
.ao-qp--b .ao-qp-help{{border-top:1px solid #e3d6c1;}}
.ao-qp--b .ao-qp-help p{{color:#6a5f58;font-family:{SERIF};}}
.ao-qp--b .ao-qp-help a{{border-radius:2px;background:#201814;color:#f6eddf !important;letter-spacing:1px;}}
.ao-qp--b .ao-qp-help a:hover{{background:#a07c3b;}}
@media (max-width:640px){{.ao-qp--b{{padding:28px 16px 24px;}}.ao-qp--b .ao-qp-series{{gap:0 14px;}}.ao-qp--b .ao-qp-series a{{padding:11px 2px;}}.ao-qp--b .ao-qp-series a::after{{display:none;}}.ao-qp--b .ao-qp-series em{{position:absolute;top:-9px;right:0;background:#faf6ef;}}.ao-qp--b .ao-qp-series a{{padding-top:13px;}}}}
'''),
'c':('Option C｜Sage 鼠尾草（柔和自然）',('<span>①</span>','<span>②</span>','<span>③</span>'),f'''
.ao-qp--c{{padding:0 0 30px;border-radius:26px;overflow:hidden;background:#f4f1ea;color:#2f2a22;box-shadow:0 20px 50px rgba(40,50,30,.08);}}
.ao-qp--c .ao-qp-head{{margin:0 0 28px;padding:40px 24px 34px;background:linear-gradient(160deg,#5b6b52 0%,#3f4c39 100%);color:#fff;}}
.ao-qp--c .ao-qp-eyebrow{{color:#d8e0c8;}}
.ao-qp--c .ao-qp-title{{font-family:{SERIF};color:#fff !important;letter-spacing:2px;}}
.ao-qp--c .ao-qp-sub{{color:#e4eadb;}}
.ao-qp--c .ao-qp-sec,.ao-qp--c .ao-qp-help{{margin-left:32px;margin-right:32px;}}
.ao-qp--c .ao-qp-lbl{{color:#3f4c39;}}
.ao-qp--c .ao-qp-lbl span{{display:inline-flex;align-items:center;justify-content:center;width:26px;height:26px;border-radius:50%;background:#3f4c39;color:#fff;font-size:12px;}}
.ao-qp--c .ao-qp-lbl::after{{background:#d9d4c6;}}
.ao-qp--c .ao-qp-ppl a{{border-radius:999px;min-height:70px;background:#fff;border:1px solid #e2ddd0;color:#2f2a22 !important;}}
.ao-qp--c .ao-qp-ppl small{{color:#5b6b52;}}
.ao-qp--c .ao-qp-ppl em{{color:#8b8576;}}
.ao-qp--c .ao-qp-ppl a:hover{{background:#3f4c39;border-color:#3f4c39;}}
.ao-qp--c .ao-qp-ppl a:hover b,.ao-qp--c .ao-qp-ppl a:hover em{{color:#fff;}}
.ao-qp--c .ao-qp-ppl a:hover small{{color:#d8e0c8;}}
.ao-qp--c .ao-qp-series a{{border-radius:16px;background:#fff;border:1px solid #e8e3d6;color:#2f2a22 !important;}}
.ao-qp--c .ao-qp-series a:hover{{border-color:#5b6b52;transform:translateY(-2px);box-shadow:0 10px 22px rgba(40,50,30,.08);}}
.ao-qp--c .ao-qp-series i{{border-radius:12px;background:#eef0e6;}}
.ao-qp--c .ao-qp-series small{{color:#8b8576;}}
.ao-qp--c .ao-qp-series em{{border-radius:999px;background:#5b6b52;color:#fff;}}
.ao-qp--c .ao-qp-series a.is-hot{{background:#fbf6ea;border-color:#d8c49a;}}
.ao-qp--c .ao-qp-series a.is-hot em{{background:#b08a3e;}}
.ao-qp--c .ao-qp-series a.is-hw{{background:#fff4ea;border-color:#f3c79e;}}
.ao-qp--c .ao-qp-series a.is-hw i{{background:#ffe3cc;}}
.ao-qp--c .ao-qp-series a.is-hw em{{background:#e8711c;}}
.ao-qp--c .ao-qp-pop a{{border-radius:20px;background:#fff;border:1px solid #e8e3d6;color:#2f2a22 !important;}}
.ao-qp--c .ao-qp-pop a:hover{{box-shadow:0 16px 34px rgba(40,50,30,.12);transform:translateY(-3px);}}
.ao-qp--c .ao-qp-pi small{{color:#5b6b52;}}
.ao-qp--c .ao-qp-pi em{{color:#8b8576;}}
.ao-qp--c .ao-qp-pr strong{{color:#3f4c39;}}
.ao-qp--c .ao-qp-pr span{{color:#5b6b52;}}
.ao-qp--c .ao-qp-help{{border-top:1px dashed #cfc9b9;}}
.ao-qp--c .ao-qp-help p{{color:#5f594c;}}
.ao-qp--c .ao-qp-help a{{border-radius:999px;background:#25d366;color:#fff !important;box-shadow:0 8px 18px rgba(37,211,102,.28);}}
.ao-qp--c .ao-qp-help a:hover{{background:#1ebe5b;}}
@media (max-width:640px){{.ao-qp--c{{border-radius:20px;}}.ao-qp--c .ao-qp-head{{padding:28px 16px 24px;margin-bottom:22px;}}.ao-qp--c .ao-qp-sec,.ao-qp--c .ao-qp-help{{margin-left:14px;margin-right:14px;}}.ao-qp--c .ao-qp-ppl a{{border-radius:16px;}}}}
''')}

JS='''<script>
(function(){
  /* 自動更新「本週人氣推介」價錢（讀取 WooCommerce 現價；失敗則保留原價） */
  var box=document.currentScript&&document.currentScript.previousElementSibling;
  if(!box||!window.fetch)return;
  var cards=box.querySelectorAll('[data-pid]');var ids=[].map.call(cards,function(a){return a.getAttribute('data-pid')}).join(',');
  fetch('/wp-json/wc/store/v1/products?include='+ids).then(function(r){return r.json()}).then(function(list){
    list.forEach(function(p){var a=box.querySelector('[data-pid="'+p.id+'"] [data-price]');if(!a||!p.prices)return;var m=Math.pow(10,p.prices.currency_minor_unit||0);a.textContent='HK$'+Math.round(p.prices.price/m).toLocaleString('en-US');});
  }).catch(function(){});
})();
</script>'''

for k,(name,labels,css) in THEMES.items():
    code=f'<!-- ===== Kitchen AO｜/product-category/party/ 快速選擇派對套餐｜{name}（Raw HTML）===== -->\n'+markup(k,labels)+'\n'+JS+'\n<style>\n'+BASE+css+'</style>\n'
    open(f'option-{k}.html','w',encoding='utf-8').write(code)
    print(k,len(code))
