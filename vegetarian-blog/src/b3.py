# -*- coding: utf-8 -*-
# B3 第二稿：初一十五食齋懶人包（自動日子表＋中國日曆 KV＋B6 版面）
from common import *
import datetime as dt, re, kv_b3, b3_lunar, tbl_poster
PID = 'B3'
BLOGS['B6'] = ('Vegan、Vegetarian 中文是甚麼？Flexitarian、Pescatarian 有何分別？港台歐美素食用詞一次看清', BLOGS['B6'][1])
TODAY = dt.date.today()

B2L = link('B2', '《素食分類天書》')
B6L = link('B6', '《Vegan、Vegetarian 中文是甚麼？》')
YES, NO, MID = '<td class="c y">✓</td>', '<td class="c n">✗</td>', '<td class="c m">△</td>'
LEG = '<p class="ao-tcap" style="margin:10px 0 4px!important">✓＝可以吃，✗＝不吃，△＝視乎個人、宗教團體。</p>\n'

body = f'''
<p class="ao-intro">不少香港人習慣在每月農曆初一、十五食齋，亦有人在觀音誕、佛誕或農曆新年年初一茹素。{k('初一十五食齋')}有甚麼原因？可以吃蛋、喝牛奶嗎？有哪些{k('食齋禁忌')}？本文按香港天文台的公曆與農曆對照表，自動列出由今日起計 12 個月的{k('初一十五')}及食齋節日，並一次解答「{k('雞蛋是素食嗎')}」等常見疑問。</p>
<div class="ao-qa"><p class="t">下一個初一十五</p><p id="b3-next">{b3_lunar.next_text(TODAY)}</p></div>
<div class="ao-qa"><p class="t">快速答案</p><p>初一十五食齋是指在每月農曆初一及十五兩日不吃肉類及海鮮的習俗。可否吃蛋、喝牛奶，視乎個人或所屬宗教團體的要求：蛋奶素可以吃蛋及奶；傳統佛教齋戒一般不吃蛋及五辛；全素則不吃任何動物來源食品。</p></div>
<nav class="ao-toc"><div class="t">目錄</div><ul>
<li><a href="#tables">初一十五食齋列表速查</a></li>
<li><a href="#what">初一十五食齋是甚麼？</a></li>
<li><a href="#dates">未來 12 個月初一十五日子表</a></li>
<li><a href="#egg">初一十五食齋可以吃蛋、喝牛奶嗎？</a></li>
<li><a href="#taboo">食齋禁忌一覽</a></li>
<li><a href="#eat">初一十五食齋吃甚麼？</a></li>
<li><a href="#faq">常見問題</a></li></ul></nav>
<style>.ao-article .ao-toc ul li,.ao-article .ao-toc ul li a{{font-size:15.5px!important;line-height:1.7!important}}@media(max-width:640px){{.ao-article .ao-toc ul li,.ao-article .ao-toc ul li a{{font-size:14.5px!important}}}}.ao-article .b3-past{{display:inline-block;font-size:12px;font-weight:700;color:#8a7f70;background:#EDE6DA;border-radius:10px;padding:0 8px;margin-left:4px;line-height:20px}}.ao-article .b3-nx{{display:inline-block;font-size:12px;font-weight:800;color:#fff;background:#B5382B;border-radius:10px;padding:0 8px;margin-left:4px;line-height:20px}}.ao-article td.b3-p{{color:#A39886!important}}.ao-article .b3-y{{font-size:12.5px;color:#8a7f70;font-weight:600}}</style>
<!--TBL_INDEX-->

<h2 class="ao-h2" id="what">初一十五食齋是甚麼？</h2>
<p>農曆每月初一稱為「朔日」，即月亮最暗的一日；十五稱為「望日」，即月圓之日。傳統上這兩日是拜神上香的日子，受佛教、道教及民間信仰影響，不少人會在當日{k('初一十五吃素')}，以示虔誠。食齋的嚴格程度因人而異：有人只戒肉類及海鮮，有人連蛋、奶及五辛也一併戒口。各種吃素方式的分別，可參考{B2L}。</p>
<h3 class="ao-h3">為何初一十五要食齋？</h3>
<ul class="ao-ck">
<li><b>拜神祈福：</b>初一十五上香拜神，食齋被視為潔淨身心、表達誠意的方式。</li>
<li><b>佛教「齋日」：</b>佛教有「十齋日」的說法，即每月初一、初八、十四、十五、十八、廿三、廿四、廿八、廿九及三十，初一及十五亦在其中。</li>
<li><b>許願還願：</b>部分人會為家人健康、考試或工作許願，承諾在初一十五食齋。</li>
<li><b>健康及習慣：</b>亦有人純粹借此每月減少吃肉兩日，作為飲食調整。</li>
</ul>
<h3 class="ao-h3">初一十五食齋由甚麼時候開始？</h3>
<p>一般做法是由當日早上起床開始，至晚上就寢為止，即整個公曆日子都食齋。亦有人按傳統時辰，由前一晚子時（晚上 11 時）起計。兩種做法都常見，按家中習慣或所屬宗教團體的要求即可。</p>

<h2 class="ao-h2" id="dates">未來 12 個月初一十五日子表</h2>
<p>下表按香港天文台〈公曆與農曆日期對照表〉整理，頁面會按你瀏覽當日的日期，自動顯示由本月起計 12 個月的{k('初一十五食齋')}日子，方便預早安排家庭聚餐。</p>
<p class="t ao-tbt">列表1｜未來 12 個月初一十五日子｜自動更新</p>
<div class="ao-tw"><table class="ao-tbl ao-tblc" id="b3-dates"><thead><tr><th style="width:34%">農曆月份</th><th>初一</th><th>十五</th></tr></thead><tbody>{b3_lunar.static_rows(TODAY)}</tbody></table></div>
<p class="ao-tcap">計算方法：按天文台資料取得每個農曆月初一的公曆日期，十五＝初一＋14 日。</p>
<h3 class="ao-h3">其他食齋節日：觀音誕、佛誕、盂蘭節</h3>
<p>除了初一十五，不少家庭亦會在以下節日食齋。觀音誕每年有三次，分別是農曆二月十九、六月十九及九月十九；盂蘭節部分家庭在七月十四拜祭，下表以七月十五列出。</p>
<p class="t ao-tbt">列表2｜未來 12 個月食齋節日｜自動更新</p>
<div class="ao-tw"><table class="ao-tbl ao-tblc" id="b3-fest"><thead><tr><th style="width:34%">節日</th><th>農曆</th><th>公曆日期</th></tr></thead><tbody>{b3_lunar.static_fest(TODAY)}</tbody></table></div>
<div class="ao-tip">💡 節日家庭聚會人數較多，若想一家人一齊食齋又不想下廚，可考慮{link('B1','素食到會')}，並預先查詢菜式是否含蛋及五辛。</div>

<h2 class="ao-h2" id="egg">初一十五食齋可以吃蛋、喝牛奶嗎？</h2>
<div class="ao-qa"><p class="t">快速答案</p><p>{k('初一十五吃素可以吃蛋嗎')}並無劃一答案：蛋奶素可以吃蛋及奶；傳統佛教齋戒一般不吃蛋，對奶類則較寬鬆；全素不吃蛋及奶。最穩妥是按個人信仰或所屬宗教團體的要求而定。</p></div>
<p>衞生署衞生防護中心把素食分為蛋奶素、蛋素、奶素及全素，其中蛋奶素及蛋素都包括蛋類。因此，「{k('食齋可以食雞蛋嗎')}」的答案，取決於你選擇哪一種吃法。若是為家中長輩預備齋菜，最好先問清楚對方的習慣。</p>
<h3 class="ao-h3">不同吃素方式：可否吃蛋、奶、五辛？</h3>
<p>五辛是指蔥、蒜、韭、蕎頭及興渠。以下按常見的吃素方式比較，完整的素食分類可參考{B2L}；五辛在香港、台灣及歐美的不同定義，可參考{B6L}。</p>
{LEG}<p class="t ao-tbt">列表3｜不同吃素方式：蛋、奶、五辛比較｜比較表</p>
<div class="ao-tw"><table class="ao-tbl ao-tblc"><thead><tr><th style="width:40%">吃素方式</th><th class="c">蛋</th><th class="c">奶</th><th class="c">五辛</th></tr></thead><tbody>
<tr><td><b>蛋奶素</b></td>{YES}{YES}{MID}</tr>
<tr><td><b>蛋素</b></td>{YES}{NO}{MID}</tr>
<tr><td><b>奶素</b></td>{NO}{YES}{MID}</tr>
<tr><td><b>五辛素</b>（可吃五辛，不吃蛋奶）</td>{NO}{NO}{YES}</tr>
<tr><td><b>全素／純素</b></td>{NO}{NO}{MID}</tr>
<tr><td><b>傳統佛教齋戒</b></td>{NO}{MID}{NO}</tr>
<tr><td><b>鍋邊素／方便素</b></td>{MID}{MID}{MID}</tr>
</tbody></table></div>
<h3 class="ao-h3">初一十五吃素可以喝牛奶嗎？</h3>
<p>蛋奶素及奶素可以喝牛奶；全素不喝。傳統佛教齋戒對奶類的要求較寬鬆，不少人會飲用，但亦有寺院及家庭一併戒口。如屬發願吃素，應按當初許下的承諾決定。</p>
<h3 class="ao-h3">雞蛋、鹹蛋、蛋撻是素食嗎？</h3>
<p>「{k('蛋是素食嗎')}」「{k('素食可以吃蛋嗎')}」是十分常見的疑問。蛋類不屬肉類，蛋奶素及蛋素人士可以吃；全素人士則不吃。以下是常見蛋類食物的分類：</p>
{LEG}<p class="t ao-tbt">列表4｜常見蛋類食物是否素食｜6 款食物</p>
<div class="ao-tw"><table class="ao-tbl ao-tblc"><thead><tr><th style="width:26%">食物</th><th class="c" style="width:17%">蛋奶素／蛋素</th><th class="c" style="width:13%">全素</th><th>備註</th></tr></thead><tbody>
<tr><td><b>雞蛋、鴨蛋、鵪鶉蛋</b></td>{YES}{NO}<td>屬蛋類</td></tr>
<tr><td><b>鹹蛋、鹹蛋黃</b></td>{YES}{NO}<td>以鴨蛋醃製</td></tr>
<tr><td><b>皮蛋</b></td>{YES}{NO}<td>以鴨蛋製成</td></tr>
<tr><td><b>茶葉蛋</b></td>{MID}{NO}<td>部分滷汁以肉類或蔥蒜調味</td></tr>
<tr><td><b>蛋撻、葡撻</b></td>{MID}{NO}<td>含蛋及奶；部分酥皮以豬油製作，購買前宜向店方查詢</td></tr>
<tr><td><b>蛋糕、雞蛋仔</b></td>{MID}{NO}<td>含蛋；留意是否加入豬油或肉鬆等配料</td></tr>
</tbody></table></div>
<h3 class="ao-h3">素食者可以用甚麼代替雞蛋？</h3>
<p>煮餸時可用滑豆腐代替炒蛋；烘焙時可用香蕉蓉或亞麻籽加水代替蛋液，全素朋友亦可食用。</p>

<h2 class="ao-h2" id="taboo">食齋禁忌一覽</h2>
<p>除了肉類及海鮮，不少日常調味料及食物都含動物成分。以下整理常見的{k('食齋禁忌')}，按類別列出可以吃及要避免的食物：</p>
<p class="t ao-tbt">列表5｜食齋可以吃及要避免的食物｜5 個類別</p>
<div class="ao-tw"><table class="ao-tbl ao-tblc"><thead><tr><th style="width:22%">類別</th><th>可以吃</th><th>要避免</th></tr></thead><tbody>
<tr><td><b>湯底及調味</b></td><td>素上湯、昆布湯、豉油、素蠔油</td><td>肉湯、上湯、蠔油、魚露、蝦醬、雞粉</td></tr>
<tr><td><b>蛋白質</b></td><td>豆腐、腐竹、麵筋、豆類</td><td>肉類、海鮮；蛋及奶視乎吃法</td></tr>
<tr><td><b>蔬菜</b></td><td>各類蔬菜及菇菌</td><td>嚴守佛教齋戒者避免五辛（蔥、蒜、韭、蕎頭、興渠）</td></tr>
<tr><td><b>飲品</b></td><td>茶、豆漿、果汁</td><td>酒（佛教戒律有戒酒的要求）</td></tr>
<tr><td><b>零食甜品</b></td><td>水果、果仁、豆沙</td><td>含明膠（魚膠粉）的啫喱及軟糖；以豬油製作的酥皮</td></tr>
</tbody></table></div>
<h3 class="ao-h3">不小心破戒怎麼辦？</h3>
<p>{k('初一十五吃素破戒')}的處理方法因人而異。不少人會在下一個齋日補回，或誠心懺悔後繼續；如屬發願吃素，可按所屬宗教團體的建議處理。食齋重在心意，不必過分自責。</p>

<h2 class="ao-h2" id="eat">初一十五食齋吃甚麼？</h2>
<p>常見的{k('食齋食物')}以豆腐、菇菌及時令蔬菜為主。以下菜式在家中容易預備，亦方便按需要走蛋或走五辛：</p>
<p class="t ao-tbt">列表6｜常見齋菜及走蛋、走五辛提示｜5 款齋菜</p>
<div class="ao-tw"><table class="ao-tbl ao-tblc"><thead><tr><th style="width:24%">菜式</th><th style="width:34%">主要材料</th><th>提示</th></tr></thead><tbody>
<tr><td><b>羅漢齋</b></td><td>冬菇、腐竹、雲耳、粉絲、白果</td><td>部分做法以蠔油調味，可改用素蠔油</td></tr>
<tr><td><b>冬菇炆豆腐</b></td><td>冬菇、豆腐</td><td>不含蛋；留意是否以蠔油調味</td></tr>
<tr><td><b>腐竹炆粉絲</b></td><td>腐竹、粉絲、紅蘿蔔</td><td>不含蛋，適合全素</td></tr>
<tr><td><b>素炒雜菜</b></td><td>西蘭花、甘筍、荷蘭豆</td><td>常以蒜蓉起鑊，需要時可走蒜</td></tr>
<tr><td><b>素鵝</b></td><td>腐皮、冬菇</td><td>不含蛋；醬汁宜用素蠔油</td></tr>
</tbody></table></div>
<p>若擔心營養不足，可參考衞生防護中心的建議，多吃豆類、大豆製品及深綠色蔬菜。</p>
'''

