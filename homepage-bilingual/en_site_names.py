# -*- coding: utf-8 -*-
"""/en/ 頁面現有英文產品名及分類名（2026-10-28 用 Chrome 讀取 H1），Meta Title 以此為準"""
import re
RAW = {
3909:"AO 5-6pax Gourmet Set",3913:"Petite Kids' Delight Meal (5+ Persons)",5355:"Cozy Little Happiness Couple Set",5359:"AO 12-16pax Refreshment set",
6063:"A0900 FRIED SQUID TENEACLES AND ONION RINGS",6064:"A24(S) Grilled Cheese Sausages in Tomato Sauce（2lbs）",6068:"A1500 TYPHOON SHELTER STYLE CRISPY SEAFOOD TOFU WITH SWEET SEAFOOD SAUCE",
6070:"A1600 JAPANESE CHICKEN SKIN DUMPLINGS WITH CRISPY ONION RINGS",6071:"A0200 GRILLED SATAY SKEWERS (PORK & CHICKEN)",6072:"A1800 芝士海鮮牛角酥",
6074:"A0500 HONEY GLAZED CHICKEN WINGS WITH CRISPY POTATO WEDGES",6076:"A0600 DEEP-FRIED BLACK TRUFFLE CUTTLEFISH PASTE WONTONS",6077:"A0700 迷你芝士手打漢堡",6078:".",
6082:"A0400 TERIYAKI EEL & JAPANESE EGG SALAD BUTTER PASTRY CUPS",6086:"S0700 PRAWN & PEACH SALAD WITH THOUSAND ISLAND DRESSING",
6088:"S0500 Slow-cooked Chicken Breast Salad with Green Apple, Celery & Walnuts",6090:"S0400 TERIYAKI SQUID SALAD WITH ORANGE RED WINE VINAIGRETTE",
6097:"S0200 Snow Crab, Salmon Roe & Mango Salad",6099:"S0300 Smoked Salmon Signature Caesar Salad",
6101:"P07(L) Creamy Carbonara Penne with Cheese & Fermented Beancurd (4 lb)",6103:"P10(L) Baked Cheesy Bolognese Farfalle (4 lb)",
6108:"P04(L) XO Sauce Clam Meat Garlic Spaghetti (4 lb)",6111:"P03(L) Black Truffle Wild Mushroom Asparagus Cream Pasta (4 lb)",
6115:"P01(L) Pan-seared Scallop & Prawn Risotto with Fresh Herb Sauce (4 lb)",6130:"5-Person Customizable Platter",
6242:"AO 8-10pax Gourmet Set",6262:"AO 12-16 Gourmet Set",6264:"AO 26-30pax Gourmet Set",6265:"AO 35-40pax Gourmet Set",6271:"Romantic Luxury Ceremony Set for Two",
6274:"M01(L) 「香港燒」烤燶邊香草蜜糖鹿兒島叉燒扒 (4磅)",6275:"M02(L) Red Wine Braised Wagyu Beef Short Ribs with Fresh Tomato (4 lb)",
6276:"M03(L) SLOW-ROASTED FRENCH YELLOW SPRING CHICKEN WITH HOUSE-MADE BLACK TRUFFLE BUTTER",6278:"M09(L) GRILLED SIRLOIN WITH THAI-STYLE SIGNATURE SAUCE (4 LB)",
6279:"M08(16) PAN-SEARED NEW ZEALAND GRAIN-FED LAMB RACK (12-16 RIBS）",6280:"M0600 SPANISH-STYLE CRISPY SUCKLING PIG",6283:"M05(M) Honey Glazed German Pork Knuckle (Whole)",
6394:"Party Big Happy Kids' Party Set (5+ Persons)",6401:"AO 18-22pax Gourmet Set",6407:"AO 18-22pax Refreshment set",6408:"AO 26-30pax Refreshment set",
6409:"AO 35-40pax 輕食宴會套餐 Refreshment set",6483:"7-inch Paper Plates",6485:"9-inch Stainless Steel Food Tongs",6488:"Cutlery Set (Knife, Fork, Spoon)",
6489:"Heat Retaining Warm Patches",6641:"A0100 BAKED TUNA & DUAL CHEESE CRISPY BAGUETTE",7420:"A2800 CRISPY TAIWANESE BASIL POPCORN CHICKEN",
7421:"A2900 TAIWANESE TRIO SAUSAGE PLATTER WITH TRADITIONAL SCALLION PANCAKES",7422:"A3100 BRAISED ABALONE & WILD MUSHROOM PUFF PASTRY WITH OYSTER & ABALONE SAUCE",
7424:"A3200 NACHOS WITH CHEESE & TRIO OF DIPS",7426:"A3000 CREAM CHEESE CHICKEN QUESADILLAS",7494:"M0600 SPANISH-STYLE CRISPY SUCKLING PIG",
9205:"A3300 EGG DUMPLINGS IN FRENCH LOBSTER BISQUE SAUCE",9206:"A3400 SESAME SHRIMP TOAST WITH THAI SWEET CHILI SAUCE",
9208:"A3800 SHANGHAI-STYLE DEEP-FRIED MANTOU WITH CONDENSED MILK",9209:"A3900 BAKED EGGPLANT WITH GARLIC",
9210:"M11(L) Coconut Curry Seafood Sole Fillet with Garlic Bread (4 lb)",10377:"Three-Tier Silver Bubble Food Stand",10379:"Three-Tier Gold Bubble Food Stand",
10380:"Three-Tier Tiffany Green Lace Food Stand",10381:"Three-Tier Yellow & White Gilded Edge Food Stand",10382:"Three-Tier Black Lace Food Stand",
10383:"Three-Tier Gold Food Stand",10384:"Three-Tier Pink Lace Food Stand",10385:"三層銀色食物架",10386:"Three-Tier Blue & White Gilded Edge Food Stand",
10387:"Three-Tier Pink & White Gilded Edge Food Stand",10388:"三層藍球造型食物架",10389:"Three-Tier Mermaid-Shaped Food Stand",
10570:"-T0210 Colorful Jelly Cup (10 Cups)",10572:"-T0310 Chocolate Mini Dount (10 pcs)",11389:"「有得解」新一代果汁系列",13965:"Staff Meal",13981:"Commercial Lunch Box",
13985:"EXECUTIVE – SET A",13996:"EXECUTIVE – SET B",13998:"EXECUTIVE – SET C",13999:"EXECUTIVE – SET D",
14005:"Royal Snackers Box LV.1",14006:"Royal Snackers Box LV.2",14007:"Royal Snackers Box LV.3",
14045:"舌尖上的餐桌 九宮格Canapes Lv. 1",14047:"舌尖上的餐桌 九宮格Canapes Lv. 2",14048:"舌尖上的餐桌 九宮格Canapes Lv. 3",14052:"noah Nonbe",
14071:"Vita Gor Yin Hai",14079:"Vita Lemon Tea",14083:"QOO",14099:"Vita Apple Green Tea",14102:"Coca Cola collection",
14219:"Chill Picnic Box (Small size)",14228:"Chill Picnic Box (For 4-6 Persons)",14238:"AO 15-20pax Boat Party Set",14300:"肉食獸!!!上將陸港之選盛盒",
14306:"肉食獸!!!上將陸港之選巨量盛盒",14307:"AO 21-25pax Boat Party Set",14308:"AO 26-30pax Boat Party Set",14309:"AO 31-35pax Boat Party Set",
14314:"AO 36-40pax Boat Party Set",14342:"AO 100百人慶典派對到會套餐 Centenary Celebration Party Set",
14515:"D01 French Rainbow Macarons (10 pcs)",14517:"D02 Coconut Jelly Cups (10 pcs)",14519:"D03 Mini Filled Waffles (10 pcs)",
14521:"D04 Chocolate Madeleine Cakes (10 pcs)",14523:"D05 Pearl Profiteroles (10 pcs)",14525:"D06 Caramel Portuguese Tarts (10 pcs)",14527:"D07 Molten Cheese Tarts (10 pcs)",
14594:"A59 忌廉白汁菠菜 (1磅)",14595:"A60 櫻花蝦和風炒野菜 (1磅)",14596:"A61 手壓香濃薯蓉 (1磅)",14597:"A62 蒜香炒翠玉瓜 (1磅)",14598:"A63 牛油蜂蜜粟米 (1磅)",
14599:"A64 錫紙焗番薯 (1磅)",14600:"A65 上湯枸杞葉 (1磅)",14715:"AO 6-8pax Vegetarian Delight",14750:"AO 10-12pax Vegetarian Delight",
14758:"AO 16-19pax Vegetarian Delight",14759:"AO 22-26 Vegetarian Delight",
14842:"M12(L) Cantonese-style Eight Treasure Glutinous Rice Stuffed Duck (3 pcs)",14843:"M13(L) Charcoal-grilled Juicy Pork Neck with Kaffir Lime Leaves (4 lb)",
14849:"P15(L) Seafood Fried Rice with Thai Prawn Oil, Crispy Shallots, Scallops & Crab Roe (4 lb)",14852:"P18(L) Korean-style Pork Belly & Mushroom Stir-fried Udon (4 lb)",
14853:"P22(L) Black Pepper Beef Tenderloin Strips with Chive Flower Spaghetti (4 lb)",15908:"AO 48-54pax Gourmet Set",15909:"AO 63-68pax Gourmet Set",15910:"AO 78-85pax Gourmet Set",
19253:"維他樽裝無糖冷泡茶",19578:"MS02(L) Saikyo Miso & “Fujikinran” Whisky Glazed Kagoshima Char Siu (4 lb)",19579:"PS01(L)「冩樂」清酒煮蟹皇灸燒左口魚醬油煲仔飯 (4磅)",
20215:"C01(01) 一口和牛野菌串 (1串)",20216:"C02(01) 刁草煙三文魚露筍卷 (1件)",20217:"C03(01) 意大利燴菜雞胸蕃茄麵包卷 (1件)",20218:"C04(01) 慢煮雞胸意大利燴菜粒三文治 (1件)",
20220:"C05(01) 檸檬刁草海蝦俄羅斯鬆餅 (1件)",20221:"C06(01) 法式鵝肝慕斯開心果曲奇青檸啫喱 (1件)",20222:"C07(01) 炙燒帶子芋頭紫椰菜串 (1串)",20223:"C08(01) 烤鴨絲青瓜大蒜卷 (1件)",
20224:"C09 無花果鴨胸crostini (1件)",20225:"C10(01) 煙三文魚卷牛油果醬法包多士 (1件)",20231:"C11(01) 煙鴨胸粟子蓉雜啤梨撻 (1件)",20232:"C12(01) 照燒慢煮雞卷配牛油果蓉 (1件)",
20928:"AO 5-6pax 中秋佳節團圓套餐 2026",20929:"AO 8-10pax 中秋佳節團圓套餐 2026",20930:"AO 12-16pax 中秋佳節團圓套餐 2026",20931:"AO 18-22pax 中秋佳節團圓套餐 2026",
20932:"AO 26-30pax 中秋佳節團圓套餐 2026",20933:"AO 35-40pax 中秋佳節團圓套餐 2026",
21619:"AO 5-6 pax Spooktacular Halloween Party Set",21620:"AO 8-10 pax Spooktacular Halloween Party Set",21621:"AO 12-16 pax Spooktacular Halloween Party Set",
21622:"AO 18-22 pax Spooktacular Halloween Party Set",21623:"AO 26-30 pax Spooktacular Halloween Party Set",21624:"AO 35-40 pax Spooktacular Halloween Party Set",
}
# 網站英文名可能有問題，要人手確認
ISSUES = {
 6063: '網站英文名「Fried Squid Tentacles」錯誤：中文名及網址都是雞軟骨（chicken cartilage），Meta 已改用正確名稱，請同時修正網站英文產品名',
 10572: '英文名 Dount 拼錯，應為 Doughnut',
 6078: '英文名只有「.」，未有翻譯',
}
SMALL = {'and','with','in','of','on','the','a','for','to','or'}
def tc(s):
    if s.upper() != s: return s
    w = s.lower().split(' ')
    out = ' '.join(x if (i and x in SMALL and i < len(w) - 1) else (x[:1].upper() + x[1:]) for i, x in enumerate(w))
    out = re.sub(r'\((\w)', lambda m: '(' + m.group(1).upper(), out)
    return out.replace('Xo ', 'XO ').replace('Ao ', 'AO ')
