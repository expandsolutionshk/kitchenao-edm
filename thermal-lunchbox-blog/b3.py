# -*- coding: utf-8 -*-
"""Blog 3｜飲品保溫杯、保溫瓶、保溫壺篇：象印、虎牌、膳魔師三大品牌比較
價錢及規格於 2026-10-28 在各品牌香港官方網店產品頁記錄，以網店實時價錢為準。
"""
import html
E = html.escape

B3_NAME = 'Blog 3｜飲品保溫杯、保溫瓶、保溫壺篇'
PRICE_DATE_B3 = '2026 年 10 月 28 日'

# 類型：A 保溫杯（480–500ml）、B 大容量保溫瓶／保溫壺（1L 以上）、C 兒童保溫水壺
# (type, brand, name, sku, size, spec, price, shop, url, img, scores[保熱, 保冷, 便攜], scene, desc)
B3_PRODUCTS = [
 ('A', '象印 Zojirushi', '象印0.48L 不銹鋼保溫杯(一體式中栓)【香港行貨】', 'SM-WS48', '480ml',
  '6 小時：熱 71°C 以上／冷 8°C 以下；0.21kg；一按彈蓋，一體式中栓', '$199（原價 $249）', '生活館 Life Gallery（象印香港代理網店）',
  'https://eshop.lifekan.com/products/zojirushi-048l-stainless-steel-vacuum-bottle-one-piece-stopper%E3%80%90hk-licensed%E3%80%91-sm-ws48',
  'https://img.shoplineapp.com/media/image_clips/66029bb155a04200119c1fad/original.jpg', [5, 5, 5],
  '上班族、通勤，想熱飲保持較高溫度', '三款 480ml 至 500ml 保溫杯之中，官方 6 小時保熱數字最高。一體式中栓減少零件，清洗較方便，但官方提示不可浸泡。'),
 ('A', '虎牌 Tiger', '夢重力超輕彈蓋式不銹鋼真空保溫杯 MMJ-S036/S048/S060', 'MMJ-S048', '480ml',
  '6 小時：熱 67°C 以上／冷 8°C 以下；0.19kg；可放入洗碗碟機', '$198（原價 $308）', 'TIGER 虎牌香港官方網店',
  'https://www.tigerhkeshop.com/products/ultra-light-one-push-lid-stainless-steel-thermal-bottle-mmj-s036s048s060',
  'https://img.shoplineapp.com/media/image_clips/66fa2e82076cbd000b6ef912/original.png', [4, 5, 5],
  '重視輕巧及清洗方便的用家', '三款之中最輕（0.19kg），而且官方註明可放入洗碗碟機。另有 360ml 及 600ml 容量可選。'),
 ('A', '膳魔師 Thermos', '500毫升真空保溫瓶 - 深藍', 'JNL-502SS-NVY', '500ml',
  '6 小時：熱 68°C 以上／冷 10°C 以下；210g；口徑 4cm；可放入洗碗碟機', '$368', 'THERMOS 香港官方網店',
  'https://www.thermos.com.hk/product/949d0ff3-9764-40ce-8627-d7ee947a93cc',
  'https://assets.omniwe.com/generated/06d60170d0dbc001dbed68d744b1caf022125033.png', [4, 4, 5],
  '想放入洗碗碟機、需要稍大容量', '容量 500ml，飲用口可拆出清洗，並可放入洗碗碟機。官網以原價發售，價錢比另外兩款高。'),
 ('B', '象印 Zojirushi', '象印 1L 不銹鋼真空瓶【香港行貨】', 'SJ-JS10', '1.0L',
  '杯蓋連一按式內塞；口徑約 4cm，可放冰粒；杯蓋 Ag+ 抗菌處理', '$269（原價 $299）', '生活館 Life Gallery（象印香港代理網店）',
  'https://eshop.lifekan.com/products/zojirushi-1l-portable-pot--ss%E3%80%90hk-licensed%E3%80%91-sj-js10',
  'https://img.shoplineapp.com/media/image_clips/63ef25d25d1bed001af354c0/original.jpg', [None, None, 4],
  '行山、郊遊，多人分享熱飲', '杯蓋可直接當杯使用，適合戶外分享。網店文字未列 6 小時保溫數字，選購前可向店舖查詢。豐澤亦以同價 $269 發售。'),
 ('B', '虎牌 Tiger', '不銹鋼保溫壺 MHK-A', 'MHK-A120', '1.2L',
  '6 小時：熱 78°C 以上；24 小時：熱 55°C 以上；不適用於保冷；0.95kg', '$328（原價 $378）', 'TIGER 虎牌香港官方網店',
  'https://www.tigerhkeshop.com/products/stainless-steel-thermal-bottle-mhk-a-7',
  'https://img.shoplineapp.com/media/image_clips/60890196590eeb001da604de/original.jpg', [5, None, 2],
  '辦公室或家中長時間保熱水、茶', '24 小時後仍保持 55°C 以上，適合放在枱面長時間保熱。重量 0.95kg，較適合放在家中或辦公室，不適合長時間手提。另有 1.49L 至 2L 容量。'),
 ('B', '膳魔師 Thermos', '1000毫升真空保溫瓶 - 深灰', 'JOS-1000-DGY', '1000ml',
  '6 小時：熱 75°C 以上／冷 9°C 以下；口徑 4cm；附手挽', '$428', 'THERMOS 香港官方網店',
  'https://www.thermos.com.hk/product/4186b221-d7cc-49ff-aa3f-ad07e7986dee',
  'https://assets.omniwe.com/generated/b418c0303b7d0efbdd6c94452ee6755dfbb1ed06.png', [5, 5, None],
  '運動、行山，熱飲凍飲兩用', '三款大容量之中，唯一同時列出保熱及保冷數字，冷熱兩用。官網重量標示為「400kg」，相信是 400g 的筆誤，所以便攜度未有評分。'),
 ('C', '象印 Zojirushi', '象印 0.5L不銹鋼兒童壺 (吸管型)【香港行貨】', 'SD-CAE50', '500ml',
  '吸管型一按彈蓋；上蓋可拆洗；附孭帶及名牌；粉紅色、藍色', '$279（原價 $378）', '生活館 Life Gallery（象印香港代理網店）',
  'https://eshop.lifekan.com/products/zojirushi-05l-ss-portable-pot-straw%E3%80%90hk-licensed%E3%80%91-sd-cae50',
  'https://img.shoplineapp.com/media/image_clips/68d4c2f0df54080018b6a946/original.jpg', [None, None, None],
  '幼稚園及小學生上學', '吸管型設計，附孭帶及名牌，方便小朋友自己使用。網店文字未列保溫數字及重量，選購前可向店舖查詢。'),
 ('C', '虎牌 Tiger', '兒童兩用不銹鋼真空保溫杯 MBR-G06G', 'MBR-G06G', '640ml（杯蓋）／600ml（吸管蓋）',
  '附吸管蓋及杯蓋；6 小時：熱 73°C 以上（杯蓋）／冷 8°C 以下；0.39kg', '$398', 'TIGER 虎牌香港官方網店',
  'https://www.tigerhkeshop.com/products/kids-two-way-stainless-steel-thermal-bottle-mbr-g06g',
  'https://img.shoplineapp.com/media/image_clips/6a19053ed15c07ce86c884ec/original.png', [5, 5, 4],
  '小學生，冬天熱飲、夏天凍飲', '一個水壺兩種蓋：小朋友用吸管蓋，長大後可轉杯蓋。用吸管蓋時官方提示不要裝 40°C 以上的飲品。'),
 ('C', '膳魔師 Thermos', 'OHIGE no PON 400毫升吸管保溫瓶 - 黄色', 'FHL-402-OPCAT', '400ml',
  '保冷專用；6 小時：冷 12°C 以下；200g；口徑 4.4cm', '$368', 'THERMOS 香港官方網店',
  'https://www.thermos.com.hk/product/7a3b8d12-7423-4b1c-b8c5-1759f796c544',
  'https://assets.omniwe.com/generated/6254ca3cb48a186a7176222943f476c5614193c7.png', [None, 3, 5],
  '幼童夏天裝凍水', '只限保冷，不可以裝熱飲。重量只有 200g，適合年紀較小的小朋友。'),
]

