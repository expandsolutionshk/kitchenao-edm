# -*- coding: utf-8 -*-
from common import *
PID='B6'
T=[('Vegetarian','素食者；素食的','不吃肉類及海鮮，一般可吃蛋奶'),
('Vegan','純素者；全素','不吃任何動物來源食品，包括蛋、奶、蜜糖'),
('Veganism','純素主義','除飲食外，亦避免使用皮革等動物製品'),
('Vegetarianism','素食主義','奉行素食的理念'),
('Lacto-ovo-vegetarian','蛋奶素','吃蛋及奶類製品，不吃肉'),
('Ovo-vegetarian','蛋素','吃蛋，不吃奶類及肉'),
('Lacto-vegetarian','奶素','吃奶類，不吃蛋及肉'),
('Strict vegetarian','全素','衞生防護中心以此對應全素食（vegan）'),
('Flexitarian','彈性素食者','以素為主，間中吃肉'),
('Pescatarian','海鮮素者','不吃肉，但吃魚及海鮮'),
('Plant-based','植物性（飲食）','以植物為主，常用於食品標示'),
('Raw vegan','生機純素','只吃未經高溫烹調的純素食物'),
('Vegan-friendly','純素友善','提供純素選擇的餐廳或產品'),
('Veganuary','一月純素挑戰','源自英國，鼓勵人在一月嘗試純素'),
('Buddhist vegetarian / no five pungent spices','五辛素','不吃肉及蔥、蒜、韭等五辛；並無統一英文名稱')]
rows=''.join(f'<tr><td><b>{e}</b></td><td>{c}</td><td>{d}</td></tr>' for e,c,d in T)
body=f'''
<p class="ao-intro">{k('vegetarian 中文')}是甚麼？{k('vegan 中文')}又是甚麼意思？在餐廳菜單、食品包裝及旅行時，經常會見到這些英文字。本文以衞生署衞生防護中心的中英文分類為基礎，整理常用的{k('素食英文')}用語、Vegetarian 與 Vegan 的分別，以及點餐時可直接使用的英文句子。</p>
<div class="ao-qa"><p class="t">快速答案</p><p><b>Vegetarian</b> 的中文是「素食者」或「素食的」，一般指不吃肉類及海鮮、但可吃蛋奶的人；<b>Vegan</b> 的中文是「純素」或「全素」，指不吃任何動物來源食品（包括蛋、奶及蜜糖）。<b>{k('Veganism 中文')}</b>是「純素主義」。</p></div>
<nav class="ao-toc"><div class="t">目錄</div><ul>
<li><a href="#list">素食英文用語一覽表</a></li>
<li><a href="#diff">Vegetarian 和 Vegan 有甚麼分別？</a></li>
<li><a href="#flex">Flexitarian 彈性素食是甚麼？</a></li>
<li><a href="#words">素食者英文、齋菜英文怎樣講？</a></li>
<li><a href="#order">點餐實用英文句子</a></li>
<li><a href="#faq">常見問題</a></li></ul></nav>

<h2 class="ao-h2" id="list">素食英文用語一覽表</h2>
<div class="ao-tw"><table class="ao-tbl"><thead><tr><th>英文</th><th>中文</th><th>意思</th></tr></thead><tbody>{rows}</tbody></table></div>
<p class="ao-tcap">蛋奶素、蛋素、奶素及全素的英文對照參考衞生署衞生防護中心；Flexitarian 譯名參考香港大學傳譯課程詞彙表。</p>

<h2 class="ao-h2" id="diff">Vegetarian 和 Vegan 有甚麼分別？</h2>
<div class="ao-tw"><table class="ao-tbl"><thead><tr><th></th><th>Vegetarian 素食者</th><th>Vegan 純素者</th></tr></thead><tbody>
<tr><td>肉類、海鮮</td><td class="c n">✗</td><td class="c n">✗</td></tr>
<tr><td>蛋</td><td class="c y">✓（一般）</td><td class="c n">✗</td></tr>
<tr><td>奶類製品</td><td class="c y">✓（一般）</td><td class="c n">✗</td></tr>
<tr><td>蜜糖</td><td class="c m">△</td><td class="c n">✗</td></tr>
<tr><td>皮革、羊毛等用品</td><td class="c m">不一定</td><td class="c m">奉行純素主義者多會避免</td></tr>
</tbody></table></div>
<p>簡單來說，Vegan 是 Vegetarian 中最嚴格的一種。各類素食的中文定義及分別，可參考{link('B2','《素食分類天書》')}。</p>

<h2 class="ao-h2" id="flex">Flexitarian 彈性素食是甚麼？</h2>
<p>Flexitarian 由 flexible（彈性）及 vegetarian 組成，中文譯作「{k('彈性素食者')}」，指以植物性飲食為主、間中吃肉的人。香港推廣的 Green Monday「一週一素」便屬{k('彈性素食')}的一種，詳見{link('B4','《吃素好處與營養》')}。</p>

<h2 class="ao-h2" id="words">素食者英文、齋菜英文怎樣講？</h2>
<ul><li><b>{k('素食者英文')}：</b>vegetarian；純素者是 vegan。</li>
<li><b>食素英文：</b>to be vegetarian／to eat vegetarian（例如 I eat vegetarian on Mondays.）。</li>
<li><b>齋菜、素菜英文：</b>vegetarian dish；整份素食餐可說 vegetarian meal。</li>
<li><b>蛋奶素英文：</b>lacto-ovo-vegetarian。</li>
<li><b>素食主義英文：</b>vegetarianism；純素主義是 veganism。</li>
<li><b>Vegetarian food 中文：</b>素食；vegan food 即純素食物。</li></ul>

<h2 class="ao-h2" id="order">點餐實用英文句子</h2>
<div class="ao-tw"><table class="ao-tbl"><thead><tr><th>情境</th><th>英文句子</th></tr></thead><tbody>
<tr><td>表明身份</td><td>I'm vegetarian. / I'm vegan.</td></tr>
<tr><td>問有沒有素食</td><td>Do you have any vegetarian options?</td></tr>
<tr><td>問蛋奶</td><td>Does this dish contain egg or dairy?</td></tr>
<tr><td>問隱藏成分</td><td>Is this made with meat stock, fish sauce or oyster sauce?</td></tr>
<tr><td>五辛</td><td>Could you make it without onion, garlic or spring onion?</td></tr>
</tbody></table></div>
<div class="ao-ctabox"><h3>🌱 公司有外籍同事吃素？</h3><p>「素」味人生素食到會套餐附飲食標示，方便照顧 vegetarian 及有特別飲食需要的同事。</p><a class="btn" href="{LP}">了解素食到會</a><a class="btn" href="{C1}">揀選「素」味人生套餐</a></div>
'''
faqs=[
('Vegetarian 中文是什麼？','Vegetarian 的中文是素食者或素食的，一般指不吃肉類及海鮮、但可吃蛋奶的人。'),
('Vegan 中文是什麼？','Vegan 的中文是純素或全素，指不吃任何動物來源食品，包括蛋、奶及蜜糖。'),
('Veganism 中文是什麼？','Veganism 是純素主義，除飲食外，亦避免使用皮革、羊毛等動物製品。'),
('Vegetarian 和 Vegan 有什麼分別？','Vegetarian 一般可吃蛋奶，Vegan 則不吃任何動物來源食品，是最嚴格的素食。'),
('蛋奶素英文是什麼？','蛋奶素的英文是 lacto-ovo-vegetarian。'),
('Flexitarian 是什麼意思？','Flexitarian 即彈性素食者，以植物性飲食為主、間中吃肉。'),
('五辛素英文怎樣講？','五辛素並無統一英文名稱，可解釋為 Buddhist vegetarian without onion, garlic and other pungent vegetables。'),
]
srcs=[SRC['chp_en'],SRC['chp'],SRC['hku'],SRC['ao_set']]
open(HERE.parent/'b6-vegan-vegetarian-meaning.html','w',encoding='utf-8').write(page(PID,
 'Vegan、Vegetarian 中文是甚麼？素食英文用語一覽及分別',
 'Vegetarian 中文是素食者，Vegan 中文是純素／全素。一表看清蛋奶素、Flexitarian、Pescatarian 等素食英文用語，附點餐實用英文句子。',
 ['vegetarian 中文','vegan 中文','veganism 中文','素食英文'],'素食英文用語','Vegetarian、Vegan、Flexitarian 等中英對照，附點餐實用句子。',body,faqs,srcs,['B2','B4','B1']))
print('b6 ok')