body = tbl_poster.apply(body, '{n} 個初一十五食齋列表速查')
body = '<style>#lafka_page_title h1.heading-title{text-transform:none!important}</style>\n' + body

# CTA：沿用 B2 的 CTA 版面
cta = [l for l in (HERE / 'b2.py').read_text(encoding='utf-8').split('\n') if l.startswith('<div class="ao-ctabox">')][0]
cta = cta.replace('🌱 一次照顧所有素食朋友', '🙏 節日一家人食齋，交給素食到會').replace('{C1}', C1)
cta = re.sub(r'<p>「素」味人生素食到會套餐[^<]*</p>',
             '<p>「素」味人生素食到會套餐設有「鮮百合炒秋葵雲耳蓮藕片配燴冬瓜」、「香橙甘筍南瓜蓉配西蘭花配橄欖油浸燈籠椒」等以蔬菜為主的菜式，6 至 26 人均有選擇；如需走蛋、走五辛，請於落單前向客服確認。最少提早三日預訂。</p>', cta, 1)
body += cta + '\n' + b3_lunar.js() + '\n'

faqs = [
 ('初一十五食齋可以吃甚麼？', '可以吃豆腐、腐竹、麵筋、菇菌、各類蔬菜、穀物及水果，例如羅漢齋、冬菇炆豆腐及素炒雜菜。蛋、奶及五辛是否可吃，視乎個人或宗教團體的要求。'),
 ('初一十五食齋可以吃蛋嗎？', '視乎吃法：蛋奶素及蛋素可以吃蛋；傳統佛教齋戒或全素一般不吃蛋。'),
 ('初一十五吃素可以喝牛奶嗎？', '蛋奶素及奶素可以喝牛奶；全素不喝。傳統佛教齋戒對奶類較寬鬆，但亦有人一併戒口。'),
 ('雞蛋屬於素食嗎？', '蛋類不屬肉類，蛋奶素及蛋素人士可以吃；全素人士不吃。'),
 ('鹹蛋是素食嗎？', '鹹蛋以鴨蛋醃製，屬蛋類，適合蛋奶素及蛋素人士，全素人士不吃。'),
 ('蛋撻是素食嗎？', '蛋撻含蛋及奶，只適合蛋奶素人士；部分酥皮以豬油製作，購買前宜向店方查詢。'),
 ('五辛素可以吃蛋、奶嗎？', '五辛素是指可以吃五辛（蔥、蒜、韭、蕎頭、興渠）的素食，按台灣的「植物五辛素」定義，不吃蛋及奶。'),
 ('蛋奶素可以吃洋蔥嗎？', '可以。蛋奶素的定義只涉及蛋及奶，是否吃洋蔥、蔥蒜等五辛，視乎個人或宗教團體的要求。'),
 ('鍋邊素可以吃蛋嗎？', '鍋邊素是指只吃菜、但接受與肉同煮的吃法，可否吃蛋並無統一標準，按個人習慣而定。'),
 ('發願吃素可以吃蛋嗎？', '應按當初許下的承諾決定。如發願時承諾全素，便不吃蛋；如只承諾不吃肉，則可按蛋奶素的方式。'),
 ('初一十五食齋由甚麼時候開始？', '一般由當日早上起床至晚上就寢為止；亦有人按傳統時辰，由前一晚子時（晚上 11 時）起計。'),
 ('初一十五食齋可以飲酒嗎？', '佛教戒律有戒酒的要求，不少人在食齋日亦會避免飲酒，可按個人信仰決定。'),
 ('觀音誕是哪幾日？', '每年農曆二月十九、六月十九及九月十九。2027 年分別是 3 月 26 日、7 月 22 日及 10 月 18 日。'),
 ('素食者可以用甚麼代替雞蛋？', '煮餸可用滑豆腐，烘焙可用香蕉蓉或亞麻籽加水代替蛋液。'),
]
HKO = lambda y, z: ('政府', f'香港天文台〈{y}（{z}）年公曆與農曆日期對照表〉', f'https://www.hko.gov.hk/tc/gts/time/calendar/text/files/T{y}c.txt')
srcs = [SRC['hko26'], SRC['hko27'], HKO(2028, '戊申 - 肖猴'), HKO(2029, '己酉 - 肖雞'), HKO(2030, '庚戌 - 肖狗'), SRC['hol27'], SRC['chp'], SRC['ao_set']]

META_T = '初一十五食齋懶人包｜食齋原因、禁忌及未來 12 個月日子表'
META_D = '初一十五食齋可以吃蛋、喝牛奶嗎？雞蛋、鹹蛋、蛋撻是素食嗎？按天文台資料自動列出未來 12 個月初一十五及觀音誕、佛誕日子，附食齋禁忌及齋菜建議。'
open(HERE.parent / 'b3-chu-yat-sap-ng-guide.html', 'w', encoding='utf-8').write(page(PID, META_T, META_D,
     ['初一十五食齋', '食齋禁忌', '雞蛋是素食嗎'], '', '', body, faqs, srcs, ['B2', 'B6', 'B1'], kv_html=kv_b3.block('h1')))
open(HERE.parent / 'b3-chu-yat-sap-ng-guide-WORDPRESS.html', 'w', encoding='utf-8').write(
     wp_page(PID, body, faqs, srcs, [], kv_b3.block('div')))
print('b3 ok')
