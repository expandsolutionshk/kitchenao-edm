# -*- coding: utf-8 -*-
"""全網英文 Meta（2026-10-28）：頁面 52、Blog 17、產品 156、產品分類 38
資料來源：aoaodelivery.com 網站地圖逐頁讀取的頁面 ID 及中文 Title；英文由 Claude 撰寫（英式英文）
kind: page / post / product / term / special（shop、blog 列表頁，匯入時自動找 ID）
"""

def dish(n): return f'{n}, freshly made by Kitchen AO for parties and corporate events. Order online with delivery across Hong Kong.'
def drink(n): return f'Add {n} to your Kitchen AO catering order. Drinks are delivered together with your party food across Hong Kong.'
def supply(n): return f'{n} for your party table. Add it to your Kitchen AO catering order for delivery across Hong Kong.'
def canape(n): return f'{n}: a bite-sized canapé by Kitchen AO for receptions and corporate events, delivered across Hong Kong.'
def dessert(n): return f'{n} from Kitchen AO, a sweet treat for parties and office celebrations, delivered across Hong Kong.'
def gourmet(p): return f'Kitchen AO Gourmet party set for {p} guests: hot mains, pasta, salads and snacks in one order. Delivered across Hong Kong. Order online or get a quote.'
def refresh(p): return f'Kitchen AO refreshment set for {p} guests: light bites and snacks for meetings, seminars and tea receptions. Delivered across Hong Kong.'
def veg(p, price): return f'Vegetarian catering set for {p} guests from {price}: snacks, salad, pasta and mains, all meat-free. Order three days ahead; delivered across Hong Kong.'
def boat(p): return f'Kitchen AO boat party set for {p} guests: party food packed for junk trips and yacht parties, with delivery to the pier in Hong Kong.'
def district(a, extra): return f'Catering delivery in {a}: Kitchen AO party sets, lunch boxes and canapés{extra}. Free delivery on orders over HK$1,450.'

T = 'term'; P = 'page'; B = 'post'; PR = 'product'

