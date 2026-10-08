BAT='<svg viewBox="0 0 100 44"><path d="M50 18 L53 9 L55.5 17 C62 12 78 6 97 10 C89 14 85 20 87 27 C81 22 75 22 71 29 C67 24 61 24 57.5 31 C55 29 52.5 33 50 38 C47.5 33 45 29 42.5 31 C39 24 33 24 29 29 C25 22 19 22 13 27 C15 20 11 14 3 10 C22 6 38 12 44.5 17 L47 9 Z" fill="#2a0d3d"/><circle cx="47.6" cy="20" r="1.6" fill="#FFE14D"/><circle cx="52.4" cy="20" r="1.6" fill="#FFE14D"/></svg>'
BATS='<span class="ao-hw-bats" aria-hidden="true"><i class="b1">%s</i><i class="b2">%s</i><i class="b3">%s</i></span>'%(BAT,BAT,BAT)
CAT='https://aoaodelivery.com/product-category/halloween-set/'
UP='https://aoaodelivery.com/wp-content/uploads/2026/10/'
def cta(label,ref,txt):
    return f'<a class="ao-hw-cta" href="{CAT}?ao_ref=hw26_blog_{ref}" onclick="window.dataLayer=window.dataLayer||[];dataLayer.push({{event:\'cta_click\',cta_label:\'{label}\'}});">{BATS}<span class="ao-hw-txt">{txt}</span></a>'
DISH=[
 ('2026-halloween-story-_post-2-scaled.jpg','🎃','哈囉喂','「原個直送」日本南瓜海鮮意大利飯','以原個日本南瓜作器皿直送到會，南瓜蓉融入每顆米粒，配以彈牙海鮮，賣相與味道同樣出色。'),
 ('2026-halloween-story-_post-3-scaled.jpg','👁️','惡魔的眼睛','開心果醬荔枝藍苺酥盒','牛油酥盒釀入開心果醬，再以荔枝及藍莓砌成一隻隻「惡魔眼睛」，甜而不膩，一口一件，最適合派對享用。'),
 ('2026-halloween-story-_post-1-scaled.jpg','🩸','血淋淋科學怪人','香濃蕃茄手指腸仔','形似「斷指」的腸仔，淋上香濃蕃茄醬營造血淋淋效果，嚇人之餘又惹味，最受小朋友歡迎。'),
 ('2025-Halloween-burger-1-600x750.jpg','🍔','萬聖節','迷你芝士手打牛肉漢堡','手打牛肉配半溶芝士，換上萬聖節造型新裝，迷你尺寸方便拿取，大人小孩都適合。'),
 ('2026-halloween-story-_post-4-scaled.jpg','🦇','小蝙蝠','墨汁雞翼','以墨汁染成漆黑的雞翼，外層香脆、內裏嫩滑多汁，是餐桌上最搶眼的「小蝙蝠」。'),
]
cards=''.join(f'''
<div class="ao-menucard{' ao-menucard--hero' if n==0 else ''}">
<div class="ph"><img loading="lazy" decoding="async" src="{UP}{img}" alt="{a}{b} — Kitchen AO 2026 萬聖節到會"></div>
<div class="body">{'<span class="ao-hw-bigico" aria-hidden="true">'+ic+'</span><span class="ao-hw-must">今年主打</span>' if n==0 else ''}<p class="name">{'' if n==0 else '<span class="ic">'+ic+'</span>'}<small>{a}</small>{b}</p><p class="desc">{d}</p></div>
</div>''' for n,(img,ic,a,b,d) in enumerate(DISH))
SETS=[('5-6','133800','ao-5-6pax',1458),('8-10','191800','ao-8-10pax',2088),('12-16','288800','ao-12-16pax',3138),('18-22','375800','ao-18-22pax',4088),('26-30','500800','ao-26-30pax',5448),('35-40','655800','ao-35-40pax',7128)]
SFX={'35-40':''}
SLUG='-halloween%e8%90%ac%e8%81%96%e7%af%80%e7%8b%82%e5%98%a9%e5%a5%97%e9%a4%90/'
sets=''.join(f'<a class="ao-hw-set" href="https://aoaodelivery.com/product/{s}{SLUG}?ao_ref=hw26_blog_set{p.replace("-","_")}" onclick="window.dataLayer=window.dataLayer||[];dataLayer.push({{event:\'cta_click\',cta_label:\'hw_blog_set_{p}\'}});"><span class="ph"><img loading="lazy" decoding="async" src="{UP}2026-Halloween-{p}{SFX.get(p,"_set-photo")}-600x600.jpg" width="600" height="600" alt="Halloween 萬聖節狂嘩套餐 {p} 人"></span><span class="tx"><b>{p}<small>人</small></b><span class="pr"><del>${rp:,}<sup>.00</sup></del> <ins>${int(pr)//100:,}<sup>.00</sup></ins></span><i>查看菜式 →</i></span></a>' for p,pr,s,rp in SETS)

