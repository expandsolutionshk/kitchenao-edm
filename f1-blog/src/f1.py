# -*- coding: utf-8 -*-
# F1 車手飲食 × F1 觀賽派對健康到會 blog → ../f1-driver-diet-watch-party.html 及 -WORDPRESS.html
import sys, pathlib
HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE.parent.parent / 'vegetarian-blog' / 'src'))
import common as C
from common import k

PID = 'F1'
TITLE = 'F1 車手一日吃甚麼？車手餐單 × F1 觀賽派對健康到會攻略'
URL = 'https://aoaodelivery.com/blog/f1-driver-diet-watch-party/'
C.BLOGS[PID] = (TITLE, URL)
AO = 'https://aoaodelivery.com'
def a(u, t): return f'<a href="{u}">{t}</a>'
def ext(u, t): return f'<a href="{u}" target="_blank" rel="noopener">{t}</a>'

CTA = (HERE / 'cta.html').read_text(encoding='utf-8').replace('車手式的沙律、烤肉和海鮮，配合派對的小食和甜品', '沙律、肉類、海鮮配合小食和甜品')

S = {
 'rb':   ('媒體', 'Red Bull — What does an F1 driver eat in a day?（2024 年 5 月）', 'https://www.redbull.com/us-en/formula-one-driver-diet'),
 'rbtw': ('媒體', 'Red Bull 台灣中文版（同一篇文章）', 'https://www.redbull.com/tw-zh/formula-one-driver-diet'),
 'bi':   ('媒體', 'Business Insider — McLaren 公開 F1 車手訓練日餐單（2017 年）', 'https://businessinsider.nl/mclaren-formula-one-driver-racer-diet-plan-2017-3'),
 'rn':   ('媒體', 'RacingNews365 — Why do F1 drivers get weighed after a race?', 'https://racingnews365.com/why-do-f1-drivers-get-weighed-after-a-race'),
 'fr':   ('媒體', 'Flow Racers — What Do F1 Drivers Eat Before A Race?', 'https://flowracers.com/blog/f1-driver-pre-race-nutrition/'),
 'vfl':  ('媒體', 'Vegan Food & Living — Lewis Hamilton shares his go-to vegan snack（2022 年 8 月）', 'https://www.veganfoodandliving.com/news/lewis-hamilton-shares-go-to-vegan-snack-he-eats-daily/'),
 'gpv':  ('媒體', 'GRANDPRIX247 — Vettel: I have more vegetables on my plate now（2019 年 12 月）', 'https://www.grandprix247.com/formula-1-news/vettel-i-have-more-vegetables-on-my-plate-now'),
 'gpl':  ('媒體', 'GRANDPRIX247／Reuters — Leclerc supports Hamilton but not going vegan himself（2019 年 10 月）', 'https://www.grandprix247.com/formula-1-news/leclerc-supports-hamilton-but-not-going-vegan-himself'),
 'gpb':  ('媒體', 'GPblog — Verstappen reveals his training week and diet（2021 年 9 月）', 'https://www.gpblog.com/en/news/verstappen-reveals-his-training-week-and-diet.html'),
 'gpf':  ('媒體', 'GPFans — Inside the diet of an F1 driver: Private chefs, blood tests and NO fish（2025 年 11 月）', 'https://www.gpfans.com/en/f1-news/1066611/diet-f1-driver-lando-norris-private-chef/'),
 'f1t':  ('官方', 'Formula 1 — Official Grand Prix start times for 2026 F1 season confirmed', 'https://www.formula1.com/en/latest/article/official-grand-prix-start-times-for-2026-f1-season-confirmed.2UgPfArqH76tzlOYh21jSG'),
 'scmp': ('香港媒體', 'South China Morning Post（STYLE）— What did vegan racing driver Lewis Hamilton eat to fuel his fifth F1 world title?', 'https://www.scmp.com/magazines/style/people-events/article/2175510/what-did-vegan-racing-driver-lewis-hamilton-eat-fuel'),
 'hksi': ('香港機構', '香港體育學院運動營養監控中心《運動營養教育系列手冊 XXII：運動營養補充品應用》（2020 年 5 月）', 'https://hksi.org.hk/f/page/509/S22.%20%E9%81%8B%E5%8B%95%E7%87%9F%E9%A4%8A%E8%A3%9C%E5%85%85%E5%93%81%E6%87%89%E7%94%A8.pdf'),
 'ao':   ('Kitchen AO', '派對到會套餐（分類及價目）', AO + '/product-category/party/'),
 'del':  ('Kitchen AO', '送貨需知及免運費優惠', AO + '/delivery/'),
}

