BAT='<svg viewBox="0 0 100 44"><path d="M50 18 L53 9 L55.5 17 C62 12 78 6 97 10 C89 14 85 20 87 27 C81 22 75 22 71 29 C67 24 61 24 57.5 31 C55 29 52.5 33 50 38 C47.5 33 45 29 42.5 31 C39 24 33 24 29 29 C25 22 19 22 13 27 C15 20 11 14 3 10 C22 6 38 12 44.5 17 L47 9 Z" fill="#2a0d3d"/><circle cx="47.6" cy="20" r="1.6" fill="#FFE14D"/><circle cx="52.4" cy="20" r="1.6" fill="#FFE14D"/></svg>'
BATS='<span class="ao-hw-bats" aria-hidden="true"><i class="b1">%s</i><i class="b2">%s</i><i class="b3">%s</i></span>'%(BAT,BAT,BAT)
CAT='https://aoaodelivery.com/product-category/halloween-set/'
UP='https://aoaodelivery.com/wp-content/uploads/2026/10/'
def cta(label,ref,txt):
    return f'<a class="ao-hw-cta" href="{CAT}?ao_ref=hw26_blog_{ref}" onclick="window.dataLayer=window.dataLayer||[];dataLayer.push({{event:\'cta_click\',cta_label:\'{label}\'}});">{BATS}<span class="ao-hw-txt">{txt}</span></a>'
DISH=[
 ('2026-halloween-story-_post-2-scaled.jpg','🎃','哈囉喂','日本南瓜海鮮意大利飯（原個直送）','原個日本南瓜做器皿直送到會，南瓜蓉融入每粒米飯，配彈牙海鮮，打卡同味道一樣出色。'),
 ('2026-halloween-story-_post-3-scaled.jpg','👁️','惡魔的眼睛','開心果醬荔枝藍苺酥盒','牛油酥盒釀入開心果醬，再以荔枝同藍莓砌成一隻隻「惡魔眼睛」，甜而不膩，一口一件最啱派對。'),
 ('2026-halloween-story-_post-1-scaled.jpg','🩸','血淋淋科學怪人','香濃蕃茄手指腸仔','似足「斷指」嘅腸仔，淋上香濃蕃茄醬營造血淋淋效果，嚇人得嚟又惹味，小朋友最搶手。'),
 ('2025-Halloween-burger-1-600x750.jpg','🍔','萬聖節','迷你芝士手打牛肉漢堡','手打牛肉配半溶芝士，換上萬聖節造型新裝，迷你尺寸方便拎住食，大人細路都啱。'),
 ('2026-halloween-story-_post-4-scaled.jpg','🦇','小蝙蝠','墨汁雞全翼','以墨汁染成漆黑嘅雞全翼，外層香脆、內裏嫩滑多汁，係枱面上最搶眼嘅「小蝙蝠」。'),
]
cards=''.join(f'''
<div class="ao-menucard{' ao-menucard--hero' if n==0 else ''}">
<div class="ph"><img loading="lazy" decoding="async" src="{UP}{img}" alt="{a}{b} — KitchenAO 2026 萬聖節到會"></div>
<div class="body">{'<span class="ao-hw-bigico" aria-hidden="true">'+ic+'</span><span class="ao-hw-must">今年主打</span>' if n==0 else ''}<p class="name">{'' if n==0 else '<span class="ic">'+ic+'</span>'}<small>{a}</small>{b}</p><p class="desc">{d}</p></div>
</div>''' for n,(img,ic,a,b,d) in enumerate(DISH))
SETS=[('5-6','133800','ao-5-6pax'),('8-10','191800','ao-8-10pax'),('12-16','288800','ao-12-16pax'),('18-22','375800','ao-18-22pax'),('26-30','500800','ao-26-30pax'),('35-40','655800','ao-35-40pax')]
SLUG='-halloween%e8%90%ac%e8%81%96%e7%af%80%e7%8b%82%e5%98%a9%e5%a5%97%e9%a4%90/'
sets=''.join(f'<a class="ao-hw-set" href="https://aoaodelivery.com/product/{s}{SLUG}?ao_ref=hw26_blog_set{p.replace("-","_")}" onclick="window.dataLayer=window.dataLayer||[];dataLayer.push({{event:\'cta_click\',cta_label:\'hw_blog_set_{p}\'}});"><b>{p}<small>人</small></b><span>${int(pr)//100:,}</span><i>查看 →</i></a>' for p,pr,s in SETS)