CSS=open('style.css').read()
HTML=f'''<div class="ao-article ao-hw26">
<style>
{CSS}
</style>

<a class="ao-hw-kvlink" href="{CAT}?ao_ref=hw26_blog_kv" onclick="window.dataLayer=window.dataLayer||[];dataLayer.push({{event:'cta_click',cta_label:'hw_blog_kv'}});"><img class="ao-hw-kv" src="{UP}2025-Halloween-banner-1_banner_banner-1536x717.jpg" width="1536" height="717" alt="Kitchen AO Halloween 萬聖節狂嘩套餐 2026 到會" fetchpriority="high" decoding="async"></a>

<div class="ao-hw-ticket">
<div class="ao-hw-t1"><span class="ao-hw-dot"></span>即日接受訂購</div>
<div class="ao-hw-t2"><small>送貨日期</small><b><span>10月23日</span> – <span>11月1日</span></b></div>
</div>

<div class="ao-introcard">
<span class="ao-hw-badge" aria-hidden="true">🎃</span>
<p class="ao-q">🎃 想舉辦一場全場尖叫的萬聖節派對？</p>
<p class="ao-intro">「Trick or Treat！」Kitchen AO <strong>2026 年 Halloween 萬聖節狂嘩套餐</strong>正式登場！今年推出 <strong>5 款全新搞鬼主打菜式</strong>，由「惡魔的眼睛」酥盒到原個日本南瓜海鮮意大利飯，<strong>5 至 40 人</strong>均有合適套餐，全港送遞，無論是家庭派對、朋友聚會或公司 Halloween Party 都同樣適合。</p>
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
<li><a href="#halloween-origin">萬聖節由來：為何要扮鬼、點南瓜燈？</a></li>
<li><a href="#halloween-party-home">在家舉辦 Halloween Party 4 步攻略</a></li>
<li><a href="#company-halloween-party">公司 Halloween Party 攻略</a></li>
<li><a href="#why-halloween-catering">為何選擇 Kitchen AO 萬聖節到會？</a></li>
<li><a href="#menu-details">2026 萬聖節狂嘩套餐：5 大主打菜式</a></li>
<li><a href="#sets">按人數選擇套餐（5 至 40 人）</a></li>
<li><a href="#faq">萬聖節到會常見問題</a></li>
</ul>
</nav>

<h2 id="halloween-origin" class="ao-h2">萬聖節由來：為何要扮鬼、點南瓜燈？</h2>
<p>萬聖節（Halloween）源自約 2,000 年前古凱爾特人的 <strong>薩溫節（Samhain）</strong>。凱爾特人以 10 月 31 日作為一年收成的終結，相信當晚生者與亡靈之間的界線最為薄弱，鬼魂會重返人間。為免被認出，人們會戴上面具、穿上奇裝異服，並燃點篝火驅邪。</p>
<p>其後基督教將 11 月 1 日定為「諸聖節」（All Hallows' Day），其前夕稱為 <strong>All Hallows' Eve</strong>，後來逐漸簡化為今天的 <strong>Halloween</strong>。</p>
<div class="ao-hw-facts">
<div class="ao-hw-fact"><span class="fi">🎃</span><p class="ft">南瓜燈的故事</p><p class="fd">南瓜燈的英文名稱是 <strong>Jack-o'-lantern</strong>，源自愛爾蘭傳說：一名叫 Jack 的男子曾戲弄魔鬼，死後天堂與地獄都不願接納他，他只好提着一盞以蘿蔔雕成的燈籠四處遊蕩。愛爾蘭移民到達美國後，發現南瓜體積更大、更易雕刻，南瓜燈從此成為萬聖節最經典的象徵。</p></div>
<div class="ao-hw-fact"><span class="fi">🍬</span><p class="ft">Trick or Treat 不給糖就搗蛋</p><p class="fd">小朋友扮成鬼怪逐家逐戶討糖的習俗，源自古時向亡靈獻上食物以換取祝福的傳統。時至今日，萬聖節已成為全球大人小孩都喜愛的扮裝派對節日，香港更是亞洲萬聖節氣氛最濃厚的城市之一。</p></div>
</div>
<div class="ao-hw-quote"><span class="qi">🎃</span><p>今年 Kitchen AO 的主打菜式 <strong>哈囉喂「原個直送」日本南瓜海鮮意大利飯</strong>，正是以原個日本南瓜作器皿，向經典南瓜燈致敬！</p></div>

<h2 id="halloween-party-home" class="ao-h2">在家舉辦 Halloween Party 4 步攻略</h2>
<p>不想到主題樂園人擠人？在家中或包場舉辦萬聖節派對，同樣可以玩得盡興。只需依照以下 4 個步驟，便能輕鬆成為稱職的派對主人：</p>
<div class="ao-hw-steps">
<div class="ao-hw-step"><span class="sn">1</span><p class="st">訂定主題及 Dress Code</p><p class="sd">例如「吸血鬼晚宴」、「殭屍醫院」、「女巫聚會」或「全場扮演卡通角色」。預先通知賓客 Dress Code，大家一出場便充滿氣氛。</p></div>
<div class="ao-hw-step"><span class="sn">2</span><p class="st">佈置：橙、紫、黑三色已足夠</p><p class="sd">南瓜燈、蝙蝠貼紙、蜘蛛網、LED 蠟燭配黑色枱布，已足以營造詭異氣氛。再把燈光調暗、播放 Halloween 歌單，效果即時加倍。</p></div>
<div class="ao-hw-step"><span class="sn">3</span><p class="st">派對遊戲</p><ul class="sl"><li><b>扮裝比賽：</b>設「最恐怖」、「最搞笑」、「最具心思」等獎項</li><li><b>盲摸神秘箱：</b>箱內放入啫喱、意粉等物件，讓賓客猜猜是甚麼「恐怖物體」</li><li><b>Trick or Treat 尋寶遊戲：</b>將糖果藏在家中不同角落，最受小朋友歡迎</li></ul></div>
<div class="ao-hw-step"><span class="sn">4</span><p class="st">食物：造型要搞鬼，味道要認真</p><p class="sd">派對食物最好選擇<strong>一口份量、方便拿取</strong>的款式，例如酥盒、迷你漢堡、雞翼，邊玩邊吃也不會弄得一團糟。造型搞鬼的食物更是全晚的<strong>打卡焦點</strong>。</p></div>
</div>
<div class="ao-hw-quote"><span class="qi">👻</span><p>不想親自下廚？Kitchen AO <strong>萬聖節狂嘩套餐</strong>適合 5 至 40 人，包括「惡魔的眼睛」酥盒、「血淋淋科學怪人」手指腸仔及小蝙蝠墨汁雞翼，直送到門，讓你專心享受派對。</p></div>

<h2 id="company-halloween-party" class="ao-h2">公司 Halloween Party 攻略：提升團隊凝聚力</h2>
<p>萬聖節是公司舉辦 <strong>Team Building</strong> 活動的好時機：氣氛輕鬆、人人都能參與，又不必像周年晚宴般隆重。以下重點可助 HR 及活動負責人輕鬆籌備：</p>
<div class="ao-hw-corp">
<div class="ao-hw-corpbox"><p class="ct">🗓️ 時間與場地</p><p>建議選擇萬聖節前的星期五下午或午膳時段，在公司茶水間、會議室或公共空間進行，同事參與度最高。</p></div>
<div class="ao-hw-corpbox"><p class="ct">🎭 活動建議</p><ul><li><b>Costume 比賽：</b>以部門組隊，增加跨部門互動</li><li><b>辦公桌佈置比賽：</b>由同事投票選出最恐怖的座位</li><li><b>Halloween 打卡位：</b>擺放南瓜及蝙蝠背景板，方便同事拍照分享</li></ul></div>
</div>
<div class="ao-hw-corpbox ao-hw-corpbox--full"><p class="ct">🍽️ 到會份量如何計算？</p><p>公司派對一般<strong>每人 1 份主菜加 3 至 4 件小食</strong>已經足夠。Kitchen AO 萬聖節套餐按人數設計：</p>
<div class="ao-hw-portion"><span><b>約 15 人</b>12–16 人套餐</span><span><b>約 20 人</b>18–22 人套餐</span><span><b>30 人以上</b>26–30 或 35–40 人套餐</span></div>
<p style="margin-top:12px!important;">如需籌辦更大型的公司活動，歡迎透過 WhatsApp 聯絡企業客戶專員，安排服務生、酒會 Finger Food 或 Cocktail 服務。</p>
<div class="ao-hw-corpcta"><a class="ao-hw-wa" href="https://api.whatsapp.com/send?phone=85269011987&amp;text=企業及商務到會服務查詢" target="_blank" rel="noopener" onclick="window.dataLayer=window.dataLayer||[];dataLayer.push({{event:'cta_click',cta_label:'hw_blog_corp_whatsapp'}});">WhatsApp 聯絡企業客戶專員</a><a class="ao-hw-link" href="https://aoaodelivery.com/business-event/" onclick="window.dataLayer=window.dataLayer||[];dataLayer.push({{event:'cta_click',cta_label:'hw_blog_corp_business'}});">👉 了解更多：商務活動到會服務 →</a></div>
</div>

<h2 id="why-halloween-catering" class="ao-h2">為何選擇 Kitchen AO 萬聖節派對到會？</h2>
<div class="ao-why">
<ul>
<li><b>搞鬼造型，驚喜滿分：</b>廚師團隊將經典派對食物改造成充滿萬聖節氣氛的「暗黑料理」，絕對是派對的打卡焦點！</li>
<li><b>星級滋味，絕非「地獄廚神」：</b>雖然賣相搞鬼，但我們嚴選新鮮食材，保證每一口都是餐廳級數的美味。</li>
<li><b>一站式服務，輕鬆辦 Party：</b>只需在網上選好人數及菜式，我們便會準時將整個套餐直送府上，讓你專心狂歡！</li>
<li><b>適合任何嘩鬼派對：</b>無論是家庭親子派對、朋友聚會，還是公司 Halloween Party，都能完美融入你的活動。</li>
</ul>
</div>

<h2 id="menu-details" class="ao-h2">🎃 2026 萬聖節狂嘩套餐：5 大主打菜式</h2>
<p>今年 5 款萬聖節限定菜式，造型搞鬼、味道認真。每個套餐可按人數選擇前菜、沙律、意粉／意大利飯及主菜，並配搭以下主打菜式：</p>

<ul class="ao-hw-menu">
<li><span class="ao-hw-ico">👁️</span><span><small>惡魔的眼睛</small><b>開心果醬荔枝藍苺酥盒</b></span></li>
<li><span class="ao-hw-ico">💉</span><span><small>血淋淋科學怪人</small><b>香濃蕃茄手指腸仔</b></span></li>
<li><span class="ao-hw-ico">👻</span><span><small>萬聖節</small><b>迷你芝士手打牛肉漢堡</b></span></li>
<li><span class="ao-hw-ico">🦇</span><span><small>小蝙蝠</small><b>墨汁雞翼</b></span></li>
<li><span class="ao-hw-ico">🎃</span><span><small>哈囉喂</small><b>「原個直送」日本南瓜海鮮意大利飯</b></span></li>
</ul>

<div class="ao-menugrid">{cards}
</div>

<p style="margin-top:22px;">套餐內亦可選配 <strong>👻 怪誕骷髏頭白菌芝士焗肉醬蝴蝶粉</strong>，以及 Kitchen AO 人氣前菜、沙律及主菜，自由組合成你的萬聖節派對餐桌。</p>

<div class="ao-cta">{cta('hw_blog_cta_menu','menu','👻 查看全部萬聖節套餐菜式')}</div>

<h2 id="sets" class="ao-h2">按人數選擇套餐（5 至 40 人）</h2>
<p>共有 6 個人數選擇，按一下即可選擇菜式及下單：</p>
<div class="ao-hw-sets">{sets}</div>
<p class="ao-hw-note">* 價錢為網站現時優惠價，以下單頁面顯示為準。</p>

<p style="margin-top:30px;">今個萬聖節，就以 Kitchen AO 的搞鬼派對美食，驚艷所有嘩鬼朋友吧！🎃 <strong>送貨日期為 10 月 23 日至 11 月 1 日</strong>，萬聖節是訂單高峰期，建議盡早預訂。</p>

<div class="ao-cta ao-cta--2">
{cta('hw_blog_cta_bottom','bottom','🎃 立即預訂萬聖節套餐')}
<a class="ao-hw-wa" href="https://api.whatsapp.com/send?phone=85269011987&amp;text=你好，我想查詢 2026 萬聖節狂嘩套餐" target="_blank" rel="noopener" onclick="window.dataLayer=window.dataLayer||[];dataLayer.push({{event:'cta_click',cta_label:'hw_blog_whatsapp'}});">WhatsApp 查詢</a>
</div>

<h2 id="faq" class="ao-h2">萬聖節到會 Q&amp;A</h2>

<details class="ao-faq"><summary>Q1：2026 萬聖節套餐何時送貨？應提早多久預訂？</summary><div class="a">萬聖節套餐送貨日期為 <strong>10 月 23 日至 11 月 1 日</strong>，即日起接受訂購。萬聖節是訂單高峰期，可於送貨日 1–3 日前預訂；<strong>10 月 22 日前預訂更可享 92 折</strong>。</div></details>

<details class="ao-faq"><summary>Q2：套餐有甚麼優惠？可以使用優惠碼嗎？</summary><div class="a">10 月 22 日前預訂享 92 折，各區滿 $1,450 免費送遞。可使用會員優惠現金券，但其他優惠碼不適用。</div></details>

<details class="ao-faq"><summary>Q3：套餐內的食物會好辣嗎？適合小朋友嗎？</summary><div class="a">請放心，萬聖節套餐主要以搞鬼造型為主，口味以大眾化派對美食為基礎，並沒有辛辣元素，非常適合有小朋友參與的家庭派對。</div></details>

<details class="ao-faq"><summary>Q4：除了套餐菜式，可以額外加配其他食物嗎？</summary><div class="a">可以！下單頁面設有小食加配及優惠價加配，你亦可於常規到會餐單自由選配其他食物，打造更豐富的萬聖節自助餐。</div></details>

<details class="ao-faq"><summary>Q5：你們的送貨服務覆蓋哪些地區？</summary><div class="a">我們的到會服務覆蓋全港九新界大部分地區（偏遠地區及離島除外），各區運費及免運費安排請參閱<a href="https://aoaodelivery.com/delivery/">送貨需知及免運費優惠</a>，亦歡迎下單時提供地址查詢詳情。</div></details>

<details class="ao-faq"><summary>Q6：萬聖節的由來是甚麼？</summary><div class="a">萬聖節源自約 2,000 年前古凱爾特人的薩溫節（Samhain）。他們相信 10 月 31 日晚上亡靈會重返人間，因此會戴上面具、扮成鬼怪以避開鬼魂，後來逐漸演變成今天的 Halloween 扮裝派對。</div></details>

<details class="ao-faq"><summary>Q7：公司 Halloween Party 需要準備多少食物？</summary><div class="a">一般每人 1 份主菜加 3 至 4 件小食已經足夠。約 15 人可選 12–16 人套餐，約 20 人可選 18–22 人套餐，30 人以上可選 26–30 人或 35–40 人套餐。</div></details>

<div class="ao-bottombar">
<button class="ao-share" type="button" onclick="navigator.clipboard&&navigator.clipboard.writeText(location.href);var t=this;t.textContent='✅ 已複製連結';setTimeout(function(){{t.textContent='🔗 複製文章連結';}},2000);">🔗 複製文章連結</button>
<div class="ao-helpful" id="aoHelpful">
<div class="ao-help-row"><span id="aoQ">這篇文章對你有幫助嗎？</span><button type="button" id="aoUp" onclick="aoVote('up')">👍 有用</button><button type="button" id="aoDown" onclick="aoVote('down')">👎 一般</button></div>
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
    {{"@type":"Question","name":"2026 萬聖節套餐何時送貨？應提早多久預訂？","acceptedAnswer":{{"@type":"Answer","text":"萬聖節套餐送貨日期為 10 月 23 日至 11 月 1 日，即日起接受訂購。萬聖節是訂單高峰期，可於送貨日 1–3 日前預訂；10 月 22 日前預訂可享 92 折。"}}}},
    {{"@type":"Question","name":"Kitchen AO 萬聖節套餐有甚麼優惠？可以使用優惠碼嗎？","acceptedAnswer":{{"@type":"Answer","text":"10 月 22 日前預訂享 92 折，各區滿 $1,450 免費送遞。可使用會員優惠現金券，但其他優惠碼不適用。"}}}},
    {{"@type":"Question","name":"Kitchen AO 萬聖節到會食物會好辣嗎？適合小朋友嗎？","acceptedAnswer":{{"@type":"Answer","text":"套餐以搞鬼造型為主，口味大眾化、沒有辛辣元素，非常適合有小朋友參與的家庭派對。"}}}},
    {{"@type":"Question","name":"除了套餐菜式，可以額外加配其他食物嗎？","acceptedAnswer":{{"@type":"Answer","text":"可以。下單頁面設有小食加配及優惠價加配，亦可於常規到會餐單自由選配其他食物。"}}}},
    {{"@type":"Question","name":"Kitchen AO 的萬聖節到會送貨覆蓋哪些地區？","acceptedAnswer":{{"@type":"Answer","text":"到會服務覆蓋全港九新界大部分地區（偏遠地區及離島除外），各區運費及免運費安排請參閱 https://aoaodelivery.com/delivery/ ，亦可於下單時提供地址查詢詳情。"}}}},
    {{"@type":"Question","name":"萬聖節的由來是甚麼？","acceptedAnswer":{{"@type":"Answer","text":"萬聖節源自約 2,000 年前古凱爾特人的薩溫節（Samhain）。他們相信 10 月 31 日晚上亡靈會重返人間，因此會戴上面具、扮成鬼怪以避開鬼魂，後來逐漸演變成今天的 Halloween 扮裝派對。"}}}},
    {{"@type":"Question","name":"公司 Halloween Party 需要準備多少食物？","acceptedAnswer":{{"@type":"Answer","text":"一般每人 1 份主菜加 3 至 4 件小食已經足夠。約 15 人可選 12–16 人套餐，約 20 人可選 18–22 人套餐，30 人以上可選 26–30 人或 35–40 人套餐。"}}}}
  ]
}}
</script>
'''
open('blog-halloween-2026.html','w').write(HTML)
open('preview.html','w').write('<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Preview</title></head><body style="margin:0;padding:30px 16px;background:#fff">'+HTML+'</body></html>')
print(len(HTML))
