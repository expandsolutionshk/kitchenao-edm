# -*- coding: utf-8 -*-
"""雙 11 EDM Key Visual（方案 C 香檳奶油，多層次版）
來源圖放 /tmp/kv（由網站下載）；輸出 img/d11-kv.jpg（1200x1500）"""
import os, math
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageChops
H = os.path.dirname(os.path.abspath(__file__))
SRC = '/tmp/kv/'
W, HH = 1200, 1500
CJK = '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
POP = '/usr/share/fonts/truetype/google-fonts/Poppins-BoldItalic.ttf'
POPB = '/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf'
def f_cjk(s): return ImageFont.truetype(CJK, s, index=4)
GOLD_D, GOLD, GOLD_L, INK = (150, 108, 38), (200, 162, 74), (240, 214, 150), (26, 26, 26)

def lerp(a, b, t): return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

# ---------- 1. 背景：香檳漸變 ----------
bg = Image.new('RGB', (W, HH))
top, mid, bot = (253, 248, 239), (243, 226, 196), (226, 198, 150)
for y in range(HH):
    t = y / HH
    c = lerp(top, mid, t / .62) if t < .62 else lerp(mid, bot, (t - .62) / .38)
    ImageDraw.Draw(bg).line([(0, y), (W, y)], fill=c)
bg = bg.convert('RGBA')

def glow(size, center, radius, color, alpha):
    g = Image.new('RGBA', size, color + (0,))
    m = Image.new('L', size, 0)
    ImageDraw.Draw(m).ellipse([center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius], fill=alpha)
    g.putalpha(m.filter(ImageFilter.GaussianBlur(radius * .45)))
    return g

# 斜向光束（層次一）
beams = Image.new('RGBA', (W, HH), (255, 255, 255, 0))
d = ImageDraw.Draw(beams)
for x0, w, a in [(-200, 160, 70), (180, 90, 55), (760, 220, 60), (1040, 80, 45)]:
    d.polygon([(x0, 0), (x0 + w, 0), (x0 + w + 520, HH), (x0 + 520, HH)], fill=(255, 255, 255, a))
bg = Image.alpha_composite(bg, beams.filter(ImageFilter.GaussianBlur(28)))
# 主圖後光暈（層次二）
bg = Image.alpha_composite(bg, glow((W, HH), (600, 900), 430, (255, 252, 244), 235))

# 檯面：下方淺色平台＋金幼線（層次三）
stage = Image.new('RGBA', (W, HH), (0, 0, 0, 0))
sd = ImageDraw.Draw(stage)
SY = 1110
for y in range(SY, HH):
    t = (y - SY) / (HH - SY)
    sd.line([(0, y), (W, y)], fill=lerp((250, 240, 222), (232, 208, 166), t) + (255,))
bg = Image.alpha_composite(bg, stage)
d = ImageDraw.Draw(bg)
d.line([(0, SY), (W, SY)], fill=GOLD + (255,), width=3)
hl = Image.new('RGBA', (W, HH), (0, 0, 0, 0))
ImageDraw.Draw(hl).rectangle([0, SY + 3, W, SY + 26], fill=(255, 255, 255, 120))
bg = Image.alpha_composite(bg, hl.filter(ImageFilter.GaussianBlur(6)))

# ---------- 2. 11.11（金色漸變＋立體陰影） ----------
F11 = ImageFont.truetype(POP, 330)
txt = '11.11'
bb = F11.getbbox(txt); tw, th = bb[2] - bb[0], bb[3] - bb[1]
tx, ty = (W - tw) // 2 - bb[0], 70 - bb[1]
# 立體層：多次偏移
ext = Image.new('RGBA', (W, HH), (0, 0, 0, 0))
ed = ImageDraw.Draw(ext)
for i in range(16, 0, -1):
    ed.text((tx + i * .9, ty + i), txt, font=F11, fill=lerp(GOLD_D, (110, 78, 25), i / 16) + (255,))
sh = Image.new('RGBA', (W, HH), (0, 0, 0, 0))
ImageDraw.Draw(sh).text((tx + 22, ty + 34), txt, font=F11, fill=(90, 60, 20, 90))
bg = Image.alpha_composite(bg, sh.filter(ImageFilter.GaussianBlur(18)))
bg = Image.alpha_composite(bg, ext)
mask = Image.new('L', (W, HH), 0)
ImageDraw.Draw(mask).text((tx, ty), txt, font=F11, fill=255)
grad = Image.new('RGBA', (W, HH))
for y in range(HH):
    t = min(max((y - ty - bb[1]) / th, 0), 1)
    c = lerp(GOLD_L, GOLD, t / .55) if t < .55 else lerp(GOLD, GOLD_D, (t - .55) / .45)
    ImageDraw.Draw(grad).line([(0, y), (W, y)], fill=c + (255,))
