# -*- coding: utf-8 -*-
"""聖誕到會場景頁：英文翻譯（給 build_a_christmas.py 生成中英自動切換版用）"""
import re
SER_EN = {'聖誕寶藏箱': 'Christmas Treasure Box', '聖誕金雞獻禮': 'Christmas Golden Roast', '聖誕開箱雙寶': 'Christmas Twin Treasures'}
FULL_EN = {'煙燻慢煮美國牛翼板肉盛宴': 'Smoked Slow-Cooked US Beef Chuck Flap Feast',
           '燒南乳香慢煮原隻黃油雞': 'Slow-Cooked Red Beancurd Whole Yellow Chicken',
           '原隻黃油雞 × 煙燻慢煮美國牛翼板肉': 'Whole Yellow Chicken × Smoked Slow-Cooked US Beef Chuck Flap',
           '燒南乳香慢煮原隻黃油雞 × 煙燻慢煮美國牛翼板肉': 'Whole Yellow Chicken × Smoked US Beef Chuck Flap'}
NAME_ALL = {**SER_EN, **FULL_EN}
D = {
 '｜聖誕套餐輸入優惠碼': '| Enter code', '享七九折，至 2026 年 11 月 30 日 23:59': 'for 21% off Christmas sets until 30 Nov 2026, 23:59',
 '首頁': 'Home', '到會場景': 'Catering Occasions', '/ 聖誕到會': '/ Christmas Catering',
 '聖誕到會 2026：燒南乳香慢煮原隻黃油雞聖誕套餐': 'Christmas catering 2026: slow-cooked red beancurd whole yellow chicken Christmas set',
 '聖誕到會 2026｜聖誕大餐外賣及派對套餐': 'Christmas Catering 2026 | Christmas Dinner Delivery & Party Sets',
 '原隻黃油雞、寶箱煙燻牛翼板肉及八款聖誕新菜，5 至 100 人聖誕派對一站配搭，送到你的餐桌。':
   'Whole yellow chicken, smoked beef chuck flap in a treasure box and eight new Christmas dishes. Everything for a Christmas party of 5 to 100 guests, delivered to your table.',
 '選購聖誕套餐': 'Shop Christmas Sets', 'WhatsApp 查詢': 'WhatsApp Us', '早鳥優惠：輸入': 'Early bird: enter', '聖誕套餐享七九折（21% OFF）': 'for 21% off Christmas sets',
 '2026 聖誕到會套餐': '2026 Christmas Catering Sets',
 'Kitchen AO 聖誕到會套餐專為 5 至 100 人的聖誕聚會而設，由家庭聖誕大餐、好友派對到公司聖誕派對，都可以按人數揀選。今年三大系列分別以寶箱煙燻慢煮美國牛翼板肉、燒南乳香慢煮原隻黃油雞為主角，配前菜、沙律、意粉及飯和甜品，一份聖誕到會餐單就能照顧全場賓客。':
   'Kitchen AO Christmas catering sets are designed for gatherings of 5 to 100 guests, from family Christmas dinners and parties with friends to office Christmas parties. Simply choose by headcount. This year\'s three series star our smoked slow-cooked US beef chuck flap in a treasure box and a slow-cooked red beancurd whole yellow chicken, with starters, salads, pasta and rice, and dessert. One Christmas catering menu takes care of every guest.',
 '平安夜及聖誕節是全年聖誕訂餐高峰，送貨時段有限，建議盡早預訂。': 'Christmas Eve and Christmas Day are the busiest days of the year and delivery slots are limited, so we recommend booking early.',
 '精選推介': 'Top Picks', '按人數揀': 'By Headcount', '按場合揀': 'By Occasion', '聖誕新菜': 'New Dishes', '送貨安排': 'Delivery', '常見問題': 'FAQ',
 '聖誕到會精選推介': 'Christmas Catering Top Picks',
 '由 5 人家庭聖誕大餐到 100 人公司聖誕派對，先看最受歡迎的六款聖誕套餐。': 'From a family Christmas dinner for 5 to an office party for 100, start with our six most popular Christmas sets.',
 '上一個': 'Previous', '下一個': 'Next', '上一組': 'Previous set', '下一組': 'Next set', 'Early Bird 七九折': 'Early Bird 21% Off',
 '2026 聖誕新菜': 'New Christmas Dishes 2026', '開箱，就是聖誕': 'Open the Box, It\'s Christmas',
 '按圖上的圓點，看看每款主菜屬於哪個聖誕套餐。': 'Tap the dots on the photo to see which Christmas set each main belongs to.',
 '查看套餐': 'View Set', '三大聖誕套餐系列': 'Three Christmas Set Series',
 '全部套餐均可自由配搭菜式，部分精選菜式需另加差價。': 'Every set can be customised. Some premium dishes carry a surcharge.',
 '查看系列頁': 'View series',
 '聖誕開箱雙寶同時送上原隻黃油雞及寶箱煙燻牛翼板肉兩款主菜，專為 48 至 100 人的公司年終派對、學校及機構聖誕活動而設。如需正式報價及收據，可經':
   'Christmas Twin Treasures brings two showpiece mains, a whole yellow chicken and smoked beef chuck flap in a treasure box, for year-end office parties and Christmas events at schools and organisations of 48 to 100 guests. For a formal quotation and receipt, please use our',
 '到會報價查詢': 'catering quote enquiry', '聯絡我們。': 'form.',
 '聖誕金雞獻禮以本地原隻黃油雞配南乳醃製，低溫慢煮後高溫炙燒，皮脆肉嫩，再配聖誕玫瑰金巴利汁，中西合璧。由 5-6 人小型聖誕聚會到 35-40 人大型聖誕派對都有合適份量。':
   'Christmas Golden Roast features a local whole yellow chicken marinated in red beancurd, slow-cooked then roasted at high heat for crisp skin and tender meat, served with a Christmas rose Campari sauce. East meets West, with portions for intimate gatherings of 5-6 up to large parties of 35-40.',
 '聖誕寶藏箱以稀有的美國牛翼板肉為主角，慢煮至五成熟再以煙燻木料炙烤，配八款聖誕新菜，適合 5 至 40 人的家庭聖誕大餐、好友派對及':
   'Christmas Treasure Box stars rare US beef chuck flap, slow-cooked to medium and finished over smoking wood, with eight new Christmas dishes. Ideal for family Christmas dinners, parties with friends and',
 '公司聖誕派對到會': 'office Christmas party catering', '。全港限量 100 個，送到即可開箱上桌。': ' of 5 to 40 guests. Limited to 100 boxes in Hong Kong, ready to open and serve on arrival.',
 '寶箱煙燻慢煮美國牛翼板肉': 'Treasure Box Smoked Slow-Cooked US Beef Chuck Flap', 'KITCHEN AO · 全港限量 100 個': 'KITCHEN AO · LIMITED TO 100 BOXES',
 '聖誕寶藏箱．煙燻慢煮美國牛翼板肉盛宴': 'Christmas Treasure Box · Smoked Slow-Cooked US Beef Chuck Flap Feast',
 'HK$1,928 起': 'From HK$1,928',
 '下肩胛翼板肉在日式燒肉稱為「羽下肉」或「座布團」，每頭牛僅約 2 至 3 公斤。油花細密均勻，慢煮至五成熟後以煙燻木料高溫炙烤，外層焦香、內裏鎖住肉汁，以復古寶箱盛載，開箱一刻就是全場焦點。':
   'Known in Japanese yakiniku as "zabuton", the chuck flap yields only about 2 to 3 kg per animal. Finely and evenly marbled, it is slow-cooked to medium then seared over smoking wood for a caramelised crust that locks in the juices. Served in a vintage treasure box, it steals the show the moment it opens.',
 '套餐包括：': 'The set includes:',
 '芒果粟子蓉冬日酥盒': 'Mango & Chestnut Winter Puff Pastry Cups', '明太子芝士忌廉牛角酥': 'Mentaiko Cream Cheese Croissants',
 '西班牙辣肉腸熔岩芝士杯': 'Spanish Chorizo Lava Cheese Cups', '紅寶神石榴沙律系列': 'Ruby Pomegranate Salad Series',
 '皇帝蟹棒蟹肉芒果牛油果沙律': 'King Crab Stick, Crab Meat, Mango & Avocado Salad', '雙重龍蝦三重芝士煲仔鍋飯': 'Double Lobster Three-Cheese Claypot Rice',
 '玫瑰醬泡菜海蝦意大利飯': 'Rosé Gochujang Kimchi Prawn Risotto', '聖誕馴鹿脆脆開心果朱古力撻': 'Christmas Reindeer Crunchy Pistachio Chocolate Tarts',
 '聖誕神秘加配：聖誕樹芝士火腿拼盤': 'Christmas Secret Add-on: Christmas Tree Cheese & Cold Cut Platter',
 '選擇人數': 'Choose Headcount', '套餐配搭說明': 'Customisation', '溫馨提示': 'Note',
 '套餐菜式可按喜好自由配搭；部分精選菜式需另加差價，實際價錢以落單頁面選項為準。': 'Dishes can be mixed and matched to your taste. Some premium dishes carry a surcharge, shown on the order page.',
 '煲仔鍋飯一般以原煲盛載；如瓦煲缺貨，會以錫紙盤代替，恕不另行通知。': 'Claypot rice is usually served in its original claypot. If claypots are out of stock, it will be served in a foil tray without prior notice.',
 '預留至少 30 分鐘緩衝時間；Party Room、辦公室及學校請先確認收貨安排。詳情見': 'Allow at least 30 minutes of buffer time. For party rooms, offices and schools, please confirm receiving arrangements in advance. See our',
 '送貨需知': 'delivery information', '按人數揀聖誕套餐': 'Choose a Christmas Set by Headcount',
 '輸入出席人數，即時建議合適的聖誕到會套餐。': 'Enter your headcount for an instant Christmas catering set suggestion.',
 '例如 20': 'e.g. 20', '建議套餐': 'Suggest a Set', '出席人數': 'Guests', '另一選擇': 'Alternative', '100 人以上': '100+ guests',
 '聖誕到會推介：按場合揀套餐': 'Christmas Catering Ideas by Occasion',
 '公司聖誕派對': 'Office Christmas Parties', '部門聚餐、年終派對及客戶活動，按人數揀套餐，可索取正式報價。': 'Team dinners, year-end parties and client events. Choose by headcount and request a formal quotation.',
 '公司聖誕派對到會 →': 'Office Christmas party catering →', '家庭聖誕聚會': 'Family Christmas Gatherings',
 '5 至 10 人小型套餐，一款原隻主菜配前菜、沙律、主食及甜品，在家輕鬆開餐。': 'Sets for 5 to 10 guests with a whole showpiece main, starters, salad, mains and dessert. Christmas dinner at home, made easy.',
 '揀家庭聖誕套餐 →': 'Family Christmas sets →', '學校、教會及機構': 'Schools, Churches & Organisations',
 '人數較多、年齡層闊，可加配兒童及素食選擇，並預先統計飲食需要。': 'Larger groups with all ages. Add children\'s and vegetarian options, and collect dietary needs in advance.',
 '到會報價查詢 →': 'Catering quote enquiry →', '素食朋友': 'Vegetarian Guests',
 '套餐以外可加配素食菜式，或選擇「素」味人生素食到會套餐。': 'Add vegetarian dishes to any set, or choose our vegetarian catering sets.',
 '素食到會套餐 →': 'Vegetarian catering sets →',
 '今年聖誕套餐全新加入的前菜、沙律、意粉及飯和甜品。': 'New starters, salads, pasta and rice, and desserts in this year\'s Christmas sets.',
 '原個布袋芝士切開即流心，飯底吸滿濃郁龍蝦汁': 'A whole burrata that oozes when cut, over rice soaked in rich lobster bisque',
 '韓式玫瑰醬配泡菜，奶香柔和、微辣開胃': 'Korean rosé sauce with kimchi, creamy with a gentle kick',
 '日本栗子蓉配新鮮芒果粒，酸甜開胃的前菜': 'Japanese chestnut purée with fresh mango, a sweet and tangy starter',
 '牛角酥夾入明太子芝士忌廉，鹹香柔滑': 'Croissants filled with mentaiko cream cheese, savoury and smooth',
 '大蝦柚肉或煙火雞胸蜜桃兩款任選': 'Choose prawn & pomelo or smoked turkey breast & peach',
 '開心果白朱古力配脆脆，朱古力曲奇鹿角': 'Pistachio white chocolate with crunchy pearls and chocolate cookie antlers',
 '聖誕小食及甜品加配': 'Christmas Snack & Dessert Add-ons', '人數較多或想更豐富，可加配單點小食及甜品。': 'For larger groups or a bigger spread, add à la carte snacks and desserts.',
 '惹味小食': 'Snacks', '雞翼、迷你漢堡、九層塔香酥雞等派對熱門小食。': 'Party favourites such as chicken wings, mini burgers and basil popcorn chicken.',
 '選購小食 →': 'Shop snacks →', '甜品': 'Desserts', '馬卡龍、芝士撻等一口甜品，為聖誕派對作結。': 'Bite-sized sweets such as macarons and cheese tarts to finish the party.',
 '選購甜品 →': 'Shop desserts →', '派對用品': 'Party Supplies', '餐具、暖貼及三層食物架，方便擺放及保溫。': 'Cutlery, heat packs and three-tier food stands for easy serving and keeping food warm.',
 '選購用品 →': 'Shop supplies →', '聖誕神秘加配': 'Christmas Secret Add-on',
 '聖誕樹芝士火腿拼盤，派對焦點冷盤，上桌即成拍照焦點。': 'Christmas Tree Cheese & Cold Cut Platter, a party showpiece and instant photo moment.',
 '於套餐內加配 →': 'Add within your set →', '平安夜及聖誕節到會送貨安排': 'Christmas Eve and Christmas Day catering delivery',
 '平安夜及聖誕節送貨安排': 'Christmas Eve & Christmas Day Delivery',
 '平安夜（12 月 24 日）及聖誕節（12 月 25 日）熱門時段較快額滿，宜盡早確定日期及時間。': 'Popular slots on Christmas Eve (24 Dec) and Christmas Day (25 Dec) fill up quickly, so confirm your date and time early.',
 '預留至少 30 分鐘緩衝時間，避免開餐與送貨時間太接近。': 'Allow at least 30 minutes of buffer between delivery and mealtime.',
 '落單時寫清楚收貨人、電話及大廈資料；Party Room、辦公室及學校請先確認收貨安排。': 'Include the recipient, phone number and building details when ordering. For party rooms, offices and schools, please confirm receiving arrangements in advance.',
 '查看送貨需知': 'Delivery Information',
 '部門聚餐、年終派對及客戶活動，按人數配搭聖誕套餐，可索取正式報價及收據。': 'Team dinners, year-end parties and client events. Build your Christmas sets by headcount, with formal quotations and receipts available.',
 '公司到會方案': 'Corporate Catering', '聖誕到會常見問題': 'Christmas Catering FAQ',
 '聖誕到會要提早幾多日預訂？': 'How far in advance should I book Christmas catering?',
 '平安夜及聖誕節是全年到會高峰，熱門送貨時段較快額滿，建議盡早預訂。2026 年 11 月 30 日 23:59 前輸入優惠碼 MEGA79，聖誕套餐更可享七九折。':
   'Christmas Eve and Christmas Day are the busiest catering days of the year and popular delivery slots fill up quickly, so we recommend booking early. Enter code MEGA79 before 30 Nov 2026, 23:59 for 21% off Christmas sets.',
 '平安夜及聖誕節可以送貨嗎？': 'Do you deliver on Christmas Eve and Christmas Day?',
 '可以按落單頁面提供的日期及時段送貨。平安夜（12 月 24 日）及聖誕節（12 月 25 日）時段有限，建議預留至少 30 分鐘緩衝時間，詳情可參考送貨需知。':
   'Yes, on the dates and time slots shown on the order page. Slots on Christmas Eve (24 Dec) and Christmas Day (25 Dec) are limited. Please allow at least 30 minutes of buffer time and see our delivery information for details.',
 '聖誕到會套餐每位大約幾錢？': 'How much does Christmas catering cost per person?',
 'Kitchen AO 2026 聖誕套餐以原價計，每位約 HK$226 至 386，人數愈多每位愈低；11 月 30 日前以 MEGA79 再享七九折。':
   'At regular prices, Kitchen AO 2026 Christmas sets cost about HK$226 to 386 per person, and less per person for larger groups. Enter MEGA79 before 30 Nov for a further 21% off.',
 '聖誕大餐吃什麼？': 'What should I serve for Christmas dinner?',
 '一桌完整的聖誕大餐一般包括一至兩款焦點主菜（例如原隻燒雞或燒牛肉）、前菜、沙律、意粉或飯，以及甜品。Kitchen AO 聖誕套餐已按人數配搭好以上各類菜式。':
   'A complete Christmas dinner usually includes one or two showpiece mains (such as a whole roast chicken or roast beef), starters, salad, pasta or rice, and dessert. Kitchen AO Christmas sets include all of these, portioned by headcount.',
 '聖誕套餐有沒有火雞？': 'Do your Christmas sets include turkey?',
 '2026 年聖誕套餐的主菜為燒南乳香慢煮原隻黃油雞及寶箱煙燻慢煮美國牛翼板肉。如有其他主菜需要，歡迎 WhatsApp 查詢。':
   'Our 2026 Christmas mains are a slow-cooked red beancurd whole yellow chicken and smoked slow-cooked US beef chuck flap in a treasure box. For other mains, please ask us on WhatsApp.',
 '10 人或 20 人聖誕派對應揀哪個套餐？': 'Which set should I choose for 10 or 20 guests?',
 '10 人可選 8-10 人套餐；20 人可選 18-22 人套餐。人數介乎兩個套餐之間時，可選較大的套餐，或選較小的套餐再加配單點小食，詳見上方「按人數揀聖誕套餐」。':
   'For 10 guests, choose the 8-10 pax set. For 20 guests, choose the 18-22 pax set. If your headcount falls between two sets, choose the larger set, or the smaller set plus à la carte snacks. See "Choose a Christmas Set by Headcount" above.',
 '聖誕套餐的菜式可以更換嗎？': 'Can I change the dishes in a Christmas set?',
 '可以加素食或兒童菜式嗎？': 'Can I add vegetarian or children\'s dishes?',
 '可以在套餐以外加配單點小食及甜品，素食朋友亦可選擇「素」味人生素食到會套餐。': 'Yes. You can add à la carte snacks and desserts to any set, and vegetarian guests can choose our vegetarian catering sets.',
 '公司聖誕派對可以索取報價嗎？': 'Can I get a quotation for an office Christmas party?',
 '可以。公司、學校及機構訂購如需正式報價及收據，可經到會報價查詢聯絡我們。': 'Yes. Companies, schools and organisations needing a formal quotation and receipt can contact us through our catering quote enquiry form.',
 '聖誕到會包括餐具嗎？': 'Is cutlery included?',
 '落單時可選擇是否需要碟及餐具，亦可加配食物夾等用品。': 'You can choose plates and cutlery when ordering, and add serving tongs and other supplies.',
 '今年聖誕，交給 Kitchen AO': 'This Christmas, Leave It to Kitchen AO',
 '5 至 100 人聖誕到會套餐，11 月 30 日前 MEGA79 七九折。': 'Christmas catering sets for 5 to 100 guests. 21% off with MEGA79 until 30 Nov.',
 # JS
 '｜尚餘 ': ' | ', ' 天 ': ' days ', ' 小時': ' hrs left',
 '請輸入人數': 'Please enter a headcount', '100 人以上請經到會報價查詢聯絡我們': 'For 100+ guests, please use our catering quote enquiry',
 '建議：': 'Suggested: ', '，或 ': ', or ', ' 人套餐加配單點': ' pax set plus à la carte',
}
def money_en(m): return m
# ---- 2026-11-19 新增 ----
D.update({'本地原隻黃油雞以南乳醃製及鹽水浸漬，低溫慢煮後高溫炙燒至皮脆肉嫩，配聖誕玫瑰金巴利汁，專屬木箱盛載，全港限量 100 個。': 'Local whole yellow chicken marinated in red beancurd and brined, slow-cooked then roasted until crisp-skinned and tender, served with festive rose Campari sauce in its own wooden box. Limited to 100 sets in Hong Kong.', '聖誕金雞獻禮以本地原隻黃油雞配南乳醃製，低溫慢煮後高溫炙燒，皮脆肉嫩，再配聖誕玫瑰金巴利汁。全港限量 100 個，由 5-6 人小型聖誕聚會到 35-40 人大型聖誕派對都有合適份量。': 'Christmas Golden Roast features a whole local yellow chicken marinated in red beancurd, slow-cooked then roasted for crisp skin and tender meat, served with festive rose Campari sauce. Limited to 100 sets in Hong Kong, with portions from intimate gatherings of 5–6 to parties of 35–40.', '聖誕套餐供應及送貨日期': 'Christmas Set Availability', '12 月 19 日前，其他套餐及單點照常供應。': 'Other sets and à la carte items are available as usual until 19 December.', '除企業訂單外，其他日子不供應': 'Outside these dates, apart from corporate orders, we do not offer ', '聖誕套餐': 'Christmas sets', '套餐供應情況會持續於網站更新，請密切留意網站內容及參閱': 'Availability will be updated on our website. Please check regularly and see our ', '聖誕套餐於 2026 年 12 月 12 日至 27 日供應及送貨；平安夜及聖誕節是全年聖誕訂餐高峰，送貨時段有限，建議盡早預訂。': 'Christmas sets are available for delivery from 12 to 27 December 2026. Christmas Eve and Christmas Day are our busiest days, with limited delivery slots, so please book early.', '聖誕套餐供應及送貨日期為 12 月 12 日至 27 日；12 月 19 日前，其他套餐及單點照常供應。': 'Christmas sets are available for delivery from 12 to 27 December; other sets and à la carte items are available as usual until 19 December.', '慢煮數小時，煙燻數分鐘，開箱驚喜只需一秒。': '', '每款均可配八款 XMAS SPECIAL 全新菜式': 'each available with eight new XMAS SPECIAL dishes', '聖誕套餐甚麼日子供應？': 'When are the Christmas sets available?', '聖誕套餐於 2026 年 12 月 12 日至 12 月 27 日供應及送貨。12 月 19 日前，其他套餐及單點照常供應；除企業訂單外，其他日子不供應聖誕套餐。供應情況會持續於網站更新，請留意送貨需知。': 'Christmas sets are available for delivery from 12 to 27 December 2026. Other sets and à la carte items are available as usual until 19 December. Apart from corporate orders, Christmas sets are not offered on other dates. Availability will be updated on our website, so please check our delivery information.'})

