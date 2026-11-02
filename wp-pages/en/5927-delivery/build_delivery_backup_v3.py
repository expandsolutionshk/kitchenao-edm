# -*- coding: utf-8 -*-
"""送貨需知 /delivery/ (5927)：中英 Raw HTML，分頁列按下切換內容（內容全部在 HTML 內，SEO 不受影響）
輸出 zh-rawhtml.html（Extra class ao-zh）及 en-rawhtml.html（Extra class ao-en）"""
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))
IDS = ['free-shipping', 'shipping-fees', 'delivery-time', 'important', 'weather', 'faq']

src_en = open(os.path.join(HERE, 'en.html'), encoding='utf-8').read()
CSS = re.search(r'<style>(.*?)</style>', src_en, re.S).group(1).strip()
CSS += '''
.ao-dlv.js-tabs .ao-pane{display:none;}
.ao-dlv.js-tabs .ao-pane.on{display:block;}
.ao-dlv.js-tabs .ao-pane > h2:first-child{margin-top:26px;}
.ao-dlv .ao-dlv-cta a{width:auto;min-width:280px;max-width:100%;}
@media(max-width:600px){.ao-dlv .ao-dlv-cta a{width:100%;min-width:0;max-width:320px;white-space:normal;}}
/* v3：分頁改為格狀按鈕，全部一次顯示（桌面 3 欄、手機 2 欄） */
.ao-dlv .ao-tabwrap{margin:20px 0 6px;}
.ao-dlv .ao-tabwrap:before,.ao-dlv .ao-tabwrap:after,.ao-dlv .ao-tabhint{display:none!important;}
.ao-dlv .ao-tabs{display:grid!important;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;height:auto!important;overflow:visible!important;border:0!important;margin:0!important;padding:0;}
.ao-dlv .ao-tabs a{flex:none!important;height:auto!important;min-height:48px;padding:10px 12px!important;white-space:normal!important;text-align:center;line-height:1.3!important;font-size:15px;border:1.5px solid #E4DAC6!important;border-radius:12px;background:#FAF7F1;color:#5E5648;box-shadow:none!important;letter-spacing:0;}
.ao-dlv .ao-tabs a:hover{border-color:#C8A24A!important;color:#1A1A1A;}
.ao-dlv .ao-tabs a.on{background:#1A1A1A;border-color:#1A1A1A!important;color:#F7CE46!important;box-shadow:none!important;}
@media(max-width:600px){.ao-dlv .ao-tabs{grid-template-columns:repeat(2,minmax(0,1fr));gap:8px;}.ao-dlv .ao-tabs a{min-height:46px;font-size:14px!important;padding:8px 8px!important;}}
/* v3：CTA 按鈕字一定在按鈕內 */
.ao-dlv .ao-dlv-cta a{display:inline-flex!important;align-items:center;justify-content:center;width:auto!important;min-width:260px;max-width:100%;padding:14px 30px!important;white-space:nowrap!important;box-sizing:border-box;}
@media(max-width:600px){.ao-dlv .ao-dlv-cta{flex-direction:column;align-items:center;}.ao-dlv .ao-dlv-cta a{width:100%!important;min-width:0;max-width:340px;white-space:normal!important;padding:13px 18px!important;}}'''

JS = '''<script>(function(){var r=document.querySelector(".ao-dlv");if(!r)return;var n=r.querySelector(".ao-tabs");if(!n)return;var T=[].slice.call(n.querySelectorAll("a")),P=T.map(function(a){return document.getElementById(a.getAttribute("href").slice(1))});if(P.some(function(p){return !p}))return;r.classList.add("js-tabs");n.setAttribute("role","tablist");var W=n.parentNode;function edge(){var x=n.scrollLeft,m=n.scrollWidth-n.clientWidth;W.classList.toggle("can-l",x>4);W.classList.toggle("can-r",x<m-4);}function show(i,push){T.forEach(function(a,k){var on=k===i;a.classList.toggle("on",on);a.setAttribute("aria-selected",on?"true":"false");P[k].classList.toggle("on",on);});var a=T[i];if(n.scrollWidth>n.clientWidth)n.scrollTo({left:a.offsetLeft-(n.clientWidth-a.offsetWidth)/2,behavior:"smooth"});if(push&&history.replaceState)history.replaceState(null,"","#"+P[i].id);}function toTop(){var top=W.getBoundingClientRect().top+window.pageYOffset-120;if(window.pageYOffset>top)window.scrollTo({top:top,behavior:"smooth"});}T.forEach(function(a,i){a.setAttribute("role","tab");P[i].setAttribute("role","tabpanel");a.addEventListener("click",function(e){e.preventDefault();show(i,true);toTop();});});function fromHash(){var h=location.hash.slice(1);if(!h)return 0;var el=document.getElementById(h);if(!el)return 0;for(var k=0;k<P.length;k++){if(P[k]===el||P[k].contains(el))return k;}return 0;}show(fromHash(),false);window.addEventListener("hashchange",function(){show(fromHash(),false);});n.addEventListener("scroll",edge,{passive:true});window.addEventListener("resize",edge);edge();setTimeout(function(){if(n.scrollWidth>n.clientWidth+4&&n.scrollLeft<4){n.scrollTo({left:60,behavior:"smooth"});setTimeout(function(){n.scrollTo({left:0,behavior:"smooth"})},650);}},900);})();</script>'''


def build(body):
    body = body.strip()
    # 天氣由 h3 升為 h2（獨立分頁）
    body = re.sub(r'<h3 id="weather">(.*?)</h3>', r'<h2 id="weather">\1</h2>', body)
    nav_end = body.index('</nav>')
    head_end = body.index('</div>', nav_end) + 6
    head, rest = body[:head_end], body[head_end:]
    ld = rest.index('<script type="application/ld+json">')
    content, tail = rest[:ld], rest[ld:]
    # 按 h2 id 切成分頁，id 由 h2 移到 section
    parts = re.split(r'(?=<h2 id=")', content)
    out = [parts[0].strip()] if parts[0].strip() else []
    seen = []
    for p in parts[1:]:
        pid = re.match(r'<h2 id="([^"]+)">', p).group(1)
        seen.append(pid)
        p = p.replace(f'<h2 id="{pid}">', '<h2>', 1).strip()
        out.append(f'<section class="ao-pane" id="{pid}">\n{p}\n</section>')
    assert seen == IDS, seen
    return '<div class="ao-dlv">\n<style>\n' + CSS + '\n</style>\n\n' + head + '\n\n' + '\n\n'.join(out) + '\n' + tail.strip() + '\n' + JS + '\n</div>\n'


en_body = src_en[src_en.index('</style>') + 8: src_en.index('<script>(function(){')]
zh_body = open(os.path.join(HERE, 'zh_body_src.html'), encoding='utf-8').read()

if __name__ == '__main__':
    open(os.path.join(HERE, 'zh-rawhtml.html'), 'w', encoding='utf-8').write(build(zh_body))
    open(os.path.join(HERE, 'en-rawhtml.html'), 'w', encoding='utf-8').write(build(en_body))
    print('ok')