CSS=open('style.css').read()
HTML=f'''<div class="ao-article ao-hw26">
<style>
{CSS}
</style>

<a class="ao-hw-kvlink" href="{CAT}?ao_ref=hw26_blog_kv" onclick="window.dataLayer=window.dataLayer||[];dataLayer.push({{event:'cta_click',cta_label:'hw_blog_kv'}});"><img class="ao-hw-kv" src="{UP}2025-Halloween-banner-1_banner_banner-1536x717.jpg" width="1536" height="717" alt="KitchenAO Halloween 萬聖節狂嘩套餐 2026 到會" fetchpriority="high" decoding="async"></a>

<div class="ao-hw-ticket">
<div class="ao-hw-t1"><span class="ao-hw-dot"></span>即日接受訂購</div>
<div class="ao-hw-t2"><small>送貨日期</small><b><span>10月23日</span> – <span>11月1日</span></b></div>
</div>

<div class="ao-introcard">
<p class="ao-q">🎃 想搞一場全場尖叫嘅萬聖節派對？</p>
<p class="ao-intro">「Trick or Treat！」KitchenAO <strong>2026 年 Halloween 萬聖節狂嘩套餐</strong>正式登場！今年推出 <strong>5 款全新搞鬼主打菜式</strong>，由「惡魔的眼睛」酥盒到原個日本南瓜海鮮意大利飯，<strong>5 人至 40 人</strong>都有合適套餐，全港送遞，屋企派對、朋友聚會、公司 Halloween Party 一樣咁啱。</p>
</div>

<div class="ao-hw-terms">
<p class="ao-hw-terms-t">👻 2026 萬聖節優惠</p>
<ul>
<li><b>10 月 22 日前預訂</b>・即享 <b>92 折</b></li>
<li>各區<b>免費送遞</b>（滿 $1,450）</li>
<li>可使用會員優惠現金券，但其他優惠碼不適用</li>
</ul>
</div>

<div class="ao-cta">{cta('hw_blog_cta_top','top','🎃 立即預訂萬聖節套餐')}</div>

<div class="ao-tagsec">
<span class="lbl">此文章相關 Tag</span>
<div class="ao-tags">
<span>萬聖節到會</span>
<span>派對到會</span>
<span>公司活動到會</span>
<span>親子派對</span>
</div>
</div>

<nav class="ao-toc">
<div class="t">目錄</div>
<ul>
<li><a href="#why-halloween-catering">為何選擇 KitchenAO 萬聖節到會？</a></li>
<li><a href="#menu-details">2026 萬聖節狂嘩套餐：5 大主打菜式</a></li>
<li><a href="#sets">按人數揀套餐（5 至 40 人）</a></li>
<li><a href="#faq">萬聖節到會常見問題</a></li>
</ul>
</nav>

<h2 id="why-halloween-catering" class="ao-h2">為何選擇 KitchenAO 萬聖節派對到會？</h2>
<div class="ao-why">
<ul>
<li><b>搞鬼造型，驚喜滿分：</b>廚師團隊將經典派對食物改造成充滿萬聖節氣氛嘅「暗黑料理」，絕對係派對打卡焦點！</li>
<li><b>星級滋味，絕非「地獄廚神」：</b>雖然賣相搞鬼，但我們嚴選新鮮食材，保證每一口都係餐廳級數嘅美味。</li>
<li><b>一站式服務，輕鬆搞 Party：</b>網上揀好人數同菜式，我們準時將成個套餐直送到府上，你專心狂歡就得！</li>
<li><b>適合任何嘩鬼派對：</b>無論係家庭親子派對、朋友聚會，定係公司 Halloween Party，都可以完美融入你嘅活動。</li>
</ul>
</div>

<h2 id="menu-details" class="ao-h2">🎃 2026 萬聖節狂嘩套餐：5 大主打菜式</h2>
<p>今年 5 款萬聖節限定菜式，造型搞鬼、味道認真。每個套餐可按人數揀選前菜、沙律、意粉／意大利飯同主菜，再配搭以下主打菜式：</p>

<div class="ao-menugrid">{cards}
</div>

<p style="margin-top:22px;">套餐內亦可選配 <strong>👻 怪誕骷髏頭白菌芝士焗肉醬蝴蝶粉</strong>，以及 KitchenAO 人氣前菜、沙律同主菜，自由組合成你嘅萬聖節派對枱。</p>

<div class="ao-cta">{cta('hw_blog_cta_menu','menu','👻 睇全部萬聖節套餐菜式')}</div>

<h2 id="sets" class="ao-h2">按人數揀套餐（5 至 40 人）</h2>
<p>6 個人數選擇，按一下直接揀菜式落單：</p>
<div class="ao-hw-sets">{sets}</div>
<p class="ao-hw-note">* 價錢為網站現時優惠價，以下單頁面顯示為準。</p>

<p style="margin-top:30px;">今個萬聖節，就用 KitchenAO 嘅搞鬼派對美食，驚艷你所有嘩鬼朋友吧！🎃 <strong>送貨日期為 10 月 23 日至 11 月 1 日</strong>，萬聖節係訂單高峰期，建議盡早預訂。</p>

<div class="ao-cta ao-cta--2">
{cta('hw_blog_cta_bottom','bottom','🎃 立即預訂萬聖節套餐')}
<a class="ao-hw-wa" href="https://api.whatsapp.com/send?phone=85269011987&amp;text=你好，我想查詢 2026 萬聖節狂嘩套餐" target="_blank" rel="noopener" onclick="window.dataLayer=window.dataLayer||[];dataLayer.push({{event:'cta_click',cta_label:'hw_blog_whatsapp'}});">WhatsApp 查詢</a>
</div>

<h2 id="faq" class="ao-h2">萬聖節到會 Q&amp;A</h2>

<details class="ao-faq"><summary>Q1：2026 萬聖節套餐幾時送貨？應該提早幾耐預訂？</summary><div class="a">萬聖節套餐送貨日期為 <strong>10 月 23 日至 11 月 1 日</strong>，即日已接受訂購。萬聖節係訂單高峰期，建議最少提早 7–10 日預訂；<strong>10 月 22 日前預訂更可享 92 折</strong>。</div></details>

<details class="ao-faq"><summary>Q2：套餐有咩優惠？可唔可以用優惠碼？</summary><div class="a">10 月 22 日前預訂享 92 折，各區滿 $1,450 免費送遞。可使用會員優惠現金券，但其他優惠碼不適用。</div></details>

<details class="ao-faq"><summary>Q3：套餐內的食物會好辣嗎？適合小朋友嗎？</summary><div class="a">請放心，萬聖節套餐主要以搞鬼造型為主，口味以大眾化派對美食為基礎，並冇辛辣元素，非常適合有小朋友參與嘅家庭派對。</div></details>

<details class="ao-faq"><summary>Q4：除咗套餐菜式，可以額外加配其他食物嗎？</summary><div class="a">可以！下單頁面設有小食加配同優惠價加配，你亦可以喺常規到會餐單自由選配其他食物，打造更豐富嘅萬聖節自助餐。</div></details>

<details class="ao-faq"><summary>Q5：你們的送貨服務覆蓋哪些地區？</summary><div class="a">我們的到會服務覆蓋全港九新界大部分地區（偏遠地區及離島除外），歡迎下單時提供地址查詢詳情及運費。</div></details>

<div class="ao-bottombar">
<button class="ao-share" type="button" onclick="navigator.clipboard&&navigator.clipboard.writeText(location.href);var t=this;t.textContent='✅ 已複製連結';setTimeout(function(){{t.textContent='🔗 複製文章連結';}},2000);">🔗 複製文章連結</button>
<div class="ao-helpful" id="aoHelpful">
<div class="ao-help-row"><span id="aoQ">呢篇文章有冇幫到你？</span><button type="button" id="aoUp" onclick="aoVote('up')">👍 有用</button><button type="button" id="aoDown" onclick="aoVote('down')">👎 一般</button></div>
<div class="ao-rate" id="aoRate" style="display:none"><div class="ao-rate-bar"><span id="aoRateFill"></span></div><div class="ao-rate-txt"><b id="aoRatePct"></b> 讀者覺得有用 · <span id="aoRateTotal"></span></div></div>
</div>
</div>
{open('vote.js').read()}

<div class="ao-tagsec">
<span class="lbl">此文章相關 Tag</span>
<div class="ao-tags">
<span>萬聖節到會</span>
<span>派對到會</span>
<span>公司活動到會</span>
<span>親子派對</span>
</div>
</div>

<div class="ao-related">
<p class="ao-related-t">📖 延伸閱讀</p>
<a href="https://aoaodelivery.com/blog/kids-birthday-party-catering/">【香港家長必讀】小朋友生日會到會挑選指南 →</a>
<a href="https://aoaodelivery.com/blog/company-event-catering-guide/">香港公司活動到會攻略 2026｜Budget、餐單、服務全指南 →</a>
<a href="https://aoaodelivery.com/blog/laser-printed-food-party/">【香港到會新玩法】激光打印漢堡／馬卡龍 派對焦點 →</a>
</div>

</div>

<script type="application/ld+json">
{{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {{"@type":"Question","name":"2026 萬聖節套餐幾時送貨？應該提早幾耐預訂？","acceptedAnswer":{{"@type":"Answer","text":"萬聖節套餐送貨日期為 10 月 23 日至 11 月 1 日，即日已接受訂購。建議最少提早 7–10 日預訂；10 月 22 日前預訂可享 92 折。"}}}},
    {{"@type":"Question","name":"KitchenAO 萬聖節套餐有咩優惠？可唔可以用優惠碼？","acceptedAnswer":{{"@type":"Answer","text":"10 月 22 日前預訂享 92 折，各區滿 $1,450 免費送遞。可使用會員優惠現金券，但其他優惠碼不適用。"}}}},
    {{"@type":"Question","name":"KitchenAO 萬聖節到會食物會好辣嗎？適合小朋友嗎？","acceptedAnswer":{{"@type":"Answer","text":"套餐以搞鬼造型為主，口味大眾化、冇辛辣元素，非常適合有小朋友參與嘅家庭派對。"}}}},
    {{"@type":"Question","name":"除咗套餐菜式，可以額外加配其他食物嗎？","acceptedAnswer":{{"@type":"Answer","text":"可以。下單頁面設有小食加配同優惠價加配，亦可於常規到會餐單自由選配其他食物。"}}}},
    {{"@type":"Question","name":"KitchenAO 的萬聖節到會送貨覆蓋哪些地區？","acceptedAnswer":{{"@type":"Answer","text":"到會服務覆蓋全港九新界大部分地區（偏遠地區及離島除外），下單時提供地址即可查詢詳情及運費。"}}}}
  ]
}}
</script>
'''
open('blog-halloween-2026.html','w').write(HTML)
open('preview.html','w').write('<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Preview</title></head><body style="margin:0;padding:30px 16px;background:#fff">'+HTML+'</body></html>')
print(len(HTML))
