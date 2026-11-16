# -*- coding: utf-8 -*-
"""Blog 2 聖誕派對食物 mock-up 生成器
用法：python3 build.py <輸出 html>"""
import html, sys, os, json, urllib.parse
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1]

def img(p, w=600, h=450):
    return f'https://images.unsplash.com/{p}?w={w}&h={h}&fit=crop&crop=entropy&q=80&auto=format'

def dishes(items):
    return '<p class="swipe">左右滑動查看更多 →</p><div class="xd-grid">' + ''.join(
        f'<figure class="xd"><div class="ph"><img src="{img(p)}" width="600" height="450" loading="lazy" alt="{html.escape(n)}">'
        f'</div><figcaption><b>{n}</b><span>{d}</span></figcaption></figure>'
        for n, d, p, u in items) + '</div>'

HOLLY = ('<svg viewBox="0 0 48 24" aria-hidden="true"><path d="M24 12c-6-8-14-8-20-4 4 1 6 4 6 7 4-3 9-4 14-3zM24 12c6-8 14-8 20-4-4 1-6 4-6 7-4-3-9-4-14-3z" fill="#2F5D3A"/>'
         '<circle cx="21" cy="13" r="3" fill="#B03426"/><circle cx="27" cy="13" r="3" fill="#B03426"/><circle cx="24" cy="9" r="3" fill="#C9372A"/></svg>')

IB = 'https://aoaodelivery.com/wp-content/uploads/2026/11/'
V5 = ['寶箱煙燻慢煮美國牛翼板肉', '燒南乳香慢煮原隻黃油雞', '芒果粟子蓉冬日酥盒', '聖誕馴鹿脆脆開心果朱古力撻', '雙重龍蝦三重芝士煲仔鍋飯', '玫瑰醬泡菜海蝦意大利飯',
      '紅寶神石榴大蝦柚肉沙律', '紅寶神石榴煙火雞胸蜜桃沙律', '皇帝蟹棒蟹肉芒果牛油果沙律', '聖誕樹芝士火腿拼盤', '西班牙辣肉腸熔岩芝士杯']
XS = '<span class="xs"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2v20M3.3 7l17.4 10M3.3 17L20.7 7M12 5l-2-2M12 5l2-2M12 19l-2 2M12 19l2 2" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"/></svg>XMAS SPECIAL</span>'
def xs(n): return XS if any(v in n for v in V5) else ''
def ao(title, groups, cta, pics=()):
    g = ''
    for t, s, its in groups:
        one = ' one' if len(its) == 1 else ''
        g += '<div class="a-sec">' + (f'<p class="a-st"><i></i>{t}<i></i></p>' if t else '') + f'<ul class="{one.strip()}">' + ''.join(
            (f'<li>{xs(n)}<a href="{u}">{n}</a><span>{d}</span></li>' if u else f'<li>{xs(n)}<a class="todo" href="#">{n}</a><span>{d}</span></li>')
            for n, d, u in its) + '</ul></div>'
    return (f'<div class="optA"><div class="a-in"><div class="a-top">{HOLLY}</div><p class="a-k">KITCHEN AO · CHRISTMAS MENU</p>'
            f'<h4>{title}</h4><p class="a-orn">— ✧ —</p><p class="xs-note">{XS} ＝ 2026 聖誕新菜及主打</p>' + (('<div class="a-pics n' + str(len(pics)) + '">' + ''.join(f'<figure><img src="{IB}{f}" alt="{c}" loading="lazy"><figcaption>{c}</figcaption></figure>' for f, c in pics) + '</div>') if pics else '') + f'{g}<a class="a-cta todo" href="#">{cta}</a></div></div>')

P = 'https://aoaodelivery.com/product/'
SNK = [('芝士焗釀啡蘑菇', '啡蘑菇釀入香草麵包糠及芝士焗香，一口一件。不含肉類的做法亦適合素食朋友，宜焗好後盡快上桌。', 'photo-1640456604089-cc18763be2b5', 'Nick Nice'),
       ('煙三文魚一口小食', '煙三文魚配忌廉芝士及蒔蘿，放在脆餅或多士上。屬冷盤小食，可預早擺盤，適合辦公室派對。', 'photo-1780134758247-f780bcb9dca5', 'waa towaw'),
       ('香烤牛肉丸配番茄汁', '肉丸沾滿微酸番茄汁，香濃多汁。醬汁有助保持濕潤，放久一點亦不易乾身。', 'photo-1768187067375-4cd5a79fec41', 'Kris Tian'),
       ('芝士流心多士粒', '外層金黃香脆，內裡芝士融化。最怕放涼變硬，宜最後才焗或用焗爐翻熱。', 'photo-1784217066743-4b7d5cde08fd', 'Rodrigo Rodrigues'),
       ('派對炸物拼盤', '洋蔥圈、炸雞塊及烤雞翼最受年輕人歡迎。炸物遇蒸氣會變腍，運送時宜用透氣容器。', 'photo-1766589152198-38630c391dfb', 'Diego Arenas de Rodrigo')]
SAL = [('紅石榴果仁沙律', '沙律菜拌入紅石榴粒、合桃及蘋果片，紅綠相映。醬汁宜另上，食用前才拌勻，菜葉保持爽脆。', 'photo-1662192513841-c890cc6ff3f9', 'kimia kazemi'),
       ('煙三文魚凱撒沙律', '凱撒醬配羅馬生菜、脆麵包粒及煙三文魚，百搭穩妥，亦是最多人接受的沙律款式。', 'photo-1745443710671-31f3f6fdc4b0', 'Meg von Haartman'),
       ('巴馬火腿蜜瓜冷盤', '火腿鹹香包裹香甜蜜瓜，經典意式開胃組合。無需翻熱，最適合先上桌招呼賓客。', 'photo-1746494557472-b00a5c871b93', 'Enmanuel Abreu')]
