# -*- coding: utf-8 -*-
"""雙 11 KV 方案比較：3 款 11.11 字體設計 × 3 款贈品卡
輸出 img/kv-opt-1.jpg、kv-opt-2.jpg、kv-opt-3.jpg 及 kv-options-v2.html"""
import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageChops
H = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src') + '/'
W, HH = 1200, 1600
CJK = '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
CJKR = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
POPB = '/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf'
LORA_I = '/usr/share/fonts/truetype/google-fonts/Lora-Italic-Variable.ttf'
LATO_T = '/usr/share/fonts/truetype/lato/Lato-Thin.ttf'
LATO_BI = '/usr/share/fonts/truetype/lato/Lato-BlackItalic.ttf'
LATO_B = '/usr/share/fonts/truetype/lato/Lato-Black.ttf'
def f_cjk(s, bold=True): return ImageFont.truetype(CJK if bold else CJKR, s, index=4)
GOLD_D, GOLD, GOLD_L, INK, RED = (150, 108, 38), (200, 162, 74), (240, 214, 150), (26, 26, 26), (176, 52, 38)
def lerp(a, b, t): return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))
def layer(): return Image.new('RGBA', (W, HH), (0, 0, 0, 0))

def background():
    bg = Image.new('RGB', (W, HH)); dd = ImageDraw.Draw(bg)
    top, mid, bot = (253, 248, 239), (243, 226, 196), (226, 198, 150)
    for y in range(HH):
        t = y / HH
        dd.line([(0, y), (W, y)], fill=lerp(top, mid, t / .62) if t < .62 else lerp(mid, bot, (t - .62) / .38))
    bg = bg.convert('RGBA')
    beams = layer(); d = ImageDraw.Draw(beams)
    for x0, w, a in [(-200, 160, 70), (180, 90, 55), (760, 220, 60), (1040, 80, 45)]:
        d.polygon([(x0, 0), (x0 + w, 0), (x0 + w + 520, HH), (x0 + 520, HH)], fill=(255, 255, 255, a))
    bg = Image.alpha_composite(bg, beams.filter(ImageFilter.GaussianBlur(28)))
    g = Image.new('RGBA', (W, HH), (255, 252, 244, 0)); m = Image.new('L', (W, HH), 0)
    ImageDraw.Draw(m).ellipse([600 - 430, 1000 - 430, 600 + 430, 1000 + 430], fill=235)
    g.putalpha(m.filter(ImageFilter.GaussianBlur(190))); bg = Image.alpha_composite(bg, g)
    SY = 1225; st = layer(); sd = ImageDraw.Draw(st)
    for y in range(SY, HH):
        sd.line([(0, y), (W, y)], fill=lerp((250, 240, 222), (232, 208, 166), (y - SY) / (HH - SY)) + (255,))
    bg = Image.alpha_composite(bg, st); ImageDraw.Draw(bg).line([(0, SY), (W, SY)], fill=GOLD + (255,), width=3)
    hl = layer(); ImageDraw.Draw(hl).rectangle([0, SY + 3, W, SY + 26], fill=(255, 255, 255, 120))
    return Image.alpha_composite(bg, hl.filter(ImageFilter.GaussianBlur(6)))

def grad_fill(mask, y0, y1, stops):
    g = Image.new('RGBA', (W, HH)); d = ImageDraw.Draw(g)
    for y in range(HH):
        t = min(max((y - y0) / max(y1 - y0, 1), 0), 1)
        c = lerp(stops[0], stops[1], t / .5) if t < .5 else lerp(stops[1], stops[2], (t - .5) / .5)
        d.line([(0, y), (W, y)], fill=c + (255,))
    g.putalpha(mask); return g

def centered(font, txt, top):
    bb = font.getbbox(txt); return (W - (bb[2] - bb[0])) // 2 - bb[0], top - bb[1], bb

