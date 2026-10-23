# -*- coding: utf-8 -*-
# B6 第二稿：以客戶新稿（docx）為基礎，按 B2 定義統一、補回 B6 關鍵字
from common import *
import kv_mag, kv_b6_fonts, pathlib, re
PID = 'B6'
BLOGS['B6'] = ('Vegan、Vegetarian 中文是甚麼？Flexitarian、Pescatarian 有何分別？港台歐美素食用詞一次看清', BLOGS['B6'][1])

W = 'https://aoaodelivery.com/wp-content/uploads/2026/10/veg-b2-kv-'
MCOLS = [(W + 'egg.jpg', '蛋奶素', 'Lacto-ovo-vegetarian'), (W + 'milk.jpg', '奶素', 'Lacto-vegetarian'),
         (W + 'wuxin.jpg', '五辛素', 'Five pungent spices'), (W + 'vegan.jpg', '純素', 'Vegan')]
KVT = dict(kicker='素食英文速查', ttl='Vegan 中文是甚麼？<br>素食英文<em>一表看清</em>',
           dek='Vegetarian、Vegan、Flexitarian……<br>點餐英文一次學會！')

LEG = '<p class="ao-tcap" style="margin:10px 0 4px!important">下表「中文」一欄為香港常用譯法；詳細的素食分類及出處，可參考{}。</p>\n'
B2L = link('B2', '《素食分類天書》')