DATA = [
# ---------------- 頁面 ----------------
(P, 3, 'Privacy Policy', 'Privacy Policy | Kitchen AO', 'How Kitchen AO collects, uses and protects your personal data when you browse our website, send an enquiry or place a catering order.'),
(P, 17, '關於 Kitchen AO', 'About Kitchen AO | Hong Kong Catering Brand & Chef Team', 'Discover the story, chef team and catering philosophy behind Kitchen AO. We serve corporate events, parties and family gatherings across Hong Kong.'),
(P, 2025, '聯絡我們', 'Contact Us | Kitchen AO Catering Hong Kong', 'Contact Kitchen AO by WhatsApp, phone or email for catering menus, quotes and delivery arrangements for parties and corporate events in Hong Kong.'),
(P, 5924, '購買流程', 'How to Order Catering Online | Kitchen AO Hong Kong', 'A step-by-step guide to ordering Kitchen AO catering online: browse menus, add to cart, enter delivery details and confirm your order.'),
(P, 5927, '送貨需知', 'Free Catering Delivery Hong Kong | Fees & Times | Kitchen AO', 'Delivery fees for Hong Kong Island, Kowloon and the New Territories. Free delivery on orders over HK$1,450, delivery time slots and typhoon arrangements.'),
(P, 6029, '最新消息', 'Latest News & Offers | Kitchen AO Catering', 'The latest catering offers, seasonal menus and member promotions from Kitchen AO in Hong Kong.'),
(P, 6051, '常見問題', 'Catering FAQ | Ordering & Delivery | Kitchen AO Hong Kong', 'Answers to common questions about ordering, delivery times, delivery fees, minimum spend and menu suggestions for Kitchen AO catering in Hong Kong.'),
(P, 6053, '派對美食食物', 'Party Food Catering Hong Kong | Birthday Party | Kitchen AO', 'Party food catering for birthdays and celebrations in Hong Kong: finger food, hot dishes, desserts and kids menus, delivered to your venue.'),
(P, 6341, '商務活動', 'Business Event Catering Hong Kong | Kitchen AO', 'Catering for business meetings, product launches, openings and receptions in Hong Kong. Finger food, canapés and buffets arranged to suit your event.'),
(P, 7014, '首頁', 'Catering Hong Kong | Party & Corporate Catering | Kitchen AO', 'Kitchen AO provides catering across Hong Kong for birthday parties, corporate events and boat parties. Browse party sets, get a quote and order online.'),
(P, 7024, '遊船河到會', 'Boat Party Catering Hong Kong | Junk Trip Food | Kitchen AO', 'Boat party and junk trip catering in Hong Kong: party sets for 15 to 40 guests, packed for the boat and delivered to the pier.'),
(P, 7032, '小食到會推介', 'Finger Food & Wedding Catering Hong Kong | Kitchen AO', 'Finger food and snack catering for weddings, cocktail receptions and parties in Hong Kong. Bite-sized dishes delivered ready to serve.'),
(P, 9249, '商業活動照片', 'Corporate Event Catering Gallery | Kitchen AO', 'Photos of Kitchen AO catering at corporate events, product launches and business receptions in Hong Kong.'),
(P, 10436, '高級餐盒', 'Executive Meal Boxes Hong Kong | Kitchen AO', 'Premium executive meal boxes for board meetings, VIP guests and corporate lunches in Hong Kong, delivered to your office.'),
(P, 10443, '員工膳食餐盒', 'Staff Meal Boxes Hong Kong | Team Lunch | Kitchen AO', 'Staff meal boxes for team lunches, training days and shift workers in Hong Kong. Balanced meals delivered to your office.'),
(P, 10477, '商務餐盒', 'Corporate Lunch Boxes Hong Kong | Meetings | Kitchen AO', 'Corporate lunch boxes for meetings, seminars and office lunches in Hong Kong, delivered on time to your workplace.'),
(P, 10737, '報價查詢', 'Catering Quote Hong Kong | Party & Corporate | Kitchen AO', 'Tell us your event date, headcount and budget, and Kitchen AO will send a tailored catering menu and quote for your party, corporate event or gathering.'),
(P, 10740, '皇家小食盒', 'Royal Snack Boxes | Canapé Catering Hong Kong | Kitchen AO', 'Royal snack boxes of premium canapés for VIP receptions, cocktail events and corporate gatherings in Hong Kong.'),
(P, 10744, '飲品及雞尾酒服務', 'Drinks & Cocktail Service Hong Kong | Kitchen AO', 'Drinks and cocktail service for receptions, openings and parties in Hong Kong, arranged together with your Kitchen AO catering.'),
(P, 10940, '舌尖上的餐桌', 'Gourmet Canapé Box | 9-Grid Canapés | Kitchen AO', 'A box of nine gourmet canapés for receptions, meetings and gifts. Elegant bite-sized catering from Kitchen AO, delivered across Hong Kong.'),
(P, 11197, '合作夥伴與服務實績', 'Partners & Client Portfolio | Kitchen AO Catering', 'Kitchen AO has catered for companies, healthcare organisations, schools and public bodies in Hong Kong. See selected partners and enquire today.'),
(P, 11204, '精選圖庫', 'Catering Photo Gallery | Kitchen AO Hong Kong', 'Browse photos of Kitchen AO catering at corporate events, openings, weddings and parties across Hong Kong.'),
(P, 11216, '客人好評', 'Customer Reviews | Kitchen AO Catering Hong Kong', 'Read what customers say about Kitchen AO catering for parties, corporate events and family gatherings in Hong Kong.'),
(P, 12099, '母親手作盆菜', 'Handmade Poon Choi | Kitchen AO Hong Kong', 'Handmade poon choi from Kitchen AO for Chinese New Year and family gatherings, delivered across Hong Kong.'),
(P, 14653, '婚禮活動照片', 'Wedding Catering Gallery | Kitchen AO Hong Kong', 'Photos of Kitchen AO catering at weddings and wedding receptions in Hong Kong.'),
(P, 14689, '開張活動照片', 'Grand Opening Catering Gallery | Kitchen AO', 'Photos of Kitchen AO catering at shop openings and launch events in Hong Kong.'),
(P, 14961, '地區到會分類', 'Catering by District | Hong Kong Delivery | Kitchen AO', 'Find Kitchen AO catering delivery in your district, from Central and Causeway Bay to Kwun Tong, Sha Tin and Yuen Long.'),
(P, 14963, '荃灣到會', 'Catering Tsuen Wan 2026 | Party Food Delivery | Kitchen AO', district('Tsuen Wan', '')),
(P, 14968, '中環到會', 'Catering Central Hong Kong 2026 | Kitchen AO', district('Central', ' for offices and events')),
(P, 14972, '銅鑼灣到會', 'Catering Causeway Bay 2026 | Party Food Delivery | Kitchen AO', district('Causeway Bay', '')),
(P, 14981, '灣仔到會', 'Catering Wan Chai 2026 | Corporate & Party | Kitchen AO', district('Wan Chai', ' for the convention district')),
(P, 14984, '鰂魚涌到會', 'Catering Quarry Bay 2026 | Office Catering | Kitchen AO', district('Quarry Bay', ' for Taikoo Place offices')),
(P, 14988, '北角到會', 'Catering North Point 2026 | Party Food Delivery | Kitchen AO', district('North Point', '')),
(P, 15011, '西營盤到會', 'Catering Sai Ying Pun 2026 | Party Food Delivery | Kitchen AO', district('Sai Ying Pun', '')),
(P, 15014, '九龍城到會', 'Catering Kowloon City 2026 | Party Food Delivery | Kitchen AO', district('Kowloon City', '')),
(P, 15017, '觀塘到會', 'Catering Kwun Tong 2026 | Corporate Catering | Kitchen AO', district('Kwun Tong', ' for Kowloon East offices')),
(P, 15020, '旺角到會', 'Catering Mong Kok 2026 | Party Room & Corporate | Kitchen AO', district('Mong Kok', ' for party rooms')),
(P, 15023, '深水埗到會', 'Catering Sham Shui Po 2026 | Party Food Delivery | Kitchen AO', district('Sham Shui Po', '')),
(P, 15027, '尖沙咀到會', 'Catering Tsim Sha Tsui 2026 | Event Catering | Kitchen AO', district('Tsim Sha Tsui', ' for events')),
(P, 15029, '元朗到會', 'Catering Yuen Long 2026 | Family Party Food | Kitchen AO', district('Yuen Long', ' for family parties')),
(P, 15033, '沙田到會', 'Catering Sha Tin 2026 | Family & Corporate | Kitchen AO', district('Sha Tin', '')),
(P, 15035, '屯門到會', 'Catering Tuen Mun 2026 | Party & BBQ Food | Kitchen AO', district('Tuen Mun', ' for family parties')),
(P, 15421, '客製化紀念品', 'Custom Souvenirs & Corporate Gifts Hong Kong | Kitchen AO', 'Kitchen AO creates custom souvenirs and corporate gifts, from design and production to delivery. Ideal for company events, staff rewards and festive gifts.'),
(P, 18404, '公司到會', 'Corporate Catering Hong Kong | Annual Dinner & Office Lunch', 'Corporate catering in Hong Kong for annual dinners, office lunches, openings and anniversaries. Menus tailored to headcount and budget. Request a quote.'),
(P, 18568, '服務概覽', 'Our Catering Services | Kitchen AO Hong Kong', 'An overview of Kitchen AO catering services in Hong Kong: party sets, corporate lunch boxes, canapés, boat party food and custom gifts.'),
(P, 18621, '到會推介', 'Hong Kong Catering Recommendations 2026 | Kitchen AO', 'Looking for catering recommendations in Hong Kong? Kitchen AO caters corporate events, birthday parties and family gatherings with flexible menus and delivery.'),
(P, 21018, '中秋月餅預訂', 'Mooncake Pre-order 2026 | Custom Logo Gift Boxes | Kitchen AO', 'Pre-order lava custard mooncakes for Mid-Autumn Festival 2026, with corporate gift boxes printed with your company logo.'),
('special', 'shop', '商店', 'Shop Catering Online | Kitchen AO Hong Kong', 'Shop Kitchen AO catering online: party sets, à la carte dishes, desserts, drinks and party supplies, delivered across Hong Kong.'),
('special', 'blog', 'Blog', 'Catering Blog | Party & Event Tips | Kitchen AO Hong Kong', 'Guides and ideas for party catering, corporate events, festivals and vegetarian menus in Hong Kong from the Kitchen AO team.'),
# ---------------- Blog ----------------
(B, 14128, '到會中伏', 'How to Avoid Catering Mistakes: 5 Pitfalls | Kitchen AO', 'Five common catering pitfalls in Hong Kong and how to avoid them, with expert tips on menus, quantities, delivery and budget.'),
(B, 14164, '公司活動到會', 'Corporate Event Catering Guide 2026 | Budget & Menus | Kitchen AO', 'Plan corporate event catering in Hong Kong: budget per head, menu ideas, service options and timelines for a professional event.'),
(B, 14183, '小朋友生日會', 'Kids Birthday Party Catering 2026 | Hong Kong Guide | Kitchen AO', 'How to choose kids birthday party catering in Hong Kong: child-friendly menus, portions, allergies and party set ideas.'),
(B, 14400, '激光打印食物', 'Laser-Printed Party Food | Custom Burgers & Macarons | Kitchen AO', 'Laser-printed burgers and engraved macarons: a new way to personalise party food and corporate events in Hong Kong.'),
(B, 14610, '母親節', "Mother's Day Catering Offer | Free Handmade Cookies | Kitchen AO", "Celebrate Mother's Day with Kitchen AO catering and receive free handmade cookies with your order. Delivered across Hong Kong."),
(B, 14795, '素食到會', 'Vegetarian Catering Hong Kong 2026 | Party Guide | Kitchen AO', 'How to cater for vegetarian guests at your party: meat-free menu ideas, labelling tips and vegetarian catering sets in Hong Kong.'),
(B, 14835, '船河食物', 'Boat Party Food Checklist 2026 | Junk Trip Catering | Kitchen AO', 'Everything you need for a Hong Kong junk trip: boat party food checklist, quantities, packing tips and free-delivery catering sets.'),
(B, 15897, '中秋', 'Mid-Autumn Festival Catering 2026 | Reunion Sets | Kitchen AO', 'Six Mid-Autumn reunion catering sets and corporate mooncakes for family gatherings and company celebrations in Hong Kong.'),
(B, 16290, '萬聖節', 'Halloween Party Catering 2026 | Party Food Ideas | Kitchen AO', 'Halloween party food ideas and catering sets for 2026, plus the story behind Halloween. Spooky party catering delivered across Hong Kong.'),
(B, 16468, '聖誕', 'Christmas Party Catering Hong Kong | Festive Sets | Kitchen AO', 'Christmas party catering sets with festive dishes delivered across Hong Kong, for family gatherings and office Christmas parties.'),
(B, 17646, '團年飯', 'Chinese New Year Reunion Dinner Guide 2026 | Kitchen AO', 'Reunion dinner and opening dinner explained: Chinese New Year traditions, lucky dishes and their meanings for 2026.'),
(B, 18461, '到會邊間好', 'Best Catering in Hong Kong 2026 | How to Compare | Kitchen AO', 'Which catering service in Hong Kong is best for you? Compare menus, prices, delivery and service with our 2026 checklist.'),
(B, 18495, '公司到會點揀', 'How to Choose Corporate Catering in Hong Kong | Kitchen AO', 'Five key points for choosing quality corporate catering in Hong Kong, from menu variety and food safety to punctual delivery.'),
(B, 21808, '野餐好去處', 'Best Picnic Spots in Hong Kong 2026 | 33 Parks | Kitchen AO', '33 picnic spots in Hong Kong with large lawns, sea views and pet-friendly areas, plus parking tips and picnic box ideas.'),
(B, 21876, '素食種類', 'Types of Vegetarian Diets Explained | Kitchen AO', 'Lacto-ovo, five-pungent-free, vegan and plant-based: a clear guide to the types of vegetarian diets common in Hong Kong.'),
(B, 21890, 'Vegan Vegetarian 中文', 'Vegan vs Vegetarian: Meanings in Chinese | Kitchen AO', 'What vegan, vegetarian, flexitarian and pescatarian mean, with the Chinese terms used in Hong Kong, Taiwan and the West.'),
# ---------------- 產品分類 ----------------
(T, 15, '其他', 'Other Items | Kitchen AO Catering', 'Other catering items and add-ons from Kitchen AO, delivered with your party order across Hong Kong.'),
(T, 21, '派對到會套餐', 'Party Catering Sets Hong Kong | Kitchen AO', 'Party catering sets for birthdays, office parties and family gatherings in Hong Kong, for 2 to 100+ guests. Order online with delivery.'),
(T, 24, '輕食宴會套餐', 'Refreshment Sets | Meeting & Tea Catering | Kitchen AO', 'Refreshment sets of light bites for meetings, seminars and tea receptions in Hong Kong, for 12 to 40 guests.'),
(T, 25, '雙人套餐', 'Couple Sets | Dinner for Two Delivery | Kitchen AO', 'Dinner sets for two for anniversaries and special occasions, delivered to your home across Hong Kong.'),
(T, 26, '手指食物拼盤', 'Finger Food Platters Hong Kong | Kitchen AO', 'Finger food platters for parties and receptions in Hong Kong. Choose your own combination, delivered ready to serve.'),
(T, 40, '甜品', 'Desserts & Sweet Treats | Catering Hong Kong | Kitchen AO', 'Macarons, mini tarts, jelly cups and more: dessert catering for parties and office celebrations, delivered across Hong Kong.'),
(T, 45, '單點美食', 'À La Carte Catering Menu Hong Kong | Kitchen AO', 'Build your own catering menu with à la carte snacks, salads, pasta, mains, seafood and desserts, delivered across Hong Kong.'),
(T, 64, '餐具及暖貼加配', 'Tableware & Food Warmers | Party Add-ons | Kitchen AO', 'Add plates, cutlery, food tongs and heat packs to your catering order to keep party food warm and ready to serve.'),
(T, 66, '美食派對 Gourmet Set', 'Gourmet Party Sets by Headcount | Kitchen AO', 'Gourmet party sets for 5 to 30 guests with hot mains, pasta, salads and snacks. Choose by headcount and order online.'),
(T, 67, '兒童套餐', 'Kids Party Sets | Children Catering Hong Kong | Kitchen AO', "Kids party catering sets with child-friendly dishes for birthdays and school events in Hong Kong, from 5 children."),
(T, 80, '冷盤小食', 'Cold Platters & Starters | Party Catering | Kitchen AO', 'Cold platters and starters for parties: chilled appetisers and cold cuts, delivered with your Kitchen AO catering order.'),
(T, 81, '惹味小食', 'Party Snacks: Fried Bites & Skewers | Kitchen AO', 'Crowd-pleasing party snacks including fried bites, chicken wings and satay skewers, delivered across Hong Kong.'),
(T, 82, '沙律', 'Salads | Catering Hong Kong | Kitchen AO', 'Fresh salads for parties and office lunches, from Caesar salad to seafood and chicken salads, delivered across Hong Kong.'),
(T, 83, '意粉 / 意大利飯', 'Pasta & Risotto Catering | Kitchen AO Hong Kong', 'Baked pasta, cream pasta and risotto in party trays, freshly prepared and delivered across Hong Kong.'),
(T, 84, '肉類', 'Meat Mains | Catering Hong Kong | Kitchen AO', 'Roast pork, wagyu short rib, lamb rack, roast chicken and suckling pig: meat mains for parties and banquets in Hong Kong.'),
(T, 85, '海鮮', 'Seafood Dishes | Catering Hong Kong | Kitchen AO', 'Seafood catering dishes for parties and receptions, freshly prepared and delivered across Hong Kong.'),
(T, 86, '飲品', 'Drinks & Beverages | Catering Hong Kong | Kitchen AO', 'Soft drinks, juices and tea to add to your Kitchen AO catering order, delivered with your party food.'),
(T, 107, '派對用品', 'Party Supplies | Tableware & Food Stands | Kitchen AO', 'Party supplies including tableware, food warmers and three-tier food stands to complete your catering setup.'),
(T, 111, '員工膳食餐盒', 'Staff Meal Boxes | Team Lunch Catering | Kitchen AO', 'Staff meal boxes for team lunches and training days, delivered to offices across Hong Kong.'),
(T, 112, '商務餐盒', 'Corporate Lunch Boxes | Meeting Catering | Kitchen AO', 'Corporate lunch boxes for meetings and seminars in Hong Kong, delivered on time to your office.'),
(T, 113, '高級餐盒', 'Executive Meal Boxes | Premium Lunch | Kitchen AO', 'Executive meal boxes for board meetings and VIP guests, with premium dishes delivered across Hong Kong.'),
(T, 114, '皇家小食盒', 'Royal Snack Boxes | Premium Canapés | Kitchen AO', 'Premium canapé boxes for VIP receptions and cocktail events, delivered across Hong Kong.'),
(T, 115, '九宮格 Canapés', '9-Grid Canapé Boxes | Gourmet Bites | Kitchen AO', 'Gourmet canapé boxes with nine bite-sized creations for receptions, meetings and corporate gifts.'),
(T, 116, '酒類', 'Wine & Alcohol | Party Drinks | Kitchen AO', 'Wine and alcoholic drinks to add to your party catering order in Hong Kong.'),
(T, 117, '三層氣氛食物架', 'Three-Tier Food Stands | Party Display | Kitchen AO', 'Three-tier food stands in themed colours and designs to display party food and desserts.'),
(T, 118, 'Chill一下野餐盒', 'Picnic Boxes Hong Kong | Outdoor Party Snacks | Kitchen AO', 'Ready-to-go picnic boxes of party snacks for outdoor picnics in Hong Kong parks, for 2 to 6 people.'),
(T, 120, '船河派對套餐', 'Boat Party Sets | Junk Trip Catering | Kitchen AO', 'Boat party sets for 15 to 40 guests, packed for junk trips and delivered to the pier in Hong Kong.'),
(T, 121, '肉食獸', 'Meat Lovers Party Sets | Kitchen AO Hong Kong', 'Meat-heavy party sets for carnivores, with roasts and grilled meats for 7 to 13 guests.'),
(T, 124, '2-6人分享選項', 'Party Food for 2 to 6 People | Kitchen AO', 'Catering sets and sharing dishes for 2 to 6 people, ideal for small gatherings at home or in the office.'),
(T, 125, '7-11人分享選項', 'Party Food for 7 to 11 People | Kitchen AO', 'Catering sets for 7 to 11 guests, ideal for birthday parties and small team celebrations in Hong Kong.'),
(T, 126, '12-16人分享選項', 'Party Food for 12 to 16 People | Kitchen AO', 'Catering sets for 12 to 16 guests for birthdays, office parties and family gatherings in Hong Kong.'),
(T, 127, '18-25人分享選項', 'Party Food for 18 to 25 People | Kitchen AO', 'Catering sets for 18 to 25 guests for company events and larger parties in Hong Kong.'),
(T, 128, '30人以上分享選項', 'Catering for 30+ Guests | Kitchen AO Hong Kong', 'Catering sets for 30 or more guests for corporate events, receptions and big celebrations in Hong Kong.'),
(T, 129, '100人以上分享選項', 'Catering for 100+ Guests | Large Events | Kitchen AO', 'Large-scale catering for 100 or more guests, for annual dinners, school events and big celebrations in Hong Kong.'),
(T, 131, '配菜', 'Side Dishes & Vegetables | Catering | Kitchen AO', 'Side dishes and seasonal vegetables to complete your party menu, delivered across Hong Kong.'),
(T, 132, '「素」味人生', 'Vegetarian Catering Sets for 6–26 | Kitchen AO', 'Vegetarian catering sets for 6 to 26 guests, from HK$1,388. Meat-free snacks, salads, pasta and mains, delivered across Hong Kong.'),
(T, 194, '中秋佳節團圓套餐 2026', 'Mid-Autumn Reunion Sets 2026 | Kitchen AO', 'Mid-Autumn Festival 2026 reunion catering sets for family gatherings and company celebrations in Hong Kong.'),
(T, 196, 'Halloween萬聖節狂嘩套餐', 'Halloween Party Sets 2026 | Kitchen AO Hong Kong', 'Halloween party catering sets with spooky-themed dishes for 5 to 40 guests, delivered across Hong Kong.'),
]