def tr(t):
    """翻譯一段中文；找不到回傳 None"""
    if t in D: return D[t]
    if t in NAME_ALL: return NAME_ALL[t]
    m = re.fullmatch(r'(\d+)-(\d+)人(聖誕寶藏箱|聖誕金雞獻禮|聖誕開箱雙寶)聖誕套餐', t)
    if m: return f'{m[1]}-{m[2]} pax {SER_EN[m[3]]} Christmas Set'
    m = re.fullmatch(r'(聖誕寶藏箱|聖誕金雞獻禮|聖誕開箱雙寶)聖誕套餐', t)
    if m: return f'{SER_EN[m[1]]} Christmas Set'
    m = re.fullmatch(r'(\d+)–(\d+) 人(.*)聖誕套餐', t)
    if m: return f'{m[1]}–{m[2]} Guests' + (f' {FULL_EN[m[3]]}' if m[3] else '') + ' Christmas Set'
    m = re.fullmatch(r'MEGA79 後(約)? (HK\$[\d,]+)( 起)?', t)
    if m: return ('From ' if m[3] else 'Approx. ' if m[1] else '') + f'{m[2]} with MEGA79'
    m = re.fullmatch(r'每位約 (HK\$[\d,]+)–(HK\$[\d,]+)', t)
    if m: return f'Approx. {m[1]}–{m[2]} per guest'
    m = re.fullmatch(r'(\d+) 款套餐 ·', t)
    if m: return f'{m[1]} sets ·'
    m = re.fullmatch(r'KITCHEN AO · (.+)', t)
    if m and m[1] in SER_EN: return f'KITCHEN AO · {SER_EN[m[1]].replace("Christmas ", "").upper()}'
    m = re.fullmatch(r'(\d+) 至 (\d+) 人', t)
    if m: return f'{m[1]}–{m[2]} guests'
    m = re.fullmatch(r'(\d+) 人', t)
    if m: return f'{m[1]} guests'
    m = re.fullmatch(r'(\d+-\d+) 人套餐', t)
    if m: return f'{m[1]} pax set'
    m = re.fullmatch(r'(\d+-\d+) 人開箱雙寶', t)
    if m: return f'{m[1]} pax Twin Treasures'
    m = re.fullmatch(r'或 (\d+-\d+) 人(套餐)?加配單點', t)
    if m: return f'or {m[1]} pax set plus à la carte'
    m = re.fullmatch(r'第 (\d+) 組', t)
    if m: return f'Set {m[1]}'
    m = re.fullmatch(r'(\d+-\d+) 人套餐（寶藏箱 (HK\$[\d,]+)／金雞獻禮 (HK\$[\d,]+)）', t)
    if m: return f'{m[1]} pax set (Treasure Box {m[2]} / Golden Roast {m[3]})'
    m = re.fullmatch(r'(\d+-\d+) 人開箱雙寶（(HK\$[\d,]+)）', t)
    if m: return f'{m[1]} pax Twin Treasures ({m[2]})'
    return None

