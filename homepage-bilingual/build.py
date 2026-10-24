# -*- coding: utf-8 -*-
# 首頁中英文版：由現有首頁 HTML（src-sections.json）生成 WPCode PHP snippet＋預覽
# 用法：python3 build.py
import json, re, html as H, os
HERE = os.path.dirname(os.path.abspath(__file__))
R = json.load(open(os.path.join(HERE, 'src-sections.json'), encoding='utf-8'))
SITE = 'https://aoaodelivery.com/'

# ───────── 1. 中文版修正（書面語、H1、錯字）
ZH_FIX = {
    '一般可安排送貨至港九新界多個地區，實際收費會按地點、時段及訂單內容而定。偏遠地區或指定時段或會有額外運費，運費會根據送貨地區及訂單總金額計算。我們設有免運費門檻：單一訂單滿 HK$700 可享部分區域運費減免，滿 HK$1,450 可享全港免運費（不派送地區除外）。詳細收費請參考 送貨需知。':
        '一般可安排送貨至港九新界多個地區，實際收費會按地點、時段及訂單內容而定。偏遠地區或指定時段或會有額外運費，運費會根據送貨地區及訂單總金額計算。我們設有免運費門檻：單一訂單滿 HK$700 可享部分區域運費減免，滿 HK$1,450 可享全港免運費（不派送地區除外）。詳細收費請參考<a href="https://aoaodelivery.com/delivery/">送貨需知</a>。',
    '點解客人揀 Kitchen AO': '為何選擇 Kitchen AO？',
    '由食材、出品到配送安排，我哋希望每一個重要場合都更安心、更體面。': '由食材、出品到配送安排，我們希望每一個重要場合都更安心、更體面。',
    '除咗餐飲選擇，亦可配搭部分派對用品與加配項目，安排更完整方便。': '除了餐飲選擇，亦可配搭部分派對用品與加配項目，安排更完整方便。',
    '以下整理咗客人最常查詢的訂購、送貨及餐單安排問題，方便你快速了解。': '以下整理了客人最常查詢的訂購、送貨及餐單安排問題，方便你快速了解。',
    '建議你盡早預訂，尤其係週末、節日或大型活動日子會較快額滿。實際截單時間可按餐單種類、訂單規模及送貨安排而定，建議直接 WhatsApp 查詢。':
        '建議你盡早預訂，尤其是週末、節日或大型活動日子會較快額滿。實際截單時間按餐單種類、訂單規模及送貨安排而定，建議直接 WhatsApp 查詢。',
    '可以。無論係生日派對、公司活動、商務午餐或船河聚會，都可以按人數、預算及用餐形式調整餐單內容，亦可配搭單點美食。':
        '可以。無論是生日派對、公司活動、商務午餐或船河聚會，都可以按人數、預算及用餐形式調整餐單內容，亦可配搭單點美食。',
}
MARQUEE_ZH = '舊會員優惠：系統會根據你上一張訂單的金額，自動為今次訂單減價。上一張訂單滿 $2,000，今次減 $100；滿 $4,000 減 $200，如此類推。優惠可與「買送」優惠同時使用，但不可合併訂單計算，亦不適用於客服人手輸入的訂單。'
MARQUEE_EN = 'Returning customer offer: we automatically discount this order based on your previous order. Previous order of $2,000 or more: $100 off; $4,000 or more: $200 off, and so on. Can be combined with "Buy & Get" offers, but orders cannot be merged and the offer does not apply to orders placed manually by our customer service team.'
H2_ZH = '香港到會推介：派對、公司及船河到會套餐'
H2_EN = 'Hong Kong Catering for Parties, Corporate Events and Boat Parties'

