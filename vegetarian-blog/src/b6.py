# -*- coding: utf-8 -*-
# B6 第二稿：以客戶新稿（docx）為基礎，按 B2 定義統一、補回 B6 關鍵字
from common import *
import kv_mag, pathlib, re
PID = 'B6'
BLOGS['B6'] = ('Vegan 中文是甚麼？與 Vegetarian 有何分別？一文看清素食英文與點餐用語', BLOGS['B6'][1])

W = 'https://aoaodelivery.com/wp-content/uploads/2026/10/veg-b2-kv-'
MCOLS = [(W + 'egg.jpg', '蛋奶素', 'Lacto-ovo-vegetarian'), (W + 'milk.jpg', '奶素', 'Lacto-vegetarian'),
         (W + 'wuxin.jpg', '五辛素', 'Five pungent spices'), (W + 'vegan.jpg', '純素', 'Vegan')]
KVT = dict(kicker='素食英文速查', ttl='Vegan 中文是甚麼？<br>素食英文<em>一表看清</em>',
           dek='Vegetarian、Vegan、Flexitarian……<br>點餐英文一次學會！')

LEG = '<p class="ao-tcap" style="margin:10px 0 4px!important">下表「中文」一欄為香港常用譯法；詳細的素食分類及出處，可參考{}。</p>\n'
B2L = link('B2', '《素食分類天書》')

