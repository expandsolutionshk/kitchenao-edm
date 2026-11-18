# -*- coding: utf-8 -*-
# 香港到會避伏指南 2026｜Blog KV 兩個方案（HTML，container query 響應式）
import pathlib
HERE = pathlib.Path(__file__).parent
PID = '1740047602722-b4993b79e4b7'   # Unsplash: dHeKcZ0a-xY（木枱派對美食）
def ux(w, h): return f'https://images.unsplash.com/photo-{PID}?w={w}&h={h}&fit=crop&crop=entropy&q=78&auto=format'
IMG_W = ux(1600, 900)    # 16:9
IMG_M = ux(900, 1125)    # 4:5

CSS = r'''
.ao-kv{container-type:inline-size;margin:0 0 24px;font-family:inherit}
.ao-kv *{box-sizing:border-box}
.ao-kv picture,.ao-kv img{display:block;width:100%;height:100%}
.ao-kv img{object-fit:cover}

/* ===== 方案 1：相片全幅＋左側漸層大標題 ===== */
.ao-kv.v1 .f{position:relative;aspect-ratio:16/9;overflow:hidden;border-radius:8px;background:#141414}
.ao-kv.v1 .f:after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(14,12,10,.92) 0%,rgba(14,12,10,.78) 34%,rgba(14,12,10,.18) 68%,rgba(14,12,10,0) 100%)}
.ao-kv.v1 .tx{position:absolute;z-index:2;left:6cqw;top:50%;transform:translateY(-50%);width:52cqw;color:#fff}
.ao-kv.v1 .eb{display:flex;align-items:center;gap:1.2cqw;font-size:1.25cqw;letter-spacing:.32em;font-weight:700;color:#E4C77E;text-transform:uppercase;margin:0 0 2cqw}
.ao-kv.v1 .eb:before{content:"";width:4cqw;height:2px;background:#C8A24A}
.ao-kv.v1 .h{font-size:5.6cqw;line-height:1.18;font-weight:900;margin:0;letter-spacing:.02em;color:#fff}
.ao-kv.v1 .h em{font-style:normal;color:#E4C77E}
.ao-kv.v1 .s{font-size:1.9cqw;line-height:1.6;color:#EDE6D8;margin:1.8cqw 0 0;font-weight:500}
.ao-kv.v1 .chips{display:flex;flex-wrap:wrap;gap:.8cqw;margin:2.6cqw 0 0}
.ao-kv.v1 .chips span{font-size:1.3cqw;font-weight:700;color:#141414;background:#E4C77E;border-radius:40px;padding:.5cqw 1.4cqw}
.ao-kv.v1 .br{position:absolute;z-index:2;right:3cqw;bottom:2.6cqw;font-size:1.15cqw;letter-spacing:.3em;color:#fff;font-weight:700;opacity:.9}

@container (max-width:640px){
 .ao-kv.v1 .f{aspect-ratio:4/5}
 .ao-kv.v1 .f:after{background:linear-gradient(0deg,rgba(14,12,10,.95) 0%,rgba(14,12,10,.82) 38%,rgba(14,12,10,.15) 70%,rgba(14,12,10,0) 100%)}
 .ao-kv.v1 .tx{left:7cqw;right:7cqw;width:auto;top:auto;bottom:9cqw;transform:none}
 .ao-kv.v1 .eb{font-size:3cqw;gap:2.4cqw;margin-bottom:3.6cqw}
 .ao-kv.v1 .eb:before{width:8cqw}
 .ao-kv.v1 .h{font-size:11.2cqw;line-height:1.16}
 .ao-kv.v1 .s{font-size:4.1cqw;margin-top:3.4cqw}
 .ao-kv.v1 .chips{gap:2cqw;margin-top:4.6cqw}
 .ao-kv.v1 .chips span{font-size:3.2cqw;padding:1.2cqw 3.2cqw}
 .ao-kv.v1 .br{top:6cqw;left:7cqw;right:auto;bottom:auto;font-size:2.8cqw}
}

/* ===== 方案 2：黑白分段（左黑底標題、右相片＋圓形數字） ===== */
.ao-kv.v2 .f{display:grid;grid-template-columns:46% 54%;aspect-ratio:16/9;border-radius:8px;overflow:hidden;background:#141414}
.ao-kv.v2 .tx{position:relative;padding:5cqw 4.4cqw;display:flex;flex-direction:column;justify-content:center;color:#fff}
.ao-kv.v2 .eb{font-size:1.15cqw;letter-spacing:.32em;font-weight:700;color:#C8A24A;text-transform:uppercase;margin:0 0 1.8cqw}
.ao-kv.v2 .ln{width:4cqw;height:.35cqw;border-radius:2px;background:#C8A24A;margin:0 0 2cqw}
.ao-kv.v2 .h{font-size:4.5cqw;line-height:1.2;font-weight:900;margin:0;color:#fff}
.ao-kv.v2 .h small{display:block;font-size:2.1cqw;color:#E4C77E;font-weight:800;letter-spacing:.06em;margin:0 0 .8cqw}
.ao-kv.v2 .s{font-size:1.6cqw;line-height:1.7;color:#cfc7b8;margin:1.8cqw 0 0}
.ao-kv.v2 .st{display:flex;gap:2.4cqw;margin:2.6cqw 0 0;padding:2cqw 0 0;border-top:1px solid #34302a}
.ao-kv.v2 .st div{font-size:1.25cqw;color:#cfc7b8;line-height:1.4}
.ao-kv.v2 .st b{display:block;font-size:3.4cqw;color:#E4C77E;font-weight:900;line-height:1.1}
.ao-kv.v2 .ph{position:relative}
.ao-kv.v2 .badge{position:absolute;left:-5cqw;bottom:4cqw;width:10cqw;height:10cqw;border-radius:50%;background:#F7F5F0;border:.35cqw solid #C8A24A;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;color:#141414;z-index:2}
.ao-kv.v2 .badge b{font-size:2.6cqw;font-weight:900;line-height:1}
.ao-kv.v2 .badge span{font-size:.95cqw;letter-spacing:.14em;font-weight:800;color:#9A7B2E;margin-top:.4cqw}
.ao-kv.v2 .br{position:absolute;left:4.4cqw;bottom:3cqw;font-size:1.05cqw;letter-spacing:.3em;color:#8d857a;font-weight:700}

@container (max-width:640px){
 .ao-kv.v2 .f{grid-template-columns:1fr;grid-template-rows:auto auto;aspect-ratio:auto}
 .ao-kv.v2 .ph{order:-1;aspect-ratio:4/3}
 .ao-kv.v2 .tx{padding:9cqw 7cqw 13cqw}
 .ao-kv.v2 .eb{font-size:2.9cqw;margin-bottom:3.2cqw}
 .ao-kv.v2 .ln{width:10cqw;height:.9cqw;margin-bottom:3.6cqw}
 .ao-kv.v2 .h{font-size:9.6cqw}
 .ao-kv.v2 .h small{font-size:4.4cqw;margin-bottom:1.6cqw}
 .ao-kv.v2 .s{font-size:3.9cqw;margin-top:3.4cqw}
 .ao-kv.v2 .st{gap:6cqw;margin-top:5cqw;padding-top:4.4cqw}
 .ao-kv.v2 .st div{font-size:3.1cqw}
 .ao-kv.v2 .st b{font-size:8.4cqw}
 .ao-kv.v2 .badge{left:auto;right:5cqw;bottom:-9cqw;width:22cqw;height:22cqw;border-width:.8cqw}
 .ao-kv.v2 .badge b{font-size:6cqw}
 .ao-kv.v2 .badge span{font-size:2.2cqw}
 .ao-kv.v2 .br{left:7cqw;bottom:5cqw;font-size:2.5cqw}
}
'''

