# 香港到會避伏指南 2026｜blog 列表／精選圖片 JPG（雜誌封面 A 版面）
# 用法：python3 make_kv_jpg.py <相片路徑>
import sys, pathlib
from PIL import Image, ImageDraw, ImageFont, ImageOps
HERE = pathlib.Path(__file__).parent
W, H = 1600, 900
SER_B = ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc', 10, index=2)  # TC
def f(path, size, idx=0): return ImageFont.truetype(path, size, index=idx)
SB = '/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'; SR = '/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc'
SANS = '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
ITAL = '/usr/share/fonts/truetype/dejavu/DejaVuSerif-BoldItalic.ttf'
TC = 2  # NotoSerifCJK ttc index for TC? 0=JP,1=KR,2=SC,3=TC,4=HK

src = Image.open(sys.argv[1]).convert('RGB')
canvas = Image.new('RGB', (W, H), '#ffffff')
pw = int(W * .44)
photo = ImageOps.fit(src, (W - pw, H), Image.LANCZOS, centering=(.5, .5))
canvas.paste(photo, (pw, 0))
d = ImageDraw.Draw(canvas)
def sp(xy, t, font, fill, ls):
    x, y = xy
    for ch in t:
        d.text((x, y), ch, font=font, fill=fill); x += d.textlength(ch, font=font) + ls
    return x
ink = '#141414'
x0, y0 = 58, 52
# masthead
sp((x0, y0 + 8), 'CATERING GUIDE · 2026', f(SANS, 16, 3), ink, 4.5)
logo = Image.open(HERE.parent / 'halloween-edm-2026' / 'img' / 'logo-header-pill.png').convert('RGBA').crop((40, 21, 508, 99))
lh = 36; logo = logo.resize((int(logo.width * lh / logo.height), lh), Image.LANCZOS)
canvas.paste(logo, (pw - 58 - logo.width, y0 - 2), logo)
d.rectangle((x0, y0 + 52, pw - 58, y0 + 55), fill=ink)
# kicker + title
d.text((x0, 300), '香 港 到 會', font=f(SR, 36, 3), fill=ink)
tf = f(SB, 138, 3)
d.text((x0 - 4, 350), '避伏', font=tf, fill=ink)
d.text((x0 - 4, 510), '指南', font=tf, fill=ink)
# rule + 5 大常見陷阱
d.rectangle((x0, 704, pw - 58, 705), fill=ink)
d.text((x0, 712), '5', font=f(ITAL, 92), fill='#A8322A')
d.text((x0 + 72, 742), '大常見陷阱', font=f(SB, 46, 3), fill=ink)
d.text((x0, 812), '照騙｜份量｜遲到｜隱藏收費｜服務', font=f(SR, 24, 3), fill='#4a443d')
# footer
ff = f(SANS, 15, 3)
d.text((x0, 856), '附落單前必問 10 條問題', font=ff, fill='#6b645c')
t = '2026 年版'; d.text((pw - 58 - d.textlength(t, font=ff), 856), t, font=ff, fill='#6b645c')
d.rectangle((0, 0, W - 1, H - 1), outline=ink, width=2)
out = HERE / 'img' / 'catering-pitfalls-guide-2026.jpg'
canvas.save(out, 'JPEG', quality=88, optimize=True, progressive=True)
print(out, out.stat().st_size)
