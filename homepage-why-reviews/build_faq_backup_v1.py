# Kitchen AO 首頁「常見問題」黑金禮賓版（配合方案 2）
SERIF='"Noto Serif TC","Songti TC","Source Han Serif TC","PMingLiU",serif'
WA='https://wa.me/85269011987'
WASVG='<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path fill="#fff" d="M17.47 14.38c-.3-.15-1.75-.86-2.02-.96-.27-.1-.47-.15-.67.15-.2.3-.77.96-.94 1.16-.17.2-.35.22-.64.07-.3-.15-1.25-.46-2.38-1.47-.88-.79-1.47-1.76-1.65-2.06-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.03-.52-.07-.15-.67-1.6-.92-2.2-.24-.58-.49-.5-.67-.5h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48 0 1.46 1.07 2.88 1.21 3.08.15.2 2.1 3.2 5.08 4.49.71.31 1.26.49 1.7.63.71.23 1.36.2 1.87.12.57-.08 1.75-.72 2-1.41.25-.69.25-1.29.17-1.41-.07-.12-.27-.2-.57-.35zM12.05 21.8h-.01a9.8 9.8 0 0 1-5-1.37l-.36-.21-3.72.98 1-3.63-.24-.37a9.79 9.79 0 0 1-1.5-5.22c0-5.4 4.4-9.8 9.83-9.8 2.62 0 5.09 1.03 6.94 2.88a9.75 9.75 0 0 1 2.87 6.93c0 5.41-4.4 9.81-9.81 9.81zm8.36-18.17A11.75 11.75 0 0 0 12.05.17C5.5.17.17 5.5.17 12.05c0 2.09.55 4.13 1.59 5.93L.07 24l6.17-1.62a11.83 11.83 0 0 0 5.8 1.48h.01c6.55 0 11.88-5.33 11.88-11.88 0-3.17-1.24-6.16-3.48-8.4z"/></svg>'
L=lambda u,t:'<a href="%s">%s</a>'%(u,t)
Q=[('到會服務需要幾日前預訂？','建議你盡早預訂，尤其係週末、節日或大型活動日子會較快額滿。實際截單時間可按餐單種類、訂單規模及送貨安排而定，建議直接 '+L(WA,'WhatsApp 查詢')+'。'),
('到會有沒有最低消費或最低訂購要求？','不同套餐、單點類別及送貨安排可能設有不同要求。你可以先提供活動日期、人數及送貨地點，我們會按需要提供最合適的建議。'),
('送貨覆蓋哪些地區？會收送貨費嗎？','一般可安排送貨至港九新界多個地區，實際收費會按地點、時段及訂單內容而定。偏遠地區或指定時段或會有額外運費，運費會根據送貨地區及訂單總金額計算。<span class="fr">單一訂單滿 <b>HK$700</b> 可享部分區域運費減免，滿 <b>HK$1,450</b> 可享全港免運費（不派送地區除外）。</span>詳細收費請參考'+L('https://aoaodelivery.com/delivery/','送貨需知')+'。'),
('可以按活動需要客製到會餐單嗎？','可以。無論係生日派對、公司活動、商務午餐或船河聚會，都可以按人數、預算及用餐形式調整餐單內容，亦可配搭'+L('https://aoaodelivery.com/product-category/a-la-carte/','單點美食')+'。'),
('有沒有素食到會選擇？','有。可參考'+L('https://aoaodelivery.com/product-category/party/vegetarians-set/','「素」味人生素食套餐')+'；如有其他飲食要求，歡迎訂購前 WhatsApp 查詢，我們會按餐單建議合適選擇。'),
('會提供餐具、紙碟或派對用品嗎？','可按需要加配餐具、飲品及部分'+L('https://aoaodelivery.com/product-category/party-supplies/','派對用品')+'，方便你一站式安排整個活動。實際供應內容可按當時餐單及加購選項確認。')]
css='''<style>
.aofq{--g:#9a7b4f;--gd:#c9a45c;--gl:#E4C77E;--ln:#ece6da;--ink:#1a1816;font-size:15px;line-height:1.8;color:#4a4540}
.aofq *{box-sizing:border-box;border-radius:0}
.aofq .wrap{max-width:1180px;margin:0 auto;padding:80px 24px;display:grid;grid-template-columns:5fr 7fr;gap:72px;align-items:start}
.aofq .ey{font-size:12px;letter-spacing:.3em;color:var(--g);text-transform:uppercase;margin:0 0 14px}
.aofq h2{font-family:SERIF;font-weight:600;font-size:36px;line-height:1.3;color:var(--ink);margin:0 0 16px;letter-spacing:.05em}
.aofq .sub{margin:0;color:#6b645b}
.aofq .sub span{display:block}
.aofq .more{display:inline-block;margin-top:22px;font-size:14px;letter-spacing:.12em;color:var(--ink)!important;text-decoration:none!important;border-bottom:1px solid var(--gd);padding-bottom:2px}
.aofq .more:hover{color:var(--g)!important}
.aofq .ask{margin-top:40px;padding-top:28px;border-top:1px solid var(--ln)}
.aofq .ask p{margin:0 0 14px;font-family:SERIF;font-size:17px;color:var(--ink);letter-spacing:.05em}
.aofq .bt{display:flex;flex-wrap:wrap;gap:10px}
.aofq .bt a{display:inline-flex;align-items:center;gap:9px;padding:13px 22px;font-size:13px;font-weight:700;letter-spacing:.16em;text-decoration:none!important;line-height:1;transition:opacity .25s,background .25s,color .25s}
.aofq .bt .wa{background:#25D366;color:#fff!important}
.aofq .bt .wa:hover{opacity:.88}
.aofq .bt .ct{background:#1a1816;color:var(--gl)!important;border:1px solid #1a1816}
.aofq .bt .ct:hover{background:var(--gl);color:#1a1816!important;border-color:var(--gl)}
.aofq .ls{border-top:1px solid var(--ln)}
.aofq details{border-bottom:1px solid var(--ln)}
.aofq summary{list-style:none;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:20px;padding:24px 0;font-family:SERIF;font-weight:600;font-size:18px;color:var(--ink);letter-spacing:.04em}
.aofq summary::-webkit-details-marker{display:none}
.aofq summary:after{content:"+";font-family:Arial,sans-serif;font-weight:300;font-size:24px;line-height:1;color:var(--gd);flex:0 0 auto;transition:transform .25s}
.aofq details[open] summary:after{transform:rotate(45deg)}
.aofq summary:hover{color:var(--g)}
.aofq .an{padding:0 44px 26px 0;color:#5e574e}
.aofq .an a{color:var(--ink)!important;text-decoration:none!important;border-bottom:1px solid var(--gd)}
.aofq .an a:hover{color:var(--g)!important}
.aofq .fr{display:block;margin:12px 0;padding:12px 16px;background:#f6f1e7;color:#4a4540}
.aofq .fr b{color:var(--ink)}
@media(max-width:1024px){.aofq .wrap{grid-template-columns:1fr;gap:36px}}
@media(max-width:680px){.aofq .wrap{padding:60px 20px}.aofq h2{font-size:28px}.aofq summary{font-size:16px;padding:20px 0}.aofq .an{padding-right:0}.aofq .ask{border-top:0;padding-top:0;margin-top:28px}.aofq .bt a{flex:1;justify-content:center}}
</style>'''.replace('SERIF',SERIF)
h=['<section class="aofq" itemscope itemtype="https://schema.org/FAQPage"><div class="wrap"><div class="hd">',
'<p class="ey">FAQ</p><h2>到會常見問題</h2><p class="sub"><span>以下整理咗客人最常查詢的訂購、送貨及餐單安排問題，</span><span>方便你快速了解。</span></p>',
'<a class="more" href="https://aoaodelivery.com/%e5%b8%b8%e8%a6%8b%e5%95%8f%e9%a1%8c/">查看全部常見問題</a>',
'<div class="ask"><p>仲有其他問題？</p><div class="bt"><a class="wa" href="'+WA+'" target="_blank" rel="noopener noreferrer" aria-label="WhatsApp 查詢">'+WASVG+'WhatsApp 查詢</a><a class="ct" href="https://aoaodelivery.com/contacts/">聯絡我們</a></div></div></div><div class="ls">']
for n,(q,a) in enumerate(Q):
    h.append('<details itemscope itemprop="mainEntity" itemtype="https://schema.org/Question"%s><summary><span itemprop="name">%s</span></summary><div class="an" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer"><div itemprop="text">%s</div></div></details>'%(' open' if n==0 else '',q,a))
h.append('</div></div></section>')
o=css+''.join(h)
assert '<script' not in o and '——' not in o and '→' not in o
open('faq-option2-rawhtml.html','w').write(o)
open('/sessions/great-festive-darwin/mnt/Downloads/首頁-常見問題-黑金禮賓-rawhtml.html','w').write(o)
open('/sessions/great-festive-darwin/mnt/Downloads/首頁-常見問題-預覽.html','w').write('<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body style="margin:0;font-family:Rubik,\'PingFang HK\',sans-serif">'+o+'</body></html>')
print(len(o))