body = f'''
<p class="ao-intro">一場 {k('F1')} 大獎賽動輒一個半小時，車手要在攝氏 50 度的駕駛艙內承受高 G 力，一場比賽可流失 2 至 4 公斤汗水。因此，{k('F1車手飲食')}由專屬營養師按時間計劃：吃甚麼、何時吃、喝多少，都有講究。咸美頓（Lewis Hamilton）吃植物性飲食，勒克萊爾（Charles Leclerc）坦言愛吃牛肉，諾里斯（Lando Norris）不吃魚卻有私人廚師按驗血報告煮食——同是頂級車手，{k('F1車手餐單')}原來各有不同。本文看看車手們實際吃甚麼，再把他們的飲食原則，搬到你的 {k('F1觀賽派對')}上。</p>
<div class="ao-qa"><p class="t">30 秒看懂</p><p>F1 車手的飲食重點是<b>慢釋放碳水化合物、低脂蛋白質、大量蔬果及充足水分</b>：早餐多是燕麥粥配水果，午餐是沙律配雞胸或豆腐，晚餐是烤魚配番薯。比賽日吃得輕、不吃陌生食物；賽後才補充大餐。籌備觀賽派對時，可以參考這個比例：多沙律蔬果、選烤肉海鮮、主食適量，再按比賽的香港時間決定吃正餐還是輕食。</p></div>
<nav class="ao-toc"><div class="t">目錄</div><ul>
<li><a href="#why">F1 車手為甚麼要嚴格控制飲食？</a></li>
<li><a href="#menu">F1 車手餐單：一日三餐吃甚麼？</a></li>
<li><a href="#nutri">三大營養重點：碳水化合物、蛋白質、水分</a></li>
<li><a href="#raceday">比賽日怎樣吃？賽前、賽中、賽後</a></li>
<li><a href="#compare">誰吃素？誰吃肉？5 位車手飲食比較</a></li>
<li><a href="#comfort">車手也有「放縱餐」</a></li>
<li><a href="#schedule">2026 年餘下賽事香港時間：觀賽派對時間表</a></li>
<li><a href="#party">借鏡車手餐單：F1 觀賽派對到會怎樣揀？</a></li>
<li><a href="#faq">常見問題</a></li></ul></nav>

<h2 class="ao-h2" id="why">F1 車手為甚麼要嚴格控制飲食？</h2>
<p>駕駛 F1 賽車不只是技術活，更是一項耐力運動。Red Bull 指出，在最炎熱的新加坡站，車手一場比賽可流失 3 至 4 公斤汗水；RacingNews365 則指一般賽事約流失 2 至 3 公斤。Flow Racers 補充，引擎貼近駕駛艙，艙內溫度可達攝氏 50 度，車手還要穿上密封的防火賽車服。</p>
<p>體重同樣是關鍵。賽車愈輕愈快，以往有車手為了減重而刻意節食。國際汽聯（FIA）於 2019 年起設立車手最低重量 80 公斤（連頭盔、賽車服及鞋），不足的部分須在車上加配重，賽後亦會再過磅，一方面核實重量，一方面監察車手流失了多少水分。換言之，車手要「夠輕」，但不能餓壞身體，飲食就是兩者之間的平衡。</p>
<div class="ao-tw"><table class="ao-tbl"><thead><tr><th>項目</th><th>數字</th><th>出處</th></tr></thead><tbody>
<tr><td>一場比賽流失汗水</td><td>一般 2–3 公斤；新加坡站 3–4 公斤</td><td>RacingNews365、Red Bull</td></tr>
<tr><td>駕駛艙溫度</td><td>最高約攝氏 50 度</td><td>Flow Racers</td></tr>
<tr><td>車手最低重量</td><td>80 公斤（連裝備，2019 年起）</td><td>RacingNews365</td></tr>
<tr><td>Red Bull 車手身高體重（2024 年）</td><td>韋斯塔潘 180 厘米／71 公斤；角田裕毅 159 厘米／53 公斤</td><td>Red Bull</td></tr>
</tbody></table></div>

<h2 class="ao-h2" id="menu">F1 車手餐單：一日三餐吃甚麼？</h2>
<p>以下兩份餐單，一份是 Red Bull 介紹旗下車手比賽週末的典型餐單；另一份是 McLaren 於 2017 年公開、阿朗素（Fernando Alonso）及雲杜尼（Stoffel Vandoorne）季前訓練期間使用的訓練日餐單。兩者有一個共通點：<b>以燕麥、全穀、番薯等慢釋放碳水化合物為主，蛋白質選雞、魚、豆腐，每餐都有蔬菜或水果</b>。</p>
<div class="ao-tw"><table class="ao-tbl"><thead><tr><th>餐次</th><th>Red Bull 車手：比賽週末</th><th>McLaren 阿朗素、雲杜尼：季前訓練日</th></tr></thead><tbody>
<tr><td><b>早餐</b></td><td>燕麥粥配莓果、香蕉、果仁，以蜜糖調味</td><td>7 時：約 550 千卡的燕麥粥配水果及種子，訓練前一小時進食；可配橙汁（加少許檸檬）及綠茶</td></tr>
<tr><td><b>午餐</b></td><td>沙律，再配雞胸、番茄莎莎及烚菜；甜品是水果</td><td>12 時 30 分：蒜香豆腐炒雜菜配糙米飯；可喝咖啡或綠茶，配幾小塊 85% 黑朱古力</td></tr>
<tr><td><b>晚餐</b></td><td>番茄湯，再配烤魚、番薯及沙律；甜品是乳酪</td><td>6 時 30 分：當日第一份肉或魚——烤鯖魚配小份焗番薯及沙律；甜品是乳酪配莓果</td></tr>
<tr><td><b>宵夜</b></td><td>—</td><td>9 時：薄脆餅配 Marmite 及水果；10 時就寢</td></tr>
</tbody></table></div>
<p class="ao-tcap">資料來源：Red Bull（2024 年）、Business Insider 轉載 McLaren 餐單（2017 年）。不同車手及車隊的餐單各有不同，僅供參考。</p>

<h2 class="ao-h2" id="nutri">三大營養重點：碳水化合物、蛋白質、水分</h2>
<h3 class="ao-h3">1. 碳水化合物：揀慢釋放的</h3>
<p>Red Bull 指出，車手在比賽及訓練前都會補充碳水化合物，但主要來自穀物、糙米及豆類等高纖維、慢釋放的來源，而不是意粉或薯條。這類食物同時含鉀和鎂，有助肌肉及神經系統運作。另外，車手每日最少要吃五至七份蔬果。</p>
<h3 class="ao-h3">2. 蛋白質：低脂為主</h3>
<p>蛋白質幫助肌肉修復。Red Bull 的文章提到車手需要高蛋白飲食，並以雞、魚等低脂肉類為主；素食車手則可選豆腐及豆類。香港體育學院的運動營養手冊亦指出，研究顯示運動後進食 25 至 30 克蛋白質，有助促進肌肉蛋白質合成，而且正餐和小食應首選天然食物，補充品不能代替健康飲食。</p>
<h3 class="ao-h3">3. 水分及電解質：比賽成敗關鍵</h3>
<p>車手比賽時只能透過頭盔上的飲管補水，喝的多是含葡萄糖、礦物質及電解質的飲品（Flow Racers）。香港體育學院的手冊說明，運動飲品含 6% 至 8% 碳水化合物及電解質，<b>適合超過 90 分鐘的運動，或在炎熱環境下進行超過 60 分鐘的高強度運動</b>。換句話說，一般人在家觀賽，喝清水已經足夠。</p>
<div class="ao-warn">⚠️ 運動飲品含糖及熱量，香港體育學院提醒過量使用會導致不必要的體重增加。觀賽時坐着不動，不宜當汽水般飲用。</div>

<h2 class="ao-h2" id="raceday">比賽日怎樣吃？賽前、賽中、賽後</h2>
<div class="ao-tw"><table class="ao-tbl"><thead><tr><th>時段</th><th>做法</th></tr></thead><tbody>
<tr><td><b>賽前</b></td><td>早餐及午餐都吃得輕，避免飽滯；紅肉太重，多選雞、魚、蛋或植物蛋白，配米飯、古斯古斯、藜麥、番薯等碳水化合物。賽前數小時完成進食，讓身體有時間消化（Flow Racers）。</td></tr>
<tr><td><b>不吃陌生食物</b></td><td>整個比賽週末都不吃身體不習慣的食物，以免食物中毒或敏感；Flow Racers 舉例，韋伯（Mark Webber）在 2007 年日本站就曾受食物中毒影響。</td></tr>
<tr><td><b>賽中</b></td><td>不能進食，只能透過飲管飲用電解質飲品（Flow Racers）。</td></tr>
<tr><td><b>賽後</b></td><td>過磅後補充水分，再以蛋白質及碳水化合物為主的正餐恢復體力；如下週末再有比賽，仍要控制份量（RacingNews365、Flow Racers）。</td></tr>
</tbody></table></div>

<h2 class="ao-h2" id="compare">誰吃素？誰吃肉？5 位車手飲食比較</h2>
<p>車手的餐單由營養師和廚師按個人需要設計，所以並非人人一樣。以下比較 5 位車手公開談過的飲食習慣：</p>
<div class="ao-tw"><table class="ao-tbl"><thead><tr><th>車手</th><th>飲食取向</th><th>代表食物／習慣</th><th>出處</th></tr></thead><tbody>
<tr><td><b>咸美頓</b><br><small>Lewis Hamilton</small></td><td><span class="ao-tag">🌱 植物性飲食</span></td><td>牛油果多士、植物蛋白果昔（每日兩至三次）、多牛油果的沙律、植物性咖喱、鷹嘴豆蓉</td><td>Vegan Food &amp; Living（轉述 Men's Health、Vanity Fair）；《南華早報》</td></tr>
<tr><td><b>維特爾</b><br><small>Sebastian Vettel</small></td><td><span class="ao-tag w">🥗 少肉多菜</span></td><td>試過純素約六星期後恢復吃肉，但從此少吃肉、多吃菜，更重視食材質素</td><td>GRANDPRIX247（轉述瑞士《Blick》，2019 年）</td></tr>
<tr><td><b>勒克萊爾</b><br><small>Charles Leclerc</small></td><td><span class="ao-tag r">🥩 吃肉</span></td><td>坦言喜歡牛肉，不打算吃純素，但會研究不同飲食方法</td><td>路透社訪問（GRANDPRIX247 轉載，2019 年）</td></tr>
<tr><td><b>韋斯塔潘</b><br><small>Max Verstappen</small></td><td><span class="ao-tag r">🥩 吃肉</span></td><td>飲食經嚴格管理，確保吃夠；會按比賽地點及天氣調整；最愛的安慰食物是番茄湯</td><td>GPblog（轉述 Men's Health，2021 年）；Red Bull</td></tr>
<tr><td><b>諾里斯</b><br><small>Lando Norris</small></td><td><span class="ao-tag w">🍔 吃肉不吃魚</span></td><td>私人廚師煮食，定期驗血補充欠缺的營養；賽後會吃漢堡</td><td>GPFans（轉述米芝蓮廚師 Sidney Schutte 訪問，2025 年）</td></tr>
</tbody></table></div>
<p class="ao-tcap">以上為車手在不同年份的公開說法，飲食習慣或已改變。</p>

<h3 class="ao-h3">咸美頓：植物性飲食的代表</h3>
<p>七屆世界冠軍咸美頓（現效力法拉利）約於 2017 年轉吃植物性飲食。他接受 Men's Health 訪問時說，早上會吃牛油果多士，每天喝兩至三次加入植物蛋白的果昔，午餐是多牛油果的沙律，晚餐愛吃植物性咖喱，平日以果仁及純素蛋白棒補充能量。鷹嘴豆蓉更是他的日常小食：</p>
<blockquote class="ao-quote">「我以前看到鷹嘴豆蓉就想：『我絕對不會吃！』現在我很愛吃，每天都吃。」<cite>——咸美頓接受《Vanity Fair》訪問（Vegan Food &amp; Living 轉述，2022 年）</cite></blockquote>
<p>醫生曾警告他吃純素難以攝取足夠蛋白質，他的回應是：「轉吃植物性飲食後，我再贏了五次世界冠軍，表現比以往更穩定。」據《南華早報》報道，他更曾在<b>香港找到一款素漢堡，還請人送到日本，比賽期間每天吃</b>。不過，報道亦引述曾與 McLaren 及法拉利合作的運動生化學家 Rob Child 提醒，純素運動員要仔細規劃飲食，例如攝取足夠的健康脂肪。如果派對上有素食朋友，可參考{a(AO + '/blog/vegetarian-catering-hong-kong/', '素食到會安排攻略')}。</p>

<h3 class="ao-h3">維特爾：試過純素，最後「少肉多菜」</h3>
<blockquote class="ao-quote">「這個實驗維持了大約六個星期，我從中學到很多……世上沒有一種『正確』的飲食，因為每個人都不同。」<cite>——維特爾接受瑞士《Blick》訪問（GRANDPRIX247 轉載，2019 年）</cite></blockquote>
<p>四屆世界冠軍維特爾表示，雖然最終恢復吃肉，但現在吃少了肉，碟上的蔬菜也多了。</p>

<h3 class="ao-h3">勒克萊爾：喜歡牛肉，但願意嘗試</h3>
<blockquote class="ao-quote">「我不是純素食者，但我一直在研究這些方法……我喜歡牛肉，但也想多往（植物性飲食）那個方向試試。」<cite>——勒克萊爾接受路透社訪問（GRANDPRIX247 轉載，2019 年）</cite></blockquote>

<h3 class="ao-h3">韋斯塔潘：吃得夠，比吃得少更重要</h3>
<blockquote class="ao-quote">「體重在賽車中十分重要，所以我的飲食經過仔細管理。這是一項很耗體力的運動，我一定確保自己吃得夠。」<cite>——韋斯塔潘接受 Men's Health 訪問（GPblog 轉述，2021 年）</cite></blockquote>
<p>他補充，飲食會因應比賽地點和天氣調整，在潮濕天氣下消耗的熱量，與在賽道上不相伯仲。</p>

<h3 class="ao-h3">諾里斯：不吃魚，靠私人廚師補營養</h3>
<blockquote class="ao-quote">「我的飲食頗嚴格，由廚師負責我所有食物。我經常驗血，看看自己缺少甚麼；因為我不吃魚，奧米加 3 通常很低，廚師就會煮針對性的食物，補充鐵、鎂、奧米加 3 等。」<cite>——諾里斯接受米芝蓮二星廚師 Sidney Schutte 訪問（GPFans 轉述，2025 年）</cite></blockquote>
<p>有趣的是，他賽後通常會吃一個漢堡：「這不算作弊，是體能教練給我的！」可見車手並非完全戒口，而是把「放縱餐」安排在適當時候。</p>

<h2 class="ao-h2" id="comfort">車手也有「放縱餐」</h2>
<p>再自律的車手也有心頭好。Red Bull 提到，韋斯塔潘（Max Verstappen）的「安慰食物」只是一碗番茄湯，那是他童年最愛；角田裕毅則是真正的「食家」，計劃退役後開一間融合日本菜與世界各地美食的餐廳。咸美頓亦承認自己愛吃班戟，又想念朱古力醬和糖果。前小紅牛車隊領隊 Franz Tost 的看法則很直接：營養是紀律的一部分，再美味的意大利肉腸也不應出現在他車手的餐碟上。</p>
<p>對一般觀眾而言，這正好說明：<b>平日吃得均衡，偶爾在派對上放縱一下並無不可</b>，重點是整體比例。</p>

<h2 class="ao-h2" id="schedule">2026 年餘下賽事香港時間：觀賽派對時間表</h2>
<p>按 F1 官方公布的 2026 年正賽開始時間（當地時間）換算，餘下六站的香港時間如下。不同時段適合不同的派對形式：</p>
<div class="ao-tw"><table class="ao-tbl"><thead><tr><th>分站</th><th>香港時間（正賽開始）</th><th>派對建議</th></tr></thead><tbody>
<tr><td>美國站（奧斯汀）</td><td>10 月 26 日（一）凌晨 4:00</td><td>清晨觀賽，賽後早餐聚會</td></tr>
<tr><td>墨西哥站</td><td>11 月 2 日（一）凌晨 4:00</td><td>清晨觀賽，賽後早餐聚會</td></tr>
<tr><td>巴西站</td><td>11 月 9 日（一）凌晨 1:00</td><td>深夜輕食，份量宜少</td></tr>
<tr><td>拉斯維加斯站</td><td>11 月 22 日（日）中午 12:00</td><td>⭐ 週日午餐派對</td></tr>
<tr><td>卡塔爾站</td><td>11 月 30 日（一）零時正</td><td>深夜輕食，份量宜少</td></tr>
<tr><td>阿布達比站（季尾戰）</td><td>12 月 6 日（日）晚上 9:00</td><td>⭐ 週日晚餐派對，最適合大型聚會</td></tr>
</tbody></table></div>
<p class="ao-tcap">按 F1 官方公布的當地開賽時間換算為香港時間（UTC+8）；如賽程有變，以 F1 官方公布為準。</p>

<h2 class="ao-h2" id="party">借鏡車手餐單：F1 觀賽派對到會怎樣揀？</h2>
<p>觀賽不用像車手般嚴格，但他們的飲食原則很適合用來安排一場健康又滿足的 {k('派對到會')}：</p>
<div class="ao-adv"><p class="t">來自 Kitchen AO 的建議</p>
<div class="r"><span class="n">🥗</span><div><b>先鋪滿蔬果，再加主菜</b><p>車手每餐都有沙律或水果。到會可多點一份沙律或蔬菜拼盤，讓大家先吃菜，自然不會吃得太膩。</p></div></div>
<div class="r"><span class="n">🍗</span><div><b>蛋白質選烤肉、海鮮或豆類</b><p>雞、魚是車手餐單的主角；燒烤肉類及海鮮比炸物清爽，素食朋友則可選豆類或「素」味人生套餐。</p></div></div>
<div class="r"><span class="n">🍝</span><div><b>主食份量適中</b><p>意粉、飯類可以有，但不必堆滿；跟車手一樣，碳水化合物「夠用就好」。</p></div></div>
<div class="r"><span class="n">⏰</span><div><b>按開賽時間決定吃甚麼</b><p>晚上 9 時的阿布達比站適合吃正餐；零時或凌晨開賽的分站，宜選手指食物及拼盤，避免深夜吃得太飽。</p></div></div>
<div class="r"><span class="n">💧</span><div><b>清水為主，酒精適量</b><p>車手在比賽中最重視補水。派對上可準備充足清水及無糖飲品，含酒精飲品適可而止。</p></div></div>
</div>
<p>Kitchen AO 的{a(AO + '/product-category/party/foot-party/', '美食派對 Gourmet 套餐')}適合阿布達比站等晚餐派對；{a(AO + '/product-category/party/refreshment-set/', '輕食宴會套餐')}及{a(AO + '/product-category/party/platter/', '手指食物拼盤')}適合深夜場；另可{a(AO + '/product-category/a-la-carte/salad/', '單點沙律')}增加蔬菜份量。素食朋友可選{a(AO + '/product-category/party/vegetarians-set/', '「素」味人生素食到會')}；公司舉辦 F1 主題活動，可參考{a(AO + '/business-event/', '商務活動到會')}或{a(AO + '/catering-quote-enquiry/', '索取報價')}。送貨範圍及免運費優惠，請參閱{a(AO + '/delivery/', '送貨需知')}。</p>
{CTA}
'''

