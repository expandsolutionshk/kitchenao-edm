# -*- coding: utf-8 -*-
"""雙 11 KV v3：方案 3 字體＋兩張完整產品主圖＋四重賞贈品列（圓章完整）
來源圖：/tmp/kv（網站下載＋客戶提供餐盒相 bento.jpg）；輸出 img/d11-kv.jpg"""
import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageChops
H = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src') + '/'
W, HH = 1200, 3520
CJK = '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
CJKR = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
POPB = '/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf'
LATO_BI = '/usr/share/fonts/truetype/lato/Lato-BlackItalic.ttf'
def f_cjk(s, bold=True): return ImageFont.truetype(CJK if bold else CJKR, s, index=4)
def f_pop(s): return ImageFont.truetype(POPB, s)
GOLD_D, GOLD, GOLD_L, INK, RED = (150, 108, 38), (200, 162, 74), (240, 214, 150), (26, 26, 26), (176, 52, 38)
def lerp(a, b, t): return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))
def layer(): return Image.new('RGBA', (W, HH), (0, 0, 0, 0))
SY = 1395
GLOW_Y = 1130

def background():
    bg = Image.new('RGB', (W, HH)); dd = ImageDraw.Draw(bg)
    top, mid, bot = (253, 248, 239), (243, 226, 196), (226, 198, 150)
    for y in range(HH):
        t = y / HH
        dd.line([(0, y), (W, y)], fill=lerp(top, mid, t / .6) if t < .6 else lerp(mid, bot, (t - .6) / .4))
    bg = bg.convert('RGBA')
    beams = layer(); d = ImageDraw.Draw(beams)
    for x0, w, a in [(-200, 160, 70), (180, 90, 55), (760, 220, 60), (1040, 80, 45)]:
        d.polygon([(x0, 0), (x0 + w, 0), (x0 + w + 600, HH), (x0 + 600, HH)], fill=(255, 255, 255, a))
    bg = Image.alpha_composite(bg, beams.filter(ImageFilter.GaussianBlur(28)))
    g = Image.new('RGBA', (W, HH), (255, 252, 244, 0)); m = Image.new('L', (W, HH), 0)
    ImageDraw.Draw(m).ellipse([600 - 520, GLOW_Y - 360, 600 + 520, GLOW_Y + 360], fill=235)
    g.putalpha(m.filter(ImageFilter.GaussianBlur(170))); bg = Image.alpha_composite(bg, g)
    st = layer(); sd = ImageDraw.Draw(st)
    for y in range(SY, HH):
        sd.line([(0, y), (W, y)], fill=lerp((250, 240, 222), (232, 208, 166), (y - SY) / (HH - SY)) + (255,))
    bg = Image.alpha_composite(bg, st); ImageDraw.Draw(bg).line([(0, SY), (W, SY)], fill=GOLD + (255,), width=3)
    hl = layer(); ImageDraw.Draw(hl).rectangle([0, SY + 3, W, SY + 26], fill=(255, 255, 255, 120))
    return Image.alpha_composite(bg, hl.filter(ImageFilter.GaussianBlur(6)))

def title(bg, top=140, size=320):  # 方案 3：粗體雙層
    f = ImageFont.truetype(LATO_BI, size); bb = f.getbbox('11.11')
    tx, ty = (W - (bb[2] - bb[0])) // 2 - bb[0], top - bb[1]
    d = ImageDraw.Draw(bg); d.text((tx + 16, ty + 14), '11.11', font=f, fill=(0, 0, 0, 0), stroke_width=5, stroke_fill=GOLD)
    sh = layer(); ImageDraw.Draw(sh).text((tx + 6, ty + 18), '11.11', font=f, fill=(60, 40, 10, 90))
    bg = Image.alpha_composite(bg, sh.filter(ImageFilter.GaussianBlur(14)))
    ImageDraw.Draw(bg).text((tx, ty), '11.11', font=f, fill=INK)
    m = Image.new('L', (W, HH), 0); ImageDraw.Draw(m).text((tx, ty), '11.11', font=f, fill=255)
    hi = Image.new('RGBA', (W, HH), (0, 0, 0, 0)); ImageDraw.Draw(hi).rectangle([0, ty + bb[1], W, ty + bb[1] + 12], fill=GOLD + (255,))
    hi.putalpha(ImageChops.multiply(hi.getchannel('A'), m))
    return Image.alpha_composite(bg, hi)