# ---------- 11.11 三款 ----------
def title_1(bg):  # 古典襯線：Lora 粗斜體＋金漸變＋細陰影＋英文小標
    f = ImageFont.truetype(LORA_I, 300); f.set_variation_by_name(b'Bold Italic')
    tx, ty, bb = centered(f, '11.11', 70)
    sh = layer(); ImageDraw.Draw(sh).text((tx + 8, ty + 14), '11.11', font=f, fill=(110, 75, 25, 110))
    bg = Image.alpha_composite(bg, sh.filter(ImageFilter.GaussianBlur(10)))
    m = Image.new('L', (W, HH), 0); ImageDraw.Draw(m).text((tx, ty), '11.11', font=f, fill=255)
    bg = Image.alpha_composite(bg, grad_fill(m, 70, 70 + bb[3] - bb[1], [GOLD_L, GOLD, GOLD_D]))
    fs = ImageFont.truetype(POPB, 26); d = ImageDraw.Draw(bg); s = 'D O U B L E   E L E V E N   ·   2 0 2 6'
    d.text(((W - d.textlength(s, font=fs)) / 2, 34), s, font=fs, fill=GOLD_D)
    return bg

def title_2(bg):  # 幼身極簡：Lato Thin 超大字，金色＋柔光
    f = ImageFont.truetype(LATO_T, 360)
    tx, ty, bb = centered(f, '11.11', 40)
    gl = layer(); ImageDraw.Draw(gl).text((tx, ty), '11.11', font=f, fill=(255, 255, 255, 255))
    bg = Image.alpha_composite(bg, gl.filter(ImageFilter.GaussianBlur(12)))
    d = ImageDraw.Draw(bg)
    for dx in (0, 1, 2): d.text((tx + dx, ty), '11.11', font=f, fill=GOLD_D)
    fs = ImageFont.truetype(POPB, 24); s = 'D O U B L E   E L E V E N'
    d.text(((W - d.textlength(s, font=fs)) / 2, 372), s, font=fs, fill=INK)
    return bg

def title_3(bg):  # 粗體雙層：Lato 黑斜體，黑字＋金色錯位描邊
    f = ImageFont.truetype(LATO_BI, 320)
    tx, ty, bb = centered(f, '11.11', 60)
    d = ImageDraw.Draw(bg)
    d.text((tx + 16, ty + 14), '11.11', font=f, fill=(0, 0, 0, 0), stroke_width=5, stroke_fill=GOLD)
    sh = layer(); ImageDraw.Draw(sh).text((tx + 6, ty + 18), '11.11', font=f, fill=(60, 40, 10, 90))
    bg = Image.alpha_composite(bg, sh.filter(ImageFilter.GaussianBlur(14)))
    d = ImageDraw.Draw(bg); d.text((tx, ty), '11.11', font=f, fill=INK)
    m = Image.new('L', (W, HH), 0); ImageDraw.Draw(m).text((tx, ty), '11.11', font=f, fill=255)
    hi = Image.new('RGBA', (W, HH), (0, 0, 0, 0)); ImageDraw.Draw(hi).rectangle([0, ty + bb[1], W, ty + bb[1] + 12], fill=GOLD + (255,))
    hi.putalpha(ImageChops.multiply(hi.getchannel('A'), m))
    return Image.alpha_composite(bg, hi)

def headline(bg):
    d = ImageDraw.Draw(bg)
    def line(parts, font, y):
        total = sum(d.textlength(p, font=font) for p, _ in parts); x = (W - total) / 2
        for p, c in parts:
            d.text((x + 3, y + 4), p, font=font, fill=(255, 255, 255)); d.text((x, y), p, font=font, fill=c); x += d.textlength(p, font=font)
    line([('一連七天', INK)], f_cjk(120), 418)
    line([('全網所有套餐及單點 ', INK), ('11% OFF', RED)], f_cjk(62), 590)
    fs = f_cjk(32); sub = '雙 11 網站下單限定・滿 HK$1,500 再送人氣小食'
    d.text(((W - d.textlength(sub, font=fs)) / 2, 690), sub, font=fs, fill=(107, 90, 63))
    return bg