# ---------------- 產品（每項：ID、中文名、英文名、類型） ----------------
PRODUCTS = [
 (3909,'Gourmet 到會 (5-6人)','Gourmet Party Set for 5–6','gourmet:5 to 6'),
 (3913,'小巧兒童餐','Kids Party Meal (from 5 Children)','kids'),
 (5355,'二人小確幸套餐','Little Joys Dinner Set for Two','couple'),
 (5359,'AO 12-16pax 輕食宴會套餐','Refreshment Set for 12–16','refresh:12 to 16'),
 (6063,'酥炸雞軟骨配洋蔥圈','Crispy Chicken Cartilage with Onion Rings','dish'),
 (6064,'甜甜鮮茄菠蘿焗芝士腸','Baked Cheese Sausages with Tomato & Pineapple','dish'),
 (6068,'避風塘炸海鮮豆腐','Typhoon Shelter Fried Seafood Tofu','dish'),
 (6070,'日式雞皮餃子配洋蔥圈','Japanese Chicken Skin Gyoza with Onion Rings','dish'),
 (6071,'香烤沙嗲串燒 (豬雞)','Grilled Satay Skewers (Pork & Chicken)','dish'),
 (6072,'芝士肉鬆海鮮牛角酥','Cheese, Pork Floss & Seafood Croissants','dish'),
 (6074,'蜜蜜燒雞翼配脆薯角','Honey Roast Chicken Wings with Potato Wedges','dish'),
 (6076,'黑松露墨魚滑炸雲吞','Black Truffle Cuttlefish Fried Wontons','dish'),
 (6077,'迷你芝士手打豬肉牛肉漢堡','Mini Cheese Pork & Beef Burgers','dish'),
 (6078,'泰式白雲鳳爪','Thai-Style Chilled Chicken Feet','dish'),
 (6082,'照燒鰻魚日本蛋沙律牛油酥盒','Teriyaki Eel & Egg Salad Vol-au-vents','dish'),
 (6086,'千島汁大蝦蜜桃沙律','Prawn & Peach Salad with Thousand Island','dish'),
 (6088,'慢煮水嫰雞胸沙律','Sous-Vide Chicken Breast Salad','dish'),
 (6090,'照燒魷魚香橙紅酒醋沙律','Teriyaki Squid Salad with Orange Vinaigrette','dish'),
 (6097,'松葉蟹三文魚籽芒果沙律','Snow Crab, Salmon Roe & Mango Salad','dish'),
 (6099,'油香煙三文魚凱撒沙律','Smoked Salmon Caesar Salad','dish'),
 (6101,'芝士腐乳卡邦尼長通粉','Fermented Bean Curd Carbonara Penne','dish'),
 (6103,'芝士焗特調肉醬蝴蝶粉','Baked Bolognese Farfalle with Cheese','dish'),
 (6108,'XO醬蜆肉香蒜意大利麵','XO Sauce Clam & Garlic Spaghetti','dish'),
 (6111,'黑松露野菌蘆筍忌廉意粉','Black Truffle Mushroom & Asparagus Cream Pasta','dish'),
 (6115,'香煎帶子海蝦意大利飯','Pan-Seared Scallop & Prawn Risotto','dish'),
 (6130,'5人自選拼盤','Build-Your-Own Platter for 5','platter'),
 (6242,'美食派對 Gourmet Set (8-10pax)','Gourmet Party Set for 8–10','gourmet:8 to 10'),
 (6262,'Gourmet 到會 (12-16人)','Gourmet Party Set for 12–16','gourmet:12 to 16'),
 (6264,'美食派對 Gourmet Set (26-30pax)','Gourmet Party Set for 26–30','gourmet:26 to 30'),
 (6265,'Kitchen AO Gourmet Set','Gourmet Party Set','gourmet:5 to 30'),
 (6271,'二人豪華儀式感UP!套餐','Deluxe Celebration Set for Two','couple'),
 (6274,'焗燶邊香草蜜糖鹿兒島叉燒扒','Kagoshima Honey Herb Char Siu','dish'),
 (6275,'紅酒慢燴鮮蕃茄和牛牛肋條','Red Wine Braised Wagyu Short Ribs','dish'),
 (6276,'自家製黑松露牛油慢焗法國黃油雞','Black Truffle Butter Roast French Chicken','dish'),
 (6278,'泰好味汁燒西冷牛','Thai-Style Grilled Sirloin','dish'),
 (6279,'香煎紐西蘭穀飼羊架','Pan-Seared New Zealand Lamb Rack','dish'),
 (6280,'西班牙脆嫩乳香乳豬','Spanish Roast Suckling Pig','dish'),
 (6283,'蜜蜜糖德國鹹豬手','Honey-Glazed German Pork Knuckle','dish'),
 (6394,'派對大快樂兒童餐','Kids Party Feast (from 5 Children)','kids'),
 (6401,'Gourmet 到會套餐 (18-22人)','Gourmet Party Set for 18–22','gourmet:18 to 22'),
 (6407,'AO 18-22pax 輕食宴會套餐','Refreshment Set for 18–22','refresh:18 to 22'),
 (6408,'AO 26-30pax 輕食宴會套餐','Refreshment Set for 26–30','refresh:26 to 30'),
 (6409,'輕食宴會套餐 (35-40人)','Refreshment Set for 35–40','refresh:35 to 40'),
 (6483,'7寸紙碟','7-Inch Paper Plates','supply'),
 (6485,'9寸不鏽鋼食物夾','9-Inch Stainless Steel Food Tongs','supply'),
 (6488,'塑膠餐具套裝（刀叉勺）','Plastic Cutlery Sets (Knife, Fork & Spoon)','supply'),
 (6489,'為套餐保溫額外加上暖貼','Heat Packs to Keep Your Set Warm','supply'),
 (6641,'焗雙色芝士吞拿魚脆法包','Baked Two-Cheese Tuna Baguette','dish'),
 (7420,'九層塔香酥雞','Taiwanese Popcorn Chicken with Basil','dish'),
 (7421,'台式三色腸拼盤配蔥油餅','Taiwanese Sausage Platter with Scallion Pancake','dish'),
 (7422,'蠔油鮑汁野菌鮑魚酥','Abalone & Mushroom Pastry in Oyster Sauce','dish'),
 (7424,'墨西哥芝士玉米片配三色醬','Cheese Nachos with Three Dips','dish'),
 (7426,'忌廉芝士嫩雞墨西哥餡餅','Cream Cheese Chicken Quesadillas','dish'),
 (7494,'西班牙脆嫩乳香乳豬','Spanish Roast Suckling Pig','dish'),
 (9205,'法式龍蝦汁燴蛋餃','Egg Dumplings in French Lobster Bisque','dish'),
 (9206,'懷舊芝麻蝦滑多士','Classic Sesame Prawn Toast','dish'),
 (9208,'上海古早炸饅頭配煉奶','Fried Shanghai Mantou with Condensed Milk','dish'),
 (9209,'惹味蒜香焗茄子','Garlic Baked Aubergine (Vegetarian)','dish'),
 (9210,'椰香咖哩海鮮龍脷柳配蒜蓉包','Coconut Curry Seafood & Sole with Garlic Bread','dish'),
 (10377,'三層銀色波波食物架','Three-Tier Silver Polka Dot Food Stand','stand'),
 (10379,'三層金色波波食物架','Three-Tier Gold Polka Dot Food Stand','stand'),
 (10380,'三層花邊Tiffany green食物架','Three-Tier Tiffany Green Lace Food Stand','stand'),
 (10381,'三層黃白燙金邊食物架','Three-Tier Yellow & White Gold-Trim Food Stand','stand'),
 (10382,'三層黑色花邊食物架','Three-Tier Black Lace Food Stand','stand'),
 (10383,'三層金色食物架','Three-Tier Gold Food Stand','stand'),
 (10384,'三層粉紅色花邊食物架','Three-Tier Pink Lace Food Stand','stand'),
 (10385,'三層銀色食物架','Three-Tier Silver Food Stand','stand'),
 (10386,'三層藍白燙金邊食物架','Three-Tier Blue & White Gold-Trim Food Stand','stand'),
 (10387,'三層粉白燙金邊食物架','Three-Tier Pink & White Gold-Trim Food Stand','stand'),
 (10388,'三層藍球造型食物架','Three-Tier Basketball Food Stand','stand'),
 (10389,'三層美人魚造型食物架','Three-Tier Mermaid Food Stand','stand'),
 (10570,'T0210 幻彩四色靚靚啫喱杯 (10杯)','Colourful Jelly Cups (10 Cups)','dessert'),
 (10572,'T0310 朱古力迷你冬甩 (10個)','Chocolate Mini Doughnuts (10 pcs)','dessert'),
 (11389,'「有得解」新一代果汁系列','Yau Dak Gaai Juice Range','drink'),
 (13965,'員工膳食餐盒 Staff Meal','Staff Meal Box','box:staff'),
 (13981,'商務餐盒','Corporate Lunch Box','box:corp'),
 (13985,'EXECUTIVE - SET A','Executive Meal Box Set A','box:exec'),
 (13996,'EXECUTIVE - SET B','Executive Meal Box Set B','box:exec'),
 (13998,'EXECUTIVE - SET C','Executive Meal Box Set C','box:exec'),
 (13999,'EXECUTIVE - SET D','Executive Meal Box Set D','box:exec'),
 (14005,'皇家小食盒 LV.1','Royal Snack Box Level 1','royal'),
 (14006,'皇家小食盒 LV.2','Royal Snack Box Level 2','royal'),
 (14007,'皇家小食盒 LV.3','Royal Snack Box Level 3','royal'),
 (14045,'舌尖上的餐桌 九宮格Canapes Lv. 1','9-Grid Canapé Box Level 1','grid'),
 (14047,'舌尖上的餐桌 九宮格Canapes Lv. 2','9-Grid Canapé Box Level 2','grid'),
 (14048,'舌尖上的餐桌 九宮格Canapes Lv. 3','9-Grid Canapé Box Level 3','grid'),
 (14052,'noah Nonbe 戰神解酒丸','Noah Nonbe Hangover Tablets','other'),
 (14071,'維他 - 維他果然系','Vita Gor Yin Hai Tea','drink'),
 (14079,'維他檸檬茶','Vita Lemon Tea','drink'),
 (14083,'QOO - 兒童果汁之選','Qoo Kids Juice','drink'),
 (14099,'維他蘋果綠茶','Vita Apple Green Tea','drink'),
 (14102,'Coca Cola 系列','Coca-Cola Range','drink'),
 (14219,'Chill一下野餐盒 (小)','Chill Picnic Box (Small)','picnic'),
 (14228,'Chill一下野餐盒 (大)','Chill Picnic Box (Large, 4–6 People)','picnic'),
 (14238,'狂歡派對到會套餐15-20pax','Party Catering Set for 15–20','boat:15 to 20'),
 (14300,'肉食獸到會 上將海港盛盒','Meat Lovers Harbour Feast Box for 7–11','meat'),
 (14306,'肉食派對到會 (8-13人)','Meat Lovers Party Set for 8–13','meat'),
 (14307,'狂歡派對船河套餐 21-25pax','Boat Party Set for 21–25','boat:21 to 25'),
 (14308,'船河套餐','Boat Party Set','boat:15 to 40'),
 (14309,'狂歡派對船河套餐31-35pax','Boat Party Set for 31–35','boat:31 to 35'),
 (14314,'狂歡派對到會套餐36-40pax','Boat Party Set for 36–40','boat:36 to 40'),
 (14342,'100人到會套餐 百人斬大滿貫','Grand Catering Set for 100 Guests','big'),
 (14515,'D01 法式七彩馬卡龍 (10個)','French Macarons (10 pcs)','dessert'),
 (14517,'D02 椰果啫喱杯 (10個)','Coconut Jelly Cups (10 pcs)','dessert'),
 (14519,'D03 迷你夾心鬆餅 (10個)','Mini Filled Waffles (10 pcs)','dessert'),
 (14521,'D04 朱古力馬德蓮蛋糕 (10個)','Chocolate Madeleines (10 pcs)','dessert'),
 (14523,'D05 珍珠小泡芙 (10個)','Mini Cream Puffs (10 pcs)','dessert'),
 (14525,'D06 焦糖葡撻 (10個)','Caramel Portuguese Egg Tarts (10 pcs)','dessert'),
 (14527,'D07 流心芝士撻 (10個)','Molten Cheese Tarts (10 pcs)','dessert'),
 (14594,'忌廉白汁菠菜','Creamed Spinach','side'),
 (14595,'櫻花蝦和風炒野菜','Japanese Stir-Fried Vegetables with Sakura Shrimp','side'),
 (14596,'手壓香濃薯蓉','Creamy Mashed Potatoes','side'),
 (14597,'蒜香炒翠玉瓜','Garlic Sautéed Courgette','side'),
 (14598,'牛油蜂蜜粟米','Honey Butter Sweetcorn','side'),
 (14599,'錫紙焗番薯','Foil-Baked Sweet Potatoes','side'),
 (14600,'上湯枸杞葉','Goji Leaves in Superior Broth','side'),
 (14715,'「素」味人生素食到會套餐 6–8 人','Vegetarian Catering Set for 6–8','veg:6 to 8:HK$1,388'),
 (14750,'「素」味人生素食到會套餐 10–12 人','Vegetarian Catering Set for 10–12','veg:10 to 12:HK$1,988'),
 (14758,'「素」味人生素食到會套餐 16–19 人','Vegetarian Catering Set for 16–19','veg:16 to 19:HK$2,988'),
 (14759,'「素」味人生素食到會套餐 22–26 人','Vegetarian Catering Set for 22–26','veg:22 to 26:HK$3,788'),
 (14842,'粵式手工糯米八寶鴨','Cantonese Eight-Treasure Glutinous Rice Duck','dish'),
 (14843,'檸檬葉炭烤爆汁豬頸肉','Charcoal-Grilled Pork Jowl with Lime Leaf','dish'),
 (14849,'泰國蝦頭油珍珠帶子蟹籽炒飯','Thai Prawn Oil Fried Rice with Scallops & Crab Roe','dish'),
 (14852,'韓式風味豚腩肉香菇炒烏冬','Korean Pork Belly & Mushroom Fried Udon','dish'),
 (14853,'黑椒牛柳絲韭菜花炒意粉','Black Pepper Beef & Chive Flower Spaghetti','dish'),
 (15908,'Kitchen AO Gourmet Set','Gourmet Party Set','gourmet:5 to 30'),
 (15909,'Kitchen AO Gourmet Set','Gourmet Party Set','gourmet:5 to 30'),
 (15910,'Kitchen AO Gourmet Set','Gourmet Party Set','gourmet:5 to 30'),
 (19253,'維他樽裝無糖冷泡茶','Vita Unsweetened Cold Brew Tea','drink'),
 (19578,'西京燒威士忌白味噌燒鹿兒島叉燒扒 (4磅)','Whisky Miso Kagoshima Char Siu (4 lb)','dish'),
 (19579,'清酒煮蟹皇灸燒左口魚醬油煲仔飯 (4磅)','Sake Crab Roe & Flounder Claypot Rice (4 lb)','dish'),
 (20215,'C01 一口和牛野菌串','Wagyu & Wild Mushroom Skewer','canape'),
 (20216,'C02 刁草煙三文魚露筍卷','Dill Smoked Salmon & Asparagus Roll','canape'),
 (20217,'C03 意大利燴菜雞胸蕃茄麵包卷','Ratatouille Chicken & Tomato Bread Roll','canape'),
 (20218,'C04 慢煮雞胸意大利燴菜粒三文治','Sous-Vide Chicken & Ratatouille Sandwich','canape'),
 (20220,'C05 檸檬刁草海蝦俄羅斯鬆餅','Lemon Dill Prawn Blini','canape'),
 (20221,'C06 法式鵝肝慕斯開心果曲奇青檸啫喱','Foie Gras Mousse with Pistachio Cookie & Lime Jelly','canape'),
 (20222,'C07 炙燒帶子芋頭紫椰菜串','Seared Scallop, Taro & Red Cabbage Skewer','canape'),
 (20223,'C08 烤鴨絲青瓜大蒜卷','Roast Duck, Cucumber & Garlic Roll','canape'),
 (20224,'C09 無花果鴨胸crostini','Fig & Duck Breast Crostini','canape'),
 (20225,'C10 煙三文魚卷牛油果醬法包多士','Smoked Salmon & Avocado Baguette Toast','canape'),
 (20231,'C11 煙鴨胸粟子蓉雜啤梨撻','Smoked Duck, Chestnut & Pear Tart','canape'),
 (20232,'C12 照燒慢煮雞卷配牛油果蓉','Teriyaki Chicken Roll with Avocado','canape'),
 (20928,'Gourmet 到會 (5-6人)','Gourmet Party Set for 5–6','gourmet:5 to 6'),
 (20929,'美食派對 Gourmet Set (8-10pax)','Gourmet Party Set for 8–10','gourmet:8 to 10'),
 (20930,'Gourmet 到會 (12-16人)','Gourmet Party Set for 12–16','gourmet:12 to 16'),
 (20931,'Gourmet 到會套餐 (18-22人)','Gourmet Party Set for 18–22','gourmet:18 to 22'),
 (20932,'美食派對 Gourmet Set (26-30pax)','Gourmet Party Set for 26–30','gourmet:26 to 30'),
 (20933,'Kitchen AO Gourmet Set','Gourmet Party Set','gourmet:5 to 30'),
 (21619,'Gourmet 到會 (5-6人)','Gourmet Party Set for 5–6','gourmet:5 to 6'),
 (21620,'美食派對 Gourmet Set (8-10pax)','Gourmet Party Set for 8–10','gourmet:8 to 10'),
 (21621,'Gourmet 到會 (12-16人)','Gourmet Party Set for 12–16','gourmet:12 to 16'),
 (21622,'Gourmet 到會套餐 (18-22人)','Gourmet Party Set for 18–22','gourmet:18 to 22'),
 (21623,'美食派對 Gourmet Set (26-30pax)','Gourmet Party Set for 26–30','gourmet:26 to 30'),
 (21624,'Kitchen AO Gourmet Set','Gourmet Party Set','gourmet:5 to 30'),
]