def line(d, parts, font, y, sh=True):
    total = sum(d.textlength(p, font=font) for p, _ in parts); x = (W - total) / 2
    for p, c in parts:
        if sh: d.text((x + 3, y + 4), p, font=font, fill=(255, 255, 255))
        d.text((x, y), p, font=font, fill=c); x += d.textlength(p, font=font)

def headline(bg):
    d = ImageDraw.Draw(bg)
    line(d, [('一連七天', INK)], f_cjk(120), 520)
    line(d, [('滿 HK$1,100 ', INK), ('全網 11% OFF', RED)], f_cjk(64), 690)
    fs = f_cjk(32); sub = '滿 HK$1,500 起再送人氣小食，最多送 3 款'
    d.text(((W - d.textlength(sub, font=fs)) / 2, 792), sub, font=fs, fill=(107, 90, 63))
    return bg

def framed(im, w, rot, border=16):
    im = im.resize((w, int(w * im.height / im.width)), Image.LANCZOS).convert('RGBA')
    m = Image.new('L', im.size, 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, im.width - 1, im.height - 1], 18, fill=255); im.putalpha(m)
    fw, fh = im.width + border * 2, im.height + border * 2
    fr = Image.new('RGBA', (fw, fh), (0, 0, 0, 0))
    mk = Image.new('L', (fw, fh), 0); ImageDraw.Draw(mk).rounded_rectangle([0, 0, fw - 1, fh - 1], 28, fill=255)
    b = Image.new('RGBA', (fw, fh), (255, 255, 255, 255)); b.putalpha(mk); fr.alpha_composite(b)
    ImageDraw.Draw(fr).rounded_rectangle([3, 3, fw - 4, fh - 4], 26, outline=GOLD, width=3)
    fr.alpha_composite(im, (border, border))
    fr = fr.rotate(rot, resample=Image.BICUBIC, expand=True)
    s = Image.new('RGBA', (fr.width + 100, fr.height + 100), (0, 0, 0, 0))
    s.paste((70, 45, 15, 120), (62, 78), fr.getchannel('A')); s = s.filter(ImageFilter.GaussianBlur(20)); s.alpha_composite(fr, (50, 50))
    return s

def _src3():
    pot = Image.open(SRC + 'd11src-c3.jpg').convert('RGB').crop((120, 585, 1600, 1600))
    bento = Image.open(SRC + 'bento.jpg').convert('RGB').crop((0, 160, 1200, 1600))
    buf = Image.open(SRC + 'photo3.jpg').convert('RGB').crop((0, 820, 1920, 2560))
    return pot, bento, buf
def fit(im, w, h):  # 置中裁切到指定比例
    r = w / h
    if im.width / im.height > r:
        nw = int(im.height * r); x = (im.width - nw) // 2; im = im.crop((x, 0, x + nw, im.height))
    else:
        nh = int(im.width / r); y = (im.height - nh) // 2; im = im.crop((0, y, im.width, y + nh))
    return im.resize((w, h), Image.LANCZOS)
def tile(im, w, h, radius=20, border=10, rot=0, shadow=True):
    im = fit(im, w, h).convert('RGBA')
    m = Image.new('L', im.size, 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, w - 1, h - 1], radius, fill=255); im.putalpha(m)
    fw, fh = w + 2 * border, h + 2 * border
    fr = Image.new('RGBA', (fw, fh), (0, 0, 0, 0))
    mk = Image.new('L', (fw, fh), 0); ImageDraw.Draw(mk).rounded_rectangle([0, 0, fw - 1, fh - 1], radius + border, fill=255)
    bb = Image.new('RGBA', (fw, fh), (255, 255, 255, 255)); bb.putalpha(mk); fr.alpha_composite(bb)
    ImageDraw.Draw(fr).rounded_rectangle([2, 2, fw - 3, fh - 3], radius + border - 2, outline=GOLD, width=3)
    fr.alpha_composite(im, (border, border))
    if rot: fr = fr.rotate(rot, resample=Image.BICUBIC, expand=True)
    s = Image.new('RGBA', (fr.width + 100, fr.height + 100), (0, 0, 0, 0))
    if shadow: s.paste((70, 45, 15, 115), (60, 76), fr.getchannel('A')); s = s.filter(ImageFilter.GaussianBlur(20))
    s.alpha_composite(fr, (50, 50)); return s