# ───────── 2. 英文翻譯（逐段，對應現有 HTML 的文字）
EN = {
    '派對到會・': 'Party Catering · ', '公司活動餐飲': 'Corporate Events', '一站式安排': 'All in One Place',
    'Kitchen AO 專注香港到會服務，適合生日派對、企業活動、家庭聚餐、船河聚會及品牌場合。由精緻擺盤、主打熱食到特色餐單，幫你把聚會做得更體面、更方便。':
        'Kitchen AO provides catering across Hong Kong for birthday parties, corporate events, family gatherings, boat parties and brand events. From elegant platters and signature hot dishes to themed menus, we make every gathering easier and more impressive.',
    '查看餐單': 'View Menu', 'WhatsApp 查詢': 'WhatsApp Us', '專人活動報價查詢': 'Get an Event Quote',
    '🎃 Halloween 萬聖節狂嘩套餐': '🎃 Halloween Party Sets', '10月23日–11月1日送貨': 'Delivery 23 Oct – 1 Nov',
    '適合生日派對': 'Birthday parties', '精緻擺盤到會': 'Elegant platters',
    '適合不同活動場合的到會服務': 'Catering for Every Occasion',
    '由派對聚會到公司活動，Kitchen AO 提供靈活而體面的餐飲安排。': 'From parties to corporate events, Kitchen AO offers flexible, well-presented catering.',
    '派對到會': 'Party Catering',
    '適合生日會、朋友聚會、家庭聚餐，套餐選擇靈活，方便分享。': 'Ideal for birthdays, friends’ gatherings and family meals, with flexible sets made for sharing.',
    '小型聚會到大型派對都可安排': 'From small gatherings to large parties',
    '適合會議茶點、開幕酒會、員工聚餐，出餐穩定，送達準時。': 'For meetings, opening receptions and staff meals, with consistent quality and punctual delivery.',
    '商務場合更體面，安排更省心': 'Polished for business, easy to arrange',
    '船河及商務午餐': 'Boat Parties & Business Lunches',
    '適合外出活動、船河聚會及商務午餐，保溫穩定，方便分發。': 'For outings, boat parties and business lunches, kept warm and easy to serve.',
    '方便攜帶，兼顧賣相與實用性': 'Easy to carry, good-looking and practical',
    '熱門到會套餐推薦': 'Popular Catering Sets',
    '精選適合派對、公司聚會及輕食場合的人氣餐單，方便你快速開始預訂。': 'Our most popular menus for parties, corporate gatherings and light refreshments, so you can start ordering quickly.',
    '派對到會套餐': 'Party Catering Sets',
    '適合生日會、朋友聚餐及節日慶祝，菜式豐富，方便多人分享。': 'For birthdays, get-togethers and festive celebrations, with a generous variety for sharing.',
    '適合家庭聚會及派對場合': 'Great for family gatherings and parties',
    '查看套餐': 'View Sets', '輕食宴會套餐': 'Refreshment Sets',
    '適合會議茶點、開幕活動及下午茶聚會，款式精緻，取用方便。': 'For meeting breaks, openings and afternoon tea, with refined bites that are easy to pick up.',
    '適合公司活動及商務場合': 'Great for corporate and business events',
    '單點美食精選': 'À La Carte Selection',
    '自由配搭小食、主菜、甜品及飲品，適合想靈活安排餐單的客人。': 'Mix and match snacks, mains, desserts and drinks to build the menu you need.',
    '方便加配或自組專屬餐單': 'Add extras or create your own menu',
    '查看美食': 'Browse Dishes',
    '黑白叉燒新產品限定優惠': 'New Black & White Char Siu: Limited Offer',
    '輸入優惠碼': 'Enter promo code', '，全單享 95 折。': ' for 5% off your whole order.',
    '用 WIN95 查詢優惠': 'Ask about WIN95',
    '為何選擇 Kitchen AO？': 'Why Choose Kitchen AO?',
    '由食材、出品到配送安排，我們希望每一個重要場合都更安心、更體面。': 'From ingredients and cooking to delivery, we want every important occasion to feel effortless and impressive.',
    '酒店級廚師團隊': 'Hotel-Trained Chefs',
    '由經驗廚師團隊主理，重視食材、味道與賣相，令每份到會餐點更有水準。': 'Our experienced chefs focus on ingredients, flavour and presentation, raising the standard of every dish.',
    '適合重視質素與形象的聚會場合': 'For occasions where quality and image matter',
    '靈活客製餐單': 'Flexible Custom Menus',
    '可選預設套餐，亦可按活動形式加入單點美食，自由組合更貼近實際需要。': 'Choose a ready-made set or add à la carte dishes to suit your event.',
    '更方便配合人數、預算與口味': 'Easy to match headcount, budget and taste',
    '專人準時送遞': 'Reliable, On-Time Delivery',
    '由團隊安排送餐流程，重視時間管理，務求按預定時段將餐點送達。': 'Our team plans every delivery carefully to arrive within your booked time slot.',
    '重要場合更安心，減少臨場壓力': 'Peace of mind on the big day',
    '一站式派對配套': 'One-Stop Party Add-ons',
    '除了餐飲選擇，亦可配搭部分派對用品與加配項目，安排更完整方便。': 'Beyond food, add party supplies and extras to complete your event in one order.',
    '適合想一次過處理活動細節的客人': 'For hosts who want everything sorted at once',
    '甚麼是到會服務？': 'What Is Catering Service?',
    '到會服務是按活動需要，將預先準備好的美食準時送到指定地點，適合派對、公司活動、會議及家庭聚會。':
        'Catering means freshly prepared food delivered on time to your venue, perfect for parties, corporate events, meetings and family gatherings.',
    '豐富餐單': 'Wide Menu Choice', '由小食、主菜到甜品，配搭更靈活。': 'From snacks and mains to desserts, mix and match freely.',
    '準時送達': 'On-Time Delivery', '按預訂時間送到活動場地，安排更安心。': 'Delivered to your venue at the time you booked.',
    '適合多種場合': 'For Every Occasion', '派對、商務午餐、會議茶點及節日聚會都適合。': 'Parties, business lunches, meeting breaks and festive gatherings.',
    '客戶真實評價': 'What Our Customers Say',
    '來自派對聚會、公司活動及商務餐飲客戶的真實回饋，讓你更放心安排重要場合。': 'Real feedback from party, corporate and business catering customers.',
    'Google 商戶評價': 'Google Reviews', '查看 Google 評論': 'Read Google Reviews',
    '生日派對客戶': 'Birthday party customer',
    '公司活動當日準時送達，包裝整齊，方便同事自取，整體感覺專業又省心，之後都會再回購。':
        'Delivered on time for our company event, neatly packed and easy for colleagues to help themselves. Professional and hassle-free. We will order again.',
    '黃先生': 'Mr Wong', '公司活動餐飲客戶': 'Corporate event customer',
    '餐單配搭夠彈性，我哋按人數再加配單點小食就已經好夠，朋友都話方便又好食，整體體驗幾滿意。':
        'The menu was flexible. We added a few à la carte snacks for our headcount and it was plenty. Our friends found it convenient and delicious.',
    '林小姐': 'Ms Lam', '聚會到會客戶': 'Party catering customer',
    '常見問題': 'Frequently Asked Questions',
    '以下整理了客人最常查詢的訂購、送貨及餐單安排問題，方便你快速了解。': 'Answers to the most common questions about ordering, delivery and menus.',
    '需要幾日前預訂到會服務？': 'How far in advance should I book?',
    '建議你盡早預訂，尤其是週末、節日或大型活動日子會較快額滿。實際截單時間按餐單種類、訂單規模及送貨安排而定，建議直接 WhatsApp 查詢。':
        'Please book as early as possible, especially for weekends, festivals and large events, which fill up quickly. Order cut-off times depend on the menu, order size and delivery arrangements. WhatsApp us for details.',
    '有沒有最低消費或最低訂購要求？': 'Is there a minimum order?',
    '不同套餐、單點類別及送貨安排可能設有不同要求。你可以先提供活動日期、人數及送貨地點，我們會按需要提供最合適的建議。':
        'Requirements vary by set, à la carte category and delivery arrangement. Tell us your event date, headcount and delivery address and we will recommend the best option.',
    '送貨覆蓋哪些地區？會收送貨費嗎？': 'Which areas do you deliver to? Is there a delivery fee?',
    '一般可安排送貨至港九新界多個地區，實際收費會按地點、時段及訂單內容而定。偏遠地區或指定時段或會有額外運費，運費會根據送貨地區及訂單總金額計算。我們設有免運費門檻：單一訂單滿 HK$700 可享部分區域運費減免，滿 HK$1,450 可享全港免運費（不派送地區除外）。詳細收費請參考':
        'We deliver to most areas across Hong Kong Island, Kowloon and the New Territories. Fees depend on location, time slot and order details; remote areas or specific time slots may cost extra. Orders over HK$700 enjoy reduced delivery fees in selected areas, and orders over HK$1,450 enjoy free delivery across Hong Kong (excluding non-delivery areas). See ',
    '送貨需知': 'Delivery Information', '。': '.',
    '可以按活動需要客製餐單嗎？': 'Can you customise the menu for my event?',
    '可以。無論是生日派對、公司活動、商務午餐或船河聚會，都可以按人數、預算及用餐形式調整餐單內容，亦可配搭單點美食。':
        'Yes. For birthday parties, corporate events, business lunches or boat parties, we can adjust the menu to your headcount, budget and dining style, and add à la carte dishes.',
    '會提供餐具、紙碟或派對用品嗎？': 'Do you provide cutlery, paper plates or party supplies?',
    '可按需要加配餐具、飲品及部分派對用品，方便你一站式安排整個活動。實際供應內容可按當時餐單及加購選項確認。':
        'Yes, you can add cutlery, drinks and selected party supplies to arrange everything in one place. Availability depends on the current menu and add-on options.',
    '聯絡我們': 'Contact Us',
}
EN_ATTR = {
    'Kitchen AO 到會服務與精緻食物擺設': 'Kitchen AO catering service with an elegant food display',
    'Kitchen AO x 101wine group 黑白叉燒新產品 banner': 'Kitchen AO x 101wine group new Black & White Char Siu banner',
    'Kitchen AO 廚師團隊主理到會好食': 'Kitchen AO chef team preparing catering dishes',
    'Kitchen AO 多元化香港到會美食服務': 'Kitchen AO catering menu variety in Hong Kong',
    'Kitchen AO 到會服務保溫技術': 'Kitchen AO catering delivery keeping food warm',
}
WA_EN = {'你好，我想查詢 Kitchen AO 到會餐單及報價': 'Hi, I would like to ask about Kitchen AO catering menus and a quote',
         '你好，我想查詢黑白叉燒新產品，同埋 WIN95 95折優惠': 'Hi, I would like to ask about the new Black & White Char Siu and the WIN95 offer'}