CRIT = ['保熱能力', '保冷能力', '便攜／重量']
TYPE_LABEL = {'A': '保溫杯（480ml 至 500ml）', 'B': '大容量保溫瓶／保溫壺（1L 以上）', 'C': '兒童保溫水壺'}

TYPES_B3 = [('保溫杯（480ml 至 500ml）', [4, 5, 5], '上班、上學、通勤隨身'),
            ('大容量保溫瓶／保溫壺（1L 以上）', [5, 4, 2], '行山、辦公室、家中長時間保熱'),
            ('兒童保溫水壺', [4, 4, 4], '幼稚園及小學生上學')]
TYPE_CRIT_B3 = ['保熱能力', '保冷能力', '便攜']

# 三大品牌比較表（以 480ml 至 500ml 保溫杯官方數字比較）
BRAND_TABLE = [
 ('象印 Zojirushi', 'SM-WS48', '71°C 以上', '8°C 以下', '0.21kg', '官方未有註明', '$199（原價 $249）', '生活館（象印香港代理）'),
 ('虎牌 Tiger', 'MMJ-S048', '67°C 以上', '8°C 以下', '0.19kg', '可以', '$198（原價 $308）', '虎牌香港官方網店'),
 ('膳魔師 Thermos', 'JNL-502SS', '68°C 以上', '10°C 以下', '0.21kg', '可以', '$368', '膳魔師香港官方網店'),
]