def put(bg, t, x, y): bg.alpha_composite(t, (x - 50, y - 50))

HERO_MODE = os.environ.get('HERO', 'A')
def heroes(bg):
    pot, bento, buf = _src3()
    if HERO_MODE == 'A':   # 三聯直幅：中間較大較高
        pot2 = Image.open(SRC + 'pot1024.jpg').convert('RGB')
        put(bg, tile(bento, 290, 390, rot=0), 40, 940)
        put(bg, tile(buf, 290, 390, rot=0), 870, 940)
        put(bg, tile(pot2, 440, 440, rot=0), 380, 905)
    elif HERO_MODE == 'B': # 編輯式拼貼：左大圖＋右兩格，直角對齊
        put(bg, tile(pot, 660, 480, radius=14), 40, 750)
        put(bg, tile(bento, 420, 226, radius=14), 730, 750)
        put(bg, tile(buf, 420, 226, radius=14), 730, 1004)
    else:                  # 扇形疊卡：三張打斜重疊，中間最前
        put(bg, tile(bento, 340, 420, rot=9), 700, 760)
        put(bg, tile(buf, 340, 420, rot=-9), 70, 760)
        put(bg, tile(pot, 480, 400, rot=0), 360, 790)
    return bg

ITEMS = {
 'off': None,
 'a1600': ('d11src-g1.png', (90, 90, 1042, 640), '日式雞皮餃子', 198),
 'a1500': ('d11src-g3.png', (100, 90, 1042, 640), '避風塘海鮮豆腐', 178),
 'a0500': ('d11src-g2.jpg', (40, 60, 1024, 630), '蜜蜜燒雞翼', 188),
}
def _photo(key, w, h):
    src, crop, _, _ = ITEMS[key]
    im = Image.open(SRC + src).convert('RGB').crop(crop)
    th = int(w * im.height / im.width); im = im.resize((w, th), Image.LANCZOS)
    top = max(0, (th - h) // 2); im = im.crop((0, top, w, top + h)).convert('RGBA')
    m = Image.new('L', im.size, 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, w - 1, h - 1], 12, fill=255); im.putalpha(m); return im
def _off_block(d, x, y, w, h, big):
    d.rounded_rectangle([x, y, x + w - 1, y + h - 1], 12, fill=INK)
    f1 = f_pop(int(h * .48)); t = '11%'; d.text((x + (w - d.textlength(t, font=f1)) / 2, y + h * .06), t, font=f1, fill=GOLD_L)
    f2 = f_pop(int(h * .2)); t = 'OFF'; d.text((x + (w - d.textlength(t, font=f2)) / 2, y + h * .64), t, font=f2, fill=(255, 255, 255))
def _card_canvas(cw, ch):
    c = Image.new('RGBA', (cw, ch), (0, 0, 0, 0)); mk = Image.new('L', (cw, ch), 0)
    ImageDraw.Draw(mk).rounded_rectangle([0, 0, cw - 1, ch - 1], 18, fill=255)
    b = Image.new('RGBA', (cw, ch), (255, 255, 255, 255)); b.putalpha(mk); c.alpha_composite(b)
    ImageDraw.Draw(c).rounded_rectangle([1, 1, cw - 2, ch - 2], 18, outline=(232, 218, 190), width=2); return c
def back_card(key, w=180):  # 後排：標題在上，壓在前卡後仍看得到
    pad = 10; ph = int(w * .6); cap = 62; cw, ch = w + 2 * pad, cap + ph + 2 * pad
    c = _card_canvas(cw, ch); d = ImageDraw.Draw(c)
    if key == 'off':
        name, sub = '全單 11% OFF', '全網套餐及單點'
    else:
        name, sub = ITEMS[key][2], f'10 件・原價 ${ITEMS[key][3]}'
    fn = f_cjk(22 if len(name) <= 6 else 19); fs = f_cjk(16, False)
    d.text(((cw - d.textlength(name, font=fn)) / 2, pad - 2), name, font=fn, fill=INK)
    d.text(((cw - d.textlength(sub, font=fs)) / 2, pad + 30), sub, font=fs, fill=GOLD_D)
    if key == 'off': _off_block(d, pad, pad + cap, w, ph, False)
    else: c.alpha_composite(_photo(key, w, ph), (pad, pad + cap))
    return c
