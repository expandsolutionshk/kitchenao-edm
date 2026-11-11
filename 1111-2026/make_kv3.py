# -*- coding: utf-8 -*-
"""雙 11 KV v3：方案 3 字體＋兩張完整產品主圖＋四重賞贈品列（圓章完整）
來源圖：/tmp/kv（網站下載＋客戶提供餐盒相 bento.jpg）；輸出 img/d11-kv.jpg"""
import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageChops
H = os.path.dirname(os.path.abspath(__file__))
SRC = '/tmp/kv/'
W, HH = 1200, 3160
CJK = '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
CJKR = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
POPB = '/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf'
LATO_BI = '/usr/share/fonts/truetype/lato/Lato-BlackItalic.ttf'
def f_cjk(s, bold=True): return ImageFont.truetype(CJK if bold else CJKR, s, index=4)
def f_pop(s): return ImageFont.truetype(POPB, s)
GOLD_D, GOLD, GOLD_L, INK, RED = (150, 108, 38), (200, 162, 74), (240, 214, 150), (26, 26, 26), (176, 52, 38)
def lerp(a, b, t): return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))
def layer(): return Image.new('RGBA', (W, HH), (0, 0, 0, 0))
SY = 1250

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
    ImageDraw.Draw(m).ellipse([600 - 520, 1010 - 360, 600 + 520, 1010 + 360], fill=235)
    g.putalpha(m.filter(ImageFilter.GaussianBlur(170))); bg = Image.alpha_composite(bg, g)
    st = layer(); sd = ImageDraw.Draw(st)
    for y in range(SY, HH):
        sd.line([(0, y), (W, y)], fill=lerp((250, 240, 222), (232, 208, 166), (y - SY) / (HH - SY)) + (255,))
    bg = Image.alpha_composite(bg, st); ImageDraw.Draw(bg).line([(0, SY), (W, SY)], fill=GOLD + (255,), width=3)
    hl = layer(); ImageDraw.Draw(hl).rectangle([0, SY + 3, W, SY + 26], fill=(255, 255, 255, 120))
    return Image.alpha_composite(bg, hl.filter(ImageFilter.GaussianBlur(6)))

def title(bg):  # 方案 3：粗體雙層
    f = ImageFont.truetype(LATO_BI, 320); bb = f.getbbox('11.11')
    tx, ty = (W - (bb[2] - bb[0])) // 2 - bb[0], 60 - bb[1]
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
    line(d, [('一連七天', INK)], f_cjk(120), 410)
    line(d, [('滿 HK$1,100 ', INK), ('全網 11% OFF', RED)], f_cjk(64), 580)
    fs = f_cjk(32); sub = '滿 HK$1,500 起再送人氣小食，最多送 3 款'
    d.text(((W - d.textlength(sub, font=fs)) / 2, 682), sub, font=fs, fill=(107, 90, 63))
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
        put(bg, tile(bento, 290, 390, rot=0), 40, 800)
        put(bg, tile(buf, 290, 390, rot=0), 870, 800)
        put(bg, tile(pot2, 440, 440, rot=0), 380, 760)
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
def _float(c, rot, blur=12, off=(8, 14), alpha=95):
    c = c.rotate(rot, resample=Image.BICUBIC, expand=True)
    s = Image.new('RGBA', (c.width + 50, c.height + 50), (0, 0, 0, 0))
    s.paste((70, 45, 15, alpha), (25 + off[0], 25 + off[1]), c.getchannel('A')); s = s.filter(ImageFilter.GaussianBlur(blur)); s.alpha_composite(c, (25, 25)); return s