faqs = [
 ('F1 車手一日吃甚麼？', '以 Red Bull 介紹的比賽週末餐單為例：早餐是燕麥粥配莓果、香蕉及果仁；午餐是沙律配雞胸、番茄莎莎及烚菜；晚餐是番茄湯、烤魚、番薯及沙律，甜品是水果或乳酪。'),
 ('F1 車手一場比賽會減多少磅？', 'RacingNews365 指一般流失約 2 至 3 公斤，主要是汗水；Red Bull 指在炎熱的新加坡站可達 3 至 4 公斤。'),
 ('F1 車手比賽期間可以吃東西嗎？', '不可以。車手只能透過頭盔上的飲管飲用含葡萄糖、礦物質及電解質的飲品，所以賽前數小時就要完成進食。'),
 ('F1 車手有體重限制嗎？', '有。FIA 自 2019 年起規定車手連頭盔、賽車服及鞋最少 80 公斤，不足的部分要在車上加配重，賽後亦會過磅。'),
 ('哪些 F1 車手吃素？', '最著名的是咸美頓，約於 2017 年轉吃植物性飲食。維特爾曾試過純素約六星期，之後恢復吃肉但少吃肉、多吃菜；勒克萊爾曾試吃純素，但表明喜歡牛肉；韋斯塔潘及諾里斯則吃肉，諾里斯不吃魚。'),
 ('在家觀賽需要喝運動飲品嗎？', '一般不需要。香港體育學院指運動飲品適合超過 90 分鐘的運動，或炎熱環境下超過 60 分鐘的高強度運動；坐着觀賽喝清水已足夠，過量飲用反而增加熱量。'),
 ('F1 觀賽派對到會怎樣安排？', '先看比賽的香港開始時間：晚上的分站可吃正餐，深夜或凌晨的分站宜選輕食及拼盤。菜式可參考車手原則——多蔬果、選烤肉海鮮、主食適量，並照顧素食朋友的需要。'),
]
srcs = [S[x] for x in ['rb', 'rbtw', 'bi', 'rn', 'fr', 'vfl', 'gpv', 'gpl', 'gpb', 'gpf', 'f1t', 'scmp', 'hksi', 'ao', 'del']]