def clean(raw):
    s = raw.strip().lstrip('-').strip()
    s = re.sub(r'^[A-Z]{1,2}\d{1,4}(\([A-Z0-9]+\))?\s+', '', s)
    s = re.sub(r'\s*[（(]\s*\d[\d.\s-]*(lbs?|LB|磅|pcs|件|串|RIBS)[^)）]*[)）]?\s*$', '', s, flags=re.I)
    s = s.replace('TENEACLES', 'TENTACLES').replace('Dount', 'Doughnut')
    s = tc(s.strip())
    if re.search(r'[一-鿿]', s) or len(s) < 3: return None
    return s
EN = {k: clean(v) for k, v in RAW.items()}

# 網站未有英文名的產品：建議英文名（同時建議在 TranslatePress 補上）
FALLBACK = {
 6409: 'AO 35-40pax Refreshment Set', 14342: 'AO 100pax Centenary Celebration Party Set',
 14300: "Meat Monster Admiral's Harbor Choice Feast Box", 14306: "Meat Monster Admiral's Harbor Choice Jumbo Feast Box",
 14045: 'Nine Delights Gourmet Canapés Box Lv. 1', 14047: 'Nine Delights Gourmet Canapés Box Lv. 2', 14048: 'Nine Delights Gourmet Canapés Box Lv. 3',
 20928: 'AO 5-6pax Mid-Autumn Reunion Set 2026', 20929: 'AO 8-10pax Mid-Autumn Reunion Set 2026', 20930: 'AO 12-16pax Mid-Autumn Reunion Set 2026',
 20931: 'AO 18-22pax Mid-Autumn Reunion Set 2026', 20932: 'AO 26-30pax Mid-Autumn Reunion Set 2026', 20933: 'AO 35-40pax Mid-Autumn Reunion Set 2026',
}
FIX = {14052: 'Noah Nonbe', 14102: 'Coca-Cola Collection', 13985: 'Executive – Set A', 6063: 'Crispy Fried Chicken Cartilage with Onion Rings'}
for k, v in FIX.items(): EN[k] = v
