# B2 KV 定稿：M1-D 雜誌專題式＋水彩筆刷四色分類（responsive：桌面 16:9／手機 4:5）
from kv_fresh import LOGO
from brush import brush

CLR = ['#E9A400', '#3C8FCB', '#E8743B', '#2F8F4E']   # 蛋奶素 黃／奶素 藍／五辛素 橙／純素 綠

CSS = '''
.ao-mkv{margin:0 0 22px;font-family:-apple-system,"PingFang HK","Microsoft JhengHei",Arial,sans-serif}
.ao-mkv *{box-sizing:border-box}
.ao-mkv .kv{border:4px solid #CFE8CD;border-radius:6px;position:relative;width:100%;aspect-ratio:16/9;container-type:inline-size;overflow:hidden;background:#FBFAF6}
.ao-mkv .g{position:absolute;top:0;right:0;bottom:0;width:45%;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:.5cqw;background:#fff}
.ao-mkv .g>div{position:relative;background-size:cover;background-position:center}
.ao-mkv .g span{position:absolute;left:.6cqw;bottom:1.4cqw;transform:rotate(-2deg);white-space:nowrap;background:none no-repeat center/100% 100%;padding:.9cqw 3.6cqw 1cqw 3.2cqw;color:#fff;line-height:1.25;filter:drop-shadow(0 .3cqw .5cqw rgba(0,0,0,.18))}
.ao-mkv .g span b{display:block;font-size:2.2cqw;font-weight:900;letter-spacing:.15cqw}
.ao-mkv .g span small{display:block;font-size:1.2cqw;font-weight:700;color:rgba(255,255,255,.92);margin-top:.1cqw}
.ao-mkv .logo2{position:absolute;right:1.8cqw;top:1.8cqw;z-index:5;display:inline-flex;align-items:center;height:4.3cqw;background:#fff;border:.25cqw solid #DCEFD6;border-radius:3cqw;padding:0 1.8cqw;line-height:0}
.ao-mkv .logo2 img{max-width:none!important;margin:0!important;padding:0!important;border:0!important;box-shadow:none!important;display:block!important;width:auto!important}
.ao-mkv .logo2 .li{height:2.3cqw!important}.ao-mkv .logo2 .lt{height:2cqw!important;margin-left:1cqw!important}
.ao-mkv .tb{position:absolute;left:4.5cqw;top:50%;transform:translateY(-50%);width:46cqw}
.ao-mkv .kick{display:flex;align-items:center;gap:1.2cqw;margin:0 0 1.8cqw!important;padding:0!important;font-size:1.5cqw!important;line-height:1.4!important;letter-spacing:.3cqw;color:#7a7a7a}
.ao-mkv .kick b{color:#fff;background:none no-repeat center/100% 100%;padding:.5cqw 2.8cqw .6cqw}
.ao-mkv .kick i{flex:0 0 6cqw;height:.15cqw;background:#2C6E49}
.ao-mkv .ttl{margin:0!important;padding:0!important;border:0!important;font-family:"Noto Serif TC","Songti TC","PMingLiU",serif!important;font-size:3.7cqw!important;line-height:1.3!important;font-weight:900!important;color:#1A1A1A!important;letter-spacing:.1cqw;white-space:nowrap}
.ao-mkv .ttl em{font-style:normal;color:#2C6E49;background:none no-repeat center 70%/104% 62%;padding:0 1.6cqw;margin:0 -1.2cqw}
.ao-mkv .dek{margin:2cqw 0 0!important;padding:0 0 0 1.4cqw!important;border-left:.35cqw solid #3F9D5A;font-size:1.9cqw!important;line-height:1.6!important;color:#4a4a4a}
.ao-mkv .by{margin:2.4cqw 0 0!important;padding:0!important;font-size:1.3cqw!important;line-height:1.4!important;color:#8a8a8a;letter-spacing:.15cqw}
@media(max-width:640px){
.ao-mkv .kv{aspect-ratio:4/5}
.ao-mkv .g{top:auto;left:0;width:100%;height:50%;gap:.8cqw}
.ao-mkv .g span{left:1cqw;bottom:2.4cqw;padding:1.4cqw 5.6cqw 1.6cqw 5cqw}
.ao-mkv .g span b{font-size:3.8cqw}.ao-mkv .g span small{font-size:2.3cqw}
.ao-mkv .logo2{height:7.5cqw;padding:0 3cqw;right:4cqw;top:4cqw}.ao-mkv .logo2 .li{height:4cqw!important}.ao-mkv .logo2 .lt{height:3.4cqw!important;margin-left:1.6cqw!important}
.ao-mkv .tb{left:6cqw;right:6cqw;width:auto;top:15cqw;transform:none}
.ao-mkv .kick{font-size:3cqw!important;margin-bottom:3cqw!important}.ao-mkv .kick b{padding:.9cqw 4.4cqw 1cqw}.ao-mkv .kick i{flex-basis:10cqw;height:.3cqw}
.ao-mkv .ttl{font-size:6.6cqw!important}
.ao-mkv .dek{margin-top:3.4cqw!important;font-size:3.6cqw!important;padding-left:2.4cqw!important;border-left-width:.7cqw}
.ao-mkv .by{display:none}
}
'''

def block(cols, tag='div', kicker='素食新手入門', year='2026',
          ttl='聚會有朋友吃素？<br>新手一表看懂<em>素食種類</em>',
          dek='蛋奶素、奶素、五辛素、純素……<br>10 種吃法一次看清！', by='文：Kitchen AO 編輯部'):
    """cols: [(img_url, 名稱, 說明), ...] 共 4 格"""
    g = '<div class="g">' + ''.join(
        f'<div style="background-image:url({u})" role="img" aria-label="{n}"><span style="background-image:{brush(CLR[k], seed=k+3, opacity=.93)}"><b>{n}</b><small>{s}</small></span></div>'
        for k, (u, n, s) in enumerate(cols)) + '</div>'
    sty = (f'<style>{CSS.replace(chr(10), "")}.ao-mkv .kick b{{background-image:{brush("#2F8F4E", seed=40, opacity=.95)}}}'
           f'.ao-mkv .ttl em{{background-image:{brush("#F7CE46", seed=41, opacity=.75)}}}</style>')
    return (f'<div class="ao-mkv">{sty}<div class="kv">{g}{LOGO}<div class="tb">'
            f'<p class="kick"><b>{kicker}</b><i></i>{year}</p>'
            f'<{tag} class="ttl">{ttl}</{tag}>'
            f'<p class="dek">{dek}</p><p class="by">{by}</p></div></div></div>')
