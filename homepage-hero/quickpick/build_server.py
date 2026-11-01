# -*- coding: utf-8 -*-
"""派對分類頁快選區塊：改為伺服器端輸出（WPCode PHP snippet），避免 JS 延遲插入造成 CLS／LCP。
來源同 build_live.py（option-b.html），輸出 party-quickpick-server-snippet.txt"""
import re, json
c = open('option-b.html', encoding='utf-8').read()
c = re.sub(r'<!--.*?-->', '', c, flags=re.S)
sec = re.search(r'<section class="ao-qp.*?</section>', c, re.S).group(0)
css = re.search(r'<style>(.*?)</style>', c, re.S).group(1)
scripts = re.findall(r'<script>(.*?)</script>', c, re.S)
m = re.search(r' style="(background-image:[^"]*)"', sec)
hdr_css = ''
if m:
    hdr_css = '.ao-qp-head--photo{' + m.group(1).replace('&quot;', '"') + '}'
    sec = sec.replace(m.group(0), '')
sec = re.sub(r'>\s+<', '><', ' '.join(l.strip() for l in sec.split('\n') if l.strip()))
css = ' '.join(l.strip() for l in css.split('\n') if l.strip()) + hdr_css
seo_css = re.search(r"cs\.textContent='(\.ao-cat-seo\{\{.*?)';document\.head", open('build_live.py', encoding='utf-8').read(), re.S).group(1).replace('{{', '{').replace('}}', '}')
js = '\n'.join(scripts).replace('document.currentScript&&document.currentScript.previousElementSibling', "document.querySelector('.ao-qp')")
for bad in ['?>', '<?', '$_']:
    assert bad not in css + sec + js + seo_css, bad
php = """/**
 * Kitchen AO - Party category quick-pick (server-side, fixes CLS/LCP)
 * WPCode: PHP Snippet, Auto Insert, Run Everywhere
 * Replaces the term description output on /product-category/party/ (page 1 only).
 * The old JS loader (party-quickpick.js) exits automatically when #ao-qp-css exists.
 */
add_action( 'wp', function () {
	if ( is_admin() || ! function_exists( 'is_product_category' ) || ! is_product_category( 'party' ) ) { return; }
	if ( absint( get_query_var( 'paged' ) ) > 1 ) { return; }
	remove_action( 'woocommerce_archive_description', 'woocommerce_taxonomy_archive_description', 10 );
	add_action( 'woocommerce_archive_description', 'ao_qp_party_output', 10 );
	add_action( 'wp_footer', 'ao_qp_party_js', 30 );
} );
function ao_qp_party_output() {
	$t    = get_queried_object();
	$desc = ( $t && ! empty( $t->description ) ) ? wc_format_content( wp_kses_post( $t->description ) ) : '';
	echo '<style id="ao-qp-css">' . <<<'AOQPCSS'
__CSS__
AOQPCSS
	. '</style>';
	echo '<div class="term-description">' . <<<'AOQPSEC'
__SEC__
AOQPSEC
	. ( $desc ? '<div class="ao-cat-seo">' . $desc . '</div>' : '' ) . '</div>';
}
function ao_qp_party_js() {
	echo '<script id="ao-qp-js">' . <<<'AOQPJS'
(function(){
__JS__
})();
AOQPJS
	. '</script>';
}
"""
php = php.replace('__CSS__', css + ' ' + seo_css).replace('__SEC__', sec).replace('__JS__', js)
open('party-quickpick-server-snippet.txt', 'w', encoding='utf-8').write(php)
print(len(php), len(css), len(sec), len(js))

# ---------- 不用 snippet 版：直接貼入「商品 → 分類 → 派對到會套餐 → 描述」 ----------
DESC = '<p>Kitchen AO <strong>香港派對到會套餐</strong>，適合生日派對、朋友聚會、公司活動及船河派對，2 人至 100 人以上均可選擇，全港送遞。想慢慢比較？可用下方<strong>價錢範圍</strong>及<strong>分類</strong>，瀏覽全部派對到會套餐。</p>'
js_lines = [l.rstrip() for l in js.split('\n') if l.strip()]
assert not any(re.match(r'\s*//', l) for l in js_lines)
html = ('<style id="ao-qp-css">' + css + ' ' + seo_css + '</style>' + sec +
        '<div class="ao-cat-seo">' + DESC + '</div>' +
        '<script>(function(){\n' + '\n'.join(js_lines) + '\n})();</script>')
assert '\n\n' not in html
open('party-category-description.html', 'w', encoding='utf-8').write(html)
print('desc html', len(html), html.count('\n'))