MAIN = [('經典香烤聖誕火雞', '釀入麵包粒、香草及洋蔥慢烤，配肉汁及蔓越莓醬。一隻 12 磅火雞約夠 10 至 12 人，在家烤製需時約 3 至 4 小時。', 'photo-1763689454945-4b0f3b151969', 'Prchi Palwe'),
        ('美式 BBQ 豬肋骨', '低溫煙燻後掃上 BBQ 醬，肉質軟嫩、輕易離骨。份量易分，適合人多的派對。', 'photo-1544025162-d76694265947', 'Alexandru-Bogdan Ghita'),
        ('香草烤原塊牛肉', '以香草、黑椒及海鹽塗抹後烘烤，切片粉嫩多汁，配燒汁或芥末。原塊上桌再切，最有派對氣氛。', 'photo-1529692236671-f1f6cf9683ba', 'José Ignacio Pompé'),
        ('香草檸檬烤三文魚', '以香草海鹽烤原塊三文魚，魚肉粉嫩多汁。口味清新，可照顧不吃紅肉的賓客。', 'photo-1728963228980-71c76178616a', 'Frolicsome Fairy')]
PAS = [('肉醬千層麵（Lasagna）', '肉醬、白汁及麵皮層層相疊，面層焗至金黃。保溫度高，即使放置一段時間仍然軟滑。', 'photo-1709429790175-b02bb1b19207', 'Emanuel Ekström'),
       ('西班牙海鮮飯（Paella）', '以海鮮湯煮黃金米飯，鋪滿大蝦及海鮮，色彩繽紛。原鑊上桌，視覺效果突出。', 'photo-1756066234813-b076c0adea9a', 'Rodrigo Rodrigues')]
CAKE = [('意大利聖誕蛋糕（Panettone）', '傳統發酵糕點，內有果乾，組織鬆軟如麵包。可常溫存放，適合預早購買。', 'photo-1762304887659-7d4127c1e2e6', 'Lee Milo'),
        ('聖誕忌廉蛋糕', '海綿蛋糕夾鮮果，外層輕盈忌廉，拍照效果佳。需冷藏，宜派對當日取貨。', 'photo-1766585449820-01a8fa6f1473', '光术 山影'),
        ('聖誕樹幹蛋糕（Bûche de Noël）', '源自法國，朱古力年輪紋路配糖霜雪花，象徵一整年的溫暖及好運。', 'photo-1484300681262-5cca666b0954', 'Jill Heyer'),
        ('立體聖誕樹蛋糕', '以抹茶或開心果忌廉唧成層層樹葉，點綴珍珠糖，切開前先拍照。（相片待揀）', 'photo-1766342043778-f9d550fe2329', 'Francesco Liotti')]
DES = [('彩繪薑餅人曲奇', '薑及肉桂香氣交織，畫上糖霜笑臉，亦是伴手禮之選。（相片待揀）', 'photo-1771274023071-9d37360a6638', 'Sotirios T. Kokkinos'),
       ('聖誕朱古力禮盒', '松露朱古力或榛子夾心朱古力，濃醇甘甜，亦適合交換禮物。', 'photo-1548741487-18d363dc4469', 'Igor Lifar'),
       ('聖誕樹 Cupcake', '頂部唧上抹茶忌廉樹冠，人手一個，不用切件分食。', 'photo-1647449337399-ce46ea92a675', 'Hannia Amador'),
       ('法式聖誕馬卡龍', '紅、綠、白配色，外脆內軟，小巧易拿。', 'photo-1543921879-815164944436', 'Diliara Garifullina'),
       ('暖心心太軟聖誕 Brownie', '加熱後內餡濃郁流心，配雲呢拿雪糕，冷熱交融。', 'photo-1654796605330-8a1248a2cb07', 'ABHISHEK HAJARE')]

AO_SNK = ao('Kitchen AO 聖誕小食精選', [
    ('精緻一口酥點及烘焙', '適合拍照及站立交流', [('芒果粟子蓉冬日酥盒', '聖誕新菜｜日本栗子蓉配新鮮芒果粒，酸甜開胃的前菜', ''), ('蠔油鮑汁野菌鮑魚酥', '中式鮑魚融入酥皮點心，節日感十足', ''), ('明太子芝士忌廉牛角酥', '日式鹹甜風味', ''), ('焗雙色芝士吞拿魚脆法包', '外脆內軟，芝士拉絲', '')]),
    ('異國惹味熱食', '適合配啤酒及香檳', [('西班牙手工伊比利黑毛豬可樂餅', '外皮酥脆，內餡綿密', ''), ('西班牙辣肉腸熔岩芝士杯', '微辣肉腸配三重芝士', ''),
        ('墨西哥芝士粟米片配三色醬', '分享必備', P + 'a3100-cheese-nachos-with-flavorful-three-colour-salsa/'), ('忌廉芝士嫩雞墨西哥餡餅', '薄餅夾嫩雞及芝士', ''),
        ('日式雞皮餃子配酥炸洋蔥圈', '居酒屋風味', P + 'a1600-japanese-chicken-skin-dumplings-with-crispy-onion-rings/'), ('九層塔香酥雞', '外酥內嫩，佐酒一流', P + 'a2800-crispy-basil-chicken-dice/')]),
    ('創意海鮮及手工肉丸', '老少咸宜', [('鹹蛋黃焗釀蟹蓋', '蟹肉鮮味突出', ''), ('法式聖誕龍蝦汁燴蛋餃', '龍蝦湯慢燴手工蛋餃', ''),
        ('懷舊芝麻蝦滑多士配泰汁', '港式經典', P + 'a3400-deep-fried-sesame-shrimp-toast-with-thai-sauce/'), ('迷你芝士手打漢堡', '手打肉餅多汁', P + 'a0700-handmade-mini-cheeseburger/'),
        ('夏威夷茄醬菠蘿燴手工肉丸', '酸甜解膩', ''), ('蜜蜜燒雞翼配脆薯角', '最快被清盤的單品', P + 'a0500-honey-glazed-chicken-wings-w-potato-wedges/')])], '查看聖誕到會套餐', [('20_26xmas-chestnut-pastry.jpg', '芒果粟子蓉冬日酥盒')])