def product_meta(en, kind):
    k = kind.split(':')
    t = f'{en} | Kitchen AO'
    if k[0] == 'dish': d = dish(en)
    elif k[0] == 'side': d = f'{en}, a side dish by Kitchen AO to complete your party menu, delivered across Hong Kong.'
    elif k[0] == 'gourmet': d = gourmet(k[1])
    elif k[0] == 'refresh': d = refresh(k[1])
    elif k[0] == 'veg': d = veg(k[1], k[2])
    elif k[0] == 'boat': d = boat(k[1])
    elif k[0] == 'drink': d = drink(en)
    elif k[0] in ('supply', 'stand'): d = supply(en)
    elif k[0] == 'dessert': d = dessert(en)
    elif k[0] == 'canape': d = canape(en)
    elif k[0] == 'kids': d = f'{en}: child-friendly party food for birthdays and school events, from 5 children. Delivered across Hong Kong by Kitchen AO.'
    elif k[0] == 'couple': d = f'{en} from Kitchen AO, a dinner set for two for anniversaries and special occasions, delivered to your home in Hong Kong.'
    elif k[0] == 'platter': d = f'{en}: choose your favourite finger food for a party of five. Kitchen AO party catering delivered across Hong Kong.'
    elif k[0] == 'box':
        d = {'staff': 'Staff meal boxes for team lunches and training days, with balanced meals delivered to offices across Hong Kong.',
             'corp': 'Corporate lunch boxes for meetings and seminars, delivered on time to offices across Hong Kong by Kitchen AO.',
             'exec': f'{en}: a premium lunch box for board meetings and VIP guests, delivered to offices across Hong Kong.'}[k[1]]
    elif k[0] == 'royal': d = f'{en}: premium canapés for VIP receptions and cocktail events, delivered across Hong Kong by Kitchen AO.'
    elif k[0] == 'grid': d = f'{en}: nine gourmet canapés in one box for receptions, meetings and corporate gifts. Delivered across Hong Kong.'
    elif k[0] == 'picnic': d = f'{en}: ready-to-go party snacks for picnics in Hong Kong parks. Order online with delivery to the park entrance.'
    elif k[0] == 'meat': d = f'{en}: roasts and grilled meats for meat-loving parties, delivered across Hong Kong by Kitchen AO.'
    elif k[0] == 'big': d = 'Large-scale party catering for 100 guests, with mains, snacks, salads and desserts for annual dinners and big events in Hong Kong.'
    else: d = f'{en}, available to add to your Kitchen AO catering order with delivery across Hong Kong.'
    return t, d