OUTLINE_B3 = [
 ('H2 1｜保溫杯、保溫瓶、保溫壺有甚麼分別？', None,
  ['開首 40 至 60 字快答：按容量及用途分三類，下面用 H3 及星星評分逐類說明，爭取精選摘要。']),
 ('H2 2｜象印、虎牌、膳魔師保溫杯比較：邊個牌子好？', 'C9',
  ['H3 2.1 三大品牌 6 小時保熱、保冷數字比較（附比較表）', 'H3 2.2 重量、清洗及洗碗碟機適用比較',
   'H3 2.3 其他品牌：駱駝牌、Stanley 簡介（承接「駱駝牌保溫壺」「保溫杯 stanley」）',
   '註：只有象印網頁說明測試方法（室溫 20°C、注入 95°C 熱水），三個品牌的數字未必完全以同一標準量度。']),
 ('H2 3｜保溫杯推介：480ml 至 500ml 隨身款', 'A', ['三款產品段落：象印 SM-WS48、虎牌 MMJ-S048、膳魔師 JNL-502SS']),
 ('H2 4｜大容量保溫瓶及保溫壺推介：1L 以上', 'B',
  ['H3 4.1 象印保溫壺有甚麼款式？（承接「象印保溫壺」1,900、1.5L 枱面壺）', '三款產品段落：象印 SJ-JS10、虎牌 MHK-A120、膳魔師 JOS-1000']),
 ('H2 5｜兒童保溫水壺推介：吸管款及兩用款', 'C', ['三款產品段落：象印 SD-CAE50、虎牌 MBR-G06G、膳魔師 FHL-402']),
 ('H2 6｜保溫杯清洗、壽命及安全', None,
  ['H3 6.1 保溫瓶第一次使用怎樣清洗？', 'H3 6.2 保溫杯可以裝茶、咖啡或運動飲品嗎？', 'H3 6.3 保溫杯多久要換？凹陷後還能保溫嗎？',
   'H3 6.4 「保溫杯致癌」是真的嗎？（引用消委會或食安中心資料，不作誇大說法）']),
 ('H2 7｜常見問題', 'FAQ', ['FAQPage schema，每題先用 1 至 2 句直接回答']),
]


def stars(v):
    if v is None:
        return '<span class="na">官方未列／不適用</span>'
    return '<span class="stars">' + '★' * v + '<i>' + '★' * (5 - v) + '</i></span>'


def product_html(p):
    t, brand, name, sku, size, spec, price, shop, url, img, sc, scene, desc = p
    rate = '<br>'.join(f'{E(c)}：{stars(v)}' for c, v in zip(CRIT, sc))
    return f'''<div class="pt"><img src="{E(img)}" alt="{E(name)}" loading="lazy" referrerpolicy="no-referrer">
<p class="iu">圖片：<a href="{E(img)}" target="_blank" rel="noopener">{E(img)}</a></p>
<p>品牌：{E(brand)}<br>產品名稱：{E(name)}<br>型號：{E(sku)}<br>容量：{E(size)}<br>重點規格：{E(spec)}<br>價錢（HKD）：{E(price)}（{E(shop)}，{E(PRICE_DATE_B3)}記錄）<br>購買連結：<a href="{E(url)}" target="_blank" rel="nofollow noopener">{E(url)}</a></p>
<p>{rate}</p>
<p class="pd">{E(desc)}</p>
<p>適合場景／對象：{E(scene)}</p></div>'''


def brand_table_html():
    head = ['品牌', '型號', '6 小時保熱', '6 小時保冷', '重量', '洗碗碟機', '價錢（HKD）', '網店']
    return ('<div style="overflow:auto"><table class="cmp"><tr>' + ''.join(f'<th>{h}</th>' for h in head) + '</tr>'
            + ''.join('<tr>' + ''.join(f'<td>{E(c)}</td>' for c in r) + '</tr>' for r in BRAND_TABLE) + '</table></div>'
            + f'<p class="src">以 480ml 至 500ml 保溫杯的官方數字比較；價錢為 {PRICE_DATE_B3} 在各品牌香港官方網店記錄。</p>')


def products_for(t):
    return '<div class="plist">' + ''.join(product_html(p) for p in B3_PRODUCTS if p[0] == t) + '</div>'
