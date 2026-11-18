# -*- coding: utf-8 -*-
# Kitchen AO 2026 聖誕餐牌 PDF（中／英）：第 1 頁餐牌，第 2 頁起菜式詳細介紹
import pathlib, re, io
from fontTools.ttLib import TTCollection, TTFont, newTable
from fontTools.subset import Subsetter, Options
from fontTools.pens.cu2quPen import Cu2QuPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont as RLFont
from reportlab.lib.fonts import addMapping
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, KeepTogether, NextPageTemplate, PageBreak
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER
HERE = pathlib.Path(__file__).parent
SRC = pathlib.Path('/sessions/great-festive-darwin/mnt/Desktop/cowork - aoao/xmas-2026')
ns = {}
src = (SRC / 'make_desc.py').read_text(encoding='utf-8')
exec(src[:src.index('\n# ---------- 英文版')], ns)
import sys; sys.path.insert(0, str(SRC)); import en_text as EN
S, L, CATS, PLATTER = ns['S'], ns['L'], ns['CATS'], ns['PLATTER']
ORDER = [k for _, ks in CATS for k in ks]
GOLD, DGOLD, RED, INK, SUB, CREAM = HexColor('#C8A24A'), HexColor('#9A7B2E'), HexColor('#B03426'), HexColor('#1A1A1A'), HexColor('#5d534d'), HexColor('#FFFCF5')

import unicodedata
def N(t): return unicodedata.normalize('NFC', t)
def strip(t): return N(re.sub(r'<[^>]+>', '', t))
def rl(t):  # HTML 片段 → reportlab 標記
    t = N(t).replace('<strong>', '<b>').replace('</strong>', '</b>').replace('<br>', '<br/>')
    return t

T = {
 'zh': dict(title='聖誕套餐餐牌', eyebrow='KITCHEN AO · CHRISTMAS MENU 2026', rib='XMAS SPECIAL · 全新菜式推介', cats={c: c for c, _ in CATS},
            name=lambda k: S[k][0], secret='聖誕神秘加配', platter='聖誕樹芝士火腿拼盤', ptag='派對焦點冷盤', det='菜式詳細介紹',
            L=L, P=PLATTER,
            notes=['聖誕套餐供應及送貨日期：2026 年 12 月 12 日至 27 日', '11 月 30 日 23:59 前輸入優惠碼 MEGA79，聖誕套餐享七九折',
                   '套餐菜式可按喜好自由配搭；部分精選菜式需另加差價，以落單頁面為準'],
            foot='aoaodelivery.com　｜　WhatsApp 6901 1987'),
 'en': dict(title='Christmas Set Menu', eyebrow='KITCHEN AO · CHRISTMAS MENU 2026', rib='XMAS SPECIAL · NEW CHRISTMAS DISHES', cats=EN.CATS_EN,
            name=lambda k: EN.S_EN[k][0], secret=EN.TX_EN['secret'], platter=EN.TX_EN['platter_short'], ptag=EN.TX_EN['platter_tag'], det='Dish Details',
            L=EN.L_EN, P=EN.PLATTER_EN,
            notes=['Christmas sets are available for delivery from 12 to 27 December 2026',
                   'Enter code MEGA79 by 30 November, 23:59 for 21% off Christmas sets',
                   'Dishes can be mixed and matched; some premium dishes carry a surcharge shown on the order page'],
            foot='aoaodelivery.com　|　WhatsApp +852 6901 1987'),
}

def cjk_ttf(style, text, out):
    path = f'/usr/share/fonts/opentype/noto/NotoSerifCJK-{style}.ttc'
    f = TTCollection(path).fonts[3]
    buf = io.BytesIO(); f.save(buf); f = TTFont(io.BytesIO(buf.getvalue()))
    o = Options(); o.layout_features = []; o.name_IDs = ['*']; o.notdef_outline = True; o.hinting = False
    ss = Subsetter(o); ss.populate(text=text); ss.subset(f)
    go = f.getGlyphOrder(); gs = f.getGlyphSet(); glyf = newTable('glyf'); glyf.glyphOrder = go; glyf.glyphs = {}
    for g in go:
        pen = TTGlyphPen(None); gs[g].draw(Cu2QuPen(pen, 1.0, reverse_direction=True)); glyf.glyphs[g] = pen.glyph()
    del f['CFF ']
    if 'VORG' in f: del f['VORG']
    f['glyf'] = glyf; f['loca'] = newTable('loca')
    f['maxp'].tableVersion = 0x00010000
    for a in ('maxZones', 'maxTwilightPoints', 'maxStorage', 'maxFunctionDefs', 'maxInstructionDefs', 'maxStackElements', 'maxSizeOfInstructions', 'maxComponentElements'):
        setattr(f['maxp'], a, 0)
    f['maxp'].maxZones = 1; f['maxp'].maxComponentDepth = 0
    f['head'].indexToLocFormat = 0; f['head'].glyphDataFormat = 0
    f['post'].formatType = 3.0
    f.sfntVersion = '\x00\x01\x00\x00'
    f.save(out)

