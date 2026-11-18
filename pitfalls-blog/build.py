# -*- coding: utf-8 -*-
# 香港到會避伏指南 2026｜/blog/catering-pitfalls-guide/ 改版
import json, html, pathlib
HERE = pathlib.Path(__file__).parent
U = 'https://aoaodelivery.com'
IMG_KV = U + '/wp-content/uploads/2026/11/catering-pitfalls-guide-2026.jpg'
IMG_CMP = U + '/wp-content/uploads/2025/04/ChatGPT-Image-2025%E5%B9%B44%E6%9C%888%E6%97%A5-%E4%B8%8B%E5%8D%8804_06_04.png'

CSS = r'''
.ao-pf{--k:#141414;--g:#C8A24A;--iv:#F7F5F0;--ln:#E6DFD0;--mu:#6b645c;color:#222;font-size:18px;line-height:1.85}
.ao-pf *{box-sizing:border-box}
.ao-pf p{margin:0 0 16px}
.ao-pf a{color:#141414;text-decoration:underline;text-decoration-color:#C8A24A;text-underline-offset:3px}
.ao-pf h2{position:relative;padding:16px 0 0;margin:46px 0 16px;font-size:26px;line-height:1.4;font-weight:900;color:#141414;border:0}
.ao-pf h2:before{content:"";position:absolute;left:0;top:0;width:46px;height:4px;border-radius:3px;background:#C8A24A}
.ao-pf h3{font-size:20px;line-height:1.45;margin:0 0 8px;color:#141414;font-weight:800}
.ao-pf .eb{display:block;font-size:11.5px;letter-spacing:.28em;color:#9A7B2E;font-weight:700;text-transform:uppercase;margin:0 0 6px}
.ao-pf img{display:block;max-width:100%;height:auto;border-radius:6px}
.ao-pf figure{margin:20px 0}
.ao-pf figcaption{font-size:13px;color:var(--mu);margin-top:8px;text-align:center}

/* 開場：黑底置中 */
.ao-pf .op{background:#141414;color:#EDE6D8;text-align:center;padding:34px 26px 30px;border-radius:6px;margin:0 0 22px}
.ao-pf .op .eb{color:#C8A24A}
.ao-pf .op p{margin:0 auto;max-width:620px;font-size:17px;line-height:1.9}
.ao-pf .op b{color:#E4C77E}

/* 30 秒重點 */
.ao-pf .key{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:0 0 24px}
.ao-pf .key div{background:var(--iv);padding:18px 16px;border-radius:6px;text-align:center}
.ao-pf .key i{display:flex;align-items:center;justify-content:center;width:44px;height:44px;margin:0 auto 10px;border-radius:50%;border:1.5px solid #C8A24A;font-style:normal;font-weight:800;color:#9A7B2E;font-size:15px}
.ao-pf .key b{display:block;font-size:16.5px;color:#141414;margin-bottom:4px}
.ao-pf .key span{font-size:14px;color:var(--mu);line-height:1.7;display:block}

/* 目錄 */
.ao-pf .toc{border-top:1px solid var(--ln);border-bottom:1px solid var(--ln);padding:16px 0;margin:0 0 10px}
.ao-pf .toc ol{margin:6px 0 0;padding-left:1.4em;columns:2;column-gap:30px}
.ao-pf .toc li{margin:4px 0;font-size:15.5px;break-inside:avoid}
.ao-pf .toc a{text-decoration:none}

/* 陷阱卡 */
.ao-pf .pit{background:var(--iv);border-radius:6px;padding:24px 24px 18px;margin:0 0 16px;display:grid;grid-template-columns:62px 1fr;gap:4px 18px}
.ao-pf .pit .no{grid-row:1/span 3;width:56px;height:56px;border-radius:50%;background:#141414;color:#E4C77E;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:19px;letter-spacing:.02em}
.ao-pf .pit p{margin:0 0 10px;font-size:16.5px}
.ao-pf .pit .why{font-size:15.5px;color:#4a443d}
.ao-pf .pit .why b{color:#141414}
.ao-pf .pit .do{background:#fff;border-radius:6px;padding:12px 16px;margin:4px 0 6px}
.ao-pf .pit .do em{display:block;font-style:normal;font-size:11.5px;letter-spacing:.2em;color:#9A7B2E;font-weight:800;margin-bottom:4px}
.ao-pf .pit .do ul{margin:0;padding:0;list-style:none}
.ao-pf .pit .do li{position:relative;padding-left:22px;margin:4px 0;font-size:15.5px;line-height:1.7}
.ao-pf .pit .do li:before{content:"✓";position:absolute;left:0;top:0;color:#C8A24A;font-weight:900}

/* 表格 */
.ao-pf .tw{overflow-x:auto;-webkit-overflow-scrolling:touch;margin:14px 0 8px;border:1px solid var(--ln);border-radius:6px}
.ao-pf table{border-collapse:collapse;width:100%;min-width:600px;font-size:15px;background:#fff;margin:0}
.ao-pf th{background:#141414;color:#E4C77E;font-weight:700;text-align:left;padding:11px 14px;white-space:nowrap;border:0}
.ao-pf td{padding:11px 14px;border:0;border-top:1px solid #EEE8DC;vertical-align:top;line-height:1.65}
.ao-pf tr:nth-child(even) td{background:#FBFAF6}
.ao-pf td:first-child{font-weight:700;color:#141414;white-space:nowrap}
.ao-pf .cap{font-size:13px;color:var(--mu);margin:0 0 20px}

/* 秘訣格 */
.ao-pf .tips{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;margin:16px 0}
.ao-pf .tips div{border-top:2px solid #141414;padding:14px 2px 0}
.ao-pf .tips small{display:block;font-size:11.5px;letter-spacing:.24em;color:#9A7B2E;font-weight:800}
.ao-pf .tips b{display:block;font-size:17px;color:#141414;margin:4px 0 6px}
.ao-pf .tips p{font-size:15.5px;margin:0;color:#4a443d;line-height:1.75}

/* 檢查清單：虛線框＋頂部標籤 */
.ao-pf .chk{position:relative;border:2px dashed #C8A24A;border-radius:8px;padding:30px 22px 16px;margin:28px 0 10px;background:#fff}
.ao-pf .chk .lb{position:absolute;top:-14px;left:50%;transform:translateX(-50%);background:#141414;color:#E4C77E;font-size:13px;font-weight:800;letter-spacing:.16em;padding:5px 16px;border-radius:20px;white-space:nowrap}
.ao-pf .chk ol{list-style:none;margin:0;padding:0;counter-reset:q}
.ao-pf .chk li{counter-increment:q;border-bottom:1px solid #F0EADF;margin:0}
.ao-pf .chk li:last-child{border-bottom:0}
.ao-pf .chk label{display:flex;gap:12px;align-items:flex-start;padding:11px 2px;cursor:pointer;font-size:16px;line-height:1.65}
.ao-pf .chk input{flex:0 0 20px;width:20px;height:20px;margin:3px 0 0;accent-color:#141414;cursor:pointer}
.ao-pf .chk label b{color:#141414}
.ao-pf .chk label span{display:block;font-size:14px;color:var(--mu)}
.ao-pf .chk input:checked+div{opacity:.5;text-decoration:line-through;text-decoration-color:#C8A24A}
.ao-pf .chk .ct{text-align:center;font-size:13.5px;color:var(--mu);margin:10px 0 0}
.ao-pf .chk .ct b{color:#141414}

/* Kitchen AO 做法：黑底 */
.ao-pf .ours{background:#141414;color:#EDE6D8;border-radius:6px;padding:30px 26px;margin:20px 0}
.ao-pf .ours .eb{color:#C8A24A}
.ao-pf .ours h3{color:#fff;font-size:22px;margin:0 0 14px}
.ao-pf .ours ul{list-style:none;margin:0 0 20px;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:10px 22px}
.ao-pf .ours li{position:relative;padding-left:22px;font-size:15.5px;line-height:1.7}
.ao-pf .ours li:before{content:"✓";position:absolute;left:0;color:#C8A24A;font-weight:900}
.ao-pf .ours li b{color:#E4C77E}
.ao-pf .ours .bt{display:flex;flex-wrap:wrap;gap:10px}
.ao-pf .ours .bt a{display:inline-flex;align-items:center;justify-content:center;min-height:48px;padding:0 22px;border-radius:40px;font-weight:800;font-size:15px;text-decoration:none;letter-spacing:.04em}
.ao-pf .ours .bt a.g{background:#C8A24A;color:#141414}
.ao-pf .ours .bt a.o{border:1.5px solid #EDE6D8;color:#EDE6D8}
.ao-pf .ours .bt a:hover{opacity:.88}

/* 延伸閱讀 */
.ao-pf .rel{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:14px 0}
.ao-pf .rel a{display:block;background:var(--iv);border-radius:6px;padding:16px;text-decoration:none;font-weight:700;font-size:15.5px;line-height:1.55;color:#141414}
.ao-pf .rel a small{display:block;font-weight:600;color:#9A7B2E;font-size:11.5px;letter-spacing:.2em;margin-bottom:6px}
.ao-pf .rel a:hover{background:#EFEADF}

/* FAQ */
.ao-pf .faq details{border-bottom:1px solid var(--ln);padding:0}
.ao-pf .faq details:first-child{border-top:1px solid var(--ln)}
.ao-pf .faq summary{cursor:pointer;list-style:none;padding:15px 34px 15px 0;font-weight:800;font-size:16.5px;color:#141414;position:relative;line-height:1.6}
.ao-pf .faq summary::-webkit-details-marker{display:none}
.ao-pf .faq summary:after{content:"+";position:absolute;right:4px;top:12px;font-size:22px;color:#C8A24A;font-weight:400}
.ao-pf .faq details[open] summary:after{content:"−"}
.ao-pf .faq details>div{padding:0 0 16px;font-size:16px;color:#3b3631}
.ao-pf .faq details>div p{margin:0}

/* 編輯總結 */
.ao-pf .sum{background:var(--iv);border-radius:6px;padding:22px 24px;margin:16px 0 8px}
.ao-pf .sum p:last-child{margin:0}


/* 兩欄版面 */
.ao-pf{max-width:none;margin:0}
.ao-pf .lay{display:grid;grid-template-columns:minmax(0,1fr) 320px;gap:56px;align-items:start;padding:10px 0 40px}
.ao-pf .mn,.ao-pf .sd{min-width:0}
.ao-pf{overflow-wrap:anywhere}
.ao-pf .mob{display:none}
.ao-pf .stk{position:sticky;top:20px;display:flex;flex-direction:column;gap:14px}
.ao-pf .sb{background:#fff;border:1px solid var(--ln);border-radius:8px;padding:16px 18px;font-size:14.5px;line-height:1.7}
.ao-pf .sb-h{font-size:11.5px;font-weight:800;letter-spacing:.26em;color:#9A7B2E;margin:0 0 10px}
.ao-pf .sb-meta{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;text-align:center;font-size:13px;color:#4a443d}
.ao-pf .sb-meta b{display:block;font-size:11px;letter-spacing:.2em;color:#9A7B2E;font-weight:800}
.ao-pf .sb-toc{list-style:none;margin:0;padding:0}
.ao-pf .sb-toc li{margin:0}
.ao-pf .sb-toc a{display:flex;gap:10px;align-items:baseline;padding:7px 0;border-top:1px dashed var(--ln);text-decoration:none;color:#3f3a33;font-size:14.5px}
.ao-pf .sb-toc li:first-child a{border-top:0}
.ao-pf .sb-toc i{font-style:normal;font-size:11.5px;font-weight:800;color:#C8A24A;width:20px;flex:0 0 20px}
.ao-pf .sb-toc a.on{color:#141414;font-weight:800}
.ao-pf .sb-key{list-style:none;margin:0;padding:0;counter-reset:k}
.ao-pf .sb-key li{counter-increment:k;position:relative;padding:8px 0 8px 40px;border-top:1px dashed var(--ln);color:#4a443d;font-size:13.5px}
.ao-pf .sb-key li:first-child{border-top:0}
.ao-pf .sb-key li:before{content:"0" counter(k);position:absolute;left:0;top:9px;width:28px;height:28px;border-radius:50%;border:1.5px solid #C8A24A;color:#9A7B2E;font-size:11px;font-weight:800;display:flex;align-items:center;justify-content:center}
.ao-pf .sb-key b{display:block;color:#141414;font-size:14.5px}
.ao-pf .sb-dk{background:#141414;border-color:#141414;color:#EDE6D8}
.ao-pf .sb-dk .sb-h{color:#C8A24A}
.ao-pf .sb-dk p{margin:0;padding:6px 0;border-top:1px solid #2c2a26;display:flex;justify-content:space-between;gap:10px;font-size:13.5px}
.ao-pf .sb-dk .sb-h+p{border-top:0}
.ao-pf .sb-dk p b{color:#E4C77E;font-size:15px}
.ao-pf .sb-dk a{display:block;margin-top:10px;color:#E4C77E;text-decoration:none;font-weight:700;font-size:13.5px}
.ao-pf .sb-wa{background:var(--iv);border-color:var(--iv);color:#4a443d;font-size:13.5px}
.ao-pf .sb-wa b{display:block;color:#141414;font-size:15.5px;margin-bottom:4px}
.ao-pf .sb-wa a{display:flex;align-items:center;justify-content:center;margin-top:12px;min-height:44px;border-radius:40px;background:#141414;color:#E4C77E;text-decoration:none;font-weight:800;font-size:14px;letter-spacing:.06em}
@media(max-width:1024px){
 .ao-pf .lay{grid-template-columns:minmax(0,1fr);gap:30px}
 .ao-pf .mob{display:block}
 .ao-pf .key.mob{display:grid}
 .ao-pf .stk{position:static}
 .ao-pf .sd .sb:nth-child(2),.ao-pf .sd .sb:nth-child(3){display:none}
}
@media(max-width:767px){
 .ao-pf{font-size:16px;line-height:1.8}
 .ao-pf h2{font-size:21.5px;margin:36px 0 12px}
 .ao-pf h3{font-size:18px}
 .ao-pf .op{padding:26px 18px 22px}
 .ao-pf .op p{font-size:16px}
 .ao-pf .key{grid-template-columns:1fr;gap:8px}
 .ao-pf .key div{display:grid;grid-template-columns:44px 1fr;gap:0 12px;text-align:left;align-items:center;padding:14px}
 .ao-pf .key i{grid-row:1/span 2;margin:0}
 .ao-pf .toc ol{columns:1}
 .ao-pf .pit{grid-template-columns:1fr;padding:20px 16px 14px}
 .ao-pf .pit .no{grid-row:auto;width:46px;height:46px;font-size:16px;margin-bottom:8px}
 .ao-pf .tips{grid-template-columns:1fr}
 .ao-pf .chk{padding:28px 14px 12px}
 .ao-pf .ours{padding:24px 18px}
 .ao-pf .ours ul{grid-template-columns:1fr}
 .ao-pf .ours .bt a{flex:1 1 100%}
 .ao-pf .rel{grid-template-columns:1fr}
 .ao-pf .tw{border:0;overflow:visible}
 .ao-pf table,.ao-pf tbody,.ao-pf tr,.ao-pf td{display:block;min-width:0;width:auto}
 .ao-pf thead{display:none}
 .ao-pf tr{background:var(--iv);border-radius:8px;padding:12px 14px;margin:0 0 10px}
 .ao-pf tr:nth-child(even) td,.ao-pf td{background:none;border:0;padding:3px 0}
 .ao-pf td:first-child{font-size:16.5px;padding-bottom:6px;margin-bottom:4px;border-bottom:1px solid var(--ln);white-space:normal}
 .ao-pf td:not(:first-child){display:grid;grid-template-columns:76px 1fr;gap:8px;font-size:15px}
 .ao-pf td:not(:first-child):before{content:attr(data-l);font-size:12px;font-weight:800;color:#9A7B2E;letter-spacing:.06em;padding-top:2px}
 .ao-pf .sb-meta{grid-template-columns:repeat(3,1fr)}
 .ao-pf .chk .lb{font-size:12px;letter-spacing:.1em}
}
@media(max-width:380px){
 .ao-pf .pit{padding:18px 14px 12px}
 .ao-pf .op{padding:22px 14px 18px}
 .ao-pf .chk label{gap:10px;font-size:15px}
}
'''