def hero(bg):
    pot = Image.open(SRC + 'd11src-c3.jpg').convert('RGBA')
    cx, cy, r = 890, 1045, 530
    pot = pot.crop((cx - r, cy - r, cx + r, cy + r)).resize((560, 560), Image.LANCZOS)
    m = Image.new('L', (2240, 2240), 0); ImageDraw.Draw(m).ellipse([0, 0, 2239, 2239], fill=255); pot.putalpha(m.resize((560, 560), Image.LANCZOS))
    PX, PY = 320, 800
    sh = layer(); ImageDraw.Draw(sh).ellipse([PX + 40, PY + 500, PX + 520, PY + 600], fill=(80, 55, 20, 150))
    bg = Image.alpha_composite(bg, sh.filter(ImageFilter.GaussianBlur(26)))
    rg = layer(); dr = ImageDraw.Draw(rg)
    dr.ellipse([PX - 14, PY - 14, PX + 574, PY + 574], fill=(255, 255, 255, 255)); dr.ellipse([PX - 14, PY - 14, PX + 574, PY + 574], outline=GOLD + (255,), width=4)
    bg = Image.alpha_composite(bg, rg); bg.alpha_composite(pot, (PX, PY))
    refl = pot.transpose(Image.FLIP_TOP_BOTTOM).crop((0, 0, 560, 140)); fade = Image.new('L', (560, 140))
    for yy in range(140): ImageDraw.Draw(fade).line([(0, yy), (560, yy)], fill=int(70 * (1 - yy / 140)))
    refl.putalpha(ImageChops.multiply(refl.getchannel('A'), fade)); bg.alpha_composite(refl, (PX, PY + 576))
    return bg

# ---------- 贈品卡三款 ----------
GIFTS = [('d11src-g1.png', (90, 90, 1042, 640), '日式雞皮餃子', '1,500', '送'),
         ('d11src-g2.jpg', (40, 60, 1024, 630), '蜜蜜燒雞翼', '2,200', '再加送'),
         ('d11src-g3.png', (100, 90, 1042, 640), '避風塘海鮮豆腐', '3,000', '再加送')]
def photo(src, crop, w):
    im = Image.open(SRC + src).convert('RGB').crop(crop)
    im = im.resize((w, int(w * im.height / im.width)), Image.LANCZOS).convert('RGBA')
    m = Image.new('L', im.size, 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, im.width - 1, im.height - 1], 14, fill=255); im.putalpha(m); return im
def base(cw, ch, M=0):
    c = Image.new('RGBA', (cw + 2 * M, ch + 2 * M), (0, 0, 0, 0))
    mk = Image.new('L', c.size, 0); ImageDraw.Draw(mk).rounded_rectangle([M, M, M + cw - 1, M + ch - 1], 22, fill=255)
    b = Image.new('RGBA', c.size, (255, 255, 255, 255)); b.putalpha(mk); c.alpha_composite(b); return c

def card_1(src, crop, name, amt, verb, w):   # 角標價牌：圖左上金色價牌
    im = photo(src, crop, w); pad = 14; cw, ch = w + 2 * pad, im.height + 2 * pad + 92
    c = base(cw, ch); c.alpha_composite(im, (pad, pad)); d = ImageDraw.Draw(c)
    tag = Image.new('RGBA', (170, 92), (0, 0, 0, 0)); td = ImageDraw.Draw(tag)
    td.rounded_rectangle([0, 0, 169, 91], 14, fill=GOLD)
    td.text((14, 6), '滿', font=f_cjk(24), fill=INK); td.text((14, 30), '$' + amt, font=ImageFont.truetype(POPB, 40), fill=INK)
    c.alpha_composite(tag, (pad - 4, pad - 4))
    fv = f_cjk(22, False); fn = f_cjk(30); y = im.height + pad + 8
    d.text(((cw - d.textlength(verb, font=fv)) / 2, y), verb, font=fv, fill=GOLD_D)
    d.text(((cw - d.textlength(name, font=fn)) / 2, y + 32), name, font=fn, fill=INK)
    return c

def card_2(src, crop, name, amt, verb, w):   # 雙欄底部：左金額、右贈品
    im = photo(src, crop, w); pad = 14; cw, ch = w + 2 * pad, im.height + 2 * pad + 96
    c = base(cw, ch); c.alpha_composite(im, (pad, pad)); d = ImageDraw.Draw(c)
    y0 = im.height + pad + 12; colw = 112
    d.text((pad + 4, y0), '消費滿', font=f_cjk(20, False), fill=(140, 125, 100))
    d.text((pad + 2, y0 + 26), '$' + amt, font=ImageFont.truetype(POPB, 34), fill=GOLD_D)
    d.line([(pad + colw, y0 + 4), (pad + colw, y0 + 76)], fill=(226, 212, 186), width=2)
    d.text((pad + colw + 14, y0), verb, font=f_cjk(20, False), fill=(140, 125, 100))
    fn = f_cjk(25); lines = [name] if len(name) <= 5 else [name[:3], name[3:]]
    for k, ln in enumerate(lines): d.text((pad + colw + 14, y0 + 26 + k * 32), ln, font=fn, fill=INK)
    return c