TAG = re.compile(r'(<script.*?</script>|<style.*?</style>|<[^>]+>)', re.S)

def tr_text(htm, table):
    """只替換標籤之間的文字（完全相符，前後空白保留）"""
    out = []
    for part in TAG.split(htm):
        if not part or part.startswith('<'):
            out.append(part); continue
        s = part.strip()
        if s in table:
            lead = part[:len(part) - len(part.lstrip())]; trail = part[len(part.rstrip()):]
            out.append(lead + table[s] + trail)
        else:
            out.append(part)
    return ''.join(out)

def tr_attrs(htm, table):
    for k, v in table.items():
        htm = htm.replace(f'alt="{k}"', f'alt="{H.escape(v)}"').replace(f'title="{k}"', f'title="{H.escape(v)}"')
    return htm

def en_links(htm):
    htm = re.sub(r'href="https://aoaodelivery\.com/(?!en/|wp-content/)', 'href="https://aoaodelivery.com/en/', htm)
    for k, v in WA_EN.items():
        htm = htm.replace(k, v)
    return htm

def missing_cjk(htm):
    txt = TAG.sub(' ', htm)
    return sorted(set(m.strip() for m in re.findall(r'[^<>]*[一-鿿][^<>]*', txt) if m.strip()))

# ───────── 3. 各區塊
def hero(lang):
    h = R[0]
    return h