PITS = [
 ('01', 'pitfall-1', '照騙陷阱：食物貨不對辦',
  '餐單相片精緻吸引，送到現場卻是另一回事：擺盤簡化、配料減少，甚至食材被替換。這是香港到會最常見的投訴之一。',
  [('過度修圖', '宣傳照經大量後期處理，與實際出品有明顯落差。'),
   ('食材降級', '為控制成本，以次一級食材代替，例如以蟹柳代替蟹肉。'),
   ('擺盤誤導', '相片以特別角度或器皿拍攝，令份量看來比實際多。')],
  ['要求提供近期真實活動相片，而非只看宣傳圖。', '問清主要食材的來源及規格，並寫進訂單。', '根據《商品說明條例》，商戶的商品說明（包括圖片）須準確，如有嚴重不符可保留證據追究。']),
 ('02', 'pitfall-2', '份量不足：賓客未吃飽食物已清空',
  '活動進行到一半，食物已經清空，是主人家最尷尬的情況。到會份量縮水，往往源於雙方對「一人份量」的理解不同。',
  [('標準模糊', '餐單只寫「適合 10 人」，沒有列明每款食物的件數或重量。'),
   ('壓價競爭', '低價背後，可能是在份量上削減成本。'),
   ('未計活動性質', '雞尾酒會、正餐及會議茶點所需份量相差甚大。')],
  ['要求列明每款食物的件數、重量或盤數。', '落單時說明活動類型、時長及賓客組合（例如青少年食量較大）。', '參考下文「到會份量參考表」，按活動預留適量餘裕。']),
 ('03', 'pitfall-3', '送貨遲到：活動流程被打亂',
  '約好 7 時開餐，8 時食物仍未送到。到會遲到對公司活動及船河影響最大，船隻開航不會等人，延誤更可能影響食物溫度及質素。',
  [('排單過密', '同一時段接單過多，人手及車輛不足。'),
   ('欠缺緩衝', '沒有預留交通及上落貨時間。'),
   ('地址資料不全', '未提供樓層、入口或泊車安排，送貨員到場後再找路。')],
  ['確認送貨時段及準時率，船河及公司活動可考慮指定送達時間。', '問清遲到的處理及補償安排，並以書面確認。', '提供完整地址、樓層、聯絡人及電話，並預早通知管理處。']),
 ('04', 'pitfall-4', '隱藏收費：結帳時才發現多了三成',
  '報價總數看來划算，結帳時才加上運費、樓梯費、指定時間附加費、保溫爐租金等。到會隱藏收費是最容易被忽略的陷阱。',
  [('運費另議', '報價單只寫「運費另計」，沒有實際金額。'),
   ('附加條款', '偏遠地區、無升降機、標準時段以外送貨，均可能另收費用。'),
   ('用品另租', '保溫爐、餐具、枱布等未包括在套餐內。')],
  ['要求一份列明所有項目的到會報價單。', '對照下文「隱藏收費對照表」逐項確認。', '確認價錢是否已包括餐具及基本用品。']),
 ('05', 'pitfall-5', '服務欠佳：溝通困難，出事無人負責',
  '食物再好，如果落單時溝通困難、送貨時態度欠佳，或出現問題時投訴無門，整體體驗同樣大打折扣。',
  [('溝通不清', '查詢時回覆慢、答非所問。'),
   ('交收馬虎', '食物隨意擺放，沒有基本擺設。'),
   ('售後推卸', '食物有問題時，商戶拒絕處理或推卸責任。')],
  ['留意查詢時的回覆速度及專業程度。', '以 WhatsApp 或電郵溝通，保留所有紀錄。', '如遇嚴重糾紛，可保留單據及相片，向消費者委員會查詢或投訴。']),
]