body = f'''
<p class="ao-intro">{k('素食')}愈來愈普及：有人為了健康，有人關注動物權益，也有人因宗教信仰而茹素。素食用語亦隨之增多：{k('Vegan 中文')}是甚麼？{k('Vegetarian 中文')}又怎樣講？素食者可以吃蛋和奶嗎？間中吃肉還算不算素食者？本文整理常用的{k('素食英文')}及中英對照，並附上到外國餐廳點餐的實用句子及對話例子。全文共整理 8 個中英對照及比較表，方便查閱。</p>
<div class="ao-qa"><p class="t">30 秒看懂</p><p><b>Vegetarian</b> 中文是「素食者」，一般不吃肉類及海鮮，但可能吃蛋和奶；<b>Vegan</b> 中文是「純素（全素）」，不吃任何動物來源食品，包括蛋、奶及蜜糖；<b>Veganism</b> 中文是「純素主義」，除飲食外，亦避免使用皮革等動物製品。至於 Flexitarian（彈性素食者）、Pescatarian（海鮮素者）等，則是少吃肉的飲食方式，並不屬於素食。</p></div>
<nav class="ao-toc"><div class="t">目錄</div><ul>
<li><a href="#veg">Vegetarian 中文是甚麼？素食者英文對照</a></li>
<li><a href="#vegan">Vegan 中文是甚麼？Veganism 中文：純素主義</a></li>
<li><a href="#diff">Vegan 和 Vegetarian 有甚麼分別？</a></li>
<li><a href="#region">香港、台灣、歐美的素食用詞有甚麼分別？</a></li>
<li><a href="#flexi">Flexitarian 中文是甚麼？與 Pescatarian 有何分別？</a></li>
<li><a href="#other">素食食物及餐廳相關英文用字</a></li>
<li><a href="#say">素食者英文怎樣講？自我介紹句子</a></li>
<li><a href="#order">點餐實用素食英文</a></li>
<li><a href="#talk">素食英文對話例子：三個常見情境</a></li>
<li><a href="#faq">常見問題</a></li></ul></nav>
<style>.ao-article p.ao-tbt{{margin:18px 0 6px!important;font-size:16px!important;font-weight:800;color:#2C6E49;line-height:1.5!important}}.ao-article .ao-toc ul li,.ao-article .ao-toc ul li a{{font-size:15.5px!important;line-height:1.7!important}}@media(max-width:640px){{.ao-article .ao-toc ul li,.ao-article .ao-toc ul li a{{font-size:14.5px!important}}}}</style>

<h2 class="ao-h2" id="veg">Vegetarian 中文是甚麼？素食者英文對照</h2>
<p>{k('Vegetarian 中文')}是「素食者」，作形容詞時解「素食的」；{k('Vegetarianism 中文')}是「素食主義」（即{k('素食主義英文')}）。</p>
<p>Vegetarian 是統稱，只代表不吃肉類及海鮮；至於吃不吃蛋、奶，英文會在前面加上 Lacto（奶）或 Ovo（蛋）來區分。下表列出常見的{k('素食者英文')}，並一併列出純素（Vegan）等類型：</p>
{LEG.format(B2L)}<p class="t ao-tbt">表 1｜素食者英文對照</p>
<div class="ao-tw"><table class="ao-tbl"><thead><tr><th>英文</th><th>中文</th><th>飲食特點</th></tr></thead><tbody>
<tr><td><b>Vegetarian／Vegetarianism</b></td><td>素食者／素食主義</td><td>素食的統稱，不吃肉類及海鮮，一般可吃蛋和奶</td></tr>
<tr><td><b>Lacto-ovo-vegetarian</b></td><td>蛋奶素</td><td>吃蛋及奶類製品，不吃肉，是最常見的素食類型（{k('蛋奶素英文')}）</td></tr>
<tr><td><b>Ovo-vegetarian</b></td><td>蛋素</td><td>吃蛋，不吃肉及奶類製品</td></tr>
<tr><td><b>Lacto-vegetarian</b></td><td>奶素</td><td>吃奶類製品（如牛奶、乳酪），不吃肉及蛋</td></tr>
<tr><td><b>Buddhist vegetarian</b></td><td>佛教素／齋食</td><td>按宗教戒律不吃肉，亦不吃五辛（蔥、蒜、韭、蕎、興渠）；可否吃蛋奶視乎宗派。{k('齋菜英文')}可說 Buddhist vegetarian food</td></tr>
<tr><td><b>Five pungent spices vegetarian</b></td><td>五辛素</td><td>不吃肉類及海鮮，但可以吃五辛；這是美國農業部介紹台灣素食標示時的譯法（{k('五辛素英文')}）</td></tr>
<tr><td><b>Vegan</b></td><td>純素（全素）</td><td>不吃任何動物來源食品，包括蛋、奶及蜜糖（詳見下文）</td></tr>
<tr><td><b>Strict vegetarian</b></td><td>全素</td><td>衞生防護中心英文版以 strict vegetarian（vegan）對應全素</td></tr>
<tr><td><b>Raw vegan</b></td><td>生食純素</td><td>純素之外，只吃未經烹煮或只經低溫處理的植物性食物（{k('Raw vegan 中文')}）</td></tr>
<tr><td><b>Fruitarian</b></td><td>果食者</td><td>主要吃水果，部分人亦吃堅果及種子</td></tr>
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
<p class="t ao-tbt">表 2｜素食（Vegetarian）與純素（Vegan）比較</p>
<div class="ao-tw"><table class="ao-tbl"><thead><tr><th>項目</th><th>素食（Vegetarian）</th><th>純素（Vegan）</th></tr></thead><tbody>
<tr><td><b>飲食定義</b></td><td>不吃肉類及海鮮</td><td>不吃任何動物來源食品</td></tr>
<tr><td><b>蛋、奶、蜜糖</b></td><td>一般接受，按個人選擇分為蛋奶素、蛋素或奶素</td><td>不吃蛋、奶、芝士、蜜糖及明膠等</td></tr>
<tr><td><b>五辛</b></td><td>西方一般可吃；佛教素（齋食）不吃</td><td>西方一般可吃；台灣法規的「全素或純素」不含五辛</td></tr>
<tr><td><b>生活用品及衣著</b></td><td>較少限制，通常只規範飲食</td><td>避免真皮、羊毛、蠶絲、羽絨，以及經動物實驗的化妝及護膚品</td></tr>
<tr><td><b>理念</b></td><td>宗教信仰、個人健康、關注環保等</td><td>關注動物權益、環保及可持續發展</td></tr>
</tbody></table></div>


<h2 class="ao-h2" id="region">香港、台灣、歐美的素食用詞有甚麼分別？</h2>
<p>同一個中文詞，在香港、台灣及歐美的意思未必相同。最常令人混淆的是「全素」、「純素」與五辛：香港的定義沒有提及五辛，台灣法規的「全素或純素」不含五辛，而歐美的 Vegan 一般可以吃蔥蒜。宴客或訂餐前，宜先問清楚對方吃哪一種。</p>
<p class="t ao-tbt">表 3｜香港、台灣、歐美素食用詞比較</p>
<div class="ao-tw"><table class="ao-tbl"><thead><tr><th>用語</th><th>香港</th><th>台灣</th><th>歐美</th></tr></thead><tbody>
<tr><td><b>全素／純素</b></td><td>衞生署以「全素」對應 strict vegetarian（vegan），即不吃任何動物來源食品，沒有提及五辛</td><td>法規的「全素或純素」不含蛋、奶，亦不含五辛</td><td>Vegan：不吃任何動物來源食品，一般可吃蔥、蒜</td></tr>
<tr><td><b>五辛素</b></td><td>較少使用，一般直接說明「可以吃蔥蒜」</td><td>法規稱「植物五辛素」：不含蛋、奶，但可含五辛</td><td>沒有對應概念，Vegan 本身已可吃五辛</td></tr>
<tr><td><b>蛋奶素</b></td><td>蛋奶素</td><td>蛋奶素（另有蛋素、奶素）</td><td>Lacto-ovo-vegetarian，日常多簡稱 vegetarian</td></tr>
<tr><td><b>食齋／齋菜</b></td><td>多指佛教素，不吃五辛</td><td>多說「吃素」，佛教素亦不吃五辛</td><td>Buddhist vegetarian food</td></tr>
<tr><td><b>鍋邊素</b></td><td>較少說，有人稱「方便素」</td><td>常用，指只吃菜但接受與肉同煮</td><td>沒有正式名稱，點餐時宜直接說明</td></tr>
<tr><td><b>彈性素食</b></td><td>彈性素食者</td><td>彈性素食、彈性蔬食</td><td>Flexitarian</td></tr>
</tbody></table></div>
<p>簡單來說，向外國朋友說 vegan，對方通常不會想到五辛；招待台灣的純素朋友，則要留意菜式有沒有蔥蒜。</p>

<h2 class="ao-h2" id="flexi">Flexitarian 中文是甚麼？與 Pescatarian 有何分別？</h2>
<p>如果未打算完全戒肉，可以由少吃肉開始。以下用語都是「以植物為主、減少吃肉」的飲食方式，但除了植物性飲食外，其餘仍會吃肉或海鮮，所以並不屬於素食。</p>
<p class="t ao-tbt">表 4｜少吃肉的飲食用語</p>
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
<h3 class="ao-h3">Flexitarian 和 Pescatarian 有何分別？</h3>
<p>兩者都是少吃肉的飲食方式，亦同樣不屬於素食，分別在於「有沒有固定不吃的肉類」：</p>
<p class="t ao-tbt">表 5｜Flexitarian 與 Pescatarian 比較</p>
<div class="ao-tw"><table class="ao-tbl"><thead><tr><th>項目</th><th>Flexitarian（彈性素食者）</th><th>Pescatarian（海鮮素者）</th></tr></thead><tbody>
<tr><td><b>肉類及家禽</b></td><td>間中吃，沒有固定規限</td><td>不吃</td></tr>
<tr><td><b>魚及海鮮</b></td><td>間中吃</td><td>吃，是主要的動物蛋白來源</td></tr>
<tr><td><b>蛋、奶</b></td><td>一般會吃</td><td>一般會吃</td></tr>
<tr><td><b>飲食原則</b></td><td>以植物為主，按場合彈性調整</td><td>固定戒絕陸上動物的肉</td></tr>
<tr><td><b>英文自我介紹</b></td><td>I'm a flexitarian.</td><td>I'm a pescatarian. I eat fish but no meat.</td></tr>
</tbody></table></div>

<h2 class="ao-h2" id="other">素食食物及餐廳相關英文用字</h2>
<p>除了形容素食者的用語，到餐廳、超級市場或看外國食譜時，亦會經常遇到以下與素食食物相關的英文：</p>
<h3 class="ao-h3">素食食物及飲食</h3>
<p class="t ao-tbt">表 6｜素食食物及飲食英文</p>
<div class="ao-tw"><table class="ao-tbl"><thead><tr><th>英文</th><th>中文</th><th>意思</th></tr></thead><tbody>
<tr><td><b>Vegetarian food</b></td><td>素食食物</td><td>不含肉類及海鮮的食物，但可能含蛋奶（{k('Vegetarian food 中文')}）</td></tr>
<tr><td><b>Vegan food</b></td><td>純素食物</td><td>完全不含動物成分的食物（{k('Vegan food 中文')}）</td></tr>
<tr><td><b>Vegetarian diet</b></td><td>素食飲食</td><td>以素食為主的飲食方式（{k('Vegetarian diet 中文')}）</td></tr>
<tr><td><b>Vegan diet</b></td><td>純素飲食</td><td>完全不吃動物來源食品的飲食方式（{k('Vegan diet 中文')}）</td></tr>
<tr><td><b>Plant-based food</b></td><td>植物性食物</td><td>以植物為原料的食物，多用於包裝食品標示</td></tr>
<tr><td><b>Plant-based meat</b></td><td>植物肉</td><td>以植物蛋白製成、模仿肉類口感的替代肉</td></tr>
<tr><td><b>Mock meat</b></td><td>齋肉／素肉</td><td>傳統中式素食常見的仿製肉，多以大豆或麵筋製成</td></tr>
<tr><td><b>Dairy-free／Egg-free</b></td><td>不含奶／不含蛋</td><td>常見於包裝食品及餐牌，方便純素者及敏感人士選擇</td></tr>
</tbody></table></div>
<h3 class="ao-h3">餐廳及菜單用語</h3>
<p class="t ao-tbt">表 7｜餐廳及菜單英文</p>
<div class="ao-tw"><table class="ao-tbl"><thead><tr><th>英文</th><th>中文</th><th>意思</th></tr></thead><tbody>
<tr><td><b>Vegetarian option</b></td><td>素食選擇</td><td>餐廳為素食者提供的菜式</td></tr>
<tr><td><b>Vegetarian dish</b></td><td>素菜</td><td>不含肉類及海鮮的菜式</td></tr>
<tr><td><b>Vegetarian restaurant</b></td><td>素食餐廳</td><td>只供應素食的餐廳</td></tr>
<tr><td><b>Vegan-friendly</b></td><td>純素友善</td><td>提供純素選擇的餐廳或產品（{k('Vegan friendly 中文')}）</td></tr>
</tbody></table></div>
<h3 class="ao-h3">素食生活及活動用語</h3>
<p class="t ao-tbt">表 8｜素食生活及活動英文</p>
<div class="ao-tw"><table class="ao-tbl"><thead><tr><th>英文</th><th>中文</th><th>意思</th></tr></thead><tbody>
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
<h3 class="ao-h3">看懂外國菜單的素食標示</h3>
<ul class="ao-ck">
<li>標示 Vegetarian 或「V」的菜式只代表不含肉類及海鮮，可能含蛋、牛奶、芝士或蜜糖</li>
<li>不吃蛋奶的話，應選標示 Vegan 或「VG」的菜式</li>
<li>部分芝士以動物凝乳酶（rennet）製成，較嚴格的素食者未必會吃，可先向店員查詢</li>
<li>西方的素食菜式一般會用蔥、蒜，需要走五辛時要特別說明</li>
</ul>

<h2 class="ao-h2" id="talk">素食英文對話例子：三個常見情境</h2>
<style>.ao-article .ao-dlg{{background:#F4FBF3;border:1.5px solid #CFE8CD;border-radius:14px;padding:14px 18px;margin:12px 0 22px}}.ao-article .ao-dlg p{{margin:0 0 10px!important}}.ao-article .ao-dlg p:last-child{{margin:0!important}}.ao-article .ao-dlg b{{color:#2C6E49}}.ao-article .ao-dlg small{{display:block;color:#7a7266;font-size:15px!important;line-height:1.6}}</style>
<p>學會用語之後，以下三個情境示範實際對話時可以怎樣運用：</p>
<h3 class="ao-h3">情境一：純素者在外國餐廳點餐</h3>
<div class="ao-dlg">
<p><b>Waiter：</b>Are you ready to order?<small>可以點餐了嗎？</small></p>
<p><b>You：</b>Yes. I'm vegan. Which dishes on the menu are vegan?<small>可以。我吃純素，菜單上哪些菜式是純素的？</small></p>
<p><b>Waiter：</b>The mushroom risotto and the vegetable curry are both vegetarian.<small>野菌意大利飯和雜菜咖喱都是素食。</small></p>
<p><b>You：</b>Does the risotto contain butter or cheese? And is the curry made with chicken stock?<small>意大利飯有沒有牛油或芝士？咖喱是否用雞湯煮？</small></p>
<p><b>Waiter：</b>The risotto has parmesan, but the curry is made with vegetable stock and coconut milk.<small>意大利飯有巴馬臣芝士，但咖喱是用蔬菜湯和椰奶煮的。</small></p>
<p><b>You：</b>Great, I'll have the curry, please.<small>好的，我要咖喱，謝謝。</small></p>
</div>
<h3 class="ao-h3">情境二：公司聚會向外籍同事說明飲食需要</h3>
<div class="ao-dlg">
<p><b>Colleague：</b>We're ordering lunch for the team meeting. Do you have any dietary requirements?<small>我們會為部門會議訂午餐，你有沒有飲食要求？</small></p>
<p><b>You：</b>I'm vegetarian. I eat eggs and dairy, but no meat or seafood.<small>我吃素，吃蛋和奶，但不吃肉類及海鮮。</small></p>
<p><b>Colleague：</b>Is fish sauce okay?<small>魚露可以嗎？</small></p>
<p><b>You：</b>No, please avoid fish sauce and oyster sauce as well. Thanks!<small>不可以，麻煩也避開魚露和蠔油，謝謝！</small></p>
</div>
<h3 class="ao-h3">情境三：彈性素食者到朋友家作客</h3>
<div class="ao-dlg">
<p><b>Friend：</b>I'm making roast chicken tonight. Is that alright with you?<small>今晚我會焗雞，你可以嗎？</small></p>
<p><b>You：</b>I'm a flexitarian, so I eat mostly plant-based. I'll have the vegetables and salad, thanks.<small>我是彈性素食者，主要吃植物性食物，我吃蔬菜和沙律就可以了，謝謝。</small></p>
<p><b>Friend：</b>Should I roast the vegetables separately?<small>蔬菜要不要分開焗？</small></p>
<p><b>You：</b>No need. I don't mind if they're cooked in the same tray.<small>不用了，同一個焗盤煮也沒關係。</small></p>
</div>

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
 ('Flexitarian 和 Pescatarian 有何分別？', 'Flexitarian（彈性素食者）以植物為主，間中吃肉或魚，沒有固定規限；Pescatarian（海鮮素者）固定不吃肉類及家禽，但吃魚及海鮮。兩者都不屬於素食。'),
 ('香港、台灣、歐美的「純素」意思一樣嗎？', '不完全一樣。香港衞生署的「全素」指不吃任何動物來源食品，沒有提及五辛；台灣法規的「全素或純素」不含五辛，可吃五辛的稱為「植物五辛素」；歐美的 Vegan 一般可以吃蔥蒜。'),
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

META_T = 'Vegan、Vegetarian 中文是甚麼？Flexitarian、Pescatarian 分別｜港台歐美素食用詞'
META_D = 'Vegan 中文是純素，Vegetarian 中文是素食者；Flexitarian 和 Pescatarian 又有何分別？一表看清香港、台灣、歐美素食用詞的不同，附中英對照及點餐英文。'
open(HERE.parent / 'b6-vegan-vegetarian-meaning.html', 'w', encoding='utf-8').write(page(PID, META_T, META_D,
     ['Vegan 中文', 'Vegetarian 中文', 'Veganism 中文', '素食英文'], '', '', body, faqs, srcs, ['B2'],
     kv_html=kv_b6_fonts.block('h1')))
open(HERE.parent / 'b6-vegan-vegetarian-meaning-WORDPRESS.html', 'w', encoding='utf-8').write(
     wp_page(PID, body, faqs, srcs, [], kv_b6_fonts.block('div')))
print('b6 ok')