def fit(t, d):
    if len(t) > 60 and t.endswith(' | Kitchen AO'): t = t[:-len(' | Kitchen AO')]
    if len(t) > 60 and t.endswith(' | Kitchen AO Catering'): t = t[:-len(' | Kitchen AO Catering')]
    return t, d


def all_rows():
    rows = [r[:3] + fit(r[3], r[4]) for r in DATA]
    for pid, zh, en, kind in PRODUCTS:
        t, d = fit(*product_meta(en, kind))
        rows.append((PR, pid, zh, t, d))
    return rows


# ---------------- 2026-10-28 v2：按英文關鍵字（GSC、Semrush、Keyword Planner）調整 ----------------
# (kind, id): (title, description, 主要英文關鍵字（月搜／GSC 曝光））
KW_OVERRIDE = {
 ('page', 7014): ('Catering Hong Kong | Party & Corporate Catering | Kitchen AO',
  'Kitchen AO catering service in Hong Kong: party food delivery, corporate catering and boat party sets. Browse menus, get a quote and order online.',
  'catering hong kong 1,300；catering service hong kong 1,300（GSC 256）；catering hk 1,300；catering 2,900'),
 ('page', 18621): ('Catering Company Hong Kong | Best Picks 2026 | Kitchen AO',
  'Looking for a catering company in Hong Kong? Compare Kitchen AO party, corporate and boat party catering, with flexible menus and delivery across Hong Kong.',
  'catering company hong kong 90（GSC 53）；catering companies 70；catering company hk 90'),
 ('page', 18404): ('Corporate Catering Hong Kong | Office & Annual Dinner',
  'Corporate and office catering in Hong Kong for annual dinners, office lunches, meetings and openings. Menus tailored to headcount and budget. Request a quote.',
  'corporate catering hong kong 90（GSC 48）；corporate catering（GSC 195）；corporate catering service（GSC 125）；office catering hong kong（GSC 101）'),
 ('page', 6341): ('Event Catering Hong Kong | Business Events & Canapés',
  'Event catering in Hong Kong for business meetings, product launches, openings and receptions. Finger food, canapés and buffets arranged for your event.',
  'event catering 70（GSC 96）；catering for events 30；corporate catering events 90'),
 ('page', 6053): ('Party Food Delivery HK | Birthday Party Catering',
  'Party food delivery in Hong Kong for birthdays and celebrations: finger food, hot dishes, desserts and kids menus, delivered to your home or venue.',
  'party food delivery hk（GSC 196）；party food delivery（GSC 154）；party food 1,000；party food hk 70'),
 ('page', 7032): ('Finger Food Catering Hong Kong | Weddings & Parties',
  'Finger food catering for weddings, cocktail receptions and parties in Hong Kong. Bite-sized dishes and canapés delivered ready to serve.',
  'finger food catering（GSC 113，排第 27）；canapes 1,900'),
 ('page', 7024): ('Boat Party Catering Hong Kong | Junk Boat Food | Kitchen AO',
  'Boat party and junk boat catering in Hong Kong: party sets for 15 to 40 guests, packed for the boat and delivered to the pier.',
  'junk party 110；boat party catering'),
 ('page', 10737): ('Catering Quotation Hong Kong | Free Quote | Kitchen AO',
  'Request a free catering quotation: tell us your event date, headcount and budget, and Kitchen AO will send a tailored menu for your party or corporate event.',
  'catering quotation 30；catering packages 30'),
 ('page', 10477): ('Corporate Lunch Boxes Hong Kong | Meal Box Catering',
  'Corporate lunch boxes and meal box catering for meetings, seminars and office lunches in Hong Kong, delivered on time to your workplace.',
  'corporate lunch boxes 30；lunch box catering 30；meal box 90；office lunch delivery 70'),
 ('page', 10443): ('Staff Meal Boxes Hong Kong | Crew Meal Catering | Kitchen AO',
  'Staff meal and crew meal boxes for team lunches, film crews, training days and shift workers in Hong Kong. Balanced meals delivered to your site.',
  'staff meal（GSC 142，排第 10）；crew meal 140'),
 ('page', 10436): ('Executive Meal Boxes | Premium Lunch Catering | Kitchen AO',
  'Premium catering in executive meal boxes for board meetings, VIP guests and corporate lunches in Hong Kong, delivered to your office.',
  'premium catering 40'),
 ('page', 10740): ('Canapé Catering Hong Kong | Royal Snack Boxes | Kitchen AO',
  'Canapé catering in royal snack boxes for VIP receptions, cocktail events and corporate gatherings in Hong Kong.',
  'canapes 1,900；canapes catering hong kong 40'),
 ('page', 10940): ('Canapé Box | 9-Grid Gourmet Canapés | Kitchen AO',
  'A box of nine gourmet canapés for receptions, meetings and corporate gifts. Elegant canapé catering from Kitchen AO, delivered across Hong Kong.',
  'canapes 1,900'),
 ('page', 15017): ('Kwun Tong Catering 2026 | Corporate Catering | Kitchen AO',
  'Kwun Tong catering for Kowloon East offices and parties: party sets, lunch boxes and canapés. Free delivery on orders over HK$1,450.',
  'kwun tong catering（GSC 154，排第 25）'),
 ('special', 'shop'): ('Catering Menu & Party Food Delivery | Kitchen AO Shop',
  'Browse the Kitchen AO catering menu: party sets, à la carte dishes, desserts, drinks and party supplies, with party food delivery across Hong Kong.',
  'catering menu 70；party food delivery（GSC 154）'),
 ('post', 16468): ('Christmas Catering Hong Kong | Xmas Party Food | Kitchen AO',
  'Christmas catering in Hong Kong: festive party sets and Xmas party food for family gatherings and office Christmas parties, delivered to your door.',
  'christmas catering 90；xmas catering 90；christmas catering hong kong 70；christmas party hong kong 90'),
 ('post', 14183): ('Kids Party Food & Children\'s Party Catering 2026',
  'How to choose children\'s party catering in Hong Kong: kids party food ideas, portions, allergies and party set suggestions.',
  'kids party food 110；childrens party catering 90（GSC 37）；childrens party food 40'),
 ('post', 21808): ('Picnic Spots Hong Kong 2026 | 33 Best Parks | Kitchen AO',
  '33 picnic spots in Hong Kong with large lawns, sea views and pet-friendly areas, plus parking tips and picnic box ideas.',
  'picnic 2,400'),
 ('post', 14835): ('Junk Boat Party Food Checklist 2026 | Kitchen AO',
  'Everything you need for a Hong Kong junk boat party: food checklist, quantities, packing tips and free-delivery boat party catering sets.',
  'junk party 110；boat party'),
 ('term', 21): ('Party Catering Packages Hong Kong | Kitchen AO',
  'Party catering packages for birthdays, office parties and family gatherings in Hong Kong, for 2 to 100+ guests. Order food packages online with delivery.',
  'party catering 70；food packages 140；catering packages 30；party catering hk 40'),
 ('term', 26): ('Food Platters Hong Kong | Finger Food Platters | Kitchen AO',
  'Food platters and finger food platters for parties and receptions in Hong Kong. Build your own platter, delivered ready to serve.',
  'platter 720（GSC 排第 12）；food platter 30（GSC 排第 6）；platter service 110'),
 ('term', 40): ('Dessert Catering Hong Kong | Sweet Treats | Kitchen AO',
  'Dessert catering with macarons, mini tarts, jelly cups and more for parties and office celebrations, delivered across Hong Kong.',
  'dessert catering 30'),
 ('term', 66): ('Gourmet Party Food Packages by Headcount | Kitchen AO',
  'Gourmet party food packages for 5 to 30 guests with hot mains, pasta, salads and snacks. Choose by headcount and order online.',
  'food packages 140'),
 ('term', 67): ('Kids Party Food | Children\'s Party Catering HK | Kitchen AO',
  'Kids party food and children\'s party catering sets for birthdays and school events in Hong Kong, from 5 children.',
  'kids party food 110；childrens party catering 90'),
 ('term', 112): ('Corporate Lunch Box & Meal Box Catering | Kitchen AO',
  'Corporate lunch boxes and meal boxes for meetings and seminars in Hong Kong, delivered on time to your office.',
  'catering box 30（GSC 排第 7）；meal box 90；mealbox 40'),
 ('term', 111): ('Staff Meal & Crew Meal Boxes | Team Lunch | Kitchen AO',
  'Staff meal and crew meal boxes for team lunches, film crews and training days, delivered across Hong Kong.',
  'staff meal（GSC 142）；crew meal 140'),
 ('term', 114): ('Canapé Catering Hong Kong | Royal Snack Boxes | Kitchen AO',
  'Premium canapé boxes for VIP receptions and cocktail events, delivered across Hong Kong.',
  'canapes 1,900；canapes catering hong kong 40'),
 ('term', 115): ('Canapé Boxes | 9-Grid Gourmet Canapés | Kitchen AO',
  'Gourmet canapé boxes with nine bite-sized creations for receptions, meetings and corporate gifts.',
  'canapes 1,900'),
 ('term', 118): ('Picnic Boxes Hong Kong | Picnic Food Delivery | Kitchen AO',
  'Ready-to-go picnic boxes of party snacks for picnics in Hong Kong parks, for 2 to 6 people, delivered to the park entrance.',
  'picnic 2,400'),
 ('term', 120): ('Boat Party Sets | Junk Boat Catering | Kitchen AO',
  'Boat party sets for 15 to 40 guests, packed for junk boat trips and delivered to the pier in Hong Kong.',
  'junk party 110'),
 ('term', 132): ('Vegetarian Catering Hong Kong | Sets for 6–26 | Kitchen AO',
  'Vegetarian catering sets for 6 to 26 guests, from HK$1,388. Meat-free snacks, salads, pasta and mains, delivered across Hong Kong.',
  'vegetarian catering（待 KP 查詢）'),
 ('term', 129): ('Large Event Catering for 100+ Guests | Kitchen AO',
  'Large event catering for 100 or more guests, for annual dinners, school events and big celebrations in Hong Kong.',
  'catering for events 30'),
}
for (k, i), (t, d, kw) in KW_OVERRIDE.items():
    if not (len(t) <= 60 and len(d) <= 160): print('TOO LONG', k, i, len(t), len(d))