grad.putalpha(mask)
bg = Image.alpha_composite(bg, grad)
# 高光幼線
hi = Image.new('RGBA', (W, HH), (0, 0, 0, 0))
ImageDraw.Draw(hi).text((tx - 2, ty - 3), txt, font=F11, fill=(255, 250, 230, 110))
hi.putalpha(ImageChops.multiply(hi.getchannel('A'), ImageChops.invert(mask.transform(mask.size, Image.AFFINE, (1, 0, 3, 0, 1, 5)))))
bg = Image.alpha_composite(bg, hi)

# ---------- 3. 標題 ----------
d = ImageDraw.Draw(bg)
FT = f_cjk(78)
parts = [('全網 ', INK), ('89 折', (176, 52, 38)), ('　滿額送小食', INK)]
total = sum(d.textlength(p, font=FT) for p, _ in parts)
x = (W - total) / 2; y = 470
for p, c in parts:
    d.text((x + 3, y + 4), p, font=FT, fill=(255, 255, 255))
    d.text((x, y), p, font=FT, fill=c); x += d.textlength(p, font=FT)
FS = f_cjk(32)
sub = '雙 11 網站下單限定・滿 HK$1,500 再送人氣小食'
d.text(((W - d.textlength(sub, font=FS)) / 2, 580), sub, font=FS, fill=(107, 90, 63))

# ---------- 4. 主圖：煲仔飯圓形（倒影＋陰影） ----------
pot = Image.open(SRC + 'd11src-c3.jpg').convert('RGBA')
cx, cy, r = 890, 1045, 530          # 原圖煲邊（1600x1600）
pot = pot.crop((cx - r, cy - r, cx + r, cy + r)).resize((560, 560), Image.LANCZOS)
m = Image.new('L', (560 * 4, 560 * 4), 0); ImageDraw.Draw(m).ellipse([0, 0, 560 * 4 - 1, 560 * 4 - 1], fill=255)
pot.putalpha(m.resize((560, 560), Image.LANCZOS))
PX, PY = 320, 700
shadow = Image.new('RGBA', (W, HH), (0, 0, 0, 0))
ImageDraw.Draw(shadow).ellipse([PX + 40, PY + 500, PX + 520, PY + 600], fill=(80, 55, 20, 150))
bg = Image.alpha_composite(bg, shadow.filter(ImageFilter.GaussianBlur(26)))
ring = Image.new('RGBA', (W, HH), (0, 0, 0, 0))
ImageDraw.Draw(ring).ellipse([PX - 14, PY - 14, PX + 574, PY + 574], fill=(255, 255, 255, 255))
ImageDraw.Draw(ring).ellipse([PX - 14, PY - 14, PX + 574, PY + 574], outline=GOLD + (255,), width=4)
bg = Image.alpha_composite(bg, ring)
bg.alpha_composite(pot, (PX, PY))
# 倒影
refl = pot.transpose(Image.FLIP_TOP_BOTTOM).crop((0, 0, 560, 140))
fade = Image.new('L', (560, 140));
for yy in range(140): ImageDraw.Draw(fade).line([(0, yy), (560, yy)], fill=int(70 * (1 - yy / 140)))
refl.putalpha(ImageChops.multiply(refl.getchannel('A'), fade))
bg.alpha_composite(refl, (PX, PY + 576))