PORTION = [
 ('雞尾酒會／開幕酒會', '2 小時', '每人約 8 至 12 件小食', '以一口小食為主，時間越長件數越多'),
 ('派對正餐（生日會、聚會）', '3 小時', '主菜、飯麵、小食及甜品各一份', '青少年或男士較多時建議加一成份量'),
 ('會議茶點', '1 小時', '每人約 4 至 6 件', '以小食及甜品為主，可配咖啡或茶'),
 ('公司午餐', '1 小時', '每人一份餐盒或正餐份量', '餐盒方便分發，亦較易控制份量'),
 ('船河', '6 至 8 小時', '正餐份量再加約兩成小食', '活動時間長，宜加小食及飲品'),
]

FEES = [
 ('運費', '按地區收費；偏遠地區或離島另計', '送到我的地址運費是多少？有沒有免運費門檻？'),
 ('上樓／樓梯費', '標準運費一般只包括送到樓下', '是否送到單位門口？唐樓無升降機如何收費？'),
 ('指定時間附加費', '指定準確送達時間，或標準時段以外送貨', '標準派送時段是甚麼？指定時間要另付多少？'),
 ('保溫爐', '大部分套餐不包括，需另租', '熱食如何保溫？保溫爐如何收費及回收？'),
 ('餐具及用品', '紙碟、餐具、枱布、食物夾', '套餐包括甚麼餐具？數量是否足夠？'),
 ('節日附加費', '平安夜、聖誕、新年等熱門日子', '節日是否加價？截單日期是何時？'),
 ('改期及取消', '惡劣天氣或臨時改期', '八號風球或黑雨如何處理？取消可否退款？'),
]

