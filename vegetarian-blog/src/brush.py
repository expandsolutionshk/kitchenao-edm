# 自製筆刷 SVG（原創程序生成，非素材）：長條筆觸、兩端分叉毛邊、可選乾筆飛白
import random, urllib.parse

def brush(fill, seed=1, dry=False, opacity=1, W=600, H=100):
    r = random.Random(seed)
    x0, x1 = 70, W - 70           # 主體範圍
    shapes = []
    # 主體：上下邊微波浪
    n = 12
    top = [(x0 + (x1 - x0) * k / n, 14 + r.uniform(-3, 3)) for k in range(n + 1)]
    bot = [(x0 + (x1 - x0) * k / n, H - 14 + r.uniform(-3, 3)) for k in range(n + 1)]
    pts = top + bot[::-1]
    shapes.append('M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in pts) + 'Z')
    # 兩端：多條橫向「筆毛」尖條，長短不一
    bands = 9
    for side in (-1, 1):
        base = x0 if side == -1 else x1
        for b in range(bands):
            y_top = 14 + (H - 28) * b / bands + r.uniform(-1.5, 1.5)
            y_bot = 14 + (H - 28) * (b + 1) / bands + r.uniform(-1.5, 1.5)
            L = r.uniform(18, 66) if r.random() > .15 else r.uniform(4, 12)
            tip = base + side * L
            mid = (y_top + y_bot) / 2 + r.uniform(-2, 2)
            back = base - side * 4
            shapes.append(f'M{back:.1f},{y_top:.1f} L{base + side * L * .55:.1f},{y_top + r.uniform(0, 2):.1f} '
                          f'L{tip:.1f},{mid:.1f} L{base + side * L * .5:.1f},{y_bot - r.uniform(0, 2):.1f} L{back:.1f},{y_bot:.1f}Z')
        # 少量飛濺點
        for _ in range(3):
            cx = base + side * r.uniform(55, 85); cy = r.uniform(20, H - 20)
            shapes.append(f'M{cx:.1f},{cy:.1f} m-2.2,0 a2.2,2.2 0 1,0 4.4,0 a2.2,2.2 0 1,0 -4.4,0')
    d = ' '.join(shapes)
    streak = ''
    if dry:
        for k in range(10):
            y = r.uniform(20, H - 20)
            sx = r.choice([r.uniform(10, 140), r.uniform(W - 260, W - 120)])
            L = r.uniform(70, 170)
            streak += (f'<path d="M{sx:.0f},{y:.0f} q{L/2:.0f},{r.uniform(-2,2):.1f} {L:.0f},{r.uniform(-1.5,1.5):.1f}" '
                       f'stroke="#000" stroke-width="{r.uniform(1,2.6):.1f}" fill="none" stroke-linecap="round"/>')
    mask = f'<mask id="m"><rect width="{W}" height="{H}" fill="#fff"/>{streak}</mask>' if dry else ''
    mk = ' mask="url(#m)"' if dry else ''
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" preserveAspectRatio="none">{mask}'
           f'<path d="{d}" fill="{fill}" fill-opacity="{opacity}"{mk}/></svg>')
    return "url('data:image/svg+xml," + urllib.parse.quote(svg) + "')"