def card_3(src, crop, name, amt, verb, w, side='R'):   # 圓章：卡外側頂角黑金圓章
    M = 46; im = photo(src, crop, w); pad = 14; cw, ch = w + 2 * pad, im.height + 2 * pad + 62
    c = base(cw, ch, M); c.alpha_composite(im, (M + pad, M + pad)); d = ImageDraw.Draw(c)
    R = 60; cx, cy = (M + cw - 6, M + 6) if side == 'R' else (M + 6, M + 6)
    d.ellipse([cx - R, cy - R, cx + R, cy + R], fill=INK); d.ellipse([cx - R + 7, cy - R + 7, cx + R - 7, cy + R - 7], outline=GOLD, width=3)
    f1 = f_cjk(20); f2 = ImageFont.truetype(POPB, 26)
    d.text((cx - d.textlength('滿', font=f1) / 2, cy - 38), '滿', font=f1, fill=GOLD_L)
    d.text((cx - d.textlength('$' + amt, font=f2) / 2, cy - 12), '$' + amt, font=f2, fill=(255, 255, 255))
    fn = f_cjk(30); tg = verb; tw = d.textlength(tg, font=f_cjk(24)); nw = d.textlength(name, font=fn)
    x = M + (cw - (tw + 22 + nw)) / 2; y = M + im.height + pad + 12
    d.rounded_rectangle([x - 6, y + 4, x + tw + 8, y + 42], 10, fill=GOLD); d.text((x + 1, y + 6), tg, font=f_cjk(24), fill=(255, 255, 255))
    d.text((x + tw + 22, y), name, font=fn, fill=INK)
    return c

def float_card(c, rot):
    c = c.rotate(rot, resample=Image.BICUBIC, expand=True)
    s = Image.new('RGBA', (c.width + 80, c.height + 80), (0, 0, 0, 0))
    s.paste((70, 45, 15, 110), (50, 62), c.getchannel('A')); s = s.filter(ImageFilter.GaussianBlur(16)); s.alpha_composite(c, (40, 40)); return s

POS = [((50, 770), 7, 260), ((848, 735), -6, 250), ((830, 1080), 4, 250)]
def cards(bg, fn):
    for (g, (pos, rot, w)) in zip(GIFTS, POS):
        c = float_card(fn(*g, w, side=('L' if pos[0] < 600 else 'R')) if fn is card_3 else fn(*g, w), rot)
        off = 46 if fn is card_3 else 0
        x = pos[0] - off - (60 if (fn is card_3 and pos[0] > 600) else 0)
        bg.alpha_composite(c, (x, pos[1] - off))
    return bg

def tab_and_pill(bg):
    tab = Image.new('RGBA', (92, 300), INK + (255,)); td = ImageDraw.Draw(tab); fv = f_cjk(34)
    for i, ch_ in enumerate('雙十一限定'): td.text(((92 - td.textlength(ch_, font=fv)) / 2, 22 + i * 52), ch_, font=fv, fill=GOLD_L)
    bg.alpha_composite(tab, (W - 92, 120))
    d = ImageDraw.Draw(bg); fp = f_cjk(36); pill = '2026.11.11 至 11.17　優惠碼 D11A／D11B'
    pw = d.textlength(pill, font=fp) + 80; x0 = (W - pw) / 2; y0 = 1490
    d.rounded_rectangle([x0, y0, x0 + pw, y0 + 74], 37, fill=INK); d.text((x0 + 40, y0 + 12), pill, font=fp, fill=GOLD_L)
    return bg

def render(tfn, cfn, out):
    bg = background(); bg = tfn(bg); bg = headline(bg); bg = hero(bg); bg = cards(bg, cfn); bg = tab_and_pill(bg)
    im = bg.convert('RGB'); im.save(out, quality=86, optimize=True, progressive=True); return im

if __name__ == '__main__':
    os.makedirs(os.path.join(H, 'img'), exist_ok=True)
    for i, (t, c) in enumerate([(title_1, card_1), (title_2, card_2), (title_3, card_3)], 1):
        render(t, c, os.path.join(H, 'img', f'kv-opt-{i}.jpg'))
    print('ok')