def promo(lang):
    """會員優惠跑馬燈＋輪播圖（自建，取代插件及 WPBakery carousel）"""
    slides = re.findall(r'<div class="vc_item"><div class="vc_inner">(.*?)</div></div>', R[1], re.S)
    items = []
    for i, s in enumerate(slides):
        href = re.search(r'href="([^"]+)"', s).group(1)
        src = re.search(r'src="([^"]+)"', s).group(1)
        srcset = re.search(r'srcset="([^"]+)"', s)
        w, hgt = re.search(r'width="(\d+)" height="(\d+)"', s).groups()
        alt = ['Halloween 萬聖節狂嘩套餐', '派對到會套餐', '香港到會會員優惠', '香港到會會員優惠', '香港到會會員優惠'][i]
        alt_en = ['Halloween party catering sets', 'Party catering sets', 'Returning customer offer', 'Returning customer offer', 'Returning customer offer'][i]
        if lang == 'en':
            href = re.sub(r'^https://aoaodelivery\.com/', SITE + 'en/', href); alt = alt_en
        load = 'eager" fetchpriority="high' if i == 0 else 'lazy'
        items.append(f'<a class="ao-sl-item" href="{href}"><img src="{src}"' + (f' srcset="{srcset.group(1)}" sizes="(max-width:1200px) 100vw, 1200px"' if srcset else '')
                     + f' width="{w}" height="{hgt}" alt="{H.escape(alt)}" loading="{load}" decoding="async"></a>')
    dots = ''.join(f'<button type="button" class="ao-sl-dot" aria-label="{"Slide" if lang=="en" else "第"} {i+1}{"" if lang=="en" else " 張"}"></button>' for i in range(len(items)))
    mq = MARQUEE_EN if lang == 'en' else MARQUEE_ZH
    return (f'<section class="ao-promo"><div class="ao-mq" aria-label="{"Offer" if lang=="en" else "會員優惠"}"><div class="ao-mq-track"><span>{H.escape(mq)}</span><span aria-hidden="true">{H.escape(mq)}</span></div></div>'
            f'<div class="ao-sl"><div class="ao-sl-track">{"".join(items)}</div><div class="ao-sl-dots">{dots}</div></div></section>')