_old_all_rows = all_rows


def all_rows():
    out = []
    for r in _old_all_rows():
        o = KW_OVERRIDE.get((r[0], r[1]))
        out.append((r[0], r[1], r[2], o[0], o[1]) if o else r)
    return out


def kw_of(kind, i):
    o = KW_OVERRIDE.get((kind, i))
    return o[2] if o else ''


# ---------------- 2026-10-28 v3：Meta Title 跟網站 /en/ 頁面現有英文名稱 ----------------
from en_site_names import EN as SITE_EN, FALLBACK as SITE_FB, ISSUES as SITE_ISSUES
KIND_FIX = {6265: 'gourmet:35 to 40', 15908: 'gourmet:48 to 54', 15909: 'gourmet:63 to 68', 15910: 'gourmet:78 to 85',
            14238: 'boat:15 to 20', 14308: 'boat:26 to 30', 14342: 'big',
            20928: 'mid:5 to 6', 20929: 'mid:8 to 10', 20930: 'mid:12 to 16', 20931: 'mid:18 to 22', 20932: 'mid:26 to 30', 20933: 'mid:35 to 40',
            21619: 'hw:5 to 6', 21620: 'hw:8 to 10', 21621: 'hw:12 to 16', 21622: 'hw:18 to 22', 21623: 'hw:26 to 30', 21624: 'hw:35 to 40'}
