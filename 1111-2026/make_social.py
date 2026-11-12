# -*- coding: utf-8 -*-
"""雙 11 社交媒體 carousel，共 6 張
  4:5（1080x1350）→ social/d11-slide-N.jpg       IG 及 FB 單帖／相簿
  1:1（1080x1080）→ social/square/d11-sq-N.jpg   FB 多相帖格仔、FB／IG carousel 廣告"""
import os, sys, importlib.util
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
spec = importlib.util.spec_from_file_location('k', os.path.join(H, 'make_kv3.py')); k = importlib.util.module_from_spec(spec); spec.loader.exec_module(k)
from PIL import Image, ImageDraw, ImageFilter, ImageFont
INK, GOLD, GOLD_L, GOLD_D = k.INK, k.GOLD, k.GOLD_L, k.GOLD_D
f = k.f_cjk
LATO = '/usr/share/fonts/truetype/lato/Lato-Light.ttf'
CW = 1200

def canvas(ch):
    bg = Image.new('RGB', (CW, ch)); d = ImageDraw.Draw(bg)
    for y in range(ch): d.line([(0, y), (CW, y)], fill=k.lerp((251, 246, 236), (238, 222, 192), y / ch))
    return bg.convert('RGBA')
def ctext(d, y, t, font, fill): d.text(((CW - d.textlength(t, font=font)) / 2, y), t, font=font, fill=fill)
def spaced(d, y, t, font, fill, sp=6):
    w = sum(d.textlength(c, font=font) for c in t) + sp * (len(t) - 1); x = (CW - w) / 2
    for c in t: d.text((x, y), c, font=font, fill=fill); x += d.textlength(c, font=font) + sp
def code_card(bg, y, w=760):
    """酒店名片款：PROMOTION CODE／DOUBLE11／金短線／優惠期，高 250"""
    d = ImageDraw.Draw(bg); x0 = (CW - w) // 2; h = 250
    d.rectangle([x0, y, x0 + w, y + h], fill=(255, 255, 255), outline=GOLD, width=2)
    d.rectangle([x0 + 11, y + 11, x0 + w - 11, y + h - 11], outline=(230, 211, 166), width=2)
    spaced(d, y + 40, 'PROMOTION CODE', ImageFont.truetype(LATO, 26), GOLD_D, 8)
    spaced(d, y + 78, 'DOUBLE11', ImageFont.truetype(LATO, 64), INK, 14)
    d.line([(CW / 2 - 40, y + 172), (CW / 2 + 40, y + 172)], fill=GOLD, width=2)
    ctext(d, y + 190, '優惠期　2026.11.11 至 11.17', f(26, False), (93, 83, 77))
    return h
def footer(bg, ch):
    d = ImageDraw.Draw(bg); ctext(d, ch - 52, 'aoaodelivery.com', f(24, False), (120, 104, 80))
def shadowed(p, a=70):
    sh = Image.new('RGBA', (p.width + 80, p.height + 80), (0, 0, 0, 0)); sh.paste((70, 45, 15, a), (46, 56), p.getchannel('A'))
    sh = sh.filter(ImageFilter.GaussianBlur(20)); sh.alpha_composite(p, (40, 40)); return sh

def build(square):
    ch = 1200 if square else 1500
    out = os.path.join(H, 'social', 'square') if square else os.path.join(H, 'social'); os.makedirs(out, exist_ok=True)
    def save(bg, n):
        size = (1080, 1080) if square else (1080, 1350)
        name = f'd11-sq-{n}.jpg' if square else f'd11-slide-{n}.jpg'
        bg.convert('RGB').resize(size, Image.LANCZOS).save(os.path.join(out, name), quality=90, optimize=True, progressive=True)
    # 1 封面
    kv = k.kv_design(10, False)                      # 1200x1230
    bg = canvas(ch)
    if square:
        s = kv.resize((int(1200 * 1170 / 1230), 1170), Image.LANCZOS); bg.paste(s, ((CW - s.width) // 2, 0)); footer(bg, ch)
    else:
        bg.paste(kv, (0, 0)); code_card(bg, 1180, 720); footer(bg, ch)
    save(bg, 1)
    # 2–5 四重賞
    k.HEAD_STYLE = 'A'
    for i, t in enumerate(k.TIER, 2):
        bg = canvas(ch); d = ImageDraw.Draw(bg)
        spaced(d, 58 if square else 70, 'DOUBLE ELEVEN · FOUR REWARDS', f(24, False), GOLD_D, 6)
        ctext(d, 94 if square else 110, '雙 11 四重賞', f(54 if square else 58), INK)
        p = k.panel(*t); sc = 1.05 if square else 1.3
        p = p.resize((int(p.width * sc), int(p.height * sc)), Image.LANCZOS)
        sh = shadowed(p); bg.alpha_composite(sh, ((CW - sh.width) // 2, 150 if square else 175))
        footer(bg, ch); save(bg, i)
    # 6 使用方法
    bg = canvas(ch); d = ImageDraw.Draw(bg)
    top = 120 if square else 80
    spaced(d, top, 'HOW TO REDEEM', f(26, False), GOLD_D, 8)
    ctext(d, top + 40, '點樣享用雙 11 四重賞？', f(52 if square else 56), INK)
    steps = [('1', '網站選購套餐或單點', '人數選餐、派對套餐、單點小食均適用'),
             ('2', '結帳時輸入優惠碼 DOUBLE11', '滿 HK$1,100 全單即減 11%'),
             ('3', '按訂單金額自動送小食', '滿 $1,500／$2,200／$3,000 送 1 至 3 款')]
    y = top + (160 if square else 170); gap = 138 if square else 150
    for no, a, b in steps:
        d.ellipse([140, y, 220, y + 80], fill=INK); d.ellipse([146, y + 6, 214, y + 74], outline=GOLD, width=2)
        d.text((180 - d.textlength(no, font=f(40)) / 2, y + 12), no, font=f(40), fill=GOLD_L)
        d.text((250, y + 2), a, font=f(38), fill=INK); d.text((250, y + 54), b, font=f(27, False), fill=(110, 98, 84))
        y += gap
    d.line([(140, y + 4), (CW - 140, y + 4)], fill=GOLD, width=2)
    ctext(d, y + (40 if square else 26), '會員優惠照常享用', f(36), INK)
    ctext(d, y + (92 if square else 76), '「多買多賞」及舊會員專屬優惠可同時使用', f(26, False), (93, 83, 77))
    if square:
        yy = y + 172
        d.rounded_rectangle([200, yy, CW - 200, yy + 90], 45, fill=INK)
        ctext(d, yy + 22, '優惠碼 DOUBLE11　立即網上預訂', f(34), GOLD_L)
        ctext(d, yy + 120, 'WhatsApp 查詢：6901 1987', f(28, False), INK)
    else:
        h = code_card(bg, y + 140)
        yy = y + 140 + h + 40
        d.rounded_rectangle([200, yy, CW - 200, yy + 92], 46, fill=INK)
        ctext(d, yy + 22, '立即網上預訂　aoaodelivery.com', f(36), GOLD_L)
        ctext(d, yy + 118, 'WhatsApp 查詢：6901 1987', f(30, False), INK)
    footer(bg, ch); save(bg, 6)

build(False); build(True)
print('ok')