TIPS = [
 ('TIP 01', '網上搜尋真實評價', '查看 Google 商家評分、社交平台留言及客人相片。多看負評內容，以及商戶如何回應；評價一面倒或用字空泛的，要有保留。'),
 ('TIP 02', '查詢報價要問得夠詳細', '叫到會包甚麼？份量基準、餐具、送貨方式、額外收費，都要逐項問清楚，並要求書面到會報價單。'),
 ('TIP 03', '參考近期真實案例', '要求提供近一兩個月內同類活動的現場相片；大型活動或婚宴可查詢試食安排。'),
 ('TIP 04', '確認牌照及經營往績', '可在食物環境衞生署網站查閱持牌食物業處所資料，並了解商戶主要承辦的活動類型。'),
 ('TIP 05', '所有細節白紙黑字', '餐單、份量、價錢、送貨時間、改期及取消條款，都要以電郵或 WhatsApp 確認，並保留付款紀錄。'),
]

CHECK = [
 ('每款食物的份量基準是甚麼？', '件數、重量或盤數'),
 ('相片是否真實出品？可否提供近期活動相？', '避免照騙'),
 ('主要食材的來源及規格？', '例如牛肉部位、海鮮種類'),
 ('價錢包括甚麼？', '餐具、紙碟、食物夾、保溫用品'),
 ('送到我的地址運費多少？有否免運費門檻？', '連同樓層及有否升降機'),
 ('是否送到單位門口？', '樓梯費、上樓費'),
 ('標準送貨時段及準時安排？', '指定送達時間是否另收費'),
 ('熱食如何保溫？', '保溫包裝或保溫爐'),
 ('惡劣天氣、改期及取消如何處理？', '八號風球、黑雨'),
 ('食物有問題時如何跟進？', '聯絡方法及處理時間'),
]