def front_card(key, verb, w=260):
    pad = 12; ph = int(w * .6); lab = 96; cw, ch = w + 2 * pad, ph + 2 * pad + lab
    c = _card_canvas(cw, ch); d = ImageDraw.Draw(c)
    if key == 'off':
        _off_block(d, pad, pad, w, ph, True); name, sub = '全單 11% OFF', '全網所有套餐及單點'
    else:
        c.alpha_composite(_photo(key, w, ph), (pad, pad)); name, sub = ITEMS[key][2], f'10 件・原價 ${ITEMS[key][3]}'
    fv = f_cjk(22); fn = f_cjk(27 if len(name) <= 6 else 24)
    tw = d.textlength(verb, font=fv); nw = d.textlength(name, font=fn)
    x = (cw - (tw + 16 + 12 + nw)) / 2; y = pad + ph + 12
    d.rounded_rectangle([x - 4, y + 3, x + tw + 12, y + 39], 9, fill=GOLD); d.text((x + 4, y + 3), verb, font=fv, fill=(255, 255, 255))
    d.text((x + tw + 24, y), name, font=fn, fill=INK)
    fs = f_cjk(20, False); d.text(((cw - d.textlength(sub, font=fs)) / 2, y + 48), sub, font=fs, fill=GOLD_D)
    return c
def _float(c, rot, blur=12, off=(6, 10), alpha=65):
    c = c.rotate(rot, resample=Image.BICUBIC, expand=True)
    s = Image.new('RGBA', (c.width + 50, c.height + 50), (0, 0, 0, 0))
    s.paste((70, 45, 15, alpha), (25 + off[0], 25 + off[1]), c.getchannel('A')); s = s.filter(ImageFilter.GaussianBlur(blur)); s.alpha_composite(c, (25, 25)); return s
TIER = [  # (第幾賞, 金額, 後排, 前卡, 動詞, 總結)
 ('第一賞', '1,100', [], 'off', '全單', '全網所有套餐及單點即減 11%'),
 ('第二賞', '1,500', ['off'], 'a1600', '送', '11% OFF＋送 1 款小食・小食總值 $198'),
 ('第三賞', '2,200', ['off', 'a1600'], 'a1500', '再加送', '11% OFF＋送 2 款小食・小食總值 $376'),
 ('第四賞', '3,000', ['off', 'a1600', 'a1500'], 'a0500', '再加送', '11% OFF＋送 3 款小食・小食總值 $564'),
]
BACK_POS = {0: [], 1: [(-120, 10, -7)], 2: [(-150, 20, -9), (150, 20, 9)], 3: [(-160, 40, -10), (0, 0, 0), (160, 40, 10)]}
PW, PH = 540, 700
def panel(lv, amt, backs, front, verb, summ):
    p = Image.new('RGBA', (PW, PH + 80), (0, 0, 0, 0)); T = 80
    mk = Image.new('L', p.size, 0); ImageDraw.Draw(mk).rounded_rectangle([0, T, PW - 1, T + PH - 1], 28, fill=255)
    b = Image.new('RGBA', p.size, (255, 255, 255, 235)); b.putalpha(ImageChops.multiply(mk, Image.new('L', p.size, 235))); p.alpha_composite(b)
    ImageDraw.Draw(p).rounded_rectangle([2, T + 2, PW - 3, T + PH - 3], 26, outline=GOLD, width=2)
    cx = PW // 2; top = T + 140
    for key, (dx, dy, r) in zip(backs, BACK_POS[len(backs)]):
        c = _float(back_card(key), r); p.alpha_composite(c, (int(cx + dx - c.width / 2), top + dy - 25))
    fy = top + (150 if backs else 30)
    c = _float(front_card(front, verb, 270 if backs else 320), 0, 14, (6, 12), 70); p.alpha_composite(c, (int(cx - c.width / 2), fy - 25))
    d = ImageDraw.Draw(p)
    # 底部深色資訊條（另一層背景）
    band = Image.new('RGBA', p.size, (0, 0, 0, 0)); bd = ImageDraw.Draw(band)
    bd.rounded_rectangle([0, T + PH - 92, PW - 1, T + PH - 1], 28, fill=INK + (255,)); bd.rectangle([0, T + PH - 92, PW - 1, T + PH - 60], fill=INK + (255,))
    band.putalpha(ImageChops.multiply(band.getchannel('A'), mk)); p.alpha_composite(band); d = ImageDraw.Draw(p)
    d.line([(40, T + PH - 92), (PW - 40, T + PH - 92)], fill=GOLD, width=2)
    fs = f_cjk(26); d.text(((PW - d.textlength(summ, font=fs)) / 2, T + PH - 66), summ, font=fs, fill=GOLD_L)
    # 第幾賞：放在圓章下面，金色膠囊突出
    fl = f_cjk(28); lw = d.textlength(lv, font=fl); ly = T + 78
    d.rounded_rectangle([cx - lw / 2 - 24, ly, cx + lw / 2 + 24, ly + 46], 23, fill=GOLD)
    d.text((cx - lw / 2, ly + 3), lv, font=fl, fill=INK)
    R = 62; sx, sy = cx, T + 4
    d.ellipse([sx - R - 4, sy - R - 4, sx + R + 4, sy + R + 4], fill=(255, 255, 255))
    d.ellipse([sx - R, sy - R, sx + R, sy + R], fill=INK); d.ellipse([sx - R + 8, sy - R + 8, sx + R - 8, sy + R - 8], outline=GOLD, width=3)
    fa, fb = f_cjk(23), f_pop(29)
    d.text((sx - d.textlength('滿', font=fa) / 2, sy - 44), '滿', font=fa, fill=GOLD_L)
    d.text((sx - d.textlength('$' + amt, font=fb) / 2, sy - 13), '$' + amt, font=fb, fill=(255, 255, 255))
    return p
