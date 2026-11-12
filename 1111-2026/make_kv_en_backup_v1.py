# -*- coding: utf-8 -*-
"""英文版 KV 及四重賞圖：讀取 make_kv3.py，把中文字換成英文後執行。
輸出 img/d11-kv-en.jpg、img/d11-rewards-en.jpg"""
import os, sys, types
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
src = open(os.path.join(H, 'make_kv3.py'), encoding='utf-8').read()
R = [
 # KV
 ("line(d, [('一連七天　', INK), ('雙 11 四重賞', INK)], f_cjk(84), 384)", "line(d, [('11.11 FOUR REWARDS · 7 DAYS', INK)], f_cjk(62), 396)"),
 ("line(d, [('滿 HK$1,100 ', INK), ('全網 11% OFF', RED)], f_cjk(54), 512)", "line(d, [('Spend HK$1,100, get ', INK), ('11% OFF sitewide', RED)], f_cjk(46), 516)"),
 ("fs = f_cjk(28); sub = '滿 HK$1,500 起再送人氣小食，最多送 3 款'", "fs = f_cjk(28); sub = 'Spend HK$1,500+ for free snacks, up to 3 items'"),
 ("bg.alpha_composite(tab, (W - 84, 110))", "pass"),
 # 卡內文字
 ("'日式雞皮餃子', 198", "'Chicken Skin Gyoza', 198"), ("'避風塘海鮮豆腐', 178", "'Seafood Tofu', 178"), ("'蜜蜜燒雞翼', 188", "'Honey Chicken Wings', 188"),
 ("name, sub = '全單 11% OFF', '全網套餐及單點'", "name, sub = '11% OFF', 'All sets & a la carte'"),
 ("name, sub = '全網 11% OFF', '全網所有套餐及單點'", "name, sub = '11% OFF Sitewide', 'All sets & a la carte'"),
 ("f'10 件・原價 ${ITEMS[key][3]}'", "f'10 pcs · worth ${ITEMS[key][3]}'"),
 ("fn = f_cjk(32 if len(name) <= 6 else 30); fs = f_cjk(27, False)", "fn = f_cjk(22); fs = f_cjk(20, False)"),
 ("fv = f_cjk(30); fn = f_cjk(36); fs = f_cjk(30, False); y = pad + ph + 12", "fv = f_cjk(26); fn = f_cjk(28); fs = f_cjk(24, False); y = pad + ph + 12"),
 ("('第一賞', '1,100', [], 'off', '全單', '全網所有套餐及單點即減 11%')", "('Reward 1', '1,100', [], 'off', 'Whole order', '11% off everything')"),
 ("('第二賞', '1,500', ['off'], 'a1600', '送', '11% OFF＋送 1 款小食・小食總值 $198')", "('Reward 2', '1,500', ['off'], 'a1600', 'Free', '11% OFF + 1 free snack・Snacks worth $198')"),
 ("('第三賞', '2,200', ['off', 'a1600'], 'a1500', '再加送', '11% OFF＋送 2 款小食・小食總值 $376')", "('Reward 3', '2,200', ['off', 'a1600'], 'a1500', 'Plus', '11% OFF + 2 free snacks・Snacks worth $376')"),
 ("('第四賞', '3,000', ['off', 'a1600', 'a1500'], 'a0500', '再加送', '11% OFF＋送 3 款小食・小食總值 $564')", "('Reward 4', '3,000', ['off', 'a1600', 'a1500'], 'a0500', 'Plus', '11% OFF + 3 free snacks・Snacks worth $564')"),
 ("t1, t2 = lv, '滿 $' + amt", "t1, t2 = lv, 'Spend $' + amt"),
]
for a, b in R:
    assert a in src, a[:60]
    src = src.replace(a, b)
src = src.replace("if __name__ == '__main__'", "if False")
m = types.ModuleType('kv_en'); m.__file__ = os.path.join(H, 'make_kv3.py'); exec(compile(src, 'make_kv_en', 'exec'), m.__dict__)
k = m.kv_design(10, False); k.save(os.path.join(H, 'img', 'd11-kv-en.jpg'), quality=80, optimize=True, progressive=True)
r = m.rewards_img(); r.save(os.path.join(H, 'img', 'd11-rewards-en.jpg'), quality=80, optimize=True, progressive=True)
print('ok', k.size, r.size)
