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
.ao-dlv.js-tabs .ao-pane > h2:first-child{margin-top:26px;}'''

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