FAQ = [
 ('如何避免到會中伏？',
  '落單前做好三件事：要求查看近期真實活動相片、按活動類型計算份量、逐項確認運費及附加費。所有細節以電郵或 WhatsApp 書面確認，並保留付款紀錄，便可避開大部分到會陷阱。'),
 ('叫到會一般包括甚麼？保溫爐需要另租嗎？',
  '視乎套餐而定，一般包括食物及基本盛載器皿，餐具、紙碟及食物夾則未必包括。大部分標準到會套餐不包括保溫爐，如活動時間較長或想熱食保持溫度，需另外租用，落單前應問清楚收費及回收安排。'),
 ('一份清楚的到會報價單應列明甚麼？',
  '應列明餐單內容、每款份量、單價及總額、運費、指定時間或上樓等附加費、餐具及用品、送貨日期時間，以及改期和取消條款。只寫「運費另議」或「另加附加費」而沒有金額的報價單，應先追問清楚。'),
 ('到會份量應如何計算？',
  '按活動類型及時長計算。雞尾酒會一般每人約 8 至 12 件小食，會議茶點每人約 4 至 6 件；派對正餐則以主菜、飯麵、小食及甜品配搭。青少年或男士較多、活動時間較長時，建議預留約一成餘裕。'),
 ('唐樓無升降機或偏遠地區，到會運費會否較貴？',
  '一般會。標準運費多數只包括送到樓下或車輛可停泊的位置，唐樓樓梯費及偏遠地區附加費十分常見。落單時應提供完整地址、樓層及有否升降機，先確認實際收費。'),
 ('八號風球或黑雨時，已訂的到會如何處理？',
  '各商戶安排不同，應在落單前確認。以 Kitchen AO 為例，如於送貨時間前四小時內懸掛黑色暴雨警告或八號風球，可免費改期，並須於 60 日內重新安排派送（公眾假期及前夕除外）。'),
 ('到會食物貨不對辦，可以怎樣處理？',
  '先拍照存證，並立即聯絡到會公司要求跟進，同時保留訂單、付款及溝通紀錄。如商戶未能合理處理，可向消費者委員會查詢或投訴。'),
 ('如何查詢到會公司是否持有食環署牌照？',
  '可在食物環境衞生署網站查閱持牌食物業處所資料，以公司名稱或地址搜尋。正規商戶一般亦可提供牌照號碼供客人核實。'),
]

REL = [
 ('公司活動', '香港公司活動到會攻略 2026', U + '/blog/company-event-catering-guide/'),
 ('船河', '船P必備清單 2026｜船河食物及飲品懶人包', U + '/blog/boat-party-catering-guide/'),
 ('素食', '派對有素食朋友點安排？素食到會揀選全攻略', U + '/blog/vegetarian-catering-hong-kong/'),
]

def e(s): return html.escape(s, quote=False)