_pm = product_meta


def product_meta(en, kind):
    k = kind.split(':')
    if k[0] == 'mid':
        return fit(f'{en} | Kitchen AO', f'{en}: Mid-Autumn Festival reunion catering for {k[1]} guests, delivered across Hong Kong. Order online.')
    if k[0] == 'hw':
        return fit(f'{en} | Kitchen AO', f'{en}: Halloween party catering for {k[1]} guests with spooky-themed dishes, delivered across Hong Kong.')
    t, d = _pm(en, kind)
    if len(d) > 160: d = f'{en}, freshly made by Kitchen AO and delivered across Hong Kong.'
    if len(d) > 160: d = f'{en} by Kitchen AO.'
    return t, d


NAME_STATUS = {}
for _i, (_pid, _zh, _en, _kind) in enumerate(PRODUCTS):
    site = SITE_EN.get(_pid)
    if site:
        name, st = site, '沿用網站英文名'
    else:
        name = SITE_FB.get(_pid, _en)
        st = f'網站未有英文名，建議在 TranslatePress 補上：{name}'
    if _pid in SITE_ISSUES: st = '⚠ ' + SITE_ISSUES[_pid] + '；' + st
    PRODUCTS[_i] = (_pid, _zh, name, KIND_FIX.get(_pid, _kind))
    NAME_STATUS[('product', _pid)] = st

