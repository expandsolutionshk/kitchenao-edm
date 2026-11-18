# 激光打印食物｜KV thumbnail JPG（媒體 banner 版面）
# 用法：python3 make_kv_jpg.py <雷射包相片> <馬卡龍相片>
import sys, pathlib
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter
HERE = pathlib.Path(__file__).parent
W, H = 1600, 900
SB = '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
SERB = '/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'
f = lambda p, s, i=3: ImageFont.truetype(p, s, index=i)
cv = Image.new('RGB', (W, H), '#ffffff')
lw = int(W * .57)
burger = ImageOps.fit(Image.open(sys.argv[1]).convert('RGB'), (lw - 4, H), Image.LANCZOS, centering=(.5, .45))
mac = ImageOps.fit(Image.open(sys.argv[2]).convert('RGB'), (W - lw - 4, H), Image.LANCZOS, centering=(.5, .5))
cv.paste(burger, (0, 0)); cv.paste(mac, (lw + 4, 0))
# 下半漸暗
grad = Image.new('L', (1, 256)); [grad.putpixel((0, y), int(max(0, (y - 90) / 166) ** 1.1 * 185)) for y in range(256)]
mask = grad.resize((W, int(H * .62)))
dark = Image.new('RGB', (W, int(H * .62)), (0, 0, 0))
cv.paste(dark, (0, H - mask.height), mask)
d = ImageDraw.Draw(cv)
INK, YEL = '#1A1A1A', '#F7CE46'
def label(x, y, t, rot):
    fn = f(SB, 30); tw = d.textlength(t, font=fn)
    im = Image.new('RGBA', (int(tw) + 70, 76), (0, 0, 0, 0)); g = ImageDraw.Draw(im)
    g.rounded_rectangle((6, 6, im.width - 1, im.height - 1), 34, fill=INK)
    g.rounded_rectangle((0, 0, im.width - 7, im.height - 7), 34, fill='white', outline=INK, width=4)
    g.text((30, 12), t, font=fn, fill=INK)
    im = im.rotate(rot, expand=True, resample=Image.BICUBIC); cv.paste(im, (x, y), im)
label(30, 30, '雷射包', 3)
label(lw + 30, 32, '馬卡龍刻字', -2)
# logo 膠囊
logo = Image.open(HERE.parent / 'halloween-edm-2026' / 'img' / 'logo-header-pill.png').convert('RGBA').crop((40, 21, 508, 99))
lh = 38; logo = logo.resize((int(logo.width * lh / logo.height), lh), Image.LANCZOS)
pw, ph = logo.width + 52, 66; px = W - 30 - pw
d.rounded_rectangle((px, 28, px + pw, 28 + ph), 33, fill='white', outline=INK, width=4)
cv.paste(logo, (px + 26, 28 + (ph - lh) // 2), logo)
# 標題區
x0 = 58
pf = f(SB, 32); t = '2026 香港到會新玩法'; tw = d.textlength(t, font=pf)
d.rounded_rectangle((x0, 412, x0 + tw + 60, 466), 27, fill=INK); d.text((x0 + 30, 418), t, font=pf, fill=YEL)
tf = f(SERB, 104)
for i, (t, col) in enumerate((('激光打印食物', 'white'), ('雷射包・馬卡龍', YEL))):
    y = 474 + i * 122
    d.text((x0, y + 8), t, font=tf, fill=INK, stroke_width=9, stroke_fill=INK)
    d.text((x0, y), t, font=tf, fill=col, stroke_width=9, stroke_fill=INK)
sf = f(SB, 33); t = '公司 Logo、名字、祝福語都刻得到'; tw = d.textlength(t, font=sf)
d.rectangle((x0 + 7, 756 + 7, x0 + tw + 50 + 7, 812 + 7), fill=INK); d.rectangle((x0, 756, x0 + tw + 50, 812), fill=YEL)
d.text((x0 + 25, 761), t, font=sf, fill=INK)
d.text((x0, 834), '$228 起｜最少 3 日前預訂', font=f(SB, 30), fill='white')
# 圓章
st = Image.new('RGBA', (240, 240), (0, 0, 0, 0)); g = ImageDraw.Draw(st)
g.ellipse((14, 14, 234, 234), fill=INK); g.ellipse((4, 4, 224, 224), fill=YEL, outline=INK, width=7)
for t, s, yy in (('IG 觀看', 26, 52), ('21萬+', 58, 86), ('人氣之選', 26, 156)):
    fn = f(SB, s); g.text((114 - g.textlength(t, font=fn) / 2, yy), t, font=fn, fill=INK)
st = st.rotate(10, expand=True, resample=Image.BICUBIC); cv.paste(st, (W - st.width - 30, H - st.height - 30), st)
out = HERE / 'img' / 'laser-printed-food-kv-1600x900.jpg'
cv.save(out, 'JPEG', quality=88, optimize=True, progressive=True)
cv.resize((1200, 675), Image.LANCZOS).save(HERE / 'img' / 'laser-printed-food-kv-1200x675.jpg', 'JPEG', quality=86, optimize=True, progressive=True)
print(out)