def aside(toc):
    t = ''.join(f'<li><a href="#{a}"><i>{k+1:02d}</i>{n}</a></li>' for k, (a, n) in enumerate(toc))
    return ('<aside class="sd"><div class="stk">'
            '<div class="sb sb-meta"><div><b>作者</b>Kitchen AO 編輯部</div><div><b>更新</b>2026-11-18</div><div><b>閱讀</b>約 8 分鐘</div></div>'
            '<div class="sb"><p class="sb-h">目錄</p><ol class="sb-toc">' + t + '</ol></div>'
            '<div class="sb"><p class="sb-h">30 秒重點</p><ol class="sb-key">'
            '<li><b>看真實相片</b>要求近期活動相，避開照騙</li>'
            '<li><b>算清份量</b>按活動類型及時長計算</li>'
            '<li><b>問清收費</b>運費、樓梯費、附加費逐項確認</li></ol></div>'
            '<div class="sb sb-dk"><p class="sb-h">Kitchen AO 收費一覽</p>'
            '<p><b>HK$1,450</b>全港免運費</p><p><b>HK$700</b>九龍指定區域免運費</p><p><b>11:00–20:30</b>標準派送時段</p>'
            '<a href="' + U + '/delivery/">查看各區運費 →</a></div>'
            '<div class="sb sb-wa"><b>籌備活動想問清楚？</b>告訴我們日期、人數及預算，客服為你配搭餐單及確認收費。'
            '<a href="https://wa.me/85269011987?text=%E4%BD%A0%E5%A5%BD%EF%BC%8C%E6%88%91%E6%83%B3%E6%9F%A5%E8%A9%A2%E5%88%B0%E6%9C%83%E9%A4%90%E5%96%AE%E5%8F%8A%E5%A0%B1%E5%83%B9%E3%80%82" target="_blank" rel="noopener">WhatsApp 查詢</a></div>'
            '</div></aside>')