AO_SAL = ao('Kitchen AO 聖誕沙律及拼盤精選', [
    ('海鮮及鮮果沙律', '', [('啖啖松葉蟹三文魚籽芒果沙律', '鮮味層次分明', ''), ('皇帝蟹棒蟹肉芒果牛油果沙律', '配檸檬蛋黃醬', ''),
        ('紅寶神石榴大蝦柚肉沙律', '柚子檸檬油醋汁，酸甜解膩', ''), ('紅寶神石榴煙火雞胸蜜桃沙律', '青瓜乳酪醬，清爽輕盈', ''),
        ('油香煙三文魚特調凱撒沙律', '特製凱撒醬', P + 's0300-smoked-salmon-caesar-salad/')]),
    ('聖誕神秘加配｜派對焦點冷盤', '', [('聖誕樹芝士火腿拼盤（Shiny Cold Cut Tree-style Platter）', '火腿、芝士、乾果及果仁砌成立體聖誕樹，上桌即成拍照焦點', '')])], '瀏覽造型拼盤及沙律', [('20_26xmas-prawn-salad.jpg', '紅寶神石榴大蝦柚肉沙律')])
AO_MAIN = ao('Kitchen AO 聖誕主菜精選', [('', '', [
    ('寶箱煙燻慢煮美國牛翼板肉', '稀有下肩胛翼板肉，慢煮後煙燻炙烤，復古寶箱盛載，全港限量 100 個', ''),
    ('燒南乳香慢煮原隻黃油雞，配聖誕玫瑰金巴利汁', '本地黃油雞，皮脆肉滑，中西合璧', ''),
    ('紅酒慢燴鮮蕃茄和牛牛肋條', '慢火燉煮數小時，軟嫩入味', P + 'm0240-red-wine-braised-fresh-tomato-and-wagyu-beef-short-ribs-4-pounds/'),
    ('香烤寶雲酥羊架（五至七成熟）', '香草芥末麵包糠，外酥內嫩', ''),
    ('西班牙脆嫩乳香乳豬', '皮脆如玻璃，帶淡淡奶香', P + 'm0600-spanish-style-crispy-suckling-pig/'),
    ('烤燶邊香草蜜糖鹿兒島叉燒扒', '邊緣焦香，蜜糖香草交融', ''),
    ('炭烤泰式檸檬葉爆汁豬頸肉', '爽脆爆汁，配酸辣汁', '')])], '查看聖誕主菜套餐', [('20_26xmas-beef-box.jpg', '寶箱煙燻慢煮美國牛翼板肉'), ('20_26xmas-chicken-2.jpg', '燒南乳香慢煮原隻黃油雞')])
AO_PAS = ao('Kitchen AO 節日意粉及飯精選', [
    ('意粉', '', [('黑松露野菌蘆筍忌廉扁意粉', '掛汁力強', ''), ('爆炒 XO 醬蜆肉香蒜意大利麵', '港式鑊氣', P + 'p04l-pan-fried-xo-sauce-clam-and-garlic-pasta-4-pounds/'),
        ('香濃鹹蛋黃卡邦尼長通粉', '流沙鹹蛋黃芝士醬', ''), ('芝士焗特調肉醬蝴蝶粉', '焗至芝士拉絲', '')]),
    ('飯', '', [('雙重龍蝦三重芝士煲仔鍋飯', '原個布袋芝士流心，飯底吸滿龍蝦汁', ''), ('玫瑰醬泡菜海蝦意大利飯', '韓式玫瑰醬，微辣開胃', ''),
        ('泰國蝦頭油珍珠帶子海鮮蟹籽炒飯', '粒粒分明，鮮味滿溢', '')])], '預訂聖誕主食', [('20_26xmas-bowl-jai.jpg', '雙重龍蝦三重芝士煲仔鍋飯'), ('20_26xmas-korea-rice.jpg', '玫瑰醬泡菜海蝦意大利飯')])
AO_DES = ao('Kitchen AO 冬日手工甜品', [('', '', [
    ('聖誕馴鹿脆脆開心果朱古力撻', '開心果白朱古力醬配脆脆及開心果碎，朱古力曲奇鹿角，輕盈應節', ''),
    ('法式七彩馬卡龍', '小巧易拿', P + 'd01-french-colorful-macarons-10-pieces/'),
    ('珍珠泡芙', '配咖啡及茶', P + 'd05-pearl-sugar-puffs-10pic/')])], '預訂聖誕甜品', [('20_26xmas-pistachio-tart.jpg', '聖誕馴鹿脆脆開心果朱古力撻')])

EB = ('<div class="xeb"><div class="xeb-l xbg"><svg class="sf" style="right:14px;top:12px;width:22px" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2v20M3.3 7l17.4 10M3.3 17L20.7 7M12 5l-2-2M12 5l2-2M12 19l-2 2M12 19l2 2" stroke="currentColor" stroke-width="1.4" fill="none" stroke-linecap="round"/></svg><small>MEGA EARLY BIRD</small><b>聖誕套餐 七九折</b><span>即日起至 2026 年 11 月 30 日 23:59</span></div>'
      '<div class="xeb-c"><small>優惠碼</small><b>MEGA79</b><span>21% OFF</span></div></div>')
SNOW = ('<svg class="sf" style="{s}" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2v20M3.3 7l17.4 10M3.3 17L20.7 7M12 5l-2-2M12 5l2-2M12 19l-2 2M12 19l2 2" '
        'stroke="currentColor" stroke-width="1.4" fill="none" stroke-linecap="round"/></svg>')
TOC = [('snacks', '聖誕小食'), ('salad', '沙律、冷盤及拼盤'), ('mains', '聖誕主菜'), ('pasta', '意粉及飯'), ('dessert', '甜品、蛋糕及薑餅人'),
       ('diy', '聖誕小食 DIY'), ('portion', '份量配搭公式'), ('budget', '預算參考'), ('tips', '保溫及送貨貼士'), ('venues', '不同場地派對安排'), ('faq', '常見問題'), ('summary', '編輯總結')]
tocli = ''.join(f'<li><a href="#{a}"><i>{i:02d}</i>{t}</a></li>' for i, (a, t) in enumerate(TOC, 1))
def h2(i, a, t): return f'<h2 class="ao-h2" id="{a}"><span class="no">{i:02d}</span>{t}</h2>'

