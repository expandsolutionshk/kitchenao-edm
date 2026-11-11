# -*- coding: utf-8 -*-
"""雙 11 KV：參考 Kimpton 餐廳頁風格（全出血相片、直角、窄身大寫標題、大量留白）
三個 option：K1 全出血主圖 / K2 上相下字 / K3 雜誌格。來源相在 src/，輸出 img/kv-k1~3.jpg"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter
H = os.path.dirname(os.path.abspath(__file__)); SRC = os.path.join(H, 'src') + '/'
W = HH = 1200
CJK = '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
CJKR = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
NAR = '/usr/share/fonts/opentype/urw-base35/NimbusSansNarrow-Bold.otf'
NARR = '/usr/share/fonts/opentype/urw-base35/NimbusSansNarrow-Regular.otf'
def cjk(s, b=True): return ImageFont.truetype(CJK if b else CJKR, s, index=4)
INK, GOLD, CREAM, RED = (40, 37, 43), (200, 162, 74), (246, 242, 236), (176, 52, 38)

def grade(im):  # 統一色調：略暗、暖、降飽和、加對比
    im = im.convert('RGB')
    im = ImageEnhance.Color(im).enhance(.88); im = ImageEnhance.Brightness(im).enhance(.9); im = ImageEnhance.Contrast(im).enhance(1.08)
    warm = Image.new('RGB', im.size, (255, 236, 212)); return Image.blend(im, Image.composite(im, warm, Image.new('L', im.size, 200)), .35)
def fit(im, w, h):
    r = w / h
    if im.width / im.height > r: nw = int(im.height * r); x = (im.width - nw) // 2; im = im.crop((x, 0, x + nw, im.height))
    else: nh = int(im.width / r); y = (im.height - nh) // 2; im = im.crop((0, y, im.width, y + nh))
    return im.resize((w, h), Image.LANCZOS)
def photos():
    pot = Image.open(SRC + 'pot1024.jpg'); bento = Image.open(SRC + 'bento.jpg').crop((0, 160, 1200, 1600))
    buf = Image.open(SRC + 'photo3.jpg').crop((0, 820, 1920, 2560))
    return grade(pot), grade(bento), grade(buf)
def spaced(d, xy, t, f, fill, sp, anchor='l'):
    w = sum(d.textlength(c, font=f) for c in t) + sp * (len(t) - 1); x, y = xy
    if anchor == 'c': x -= w / 2
    for c in t: d.text((x, y), c, font=f, fill=fill); x += d.textlength(c, font=f) + sp
    return w
def ctext(d, y, t, f, fill): d.text(((W - d.textlength(t, font=f)) / 2, y), t, font=f, fill=fill)

def k1():  # 全出血主圖，白字壓相，底部漸黑
    pot, _, _ = photos(); bg = fit(pot, W, HH).convert('RGBA')
    g = Image.new('RGBA', (W, HH)); gd = ImageDraw.Draw(g)
    for y in range(HH):
        t = y / HH; a = int(150 * (1 - t / .35)) if t < .35 else (0 if t < .45 else int(225 * min(1, (t - .45) / .4)))
        gd.line([(0, y), (W, y)], fill=(18, 14, 12, max(0, a)))
    bg.alpha_composite(g); d = ImageDraw.Draw(bg)
    spaced(d, (W / 2, 70), 'DOUBLE ELEVEN · 2026', ImageFont.truetype(NARR, 30), (240, 228, 205), 6, 'c')
    f = ImageFont.truetype(NAR, 300); ctext(d, 100, '11.11', f, (255, 255, 255))
    ctext(d, 820, '一連七天', cjk(96), (255, 255, 255))
    t1, t2 = '滿 HK$1,100 全網 ', '11% OFF'; f2 = cjk(52); w = d.textlength(t1 + t2, font=f2); x = (W - w) / 2
    d.text((x, 952), t1, font=f2, fill=(255, 255, 255)); d.text((x + d.textlength(t1, font=f2), 952), t2, font=f2, fill=(228, 199, 126))
    ctext(d, 1040, '滿 HK$1,500 起再送人氣小食，最多送 3 款', cjk(28, False), (236, 226, 210))
    d.line([(W / 2 - 40, 1110), (W / 2 + 40, 1110)], fill=GOLD, width=3)
    return bg.convert('RGB')

def k2():  # 上相下字：三張相直角拼成全闊，下面白底窄身大字
    pot, bento, buf = photos(); bg = Image.new('RGB', (W, HH), (255, 255, 255)); ph = 660
    for im, x, w in [(bento, 0, 396), (pot, 400, 400), (buf, 804, 396)]: bg.paste(fit(im, w, ph), (x, 0))
    d = ImageDraw.Draw(bg); L = 80
    spaced(d, (L, ph + 60), 'DOUBLE ELEVEN · 2026', ImageFont.truetype(NARR, 28), (120, 112, 104), 6)
    d.text((L - 6, ph + 80), '11.11', font=ImageFont.truetype(NAR, 230), fill=INK)
    x2 = 640; d.line([(x2 - 40, ph + 110), (x2 - 40, ph + 440)], fill=(220, 214, 205), width=2)
    d.text((x2, ph + 104), '一連七天', font=cjk(84), fill=INK)
    d.text((x2, ph + 230), '滿 HK$1,100', font=cjk(46), fill=INK)
    d.text((x2, ph + 290), '全網 11% OFF', font=cjk(46), fill=RED)
    d.text((x2, ph + 372), '滿 HK$1,500 起再送人氣小食', font=cjk(26, False), fill=(110, 102, 96))
    d.text((x2, ph + 408), '最多送 3 款', font=cjk(26, False), fill=(110, 102, 96))
    return bg

def k3():  # 雜誌格：左大直圖，右邊米色字欄＋兩張細圖
    pot, bento, buf = photos(); bg = Image.new('RGB', (W, HH), CREAM)
    bg.paste(fit(pot, 640, HH), (0, 0)); d = ImageDraw.Draw(bg); x = 690
    spaced(d, (x, 70), 'DOUBLE ELEVEN', ImageFont.truetype(NARR, 28), (120, 112, 104), 6)
    d.text((x - 4, 96), '11.11', font=ImageFont.truetype(NAR, 200), fill=INK)
    d.line([(x, 330), (x + 60, 330)], fill=GOLD, width=3)
    d.text((x, 360), '一連七天', font=cjk(76), fill=INK)
    d.text((x, 470), '滿 HK$1,100', font=cjk(42), fill=INK); d.text((x, 524), '全網 11% OFF', font=cjk(42), fill=RED)
    d.text((x, 600), '滿 HK$1,500 起再送人氣小食', font=cjk(24, False), fill=(110, 102, 96))
    d.text((x, 634), '最多送 3 款', font=cjk(24, False), fill=(110, 102, 96))
    bg.paste(fit(bento, 245, 400), (690, 740)); bg.paste(fit(buf, 245, 400), (945, 740))
    return bg

if __name__ == '__main__':
    for i, fn in enumerate([k1, k2, k3], 1):
        fn().save(os.path.join(H, 'img', f'kv-k{i}.jpg'), quality=86, optimize=True, progressive=True)
    print('ok')