body = f'''
<p class="ao-intro">{k('素食')}愈來愈普及：有人為了健康，有人關注動物權益，也有人因宗教信仰而茹素。素食用語亦隨之增多：{k('Vegan 中文')}是甚麼？{k('Vegetarian 中文')}又怎樣講？素食者可以吃蛋和奶嗎？間中吃肉還算不算素食者？本文整理常用的{k('素食英文')}及中英對照，並附上到外國餐廳點餐的實用句子。</p>
<div class="ao-qa"><p class="t">30 秒看懂</p><p><b>Vegetarian</b> 中文是「素食者」，一般不吃肉類及海鮮，但可能吃蛋和奶；<b>Vegan</b> 中文是「純素（全素）」，不吃任何動物來源食品，包括蛋、奶及蜜糖；<b>Veganism</b> 中文是「純素主義」，除飲食外，亦避免使用皮革等動物製品。至於 Flexitarian（彈性素食者）、Pescatarian（海鮮素者）等，則是少吃肉的飲食方式，並不屬於素食。</p></div>
<nav class="ao-toc"><div class="t">目錄</div><ul>
<li><a href="#veg">Vegetarian 中文是甚麼？素食者英文一覽</a></li>
<li><a href="#vegan">Vegan 中文是甚麼？Veganism 中文：純素主義</a></li>
<li><a href="#diff">Vegan 和 Vegetarian 有甚麼分別？</a></li>
<li><a href="#flexi">Flexitarian 中文是甚麼？少吃肉的飲食用語</a></li>
<li><a href="#other">其他常見素食英文用語</a></li>
<li><a href="#say">素食者英文怎樣講？自我介紹句子</a></li>
<li><a href="#order">點餐實用素食英文</a></li>
<li><a href="#faq">常見問題</a></li></ul></nav>
<style>.ao-article .ao-toc ul li,.ao-article .ao-toc ul li a{{font-size:15.5px!important;line-height:1.7!important}}@media(max-width:640px){{.ao-article .ao-toc ul li,.ao-article .ao-toc ul li a{{font-size:14.5px!important}}}}</style>

<h2 class="ao-h2" id="veg">Vegetarian 中文是甚麼？素食者英文一覽</h2>
<p>{k('Vegetarian 中文')}即「素食者」或「素食的」，複數 vegetarians 中文同樣是指素食者；{k('Vegetarianism 中文')}則是「素食主義」（即{k('素食主義英文')}是 Vegetarianism）。{k('Vegetarian food 中文')}是「素食食物」，{k('Vegetarian diet 中文')}是「素食飲食」。Vegetarian 一般指不吃肉類及海鮮，至於吃不吃蛋、奶及蜜糖等動物來源食品，就按個人習慣及信念再細分。以下是常見的{k('素食者英文')}：</p>
{LEG.format(B2L)}<div class="ao-tw"><table class="ao-tbl"><thead><tr><th>英文</th><th>中文</th><th>飲食特點</th></tr></thead><tbody>
<tr><td><b>Vegetarian／Vegetarianism</b></td><td>素食者／素食主義</td><td>素食的統稱，不吃肉類及海鮮，一般可吃蛋和奶</td></tr>
<tr><td><b>Lacto-ovo-vegetarian</b></td><td>蛋奶素</td><td>吃蛋及奶類製品，不吃肉，是最常見的素食類型（{k('蛋奶素英文')}）</td></tr>
<tr><td><b>Ovo-vegetarian</b></td><td>蛋素</td><td>吃蛋，不吃肉及奶類製品</td></tr>
<tr><td><b>Lacto-vegetarian</b></td><td>奶素</td><td>吃奶類製品（如牛奶、乳酪），不吃肉及蛋</td></tr>
<tr><td><b>Buddhist vegetarian</b></td><td>佛教素／齋食</td><td>按宗教戒律不吃肉，亦不吃五辛（蔥、蒜、韭、蕎、興渠）；可否吃蛋奶視乎宗派。{k('齋菜英文')}可說 Buddhist vegetarian food</td></tr>
<tr><td><b>Five pungent spices vegetarian</b></td><td>五辛素</td><td>不吃肉類及海鮮，但可以吃五辛；這是美國農業部介紹台灣素食標示時的譯法（{k('五辛素英文')}）</td></tr>
</tbody></table></div>
<p>一般人說「{k('食素')}」，英文可以說 eat vegetarian 或 be vegetarian；「食齋」則多指不吃五辛的佛教素，{k('食齋英文')}可說 eat Buddhist vegetarian food。</p>

<h2 class="ao-h2" id="vegan">Vegan 中文是甚麼？Veganism 中文：純素主義</h2>
<p>完全不吃任何動物來源食品的人，英文稱為 Vegan，{k('Vegan 中文')}是「純素」或「全素」，複數 vegans 中文同樣指純素者。由 Vegan 衍生的 Veganism，{k('Veganism 中文')}稱為「純素主義」。英國 The Vegan Society 於 1944 年 11 月成立時創造了 Vegan 一詞；按其定義，純素主義除了飲食，更著重生活上的實踐：</p>
<ul class="ao-ck">
<li>飲食完全沒有動物成分：不吃肉、蛋、奶及蜜糖</li>
<li>含明膠（gelatin）的食物、魚油或含乳清蛋白的零食亦不吃</li>
<li>生活上避免使用皮草、皮革等動物製品，並反對動物實驗</li>
</ul>
<p>{k('Vegan food 中文')}即「純素食物」（{k('Vegan 食物')}），{k('Vegan diet 中文')}即「純素飲食」。要留意，西方的 Vegan 一般可以吃蔥、蒜等五辛；而台灣法規所說的「全素或純素」則不含五辛，香港衞生署的定義就沒有提及五辛。</p>

<h2 class="ao-h2" id="diff">Vegan 和 Vegetarian 有甚麼分別？</h2>
<p>{k('Vegetarian 和 Vegan 的分別')}在於飲食範圍及嚴格程度：Vegetarian 主要是一種飲食選擇，通常不吃肉但接受蛋奶；Vegan 則是全方位實踐沒有動物成分的生活。</p>
<div class="ao-tw"><table class="ao-tbl"><thead><tr><th>項目</th><th>素食（Vegetarian）</th><th>純素（Vegan）</th></tr></thead><tbody>
<tr><td><b>飲食定義</b></td><td>不吃肉類及海鮮</td><td>不吃任何動物來源食品</td></tr>
<tr><td><b>蛋、奶、蜜糖</b></td><td>一般接受，按個人選擇分為蛋奶素、蛋素或奶素</td><td>不吃蛋、奶、芝士、蜜糖及明膠等</td></tr>
<tr><td><b>五辛</b></td><td>西方一般可吃；佛教素（齋食）不吃</td><td>西方一般可吃；台灣法規的「全素或純素」不含五辛</td></tr>
<tr><td><b>生活用品及衣著</b></td><td>較少限制，通常只規範飲食</td><td>避免真皮、羊毛、蠶絲、羽絨，以及經動物實驗的化妝及護膚品</td></tr>
<tr><td><b>理念</b></td><td>宗教信仰、個人健康、關注環保等</td><td>關注動物權益、環保及可持續發展</td></tr>
</tbody></table></div>
<h3 class="ao-h3">其他純素用語：Strict vegetarian、Raw vegan、Fruitarian</h3>
<div class="ao-tw"><table class="ao-tbl"><thead><tr><th>英文</th><th>中文</th><th>飲食特點</th></tr></thead><tbody>
<tr><td><b>Strict vegetarian</b></td><td>全素</td><td>衞生防護中心英文版以 strict vegetarian（vegan）對應全素，即不吃任何動物來源食品</td></tr>
<tr><td><b>Raw vegan</b></td><td>生食純素</td><td>純素之外，只吃未經烹煮或只經低溫處理的植物性食物（{k('Raw vegan 中文')}）</td></tr>
<tr><td><b>Fruitarian</b></td><td>果食者</td><td>主要吃水果，部分人亦吃堅果及種子</td></tr>
</tbody></table></div>

<h2 class="ao-h2" id="flexi">Flexitarian 中文是甚麼？少吃肉的飲食用語</h2>
<p>如果未打算完全戒肉，可以由少吃肉開始。以下用語都是「以植物為主、減少吃肉」的飲食方式，但除了植物性飲食外，其餘仍會吃肉或海鮮，所以並不屬於素食。</p>
<div class="ao-tw"><table class="ao-tbl"><thead><tr><th>英文</th><th>中文</th><th>飲食特點</th></tr></thead><tbody>
<tr><td><b>Flexitarian</b></td><td>{k('彈性素食者')}</td><td>平日以素為主，間中吃肉或魚；亦稱彈性素食主義、彈性蔬食或彈性素食飲食法</td></tr>
<tr><td><b>Plant-based</b></td><td>植物性飲食（蔬食）</td><td>以植物為主的飲食，多基於健康或環保考慮；plant based food 中文即植物性食物，{k('蔬食者英文')}可說 plant-based eater</td></tr>
<tr><td><b>Reducetarian</b></td><td>減肉主義者</td><td>不必完全戒肉，但主動減少吃紅肉及家禽</td></tr>
<tr><td><b>Climatarian</b></td><td>氣候飲食者</td><td>為減低碳足跡而選擇較多植物性食物</td></tr>
<tr><td><b>Pescatarian</b></td><td>海鮮素者</td><td>不吃陸上動物，但吃魚及海鮮（不屬素食）</td></tr>
<tr><td><b>Pollotarian</b></td><td>禽肉飲食者</td><td>不吃紅肉，但吃雞、鴨等家禽（不屬素食）</td></tr>
<tr><td><b>—</b></td><td>鍋邊素／方便素</td><td>不吃肉，但接受與肉同煮的菜；英文沒有官方對應名稱，點餐時宜直接說明</td></tr>
</tbody></table></div>
<div class="ao-warn">⚠️ Pescatarian 及 Pollotarian 仍會吃動物，宴客或訂餐時不應當作素食者安排。</div>

<h2 class="ao-h2" id="other">其他常見素食英文用語</h2>
<div class="ao-tw"><table class="ao-tbl"><thead><tr><th>英文</th><th>中文</th><th>意思</th></tr></thead><tbody>
<tr><td><b>Plant-based meat</b></td><td>植物肉</td><td>以植物蛋白製成、模仿肉類口感的替代肉</td></tr>
<tr><td><b>Mock meat</b></td><td>齋肉／素肉</td><td>傳統中式素食常見的仿製肉，多以大豆或麵筋製成</td></tr>
<tr><td><b>Vegan-friendly</b></td><td>純素友善</td><td>提供純素選擇的餐廳或產品（{k('Vegan friendly 中文')}）</td></tr>
<tr><td><b>Go vegan</b></td><td>轉吃純素</td><td>開始實踐純素飲食及生活（{k('Go vegan 中文')}）</td></tr>
<tr><td><b>Veganuary</b></td><td>純素一月</td><td>源自英國的活動，鼓勵大眾在每年一月嘗試純素（{k('Veganuary 中文')}）</td></tr>
<tr><td><b>World Vegan Day</b></td><td>世界純素日</td><td>每年 11 月 1 日，紀念 The Vegan Society 成立</td></tr>
<tr><td><b>Meatless Monday</b></td><td>無肉星期一</td><td>每逢星期一不吃肉，與香港的 Green Monday 素食星期一活動相近</td></tr>
</tbody></table></div>
<p>總括而言，素食不只是「不吃肉」，背後因宗教、信念及生活習慣衍生出不同派別及用語。想了解各類素食吃得與吃不得的食物，可參考{B2L}。</p>

<h2 class="ao-h2" id="say">素食者英文怎樣講？自我介紹句子</h2>
<p>到外國餐廳或與外籍朋友吃飯時，可以這樣介紹自己的素食習慣（{k('純素英文')}、{k('食素英文')}）：</p>
<ul class="ao-ck">
<li>蛋奶素：I'm a lacto-ovo-vegetarian.／I'm vegetarian, but I eat eggs and dairy.</li>
<li>純素：I'm vegan.</li>
<li>每星期一天吃素：I go meatless on Mondays.</li>
<li>以蔬食為主：I'm a flexitarian.／I eat a mostly plant-based diet.</li>
<li>不介意與肉同煮（鍋邊素）：I eat mostly plant-based, but I'm fine if the vegetables are cooked with meat. I'll just pick out the vegetables.</li>
</ul>

<h2 class="ao-h2" id="order">點餐實用素食英文</h2>
<ul class="ao-ck">
<li>表明身份：I'm vegetarian.／I'm vegan.</li>
<li>問有沒有素食選擇：Do you have any vegetarian options?</li>
<li>問菜式是否含蛋奶：Does this dish contain egg or dairy?</li>
<li>問有沒有隱藏的動物成分：Is this made with meat stock, fish sauce or oyster sauce?</li>
<li>要求走五辛：Could you make it without onion, garlic or spring onion?</li>
<li>不介意同鍋烹調：I don't mind if it's cooked in the same pan or oil.</li>
</ul>
'''

