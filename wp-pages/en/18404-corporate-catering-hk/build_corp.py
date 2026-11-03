import re
"""公司到會（18404）中英 Raw HTML 產生器
python3 build_corp.py → zh-rawhtml.html（Extra class：ao-zh）、en-rawhtml.html（Extra class：ao-en）
Tab 做法：所有內容都在 HTML 內（Google 可讀取）；JavaScript 載入後才把非當前分頁隱藏，沒有 JS 時全部顯示。
"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
P = 'https://aoaodelivery.com'
WA = 'https://wa.me/85269011987'

CSS = '''<style>
.page-id-18404 h1.heading-title{word-break:keep-all;text-wrap:balance;}
.ao-corp{max-width:860px;margin:0 auto;padding-top:28px;color:#3A342B;font-size:16px;line-height:1.8;}
.ao-corp h2{position:relative;font-size:24px;font-weight:900;color:#1A1A1A;margin:36px 0 14px;padding:16px 0 0;border:0;line-height:1.4;scroll-margin-top:110px;}
.ao-corp h2:before{content:"";position:absolute;left:0;top:0;width:46px;height:4px;border-radius:3px;background:#C8A24A;}
.ao-corp h3{font-size:18px;font-weight:800;color:#1A1A1A;margin:24px 0 8px;scroll-margin-top:110px;}
.ao-corp p{margin:0 0 14px;}
.ao-corp ul,.ao-corp ol{margin:0 0 16px;padding-left:22px;}
.ao-corp li{margin:0 0 6px;}
.ao-corp a{color:#9A7B2E;font-weight:700;}
.ao-corp .ao-tabwrap{position:relative;margin:18px 0 0;}
.ao-corp .ao-tabs{display:flex;align-items:stretch;height:50px;border-top:1px solid #EEE9DF;border-bottom:1px solid #EEE9DF;overflow-x:auto;overflow-y:hidden;scrollbar-width:none;-webkit-overflow-scrolling:touch;box-sizing:border-box;}
.ao-corp .ao-tabs::-webkit-scrollbar{display:none;}
.ao-corp .ao-tabs a{flex:1 0 auto;display:flex;align-items:center;justify-content:center;height:100%;box-sizing:border-box;padding:0 16px;font-size:15px;line-height:1;font-weight:700;color:#8A8172;text-decoration:none;white-space:nowrap;box-shadow:inset 0 -2px 0 transparent;transition:color .2s,box-shadow .2s;}
.ao-corp .ao-tabs a:hover{color:#1A1A1A;}
.ao-corp .ao-tabs a.on{color:#9A7B2E;box-shadow:inset 0 -2px 0 #C8A24A;}
.ao-corp.js-tabs .ao-pane{display:none;}
.ao-corp.js-tabs .ao-pane.on{display:block;animation:aoFade .25s ease;}
.ao-corp.js-tabs .ao-pane > h2:first-child{margin-top:22px;}
@keyframes aoFade{from{opacity:0;}to{opacity:1;}}
.ao-corp .ao-scene{display:flex;flex-wrap:wrap;justify-content:center;gap:14px;margin:12px 0 18px;}
.ao-corp .ao-scene a{position:relative;display:block;box-sizing:border-box;width:calc((100% - 28px)/3);background:#F4F7FA;border:1.5px solid #DCE3EA;border-radius:16px;padding:20px 16px 18px;text-align:center;text-decoration:none;color:#4A4238;font-weight:400;transition:border-color .2s,transform .2s;}
.ao-corp .ao-scene a:hover{border-color:#C8A24A;transform:translateY(-2px);}
.ao-corp .ao-scene .no{display:inline-block;width:26px;height:26px;line-height:26px;border-radius:50%;background:#45566E;color:#fff;font-size:13px;font-weight:800;}
.ao-corp .ao-scene .ic{display:block;font-size:26px;line-height:1;margin:10px 0 8px;}
.ao-corp .ao-scene b{display:block;color:#1A1A1A;font-size:16px;font-weight:900;margin:0 0 4px;}
.ao-corp .ao-scene .en{display:block;font-size:12px;font-weight:700;color:#9A7B2E;margin:-2px 0 6px;}
.ao-corp .ao-scene .d{display:block;font-size:14px;line-height:1.6;color:#5A5246;}
.ao-corp .ao-scene .m{display:inline-block;margin-top:8px;font-size:13px;font-weight:800;color:#9A7B2E;background:#FFF8E6;border-radius:20px;padding:2px 10px;}
.ao-corp .ao-scene a.hot{background:#EEF4EC;border-color:#5E7E5C;}
.ao-corp .ao-scene a.hot .no{background:#5E7E5C;}
.ao-corp .ao-scene .tag{position:absolute;top:-11px;right:12px;background:#5E7E5C;color:#fff;font-size:12px;font-weight:800;padding:2px 10px;border-radius:12px;}
.ao-corp .ao-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:8px 0 16px;}
.ao-corp .ao-cards a{display:block;background:#fff;border:1.5px solid #EBE3D2;border-radius:14px;padding:14px 16px;text-decoration:none;color:#3A342B;font-weight:400;}
.ao-corp .ao-cards a:hover{border-color:#C8A24A;}
.ao-corp .ao-cards b{display:block;color:#1A1A1A;font-size:16px;margin-bottom:4px;}
.ao-corp .ao-cards span{font-size:14px;color:#6B6252;}
.ao-corp table{width:100%;border-collapse:collapse;margin:0 0 10px;font-size:15px;border:1px solid #EBE3D2;}
.ao-corp th{background:#1A1A1A;color:#F7CE46;text-align:left;padding:9px 12px;font-weight:800;}
.ao-corp td{border-top:1px solid #EBE3D2;padding:9px 12px;vertical-align:top;}
.ao-corp td:first-child{font-weight:800;color:#1A1A1A;background:#FAF7F1;}
.ao-corp .ao-tblwrap{overflow-x:auto;-webkit-overflow-scrolling:touch;}
.ao-corp .ao-faq{border:1px solid #EBE3D2;border-radius:12px;margin:0 0 10px;background:#fff;}
.ao-corp .ao-faq summary{cursor:pointer;list-style:none;padding:13px 44px 13px 16px;font-weight:800;color:#1A1A1A;position:relative;}
.ao-corp .ao-faq summary::-webkit-details-marker{display:none;}
.ao-corp .ao-faq summary:after{content:"+";position:absolute;right:16px;top:50%;margin-top:-14px;font-size:22px;color:#C8A24A;}
.ao-corp .ao-faq[open] summary:after{content:"\\2212";}
.ao-corp .ao-faq .a{padding:0 16px 14px;color:#4A4238;}
.ao-corp .ao-note{font-size:14px;color:#6B6252;}
.ao-corp .ao-cta{display:flex;justify-content:center;flex-wrap:wrap;gap:12px;margin:30px 0 10px;}
.ao-corp .ao-cta a{display:block;min-width:280px;max-width:100%;box-sizing:border-box;text-align:center;background:#C8A24A!important;color:#1A1A1A!important;font-size:16px;font-weight:800;line-height:1.4;white-space:nowrap;padding:14px 20px;border:2px solid #C8A24A;border-radius:40px;text-decoration:none!important;transition:background .2s,color .2s;}
.ao-corp .ao-cta a:hover{background:#1A1A1A!important;color:#F7CE46!important;border-color:#1A1A1A;}
.ao-corp .ao-cta a.alt{background:#1A1A1A!important;color:#F7CE46!important;border-color:#1A1A1A;}
.ao-corp .ao-cta a.alt:hover{background:#C8A24A!important;color:#1A1A1A!important;border-color:#C8A24A;}
.ao-corp img{max-width:100%;height:auto;border-radius:14px;}
.ao-corp .ao-kv{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:0 0 14px;}
.ao-corp .ao-kv img{display:block;width:100%;height:auto;aspect-ratio:2/3;object-fit:cover;border-radius:14px;}
.ao-corp .ao-kv img.k1{object-position:50% 30%;}
.ao-corp .ao-kv img.k2{object-position:50% 55%;}
@media(max-width:768px){.ao-corp .ao-scene a{width:calc((100% - 14px)/2);}}
@media(max-width:600px){.ao-corp .ao-cards{grid-template-columns:1fr;}.ao-corp .ao-scene a{width:100%;}.ao-corp .ao-tabs{height:46px;}.ao-corp .ao-tabs a{flex:0 0 auto;padding:0 14px;font-size:14px;}.ao-corp .ao-kv{gap:6px;}.ao-corp .ao-kv img{aspect-ratio:3/4;border-radius:10px;}.ao-corp h2{font-size:21px;}.ao-corp .ao-cta a{width:100%;min-width:0;max-width:320px;white-space:normal;}}

.ao-corp .ao-shelf{background:#1A1A1A;border-radius:18px;padding:18px 18px 14px;margin:20px 0 0;}
.ao-corp .ao-shelf-t{color:#fff !important;font-size:19px;font-weight:800;margin:0 0 2px !important;}
.ao-corp .ao-shelf-d{color:#C9BFA8 !important;font-size:14px;margin:0 0 12px !important;line-height:1.6;}
.ao-corp .ao-slwrap{position:relative;}
.ao-corp .ao-slider{display:flex;gap:12px;overflow-x:auto;overflow-y:hidden;scroll-snap-type:x proximity;scrollbar-width:none;overscroll-behavior-x:contain;-webkit-overflow-scrolling:touch;padding:0 0 4px;}
.ao-corp .ao-slider::-webkit-scrollbar{display:none;}
.ao-corp .ao-scard{flex:0 0 200px;scroll-snap-align:start;text-decoration:none !important;display:flex;flex-direction:column;}
.ao-corp .ao-scard img{width:100% !important;height:auto !important;aspect-ratio:1/1;object-fit:contain;object-position:center top;background:#2A2622;border-radius:12px !important;display:block;margin:0 !important;}
.ao-corp .ao-scard.fill img{object-fit:cover;object-position:center;}
.ao-corp .ao-scard .nm{color:#EDE6D6;font-size:14px;font-weight:600;line-height:1.45;padding:8px 2px 0;}
.ao-corp .ao-scard .pr{color:#C8A24A;font-size:13px;font-weight:700;padding:2px 2px 0;}
.ao-corp .ao-sl-btn{position:absolute;top:84px;z-index:2;width:38px;height:38px;border-radius:50%;border:2px solid #C8A24A;background:rgba(26,26,26,.92);color:#F7CE46;font-size:24px;line-height:32px;text-align:center;padding:0;cursor:pointer;}
.ao-corp .ao-sl-btn.prev{left:-8px;}.ao-corp .ao-sl-btn.next{right:-8px;}
.ao-corp .ao-sl-btn[hidden]{display:none;}
.ao-corp .ao-btn-gold{display:block;width:fit-content;margin:14px auto 10px;background:#C8A24A;color:#1A1A1A !important;border:2px solid #C8A24A;border-radius:40px;padding:10px 28px;font-size:15px;font-weight:800;text-decoration:none !important;}
.ao-corp .ao-btn-gold:hover{background:#1A1A1A;color:#F7CE46 !important;}
@media(max-width:600px){.ao-corp .ao-scard{flex-basis:62%;}.ao-corp .ao-sl-btn{top:30%;}}
.ao-corp .ao-cust{display:grid;grid-template-columns:38% 1fr;background:#FBF7EE;border:1px solid #EADFC8;border-radius:18px;overflow:hidden;margin:24px 0 10px;}
.ao-corp .ao-cust .ph{min-height:230px;background:#2A2622 center/cover no-repeat;}
.ao-corp .ao-cust .tx{padding:24px 26px;display:flex;flex-direction:column;justify-content:center;}
.ao-corp .ao-cust .eb{font-size:12px;font-weight:800;letter-spacing:3px;color:#9A7B2E;margin:0 0 4px !important;}
.ao-corp .ao-cust .t{font-size:20px;font-weight:800;color:#1A1A1A;margin:0 0 8px !important;}
.ao-corp .ao-cust .d{margin:0 0 16px !important;font-size:15px;line-height:1.8;color:#4a4238;}
.ao-corp .ao-cust .btns{display:flex;gap:10px;flex-wrap:wrap;}
.ao-corp .ao-cust .btns a{display:inline-block;padding:10px 20px;border-radius:40px;font-size:14px;font-weight:800;text-decoration:none !important;}
.ao-corp .ao-cust .b1{background:#1A1A1A;color:#F7CE46 !important;}
.ao-corp .ao-cust .b2{border:1.5px solid #1A1A1A;color:#1A1A1A !important;}
@media(max-width:640px){.ao-corp .ao-cust{grid-template-columns:1fr;}.ao-corp .ao-cust .ph{min-height:180px;}.ao-corp .ao-cust .tx{padding:20px;}.ao-corp .ao-cust .btns a{flex:1;text-align:center;}}
/* v9：深色目錄列｜桌面 2 行（5＋4）、字一行；手機 3 欄 × 3 行 */
.ao-corp .ao-tabwrap{margin:22px 0 0;}
.ao-corp .ao-tabs{display:grid !important;grid-template-columns:repeat(5,minmax(0,1fr));gap:0;height:auto !important;overflow:visible !important;background:#1A1A1A;border:0 !important;border-radius:6px;padding:6px 12px;}
.ao-corp .ao-tabs a{flex:none !important;height:auto !important;min-height:54px;display:flex;align-items:center;justify-content:center;padding:14px 6px 16px !important;white-space:nowrap !important;text-align:center;font-size:14.5px !important;font-weight:500 !important;line-height:1.3 !important;letter-spacing:.08em;color:#E9E2D3 !important;box-shadow:none !important;position:relative;}
.ao-corp .ao-tabs a:nth-child(-n+5){border-bottom:1px solid #33302b;}
.ao-corp .ao-tabs a:hover{color:#F7E3A8 !important;}
.ao-corp .ao-tabs a.on{color:#C8A24A !important;font-weight:700 !important;}
.ao-corp .ao-tabs a.on:after{content:"";position:absolute;left:50%;bottom:7px;width:22px;height:2px;margin-left:-11px;background:#C8A24A;}
.ao-corp .ao-faqsec{margin-top:40px;padding-top:6px;border-top:1px solid #EEE9DF;}
@media(max-width:768px){.ao-corp .ao-tabs{grid-template-columns:repeat(3,minmax(0,1fr));padding:4px 6px;}.ao-corp .ao-tabs a{min-height:50px;font-size:13px !important;letter-spacing:.03em;padding:12px 2px 15px !important;}.ao-corp .ao-tabs a:nth-child(-n+5){border-bottom:0;}.ao-corp .ao-tabs a:nth-child(-n+6){border-bottom:1px solid #33302b;}}
/* v10：主分類 tab＋間距 */
.ao-corp .ao-tabs .main{grid-column:1 / -1;min-height:58px;font-size:17px !important;font-weight:800 !important;letter-spacing:.12em;color:#C8A24A !important;gap:12px;}
.ao-corp .ao-tabs .main .mk{font-size:11px;letter-spacing:.25em;color:#8E836F;font-weight:700;}
.ao-corp .ao-tabs .main{background:linear-gradient(135deg,#A9832F 0%,#D9B868 38%,#F3DD9A 52%,#D2AD57 66%,#A9832F 100%);color:#1A1A1A !important;border-radius:4px 4px 0 0;overflow:hidden;box-shadow:inset 0 1px 0 rgba(255,255,255,.45),inset 0 -1px 0 rgba(0,0,0,.15);}
.ao-corp .ao-tabs .main:before{content:"";position:absolute;top:0;left:-40%;width:30%;height:100%;background:linear-gradient(100deg,rgba(255,255,255,0),rgba(255,255,255,.55),rgba(255,255,255,0));transform:skewX(-20deg);animation:aoCorpShine 5s ease-in-out infinite;pointer-events:none;}
@keyframes aoCorpShine{0%,60%{left:-40%;}85%,100%{left:120%;}}
@media (prefers-reduced-motion:reduce){.ao-corp .ao-tabs .main:before{animation:none;display:none;}}
.ao-corp .ao-tabs .main .mk{color:#4a3c1c !important;}
.ao-corp .ao-tabs .main:after{display:none;}
.ao-corp .ao-tabs .main{color:#1A1A1A !important;display:flex;align-items:center;justify-content:center;position:relative;cursor:default;}
.ao-corp .ao-pane{padding-top:8px;}
.ao-corp p{margin:0 0 20px;line-height:1.9;}
.ao-corp ul,.ao-corp ol{margin:0 0 22px;}
.ao-corp li{margin:0 0 9px;}
.ao-corp h2{margin:44px 0 18px !important;}
.ao-corp .ao-pane > h2:first-child{margin-top:34px !important;}
.ao-corp h3{margin:34px 0 12px;}
.ao-corp .ao-shelf{margin:32px 0 0 !important;}
.ao-corp .ao-btn-gold{margin:20px auto 34px !important;}
.ao-corp .ao-tblwrap{margin:0 0 20px;}
.ao-corp .ao-cust{margin:34px 0 14px !important;}
@media(max-width:768px){.ao-corp .ao-tabs .main{font-size:15px !important;min-height:52px;}.ao-corp h2{margin:36px 0 14px !important;}}
/* v11：手機版左右留白＋responsive 修正 */
@media(max-width:768px){
.ao-corp{padding-left:18px !important;padding-right:18px !important;box-sizing:border-box;-webkit-text-size-adjust:100%;font-size:15.5px;}
.ao-corp .ao-tabs{padding:4px 8px;}
.ao-corp .ao-shelf{padding:16px 14px 12px;border-radius:16px;}
.ao-corp .ao-scard{flex-basis:58%;}
.ao-corp .ao-sl-btn{width:34px;height:34px;font-size:22px;line-height:28px;}
.ao-corp .ao-sl-btn.prev{left:-6px;}.ao-corp .ao-sl-btn.next{right:-6px;}
.ao-corp .ao-cust .tx{padding:20px 18px;}
.ao-corp table{font-size:13.5px;min-width:480px;}
.ao-corp th,.ao-corp td{padding:8px 9px !important;}
.ao-corp .ao-tblwrap{margin:0 0 20px;border-radius:10px;}
.ao-corp h3{font-size:17px;margin:28px 0 10px;}
.ao-corp ul,.ao-corp ol{padding-left:20px;}
.ao-corp .ao-faq summary{padding:12px 40px 12px 14px;font-size:15px;}
.ao-corp .ao-kv{margin:0 0 18px;}
}
@media(max-width:380px){.ao-corp{padding-left:14px !important;padding-right:14px !important;}.ao-corp .ao-tabs a{font-size:12.5px !important;}.ao-corp .ao-scard{flex-basis:66%;}}
/* v12：主分類下提示語 */
.ao-corp .ao-tabs .ao-tabtip{grid-column:1 / -1;display:block;text-align:center;color:#C9BFA8;font-size:13.5px;letter-spacing:.12em;padding:12px 8px 10px;border-bottom:1px solid #33302b;}
@media(max-width:768px){.ao-corp .ao-tabs .ao-tabtip{font-size:12.5px;letter-spacing:.06em;padding:10px 6px 8px;}}
/* v13：已選擇＝方案 A 金色外框＋✓ */
.ao-corp .ao-tabs a.t.on{color:#F7E3A8 !important;font-weight:700 !important;}
.ao-corp .ao-tabs a.t.on:after{content:"✓" !important;position:relative !important;left:auto !important;bottom:auto !important;width:auto !important;height:auto !important;margin:0 0 0 6px !important;background:none !important;color:#C8A24A;font-weight:900;}
.ao-corp .ao-tabs a.t.on:before{content:"";position:absolute;inset:7px 5px;border:1.5px solid #C8A24A;border-radius:10px;background:rgba(200,162,74,.08);pointer-events:none;}
.ao-corp .ao-tabs a.t{display:flex;align-items:center;justify-content:center;}
/* v14：產品卡＝方案 B 黑金 */
.ao-corp .ao-scard{flex:0 0 240px !important;background:#221E1A;border:1px solid #3a3226;border-radius:16px;overflow:hidden;box-shadow:0 8px 22px rgba(0,0,0,.25);}
.ao-corp .ao-scard .im{display:flex;align-items:center;justify-content:center;aspect-ratio:1/1;padding:14px;background:radial-gradient(circle at 50% 35%,#3a2f22 0%,#1f1a15 72%);border-bottom:1px solid #C8A24A;box-sizing:border-box;}
.ao-corp .ao-scard .im img{width:100% !important;height:100% !important;aspect-ratio:auto !important;object-fit:contain !important;background:none !important;border-radius:8px !important;}
.ao-corp .ao-scard.fill .im{padding:0;}
.ao-corp .ao-scard.fill .im img{object-fit:cover !important;border-radius:0 !important;}
.ao-corp .ao-scard .ft{display:flex;align-items:center;gap:10px;padding:12px 14px 14px;flex:1;}
.ao-corp .ao-scard .tx{flex:1;min-width:0;display:block;}
.ao-corp .ao-scard .nm{display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;color:#F4ECDD !important;font-size:14.5px !important;font-weight:700 !important;line-height:1.4 !important;padding:0 !important;}
.ao-corp .ao-scard .pr{display:block;color:#C8A24A !important;font-size:12.5px !important;font-weight:700;padding:3px 0 0 !important;}
.ao-corp .ao-scard .buy{flex:none;background:linear-gradient(135deg,#A9832F,#E4C77E 50%,#B8913E);color:#1A1A1A;border-radius:30px;padding:7px 13px;font-size:13px;font-weight:800;}
.ao-corp .ao-sl-btn{top:100px;}
@media(max-width:768px){.ao-corp .ao-scard{flex-basis:72% !important;}.ao-corp .ao-sl-btn{top:32%;}}
</style>'''

# 分頁：按下去只換內容；網址 #hash 同步，方便分享及 FAQ 直達
JS = '''<script>(function(){var r=document.querySelector(".ao-corp");if(!r)return;var n=r.querySelector(".ao-tabs");if(!n)return;var T=[].slice.call(n.querySelectorAll("a")),P=T.map(function(a){return document.getElementById(a.getAttribute("href").slice(1))});if(P.some(function(p){return !p}))return;r.classList.add("js-tabs");n.setAttribute("role","tablist");function show(i,push){T.forEach(function(a,k){var on=k===i;a.classList.toggle("on",on);a.setAttribute("aria-selected",on?"true":"false");P[k].classList.toggle("on",on);});var a=T[i];if(n.scrollWidth>n.clientWidth)n.scrollTo({left:a.offsetLeft-(n.clientWidth-a.offsetWidth)/2,behavior:"smooth"});if(push&&history.replaceState)history.replaceState(null,"","#"+P[i].id);}T.forEach(function(a,i){a.setAttribute("role","tab");P[i].setAttribute("role","tabpanel");a.addEventListener("click",function(e){e.preventDefault();show(i,true);var top=n.getBoundingClientRect().top+window.pageYOffset-120;if(window.pageYOffset>top)window.scrollTo({top:top,behavior:"smooth"});});});function fromHash(){var h=location.hash.slice(1);if(!h)return 0;var el=document.getElementById(h);if(!el)return 0;for(var k=0;k<P.length;k++){if(P[k]===el||P[k].contains(el))return k;}return 0;}var s=fromHash();show(s,false);if(location.hash&&s){setTimeout(function(){var el=document.getElementById(location.hash.slice(1));if(el)el.scrollIntoView({behavior:"smooth"});},150);}window.addEventListener("hashchange",function(){show(fromHash(),false);});[].slice.call(r.querySelectorAll('a[href^="#"]')).forEach(function(l){if(n.contains(l))return;l.addEventListener("click",function(e){var el=document.getElementById(l.getAttribute("href").slice(1));if(!el)return;for(var k=0;k<P.length;k++){if(P[k]===el||P[k].contains(el)){e.preventDefault();show(k,true);var top=n.getBoundingClientRect().top+window.pageYOffset-120;window.scrollTo({top:top,behavior:"smooth"});return;}}});});})();</script>'''

# 度身訂製卡（方案 B2）：每個場景一張不同的 Pexels 免費相（上線前建議下載並上載到 WP 媒體庫）
PX = lambda i: f'https://images.pexels.com/photos/{i}/pexels-photo-{i}.jpeg?auto=compress&cs=tinysrgb&w=800'
CUST_IMG = {'office-lunch': PX(13065230), 'meeting': PX(30507463), 'training': PX(38730067),
            'annual-dinner': P + '/wp-content/uploads/2023/12/20221114_AOKitchen_-321-1024x1024.jpg',
            'festive': PX(24863059), 'business-event': PX(38958593), 'institutions': PX(2291367)}
def cust(pid, html):
    def f(m):
        img = CUST_IMG.get(pid)
        if not img: return m.group(0)
        return (f'<div class="ao-cust"><div class="ph" role="img" aria-label="Kitchen AO 到會菜式" style="background-image:url(\'{img}\')"></div><div class="tx">'
                f'<p class="eb">CUSTOM MENU</p><p class="t">想度身訂製餐單？</p><p class="d">{m.group(1)}</p>'
                f'<div class="btns"><a class="b1" href="{WA}?text=%E6%83%B3%E6%9F%A5%E8%A9%A2%E5%BA%A6%E8%BA%AB%E8%A8%82%E8%A3%BD%E5%85%AC%E5%8F%B8%E5%88%B0%E6%9C%83" target="_blank" rel="noopener">WhatsApp 查詢</a>'
                f'<a class="b2" href="{P}/catering-quote-enquiry/">到會報價查詢</a></div></div></div>')
    return re.sub(r'<div class="ao-custom"><b>想度身訂製？</b>(.*?)</div>', f, html, flags=re.S)

JS_SL = '''<script>(function(){document.querySelectorAll(".ao-corp .ao-slwrap").forEach(function(w){var s=w.querySelector(".ao-slider"),p=w.querySelector(".prev"),n=w.querySelector(".next");function u(){var m=s.scrollWidth-s.clientWidth;p.hidden=s.scrollLeft<4;n.hidden=s.scrollLeft>m-4;}p.addEventListener("click",function(){s.scrollBy({left:-s.clientWidth*.8,behavior:"smooth"})});n.addEventListener("click",function(){s.scrollBy({left:s.clientWidth*.8,behavior:"smooth"})});s.addEventListener("scroll",u,{passive:true});window.addEventListener("resize",u);u();document.querySelectorAll(".ao-corp .ao-tabs a").forEach(function(a){a.addEventListener("click",function(){setTimeout(u,50)})});});})();</script>'''


def build(L):
    o = ['<div class="ao-corp">', CSS, '']
    FIXED = ('faq', 'price')   # 固定顯示在所有分頁內容之後（不放 tab）
    tabs = [p for p in L['panes'] if p[0] not in FIXED]
    fixed = [p for p in L['panes'] if p[0] == 'price']
    faqp = [p for p in L['panes'] if p[0] == 'faq']
    main = None
    if L.get('main_label'):
        k = L['intro'].index('<h2>')
        top, rest = L['intro'][:k], L['intro'][k:]
        main = ('overview', L['main_label'], rest + '\n' + L.get('summary', ''))
        tabs = [('overview', L.get('all_label', '全部'), main[2])] + tabs
        o.append(top)
    else:
        o.append(L['intro'])
    o.append(f'<div class="ao-kv"><img class="k1" decoding="async" src="{P}/wp-content/uploads/2026/03/WhatsApp-Image-2026-03-25-at-3.58.36-PM-scaled.jpeg" alt="{L["img_alt"]}" width="600" height="300" /><img class="k2" decoding="async" src="{P}/wp-content/uploads/2023/11/IMG_2358.jpg" alt="{L["img_alt2"]}" width="600" height="300" /></div>')
    n = len(tabs); c = (n + 1) // 2; m = 3 if n > 4 else 2
    o.append(f'<style>.ao-corp .ao-tabs a.t{{border-bottom:0 !important;border-top:1px solid #33302b;}}@media(min-width:769px){{.ao-corp .ao-tabs{{grid-template-columns:repeat({c},minmax(0,1fr)) !important;}}.ao-corp .ao-tabs a.d1{{border-top:0;}}}}@media(max-width:768px){{.ao-corp .ao-tabs{{grid-template-columns:repeat({m},minmax(0,1fr)) !important;}}.ao-corp .ao-tabs a.m1{{border-top:0;}}}}</style>')
    o.append(f'<div class="ao-tabwrap"><nav class="ao-tabs" style="--n:{n}" aria-label="{L["nav_label"]}">')
    if main:
        o.append(f'<div class="main">{main[1]}</div>')
        if L.get('tab_hint'):
            o.append(f'<span class="ao-tabtip">{L["tab_hint"]}</span>')
    for i, (pid, label, _) in enumerate(tabs):
        cls = ['t'] + (['d1'] if i < c else []) + (['m1'] if i < m else []) + (['on'] if i == 0 else [])
        o.append(f'<a href="#{pid}" class="{" ".join(cls)}">{label}</a>')
    o.append('</nav></div>')
    allt = tabs
    for pid, label, html in allt:
        o.append(f'<section class="ao-pane" id="{pid}">\n{cust(pid, html.strip())}\n</section>')
    if L.get('summary') and not main:
        o.append(f'<section class="ao-faqsec" id="summary">\n{L["summary"].strip()}\n</section>')
    # 價錢及流程、常見問題：不放 tab，固定顯示在每個分頁最底（只輸出一次）
    for pid, label, html in fixed:
        o.append(f'<section class="ao-faqsec" id="{pid}">\n{html.strip()}\n</section>')
    for pid, label, html in faqp:
        o.append(f'<section class="ao-faqsec" id="{pid}">\n{html.strip()}\n</section>')
    faq = L['faq']
    o.append('<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}, ensure_ascii=False, separators=(',', ':')) + '</script>')
    o.append('<script type="application/ld+json">' + json.dumps(L['service'], ensure_ascii=False, separators=(',', ':')) + '</script>')
    o.append(L['cta'])
    o.append(L['updated'])
    o.append(JS)
    o.append(JS_SL)
    o.append('</div>')
    return '\n'.join(o) + '\n'


def faq_html(faq):
    return '\n'.join(f'<details class="ao-faq"><summary>{q}</summary><div class="a">{a}</div></details>' for q, a in faq)


def a(path, text):
    return f'<a href="{P}{path}">{text}</a>'


def scene(items):
    o = ['<div class="ao-scene">']
    for i, (href, ic, title, en, desc, meta, tag) in enumerate(items, 1):
        cls = ' class="hot"' if tag else ''
        t = f'<span class="tag">{tag}</span>' if tag else ''
        sub = f'<span class="en">{en}</span>' if en else ''
        o.append(f'<a href="#{href}"{cls}>{t}<span class="no">{i}</span><span class="ic" aria-hidden="true">{ic}</span><b>{title}</b>{sub}<span class="d">{desc}</span><span class="m">{meta}</span></a>')
    o.append('</div>')
    return '\n'.join(o)



# ---------- Product card slider（參考船P blog）----------
UP = P + '/wp-content/uploads/'
def sl(title, desc, items, btn_url, btn_text, cls=''):
    cards = ''.join(f'<a class="ao-scard{" fill" if len(it) > 4 else ""}" href="{P}{it[1]}" target="_blank" rel="noopener"><span class="im"><img src="{UP}{it[2]}" width="600" height="600" loading="lazy" alt="{it[0]}｜Kitchen AO 公司到會"></span><span class="ft"><span class="tx"><span class="nm">{it[0]}</span>' + (f'<span class="pr">{it[3]}</span>' if it[3] else '') + '</span><span class="buy">選購</span></span></a>' for it in items)
    return (f'<div class="ao-shelf{cls}"><p class="ao-shelf-t">{title}</p><p class="ao-shelf-d">{desc}</p>'
            f'<div class="ao-slwrap"><button type="button" class="ao-sl-btn prev" aria-label="上一個">‹</button><div class="ao-slider">{cards}</div>'
            f'<button type="button" class="ao-sl-btn next" aria-label="下一個">›</button></div></div>'
            f'<a class="ao-btn-gold" href="{P}{btn_url}" target="_blank" rel="noopener">{btn_text}</a>')
CB = '/product-category/商務活動/'
SETS = [
 ('商務餐盒', CB+'commercial-lunch-box/', '2025/04/CAB-Commercial-Meal-Lv2_頁面_1-1-724x1024-1.jpg', '每人一盒｜HK$108 起'),
 ('高級餐盒', CB+'executive-premium-meal-box/', '2025/04/螢幕截圖-2026-10-17-下午5.20.52.png', '會議及貴賓｜HK$248 起'),
 ('員工膳食餐盒 Staff Meal', CB+'staff-meal/', '2024/07/SM-Staff-Meal-Lv1-724x1024.jpg', '大量訂購'),
 ('皇家小食盒', CB+'royal-snackers-box/', '2025/04/Royal-Snacks-Box-768x543.jpg', '茶點及小休', 'fill'),
 ('舌尖上的餐桌九宮格 Canapés', CB+'a-bit-of-cuisines-gourmet-in-a-box/', '2025/04/WhatsApp-Image-2026-10-19-at-11.37.40-AM-768x542.jpeg', 'Event 及迎賓', 'fill'),
 ('美食派對 Gourmet 套餐', '/product-category/party/foot-party/', '2026/03/8-10_101-X-KITCHENAO-03-03-03-768x768.jpg', '8 至 85 人｜HK$1,988 起'),
 ('輕食宴會套餐 Refreshment', '/product-category/party/refreshment-set/', '2023/11/refreshmentparty-03-768x768.jpg', '12 至 40 人｜HK$2,688 起'),
 ('百人慶典派對到會套餐', '/product/ao100set/', '2025/04/WhatsApp-Image-2025-04-15-at-5.37.03-PM-768x512.jpeg', '100 人｜HK$13,800', 'fill'),
 ('「素」味人生素食套餐', '/product-category/party/vegetarians-set/', '2025/05/9ee996d5-e50c-4745-b847-86d8e179c481-600x600.jpg', '6 至 26 人｜HK$1,388 起'),
 ('肉食獸上將海港之選', '/product-category/party/meat-monster/', '2025/04/WhatsApp-Image-2025-04-14-at-6.13.46-PM-768x512.jpeg', '7 至 11 人｜HK$1,888 起', 'fill'),
 ('5 人自選拼盤', '/product/5-people-self-selected-platter/', '2023/10/KitchenAO_platter_thumbnail_工作區域-1-600x600-1.png', '小型聚會｜HK$498'),
]
PASTA = [
 ('「冩樂」清酒煮蟹皇灸燒左口魚醬油煲仔飯', '/product/ps01l「冩樂」清酒煮蟹皇灸燒左口魚醬油㷛仔飯-4磅/', '2026/03/WhatsApp-Image-2026-03-18-at-16.36.27-4-600x600.jpeg', ''),
 ('黑松露野菌蘆筍忌廉意粉', '/product/p03l-black-truffle-wild-mushroom-and-asparagus-cream-pasta-4-pounds/', '2023/10/cafcfef6-09ff-4233-be66-84dd307ea036-600x600.jpg', ''),
 ('黑椒牛柳絲韭菜花炒意粉', '/product/p22l-黑椒牛柳絲韭菜花炒意粉-4磅p22l-black-pepper-wagyu-strips-garlic-chive-blossom-spaghetti-4-pounds/', '2025/05/KitchenAO_DEC2023-ALA-CARTE-09-600x600.jpg', ''),
 ('爆炒 XO 醬蜆肉香蒜意大利麵', '/product/p04l-pan-fried-xo-sauce-clam-and-garlic-pasta-4-pounds/', '2019/06/Posts-27-scaled-600x600.jpg', ''),
 ('芝士腐乳卡邦尼長通粉', '/product/p07l-carbonara-penne-with-fermented-tofu-sauce-4-pounds/', '2019/06/Posts-03-scaled-600x600.jpg', ''),
 ('芝士焗特調肉醬蝴蝶粉', '/product/baked-chessy-farfalle-bolognese-4-pounds/', '2019/06/KitchenAO_JUN2023-ALA-CARTE-02-600x600.png', ''),
]
FINGER = [
 ('蠔油鮑汁野菌鮑魚酥', '/product/a3000-braised-abalone-vol-au-vent-with-mushrooms-in-oyster-sauce/', '2023/12/KitchenAO_DEC2023-ALA-CARTE-06-600x600.jpg', ''),
 ('照燒鰻魚日本蛋沙律牛油酥盒', '/product/a0400-japanese-eel-egg-salad-vol-au-vent/', '2019/06/Posts-15-1-scaled-600x600.jpg', ''),
 ('焗雙色芝士吞拿魚脆法包', '/product/a0100-baked-double-cheese-tuna-crostini/', '2019/06/Posts-06-scaled-600x600.jpg', ''),
 ('迷你芝士手打漢堡', '/product/a0700-handmade-mini-cheeseburger/', '2019/06/Posts-07-scaled-600x600.jpg', ''),
 ('懷舊芝麻蝦滑多士配泰汁', '/product/a3400-deep-fried-sesame-shrimp-toast-with-thai-sauce/', '2019/06/蝦多-03-600x600.jpg', ''),
 ('法式龍蝦汁燴蛋餃', '/product/a3300-french-egg-dumplings-in-lobster-sauce/', '2019/06/KitchenAO_DEC2023-ALA-CARTE_工作區域-1-2-600x600.jpg', ''),
]
SALAD = [
 ('油香煙三文魚特調凱撒沙律', '/product/s0300-smoked-salmon-caesar-salad/', '2019/06/Posts-17-scaled-600x600.jpg', ''),
 ('啖啖松葉蟹三文魚籽芒果沙律', '/product/s0200-snow-crabmeat-and-salmon-roe-mango-salad/', '2019/06/Posts-26-scaled-600x600.jpg', ''),
 ('照燒魷魚香橙紅酒醋沙律', '/product/s0400-teriyaki-squid-and-orange-salad-with-red-wine-vinegar-dressing/', '2019/06/Posts-20-scaled-600x600.jpg', ''),
 ('慢煮水嫩雞胸青蘋果西芹合桃沙律', '/product/s0500-slow-cooked-chicken-breast-apple-celery-and-walnut-salad/', '2019/06/Posts-08-scaled-600x600.jpg', ''),
 ('千島汁大蝦蜜桃沙律', '/product/shrimp-and-peach-salad-in-thousand-island-dressing/', '2019/06/KitchenAO_MAY2023-ALA-CARTE-06-600x600.png', ''),
]
HOT = [
 ('全隻西班牙脆嫩乳香乳豬', '/product/m0600-whole-spanish-style-crispy-suckling-pig-sliced-or-unsliced/', '2023/12/20221114_AOKitchen_-321-600x600.jpg', ''),
 ('自家製黑松露牛油慢焗法國黃油雞', '/product/m0315-homemade-black-truffle-butter-baked-cornish-hen-1-5-chickens/', '2019/06/Posts-21-scaled-600x600.jpg', ''),
 ('紅酒慢燴鮮蕃茄和牛牛肋條', '/product/m0240-red-wine-braised-fresh-tomato-and-wagyu-beef-short-ribs-4-pounds/', '2019/06/Posts-34-600x600-1.jpg', ''),
 ('「香港燒」烤燶邊香草蜜糖鹿兒島叉燒扒', '/product/m0140-roasted-kagoshima-pork-char-siu-with-herb-and-honey-glaze-4-pounds/', '2019/06/Posts-04-scaled-600x600.jpg', ''),
 ('蜜蜜糖德國鹹豬手', '/product/m0500-honey-glazed-german-salted-pork-knuckle-1-pcs/', '2019/06/Posts-25-scaled-600x600.jpg', ''),
 ('椰香咖哩海鮮龍脷柳配蒜蓉包', '/product/m07l-coconut-curry-seafood-sole-fillet-with-garlic-breads-4-pounds/', '2024/09/咖喱石班-03-600x600.jpg', ''),
]
SNACK = [
 ('蜜蜜燒雞翼配脆薯角', '/product/a0500-honey-glazed-chicken-wings-w-potato-wedges/', '2019/06/Posts-16-scaled-600x600.jpg', ''),
 ('日式雞皮餃子配酥炸洋蔥圈', '/product/a1600-japanese-chicken-skin-dumplings-with-crispy-onion-rings/', '2023/10/KitchenAO_MAY2023-ALA-CARTE-03-600x600.png', ''),
 ('香烤沙嗲串燒（豬雞）', '/product/a0200-grilled-satay-skewer-pork-and-chicken/', '2019/06/Posts-10-scaled-600x600.jpg', ''),
 ('避風塘炸海鮮豆腐配海鮮甜醬', '/product/a1500-crispy-seafood-tofu-in-traditional-typhoon-shelter-style/', '2019/06/KitchenAO_MAY2023-ALA-CARTE-04-600x600.png', ''),
 ('黑松露墨魚滑炸雲吞', '/product/a0600-fried-black-truffle-mashed-cuttlefish-wonton/', '2019/06/Posts-19-scaled-600x600.jpg', ''),
 ('上海古早炸饅頭配煉奶', '/product/a3800-shanghai-style-deep-fried-buns-with-condensed-milk/', '2019/06/KitchenAO_DEC2023-ALA-CARTE-06-2-600x600.jpg', ''),
 ('惹味蒜香焗茄子', '/product/a3900-grilled-garlic-eggplant/', '2019/06/KitchenAO_DEC2023-ALA-CARTE-02-2-600x600.jpg', ''),
]

# 共用菜式連結
def menu_lunch(lang):
    if lang == 'zh':
        return f'''<ul>
<li><strong>熱盤：</strong>{a("/product/m0500-honey-glazed-german-salted-pork-knuckle-1-pcs/", "蜜蜜糖德國鹹豬手")}、{a("/product/p03l-black-truffle-wild-mushroom-and-asparagus-cream-pasta-4-pounds/", "黑松露野菌蘆筍忌廉意粉")}</li>
<li><strong>小食：</strong>{a("/product/a0700-handmade-mini-cheeseburger/", "迷你芝士手打豬肉牛肉漢堡")}、{a("/product/a3400-deep-fried-sesame-shrimp-toast-with-thai-sauce/", "懷舊芝麻蝦滑多士")}、{a("/product/a1500-crispy-seafood-tofu-in-traditional-typhoon-shelter-style/", "避風塘炸海鮮豆腐")}</li>
<li><strong>沙律：</strong>{a("/product/s0300-smoked-salmon-caesar-salad/", "油香煙三文魚凱撒沙律")}</li>
</ul>'''
    return f'''<ul>
<li><strong>Hot dishes:</strong> {a("/product/m0500-honey-glazed-german-salted-pork-knuckle-1-pcs/", "Honey Glazed German Pork Knuckle")}, {a("/product/p03l-black-truffle-wild-mushroom-and-asparagus-cream-pasta-4-pounds/", "Black Truffle Wild Mushroom Asparagus Cream Pasta")}</li>
<li><strong>Snacks:</strong> {a("/product/a0700-handmade-mini-cheeseburger/", "Mini Hand-Pattied Cheese Burgers")}, {a("/product/a3400-deep-fried-sesame-shrimp-toast-with-thai-sauce/", "Sesame Shrimp Toast")}, {a("/product/a1500-crispy-seafood-tofu-in-traditional-typhoon-shelter-style/", "Typhoon Shelter Style Crispy Seafood Tofu")}</li>
<li><strong>Salad:</strong> {a("/product/s0300-smoked-salmon-caesar-salad/", "Smoked Salmon Signature Caesar Salad")}</li>
</ul>'''

def menu_dinner(lang):
    if lang == 'zh':
        return f'''<ul>
<li><strong>迎賓小食：</strong>{a("/product-category/商務活動/a-bit-of-cuisines-gourmet-in-a-box/", "舌尖上的餐桌九宮格 Canapés")}、{a("/product/a3000-braised-abalone-vol-au-vent-with-mushrooms-in-oyster-sauce/", "蠔油鮑汁野菌鮑魚酥")}</li>
<li><strong>主菜：</strong>{a("/product/m0315-homemade-black-truffle-butter-baked-cornish-hen-1-5-chickens/", "自家製黑松露牛油慢焗法國黃油雞")}、{a("/product/ps01l「冩樂」清酒煮蟹皇灸燒左口魚醬油㷛仔飯-4磅/", "清酒煮蟹皇灸燒左口魚醬油煲仔飯")}、{a("/product/m0500-honey-glazed-german-salted-pork-knuckle-1-pcs/", "蜜蜜糖德國鹹豬手")}</li>
<li><strong>甜品：</strong>{a("/product/d01-french-colorful-macarons-10-pieces/", "法式七彩馬卡龍")}、{a("/product/d06-caramel-tart-10個/", "焦糖葡撻")}</li>
</ul>'''
    return f'''<ul>
<li><strong>Welcome canapés:</strong> {a("/product-category/商務活動/a-bit-of-cuisines-gourmet-in-a-box/", "A Bit of Cuisines Canapé Box")}, {a("/product/a3000-braised-abalone-vol-au-vent-with-mushrooms-in-oyster-sauce/", "Braised Abalone Vol-au-vent with Mushrooms")}</li>
<li><strong>Mains:</strong> {a("/product/m0315-homemade-black-truffle-butter-baked-cornish-hen-1-5-chickens/", "Slow-roasted French Yellow Spring Chicken with Black Truffle Butter")}, {a("/product/ps01l「冩樂」清酒煮蟹皇灸燒左口魚醬油㷛仔飯-4磅/", "Sharaku Sake-Braised Crab Roe &amp; Seared Flounder Claypot Rice")}, {a("/product/m0500-honey-glazed-german-salted-pork-knuckle-1-pcs/", "Honey Glazed German Pork Knuckle")}</li>
<li><strong>Desserts:</strong> {a("/product/d01-french-colorful-macarons-10-pieces/", "French Rainbow Macarons")}, {a("/product/d06-caramel-tart-10個/", "Caramel Portuguese Tarts")}</li>
</ul>'''


# ---------------- 中文 ----------------
ZH_FAQ = [
    ('公司到會價錢是多少？', '按人數、菜式及送貨地區計算。參考價方面，員工午餐商務餐盒每位 HK$108 起，會議午餐高級餐盒每位 HK$248 起，會議茶點可選輕食宴會套餐（12 至 16 人 HK$2,688 起），年會、團年飯及公司聚會每位 HK$300 起。'),
    ('公司到會要提前多少日預訂？', '建議盡早預訂，尤其是 12 月至農曆新年的年會、春茗及團年飯旺季。所需日數視乎人數及菜式，可先透過 WhatsApp 向客服確認。'),
    ('會議可以只訂下午茶或茶點到會嗎？', '可以。會議中段的 Tea Break、下午茶或早餐會議，可選輕食宴會套餐、皇家小食盒或九宮格 Canapés，按人數及會議時間安排送達。'),
    ('公司春茗、團年飯及開年飯可以到會嗎？', '可以。年會、春茗、公司團年飯及開年飯到會一般以迎賓小食、熱盤主菜及甜品組成，每位 HK$300 起；2027 年農曆新年為 2 月 6 日，1 月至 2 月是旺季，建議盡早預訂。'),
    ('全日培訓或研討會可以一次過安排餐飲嗎？', '可以。全日培訓、研討會及工作坊可一次過安排早上茶點、午餐餐盒及下午茶，提供日程及人數後，客服會按時段配搭餐單。'),
    ('學校、醫院等機構可以訂到會嗎？', '可以。學校、醫院及社福機構的活動可按人數、場地及預算配搭餐盒、自助餐或小食拼盤，歡迎提供活動資料索取報價。'),
    ('公司到會有沒有素食選擇？', '有。請在查詢時說明素食人數及要求，例如是否需要全素或走五辛，客服會按要求安排菜單。'),
    ('怎樣預訂公司到會？', '可透過 WhatsApp 852-6901-1987、電郵 info@aoaodelivery.com，或填寫網站的到會報價查詢表格。'),
]
ZH_SCENES = [
    ('office-lunch', '🍱', '員工午餐', 'Office Lunch', '商務餐盒每人一盒，日常午餐及部門聚餐都適用', '10 至 100 人｜HK$108 起', ''),
    ('meeting', '☕', '會議餐飲', 'Breakfast, Lunch &amp; Tea Break', '早餐會議、會議午餐、下午茶及茶點', '10 至 100 人｜HK$248 起', ''),
    ('training', '📋', '培訓及研討會', 'Training, Seminar &amp; Workshop', '全日活動一次安排早上茶點、午餐及下午茶', '按日程報價', ''),
    ('annual-dinner', '🏆', '年會、春茗及團年飯', 'Annual Dinner &amp; Spring Dinner', '年會、頒獎晚宴、春茗、公司團年飯及開年飯', '50 至 200 人以上｜HK$300 起', '1 月至 2 月旺季'),
    ('festive', '🎉', '公司聚會及員工活動', 'Company Party &amp; Staff Events', 'Team Building、員工生日會、迎新歡送及家庭日', '30 至 300 人｜HK$300 起', ''),
    ('business-event', '🎤', 'Event 及 PR 活動', 'Launch, Press &amp; Brand Events', '產品發佈會、記者會、品牌活動及酒會', '20 至 200 人以上｜按餐單報價', ''),
    ('institutions', '🏫', '機構活動', 'Schools, Hospitals &amp; NGOs', '學校家長日、醫院員工午餐、社福機構講座', '按人數及形式報價', ''),
]
REFRESH = '/product-category/party/refreshment-set/'
C = '/product-category/商務活動/'
ZH = dict(
    intro=f'''<p>由每日的一盒午餐，到年尾的週年晚宴，公司活動的餐飲往往是同事最記得的細節。Kitchen AO 的<strong>香港公司到會</strong>服務，按人數及預算為企業及機構度身安排餐單，由 10 人部門午餐到 300 人公司聚會都可以配合，並設全港送貨。</p>
<h2>Kitchen AO 公司到會服務：由員工午餐到年會的一站式企業到會</h2>
<p>Kitchen AO 為企業及機構提供一站式公司到會服務（又稱企業到會），涵蓋七類活動：日常員工午餐、會議餐飲（早餐、午餐、下午茶及茶點）、全日培訓及研討會、年會、春茗及團年飯、公司聚會及員工活動、Event 及 PR 活動，以及學校、醫院及社福機構活動。</p>
<p>一張訂單可按活動需要，配搭不同的套餐及餐盒：每人一盒的餐盒方便派發，適合午餐、會議及培訓；分享式到會套餐以熱盤主菜、小食、沙律及甜品組成，適合年會、公司聚會及員工活動；Canapés 及 Finger Food 則適合 Event 及酒會等站立形式的場合。另有素食套餐照顧不同飲食需要。</p>
{sl("推薦套餐及餐盒", "由 1 人一盒到 100 人慶典，按人數及活動形式選擇。", SETS, "/product-category/party-set-by-people/", "按人數查看全部套餐")}
<p>以上套餐可再加配單點菜式，以及{a("/飲品及雞尾酒服務/", "飲品及雞尾酒服務")}、{a("/product-category/party-supplies/thin-crust-pizza/", "餐具及暖貼")}；大型活動亦可安排侍應服務。如需度身訂製餐單，歡迎提出。</p>
''',
    img_alt='Kitchen AO 團隊在公司活動現場準備到會食物',
    img_alt2='Kitchen AO 侍應在商務活動現場擺放自助餐到會餐點',
    nav_label='公司到會目錄',
    main_label='<span class="mk">ALL SERVICES</span>一站式企業到會',
    tab_hint='請選擇以下公司或企業到會活動',
    panes=[
        ('office-lunch', '員工午餐', f'''
<h2>員工午餐到會：Office Lunch 每位 HK$108 起</h2>
<p>員工午餐到會以每人一盒的餐盒為主，每位 HK$108 起，適合 10 至 100 人的日常午餐、部門聚餐及內部會議，準時送到，派發快捷，亦方便按人數增減。</p>
<h3>推薦餐盒及套餐</h3>
<ul>
<li>{a(C+"commercial-lunch-box/", "商務餐盒")}：每位 HK$108 起，多款主菜選擇，每人一盒</li>
<li>{a(C+"staff-meal/", "員工膳食餐盒")}：適合需要大量訂購的公司午餐</li>
<li>{a("/product-category/party/foot-party/", "美食派對 Gourmet 套餐")}：想以分享形式一齊食，8 至 10 人 HK$1,988 起</li>
<li>{a("/product-category/party/vegetarians-set/", "「素」味人生素食套餐")}：有同事吃素，可另加素食套餐，6 至 8 人 HK$1,388 起</li>
</ul>
<h3>加配意粉及意大利飯</h3>
{sl('意粉及意大利飯', '飽肚又方便分享，可配合餐盒一併送達。', PASTA, '/product-category/a-la-carte/pasta/', '查看全部意粉及意大利飯')}
<div class="ao-custom"><b>想度身訂製？</b>如需指定菜式、每日不同餐單或特別飲食要求（例如走五辛、無麩質），歡迎透過 {a("/catering-quote-enquiry/", "到會報價查詢")} 提出，客服會按人數及預算配搭。</div>
<p>客戶會議及董事會的午餐，可參考<a href="#meeting">會議餐飲</a>。</p>'''),
        ('meeting', '會議餐飲', f'''
<h2>會議餐飲：早餐會議、會議午餐、下午茶及茶點到會</h2>
<p>會議餐飲按時段可分為早餐、午餐及會議中段的茶點。Kitchen AO 可按會議時間安排送達：會議午餐每位 HK$248 起；下午茶及茶點到會可選輕食宴會套餐，12 至 16 人 HK$2,688 起。</p>
<h3>早餐會議 Breakfast Meeting</h3>
<p>早上會議或培訓開始前，可安排{a(C+"royal-snackers-box/", "皇家小食盒")}或小食拼盤，於會議開始前送達，方便與會者一邊交流一邊享用。</p>
<h3>會議午餐 Meeting Lunch：每位 HK$248 起</h3>
<p>適合 10 至 100 人的客戶會議、董事會及貴賓接待，可選{a(C+"executive-premium-meal-box/", "高級餐盒")}，菜式及包裝更講究，即使是一頓會議午餐，也能為公司形象加分。</p>
<h3>會議茶點及下午茶 Tea Break</h3>
<p>會議中段的 Tea Break 以一口大小的小食為主，取用方便，不會打斷會議節奏：</p>
<ul>
<li>{a(REFRESH, "輕食宴會套餐 Refreshment")}：12 至 40 人，12 至 16 人 HK$2,688 起，適合下午茶及茶點到會</li>
<li>{a(C+"royal-snackers-box/", "皇家小食盒")}：每人一盒，方便派發</li>
<li>{a(C+"a-bit-of-cuisines-gourmet-in-a-box/", "舌尖上的餐桌九宮格 Canapés")}：適合貴賓及客戶會議</li>
<li>{a("/product/5-people-self-selected-platter/", "5 人自選拼盤")}：小型會議，HK$498</li>
</ul>
<h3>加配精緻小食</h3>
{sl('精緻小食及酥盒', '一口大小、取用方便，適合會議中段的 Tea Break。', FINGER, '/product-category/a-la-carte/cold-cuts/', '查看全部冷盤小食')}
<p>甜品可加配{a("/product/d01-french-colorful-macarons-10-pieces/", "法式七彩馬卡龍")}或{a("/product/d06-caramel-tart-10個/", "焦糖葡撻")}；素食與會者可配{a("/product-category/party/vegetarians-set/", "「素」味人生素食套餐")}。</p>
<div class="ao-custom"><b>想度身訂製？</b>早餐菜式、茶點款式及份量，均可按會議人數及時段調整；如有特別要求，歡迎透過 {a("/catering-quote-enquiry/", "到會報價查詢")} 提出。</div>'''),
        ('training', '培訓及研討會', f'''
<h2>培訓、研討會及工作坊到會：全日活動餐飲一次安排</h2>
<p>全日培訓、研討會、講座及工作坊（Training Day、Seminar、Workshop），可一次過安排早上茶點、午餐及下午茶，由同一張訂單分時段送達，毋須分開訂購。提供日程及人數後，客服會按時段配搭餐單。</p>
<h3>推薦全日餐飲配搭</h3>
<div class="ao-tblwrap"><table>
<thead><tr><th>時段</th><th>建議安排</th><th>推薦套餐或餐盒</th></tr></thead>
<tbody>
<tr><td>早上（開始前）</td><td>茶點及飲品</td><td>{a(C+"royal-snackers-box/", "皇家小食盒")}</td></tr>
<tr><td>午餐</td><td>每人一盒，方便即場派發</td><td>{a(C+"commercial-lunch-box/", "商務餐盒")}或{a(C+"executive-premium-meal-box/", "高級餐盒")}</td></tr>
<tr><td>下午茶</td><td>一口小食，配合小休時間</td><td>{a(REFRESH, "輕食宴會套餐")}</td></tr>
</tbody></table></div>
<h3>加配新鮮沙律</h3>
{sl('新鮮沙律', '清爽開胃，適合配搭午餐餐盒，平衡全日的熱食。', SALAD, '/product-category/a-la-carte/salad/', '查看全部新鮮沙律')}
<p>有學員吃素，可另配{a("/product-category/party/vegetarians-set/", "「素」味人生素食套餐")}；亦可加配{a("/product-category/a-la-carte/dessert/", "甜品")}及{a("/product-category/a-la-carte/snacks/", "惹味小食")}單點。</p>
<div class="ao-custom"><b>想度身訂製？</b>連續多日的培訓，可按日更換菜式；如需配合場地限制或指定送達時間，歡迎透過 {a("/catering-quote-enquiry/", "到會報價查詢")} 提出。</div>
<p class="ao-note">建議提前確認場地擺放食物的位置及各時段的開始時間，以便安排送達。</p>'''),
        ('annual-dinner', '年會及團年飯', f'''
<h2>年會、春茗及團年飯到會：Annual Dinner、公司開年飯一次安排</h2>
<p>每年 12 月至農曆新年，是公司年會、頒獎晚宴、春茗（Spring Dinner）及團年飯最密集的時段。可按人數及形式，先選擇合適的到會套餐，再加配單點菜式，50 至 200 人以上的年會到會每位 HK$300 起。</p>
<h3>推薦年會套餐</h3>
<ul>
<li>{a("/product-category/party/foot-party/", "美食派對 Gourmet 套餐")}：熱盤主菜為主，8 至 85 人，適合團年飯及開年飯</li>
<li>{a(REFRESH, "輕食宴會套餐 Refreshment")}：一口小食為主，12 至 40 人，適合站立形式的年會及春茗酒會</li>
<li>{a("/product/ao100set/", "百人慶典派對到會套餐")}：100 人大型年會，HK$13,800</li>
<li>{a(C+"a-bit-of-cuisines-gourmet-in-a-box/", "舌尖上的餐桌九宮格 Canapés")}及{a(C+"royal-snackers-box/", "皇家小食盒")}：入場迎賓小食</li>
<li>{a("/product-category/party/vegetarians-set/", "「素」味人生素食套餐")}：照顧吃素的同事及嘉賓</li>
</ul>
<h3>加配熱盤主菜</h3>
{sl('熱盤主菜', '年會及團年飯的主角，以保溫包裝送達，開席即可上桌。', HOT, '/product-category/a-la-carte/meat/', '查看全部肉類熱盤')}
<p>甜品可加配{a("/product/d01-french-colorful-macarons-10-pieces/", "法式七彩馬卡龍")}或{a("/product/d06-caramel-tart-10個/", "焦糖葡撻")}，為晚宴作結。</p>
<h3>公司春茗、團年飯及開年飯：旺季宜早預訂</h3>
<p>2027 年農曆新年為 2 月 6 日，1 月至 2 月是公司團年飯、開年飯及春茗到會的高峰，熱門日子名額有限，建議盡早預訂。</p>
<div class="ao-custom"><b>想度身訂製？</b>可加入中式菜式、按主題配搭擺盤，或安排侍應服務及{a("/飲品及雞尾酒服務/", "飲品及雞尾酒服務")}。人數較多的年會，宜先確定開席時間及場地擺放食物的空間，再透過 {a("/catering-quote-enquiry/", "到會報價查詢")} 提出要求。</div>'''),
        ('festive', '公司聚會', f'''
<h2>公司聚會及員工活動到會：Company Party、Team Building 及員工慶祝</h2>
<p>公司聚會及員工活動（Company Party &amp; Staff Events）到會多採用自助餐形式，賓客可隨意取用，適合 30 至 300 人，每位 HK$300 起。</p>
<h3>推薦聚會套餐</h3>
<ul>
<li>{a("/product-category/party/foot-party/", "美食派對 Gourmet 套餐")}：按人數由 8 人至 85 人選擇，適合 Team Building 及公司派對</li>
<li>{a(REFRESH, "輕食宴會套餐 Refreshment")}：一口小食為主，適合邊玩邊食的活動</li>
<li>{a("/product-category/party/meat-monster/", "肉食獸上將海港之選")}：7 至 11 人，肉類盛盒</li>
<li>{a("/product-category/party/vegetarians-set/", "「素」味人生素食套餐")}：6 至 26 人，照顧吃素的同事</li>
</ul>
<h3>員工活動：生日會、迎新、歡送及慶功</h3>
<p>每月員工生日會、新同事迎新、同事歡送會及項目慶功，人數較少，可選{a("/product-category/party-set-by-people/", "人數選餐")}的小型套餐或{a("/product/5-people-self-selected-platter/", "5 人自選拼盤")}，再加配{a("/product-category/a-la-carte/dessert/", "甜品")}作慶祝。</p>
<h3>公司家庭日及開放日</h3>
<p>家庭日及開放日有不少小朋友參與，可配搭{a("/product-category/party/children/", "兒童套餐")}及容易取用的小食，照顧大人及小朋友的口味。</p>
<h3>加配惹味小食</h3>
{sl('惹味小食', '熱食小食最受歡迎，適合邊玩邊食的 Team Building 及派對。', SNACK, '/product-category/a-la-carte/snacks/', '查看全部惹味小食')}
<p>12 月的公司聖誕派對，可參考{a("/blog/christmas-catering-hong-kong/", "聖誕到會套餐")}。</p>
<div class="ao-custom"><b>想度身訂製？</b>生日會、迎新及慶功可加入{a("/blog/laser-printed-food-party/", "激光打印食物")}，把公司 Logo 或祝福字句印在食物上；亦可訂製{a("/客製化紀念品訂製服務/", "客製化紀念品")}。歡迎透過 {a("/catering-quote-enquiry/", "到會報價查詢")} 提出。</div>'''),
        ('business-event', 'Event 及 PR 活動', f'''
<h2>Event 及 PR 活動到會：產品發佈會、記者會及品牌活動</h2>
<p>產品發佈會、記者會、傳媒活動、品牌活動及 Pop-up 開幕（Product Launch、Press Event、Brand Event），多以站立形式進行，賓客邊走邊交流，一口一件的 Canapés 及 Finger Food 最合適。這類活動適合 20 至 200 人以上，價錢按餐單報價。</p>
<h3>推薦活動套餐及小食盒</h3>
<ul>
<li>{a(C+"a-bit-of-cuisines-gourmet-in-a-box/", "舌尖上的餐桌九宮格 Canapés")}：每人一盒，適合傳媒及嘉賓</li>
<li>{a(C+"royal-snackers-box/", "皇家小食盒")}：方便即場派發</li>
<li>{a(REFRESH, "輕食宴會套餐 Refreshment")}：12 至 40 人，自助形式擺放</li>
</ul>
<h3>加配單點及飲品</h3>
<p>可加配{a("/product-category/a-la-carte/snacks/", "惹味小食")}、{a("/product-category/a-la-carte/dessert/", "甜品")}，以及{a("/飲品及雞尾酒服務/", "飲品及雞尾酒服務")}。</p>
<div class="ao-custom"><b>想度身訂製？</b>可按品牌主題配搭擺盤，或以{a("/blog/laser-printed-food-party/", "激光打印")}把品牌 Logo 印在食物上，配合拍照及傳媒報道。酒會、開張及其他商務活動，詳情可參考{a("/business-event/", "商務活動")}。</div>'''),
        ('institutions', '機構活動', f'''
<h2>機構活動到會：學校、醫院及社福機構（Schools, Hospitals &amp; NGOs）</h2>
<p>除了企業，學校、醫院、診所、社福機構及政府部門亦經常需要到會。這類活動的人數、時間及場地各有不同，可先選擇合適的套餐或餐盒，再按需要加配：</p>
<h3>學校到會：家長日、開放日、畢業禮及教職員聚餐</h3>
<p>學校活動可選{a("/product-category/party/foot-party/", "美食派對 Gourmet 套餐")}、{a(REFRESH, "輕食宴會套餐")}或{a("/product/5-people-self-selected-platter/", "5 人自選拼盤")}；有小朋友參與的活動，可加配{a("/product-category/party/children/", "兒童套餐")}。12 月是學校活動及教職員聚餐的高峰，建議提早查詢。</p>
<h3>醫院、社福機構及政府部門</h3>
<ul>
<li><strong>醫院及診所：</strong>員工午餐及答謝活動，可選{a(C+"commercial-lunch-box/", "商務餐盒")}或{a(C+"staff-meal/", "員工膳食餐盒")}，每人一盒方便分派。</li>
<li><strong>社福機構及政府部門：</strong>講座、工作坊及義工活動，可選{a(C+"royal-snackers-box/", "皇家小食盒")}或小食拼盤。</li>
<li><strong>素食需要：</strong>可配{a("/product-category/party/vegetarians-set/", "「素」味人生素食套餐")}。</li>
</ul>
<div class="ao-custom"><b>想度身訂製？</b>可按機構預算、採購要求及單據安排配搭餐單；歡迎填寫 {a("/catering-quote-enquiry/", "到會報價查詢")}，提供活動日期、人數及預算。</div>'''),
        ('price', '價錢及流程', f'''
<h2>公司到會價錢怎樣計算？四個預算例子</h2>
<p>公司到會的價錢主要由人數、菜式及送貨地區決定。以下例子可作初步預算參考：</p>
<div class="ao-tblwrap"><table>
<thead><tr><th>服務</th><th>人數</th><th>每位參考價</th><th>總預算例子</th><th>特色</th></tr></thead>
<tbody>
<tr><td>員工午餐（商務餐盒）</td><td>20 人</td><td>HK$108</td><td>HK$2,160</td><td>每人一盒，方便分派</td></tr>
<tr><td>會議午餐（高級餐盒）</td><td>20 人</td><td>HK$248</td><td>HK$4,960</td><td>適合會議及貴賓接待</td></tr>
<tr><td>年會、春茗及團年飯</td><td>80 人</td><td>HK$300</td><td>HK$24,000</td><td>熱盤主菜</td></tr>
<tr><td>公司聚會及員工活動</td><td>50 人</td><td>HK$300</td><td>HK$15,000</td><td>自助餐及小食</td></tr>
</tbody></table></div>
<p class="ao-note">運費按送貨地區計算；單一訂單滿 HK$1,450 全港免運費，詳情見{a("/delivery/", "送貨需知")}。</p>
<h2 id="process">公司到會預訂流程：四步完成</h2>
<ol>
<li><strong>提供資料：</strong>人數、日期、送達時間、地址、預算及特別飲食要求。</li>
<li><strong>收取餐單及報價：</strong>客服按資料提供建議餐單。</li>
<li><strong>確認訂單及付款：</strong>可使用轉數快或 PayMe 等方式付款。</li>
<li><strong>活動當日：</strong>按約定時間送達。</li>
</ol>
<p>船河及戶外活動另行報價。可以直接填寫{a("/catering-quote-enquiry/", "到會報價查詢")}，或參考我們的{a("/合作伙伴/", "合作夥伴與服務實績")}。</p>'''),
        ('faq', '常見問題', '<h2>公司到會常見問題</h2>\n' + faq_html(ZH_FAQ)),
    ],
    summary=f'''
<h3>人數及預算一覽</h3>
<div class="ao-tblwrap"><table>
<thead><tr><th>服務</th><th>人數</th><th>到會形式</th><th>參考價</th></tr></thead>
<tbody>
<tr><td>員工午餐 Office Lunch</td><td>10 至 100 人</td><td>{a("/product-category/商務活動/commercial-lunch-box/", "商務餐盒")}</td><td>每位 HK$108 起</td></tr>
<tr><td>會議午餐 Meeting Lunch</td><td>10 至 100 人</td><td>{a("/product-category/商務活動/executive-premium-meal-box/", "高級餐盒")}</td><td>每位 HK$248 起</td></tr>
<tr><td>會議茶點及下午茶 Tea Break</td><td>12 人起</td><td>{a(REFRESH, "輕食宴會套餐")}、小食盒</td><td>12 至 16 人 HK$2,688 起</td></tr>
<tr><td>培訓及研討會（全日）</td><td>按活動而定</td><td>早上茶點、午餐、下午茶</td><td>按日程報價</td></tr>
<tr><td>年會、春茗及團年飯</td><td>50 至 200 人以上</td><td>迎賓小食、熱盤主菜、甜品</td><td>每位 HK$300 起</td></tr>
<tr><td>公司聚會及員工活動</td><td>30 至 300 人</td><td>自助餐式到會套餐</td><td>每位 HK$300 起</td></tr>
<tr><td>Event 及 PR 活動</td><td>20 至 200 人以上</td><td>Canapés、Finger Food</td><td>按餐單報價</td></tr>
<tr><td>機構活動 Schools &amp; NGOs</td><td>按活動而定</td><td>餐盒、自助餐或小食拼盤</td><td>按人數及形式報價</td></tr>
</tbody></table></div>
<p class="ao-note">以上為參考價，實際價錢按人數、菜式及送貨地區計算。</p>
<h3>企業及機構選擇 Kitchen AO 公司到會服務的四個原因</h3>
<ul>
<li><strong>菜單跟著活動走：</strong>中西菜式自由配搭，並設素食及無麩質選擇，照顧不同同事的飲食需要。</li>
<li><strong>人數可多可少：</strong>由 10 人部門午餐到 300 人公司聚會，份量都可以按人數調整。</li>
<li><strong>熱盤保持溫度：</strong>熱盤以保溫包裝送達，活動一開始即可上桌。</li>
<li><strong>報價清楚直接：</strong>提供人數、日期及預算，客服便會提供餐單、價錢及送貨安排。</li>
</ul>''',
    faq=ZH_FAQ,
    service={"@context": "https://schema.org", "@type": "Service", "serviceType": "公司到會", "name": "Kitchen AO 香港公司到會", "areaServed": {"@type": "Place", "name": "香港"}, "provider": {"@type": "Organization", "name": "Kitchen AO", "url": "https://aoaodelivery.com/"}, "url": "https://aoaodelivery.com/corporate-catering-hk/"},
    cta=f'<div class="ao-cta"><a class="alt" href="{P}/catering-quote-enquiry/">到會報價查詢</a><a href="{WA}?text=%E5%85%AC%E5%8F%B8%E5%88%B0%E6%9C%83%E6%9F%A5%E8%A9%A2" target="_blank" rel="noopener">WhatsApp 查詢公司到會</a></div>',
    updated='<p class="ao-note">最後更新：2026 年 10 月</p>',
)

# ---------------- English ----------------
EN_FAQ = [
    ('How much does corporate catering cost?', 'It depends on headcount, menu and delivery area. As a reference, office lunch commercial lunch boxes start from HK$108 per person, meeting lunch executive meal boxes from HK$248 per person, and annual dinners, year-end dinners and company gatherings from HK$300 per person.'),
    ('How far in advance should I book corporate catering?', 'We recommend booking as early as possible, especially during the busy company event season from December to Chinese New Year. The lead time depends on headcount and menu, so please check with our team on WhatsApp first.'),
    ('Do you cater year-end dinners and spring dinners?', 'Yes. Annual dinners, year-end dinners and Chinese New Year spring dinners usually include welcome canapés, hot mains and desserts, from HK$300 per person. December to February is peak season, so we recommend booking early.'),
    ('Can schools, hospitals and NGOs order catering?', 'Yes. For school, hospital and NGO events, we can arrange meal boxes, buffets or snack platters to suit your headcount, venue and budget. Send us your event details for a quotation.'),
    ('Do you offer vegetarian options for corporate catering?', 'Yes. Tell us how many vegetarian guests you have and their requirements, such as vegan or no five pungent spices, and we will arrange the menu accordingly.'),
    ('What budget do I need for annual dinner catering?', 'From HK$300 per person, annual dinner catering for 100 guests costs about HK$30,000, including welcome canapés, mains and desserts.'),
    ('How do I book corporate catering?', 'Contact us on WhatsApp at 852-6901-1987, email info@aoaodelivery.com, or fill in the catering quote enquiry form on our website.'),
]
EN_SCENES = [
    ('office-lunch', '🍱', 'Office Lunch', '', 'One commercial lunch box per person for everyday lunches, training and overtime meals', '10 to 100 guests | from HK$108', ''),
    ('office-lunch', '💼', 'Meeting &amp; Company Lunch', '', 'Executive meal boxes with a refined touch for client meetings, board meetings and VIP guests', '10 to 100 guests | from HK$248', ''),
    ('annual-dinner', '🏆', 'Annual Dinner &amp; Year-end Dinner', '', 'Annual dinners, awards nights, year-end dinners and spring dinners', '50 to 200+ guests | from HK$300', 'Dec to Feb peak'),
    ('festive', '🎉', 'Company Party &amp; Team Building', '', 'Help-yourself buffets for team building and office Christmas parties', '30 to 300 guests | from HK$300', ''),
    ('business-event', '🥂', 'Reception &amp; Grand Opening', '', 'Bite-sized canapés and finger food that keep guests mingling', '20 to 200+ guests | quoted by menu', ''),
    ('institutions', '🏫', 'Schools, Hospitals &amp; NGOs', '', 'School open days, hospital staff lunches, NGO talks and workshops', 'Quoted by headcount and format', ''),
]
EN = dict(
    intro='<p>From the daily lunch box to the year-end annual dinner, the food is often what colleagues remember most about a company event. Kitchen AO provides <strong>corporate catering in Hong Kong</strong> for companies and organisations, with menus tailored to your headcount and budget, from a 10-person department lunch to a company gathering of 300, with delivery across Hong Kong.</p>',
    img_alt='Kitchen AO team preparing corporate catering at a company event in Hong Kong',
    img_alt2='Kitchen AO staff setting up a catering buffet at a business event',
    nav_label='Corporate catering contents',
    panes=[
        ('overview', 'Overview', f'''
<h2>Our Corporate Catering Services in Hong Kong: Six Solutions for Companies and Organisations</h2>
<p>As a Hong Kong catering company, Kitchen AO offers one-stop corporate catering services. From everyday office lunches, client meeting lunches, annual dinners and year-end dinners to company parties, grand openings and events for schools, hospitals and NGOs, we have meal boxes, catering sets and canapés for every occasion, tailored to your headcount and budget, with delivery across Hong Kong. Tap a card to see each service:</p>
{scene(EN_SCENES)}
<h3>Headcount and Budget at a Glance</h3>
<div class="ao-tblwrap"><table>
<thead><tr><th>Service</th><th>Guests</th><th>Catering format</th><th>Reference price per person</th></tr></thead>
<tbody>
<tr><td>Office Lunch</td><td>10 to 100</td><td>{a("/product-category/商務活動/commercial-lunch-box/", "Commercial Lunch Box")}</td><td>From HK$108</td></tr>
<tr><td>Meeting &amp; Company Lunch</td><td>10 to 100</td><td>{a("/product-category/商務活動/executive-premium-meal-box/", "Executive Premium Meal Box")}</td><td>From HK$248</td></tr>
<tr><td>Annual Dinner &amp; Year-end Dinner</td><td>50 to 200+</td><td>Welcome canapés, hot mains, desserts</td><td>From HK$300</td></tr>
<tr><td>Company Party &amp; Team Building</td><td>30 to 300</td><td>Buffet-style catering sets</td><td>From HK$300</td></tr>
<tr><td>Reception &amp; Grand Opening</td><td>20 to 200+</td><td>Canapés and finger food</td><td>Quoted by menu</td></tr>
<tr><td>Schools, Hospitals &amp; NGOs</td><td>Varies by event</td><td>Meal boxes, buffets or snack platters</td><td>Quoted by headcount and format</td></tr>
</tbody></table></div>
<p class="ao-note">Reference prices only. Final prices depend on headcount, menu and delivery area.</p>
<h3>Four Reasons Companies and Organisations Choose Kitchen AO</h3>
<ul>
<li><strong>Menus that fit the occasion:</strong> Mix Chinese and Western dishes, with vegetarian and gluten-free options for colleagues with dietary needs.</li>
<li><strong>Any headcount:</strong> From a 10-person department lunch to a company gathering of 300, portions are adjusted to your numbers.</li>
<li><strong>Hot food, served hot:</strong> Hot dishes arrive in insulated packaging, ready to serve as soon as your event begins.</li>
<li><strong>Straightforward quotes:</strong> Share your headcount, date and budget, and our team will send a menu, price and delivery plan.</li>
</ul>'''),
        ('office-lunch', 'Office Lunch', f'''
<h2>Office Lunch Catering: Office Lunch and Meeting Lunch</h2>
<p>Office catering in Hong Kong may look simple, but the details matter. Everyday staff lunches need to arrive on time and be easy to hand out, while a lunch served at a client meeting reflects how your company treats its guests. That is why office lunch catering comes in two forms:</p>
<h3>Office Lunch: Commercial Lunch Box from HK$108</h3>
<p>For everyday lunches, in-house training and overtime meals of 10 to 100 people. One box per person makes distribution quick and lets you adjust numbers easily. See our {a("/product-category/商務活動/commercial-lunch-box/", "Commercial Lunch Box")} range, or the {a("/product-category/商務活動/staff-meal/", "Staff Meal Box")}.</p>
<h3>Meeting &amp; Company Lunch: Executive Premium Meal Box from HK$248</h3>
<p>For client meetings, board meetings and VIP guests of 10 to 100 people. More refined dishes and packaging mean even a working lunch leaves a good impression. See our {a("/product-category/商務活動/executive-premium-meal-box/", "Executive Premium Meal Box")}.</p>
<h3>Want More? Add Hot Dishes and Snacks</h3>
{menu_lunch('en')}
<p>To order by headcount in one go, see our {a("/product-category/party-set-by-people/", "party sets by number of guests")}.</p>'''),
        ('annual-dinner', 'Annual Dinner', f'''
<h2>Annual Dinner and Year-end Dinner Catering: Annual Dinners, Year-end Dinners and Spring Dinners</h2>
<p>December to Chinese New Year is the busiest time for company dinners in Hong Kong. Whether it is an annual dinner or awards night at year end, a company year-end dinner, or a spring dinner after Chinese New Year, the catering usually comes in three parts: welcome canapés as guests arrive, hot mains once dinner begins, and desserts to close the evening. This suits annual dinner catering for 50 to 200+ guests, from HK$300 per person. Sample dishes:</p>
{menu_dinner('en')}
<h3>Year-end and Spring Dinners: Book Early for Peak Season</h3>
<p>December to February is peak season, with enquiries rising for year-end dinners and spring dinners. Popular dates fill up quickly, so we recommend booking early. If you would like to add Chinese dishes, just let us know when you enquire.</p>
<h3>Planning an Annual Dinner in Hong Kong: A Catering Checklist</h3>
<p>If you are the annual dinner planner for your company, sort out the catering early so the rest of the evening runs smoothly:</p>
<ul>
<li><strong>Headcount and budget:</strong> confirm guest numbers and budget per person first. Our annual dinner menus start from HK$300 per person.</li>
<li><strong>Venue and set-up space:</strong> check how much space the venue has for setting up the food, and whether guests will be seated or standing.</li>
<li><strong>Timing:</strong> fix the start time of dinner, then arrange the delivery time around it.</li>
<li><strong>Dietary needs:</strong> collect vegetarian and other dietary requirements in advance.</li>
<li><strong>Service staff:</strong> if you need staff on site, let us know when you enquire.</li>
</ul>'''),
        ('festive', 'Company Party', f'''
<h2>Company Party Catering: Team Building and Office Christmas Parties</h2>
<p>Company party catering is usually served as a buffet so guests can help themselves, ideal for team building, product launches, staff birthday parties and office Christmas parties of 30 to 300 guests, from HK$300 per person.</p>
<ul>
<li><strong>Sample buffet dishes:</strong> {a("/product/a1600-japanese-chicken-skin-dumplings-with-crispy-onion-rings/", "Japanese Chicken Skin Dumplings with Crispy Onion Rings")}, {a("/product/a3000-braised-abalone-vol-au-vent-with-mushrooms-in-oyster-sauce/", "Braised Abalone &amp; Wild Mushroom Puff Pastry")}, {a("/product/a0200-grilled-satay-skewer-pork-and-chicken/", "Grilled Satay Skewers")}</li>
<li><strong>Catering sets:</strong> {a("/product-category/party/foot-party/", "Gourmet party sets")} for 5 to 85 guests</li>
</ul>'''),
        ('business-event', 'Receptions', f'''
<h2>Reception and Grand Opening Catering: Receptions, Openings and Product Launches</h2>
<p>Receptions and grand openings are usually standing events where guests mingle as they eat, so bite-sized canapés and finger food work best: easy to pick up, and they never interrupt a conversation. These events suit 20 to 200+ guests and are quoted by menu. See our {a("/business-event/", "event catering")} page, or choose the {a("/product-category/商務活動/a-bit-of-cuisines-gourmet-in-a-box/", "Nine Delights Gourmet Canapés Box")} and {a("/product-category/商務活動/royal-snackers-box/", "Royal Snackers Box")}.</p>'''),
        ('institutions', 'Schools &amp; NGOs', f'''
<h2>Catering for Schools, Hospitals and NGOs</h2>
<p>Besides companies, schools, hospitals, clinics, NGOs and government departments often need catering too. Headcount, timing and venue vary from event to event, so Kitchen AO can arrange meal boxes, buffets or snack platters to suit:</p>
<ul>
<li><strong>Schools:</strong> parents' days, open days, graduation ceremonies and staff gatherings, with buffets or snack platters.</li>
<li><strong>Hospitals and clinics:</strong> staff lunches, shift meals and appreciation events, with a {a("/product-category/商務活動/commercial-lunch-box/", "Commercial Lunch Box")} or {a("/product-category/商務活動/staff-meal/", "Staff Meal Box")}, one per person for easy distribution.</li>
<li><strong>NGOs and government departments:</strong> talks, workshops and volunteer events, with snack platters or the {a("/product-category/商務活動/royal-snackers-box/", "Royal Snackers Box")}.</li>
</ul>
<p>If your organisation has procurement or documentation requirements, please let us know when you enquire. Fill in our {a("/catering-quote-enquiry/", "catering quote enquiry")} form with your event date, headcount and budget.</p>'''),
        ('price', 'Prices &amp; Booking', f'''
<h2>How Much Does Corporate Catering Cost in Hong Kong? Four Budget Examples</h2>
<p>Corporate catering prices depend mainly on headcount, menu and delivery area. Use these examples as a starting point for your budget:</p>
<div class="ao-tblwrap"><table>
<thead><tr><th>Service</th><th>Guests</th><th>Reference price per person</th><th>Total budget (example)</th><th>Highlights</th></tr></thead>
<tbody>
<tr><td>Office Lunch (Commercial Lunch Box)</td><td>20</td><td>HK$108</td><td>HK$2,160</td><td>One box per person, easy to hand out</td></tr>
<tr><td>Meeting Lunch (Executive Premium Meal Box)</td><td>20</td><td>HK$248</td><td>HK$4,960</td><td>For meetings and VIP guests</td></tr>
<tr><td>Annual Dinner &amp; Year-end Dinner</td><td>80</td><td>HK$300</td><td>HK$24,000</td><td>Hot mains</td></tr>
<tr><td>Company Party &amp; Team Building</td><td>50</td><td>HK$300</td><td>HK$15,000</td><td>Buffet and snacks</td></tr>
</tbody></table></div>
<p class="ao-note">Delivery fees depend on the delivery area. Orders of HK$1,450 or more get free delivery across Hong Kong. See {a("/delivery/", "Delivery Info")} for details.</p>
<h2 id="process">How to Book Corporate Catering in Four Steps</h2>
<ol>
<li><strong>Send us your details:</strong> headcount, date, delivery time, address, budget and any dietary requirements.</li>
<li><strong>Receive a menu and quotation:</strong> our team will suggest a menu based on your details.</li>
<li><strong>Confirm and pay:</strong> payment methods include FPS and PayMe.</li>
<li><strong>On the day:</strong> delivery at the agreed time.</li>
</ol>
<p>Boat parties and outdoor events are quoted separately. Fill in our {a("/catering-quote-enquiry/", "catering quote enquiry")} form, or see our {a("/合作伙伴/", "partners and service records")}.</p>'''),
        ('faq', 'FAQ', '<h2>Corporate Catering FAQ</h2>\n' + faq_html(EN_FAQ)),
    ],
    faq=EN_FAQ,
    service={"@context": "https://schema.org", "@type": "Service", "serviceType": "Corporate catering", "name": "Kitchen AO Corporate Catering Hong Kong", "areaServed": {"@type": "Place", "name": "Hong Kong"}, "provider": {"@type": "Organization", "name": "Kitchen AO", "url": "https://aoaodelivery.com/"}, "url": "https://aoaodelivery.com/en/corporate-catering-hk/"},
    cta=f'<div class="ao-cta"><a class="alt" href="{P}/catering-quote-enquiry/">Get a Catering Quote</a><a href="{WA}?text=Corporate%20catering%20enquiry" target="_blank" rel="noopener">WhatsApp Us</a></div>',
    updated='<p class="ao-note">Last updated: October 2026</p>',
)

if __name__ == '__main__':
    open(os.path.join(HERE, 'zh-rawhtml.html'), 'w', encoding='utf-8').write(build(ZH))
    open(os.path.join(HERE, 'en-rawhtml.html'), 'w', encoding='utf-8').write(build(EN))
    print('ok')
