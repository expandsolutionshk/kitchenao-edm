# -*- coding: utf-8 -*-
"""雙 11 KV v3：方案 3 字體＋兩張完整產品主圖＋四重賞贈品列（圓章完整）
來源圖：/tmp/kv（網站下載＋客戶提供餐盒相 bento.jpg）；輸出 img/d11-kv.jpg"""
import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageChops
H = os.path.dirname(os.path.abspath(__file__))
SRC = '/tmp/kv/'
W, HH = 1200, 1920
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

def heroes(bg):
    pot = Image.open(SRC + 'd11src-c3.jpg').convert('RGB').crop((120, 585, 1600, 1600))     # 完整煲仔飯（去掉酒樽）
    bento = Image.open(SRC + 'bento.jpg').convert('RGB').crop((0, 160, 1200, 1600))         # 精緻餐盒
    b = framed(bento, 300, 4); p = framed(pot, 610, -3)
    bg.alpha_composite(b, (735, 705))
    bg.alpha_composite(p, (30, 745))
    return bg

GIFTS = [(None, '全單 11% OFF', '1,100', '第一賞'),
         (('d11src-g1.png', (90, 90, 1042, 640)), '日式雞皮餃子', '1,500', '第二賞'),
         (('d11src-g2.jpg', (40, 60, 1024, 630)), '蜜蜜燒雞翼', '2,200', '第三賞'),
         (('d11src-g3.png', (100, 90, 1042, 640)), '避風塘海鮮豆腐', '3,000', '第四賞')]
def gift_card(src, name, amt, lvl, w=228):
    M = 64; pad = 12; ih = int(w * 0.62); cw, ch = w + 2 * pad, ih + 2 * pad + 132
    c = Image.new('RGBA', (cw + 2 * M, ch + 2 * M), (0, 0, 0, 0))
    mk = Image.new('L', c.size, 0); ImageDraw.Draw(mk).rounded_rectangle([M, M, M + cw - 1, M + ch - 1], 22, fill=255)
    body = Image.new('RGBA', c.size, (255, 255, 255, 255)); body.putalpha(mk); c.alpha_composite(body)
    d = ImageDraw.Draw(c)
    if src:
        im = Image.open(SRC + src[0]).convert('RGB').crop(src[1])
        r = im.width / im.height; tw = w; th = int(tw / r)
        im = im.resize((tw, th), Image.LANCZOS)
        top = max(0, (th - ih) // 2); im = im.crop((0, top, w, top + ih)).convert('RGBA')
        m = Image.new('L', im.size, 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, w - 1, ih - 1], 14, fill=255); im.putalpha(m)
        c.alpha_composite(im, (M + pad, M + pad + 40))
        verb = '送' if amt == '1,500' else '再加送'
    else:
        d.rounded_rectangle([M + pad, M + pad + 40, M + pad + w - 1, M + pad + 40 + ih - 1], 14, fill=INK)
        f1 = f_pop(64); t = '11%'; d.text((M + pad + (w - d.textlength(t, font=f1)) / 2, M + pad + 50), t, font=f1, fill=GOLD_L)
        f2 = f_pop(34); t = 'OFF'; d.text((M + pad + (w - d.textlength(t, font=f2)) / 2, M + pad + 126), t, font=f2, fill=(255, 255, 255))
        verb = '全單'; name = '全網 11% OFF'
    y = M + ih + pad + 50
    fl = f_cjk(18, False); d.text((M + (cw - d.textlength(lvl, font=fl)) / 2, y), lvl, font=fl, fill=GOLD_D)
    fv = f_cjk(22); fn = f_cjk(26 if len(name) <= 6 else 23)
    tw = d.textlength(verb, font=fv); nw = d.textlength(name, font=fn)
    x = M + (cw - (tw + 16 + 12 + nw)) / 2; yy = y + 32
    d.rounded_rectangle([x - 4, yy + 2, x + tw + 12, yy + 38], 9, fill=GOLD); d.text((x + 4, yy + 3), verb, font=fv, fill=(255, 255, 255))
    d.text((x + tw + 24, yy), name, font=fn, fill=INK)
    # 完整圓章：右上角
    R = 50; cx, cy = M + cw // 2, M + 2
    d.ellipse([cx - R - 3, cy - R - 3, cx + R + 3, cy + R + 3], fill=(255, 255, 255))
    d.ellipse([cx - R, cy - R, cx + R, cy + R], fill=INK); d.ellipse([cx - R + 6, cy - R + 6, cx + R - 6, cy + R - 6], outline=GOLD, width=3)
    fa, fb = f_cjk(18), f_pop(22)
    d.text((cx - d.textlength('滿', font=fa) / 2, cy - 34), '滿', font=fa, fill=GOLD_L)
    d.text((cx - d.textlength('$' + amt, font=fb) / 2, cy - 10), '$' + amt, font=fb, fill=(255, 255, 255))
    return c, M

def rewards(bg):
    d = ImageDraw.Draw(bg)
    fe = f_pop(22); s = 'F O U R   R E W A R D S'
    d.text(((W - d.textlength(s, font=fe)) / 2, 1318), s, font=fe, fill=GOLD_D)
    line(d, [('雙 11 四重賞', INK)], f_cjk(52), 1350, sh=False)
    xs = [24, 312, 600, 888]; rots = [3, -2, 2, -3]
    for (src, name, amt, lvl), x, r in zip(GIFTS, xs, rots):
        c, M = gift_card(src, name, amt, lvl)
        c = c.rotate(r, resample=Image.BICUBIC, expand=True)
        s = Image.new('RGBA', (c.width + 60, c.height + 60), (0, 0, 0, 0))
        s.paste((70, 45, 15, 100), (40, 52), c.getchannel('A')); s = s.filter(ImageFilter.GaussianBlur(14)); s.alpha_composite(c, (30, 30))
        bg.alpha_composite(s, (x - M, 1470 - 30 - M))
    return bg

def tab_and_pill(bg):
    tab = Image.new('RGBA', (92, 300), INK + (255,)); td = ImageDraw.Draw(tab); fv = f_cjk(34)
    for i, ch_ in enumerate('雙十一限定'): td.text(((92 - td.textlength(ch_, font=fv)) / 2, 22 + i * 52), ch_, font=fv, fill=GOLD_L)
    bg.alpha_composite(tab, (W - 92, 120))
    d = ImageDraw.Draw(bg); fp = f_cjk(36); pill = '2026.11.11 至 11.17　優惠碼 DOUBLE11'
    pw = d.textlength(pill, font=fp) + 80; x0 = (W - pw) / 2; y0 = 1816
    d.rounded_rectangle([x0, y0, x0 + pw, y0 + 74], 37, fill=INK); d.text((x0 + 40, y0 + 12), pill, font=fp, fill=GOLD_L)
    return bg

if __name__ == '__main__':
    bg = background(); bg = title(bg); bg = headline(bg); bg = heroes(bg); bg = rewards(bg); bg = tab_and_pill(bg)
    im = bg.convert('RGB'); im.save(os.path.join(H, 'img', 'd11-kv.jpg'), quality=86, optimize=True, progressive=True)
    im.resize((600, 960)).save('/sessions/great-festive-darwin/mnt/outputs/kv3.jpg', quality=85)
    print('ok', os.path.getsize(os.path.join(H, 'img', 'd11-kv.jpg')) // 1024, 'KB')