# CTA：沿用 B2 的 CTA 版面，改文字
cta = (HERE / 'b2.py').read_text(encoding='utf-8').split('\n')
cta = [l for l in cta if l.startswith('<div class="ao-ctabox">')][0]
cta = cta.replace('🌱 一次照顧所有素食朋友', '🌱 公司聚會有素食同事？')
cta = re.sub(r'<p>「素」味人生素食到會套餐[^<]*</p>',
             '<p>「素」味人生素食到會套餐，以香濃芝士、雞蛋、大啡菇等食材入饌，6 至 26 人均有選擇。配合 Green Monday 素食星期一活動，逢星期五落單自動享 95 折，星期一即可送到；最少提早三日預訂。</p>', cta, 1)
body += cta + '\n<p class="ao-tcap">單一訂單滿 $700，九龍指定區域免運費，港島及新界區運費半價；滿 $1,450 即享全港免運費，詳情請參閱<a href="https://aoaodelivery.com/delivery/">送貨需知</a>。</p>\n'

faqs = [
 ('Vegan 中文是甚麼？', '純素 Vegan 中文是「純素」或「全素」，指不吃任何動物來源食品，包括肉、蛋、奶及蜜糖；Veganism 中文是「純素主義」，除飲食外，亦避免使用皮革等動物製品。'),
 ('Vegetarian 中文是甚麼？', 'Vegetarian 中文是「素食者」或「素食的」，一般指不吃肉類及海鮮，但可能吃蛋和奶；Vegetarianism 中文是「素食主義」。'),
 ('Vegan 和 Vegetarian 最大的分別是甚麼？', 'Vegetarian 主要是飲食選擇，不吃肉類及海鮮，但通常接受蛋奶；Vegan 則完全不吃任何動物來源食品，並在生活上避免使用真皮、羊毛等動物製品。'),
 ('素食者可以吃蛋和喝牛奶嗎？', '視乎類型。蛋奶素（Lacto-ovo-vegetarian）吃蛋及奶類；蛋素只吃蛋；奶素只吃奶類；純素則不吃蛋奶。'),
 ('西方的 Vegan 可以吃蔥蒜嗎？', '一般可以。西方 Vegan 的理念是不使用動物，並沒有五辛的概念；但台灣法規的「全素或純素」不含五辛，佛教素亦不吃五辛。到外國點餐時如需走五辛，可說 "Could you make it without onion and garlic?"。'),
 ('不想完全戒肉，有相關的英文稱呼嗎？', '可以稱為 Flexitarian（彈性素食者），即平日以素為主、間中吃肉或魚；也可以說 I eat a mostly plant-based diet。要留意 Pescatarian（海鮮素者）仍吃魚及海鮮，並不屬於素食。'),
 ('鍋邊素、方便素的英文怎樣講？', '英文沒有官方對應名稱，說 convenience vegetarian 未必人人明白。點餐時建議直接說明："I eat mostly vegetarian, but I’m okay if it’s cooked with meat."'),
 ('蔬食（Plant-based）和純素（Vegan）有甚麼分別？', '蔬食著重飲食層面，多為健康或環保而以植物為主，彈性較大；純素則是以動物權益為核心的生活信念，飲食上完全不吃動物成分，並延伸至衣著及日用品。'),
]
srcs = [SRC['chp_en'],
        ('機構', 'The Vegan Society：Definition of veganism', 'https://www.vegansociety.com/go-vegan/definition-veganism'),
        ('機構', 'The Vegan Society：History', 'https://www.vegansociety.com/about-us/history'),
        ('機構', 'The Vegan Society：World Vegan Month', 'https://www.vegansociety.com/get-involved/world-vegan-month'),
        ('機構', 'Veganuary：About', 'https://veganuary.com/about/'),
        ('辭典', 'Merriam-Webster：flexitarian', 'https://www.merriam-webster.com/dictionary/flexitarian'),
        SRC['hku'],
        ('政府', 'USDA FAS：Food and Agricultural Import Regulations and Standards Country Report: Taiwan (2022)', 'https://apps.fas.usda.gov/newgainapi/api/Report/DownloadReportByFileName?fileName=Food+and+Agricultural+Import+Regulations+and+Standards+Country+Report_Taipei_Taiwan_TW2022-0059'),
        SRC['ao_set'], SRC['ao_del']]

META_T = 'Vegan 中文是甚麼？Vegetarian、Veganism 中文及素食英文一覽｜點餐英文'
META_D = 'Vegan 中文是純素，Vegetarian 中文是素食者，兩者有甚麼分別？一表看清蛋奶素、五辛素、Flexitarian 等素食英文及中英對照，附到外國餐廳的點餐英文句子。'
open(HERE.parent / 'b6-vegan-vegetarian-meaning.html', 'w', encoding='utf-8').write(page(PID, META_T, META_D,
     ['Vegan 中文', 'Vegetarian 中文', 'Veganism 中文', '素食英文'], '', '', body, faqs, srcs, ['B2'],
     kv_html=kv_mag.block(MCOLS, 'h1', **KVT)))
open(HERE.parent / 'b6-vegan-vegetarian-meaning-WORDPRESS.html', 'w', encoding='utf-8').write(
     wp_page(PID, body, faqs, srcs, [], kv_mag.block(MCOLS, 'div', **KVT)))
print('b6 ok')