FAQ = [('聖誕派對食物有甚麼？', '常見的聖誕派對食物包括手指小食（焗釀蘑菇、煙三文魚小食、雞翼）、沙律及冷盤、焦點主菜（火雞、燒牛肉、原隻烤雞、乳豬）、意粉或焗飯，以及聖誕蛋糕、薑餅人曲奇等甜品。'),
       ('聖誕派對要準備多少食物？', '8 至 10 人約需 3 至 4 款小食、1 款沙律、1 款主菜、1 款主食及 1 款甜品；18 至 22 人可增至 5 至 6 款小食及雙主菜。詳細可參考上方的份量配搭公式。'),
       ('聖誕派對小食有甚麼推介？', '宜選方便拿取、不沾手的一口小食，例如焗釀蘑菇、煙三文魚小食、雞翼、迷你漢堡及芝士杯，並混合冷熱款式，照顧不同口味。'),
       ('一隻火雞夠幾多人吃？', '一般按每人約 1 磅（約 450 克）連骨火雞估算，即 12 磅火雞約夠 10 至 12 人。如同時有其他主菜，份量可酌量減少。'),
       ('Panettone 和聖誕蛋糕有甚麼分別？', 'Panettone 是意大利傳統發酵糕點，組織似麵包，內有果乾，較耐存放；聖誕忌廉蛋糕需冷藏，口感輕盈，造型較多變化。'),
       ('聖誕派對食物預算每位大約幾錢？', '市面連鎖快餐聖誕套餐一般約每位 HK$70 至 200；到會派對套餐包括原隻主菜、沙律、主食及甜品，以 Kitchen AO 2026 聖誕套餐為例，原價約每位 HK$226 至 386，人數愈多每位愈低。'),
       ('聖誕派對食物怎樣保溫？', '冷熱食物分開處理：先上冷盤及沙律，熱食開餐前才打開；炸物宜用透氣容器，燉煮及焗飯類保溫度較高。場地沒有焗爐時，可預備保溫袋或加配暖爐。'),
       ('薑餅人有甚麼由來？', '薑餅在中世紀歐洲已出現，相傳十六世紀英國伊利沙伯一世曾命人把薑餅造成賓客模樣；十九世紀《糖果屋》童話令薑餅屋在德國流行，其後薑餅人及薑餅屋成為聖誕節象徵。'),
       ('Party Room 聖誕派對食物怎樣安排？', '先確認 Party Room 入場時間、送貨可否直送房間及有沒有雪櫃，送貨時間宜定在入場後 15 至 30 分鐘。Party Room 多數只有微波爐，宜選燉煮、焗飯及原隻燒肉等保溫度高的菜式，炸物最後吃，並預留長枱冷熱分開擺放。'),
       ('學校、教會或機構聖誕活動訂到會要注意甚麼？', '先確認場地的飲食及明火規定，按出席上限選套餐並加配後備小食，預先統計素食、清真及過敏需要；機構採購如需正式報價及收據，可先索取報價。'),
       ('聖誕派對食物要提早幾多預訂？', '平安夜及聖誕節是送貨高峰，時段較快額滿，建議盡早預訂。2026 年 11 月 30 日 23:59 前預訂聖誕套餐，輸入優惠碼 MEGA79 更可享七九折（21% OFF）。')]
faqh = ''.join(f'<details class="ao-faq"{" open" if i == 0 else ""}><summary>{q}</summary><div class="a">{a}</div></details>' for i, (q, a) in enumerate(FAQ))
ld = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}, ensure_ascii=False)
WA = 'https://wa.me/85269011987?text=' + urllib.parse.quote('你好，我想查詢聖誕派對食物及套餐。')

def row(pax, a, b, c, d, e, link):
    L = ['小食', '沙律／冷盤', '主菜', '意粉／飯', '甜品']
    return (f'<tr><td class="rh">{pax}</td>' + ''.join(f'<td data-label="{l}">{v}</td>' for l, v in zip(L, [a, b, c, d, e]))
            + f'<td data-label="參考套餐"><a class="todo" href="#">{link}</a></td></tr>')

# KV Option 1（由 kv_xmas.py 取得；手機 .m 規則轉為 @media）
import re as _re
_src = open(os.path.join(HERE, 'kv_xmas.py'), encoding='utf-8').read().split('def pair(')[0].replace("OUT = sys.argv[1]", "")
_kv = {}; exec(_src, _kv)
_mob = '\n'.join(l.replace('.m .k', '.k') for l in _kv['CSS'].splitlines() if l.startswith('.m '))
_base = '\n'.join(l for l in _kv['CSS'].splitlines() if not l.startswith('.m ') and not l.startswith('.k2') and not l.startswith('/* ===== Option 2'))
KVCSS = _base + '\n.ao-article .kvw{margin:0 0 26px;border-radius:14px;overflow:hidden}\n@media(max-width:640px){' + _mob + '}'
KV = '<div class="kvw">' + _kv['k1']() + '</div>'
KVFONT = _kv['FONT']
CSS = open(os.path.join(HERE, 'master.css'), encoding='utf-8').read() + open(os.path.join(HERE, 'xmas.css'), encoding='utf-8').read() + KVCSS