TIER = [  # (第幾賞, 金額, 後排, 前卡, 動詞, 總結)
 ('第一賞', '1,100', [], 'off', '全單', '全網所有套餐及單點即減 11%'),
 ('第二賞', '1,500', ['off'], 'a1600', '送', '11% OFF＋送 1 款小食・總值 $198'),
 ('第三賞', '2,200', ['off', 'a1600'], 'a1500', '再加送', '11% OFF＋送 2 款小食・總值 $376'),
 ('第四賞', '3,000', ['off', 'a1600', 'a1500'], 'a0500', '再加送', '11% OFF＋送 3 款小食・總值 $564'),
]
BACK_POS = {0: [], 1: [(-120, 10, -7)], 2: [(-150, 20, -9), (150, 20, 9)], 3: [(-160, 40, -10), (0, 0, 0), (160, 40, 10)]}
PW, PH = 560, 700
def panel(lv, amt, backs, front, verb, summ):
    p = Image.new('RGBA', (PW, PH + 80), (0, 0, 0, 0)); T = 80
    mk = Image.new('L', p.size, 0); ImageDraw.Draw(mk).rounded_rectangle([0, T, PW - 1, T + PH - 1], 28, fill=255)
    b = Image.new('RGBA', p.size, (255, 255, 255, 235)); b.putalpha(ImageChops.multiply(mk, Image.new('L', p.size, 235))); p.alpha_composite(b)
    ImageDraw.Draw(p).rounded_rectangle([2, T + 2, PW - 3, T + PH - 3], 26, outline=GOLD, width=2)
    cx = PW // 2; top = T + 140
    for key, (dx, dy, r) in zip(backs, BACK_POS[len(backs)]):
        c = _float(back_card(key), r); p.alpha_composite(c, (int(cx + dx - c.width / 2), top + dy - 25))
    fy = top + (150 if backs else 30)
    c = _float(front_card(front, verb, 270 if backs else 320), 0, 16, (10, 18), 120); p.alpha_composite(c, (int(cx - c.width / 2), fy - 25))
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
ROW_Y = [1440, 2240]
def rewards(bg):
    d = ImageDraw.Draw(bg)
    fe = f_pop(22); s = 'F O U R   R E W A R D S'
    d.text(((W - d.textlength(s, font=fe)) / 2, 1318), s, font=fe, fill=GOLD_D)
    line(d, [('雙 11 四重賞', INK)], f_cjk(56), 1350, sh=False)
    pos = [(24, ROW_Y[0]), (616, ROW_Y[0]), (24, ROW_Y[1]), (616, ROW_Y[1])]
    for t, (x, y) in zip(TIER, pos):
        p = panel(*t); sh = Image.new('RGBA', (p.width + 60, p.height + 60), (0, 0, 0, 0))
        sh.paste((70, 45, 15, 70), (36, 46), p.getchannel('A')); sh = sh.filter(ImageFilter.GaussianBlur(16)); sh.alpha_composite(p, (30, 30))
        bg.alpha_composite(sh, (x - 30, y - 30))
    return bg

def tab_and_pill(bg):
    tab = Image.new('RGBA', (92, 300), INK + (255,)); td = ImageDraw.Draw(tab); fv = f_cjk(34)
    for i, ch_ in enumerate('雙十一限定'): td.text(((92 - td.textlength(ch_, font=fv)) / 2, 22 + i * 52), ch_, font=fv, fill=GOLD_L)
    bg.alpha_composite(tab, (W - 92, 120))
    d = ImageDraw.Draw(bg); fp = f_cjk(36); pill = '2026.11.11 至 11.17　優惠碼 DOUBLE11'
    pw = d.textlength(pill, font=fp) + 80; x0 = (W - pw) / 2; y0 = 3050
    d.rounded_rectangle([x0, y0, x0 + pw, y0 + 74], 37, fill=INK); d.text((x0 + 40, y0 + 12), pill, font=fp, fill=GOLD_L)
    return bg

if __name__ == '__main__':
    bg = background(); bg = title(bg); bg = headline(bg); bg = heroes(bg); bg = rewards(bg); bg = tab_and_pill(bg)
    im = bg.convert('RGB'); im.save(os.path.join(H, 'img', f'kv-hero-{HERO_MODE}.jpg'), quality=86, optimize=True, progressive=True)
    im.save(os.path.join(H, 'img', 'd11-kv.jpg'), quality=86, optimize=True, progressive=True)
    im.resize((600, 1580)).save('/sessions/great-festive-darwin/mnt/outputs/kv4.jpg', quality=85)
    print('ok', os.path.getsize(os.path.join(H, 'img', 'd11-kv.jpg')) // 1024, 'KB')