def services(lang):
    h = R[2]
    h = re.sub(r'<h1 style="text-align: center;">\s*</h1>', '', h)
    h = re.sub(r'<h1 class="h1title"([^>]*)>.*?</h1>', lambda m: f'<h2 class="h1title"{m.group(1)}>{H2_EN if lang=="en" else H2_ZH}</h2>', h, flags=re.S)
    return h

def form(lang):
    return '__FORM__'

def simple(i):
    return R[i]

def build(lang):
    parts = [hero(lang), promo(lang), services(lang), form(lang), simple(4), simple(5), simple(6), simple(7)]
    h = '\n'.join(parts)
    h = tr_text(h, ZH_FIX)
    if lang == 'en':
        h = tr_text(h, EN); h = tr_attrs(h, EN_ATTR); h = en_links(h)
    return h

CSS = '''
/* 首頁：WPBakery 自訂樣式（原本由頁面輸出） */
.vc_custom_1776576454166{padding-top:0!important;padding-bottom:0!important}
.vc_custom_1775899549282{padding-top:80px!important;padding-bottom:80px!important;background-color:#F8F6F2!important}
.vc_custom_1775901384920{padding-top:60px!important;padding-bottom:60px!important;background-color:#F8F6F2!important}
.vc_custom_1775902198440{background-color:#F8F6F2!important}
.ao-home h2.h1title{font-size:24px;line-height:1.4;margin:0 0 10px}
/* 會員優惠跑馬燈 */
.ao-promo{background:#fff;padding:20px 0 0}
.ao-mq{overflow:hidden;white-space:nowrap;color:#2448b8;font-size:15px;line-height:1.8;padding:6px 0}
.ao-mq-track{display:inline-flex;gap:100px;animation:aoMq 40s linear infinite}
.ao-mq:hover .ao-mq-track{animation-play-state:paused}
@keyframes aoMq{from{transform:translateX(0)}to{transform:translateX(calc(-50% - 50px))}}
/* 輪播圖 */
.ao-sl{position:relative;max-width:1240px;margin:10px auto 0}
.ao-sl-track{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;scrollbar-width:none;scroll-behavior:smooth}
.ao-sl-track::-webkit-scrollbar{display:none}
.ao-sl-item{flex:0 0 100%;scroll-snap-align:center}
.ao-sl-item img{display:block;width:100%;height:auto}
.ao-sl-dots{display:flex;justify-content:center;gap:6px;padding:10px 0}
.ao-sl-dot{width:10px;height:10px;padding:0;border:1px solid #333;border-radius:0;background:#333;cursor:pointer}
.ao-sl-dot.on{background:#fff}
@media (prefers-reduced-motion:reduce){.ao-mq-track{animation:none}}
'''
JS = '''(function(){document.querySelectorAll('.ao-sl').forEach(function(s){var t=s.querySelector('.ao-sl-track'),d=s.querySelectorAll('.ao-sl-dot'),n=d.length,i=0,tm;
function go(k){i=(k+n)%n;t.scrollTo({left:t.clientWidth*i});d.forEach(function(x,j){x.classList.toggle('on',j===i)});}
function auto(){clearInterval(tm);tm=setInterval(function(){go(i+1)},8000);}
d.forEach(function(x,j){x.addEventListener('click',function(){go(j);auto();})});
t.addEventListener('scroll',function(){var k=Math.round(t.scrollLeft/t.clientWidth);if(k!==i){i=k;d.forEach(function(x,j){x.classList.toggle('on',j===i)});}},{passive:true});
go(0);auto();});})();'''