PIC = (f'<picture><source media="(max-width:640px)" srcset="{IMG_M}">'
       f'<img src="{IMG_W}" alt="香港到會避伏指南 2026：派對到會美食擺滿木枱" width="1600" height="900" fetchpriority="high" decoding="async"></picture>')

V1 = ('<div class="ao-kv v1"><div class="f">' + PIC +
      '<div class="tx"><p class="eb">Catering Guide 2026</p>'
      '<p class="h">香港到會<br><em>避伏指南</em></p>'
      '<p class="s">5 大常見陷阱＋落單前必問 10 條問題</p>'
      '<div class="chips"><span>照騙</span><span>份量</span><span>遲到</span><span>隱藏收費</span><span>服務</span></div></div>'
      '<span class="br">KITCHEN AO</span></div></div>')

V2 = ('<div class="ao-kv v2"><div class="f"><div class="tx">'
      '<p class="eb">Catering Guide 2026</p><div class="ln"></div>'
      '<p class="h"><small>2026 年版</small>香港到會<br>避伏指南</p>'
      '<p class="s">落單前看清楚，避開照騙、份量不足、遲到及隱藏收費。</p>'
      '<div class="st"><div><b>5</b>大常見陷阱</div><div><b>10</b>條必問問題</div><div><b>8</b>個常見問題</div></div>'
      '<span class="br">KITCHEN AO</span></div>'
      '<div class="ph">' + PIC + '<div class="badge"><b>2026</b><span>UPDATED</span></div></div></div></div>')

def page(title, blocks):
    return ('<!doctype html><html lang="zh-HK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>' + title + '</title>'
            '<style>body{margin:0;background:#EDEAE3;font-family:-apple-system,"PingFang HK","Microsoft JhengHei",sans-serif;color:#222}'
            '.w{max-width:1280px;margin:0 auto;padding:24px 18px 60px}h1{font-size:20px;margin:0 0 4px}.n{font-size:13px;color:#777;margin:0 0 22px}'
            'h2{font-size:16px;margin:34px 0 10px}.row{display:grid;grid-template-columns:minmax(0,1fr) 375px;gap:22px;align-items:start}'
            '.lab{font-size:12px;color:#888;margin:0 0 6px}.mob{background:#fff;padding:12px;border-radius:10px}'
            '@media(max-width:900px){.row{grid-template-columns:1fr}.mob{max-width:375px}}' + CSS + '</style></head><body><div class="w">' + blocks + '</div></body></html>')

blocks = ('<h1>香港到會避伏指南 2026｜Blog KV 兩個方案</h1><p class="n">相片：Unsplash（免費商用）。每個方案同時顯示桌面（16:9）及手機（375px）版本；KV 會按所在欄位闊度自動切換。請用瀏覽器開啟以載入相片。</p>'
          '<h2>方案 1｜相片全幅＋大標題</h2><div class="row"><div><p class="lab">桌面 16:9</p>' + V1 + '</div><div class="mob"><p class="lab">手機 4:5</p>' + V1 + '</div></div>'
          '<h2>方案 2｜黑白分段＋數字重點</h2><div class="row"><div><p class="lab">桌面 16:9</p>' + V2 + '</div><div class="mob"><p class="lab">手機</p>' + V2 + '</div></div>')
(HERE / 'KV方案-香港到會避伏指南.html').write_text(page('KV 方案｜香港到會避伏指南 2026', blocks), encoding='utf-8')
(HERE / 'kv-v1.html').write_text('<style>' + CSS + '</style>' + V1, encoding='utf-8')
(HERE / 'kv-v2.html').write_text('<style>' + CSS + '</style>' + V2, encoding='utf-8')
print('ok')