page = f'''<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>聖誕派對食物 2026｜香港人聖誕派對吃甚麼？小食、主菜及甜品推介｜Kitchen AO</title>
<meta name="description" content="香港人聖誕派對吃甚麼？2026 聖誕派對食物一次看：開胃小食、沙律冷盤、焦點主菜、意粉及飯、聖誕蛋糕與甜品，附份量配搭公式及常見問題。">
{KVFONT}<style>{CSS}</style><script type="application/ld+json">{ld}</script></head><body>
<div class="mk"><b>Mock-up v2（2026-11-15）</b>｜Blog 2 聖誕派對食物｜灰色連結＝網址待補；主圖用 KV Option 1（相片暫用 Unsplash）；市面常見推介相片來自 Unsplash，統一 4:3 智能裁切</div>
<div class="page">
<div class="crumb"><a href="https://aoaodelivery.com/">首頁</a> / <a href="https://aoaodelivery.com/blog/category/catering-tips/">香港到會資訊</a> / 聖誕派對食物指南</div>
<h1 class="ttl">香港人聖誕派對吃甚麼？2026 聖誕派對食物指南｜小食、主菜、甜品及蛋糕推介</h1>
<p class="meta">Kitchen AO 編輯部｜最後更新 2026-11-15｜閱讀約 8 分鐘</p>
<div class="lay"><main class="ao-article">
{KV}
<p>臨近年尾，籌備聖誕聚會最花心思的，往往是敲定菜單。既要照顧不同朋友及同事的口味，又要兼顧拍照效果及保溫質素，一桌豐富得體的<strong>聖誕派對食物</strong>，正是聚會成功的關鍵。</p>
<p>這篇指南整理了香港人聖誕派對最常見的食物：由暖場小食、沙律冷盤、焦點主菜，到飽肚的意粉及飯，以至應節蛋糕與甜品，同時精選 Kitchen AO 的聖誕外賣單品。</p>
<p>簡單來說，聖誕派對菜單可按「小食、沙律、主菜、主食、甜品」五類配搭：小食負責暖場，沙律及冷盤平衡油膩，主菜是全場焦點，意粉或飯確保賓客吃得飽，最後以蛋糕或甜品作結。人數愈多，款數亦要相應增加：8 至 10 人約準備 7 至 8 款食物，18 至 22 人約 12 至 14 款，並可安排一款牛或豬配一款雞或海鮮作雙主菜。各人數的詳細配搭，可參考下文的<a href="#portion">份量配搭公式</a>。</p>
<div class="sb mtoc"><p class="sb-h">目錄</p><ol class="sb-toc">{tocli}</ol></div>
{EB}
{h2(1, 'snacks', '聖誕小食：派對暖場的開胃手指食物')}
<p>籌備聖誕派對食物時，開胃小食的定位在於「暖場」與「方便」。賓客剛到場時忙於寒暄，方便拿取、不沾手的一口小食最受歡迎。</p>
<p class="sub">市面常見聖誕小食</p>{dishes(SNK)}{AO_SNK}
{h2(2, 'salad', '聖誕沙律、冷盤及拼盤：提升餐桌儀式感')}
<p>在大魚大肉之間，清爽的沙律及視覺吸睛的冷盤，是平衡味蕾及提升餐桌顏值的關鍵。</p>
<p class="sub">市面常見聖誕沙律及冷盤</p>{dishes(SAL)}{AO_SAL}
{h2(3, 'mains', '聖誕主菜：焦點核心與經典故事')}
<h3 class="ao-h3">為甚麼聖誕節一定有火雞及火腿？</h3>
<p>在西方傳統中，火雞（Turkey）及蜜汁火腿（Ham）一直是家庭盛宴的象徵。火雞體型大，一隻足夠全家及親友分享，逐漸成為「團圓、慷慨與分享」的節日代表；蜜汁火腿則源於歐洲古老習俗，寓意來年豐收吉祥。</p>
<p class="sub">市面常見聖誕主菜</p>{dishes(MAIN)}{AO_MAIN}
{h2(4, 'pasta', '聖誕意粉及飯：暖胃飽肚的主食')}
<p>派對單靠小食及肉類，往往欠缺飽足感。一款味道濃郁、耐放保溫的主食，可確保每位賓客都吃得飽足。</p>
<p class="sub">市面常見聖誕意粉及飯</p>{dishes(PAS)}{AO_PAS}
{h2(5, 'dessert', '聖誕甜品、蛋糕及薑餅人：派對尾聲的甜蜜滋味')}
<p>派對尾聲，熄燈端出點起蠟燭的蛋糕，是節日氣氛最濃的一刻；小巧精緻的聖誕甜品，則方便大家一邊玩交換禮物遊戲，一邊隨手拿取。</p>
<h3 class="ao-h3">聖誕蛋糕怎樣揀？</h3>{dishes(CAKE)}
<p class="ao-tcap">Panettone 與聖誕忌廉蛋糕比較</p>
<table class="ao-rtable"><thead><tr><th></th><th>意大利聖誕蛋糕（Panettone）</th><th>聖誕忌廉蛋糕</th></tr></thead><tbody>
<tr><td class="rh">特點</td><td data-label="Panettone">傳統發酵糕點，內有酒浸提子乾及糖漬橙皮，組織鬆軟如麵包</td><td data-label="聖誕忌廉蛋糕">海綿蛋糕夾草莓或鮮果，外層是輕盈的鮮忌廉</td></tr>
<tr><td class="rh">保存</td><td data-label="Panettone">較耐存放，常溫食用</td><td data-label="聖誕忌廉蛋糕">需冷藏，宜當日食用</td></tr>
<tr><td class="rh">配搭</td><td data-label="Panettone">咖啡、紅茶或微甜氣泡酒（Moscato）</td><td data-label="聖誕忌廉蛋糕">適合任何飲品</td></tr>
<tr><td class="rh">適合</td><td data-label="Panettone">偏好歐式傳統風味的賓客</td><td data-label="聖誕忌廉蛋糕">小朋友及年輕賓客</td></tr></tbody></table>
<h3 class="ao-h3">常見應節聖誕甜品</h3>{dishes(DES)}
<h3 class="ao-h3">薑餅人的故事：為甚麼聖誕節要吃薑餅人？</h3>
<p>薑餅（Gingerbread）在中世紀歐洲已經出現，當時薑及肉桂等香料價格昂貴，加入香料的糕餅多在節慶或市集才會出售。相傳十六世紀英國伊利沙伯一世曾命宮廷廚師把薑餅造成賓客的模樣送給來訪者，人形薑餅由此廣為流傳。</p>
<p>到了十九世紀，格林兄弟的童話《糖果屋》（Hansel and Gretel）令以糖果裝飾的薑餅屋在德國大受歡迎，其後隨移民傳到歐美各地，薑餅人及薑餅屋逐漸成為聖誕節的象徵。今天，彩繪薑餅人既是派對甜品，也是聖誕樹掛飾及伴手禮。</p>
<h3 class="ao-h3">聖誕曲奇及薑餅屋</h3>
<p>除了薑餅人，聖誕曲奇亦是派對常見甜品，例如以糖霜畫上雪花、聖誕樹及襪子圖案的牛油曲奇，以及撒上糖粉的雪球曲奇。薑餅屋則適合作為派對桌上的裝飾焦點，亦可安排小朋友一起裝飾，成為派對活動之一。</p>
{AO_DES}
{h2(6, 'diy', '聖誕小食 DIY：3 款簡易派對小食做法')}
<p>想在到會套餐以外親手加一兩款小食？以下 3 款步驟簡單，毋須專業廚具，適合派對前一晚或當日準備。</p>
<h3 class="ao-h3">1. 番茄芝士聖誕花環（約 15 分鐘）</h3>
<p><strong>材料：</strong>車厘茄 1 盒、迷你水牛芝士球 1 盒、羅勒葉 1 束、橄欖油及黑醋適量</p>
<ol><li>把羅勒葉在大圓碟上排成一圈，作為花環底。</li><li>車厘茄及芝士球相間排在羅勒葉上。</li><li>上桌前淋上橄欖油及黑醋，撒少許鹽及黑椒。</li></ol>
<h3 class="ao-h3">2. 酥皮聖誕樹芝士條（約 30 分鐘）</h3>
<p><strong>材料：</strong>急凍酥皮 2 塊、青醬 3 湯匙、巴馬臣芝士碎 50 克、蛋黃 1 隻</p>
<ol><li>酥皮解凍後，一塊掃上青醬及撒上芝士碎，再蓋上另一塊。</li><li>切成三角形聖誕樹，中間切出橫條，扭成樹枝形狀。</li><li>掃上蛋黃漿，以 200°C 焗約 15 分鐘至金黃。</li></ol>
<h3 class="ao-h3">3. 簡易薑餅人曲奇（約 1 小時，另需冷藏 1 小時）</h3>
<p><strong>材料：</strong>中筋麵粉 250 克、無鹽牛油 80 克、黑糖 70 克、蜜糖 70 克、雞蛋 1 隻、薑粉 2 茶匙、肉桂粉 1 茶匙、梳打粉半茶匙</p>
<ol><li>牛油、黑糖及蜜糖隔水加熱至溶化，稍涼後加入雞蛋拌勻。</li><li>加入已篩勻的麵粉、香料及梳打粉，搓成麵糰，冷藏 1 小時。</li><li>擀成約 5 毫米厚，用模具壓出薑餅人，以 175°C 焗 8 至 10 分鐘。</li><li>放涼後以糖霜畫上表情及鈕扣。</li></ol>
<p>如派對人數較多、時間有限，可把 DIY 留給一兩款小食，主菜及其餘食物交給到會套餐，主人家亦可專心招呼賓客。</p>
{h2(7, 'portion', '聖誕派對食物份量配搭公式')}
<p>不知道要準備多少食物？可參考以下配搭公式估算：</p>
<table class="ao-rtable"><thead><tr><th>人數</th><th>小食</th><th>沙律／冷盤</th><th>主菜</th><th>意粉／飯</th><th>甜品</th><th>參考套餐</th></tr></thead><tbody>
{row('5 至 6 人', '2 至 3 款', '1 款', '1 款', '1 款', '1 款', '5-6 人聖誕套餐')}
{row('8 至 10 人', '3 至 4 款', '1 款', '1 款', '1 款', '1 款', '8-10 人聖誕套餐')}
{row('18 至 22 人', '5 至 6 款', '2 款', '2 款（一款牛或豬，一款雞或海鮮）', '2 款', '蛋糕及數款一口甜品', '18-22 人聖誕套餐')}
{row('30 人以上', '6 款以上', '2 至 3 款', '2 至 3 款', '2 至 3 款', '3 款以上', '大型聖誕派對套餐')}
</tbody></table>
<p>想省去採購、備料及烹調的工夫？Kitchen AO 的聖誕外賣派對套餐已配搭好原隻燒肉、海鮮、冷盤及小食，直送上門。公司聖誕聚會可參考<a href="https://aoaodelivery.com/corporate-catering-hk/">公司聖誕派對到會</a>。</p>
<div class="xcta xbg">{SNOW.format(s="left:22px;top:20px;width:26px")}{SNOW.format(s="right:28px;bottom:22px;width:18px")}<small>CHRISTMAS CATERING 2026</small><b>聖誕派對菜單，交給 Kitchen AO</b><span>已按人數配搭好的聖誕到會套餐，直送上門</span><a class="todo" href="#">瀏覽聖誕到會套餐</a></div>
{h2(8, 'budget', '聖誕派對食物預算參考：每位大約幾錢？')}
<p>聖誕派對食物的預算，主要視乎形式而定。市面連鎖快餐的聖誕套餐一般約每位 HK$70 至 200，以炸雞、焗飯及小食為主；到會派對套餐則包括原隻主菜、沙律、意粉或飯及甜品，每位預算較高，但毋須自行採購及烹調。</p>
<p class="ao-tcap">Kitchen AO 2026 聖誕套餐每位價錢<small>按原價及人數上下限計算；11 月 30 日前輸入 MEGA79 可再享七九折</small></p>
<table class="ao-rtable"><thead><tr><th>人數</th><th>原隻黃油雞聖誕套餐</th><th>牛翼板肉盛宴聖誕套餐</th></tr></thead><tbody><tr><td class="rh">5 至 6 人</td><td data-label="原隻黃油雞聖誕套餐">HK$281–338</td><td data-label="牛翼板肉盛宴聖誕套餐">HK$321–386</td></tr><tr><td class="rh">8 至 10 人</td><td data-label="原隻黃油雞聖誕套餐">HK$279–349</td><td data-label="牛翼板肉盛宴聖誕套餐">HK$303–379</td></tr><tr><td class="rh">12 至 16 人</td><td data-label="原隻黃油雞聖誕套餐">HK$266–354</td><td data-label="牛翼板肉盛宴聖誕套餐">HK$287–382</td></tr><tr><td class="rh">18 至 22 人</td><td data-label="原隻黃油雞聖誕套餐">HK$245–299</td><td data-label="牛翼板肉盛宴聖誕套餐">HK$268–327</td></tr><tr><td class="rh">26 至 30 人</td><td data-label="原隻黃油雞聖誕套餐">HK$246–284</td><td data-label="牛翼板肉盛宴聖誕套餐">HK$263–303</td></tr><tr><td class="rh">35 至 40 人</td><td data-label="原隻黃油雞聖誕套餐">HK$232–265</td><td data-label="牛翼板肉盛宴聖誕套餐">HK$247–283</td></tr>
<tr><td class="rh">48 至 100 人</td><td data-label="開箱雙寶聖誕套餐" colspan="2">開箱雙寶聖誕套餐：約 HK$226–259</td></tr></tbody></table>
<p>一般來說，人數愈多，每位平均價錢愈低。預算有限時，可選人數範圍上限較接近實際人數的套餐，再加配一兩款單點小食。</p>
{h2(9, 'tips', '聖誕派對食物保溫及送貨貼士')}
<h3 class="ao-h3">食物保溫：冷熱分開，熱食最後上桌</h3>
<ul><li>先上冷盤、沙律及煙三文魚小食招呼賓客，熱食留待開餐前才打開。</li><li>炸物及酥皮類宜用透氣容器，避免蒸氣令外皮變腍；燉煮及焗飯類保溫度較高，可放較後。</li><li>如場地沒有焗爐，可預備保溫袋或加配暖爐，Kitchen AO 亦提供<a href="https://aoaodelivery.com/product-category/party-supplies/thin-crust-pizza/">餐具及暖貼加配</a>。</li><li>聖誕忌廉蛋糕及忌廉甜品需冷藏，宜開餐前才取出。</li></ul>
<h3 class="ao-h3">送貨時段：平安夜及聖誕節要提早預留</h3>
<ul><li>平安夜（12 月 24 日）及聖誕節（12 月 25 日）是全年到會送貨高峰，熱門時段較快額滿，宜盡早確定日期及時間。</li><li>預留至少 30 分鐘緩衝時間，避免開餐時間與送貨時間太接近。</li><li>落單時寫清楚收貨人、電話及大廈資料，送貨安排可參考<a href="https://aoaodelivery.com/delivery/">送貨需知</a>。</li></ul>
{h2(10, 'venues', '不同場地的聖誕派對到會安排：Party Room、辦公室、家中及活動場地')}
<p>同一份聖誕派對食物，放在 Party Room、辦公室或學校禮堂，安排可以完全不同。場地有沒有升降機、可否提早入場、有沒有雪櫃及焗爐，都會影響食物款式、送貨時間及擺放方法。以下按常見場地整理重點，訂餐前可逐項確認。</p>
<p class="ao-tcap">不同聖誕派對場地重點一覽</p>
<table class="ao-rtable"><thead><tr><th>場地</th><th>最常見問題</th><th>食物建議</th><th>訂餐前要確認</th></tr></thead><tbody>
<tr><td class="rh">Party Room</td><td data-label="最常見問題">按時段租用，入場時間短；多數只有微波爐</td><td data-label="食物建議">以拼盤、冷盤及耐放熱食為主，炸物最後上</td><td data-label="訂餐前要確認">入場時間、送貨可否直送房間、有沒有雪櫃</td></tr>
<tr><td class="rh">辦公室</td><td data-label="最常見問題">大廈收貨規定多，午飯時間有限</td><td data-label="食物建議">一口小食、分格食物，方便同事站立取食</td><td data-label="訂餐前要確認">送貨升降機、收貨登記、會議室枱面</td></tr>
<tr><td class="rh">家中</td><td data-label="最常見問題">枱面有限，同時要準備其他菜式</td><td data-label="食物建議">一款原隻主菜配沙律及甜品，餘下自己加配</td><td data-label="訂餐前要確認">焗爐翻熱、雪櫃位置、碟具數量</td></tr>
<tr><td class="rh">學校、教會及機構</td><td data-label="最常見問題">人數多、年齡層闊，部分場地不可明火</td><td data-label="食物建議">份量清楚的大型套餐，加配兒童及素食選擇</td><td data-label="訂餐前要確認">場地飲食規定、過敏及素食人數、清潔安排</td></tr>
<tr><td class="rh">會所、天台及戶外</td><td data-label="最常見問題">天氣及溫度影響保溫，搬運路線較長</td><td data-label="食物建議">保溫度高的燉煮、焗飯及原隻燒肉</td><td data-label="訂餐前要確認">卸貨位置、手推車、遮擋及照明</td></tr>
<tr><td class="rh">遊艇船河</td><td data-label="最常見問題">要配合開船時間，船上空間細</td><td data-label="食物建議">即食冷盤、手指食物及有蓋容器裝的熱食</td><td data-label="訂餐前要確認">碼頭位置、上船時間、船上有沒有雪櫃</td></tr>
</tbody></table>
<h3 class="ao-h3">Party Room 聖誕派對到會</h3>
<p>Party Room 是近年香港人聖誕聚會的熱門選擇，但多數按時段計錢，入場後才開始佈置，時間比在家更緊。食物安排的重點是「入場即開餐、散場即收拾」。</p>
<ul><li><strong>送貨時間：</strong>先向 Party Room 確認幾點可入場，送貨時間定在入場後 15 至 30 分鐘最穩妥；部分 Party Room 不准提早放貨，亦不代收。</li>
<li><strong>送貨地點：</strong>工廈 Party Room 要問清楚貨用升降機、樓層及單位號碼，晚上及假日是否需要登記。</li>
<li><strong>翻熱設備：</strong>大部分 Party Room 只有微波爐，未必有焗爐；宜選燉煮、焗飯、原隻燒肉等保溫度高的菜式，炸物及酥皮放在最後吃。</li>
<li><strong>枱面及擺放：</strong>遊戲機、卡拉 OK 及枱球枱會佔去不少位置，預先留一張長枱擺食物，冷熱分開；可加配<a href="https://aoaodelivery.com/product-category/party-supplies/kid-food-stand/">三層氣氛食物架</a>節省枱面。</li>
<li><strong>餐具及清潔：</strong>確認 Party Room 有沒有提供碗碟、垃圾袋及廚餘處理，否則自備即棄餐具，散場前預留 15 分鐘收拾。</li></ul>
<h3 class="ao-h3">辦公室及公司聖誕派對</h3>
<ul><li><strong>大廈收貨安排：</strong>先向管理處確認送貨升降機、收貨時間及是否需要登記。</li><li><strong>枱面及位置：</strong>預留足夠長枱，冷熱食物分區擺放，方便同事排隊取食。</li><li><strong>餐具及垃圾：</strong>準備即棄餐具、紙巾及足夠垃圾袋，開餐後清理更快。</li><li><strong>開餐時間：</strong>午餐派對宜安排在 12:30 前送達，晚上派對則預留時間擺盤。</li><li><strong>飲食需要：</strong>事前收集同事的素食或過敏需要，並在食物旁標示。</li></ul>
<p>公司聖誕聚會的安排，可參考<a href="https://aoaodelivery.com/corporate-catering-hk/">公司聖誕派對到會</a>。</p>
<h3 class="ao-h3">家中聖誕聚會</h3>
<ul><li><strong>主菜交給到會，其餘自己加：</strong>一款原隻主菜配沙律及甜品已有足夠節日感，主人家可專心招呼客人，再親手做一兩款上文的 DIY 小食。</li>
<li><strong>翻熱次序：</strong>焗爐通常只有一個，先翻熱原隻燒肉，再翻熱焗飯，炸物最後放入焗爐數分鐘回脆。</li>
<li><strong>雪櫃空間：</strong>忌廉蛋糕、沙律及飲品都要冷藏，派對前一日先清出位置。</li>
<li><strong>小朋友及長輩：</strong>預備少辣、易咬的選擇，例如肉丸、意粉及軟身甜品。</li></ul>
<h3 class="ao-h3">學校、教會及機構聖誕活動</h3>
<ul><li><strong>場地規定：</strong>學校禮堂、教會及社區中心多數不可明火，部分場地限制食物進入的時間，宜先向負責人確認。</li>
<li><strong>人數及份量：</strong>活動人數常有變動，可按出席上限選套餐，另加配一兩款單點小食作後備。</li>
<li><strong>飲食需要：</strong>學生、長者及不同信仰的參加者較多，預先統計素食、清真及過敏需要，並在食物旁清楚標示。</li>
<li><strong>分發方式：</strong>人多時可安排義工分發，或選一口份量的小食，減少排隊時間。</li>
<li><strong>單據及報價：</strong>機構採購多需要正式報價及收據，可先經<a href="https://aoaodelivery.com/catering-quote-enquiry/">到會報價查詢</a>索取。</li></ul>
<h3 class="ao-h3">會所、天台及戶外聖誕派對</h3>
<ul><li><strong>保溫：</strong>十二月晚上氣溫較低，熱食冷得快，宜選保溫度高的菜式，並加配暖爐或保溫袋。</li>
<li><strong>搬運路線：</strong>確認卸貨位置及由停車場到場地的距離，需要時預備手推車。</li>
<li><strong>天氣後備：</strong>預留室內或有遮擋的位置擺放食物，避免風吹及落雨。</li>
<li><strong>照明：</strong>晚上戶外光線不足，食物枱附近宜加燈，方便賓客取食。</li></ul>
<h3 class="ao-h3">遊艇船河聖誕派對</h3>
<ul><li><strong>上船時間：</strong>食物要在開船前送到碼頭，送貨時間宜比上船時間早 30 分鐘，並寫清楚碼頭及船名。</li>
<li><strong>空間及搖晃：</strong>船上枱面細而且會搖晃，宜選有蓋容器及一口份量的食物，避免湯汁太多。</li>
<li><strong>雪櫃：</strong>確認船上有沒有雪櫃，忌廉甜品及生冷食物宜先放保冷袋。</li>
<li>出海派對的套餐可參考<a href="https://aoaodelivery.com/product-category/party/boat-party-set/">船河派對套餐</a>。</li></ul>
{h2(11, 'faq', '常見問題')}{faqh}
{h2(12, 'summary', '編輯總結')}
<p>一桌得體的聖誕派對食物，重點在於冷熱、鹹甜及輕重的平衡：先以一口小食暖場，再以沙律冷盤提升餐桌顏值，焦點主菜帶起氣氛，意粉或飯確保賓客吃得飽，最後以蛋糕或一口甜品作結。按人數參考份量配搭公式，便可避免食物不足或過剩。</p>
<p>如想省時省力，可直接選擇已配搭好的聖誕到會套餐。</p>{EB}
<p class="ao-tcap">資料來源</p><ol class="src"><li>USDA Food Safety and Inspection Service〈Let's Talk Turkey: A Consumer Guide to Safely Roasting a Turkey〉（火雞份量估算）</li><li>Kitchen AO 單點食物及聖誕套餐產品頁</li></ol>
<p class="src">資料於 2026 年 11 月查閱。市面常見推介相片來自 Unsplash。</p>
</main>
<aside><div class="stk">
<div class="sb"><div class="sb-meta"><div><b>作者</b>Kitchen AO 編輯部</div><div><b>更新</b>2026-11-15</div><div><b>閱讀</b>約 8 分鐘</div></div></div>
<div class="sb"><p class="sb-h">目錄</p><ol class="sb-toc" id="stoc">{tocli}</ol></div>
<div class="sb sb-eb xbg"><small>MEGA EARLY BIRD</small><b>聖誕套餐七九折</b><div class="code">MEGA79</div><span>21% OFF｜至 2026-11-30 23:59</span></div>
<div class="sb"><p class="sb-h">推介聖誕套餐</p>
<a class="sb-p todo" href="#">聖誕金雞獻禮 5-6 人<b>HK$1,688</b></a><a class="sb-p todo" href="#">聖誕寶藏箱 5-6 人<b>HK$1,928</b></a>
<a class="sb-p todo" href="#">聖誕寶藏箱 12-16 人<b>HK$4,588</b></a><a class="sb-p todo" href="#">聖誕開箱雙寶 48-54 人<b>HK$12,418</b></a>
<a class="sb-all todo" href="#">查看全部聖誕到會套餐 →</a></div>
<div class="sb sb-wa xbg"><b>聖誕派對想配搭菜單？</b>告訴我們日子、人數及預算，客服為你配搭。<a href="{WA}" target="_blank" rel="noopener">WhatsApp 查詢</a></div>
</div></aside></div></div>
<script>(function(){{var L=[].slice.call(document.querySelectorAll('#stoc a')),S=L.map(function(a){{return document.querySelector(a.getAttribute('href'))}});
function f(){{var y=scrollY+100,i=-1;S.forEach(function(s,k){{if(s&&s.offsetTop<=y)i=k}});L.forEach(function(a,k){{a.classList.toggle('on',k===i)}})}}
addEventListener('scroll',f,{{passive:true}});f();[].forEach.call(document.querySelectorAll('a.todo'),function(a){{a.addEventListener('click',function(e){{e.preventDefault()}})}})}})();</script>
</body></html>'''
open(OUT, 'w', encoding='utf-8').write(page)
print('ok', len(page))