def all_text(t):
    parts = [t['title'], t['eyebrow'], t['rib'], t['secret'], t['platter'], t['ptag'], t['det'], t['foot']] + t['notes'] + list(t['cats'].values())
    parts += [t['name'](k) for k in ORDER] + [strip(x) for k in ORDER for x in t['L'][k]] + [strip(x) for x in t['P']]
    return ''.join(parts) + '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ·.,:;()&%$+-–—|｜「」（）、，。：；・'

def build(lang):
    t = T[lang]; txt = all_text(t)
    tmp = HERE / 'pdf' / '_fonts'; tmp.mkdir(parents=True, exist_ok=True)
    cjk_ttf('Regular', txt, tmp / f'r-{lang}.ttf'); cjk_ttf('Bold', txt, tmp / f'b-{lang}.ttf')
    R, B = f'NS-{lang}', f'NSB-{lang}'
    pdfmetrics.registerFont(RLFont(R, str(tmp / f'r-{lang}.ttf'))); pdfmetrics.registerFont(RLFont(B, str(tmp / f'b-{lang}.ttf')))
    addMapping(R, 0, 0, R); addMapping(R, 1, 0, B); addMapping(R, 0, 1, R); addMapping(R, 1, 1, B)
    W, H = A4
    def frame_deco(c):
        c.setFillColor(CREAM); c.rect(0, 0, W, H, 0, 1)
        c.setStrokeColor(GOLD); c.setLineWidth(1.2); c.rect(22, 22, W - 44, H - 44)
        c.setLineWidth(.5); c.rect(28, 28, W - 56, H - 56)
    def diamond(c, x, y, r=3):
        p = c.beginPath(); p.moveTo(x, y + r); p.lineTo(x + r * .6, y); p.lineTo(x, y - r); p.lineTo(x - r * .6, y); p.close()
        c.setFillColor(GOLD); c.drawPath(p, 0, 1)
    def holly(c, x, y):
        c.setFillColor(HexColor('#2F5D3A'))
        for s in (-1, 1):
            p = c.beginPath(); p.moveTo(x, y); p.curveTo(x + s * 8, y + 8, x + s * 18, y + 7, x + s * 24, y + 2); p.curveTo(x + s * 18, y - 1, x + s * 12, y - 4, x, y); p.close(); c.drawPath(p, 0, 1)
        c.setFillColor(RED)
        for dx, dy in ((-3, 0), (3, 0), (0, 4)): c.circle(x + dx, y + dy, 2.6, 0, 1)
    def page1(c, doc):
        c.saveState(); frame_deco(c)
        y = H - 78; holly(c, W / 2, y)
        wm = HERE / 'img' / 'kitchen-ao-wordmark-gold.png'
        c.drawImage(str(wm), W / 2 - 58, y - 38, 116, 20, mask='auto')
        c.setFillColor(DGOLD); c.setFont(R, 7.5); c.drawCentredString(W / 2, y - 54, ' '.join(t['eyebrow']) if lang == 'zh' else t['eyebrow'])
        c.setFillColor(INK); c.setFont(R, 24 if lang == 'zh' else 22); c.drawCentredString(W / 2, y - 90, t['title'])
        c.setStrokeColor(GOLD); c.setLineWidth(.6); c.line(W / 2 - 40, y - 106, W / 2 - 10, y - 106); c.line(W / 2 + 10, y - 106, W / 2 + 40, y - 106); diamond(c, W / 2, y - 106)
        # 絲帶
        rw = 230; ry = y - 140
        p = c.beginPath(); p.moveTo(W / 2 - rw / 2, ry + 9); p.lineTo(W / 2 + rw / 2, ry + 9); p.lineTo(W / 2 + rw / 2 - 8, ry); p.lineTo(W / 2 + rw / 2, ry - 9); p.lineTo(W / 2 - rw / 2, ry - 9); p.lineTo(W / 2 - rw / 2 + 8, ry); p.close()
        c.setFillColor(HexColor('#8A453F')); c.drawPath(p, 0, 1)
        c.setFillColor(HexColor('#F0D39A')); c.setFont(R, 8.5); c.drawCentredString(W / 2, ry - 3, t['rib'])
        yy = ry - 40
        for cat, ks in CATS:
            c.setFillColor(RED); c.setFont(R, 10); c.drawCentredString(W / 2, yy, ' '.join(t['cats'][cat]) if lang == 'zh' else t['cats'][cat].upper())
            yy -= 18
            for k in ks:
                c.setFillColor(INK); c.setFont(B, 11.5 if lang == 'zh' else 11); c.drawCentredString(W / 2, yy, N(t['name'](k))); yy -= 17
            diamond(c, W / 2, yy + 4, 2.4); yy -= 18
        c.setFillColor(RED); c.setFont(R, 10); c.drawCentredString(W / 2, yy, ' '.join(t['secret']) if lang == 'zh' else t['secret'].upper()); yy -= 18
        c.setFillColor(INK); c.setFont(B, 11.5); c.drawCentredString(W / 2, yy, t['platter']); yy -= 14
        c.setFillColor(SUB); c.setFont(R, 8.5); c.drawCentredString(W / 2, yy, t['ptag'])
        # 底部說明
        by = 112
        c.setStrokeColor(GOLD); c.setLineWidth(.5); c.line(70, by + 26, W - 70, by + 26)
        c.setFont(R, 8); c.setFillColor(SUB)
        for i, n in enumerate(t['notes']): c.drawCentredString(W / 2, by + 10 - i * 13, n)
        c.setFillColor(DGOLD); c.setFont(R, 8); c.drawCentredString(W / 2, 52, t['foot'])
        c.restoreState()
    def later(c, doc):
        c.saveState(); frame_deco(c)
        c.setFillColor(DGOLD); c.setFont(R, 7.5); c.drawCentredString(W / 2, H - 52, t['eyebrow'])
        c.setFillColor(INK); c.setFont(R, 18); c.drawCentredString(W / 2, H - 82, ' '.join(t['det']) if lang == 'zh' else t['det'])
        c.setStrokeColor(GOLD); c.setLineWidth(.6); c.line(W / 2 - 22, H - 94, W / 2 + 22, H - 94)
        c.setFont(R, 8); c.drawCentredString(W / 2, 46, t['foot']); c.restoreState()
    st_h = ParagraphStyle('h', fontName=R, fontSize=17, leading=22, textColor=INK, alignment=TA_CENTER, spaceAfter=14)
    st_n = ParagraphStyle('n', fontName=B, fontSize=9.8 if lang == 'zh' else 9.4, leading=12.5, textColor=INK, spaceBefore=4, spaceAfter=2)
    st_b = ParagraphStyle('b', fontName=R, fontSize=7.7 if lang == 'zh' else 7.5, leading=11.2 if lang == 'zh' else 10.2, textColor=SUB, spaceAfter=3)
    out = HERE / 'pdf' / '_fonts' / f'part-{lang}.pdf'
    doc = BaseDocTemplate(str(out), pagesize=A4, title=f'Kitchen AO {t["title"]} 2026', author='Kitchen AO')
    fw = (W - 120 - 24) / 2
    doc.addPageTemplates([PageTemplate('p1', [Frame(0, 0, 1, 1)], onPage=page1),
                          PageTemplate('p2', [Frame(50, 58, fw + 10, H - 165, id='a'), Frame(50 + fw + 10 + 24, 58, fw + 10, H - 165, id='b')], onPage=later)])
    story = [NextPageTemplate('p2'), PageBreak()]
    hd = Paragraph(t['det'] if lang == 'en' else ' '.join(t['det']), st_h)
    items = [(N(t['name'](k)), t['L'][k]) for k in ORDER] + [(t['P'][0], [t['P'][1]])]
    first = True
    for n, ps in items:
        blk = [Paragraph(n, st_n)] + [Paragraph(rl(x), st_b) for x in ps] + [Spacer(1, 2)]
        story.extend(blk)
    doc.build([NextPageTemplate('p2'), PageBreak(), Spacer(1, 2)] if False else story)
    # 標題放第 2 頁頂（用 canvas 太複雜，改為在 later() 畫）
    return out

if __name__ == '__main__':
    import subprocess
    if len(sys.argv) > 1: print(build(sys.argv[1]))
    else:
        for lg in ('zh', 'en'): subprocess.run([sys.executable, __file__, lg], check=True)  # 每個語言獨立行，避免字型名稱互相干擾
        # 合併：兩個檔案都係中英 4 頁；中文檔中文先，英文檔英文先
        from pypdf import PdfReader, PdfWriter
        for first, second in (('zh', 'en'), ('en', 'zh')):
            w = PdfWriter()
            for lg in (first, second):
                for pg in PdfReader(str(HERE / 'pdf' / '_fonts' / f'part-{lg}.pdf')).pages: w.add_page(pg)
            w.add_metadata({'/Title': 'Kitchen AO Christmas Menu 2026 聖誕餐牌', '/Author': 'Kitchen AO'})
            with open(HERE / 'pdf' / f'kitchen-ao-christmas-menu-2026-{first}.pdf', 'wb') as fh: w.write(fh)
            print('ok', first)