# ---------- 5. 浮起贈品卡（打斜、有陰影） ----------
def card(src, crop, label, w=300, rot=0):
    im = Image.open(SRC + src).convert('RGB').crop(crop).resize((w, int(w * (crop[3] - crop[1]) / (crop[2] - crop[0]))), Image.LANCZOS)
    pad, lh = 14, 58
    cw, ch = w + pad * 2, im.height + pad * 2 + lh
    c = Image.new('RGBA', (cw, ch), (0, 0, 0, 0))
    mk = Image.new('L', (cw, ch), 0); ImageDraw.Draw(mk).rounded_rectangle([0, 0, cw - 1, ch - 1], 22, fill=255)
    body = Image.new('RGBA', (cw, ch), (255, 255, 255, 255)); body.putalpha(mk); c.alpha_composite(body)
    im2 = im.convert('RGBA'); m2 = Image.new('L', im.size, 0); ImageDraw.Draw(m2).rounded_rectangle([0, 0, im.width - 1, im.height - 1], 14, fill=255); im2.putalpha(m2)
    c.alpha_composite(im2, (pad, pad))
    cd = ImageDraw.Draw(c); fl = f_cjk(30)
    tag = '送'; tw2 = cd.textlength(tag, font=fl)
    lw = cd.textlength(label, font=fl) + tw2 + 30
    lx = (cw - lw) / 2; ly = im.height + pad + 10
    cd.rounded_rectangle([lx - 4, ly + 2, lx + tw2 + 14, ly + 42], 10, fill=GOLD)
    cd.text((lx + 5, ly + 1), tag, font=fl, fill=(255, 255, 255))
    cd.text((lx + tw2 + 26, ly + 1), label, font=fl, fill=INK)
    c = c.rotate(rot, resample=Image.BICUBIC, expand=True)
    s = Image.new('RGBA', (c.width + 80, c.height + 80), (0, 0, 0, 0))
    s.paste((70, 45, 15, 110), (40 + 10, 40 + 22), c.getchannel('A'))
    s = s.filter(ImageFilter.GaussianBlur(16)); s.alpha_composite(c, (40, 40))
    return s
cards = [
    (card('d11src-g1.png', (90, 90, 1042, 640), '日式雞皮餃子', 270, 7), (0, 640)),
    (card('d11src-g2.jpg', (40, 60, 1024, 630), '蜜蜜燒雞翼', 250, -6), (848, 610)),
    (card('d11src-g3.png', (100, 90, 1042, 640), '避風塘海鮮豆腐', 250, 4), (830, 960)),
]
for c, (x, y) in cards: bg.alpha_composite(c, (x, y))

# ---------- 6. 右上直條標籤＋89 折圓章 ----------
tab = Image.new('RGBA', (92, 300), INK + (255,))
td = ImageDraw.Draw(tab); fv = f_cjk(34)
for i, ch_ in enumerate('雙十一限定'):
    td.text(((92 - td.textlength(ch_, font=fv)) / 2, 22 + i * 52), ch_, font=fv, fill=GOLD_L)
bg.alpha_composite(tab, (W - 92, 120))
badge = Image.new('RGBA', (220, 220), (0, 0, 0, 0)); bd = ImageDraw.Draw(badge)
bd.ellipse([0, 0, 219, 219], fill=(176, 52, 38)); bd.ellipse([10, 10, 209, 209], outline=(255, 226, 200), width=3)
fb = ImageFont.truetype(POPB, 82); fz = f_cjk(40)
bd.text(((220 - bd.textlength('89', font=fb)) / 2, 22), '89', font=fb, fill=(255, 255, 255))
bd.text(((220 - bd.textlength('折', font=fz)) / 2, 128), '折', font=fz, fill=(255, 236, 210))
badge = badge.rotate(-10, resample=Image.BICUBIC, expand=True)
bs = Image.new('RGBA', (badge.width + 40, badge.height + 40), (0, 0, 0, 0)); bs.paste((90, 30, 20, 120), (28, 32), badge.getchannel('A')); bs = bs.filter(ImageFilter.GaussianBlur(10)); bs.alpha_composite(badge, (20, 20))
bg.alpha_composite(bs, (36, 40))

# ---------- 7. 底部膠囊 ----------
d = ImageDraw.Draw(bg); fp = f_cjk(36)
pill = '2026.11.11 至 11.17　優惠碼 D11A／D11B'
pw = d.textlength(pill, font=fp) + 80
px0 = (W - pw) / 2; py0 = 1380
d.rounded_rectangle([px0, py0, px0 + pw, py0 + 74], 37, fill=INK)
d.text((px0 + 40, py0 + 12), pill, font=fp, fill=GOLD_L)

os.makedirs(os.path.join(H, 'img'), exist_ok=True)
out = bg.convert('RGB')
out.save(os.path.join(H, 'img', 'd11-kv.jpg'), quality=86, optimize=True, progressive=True)
out.resize((600, 750), Image.LANCZOS).save('/sessions/great-festive-darwin/mnt/outputs/kv_prev.jpg', quality=85)
print('saved', os.path.getsize(os.path.join(H, 'img', 'd11-kv.jpg')) // 1024, 'KB')