ROW_Y = [1640, 2490]
def rewards(bg):
    d = ImageDraw.Draw(bg)
    fe = f_pop(22); s = 'F O U R   R E W A R D S'
    d.text(((W - d.textlength(s, font=fe)) / 2, 1490), s, font=fe, fill=GOLD_D)
    line(d, [('雙 11 四重賞', INK)], f_cjk(56), 1524, sh=False)
    pos = [(48, ROW_Y[0]), (612, ROW_Y[0]), (48, ROW_Y[1]), (612, ROW_Y[1])]
    for t, (x, y) in zip(TIER, pos):
        p = panel(*t); sh = Image.new('RGBA', (p.width + 60, p.height + 60), (0, 0, 0, 0))
        sh.paste((70, 45, 15, 70), (36, 46), p.getchannel('A')); sh = sh.filter(ImageFilter.GaussianBlur(16)); sh.alpha_composite(p, (30, 30))
        bg.alpha_composite(sh, (x - 30, y - 30))
    return bg

def tab_and_pill(bg):
    tab = Image.new('RGBA', (92, 300), INK + (255,)); td = ImageDraw.Draw(tab); fv = f_cjk(34)
    for i, ch_ in enumerate('雙十一限定'): td.text(((92 - td.textlength(ch_, font=fv)) / 2, 22 + i * 52), ch_, font=fv, fill=GOLD_L)
    bg.alpha_composite(tab, (W - 92, 170))
    d = ImageDraw.Draw(bg); fp = f_cjk(36); pill = '2026.11.11 至 11.17　優惠碼 DOUBLE11'
    pw = d.textlength(pill, font=fp) + 80; x0 = (W - pw) / 2; y0 = 3355
    d.rounded_rectangle([x0, y0, x0 + pw, y0 + 74], 37, fill=INK); d.text((x0 + 40, y0 + 12), pill, font=fp, fill=GOLD_L)
    return bg