def faq_schema(lang):
    qs = re.findall(r'<(?:summary|h3|strong|b|div)[^>]*>\s*([^<]*？)\s*</', R[7])
    return qs

zh = build('zh'); en = build('en')
left = missing_cjk(en.replace('__FORM__', ''))
print('未翻譯的中文（英文版）：', left)

def php_block(htm):
    a, b = htm.split('__FORM__')
    return a, b

za, zb = php_block(zh); ea, eb = php_block(en)
NOW = lambda s, tag: f"<<<'{tag}'\n{s}\n{tag}"
php = f'''// Kitchen AO 首頁（中英文版）｜由 homepage-bilingual/build.py 生成，請勿直接修改
// WPCode：PHP Snippet，Insert Method 選 Auto Insert › Run Everywhere；首頁用 [ao_home] 放入
add_shortcode( 'ao_home', function () {{
    global $TRP_LANGUAGE;
    $en  = ! empty( $TRP_LANGUAGE ) && strpos( $TRP_LANGUAGE, 'en' ) === 0;
    $css = {NOW(CSS, 'AOCSS')};
    $js  = {NOW(JS, 'AOJS')};
    $form = do_shortcode( '[fluentform id="4"]' );
    if ( $en ) {{
        $a = {NOW(ea, 'AOENA')};
        $b = {NOW(eb, 'AOENB')};
        $wrap = '<div class="ao-home" lang="en" data-no-translation>';
    }} else {{
        $a = {NOW(za, 'AOZHA')};
        $b = {NOW(zb, 'AOZHB')};
        $wrap = '<div class="ao-home">';
    }}
    return '<style>' . $css . '</style>' . $wrap . $a . $form . $b . '</div><script>' . $js . '</script>';
}} );
'''
open(os.path.join(HERE, 'ao-home-snippet.php'), 'w', encoding='utf-8').write(php)
open(os.path.join(HERE, 'ao-home-snippet.txt'), 'w', encoding='utf-8').write(php)

FORM_PREVIEW = '<div style="max-width:720px;margin:30px auto;padding:30px;border:2px dashed #c9b37a;border-radius:12px;text-align:center;color:#7a6a45;font:15px -apple-system,sans-serif">（電子報表格：正式網站會由 Fluent Forms 表格 #4 顯示）</div>'
for lang, htm in (('zh', zh), ('en', en)):
    doc = f'''<!doctype html><html lang="{'en' if lang=='en' else 'zh-HK'}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>首頁預覽（{lang}）</title>
<style>body{{margin:0;font-family:-apple-system,BlinkMacSystemFont,"PingFang HK","Microsoft JhengHei",sans-serif}}.vc_row{{margin:0;display:flex;flex-wrap:wrap}}.vc_column_container{{box-sizing:border-box}}.vc_column-inner{{padding:0 15px}}.vc_row-flex{{display:flex;flex-wrap:wrap}}.vc_col-sm-12{{width:100%}}.vc_col-sm-4{{width:33.33%}}.vc_col-sm-6{{width:50%}}@media(max-width:767px){{.vc_col-sm-4,.vc_col-sm-6{{width:100%}}}}img{{max-width:100%;height:auto}}{CSS}</style></head><body>
<div class="ao-home">{htm.replace('__FORM__', FORM_PREVIEW)}</div><script>{JS}</script></body></html>'''
    open(os.path.join(HERE, f'preview-{lang}.html'), 'w', encoding='utf-8').write(doc)
print('ok', len(php))
