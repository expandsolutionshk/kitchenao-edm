# -*- coding: utf-8 -*-
"""產生「一次性匯入英文 Meta」WPCode snippet（A：頁面、Blog、分類；B：產品）及審閱 Excel"""
import os
from en_meta_data import all_rows, kw_of, name_status
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
HERE = os.path.dirname(os.path.abspath(__file__))
q = lambda s: "'" + s.replace('\\', '\\\\').replace("'", "\\'") + "'"
R = all_rows()

def snippet(name, flag, rows):
    posts = [r for r in R if r in rows and r[0] in ('page', 'post', 'product')]
    terms = [r for r in rows if r[0] == 'term']
    spec = [r for r in rows if r[0] == 'special']
    L = [f"/**\n * Kitchen AO – 英文 Meta 一次性匯入 {name}（2026-10-28）",
         " * 用法：WPCode › PHP Snippet › Auto Insert › Admin Only（或 Run Everywhere）→ Active → Save",
         " *       儲存後打開任何後台頁面，頂部會顯示「已匯入 N 項」→ 之後把此 snippet 轉為 Inactive",
         " * 只會填入空白的 English SEO 方格，已填的內容不會被覆蓋。需要「中英文版通用工具 v2」已啟用。\n */",
         "add_action( 'admin_init', function () {",
         f"\tif ( get_option( '{flag}' ) || ! current_user_can( 'manage_options' ) ) return;",
         "\t$n = 0;"]
    if posts:
        L.append("\t$posts = array(")
        for r in posts: L.append(f"\t\t{r[1]} => array( {q(r[3])}, {q(r[4])} ), // {r[2][:24]}")
        L.append("\t);")
        L.append("\tforeach ( $posts as $id => $v ) {\n\t\tif ( ! get_post( $id ) ) continue;\n\t\tif ( get_post_meta( $id, '_ao_en_title', true ) === '' ) { update_post_meta( $id, '_ao_en_title', $v[0] ); $n++; }\n\t\tif ( get_post_meta( $id, '_ao_en_desc', true ) === '' ) { update_post_meta( $id, '_ao_en_desc', $v[1] ); }\n\t}")
    if terms:
        L.append("\t$terms = array(")
        for r in terms: L.append(f"\t\t{r[1]} => array( {q(r[3])}, {q(r[4])} ), // {r[2][:24]}")
        L.append("\t);")
        L.append("\tforeach ( $terms as $id => $v ) {\n\t\tif ( ! term_exists( (int) $id ) ) continue;\n\t\tif ( get_term_meta( $id, '_ao_en_title', true ) === '' ) { update_term_meta( $id, '_ao_en_title', $v[0] ); $n++; }\n\t\tif ( get_term_meta( $id, '_ao_en_desc', true ) === '' ) { update_term_meta( $id, '_ao_en_desc', $v[1] ); }\n\t}")
    for r in spec:
        idexpr = "(int) get_option( 'page_for_posts' )" if r[1] == 'blog' else "( function_exists( 'wc_get_page_id' ) ? (int) wc_get_page_id( 'shop' ) : 0 )"
        L.append(f"\t$sid = {idexpr}; // {r[2]}\n\tif ( $sid && get_post_meta( $sid, '_ao_en_title', true ) === '' ) {{ update_post_meta( $sid, '_ao_en_title', {q(r[3])} ); update_post_meta( $sid, '_ao_en_desc', {q(r[4])} ); $n++; }}")
    L += [f"\tupdate_option( '{flag}', $n . ' 項 @ ' . current_time( 'mysql' ), false );",
          "\tset_transient( 'ao_en_import_msg', '" + name + "：已匯入 ' . $n . ' 項英文 Meta（已有內容的方格沒有改動）。請把此 snippet 轉為 Inactive。', 300 );",
          "} );",
          "add_action( 'admin_notices', function () {",
          "\t$m = get_transient( 'ao_en_import_msg' );",
          "\tif ( $m ) { echo '<div class=\"notice notice-success\"><p>' . esc_html( $m ) . '</p></div>'; delete_transient( 'ao_en_import_msg' ); }",
          "} );"]
    return '\n'.join(L) + '\n'

A = [r for r in R if r[0] in ('page', 'post', 'term', 'special')]
Bp = [r for r in R if r[0] == 'product']
open(os.path.join(HERE, 'en-meta-import-A-pages-blog-categories.txt'), 'w', encoding='utf-8').write(snippet('A（頁面、Blog、分類）', 'ao_en_import_a_20261028', A))
open(os.path.join(HERE, 'en-meta-import-B-products.txt'), 'w', encoding='utf-8').write(snippet('B（產品）', 'ao_en_import_b_20261028', Bp))

wb = Workbook(); ws = wb.active; ws.title = '全網英文 Meta'
TY = {'page': '頁面', 'post': 'Blog', 'product': '產品', 'term': '產品分類', 'special': '頁面（商店／Blog 列表）'}
ws.append(['類型', 'ID', '中文頁面', 'English Title', '字元', 'English Meta Description', '字元', '主要英文關鍵字（月搜／GSC 曝光）', '網站英文產品名狀態', '匯入檔'])
for r in R:
    ws.append([TY[r[0]], r[1], r[2], r[3], len(r[3]), r[4], len(r[4]), kw_of(r[0], r[1]), name_status(r[0], r[1]), 'B' if r[0] == 'product' else 'A'])
for c in ws[1]: c.font = Font(name='Arial', bold=True, color='F7CE46'); c.fill = PatternFill('solid', fgColor='1A1A1A')
for row in ws.iter_rows(min_row=2):
    for c in row: c.font = Font(name='Arial'); c.alignment = Alignment(wrap_text=True, vertical='top')
for col, w in zip('ABCDEFGHIJ', [12, 8, 30, 48, 6, 70, 6, 40, 40, 8]): ws.column_dimensions[col].width = w
ws.freeze_panes = 'D2'; ws.auto_filter.ref = f'A1:J{ws.max_row}'
Y = PatternFill('solid', fgColor='FFF2A8')
for row in ws.iter_rows(min_row=2):
    if row[7].value:
        for c in row: c.fill = Y
    if row[8].value and not str(row[8].value).startswith('沿用'):
        row[8].fill = PatternFill('solid', fgColor='FAD4D4')
wb.save(os.path.join(HERE, '全網英文Meta_2026-10-28.xlsx'))
print(len(A), len(Bp))