def kv_square():
    """1:1 主 KV：11.11＋標題＋三張主圖＋膠囊（空間感參考 11.11 圖）"""
    global HH, SY, GLOW_Y
    HH, SY, GLOW_Y = 1200, 1030, 860
    bg = background(); bg = title(bg, top=70, size=300)
    d = ImageDraw.Draw(bg)
    line(d, [('一連七天', INK)], f_cjk(104), 372)
    line(d, [('滿 HK$1,100 ', INK), ('全網 11% OFF', RED)], f_cjk(54), 512)
    fs = f_cjk(28); sub = '滿 HK$1,500 起再送人氣小食，最多送 3 款'
    d.text(((W - d.textlength(sub, font=fs)) / 2, 596), sub, font=fs, fill=(107, 90, 63))
    pot, bento, buf = _src3(); pot2 = Image.open(SRC + 'pot1024.jpg').convert('RGB')
    put(bg, tile(bento, 250, 330), 70, 700)
    put(bg, tile(buf, 250, 330), 880, 700)
    put(bg, tile(pot2, 380, 380), 410, 670)
    tab = Image.new('RGBA', (84, 270), INK + (255,)); td = ImageDraw.Draw(tab); fv = f_cjk(30)
    for i, ch_ in enumerate('雙十一限定'): td.text(((84 - td.textlength(ch_, font=fv)) / 2, 20 + i * 47), ch_, font=fv, fill=GOLD_L)
    bg.alpha_composite(tab, (W - 84, 110))
    d = ImageDraw.Draw(bg); fp = f_cjk(32); pill = '2026.11.11 至 11.17　優惠碼 DOUBLE11'
    pw = d.textlength(pill, font=fp) + 72; x0 = (W - pw) / 2; y0 = 1106
    d.rounded_rectangle([x0, y0, x0 + pw, y0 + 64], 32, fill=INK); d.text((x0 + 36, y0 + 10), pill, font=fp, fill=GOLD_L)
    return bg.convert('RGB')

def rewards_img():
    """四重賞獨立圖：放在 EDM 優惠碼下面"""
    global HH, SY, GLOW_Y, ROW_Y
    HH, SY, GLOW_Y = 1700, 99999, -9999
    bg = Image.new('RGBA', (W, HH), (243, 231, 210, 255))
    ROW_Y = [60, 900]
    pos = [(48, ROW_Y[0]), (612, ROW_Y[0]), (48, ROW_Y[1]), (612, ROW_Y[1])]
    for t, (x, y) in zip(TIER, pos):
        p = panel(*t); sh = Image.new('RGBA', (p.width + 60, p.height + 60), (0, 0, 0, 0))
        sh.paste((70, 45, 15, 60), (34, 42), p.getchannel('A')); sh = sh.filter(ImageFilter.GaussianBlur(16)); sh.alpha_composite(p, (30, 30))
        bg.alpha_composite(sh, (x - 30, y - 30))
    return bg.convert('RGB')

def _shadowed(im, blur=22, off=(0, 18), alpha=110, pad=60):
    s = Image.new('RGBA', (im.width + 2 * pad, im.height + 2 * pad), (0, 0, 0, 0))
    s.paste((60, 40, 15, alpha), (pad + off[0], pad + off[1]), im.getchannel('A')); s = s.filter(ImageFilter.GaussianBlur(blur)); s.alpha_composite(im, (pad, pad)); return s
def _round(im, w, h, r):
    im = fit(im, w, h).convert('RGBA'); m = Image.new('L', (w, h), 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, w - 1, h - 1], r, fill=255); im.putalpha(m); return im