def build():
    h = []
    h.append('<div class="ao-pf">')
    h.append('<style>' + CSS + '</style>')
    # 開場
    h.append((HERE / 'kv-ed-a.html').read_text(encoding='utf-8'))
    h.append('<p>這份 2026 年版<strong>香港到會避伏指南</strong>，由 Kitchen AO 編輯部整理，拆解五個最常見的<strong>到會中伏</strong>位，附份量參考表、隱藏收費對照表，以及落單前必問的 10 條問題，教你如何選擇最穩妥的到會公司。</p>')
    h.append('<div class="key">'
             '<div><i>01</i><b>看真實相片</b><span>要求近期活動相，避開照騙</span></div>'
             '<div><i>02</i><b>算清份量</b><span>按活動類型及時長計算</span></div>'
             '<div><i>03</i><b>問清收費</b><span>運費、樓梯費、附加費逐項確認</span></div></div>')
    # 目錄
    toc = [('common-pitfalls', '香港到會 5 大常見陷阱'), ('portion', '到會份量參考表'), ('hidden-fees', '到會隱藏收費對照表'),
           ('expert-tips', '精明選擇到會公司 5 大秘訣'), ('checklist', '落單前必問 10 條問題'), ('kitchen-ao', 'Kitchen AO 的做法'),
           ('faq', '到會避伏常見問題'), ('conclusion', '編輯總結')]
    h.append('<nav class="toc ao-toc" aria-label="文章目錄"><span class="eb">Contents</span><ol>' + ''.join(f'<li><a href="#{a}">{t}</a></li>' for a, t in toc) + '</ol></nav>')

    # 陷阱
    h.append('<h2 id="common-pitfalls">香港到會 5 大常見陷阱</h2>')
    h.append('<p>綜合業內常見問題及客人查詢，以下五點是叫到會時最需要留意的地雷區。每一項都附上成因及避免方法。</p>')
    for no, aid, t, lead, why, do in PITS:
        w = ''.join(f'<b>{a}：</b>{b}<br>' for a, b in why)
        d = ''.join(f'<li>{x}</li>' for x in do)
        h.append(f'<div class="pit" id="{aid}"><div class="no">{no}</div><h3>{t}</h3><p>{lead}</p>'
                 f'<div><p class="why">{w}</p><div class="do"><em>避伏方法</em><ul>{d}</ul></div></div></div>')
        if no == '01':
            h.append('<figure><img src="' + IMG_CMP + '" alt="到會照騙示意：宣傳相片與實際出品對比" loading="lazy" decoding="async"><figcaption>示意圖：宣傳相片與實際出品可能存在落差</figcaption></figure>')

    # 份量表
    h.append('<h2 id="portion">到會份量參考表：按活動類型計算</h2>')
    h.append('<p>到會份量要按活動性質、時長及賓客組合計算。以下為一般參考，實際份量應與到會公司確認。</p>')
    h.append('<div class="tw"><table><thead><tr><th>活動類型</th><th>一般時長</th><th>建議份量（每人）</th><th>備註</th></tr></thead><tbody>'
             + ''.join(f'<tr><td data-l="活動類型">{a}</td><td data-l="一般時長">{b}</td><td data-l="建議份量">{c}</td><td data-l="備註">{d}</td></tr>' for a, b, c, d in PORTION) + '</tbody></table></div>')
    h.append('<p class="cap">以上為一般參考，按商戶套餐內容及賓客食量而有所不同。</p>')
    h.append('<p>想按人數直接選擇？可參考 <a href="' + U + '/product-category/party-set-by-people/">人數選餐</a>，由 2 至 100 人以上均有建議組合。</p>')

    # 收費表
    h.append('<h2 id="hidden-fees">到會隱藏收費對照表</h2>')
    h.append('<p>一份清楚的到會報價單，應列明所有收費項目。如報價單只寫「運費另議」，一定要追問實際金額。落單前可對照下表逐項確認：</p>')
    h.append('<div class="tw"><table><thead><tr><th>收費項目</th><th>常見情況</th><th>落單前應問</th></tr></thead><tbody>'
             + ''.join(f'<tr><td data-l="收費項目">{a}</td><td data-l="常見情況">{b}</td><td data-l="落單前應問">{c}</td></tr>' for a, b, c in FEES) + '</tbody></table></div>')
    
    # 秘訣
    h.append('<h2 id="expert-tips">精明選擇到會公司 5 大秘訣</h2>')
    h.append('<p>了解常見陷阱後，以下五個選擇到會公司的實用方法，可以大大減低中伏風險，找到真正的高質到會。</p>')
    h.append('<div class="tips">' + ''.join(f'<div><small>{a}</small><b>{b}</b><p>{c}</p></div>' for a, b, c in TIPS) + '</div>')

    # 清單
    h.append('<h2 id="checklist">落單前必問 10 條問題</h2>')
    h.append('<p>可以一邊查詢，一邊剔選。全部問清楚，基本上已避開大部分到會陷阱。</p>')
    h.append('<div class="chk"><span class="lb">落單前必問</span><ol>'
             + ''.join(f'<li><label><input type="checkbox"><div><b>{i+1:02d}　{q}</b><span>{s}</span></div></label></li>' for i, (q, s) in enumerate(CHECK))
             + '</ol><p class="ct">已確認 <b class="n">0</b> / 10 項</p></div>')

    # Kitchen AO
    h.append('<h2 id="kitchen-ao">Kitchen AO 的做法：價錢及安排公開透明</h2>')
    h.append('<div class="ours"><span class="eb">Why Kitchen AO</span><h3>落單前已知道全部收費</h3><ul>'
             '<li><b>網上列明價錢</b>，按人數直接選購套餐</li>'
             '<li><b>運費按地區公開</b>，網站列明各區收費</li>'
             '<li>單一訂單滿 <b>HK$1,450 全港免運費</b>（不派送地區除外）</li>'
             '<li>滿 <b>HK$700</b> 九龍指定區域免運費，港島及新界運費半價</li>'
             '<li>標準派送時段 <b>上午 11 時至晚上 8 時 30 分</b></li>'
             '<li>可<b>指定送達時間</b>（誤差 ±15 分鐘），附加費已公開列明</li>'
             '<li><b>八號風球／黑雨</b>：送貨前四小時內懸掛可免費改期</li>'
             '<li>可加配<b>餐具及派對用品</b>，一站式安排</li>'
             '</ul><div class="bt"><a class="g" href="' + U + '/product-category/party-set-by-people/">按人數選擇套餐</a>'
             '<a class="o" href="' + U + '/catering-quote-enquiry/">索取到會報價</a></div></div>')
    h.append('<p>詳細運費及派送安排，可參閱 <a href="' + U + '/delivery/">送貨需知及免運費優惠</a>。</p>')

    # 延伸閱讀
    h.append('<h2 id="related">延伸閱讀</h2><div class="rel">' + ''.join(f'<a href="{u}"><small>{c}</small>{t}</a>' for c, t, u in REL) + '</div>')

    # FAQ
    h.append('<h2 id="faq">到會避伏常見問題（FAQ）</h2><div class="faq">'
             + ''.join(f'<details><summary>{q}</summary><div><p>{a}</p></div></details>' for q, a in FAQ) + '</div>')

    # 總結
    h.append('<h2 id="conclusion">編輯總結</h2><div class="sum">'
             '<p>在香港叫到會想避開陷阱，關鍵是做足功課、問清楚、留紀錄。看真實相片、按活動計算份量、逐項確認收費，再選擇持有食環署牌照、收費透明、評價良好的到會公司，便可大大減低中伏機會。</p>'
             '<p>如正在籌備派對或公司活動，歡迎參考 <a href="' + U + '/hong-kong-catering-recommendation/">香港到會推介</a>，或直接 <a href="https://wa.me/85269011987">WhatsApp 查詢</a>。</p></div>')

    # FAQ schema
    sch = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}
    h.append('<script type="application/ld+json">' + json.dumps(sch, ensure_ascii=False) + '</script>')
    h.append('<script>(function(){var r=document.currentScript.parentNode,b=r.querySelectorAll(".chk input"),n=r.querySelector(".chk .n");if(!n)return;[].forEach.call(b,function(x){x.addEventListener("change",function(){n.textContent=r.querySelectorAll(".chk input:checked").length})})})();</script>')
    h.append('</div>')
    return '\n'.join(h)

