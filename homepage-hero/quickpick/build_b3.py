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
extra='''
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
  .ao-qp{padding:0 14px 22px;border-radius:16px;}
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