# 分類及有英文 H1 的頁面：Title 跟網站英文名
ALIGN = {
 ('term', 21): ('Party Catering Set | Party Food Packages HK | Kitchen AO', None),
 ('term', 24): ('Refreshment Sets | Meeting & Tea Catering | Kitchen AO', None),
 ('term', 25): ('Couple Set | Dinner for Two Delivery | Kitchen AO', None),
 ('term', 26): ('Finger Food Platters Hong Kong | Kitchen AO', 'Finger food platters for parties and receptions in Hong Kong. Build your own platter, delivered ready to serve.'),
 ('term', 40): ('Desserts | Dessert Catering Hong Kong | Kitchen AO', None),
 ('term', 45): ('A La Carte | Build Your Own Catering Menu | Kitchen AO', None),
 ('term', 64): ('Cutlery & Heat Pack Add-ons | Party Catering | Kitchen AO', 'Add cutlery, plates, food tongs and heat packs to your catering order to keep party food warm and ready to serve.'),
 ('term', 66): ('Gourmet Party Sets | Food Packages by Headcount | Kitchen AO', None),
 ('term', 67): ('Happy Kids Set | Kids Party Food Catering | Kitchen AO', None),
 ('term', 80): ('Cold Appetizers | Party Catering Hong Kong | Kitchen AO', 'Cold appetizers and chilled starters for parties, delivered with your Kitchen AO catering order across Hong Kong.'),
 ('term', 81): ('Savory Snacks | Fried Bites & Skewers | Kitchen AO', None),
 ('term', 83): ('Pasta | Pasta & Risotto Catering Hong Kong | Kitchen AO', None),
 ('term', 84): ('Meat | Meat Mains Catering Hong Kong | Kitchen AO', None),
 ('term', 112): ('Commercial Lunch Box | Meal Box Catering | Kitchen AO', 'Commercial lunch boxes and meal boxes for meetings and seminars in Hong Kong, delivered on time to your office.'),
 ('term', 113): ('Executive Premium Meal Box | Kitchen AO Hong Kong', 'Executive premium meal boxes for board meetings and VIP guests, delivered across Hong Kong.'),
 ('term', 114): ('Royal Snackers Box | Canapé Catering | Kitchen AO', 'Royal Snackers Box: premium canapés for VIP receptions and cocktail events, delivered across Hong Kong.'),
 ('term', 115): ('Nine Delights Gourmet Canapés Box | Kitchen AO', 'Nine Delights Gourmet Canapés Box: nine bite-sized canapés for receptions, meetings and corporate gifts.'),
 ('term', 116): ('Alcoholic Drinks | Party Catering | Kitchen AO', 'Alcoholic drinks to add to your party catering order in Hong Kong.'),
 ('term', 117): ('Three-Tier Food Stand | Party Display | Kitchen AO', None),
 ('term', 118): ('Chill Picnic Box | Picnic Food Delivery HK | Kitchen AO', None),
 ('term', 120): ('Boat Party Set | Junk Boat Catering | Kitchen AO', None),
 ('term', 121): ("Meat Monster Feast Box | Admiral's Harbor Choice", 'Meat Monster feast boxes with roasts and grilled meats for meat-loving parties of 7 to 13 guests, delivered across Hong Kong.'),
 ('term', 124): ('Party Sets for 2–6 People | Kitchen AO Catering', None),
 ('term', 125): ('Party Sets for 7–11 People | Kitchen AO Catering', None),
 ('term', 126): ('Party Sets for 12–16 People | Kitchen AO Catering', None),
 ('term', 127): ('Party Sets for 18–25 People | Kitchen AO Catering', None),
 ('term', 128): ('Party Sets for 30+ People | Kitchen AO Catering', None),
 ('term', 129): ('Party Sets for 100+ People | Large Event Catering', None),
 ('term', 131): ('Side Dishes | Party Catering Hong Kong | Kitchen AO', None),
 ('term', 132): ('Vegetarian Delight | Vegetarian Catering HK | Kitchen AO', None),
 ('term', 196): ('Spooktacular Halloween Party Set | Kitchen AO', None),
 ('page', 5924): ('How to Order | Catering Online Ordering | Kitchen AO', None),
 ('page', 6029): ('Breaking News & Offers | Kitchen AO Catering', None),
 ('page', 10477): ('Commercial Lunch Box Hong Kong | Meal Box Catering', 'Commercial lunch boxes and meal box catering for meetings, seminars and office lunches in Hong Kong, delivered on time to your workplace.'),
 ('page', 10737): ('Catering Quote Enquiry | Free Quotation | Kitchen AO', None),
 ('page', 11197): ('Partners & Service Records | Kitchen AO Catering', None),
 ('page', 11204): ('Featured Gallery | Catering Photos | Kitchen AO', None),
 ('page', 14653): ('Wedding Event Photos | Wedding Catering | Kitchen AO', None),
 ('page', 14689): ('Opening Event Photos | Grand Opening Catering | Kitchen AO', None),
 ('page', 18621): ('Hong Kong Catering Recommendations 2026 | Kitchen AO', 'Hong Kong catering recommendations for corporate events, parties and premium dining. Compare Kitchen AO sets as your catering company in Hong Kong.'),
}
_v2_all_rows = all_rows


def all_rows():
    out = []
    for r in _v2_all_rows():
        a = ALIGN.get((r[0], r[1]))
        if a:
            r = (r[0], r[1], r[2], a[0], a[1] or r[4])
        out.append(r)
    return out


def name_status(kind, i):
    return NAME_STATUS.get((kind, i), '')