D.update({'聖誕套餐只限': 'Christmas sets available', '供應': 'only', '詳情': 'Details'})
D.update({'慢煮數小時': '', '煙燻數分鐘': '', '開箱驚喜只需一秒': ''})
D.update({'開箱': '', '驚喜': '', '只需一秒': ''})
# Hero 中英一樣：中文行保留（build 時還原）
HERO_ZH = {'@@Z1@@': '慢煮數小時', '@@Z2@@': '煙燻數分鐘', '@@Z3@@': '開箱', '@@Z4@@': '驚喜', '@@Z5@@': '只需一秒'}
D.update({v: k for k, v in HERO_ZH.items()})
HERO_ZH['@@Z6@@'] = '，就是聖誕'; D['，就是聖誕'] = '@@Z6@@'
D.update({'聖誕到會 2026｜': 'Christmas Catering 2026 |', '聖誕大餐外賣及派對套餐': 'Christmas Dinner Delivery & Party Sets'})
D.update({'聖誕到會 2026': 'Christmas Catering 2026'})
D.update({'聖誕到會 2026：聖誕寶藏箱': 'Christmas catering 2026: Christmas Treasure Box'})
D.update({'開箱：聖誕寶藏箱煙燻慢煮美國牛翼板肉': 'Open the box: Christmas Treasure Box with smoked slow-cooked US beef chuck flap'})
HERO_ZH['@@Z7@@'] = '開箱，'; D['開箱，'] = '@@Z7@@'
HERO_ZH['@@Z8@@'] = '就是聖誕'; D['就是聖誕'] = '@@Z8@@'
D.update({'開箱：聖誕寶藏箱、原隻黃油雞及聖誕新菜': 'Open the box: Christmas Treasure Box, whole yellow chicken and new Christmas dishes'})
D.update({'菜式詳細介紹': 'Dish Details'})
D.update({'2026 聖誕主菜': 'Our Christmas Mains', '原隻連木箱送到': 'Delivered with the Whole Box Set', '連復古寶箱送到': 'Delivered with the Whole Treasure Box'})
D.update({'聖誕金雞獻禮．燒南乳香慢煮原隻黃油雞': 'Christmas Golden Roast · Slow-Cooked Red Beancurd Whole Yellow Chicken'})
D.update({'聖誕主菜': 'Christmas Mains', '三大套餐系列': 'Set Series', '小食及甜品': 'Snacks & Desserts', '頁內導覽': 'On this page'})
D.update({'查看完整聖誕餐牌': 'View Full Christmas Menu'})
D.update({'套餐系列': 'Set Series', '小食甜品': 'Add-ons', '菜式介紹': 'Dish Details', '按人數揀': 'Headcount', '按場合揀': 'Occasions'})
D.update({'聖誕主菜': 'Mains'})
HERO_ZH['@@Z9@@'] = '今年，交給 Kitchen AO'; D['今年，交給 Kitchen AO'] = '@@Z9@@'
D.update({'精心呈獻三大聖誕套餐，照顧不同聚會需要，與摯愛分享開箱的寶藏。': 'We proudly present our Christmas sets to suit every gathering. Share the treasures with your loved ones.'})
HERO_ZH['@@Z10@@'] = '今年，交給'; D['今年，交給'] = '@@Z10@@'