QCSS = '<style>.ao-quote{margin:14px 0 16px!important;padding:12px 18px!important;background:#FAF7F1;border-left:4px solid #C8A24A;border-radius:0 12px 12px 0;font-size:16.5px;line-height:1.8;color:#3f3a33}.ao-quote cite{display:block;margin-top:6px;font-style:normal;font-size:13px;color:#7a6a45}.ao-tbl small{color:#7a6a45;font-size:12px}</style>'
body = QCSS + body
FRI = '<span class="ao-fri">🎉 逢星期五落單「素」味人生自動 95 折</span>'
KV = f'<style>.ao-kv.f1kv:after{{content:"🏎️🏁"}}</style><div class="ao-kv f1kv"><span class="k">F1 車手飲食 × 觀賽派對 2026</span><h1>{TITLE}</h1><p>咸美頓吃素、勒克萊爾愛牛肉、諾里斯不吃魚——看車手餐單，學辦一場健康又滿足的觀賽派對。</p></div>'
KV_WP = KV.replace('<h1>', '<div class="ttl" style="font-size:26px;font-weight:900;line-height:1.3;margin:0 0 10px">').replace('</h1>', '</div>')
OUT = HERE.parent
mock = C.page(PID, 'F1 車手飲食全攻略：一日餐單、營養重點及觀賽派對到會建議｜Kitchen AO',
              'F1 車手一日吃甚麼？整合 Red Bull、McLaren、F1 官方及香港體育學院資料，拆解車手餐單、碳水化合物、蛋白質及補水重點，附 2026 年餘下賽事香港時間及 F1 觀賽派對到會建議。',
              ['F1車手飲食', 'F1車手餐單', 'F1觀賽派對', '派對到會'], '', '', body, faqs, srcs, [], kv_html=KV).replace(FRI, '')
(OUT / 'f1-driver-diet-watch-party.html').write_text(mock, encoding='utf-8')
wp = C.wp_page(PID, body, faqs, srcs, [], KV_WP).replace(FRI, '')
(OUT / 'f1-driver-diet-watch-party-WORDPRESS.html').write_text(wp, encoding='utf-8')
print('f1 ok')