# ===== 套用已發佈 blog 版面（.ao-bl：左文章、右側欄、文末分享及有用投票），來源：初一十五 blog =====
_tpl = (HERE.parent / 'vegetarian-blog' / 'b3-chu-yat-sap-ng-guide-WORDPRESS-layout.html').read_text(encoding='utf-8')
TPL_CSS = _tpl[:_tpl.index('<div class="ao-bl"')]
TPL_JS = _tpl[_tpl.index('</aside>') + 8:].split('</div>', 1)[1]
SIDE_CSS = """<style>
@media(max-width:1024px){.ao-bl-aside .ao-meta,.ao-bl-aside .ao-bshare{display:none!important}.ao-bl-aside{gap:14px}}
@media(max-width:767px){.ao-bl .ao-fb{gap:10px 8px;padding:16px}.ao-bl .ao-fb .aoshare{margin-bottom:4px}.ao-bl .ao-fb-q{flex:1 1 100%}.ao-bl .ao-fb .ao-fb-b{flex:1 1 0;text-align:center}.ao-bl .ao-fb-msg{flex:1 1 100%}}
.ao-bl .ao-fee{background:#141414;border-color:#141414;color:#EDE6D8}
.ao-bl .ao-fee h4{color:#C8A24A!important}
.ao-bl .ao-fee p{margin:0;padding:7px 0;border-top:1px solid #2c2a26;display:flex;justify-content:space-between;gap:10px;font-size:13.5px}
.ao-bl .ao-fee h4+p{border-top:0}
.ao-bl .ao-fee p b{color:#E4C77E;font-size:15px}
.ao-bl .ao-fee a{display:block;margin-top:10px;color:#E4C77E!important;text-decoration:none!important;font-weight:700;font-size:13.5px}
</style>"""
FB = ('<div class="ao-fb" id="aoFb"><div class="aoshare ao-fb-sh" data-pos="article_end"><span class="shl">分享：</span>'
      '<button type="button" class="sh-wa" aria-label="WhatsApp 分享" title="WhatsApp 分享"><i class="fab fa-whatsapp"></i></button>'
      '<button type="button" class="sh-fb" aria-label="Facebook 分享" title="Facebook 分享"><i class="fab fa-facebook-f"></i></button>'
      '<button type="button" class="sh-ig" aria-label="IG 分享" title="IG 分享"><i class="fab fa-instagram"></i></button>'
      '<button type="button" class="sh-cp" aria-label="複製連結" title="複製連結"><i class="fas fa-link"></i></button><span class="shm" aria-live="polite"></span></div>'
      '<span class="ao-fb-q">這篇文章對你有幫助嗎？</span><button type="button" class="ao-fb-b" data-v="yes">👍 有用</button><button type="button" class="ao-fb-b" data-v="no">👎 一般</button><span class="ao-fb-msg" aria-live="polite"></span></div>')
TAGS = ('<div class="ao-sec"><h3>相關主題</h3><div class="ao-tags">'
        '<a href="https://aoaodelivery.com/hong-kong-catering-recommendation/">香港到會推介</a>'
        '<a href="https://aoaodelivery.com/blog/company-event-catering-guide/">公司活動到會</a>'
        '<a href="https://aoaodelivery.com/product-category/party-set-by-people/">人數選餐</a>'
        '<a href="https://aoaodelivery.com/delivery/">送貨及運費</a></div></div>')
ASIDE = ('<aside class="ao-bl-aside">'
         '<div class="ao-meta"><span>作者</span><b>Kitchen AO 編輯部</b><span>更新</span><b>2026-11-18</b><span>閱讀</span><b>約 8 分鐘</b></div>'
         '<div class="ao-sc toc"><h4>目錄</h4><div class="ao-prog"><i id="prog"></i></div><ol class="ao-toc2" id="toc"></ol></div>'
         '<div class="ao-bshare" aria-label="分享文章"><b>分享</b><a href="#" id="cpl" class="cp" title="複製連結"><i class="fas fa-link"></i><em>複製</em></a>'
         '<a href="#" id="shwa" class="wa" target="_blank" rel="noopener" title="分享到 WhatsApp"><i class="fab fa-whatsapp"></i><em>WhatsApp</em></a>'
         '<a href="#" id="shfb" class="fb" target="_blank" rel="noopener" title="分享到 Facebook"><i class="fab fa-facebook-f"></i><em>Facebook</em></a>'
         '<a href="#" id="shig" class="ig" title="分享到 Instagram"><i class="fab fa-instagram"></i><em>IG</em></a></div>'
         '<div class="ao-sc ao-fee"><h4>Kitchen AO 收費一覽</h4><p><b>HK$1,450</b>全港免運費</p><p><b>HK$700</b>九龍指定區域免運費</p><p><b>11:00–20:30</b>標準派送時段</p>'
         '<a href="https://aoaodelivery.com/delivery/" target="_blank">查看各區運費 →</a></div>'
         '<div class="ao-cta2"><b>籌備活動想問清楚？</b><p>告訴我們日期、人數及預算，客服為你配搭餐單及確認收費。</p><a href="https://wa.me/85269011987" target="_blank">WhatsApp 查詢</a></div>'
         '</aside>')
def wrap(article):
    return (TPL_CSS + SIDE_CSS + '<div class="ao-bl"><main class="ao-bl-main" id="art">' + article +
            '<div class="ao-end">' + FB + TAGS + '</div></main>' + ASIDE + '</div>' + TPL_JS)

art = wrap(build())
(HERE / 'catering-pitfalls-WORDPRESS.html').write_text(art, encoding='utf-8')
title = '香港到會避伏指南 2026｜5 大常見陷阱＋落單前必問 10 條問題'
prev = ('<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex">'
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css"><title>預覽｜' + title + '</title><style>body{margin:0;background:#fff;font-family:-apple-system,"PingFang HK","Microsoft JhengHei",sans-serif}'
        '.wrap{max-width:1240px;margin:0 auto;padding:28px 20px 60px}.bc{font-size:13px;color:#888}.t{font-size:32px;line-height:1.35;font-weight:900;margin:8px 0 6px;color:#141414}.m{font-size:13px;color:#888;margin:0 0 24px}'
        '@media(max-width:767px){.t{font-size:24px}}</style></head><body><div class="wrap"><div class="bc">首頁 / 香港到會資訊</div>'
        '<div class="t">' + title + '</div><div class="m">Kitchen AO 編輯部　更新：2026-11-18</div>' + art + '</div></body></html>')
(HERE / 'catering-pitfalls-preview.html').write_text(prev, encoding='utf-8')
print(len(art))