def _arch(im, w, h, outline=True):
    im = fit(im, w, h).convert('RGBA'); m = Image.new('L', (w * 3, h * 3), 0); dm = ImageDraw.Draw(m)
    dm.ellipse([0, 0, w * 3 - 1, w * 3 - 1], fill=255); dm.rectangle([0, w * 3 // 2, w * 3 - 1, h * 3 - 1], fill=255)
    m = m.resize((w, h), Image.LANCZOS); im.putalpha(m)
    if outline:
        o = Image.new('RGBA', (w + 28, h + 28), (0, 0, 0, 0)); om = Image.new('L', ((w + 28) * 3, (h + 28) * 3), 0); do = ImageDraw.Draw(om)
        W3 = (w + 28) * 3; do.ellipse([0, 0, W3 - 1, W3 - 1], outline=255, width=9); do.line([(4, W3 // 2), (4, (h + 28) * 3)], fill=255, width=9); do.line([(W3 - 5, W3 // 2), (W3 - 5, (h + 28) * 3)], fill=255, width=9)
        om = om.resize(o.size, Image.LANCZOS); g = Image.new('RGBA', o.size, GOLD + (255,)); g.putalpha(om)
        o.alpha_composite(g); o.alpha_composite(im, (14, 14)); return o
    return im
CAP = ['精緻擺盤到會', '「冩樂」蟹皇左口魚煲仔飯', '自助餐到會']
def kv_design(n, pill_on=True):
    global HH, SY, GLOW_Y
    HH, SY, GLOW_Y = 1240, (1030 if n in (1, 2) else 99999), 880
    bg = background(); bg = title(bg, top=70, size=300)
    d = ImageDraw.Draw(bg)
    line(d, [('一連七天', INK)], f_cjk(104), 372)
    line(d, [('滿 HK$1,100 ', INK), ('全網 11% OFF', RED)], f_cjk(54), 512)
    fs = f_cjk(28); sub = '滿 HK$1,500 起再送人氣小食，最多送 3 款'
    d.text(((W - d.textlength(sub, font=fs)) / 2, 596), sub, font=fs, fill=(107, 90, 63))
    pot, bento, buf = _src3(); pot2 = Image.open(SRC + 'pot1024.jpg').convert('RGB')
    fc = f_cjk(22, False)
    if n == 1:   # 無框大圖＋輕微重疊＋柔和陰影＋圖下細字
        L = _shadowed(_round(bento, 300, 330, 26)); R = _shadowed(_round(buf, 300, 330, 26)); C = _shadowed(_round(pot2, 400, 400, 30), alpha=140)
        bg.alpha_composite(L, (70 - 60, 690 - 60)); bg.alpha_composite(R, (830 - 60, 690 - 60)); bg.alpha_composite(C, (400 - 60, 650 - 60))
        d = ImageDraw.Draw(bg)
        for t, x0, w, y in [(CAP[0], 70, 300, 1034), (CAP[1], 400, 400, 1064), (CAP[2], 830, 300, 1034)]:
            d.text((x0 + (w - d.textlength(t, font=fc)) / 2, y), t, font=fc, fill=(107, 90, 63))
    elif n == 2: # 拱形窗：Four Seasons 式，金幼線拱框，中間最高
        L = _shadowed(_arch(bento, 270, 360), alpha=80); R = _shadowed(_arch(buf, 270, 360), alpha=80); C = _shadowed(_arch(pot2, 360, 430), alpha=100)
        bg.alpha_composite(L, (90 - 74, 690 - 74)); bg.alpha_composite(R, (840 - 74, 690 - 74)); bg.alpha_composite(C, (406 - 74, 630 - 74))
    elif n == 3:        # 全景條：三圖連成一條，白幼隙，底部漸黑加說明
        y0, h = 660, 400; ws = [370, 448, 370]; x = 0
        strip = Image.new('RGBA', (W, h), (255, 255, 255, 255))
        for im, w, cap in zip([bento, pot2, buf], ws, CAP):
            t = fit(im, w, h).convert('RGBA'); strip.alpha_composite(t, (x, 0))
            gr = Image.new('RGBA', (w, 120), (0, 0, 0, 0)); gd = ImageDraw.Draw(gr)
            for yy in range(120): gd.line([(0, yy), (w, yy)], fill=(15, 12, 8, int(170 * yy / 120)))
            strip.alpha_composite(gr, (x, h - 120)); sd = ImageDraw.Draw(strip)
            sd.text((x + (w - sd.textlength(cap, font=fc)) / 2, h - 44), cap, font=fc, fill=(255, 245, 225))
            x += w + 6
        bg.alpha_composite(strip, (0, y0)); d = ImageDraw.Draw(bg)
        d.line([(0, y0 - 8), (W, y0 - 8)], fill=GOLD, width=3); d.line([(0, y0 + h + 8), (W, y0 + h + 8)], fill=GOLD, width=3)
    elif n == 4:  # C1：全闊全景，無隙、無漸黑，上下金線
        y0, h = 660, 400; ws = [376, 448, 376]; x = 0
        for im, w in zip([bento, pot2, buf], ws):
            bg.alpha_composite(fit(im, w, h).convert('RGBA'), (x, y0)); x += w
        d = ImageDraw.Draw(bg)
        for xx in (376, 824): d.line([(xx, y0), (xx, y0 + h)], fill=GOLD, width=3)
        d.line([(0, y0 - 2), (W, y0 - 2)], fill=GOLD, width=4); d.line([(0, y0 + h + 1), (W, y0 + h + 1)], fill=GOLD, width=4)
    elif n == 5:  # C2：內縮圓角全景，中間格加高凸出
        y0, h = 750, 360; m = 40; ws = [352, 0, 352]; cw = W - 2 * m - 352 * 2 - 24
        strip = Image.new('RGBA', (W - 2 * m, h), (0, 0, 0, 0))
        strip.alpha_composite(fit(bento, 352, h).convert('RGBA'), (0, 0)); strip.alpha_composite(fit(buf, 352, h).convert('RGBA'), (352 + 12 + cw + 12, 0))
        mk = Image.new('L', strip.size, 0); ImageDraw.Draw(mk).rounded_rectangle([0, 0, strip.width - 1, h - 1], 24, fill=255); strip.putalpha(ImageChops.multiply(strip.getchannel('A'), mk))
        bg.alpha_composite(_shadowed(strip, alpha=80), (m - 60, y0 - 60))
        C = _round(pot2, cw, h + 80, 24); fr = Image.new('RGBA', (cw + 12, h + 92), (0, 0, 0, 0)); ImageDraw.Draw(fr).rounded_rectangle([0, 0, cw + 11, h + 91], 28, fill=GOLD + (255,)); fr.alpha_composite(C, (6, 6))
        bg.alpha_composite(_shadowed(fr, alpha=130), (m + 352 + 6 - 60, y0 - 46 - 60))
    elif n == 6:  # C3：全景接黑色底，KV 底部轉黑，無縫接白色區
        y0, h = 650, 380; ws = [372, 444, 372]; x = 0
        band = Image.new('RGBA', (W, HH - y0 - 190), INK + (255,)); bg.alpha_composite(band, (0, y0 + 190))
        for im, w in zip([bento, pot2, buf], ws):
            t = _round(im, w, h, 18); bg.alpha_composite(t, (x, y0)); x += w + 6
        d = ImageDraw.Draw(bg); d.line([(0, y0 + 190), (W, y0 + 190)], fill=INK, width=1)
    tab = Image.new('RGBA', (84, 270), INK + (255,)); td = ImageDraw.Draw(tab); fv = f_cjk(30)
    for i, ch_ in enumerate('雙十一限定'): td.text(((84 - td.textlength(ch_, font=fv)) / 2, 20 + i * 47), ch_, font=fv, fill=GOLD_L)
    bg.alpha_composite(tab, (W - 84, 110))
    d = ImageDraw.Draw(bg); fp = f_cjk(32); pill = '2026.11.11 至 11.17　優惠碼 DOUBLE11'
    pw = d.textlength(pill, font=fp) + 72; x0 = (W - pw) / 2; y0 = 1112
    if not pill_on: return bg.convert('RGB').crop((0, 0, W, 1210 if n == 5 else 1100))
    if n == 6: d.rounded_rectangle([x0, y0, x0 + pw, y0 + 64], 32, outline=GOLD, width=3); d.text((x0 + 36, y0 + 10), pill, font=fp, fill=GOLD_L)
    else: d.rounded_rectangle([x0, y0, x0 + pw, y0 + 64], 32, fill=INK); d.text((x0 + 36, y0 + 10), pill, font=fp, fill=GOLD_L)
    return bg.convert('RGB')

if __name__ == '__main__' and os.environ.get('DESIGNS'):
    for n in (4, 5, 6):
        kv_design(n).save(os.path.join(H, 'img', f'kv-c{n - 3}.jpg'), quality=86, optimize=True, progressive=True)
    for n in (4, 5, 6):
        kv_design(n, False).save(os.path.join(H, 'img', f'kv-c{n - 3}-np.jpg'), quality=86, optimize=True, progressive=True)
    print('designs ok')
elif __name__ == '__main__':
    k = kv_square(); k.save(os.path.join(H, 'img', 'd11-kv.jpg'), quality=86, optimize=True, progressive=True)
    r = rewards_img(); r.save(os.path.join(H, 'img', 'd11-rewards.jpg'), quality=86, optimize=True, progressive=True)
    k.resize((600, 600)).save('/sessions/great-festive-darwin/mnt/outputs/k.jpg', quality=85)
    r.resize((600, 850)).save('/sessions/great-festive-darwin/mnt/outputs/r.jpg', quality=85)
    print('ok')
