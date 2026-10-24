// Kitchen AO 首頁（中英文版）｜由 homepage-bilingual/build.py 生成，請勿直接修改
// WPCode：PHP Snippet，Insert Method 選 Auto Insert › Run Everywhere；首頁用 [ao_home] 放入
add_shortcode( 'ao_home', function () {
    global $TRP_LANGUAGE;
    $en  = ! empty( $TRP_LANGUAGE ) && strpos( $TRP_LANGUAGE, 'en' ) === 0;
    $css = <<<'AOCSS'

/* 首頁：WPBakery 自訂樣式（原本由頁面輸出） */
.vc_custom_1776576454166{padding-top:0!important;padding-bottom:0!important}
.vc_custom_1775899549282{padding-top:80px!important;padding-bottom:80px!important;background-color:#F8F6F2!important}
.vc_custom_1775901384920{padding-top:60px!important;padding-bottom:60px!important;background-color:#F8F6F2!important}
.vc_custom_1775902198440{background-color:#F8F6F2!important}
.ao-home h2.h1title{font-size:24px;line-height:1.4;margin:0 0 10px}
/* 會員優惠跑馬燈 */
.ao-promo{background:#fff;padding:20px 0 0}
.ao-mq{overflow:hidden;white-space:nowrap;color:#2448b8;font-size:15px;line-height:1.8;padding:6px 0}
.ao-mq-track{display:inline-flex;gap:100px;animation:aoMq 40s linear infinite}
.ao-mq:hover .ao-mq-track{animation-play-state:paused}
@keyframes aoMq{from{transform:translateX(0)}to{transform:translateX(calc(-50% - 50px))}}
/* 輪播圖 */
.ao-sl{position:relative;max-width:1240px;margin:10px auto 0}
.ao-sl-track{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;scrollbar-width:none;scroll-behavior:smooth}
.ao-sl-track::-webkit-scrollbar{display:none}
.ao-sl-item{flex:0 0 100%;scroll-snap-align:center}
.ao-sl-item img{display:block;width:100%;height:auto}
.ao-sl-dots{display:flex;justify-content:center;gap:6px;padding:10px 0}
.ao-sl-dot{width:10px;height:10px;padding:0;border:1px solid #333;border-radius:0;background:#333;cursor:pointer}
.ao-sl-dot.on{background:#fff}
@media (prefers-reduced-motion:reduce){.ao-mq-track{animation:none}}

AOCSS;
    $js  = <<<'AOJS'
(function(){document.querySelectorAll('.ao-sl').forEach(function(s){var t=s.querySelector('.ao-sl-track'),d=s.querySelectorAll('.ao-sl-dot'),n=d.length,i=0,tm;
function go(k){i=(k+n)%n;t.scrollTo({left:t.clientWidth*i});d.forEach(function(x,j){x.classList.toggle('on',j===i)});}
function auto(){clearInterval(tm);tm=setInterval(function(){go(i+1)},8000);}
d.forEach(function(x,j){x.addEventListener('click',function(){go(j);auto();})});
t.addEventListener('scroll',function(){var k=Math.round(t.scrollLeft/t.clientWidth);if(k!==i){i=k;d.forEach(function(x,j){x.classList.toggle('on',j===i)});}},{passive:true});
go(0);auto();});})();
AOJS;
    $form = do_shortcode( '[fluentform id="4"]' );
    if ( $en ) {
        $a = <<<'AOENA'
<div data-vc-full-width="true" data-vc-full-width-init="false" data-vc-stretch-content="true" class="vc_row wpb_row vc_row-fluid vc_custom_1776576454166 vc_row-has-fill vc_row-o-content-middle vc_row-flex lafka-align-center">
    <div class="wpb_column vc_column_container vc_col-sm-12"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_raw_code wpb_raw_html wpb_content_element">
		<div class="wpb_wrapper">
			<section class="ao-hero" style="padding:36px 20px;background:linear-gradient(180deg,#fbf8f3 0%,#f5efe7 100%);">
  <div class="ao-hero-grid" style="max-width:1240px;margin:0 auto;display:grid;grid-template-columns:1.05fr 0.95fr;gap:28px;align-items:center;">
    <div style="order:1;">
      <div style="display:inline-block;margin:0 0 12px;padding:6px 12px;border-radius:999px;background:#efe4d1;color:#7d5b27;font-size:12px;font-weight:800;letter-spacing:0.08em;line-height:1.2;">
        KITCHEN AO HONG KONG CATERING
      </div>
      <h1 style="margin:0 0 14px;color:#201814;font-size:42px;line-height:1.15;font-weight:800;">
        <span class="ao-nw">Party Catering · </span><span class="ao-nw">Corporate Events</span><br>All in One Place
      </h1>
      <p style="margin:0 0 18px;max-width:620px;color:#5d534d;font-size:17px;line-height:1.9;">
        Kitchen AO provides catering across Hong Kong for birthday parties, corporate events, family gatherings, boat parties and brand events. From elegant platters and signature hot dishes to themed menus, we make every gathering easier and more impressive.
      </p>
      <div class="ao-hero-ctas">
        <a class="ao-hero-btn" href="https://aoaodelivery.com/en/product-category/party/" onclick="window.dataLayer=window.dataLayer||[];dataLayer.push({event:'cta_click',cta_label:'view_menu'});" style="display:inline-block;padding:14px 22px;border-radius:999px;background:#1f1714;color:#ffffff;text-decoration:none;font-size:15px;font-weight:800;line-height:1.2;">
          View Menu
        </a>
        <a class="ao-hero-btn" href="https://wa.me/85269011987?text=Hi, I would like to ask about Kitchen AO catering menus and a quote" target="_blank" rel="noopener noreferrer" onclick="window.dataLayer=window.dataLayer||[];dataLayer.push({event:'cta_click',cta_label:'whatsapp'});" style="display:inline-block;padding:14px 22px;border-radius:999px;background:#d9b06a;color:#241a12;text-decoration:none;font-size:15px;font-weight:800;line-height:1.2;">
          WhatsApp Us
        </a>
        <a class="ao-hero-btn" href="https://aoaodelivery.com/en/catering-quote-enquiry/" onclick="window.dataLayer=window.dataLayer||[];dataLayer.push({event:'cta_click',cta_label:'quote_form'});" style="display:inline-block;padding:12px 20px;border-radius:999px;background:#ffffff;color:#1f1714;text-decoration:none;font-size:15px;font-weight:800;line-height:1.2;border:2px solid #1f1714;">
          Get an Event Quote
        </a>
        <a class="ao-hero-btn ao-hero-hw" href="https://aoaodelivery.com/en/product-category/halloween-set/?ao_ref=hw26_home_hero" onclick="window.dataLayer=window.dataLayer||[];dataLayer.push({event:'cta_click',cta_label:'halloween_menu'});">
          <span class="ao-hero-bats" aria-hidden="true"><i class="b1"><svg viewBox="0 0 100 44"><path d="M50 18 L53 9 L55.5 17 C62 12 78 6 97 10 C89 14 85 20 87 27 C81 22 75 22 71 29 C67 24 61 24 57.5 31 C55 29 52.5 33 50 38 C47.5 33 45 29 42.5 31 C39 24 33 24 29 29 C25 22 19 22 13 27 C15 20 11 14 3 10 C22 6 38 12 44.5 17 L47 9 Z" fill="#2a0d3d"></path><circle cx="47.6" cy="20" r="1.6" fill="#FFE14D"></circle><circle cx="52.4" cy="20" r="1.6" fill="#FFE14D"></circle></svg></i><i class="b2"><svg viewBox="0 0 100 44"><path d="M50 18 L53 9 L55.5 17 C62 12 78 6 97 10 C89 14 85 20 87 27 C81 22 75 22 71 29 C67 24 61 24 57.5 31 C55 29 52.5 33 50 38 C47.5 33 45 29 42.5 31 C39 24 33 24 29 29 C25 22 19 22 13 27 C15 20 11 14 3 10 C22 6 38 12 44.5 17 L47 9 Z" fill="#2a0d3d"></path><circle cx="47.6" cy="20" r="1.6" fill="#FFE14D"></circle><circle cx="52.4" cy="20" r="1.6" fill="#FFE14D"></circle></svg></i><i class="b3"><svg viewBox="0 0 100 44"><path d="M50 18 L53 9 L55.5 17 C62 12 78 6 97 10 C89 14 85 20 87 27 C81 22 75 22 71 29 C67 24 61 24 57.5 31 C55 29 52.5 33 50 38 C47.5 33 45 29 42.5 31 C39 24 33 24 29 29 C25 22 19 22 13 27 C15 20 11 14 3 10 C22 6 38 12 44.5 17 L47 9 Z" fill="#2a0d3d"></path><circle cx="47.6" cy="20" r="1.6" fill="#FFE14D"></circle><circle cx="52.4" cy="20" r="1.6" fill="#FFE14D"></circle></svg></i></span>
          <span class="ao-hero-hw-txt">🎃 Halloween Party Sets <small>Delivery 23 Oct – 1 Nov</small></span>
        </a>
      </div>
      <div class="ao-hero-feats" style="display:flex;flex-wrap:wrap;gap:8px 18px;color:#6a5f58;font-size:14px;line-height:1.7;">
        <div style="white-space:nowrap;">Birthday parties</div>
        <div style="white-space:nowrap;">Corporate Events</div>
        <div style="white-space:nowrap;">Elegant platters</div>
      </div>
    </div>
    <div style="order:2;">
      <div style="position:relative;background:#ffffff;border-radius:26px;padding:14px;box-shadow:0 20px 40px rgba(40,24,15,0.10);">
        <img class="ao-hero-img" src="https://aoaodelivery.com/wp-content/uploads/2026/07/catering-hongkong-corporate.jpg" alt="Kitchen AO catering service with an elegant food display" width="1200" height="1400" fetchpriority="high" decoding="async" style="display:block;width:100%;height:680px;object-fit:cover;object-position:center top;border-radius:18px;">
      </div>
    </div>
  </div>
</section>
<style>
.ao-hero-feats > div::before{content:"\2714\00A0";}
.ao-hero .ao-nw{white-space:nowrap;}

/* ===== CTA：3 個一行等闊，Halloween 掣喺下面同一闊度 ===== */
.ao-hero-ctas{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;max-width:620px;margin:0 0 18px;}
.ao-hero-ctas .ao-hero-btn{display:flex !important;align-items:center;justify-content:center;min-height:50px;box-sizing:border-box;text-align:center;white-space:nowrap;}

/* ===== Halloween CTA（同 Pop up 一樣：漸變 + 反光 + 搖動 + 蝙蝠）===== */
.ao-hero-ctas .ao-hero-hw{grid-column:1 / -1;position:relative;overflow:hidden;padding:12px 20px;border-radius:999px;background:linear-gradient(135deg,#FF8A1F 0%,#FF5A00 100%);color:#1c1426 !important;text-decoration:none !important;font-size:16px;font-weight:800;line-height:1.25;box-shadow:0 6px 18px rgba(255,90,0,.40);animation:aoHeroWiggle 3.2s ease-in-out infinite;}
.ao-hero-ctas .ao-hero-hw::after{content:"";position:absolute;top:0;left:-60%;width:40%;height:100%;background:linear-gradient(100deg,rgba(255,255,255,0),rgba(255,255,255,.65),rgba(255,255,255,0));transform:skewX(-20deg);animation:aoHeroShine 2.8s ease-in-out infinite;z-index:3;pointer-events:none;}
.ao-hero-hw-txt{position:relative;z-index:2;}
.ao-hero img.emoji,.ao-hero img.wp-smiley{display:inline !important;width:1em !important;height:1em !important;margin:0 .15em 0 0 !important;vertical-align:-0.12em !important;border:0 !important;box-shadow:none !important;}
.ao-hero-hw-txt small{display:inline-block;margin-left:8px;padding:2px 9px;border-radius:999px;background:rgba(28,20,38,.85);color:#FFB347;font-size:12px;font-weight:700;vertical-align:2px;}
.ao-hero-bats{position:absolute;inset:0;z-index:1;pointer-events:none;}
.ao-hero-bats i{position:absolute;top:50%;left:-12%;width:36px;margin-top:-7px;animation:aoHeroBat 5s linear infinite;}
.ao-hero-bats i.b2{width:26px;margin-top:-15px;animation-duration:6s;animation-delay:1.6s;}
.ao-hero-bats i.b3{width:30px;margin-top:1px;animation-duration:5.5s;animation-delay:3.2s;}
.ao-hero-bats svg{display:block;width:100%;height:auto;transform-origin:50% 40%;animation:aoHeroFlap .16s ease-in-out infinite alternate;}
@keyframes aoHeroShine{0%{left:-60%;}55%,100%{left:130%;}}
@keyframes aoHeroWiggle{0%,78%,100%{transform:rotate(0) scale(1);}82%{transform:rotate(-1.5deg) scale(1.03);}86%{transform:rotate(1.5deg) scale(1.03);}90%{transform:rotate(-1deg) scale(1.015);}94%{transform:rotate(.6deg) scale(1.005);}}
@keyframes aoHeroBat{0%{left:-12%;transform:translateY(4px);}25%{transform:translateY(-6px);}50%{transform:translateY(5px);}75%{transform:translateY(-5px);}100%{left:108%;transform:translateY(3px);}}
@keyframes aoHeroFlap{from{transform:scaleY(1);}to{transform:scaleY(.55) scaleX(.92);}}
@media (prefers-reduced-motion:reduce){.ao-hero-bats{display:none;}.ao-hero-ctas .ao-hero-hw,.ao-hero-ctas .ao-hero-hw::after{animation:none;}}

@media (max-width:960px){
  .ao-hero-grid{grid-template-columns:1fr !important;gap:22px !important;}
  .ao-hero h1{font-size:34px !important;}
  .ao-hero .ao-hero-img{height:520px !important;}
}
@media (max-width:640px){
  .ao-hero{padding:28px 16px !important;}
  .ao-hero h1{font-size:28px !important;line-height:1.2 !important;}
  .ao-hero p{font-size:15px !important;line-height:1.8 !important;}
  .ao-hero .ao-hero-img{height:420px !important;object-position:center top !important;}
  .ao-hero-ctas{grid-template-columns:1fr;gap:10px;max-width:none;}
  .ao-hero-ctas .ao-hero-btn{width:100%;}
  .ao-hero-ctas .ao-hero-hw{flex-direction:column;}
  .ao-hero-hw-txt small{display:block;width:max-content;margin:5px auto 0;vertical-align:0;}
  .ao-hero-feats{flex-direction:column;gap:6px;}
}
</style>

		</div>
	</div>
</div></div></div></div>
<section class="ao-promo"><div class="ao-mq" aria-label="Offer"><div class="ao-mq-track"><span>Returning customer offer: we automatically discount this order based on your previous order. Previous order of $2,000 or more: $100 off; $4,000 or more: $200 off, and so on. Can be combined with &quot;Buy &amp; Get&quot; offers, but orders cannot be merged and the offer does not apply to orders placed manually by our customer service team.</span><span aria-hidden="true">Returning customer offer: we automatically discount this order based on your previous order. Previous order of $2,000 or more: $100 off; $4,000 or more: $200 off, and so on. Can be combined with &quot;Buy &amp; Get&quot; offers, but orders cannot be merged and the offer does not apply to orders placed manually by our customer service team.</span></div></div><div class="ao-sl"><div class="ao-sl-track"><a class="ao-sl-item" href="https://aoaodelivery.com/en/product-category/halloween-set/"><img src="https://aoaodelivery.com/wp-content/uploads/2026/10/2025-Halloween-banner-1_banner_banner-scaled.jpg" srcset="https://aoaodelivery.com/wp-content/uploads/2026/10/2025-Halloween-banner-1_banner_banner-scaled.jpg 2560w, https://aoaodelivery.com/wp-content/uploads/2026/10/2025-Halloween-banner-1_banner_banner-300x140.jpg 300w, https://aoaodelivery.com/wp-content/uploads/2026/10/2025-Halloween-banner-1_banner_banner-1024x478.jpg 1024w, https://aoaodelivery.com/wp-content/uploads/2026/10/2025-Halloween-banner-1_banner_banner-768x358.jpg 768w, https://aoaodelivery.com/wp-content/uploads/2026/10/2025-Halloween-banner-1_banner_banner-1536x717.jpg 1536w, https://aoaodelivery.com/wp-content/uploads/2026/10/2025-Halloween-banner-1_banner_banner-2048x956.jpg 2048w, https://aoaodelivery.com/wp-content/uploads/2026/10/2025-Halloween-banner-1_banner_banner-18x8.jpg 18w, https://aoaodelivery.com/wp-content/uploads/2026/10/2025-Halloween-banner-1_banner_banner-1440x672.jpg 1440w, https://aoaodelivery.com/wp-content/uploads/2026/10/2025-Halloween-banner-1_banner_banner-100x47.jpg 100w, https://aoaodelivery.com/wp-content/uploads/2026/10/2025-Halloween-banner-1_banner_banner-600x280.jpg 600w" sizes="(max-width:1200px) 100vw, 1200px" width="2560" height="1195" alt="Halloween party catering sets" loading="eager" fetchpriority="high" decoding="async"></a><a class="ao-sl-item" href="https://aoaodelivery.com/en/product-category/party/foot-party/"><img src="https://aoaodelivery.com/wp-content/uploads/2026/03/WhatsApp-Image-2026-03-18-at-15.55.47-scaled.jpeg" srcset="https://aoaodelivery.com/wp-content/uploads/2026/03/WhatsApp-Image-2026-03-18-at-15.55.47-scaled.jpeg 2560w, https://aoaodelivery.com/wp-content/uploads/2026/03/WhatsApp-Image-2026-03-18-at-15.55.47-300x140.jpeg 300w, https://aoaodelivery.com/wp-content/uploads/2026/03/WhatsApp-Image-2026-03-18-at-15.55.47-1024x478.jpeg 1024w, https://aoaodelivery.com/wp-content/uploads/2026/03/WhatsApp-Image-2026-03-18-at-15.55.47-768x358.jpeg 768w, https://aoaodelivery.com/wp-content/uploads/2026/03/WhatsApp-Image-2026-03-18-at-15.55.47-1536x717.jpeg 1536w, https://aoaodelivery.com/wp-content/uploads/2026/03/WhatsApp-Image-2026-03-18-at-15.55.47-2048x956.jpeg 2048w, https://aoaodelivery.com/wp-content/uploads/2026/03/WhatsApp-Image-2026-03-18-at-15.55.47-1440x672.jpeg 1440w, https://aoaodelivery.com/wp-content/uploads/2026/03/WhatsApp-Image-2026-03-18-at-15.55.47-100x47.jpeg 100w, https://aoaodelivery.com/wp-content/uploads/2026/03/WhatsApp-Image-2026-03-18-at-15.55.47-600x280.jpeg 600w" sizes="(max-width:1200px) 100vw, 1200px" width="2560" height="1195" alt="Party catering sets" loading="lazy" decoding="async"></a><a class="ao-sl-item" href="https://aoaodelivery.com/en/product-category/party/foot-party/"><img src="https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠_工作區域-1-scaled.jpg" srcset="https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠_工作區域-1-scaled.jpg 2560w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠_工作區域-1-300x125.jpg 300w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠_工作區域-1-1024x426.jpg 1024w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠_工作區域-1-768x320.jpg 768w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠_工作區域-1-1536x639.jpg 1536w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠_工作區域-1-2048x852.jpg 2048w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠_工作區域-1-18x7.jpg 18w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠_工作區域-1-1440x599.jpg 1440w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠_工作區域-1-100x42.jpg 100w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠_工作區域-1-600x250.jpg 600w" sizes="(max-width:1200px) 100vw, 1200px" width="2560" height="1065" alt="Returning customer offer" loading="lazy" decoding="async"></a><a class="ao-sl-item" href="https://aoaodelivery.com/en/product-category/party/foot-party/"><img src="https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-02-scaled.jpg" srcset="https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-02-scaled.jpg 2560w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-02-300x125.jpg 300w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-02-1024x426.jpg 1024w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-02-768x320.jpg 768w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-02-1536x639.jpg 1536w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-02-2048x852.jpg 2048w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-02-18x7.jpg 18w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-02-1440x599.jpg 1440w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-02-100x42.jpg 100w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-02-600x250.jpg 600w" sizes="(max-width:1200px) 100vw, 1200px" width="2560" height="1065" alt="Returning customer offer" loading="lazy" decoding="async"></a><a class="ao-sl-item" href="https://aoaodelivery.com/en/product-category/party/foot-party/"><img src="https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-03-scaled.jpg" srcset="https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-03-scaled.jpg 2560w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-03-300x125.jpg 300w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-03-1024x426.jpg 1024w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-03-768x320.jpg 768w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-03-1536x639.jpg 1536w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-03-2048x852.jpg 2048w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-03-18x7.jpg 18w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-03-1440x599.jpg 1440w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-03-100x42.jpg 100w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-03-600x250.jpg 600w" sizes="(max-width:1200px) 100vw, 1200px" width="2560" height="1065" alt="Returning customer offer" loading="lazy" decoding="async"></a></div><div class="ao-sl-dots"><button type="button" class="ao-sl-dot" aria-label="Slide 1"></button><button type="button" class="ao-sl-dot" aria-label="Slide 2"></button><button type="button" class="ao-sl-dot" aria-label="Slide 3"></button><button type="button" class="ao-sl-dot" aria-label="Slide 4"></button><button type="button" class="ao-sl-dot" aria-label="Slide 5"></button></div></div></section>
<div class="vc_row wpb_row vc_row-fluid vc_custom_1775899549282 vc_row-has-fill vc_column-gap-20 vc_row-o-equal-height vc_row-flex">
    <div class="wpb_column vc_column_container vc_col-sm-12"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_text_column wpb_content_element">
		<div class="wpb_wrapper">
			
<h2 class="h1title" style="text-align: center;">Hong Kong Catering for Parties, Corporate Events and Boat Parties</h2>

		</div>
	</div>

	<div class="wpb_text_column wpb_content_element">
		<div class="wpb_wrapper">
			<div style="text-align: center; padding: 10px 0 20px;">
<h2 style="font-size: 38px; color: #1f1f1f; margin: 0 0 12px;">Catering for Every Occasion</h2>
<p style="font-size: 18px; color: #666; margin: 0;">From parties to corporate events, Kitchen AO offers flexible, well-presented catering.</p>
</div>

		</div>
	</div>
<div class="vc_row wpb_row vc_inner vc_row-fluid">
	<div class="wpb_column vc_column_container vc_col-sm-4"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_text_column wpb_content_element">
		<div class="wpb_wrapper">
			<div style="background: #ffffff; padding: 32px 26px; border-radius: 8px; box-shadow: 0 8px 24px rgba(0,0,0,0.06); text-align: center; height: 100%;">
<div style="font-size: 38px; line-height: 1; margin-bottom: 16px;">🎉</div>
<h3 style="font-size: 28px; color: #1f1f1f; margin: 0 0 12px;">Party Catering</h3>
<p style="font-size: 17px; color: #555; line-height: 1.8; margin: 0 0 18px;">Ideal for birthdays, friends’ gatherings and family meals, with flexible sets made for sharing.</p>
<p style="font-size: 15px; color: #888; line-height: 1.7; margin: 0;">From small gatherings to large parties</p>
</div>

		</div>
	</div>
</div></div></div><div class="wpb_column vc_column_container vc_col-sm-4"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_text_column wpb_content_element">
		<div class="wpb_wrapper">
			<div style="background: #ffffff; padding: 32px 26px; border-radius: 8px; box-shadow: 0 8px 24px rgba(0,0,0,0.06); text-align: center; height: 100%;">
<div style="font-size: 38px; line-height: 1; margin-bottom: 16px;">🏢</div>
<h3 style="font-size: 28px; color: #1f1f1f; margin: 0 0 12px;">Corporate Events</h3>
<p style="font-size: 17px; color: #555; line-height: 1.8; margin: 0 0 18px;">For meetings, opening receptions and staff meals, with consistent quality and punctual delivery.</p>
<p style="font-size: 15px; color: #888; line-height: 1.7; margin: 0;">Polished for business, easy to arrange</p>
</div>

		</div>
	</div>
</div></div></div><div class="wpb_column vc_column_container vc_col-sm-4"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_text_column wpb_content_element">
		<div class="wpb_wrapper">
			<div style="background: #ffffff; padding: 32px 26px; border-radius: 8px; box-shadow: 0 8px 24px rgba(0,0,0,0.06); text-align: center; height: 100%;">
<div style="font-size: 38px; line-height: 1; margin-bottom: 16px;">🚤</div>
<h3 style="font-size: 28px; color: #1f1f1f; margin: 0 0 12px;">Boat Parties & Business Lunches</h3>
<p style="font-size: 17px; color: #555; line-height: 1.8; margin: 0 0 18px;">For outings, boat parties and business lunches, kept warm and easy to serve.</p>
<p style="font-size: 15px; color: #888; line-height: 1.7; margin: 0;">Easy to carry, good-looking and practical</p>
</div>

		</div>
	</div>
</div></div></div></div>



<div class="vc_row wpb_row vc_inner vc_row-fluid vc_custom_1775900383223 vc_row-has-fill vc_column-gap-20 vc_row-o-equal-height vc_row-flex">
	<div class="wpb_column vc_column_container vc_col-sm-12"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_text_column wpb_content_element">
		<div class="wpb_wrapper">
			<div style="text-align: center; padding: 10px 0 20px;">
<h2 style="font-size: 38px; color: #1f1f1f; margin: 0 0 12px;">Popular Catering Sets</h2>
<p style="font-size: 18px; color: #666; margin: 0;">Our most popular menus for parties, corporate gatherings and light refreshments, so you can start ordering quickly.</p>
</div>

		</div>
	</div>
</div></div></div></div>



<div class="vc_row wpb_row vc_inner vc_row-fluid">
	<div class="wpb_column vc_column_container vc_col-sm-4"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_text_column wpb_content_element">
		<div class="wpb_wrapper">
			<div style="background: #ffffff; padding: 32px 26px; border-radius: 8px; box-shadow: 0 8px 24px rgba(0,0,0,0.06); text-align: center; height: 100%;">
<div style="font-size: 16px; color: #b38b2d; font-weight: bold; letter-spacing: 1px; margin-bottom: 10px;">PARTY SET</div>
<h3 style="font-size: 28px; color: #1f1f1f; margin: 0 0 12px;">Party Catering Sets</h3>
<p style="font-size: 17px; color: #555; line-height: 1.8; margin: 0 0 16px;">For birthdays, get-togethers and festive celebrations, with a generous variety for sharing.</p>
<p style="font-size: 16px; color: #888; margin: 0 0 22px;">Great for family gatherings and parties</p>
<p><a style="display: inline-block; background: #c9b18a; color: #ffffff; padding: 14px 24px; text-decoration: none; border-radius: 4px;" href="https://aoaodelivery.com/en/product-category/party/">View Sets</a></p>
</div>

		</div>
	</div>
</div></div></div><div class="wpb_column vc_column_container vc_col-sm-4"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_text_column wpb_content_element">
		<div class="wpb_wrapper">
			<div style="background: #ffffff; padding: 32px 26px; border-radius: 8px; box-shadow: 0 8px 24px rgba(0,0,0,0.06); text-align: center; height: 100%;">
<div style="font-size: 16px; color: #b38b2d; font-weight: bold; letter-spacing: 1px; margin-bottom: 10px;">REFRESHMENT</div>
<h3 style="font-size: 28px; color: #1f1f1f; margin: 0 0 12px;">Refreshment Sets</h3>
<p style="font-size: 17px; color: #555; line-height: 1.8; margin: 0 0 16px;">For meeting breaks, openings and afternoon tea, with refined bites that are easy to pick up.</p>
<p style="font-size: 16px; color: #888; margin: 0 0 22px;">Great for corporate and business events</p>
<p><a style="display: inline-block; background: #c9b18a; color: #ffffff; padding: 14px 24px; text-decoration: none; border-radius: 4px;" href="https://aoaodelivery.com/en/product-category/party/refreshment-set/">View Sets</a></p>
</div>

		</div>
	</div>
</div></div></div><div class="wpb_column vc_column_container vc_col-sm-4"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_text_column wpb_content_element">
		<div class="wpb_wrapper">
			<div style="background: #ffffff; padding: 32px 26px; border-radius: 8px; box-shadow: 0 8px 24px rgba(0,0,0,0.06); text-align: center; height: 100%;">
<div style="font-size: 16px; color: #b38b2d; font-weight: bold; letter-spacing: 1px; margin-bottom: 10px;">À LA CARTE</div>
<h3 style="font-size: 28px; color: #1f1f1f; margin: 0 0 12px;">À La Carte Selection</h3>
<p style="font-size: 17px; color: #555; line-height: 1.8; margin: 0 0 16px;">Mix and match snacks, mains, desserts and drinks to build the menu you need.</p>
<p style="font-size: 16px; color: #888; margin: 0 0 22px;">Add extras or create your own menu</p>
<p><a style="display: inline-block; background: #c9b18a; color: #ffffff; padding: 14px 24px; text-decoration: none; border-radius: 4px;" href="https://aoaodelivery.com/en/product-category/a-la-carte/">Browse Dishes</a></p>
</div>

		</div>
	</div>
</div></div></div></div>



<div class="vc_row wpb_row vc_inner vc_row-fluid">
	<div class="wpb_column vc_column_container vc_col-sm-12"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_raw_code wpb_raw_html wpb_content_element">
		<div class="wpb_wrapper">
			<div style="margin:16px 0 22px;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'PingFang TC','Noto Sans TC','Microsoft JhengHei',sans-serif;">

  <a href="https://aoaodelivery.com/en/product-category/party/foot-party/" style="display:block;text-decoration:none;margin-bottom:10px;">
    <img decoding="async" src="https://aoaodelivery.com/wp-content/uploads/2026/07/左口魚煲仔飯-黑白叉燒-到會-catering-1000px.jpg" alt="Kitchen AO x 101wine group new Black &amp; White Char Siu banner" style="display:block;width:100%;height:auto;border-radius:18px;box-shadow:0 10px 24px rgba(0,0,0,0.12);">
  </a>

  <div style="padding:14px 16px;border-radius:16px;background:linear-gradient(135deg,#251915 0%,#4a2c22 55%,#16110f 100%);border:1px solid rgba(214,180,104,0.24);box-shadow:0 10px 24px rgba(23,17,12,0.10);text-align:center;">
    
    <div style="margin:0 0 6px;color:#f8f1e7;font-size:16px;font-weight:800;line-height:1.5;">
      New Black & White Char Siu: Limited Offer
    </div>

    <div style="margin:0 0 12px;color:rgba(245,237,226,0.88);font-size:14px;line-height:1.7;">
      Enter promo code <strong style="color:#f0d39a;">WIN95</strong> for 5% off your whole order.
    </div>

    <a href="https://wa.me/85269011987?text=Hi, I would like to ask about the new Black & White Char Siu and the WIN95 offer" target="_blank" rel="noopener noreferrer" style="display:inline-block;padding:13px 22px;border-radius:999px;background:linear-gradient(135deg,#f0d39a 0%,#d2a44e 100%);color:#241a12 !important;text-decoration:none;font-size:15px;font-weight:800;line-height:1.2;box-shadow:0 8px 18px rgba(0,0,0,0.14);">
      Ask about WIN95
    </a>

  </div>

</div>
		</div>
	</div>
</div></div></div></div>



</div></div></div></div>

AOENA;
        $b = <<<'AOENB'

<div class="vc_row wpb_row vc_row-fluid vc_custom_1775901384920 vc_row-has-fill vc_column-gap-20 vc_row-o-equal-height vc_row-flex">
    <div class="wpb_column vc_column_container vc_col-sm-12"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_text_column wpb_content_element">
		<div class="wpb_wrapper">
			<div style="text-align: center; padding: 10px 0 20px;">
<h2 style="font-size: 38px; color: #1f1f1f; margin: 0 0 12px;">Why Choose Kitchen AO?</h2>
<p style="font-size: 18px; color: #666; margin: 0;">From ingredients and cooking to delivery, we want every important occasion to feel effortless and impressive.</p>
</div>

		</div>
	</div>
<div class="vc_row wpb_row vc_inner vc_row-fluid vc_custom_1775901425810 vc_row-has-fill vc_column-gap-20">
	<div class="wpb_column vc_column_container vc_col-sm-3"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_single_image wpb_content_element vc_align_center wpb_content_element">
		
		<figure class="wpb_wrapper vc_figure">
			<div class="vc_single_image-wrapper   vc_box_border_grey"><img loading="lazy" decoding="async" width="150" height="150" src="https://aoaodelivery.com/wp-content/uploads/2025/04/person_14933728-150x150.png" class="vc_single_image-img attachment-thumbnail" alt="" title="Kitchen AO chef team preparing catering dishes" srcset="https://aoaodelivery.com/wp-content/uploads/2025/04/person_14933728-150x150.png 150w, https://aoaodelivery.com/wp-content/uploads/2025/04/person_14933728-300x300.png 300w, https://aoaodelivery.com/wp-content/uploads/2025/04/person_14933728-12x12.png 12w, https://aoaodelivery.com/wp-content/uploads/2025/04/person_14933728-100x100.png 100w, https://aoaodelivery.com/wp-content/uploads/2025/04/person_14933728-60x60.png 60w, https://aoaodelivery.com/wp-content/uploads/2025/04/person_14933728.png 512w" sizes="auto, (max-width: 150px) 100vw, 150px"></div>
		</figure>
	</div>

	<div class="wpb_text_column wpb_content_element">
		<div class="wpb_wrapper">
			<div style="background: #ffffff; padding: 32px 26px; border-radius: 8px; box-shadow: 0 8px 24px rgba(0,0,0,0.06); text-align: center; height: 100%;">
<h3 style="font-size: 28px; color: #1f1f1f; margin: 0 0 12px;">Hotel-Trained Chefs</h3>
<p style="font-size: 17px; color: #555; line-height: 1.8; margin: 0 0 18px;">Our experienced chefs focus on ingredients, flavour and presentation, raising the standard of every dish.</p>
<p style="font-size: 15px; color: #888; line-height: 1.7; margin: 0;">For occasions where quality and image matter</p>
</div>

		</div>
	</div>
</div></div></div><div class="wpb_column vc_column_container vc_col-sm-3"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_single_image wpb_content_element vc_align_center wpb_content_element">
		
		<figure class="wpb_wrapper vc_figure">
			<div class="vc_single_image-wrapper   vc_box_border_grey"><img loading="lazy" decoding="async" width="150" height="150" src="https://aoaodelivery.com/wp-content/uploads/2025/04/salad_649363-150x150.png" class="vc_single_image-img attachment-thumbnail" alt="" title="Kitchen AO catering menu variety in Hong Kong" srcset="https://aoaodelivery.com/wp-content/uploads/2025/04/salad_649363-150x150.png 150w, https://aoaodelivery.com/wp-content/uploads/2025/04/salad_649363-300x300.png 300w, https://aoaodelivery.com/wp-content/uploads/2025/04/salad_649363-12x12.png 12w, https://aoaodelivery.com/wp-content/uploads/2025/04/salad_649363-100x100.png 100w, https://aoaodelivery.com/wp-content/uploads/2025/04/salad_649363-60x60.png 60w, https://aoaodelivery.com/wp-content/uploads/2025/04/salad_649363.png 512w" sizes="auto, (max-width: 150px) 100vw, 150px"></div>
		</figure>
	</div>

	<div class="wpb_text_column wpb_content_element">
		<div class="wpb_wrapper">
			<div style="background: #ffffff; padding: 32px 26px; border-radius: 8px; box-shadow: 0 8px 24px rgba(0,0,0,0.06); text-align: center; height: 100%;">
<h3 style="font-size: 28px; color: #1f1f1f; margin: 0 0 12px;">Flexible Custom Menus</h3>
<p style="font-size: 17px; color: #555; line-height: 1.8; margin: 0 0 18px;">Choose a ready-made set or add à la carte dishes to suit your event.</p>
<p style="font-size: 15px; color: #888; line-height: 1.7; margin: 0;">Easy to match headcount, budget and taste</p>
</div>

		</div>
	</div>
</div></div></div><div class="wpb_column vc_column_container vc_col-sm-3"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_single_image wpb_content_element vc_align_center wpb_content_element">
		
		<figure class="wpb_wrapper vc_figure">
			<div class="vc_single_image-wrapper   vc_box_border_grey"><img loading="lazy" decoding="async" width="150" height="150" src="https://aoaodelivery.com/wp-content/uploads/2025/04/technical-support_3222533-150x150.png" class="vc_single_image-img attachment-thumbnail" alt="" title="technical-support_3222533" srcset="https://aoaodelivery.com/wp-content/uploads/2025/04/technical-support_3222533-150x150.png 150w, https://aoaodelivery.com/wp-content/uploads/2025/04/technical-support_3222533-300x300.png 300w, https://aoaodelivery.com/wp-content/uploads/2025/04/technical-support_3222533-12x12.png 12w, https://aoaodelivery.com/wp-content/uploads/2025/04/technical-support_3222533-100x100.png 100w, https://aoaodelivery.com/wp-content/uploads/2025/04/technical-support_3222533-60x60.png 60w, https://aoaodelivery.com/wp-content/uploads/2025/04/technical-support_3222533.png 512w" sizes="auto, (max-width: 150px) 100vw, 150px"></div>
		</figure>
	</div>

	<div class="wpb_text_column wpb_content_element">
		<div class="wpb_wrapper">
			<div style="background: #ffffff; padding: 32px 26px; border-radius: 8px; box-shadow: 0 8px 24px rgba(0,0,0,0.06); text-align: center; height: 100%;">
<h3 style="font-size: 28px; color: #1f1f1f; margin: 0 0 12px;">Reliable, On-Time Delivery</h3>
<p style="font-size: 17px; color: #555; line-height: 1.8; margin: 0 0 18px;">Our team plans every delivery carefully to arrive within your booked time slot.</p>
<p style="font-size: 15px; color: #888; line-height: 1.7; margin: 0;">Peace of mind on the big day</p>
</div>

		</div>
	</div>
</div></div></div><div class="wpb_column vc_column_container vc_col-sm-3"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_single_image wpb_content_element vc_align_center wpb_content_element">
		
		<figure class="wpb_wrapper vc_figure">
			<div class="vc_single_image-wrapper   vc_box_border_grey"><img loading="lazy" decoding="async" width="150" height="150" src="https://aoaodelivery.com/wp-content/uploads/2025/04/lunch-box_3101638-150x150.png" class="vc_single_image-img attachment-thumbnail" alt="" title="Kitchen AO catering delivery keeping food warm" srcset="https://aoaodelivery.com/wp-content/uploads/2025/04/lunch-box_3101638-150x150.png 150w, https://aoaodelivery.com/wp-content/uploads/2025/04/lunch-box_3101638-300x300.png 300w, https://aoaodelivery.com/wp-content/uploads/2025/04/lunch-box_3101638-12x12.png 12w, https://aoaodelivery.com/wp-content/uploads/2025/04/lunch-box_3101638-100x100.png 100w, https://aoaodelivery.com/wp-content/uploads/2025/04/lunch-box_3101638-60x60.png 60w, https://aoaodelivery.com/wp-content/uploads/2025/04/lunch-box_3101638.png 512w" sizes="auto, (max-width: 150px) 100vw, 150px"></div>
		</figure>
	</div>

	<div class="wpb_text_column wpb_content_element">
		<div class="wpb_wrapper">
			<div style="background: #ffffff; padding: 32px 26px; border-radius: 8px; box-shadow: 0 8px 24px rgba(0,0,0,0.06); text-align: center; height: 100%;">
<h3 style="font-size: 28px; color: #1f1f1f; margin: 0 0 12px;">One-Stop Party Add-ons</h3>
<p style="font-size: 17px; color: #555; line-height: 1.8; margin: 0 0 18px;">Beyond food, add party supplies and extras to complete your event in one order.</p>
<p style="font-size: 15px; color: #888; line-height: 1.7; margin: 0;">For hosts who want everything sorted at once</p>
</div>

		</div>
	</div>
</div></div></div></div>



<div class="vc_row wpb_row vc_inner vc_row-fluid">
	<div class="wpb_column vc_column_container vc_col-sm-12"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_raw_code wpb_raw_html wpb_content_element">
		<div class="wpb_wrapper">
			<div style="max-width:980px; margin:0 auto; text-align:center;">
  <h2 style="font-size:38px; color:#1f1f1f; margin:0 0 12px;">What Is Catering Service?</h2>
  <p style="font-size:18px; color:#666; line-height:1.9; margin:0 0 26px;">
    Catering means freshly prepared food delivered on time to your venue, perfect for parties, corporate events, meetings and family gatherings.
  </p>
</div>

<div style="display:flex; flex-wrap:wrap; gap:24px; justify-content:center;">
  <div style="flex:1 1 260px; max-width:300px; background:#fff; padding:28px 24px; border-radius:8px; box-shadow:0 8px 24px rgba(0,0,0,0.06); text-align:center;">
    <h3 style="font-size:24px; color:#1f1f1f; margin:0 0 10px;">Wide Menu Choice</h3>
    <p style="font-size:16px; color:#555; line-height:1.8; margin:0;">From snacks and mains to desserts, mix and match freely.</p>
  </div>

  <div style="flex:1 1 260px; max-width:300px; background:#fff; padding:28px 24px; border-radius:8px; box-shadow:0 8px 24px rgba(0,0,0,0.06); text-align:center;">
    <h3 style="font-size:24px; color:#1f1f1f; margin:0 0 10px;">On-Time Delivery</h3>
    <p style="font-size:16px; color:#555; line-height:1.8; margin:0;">Delivered to your venue at the time you booked.</p>
  </div>

  <div style="flex:1 1 260px; max-width:300px; background:#fff; padding:28px 24px; border-radius:8px; box-shadow:0 8px 24px rgba(0,0,0,0.06); text-align:center;">
    <h3 style="font-size:24px; color:#1f1f1f; margin:0 0 10px;">For Every Occasion</h3>
    <p style="font-size:16px; color:#555; line-height:1.8; margin:0;">Parties, business lunches, meeting breaks and festive gatherings.</p>
  </div>
</div>

		</div>
	</div>
</div></div></div></div>



</div></div></div></div>
<div class="vc_row wpb_row vc_row-fluid vc_custom_1775902198440 vc_row-has-fill vc_column-gap-20 vc_row-o-equal-height vc_row-flex">
    <div class="wpb_column vc_column_container vc_col-sm-12"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_text_column wpb_content_element">
		<div class="wpb_wrapper">
			<div style="text-align: center; padding: 10px 0 10px;">
<h2 style="font-size: 38px; color: #1f1f1f; margin: 0 0 12px;">What Our Customers Say</h2>
<p style="font-size: 18px; color: #666; margin: 0;">Real feedback from party, corporate and business catering customers.</p>
</div>
<div style="text-align: center; padding: 10px 0 24px;">
<div style="display: inline-block; background: #ffffff; padding: 16px 26px; border-radius: 999px; box-shadow: 0 8px 24px rgba(0,0,0,0.06);"><span style="font-size: 22px; color: #d4a017; letter-spacing: 2px;">★★★★★</span><br>
<span style="font-size: 17px; color: #333; margin-left: 10px; font-weight: bold;">4.8 / 5</span><br>
<span style="font-size: 16px; color: #777; margin-left: 8px;">Google Reviews</span></div>
</div>
<div style="text-align: center; padding: 0 0 34px;"><a style="display: inline-block; background: #c9b18a; color: #ffffff; padding: 13px 26px; text-decoration: none; border-radius: 4px;" href="https://maps.app.goo.gl/YvZdM4HqFCP7Pw9p6?g_st=ic" target="_blank" rel="noopener"><br>
Read Google Reviews<br>
</a></div>

		</div>
	</div>
<div class="vc_row wpb_row vc_inner vc_row-fluid">
	<div class="wpb_column vc_column_container vc_col-sm-4"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_text_column wpb_content_element">
		<div class="wpb_wrapper">
			<div style="background: #ffffff; padding: 32px 28px; border-radius: 8px; box-shadow: 0 8px 24px rgba(0,0,0,0.06); height: 100%;">
<div style="font-size: 22px; color: #c9b18a; margin-bottom: 14px;">★★★★★</div>
<p style="font-size: 17px; color: #444; line-height: 1.9; margin: 0 0 20px;">Excellent service and food! Thank you KitchenAO。</p>
<p style="font-size: 18px; color: #1f1f1f; font-weight: bold; margin: 0 0 6px;">Sinyi Chu</p>
<p style="font-size: 15px; color: #888; margin: 0;">Birthday party customer</p>
</div>

		</div>
	</div>
</div></div></div><div class="wpb_column vc_column_container vc_col-sm-4"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_text_column wpb_content_element">
		<div class="wpb_wrapper">
			<div style="background: #ffffff; padding: 32px 28px; border-radius: 8px; box-shadow: 0 8px 24px rgba(0,0,0,0.06); height: 100%;">
<div style="font-size: 22px; color: #c9b18a; margin-bottom: 14px;">★★★★★</div>
<p style="font-size: 17px; color: #444; line-height: 1.9; margin: 0 0 20px;">Delivered on time for our company event, neatly packed and easy for colleagues to help themselves. Professional and hassle-free. We will order again.</p>
<p style="font-size: 18px; color: #1f1f1f; font-weight: bold; margin: 0 0 6px;">Mr Wong</p>
<p style="font-size: 15px; color: #888; margin: 0;">Corporate event customer</p>
</div>

		</div>
	</div>
</div></div></div><div class="wpb_column vc_column_container vc_col-sm-4"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_text_column wpb_content_element">
		<div class="wpb_wrapper">
			<div style="background: #ffffff; padding: 32px 28px; border-radius: 8px; box-shadow: 0 8px 24px rgba(0,0,0,0.06); height: 100%;">
<div style="font-size: 22px; color: #c9b18a; margin-bottom: 14px;">★★★★★</div>
<p style="font-size: 17px; color: #444; line-height: 1.9; margin: 0 0 20px;">The menu was flexible. We added a few à la carte snacks for our headcount and it was plenty. Our friends found it convenient and delicious.</p>
<p style="font-size: 18px; color: #1f1f1f; font-weight: bold; margin: 0 0 6px;">Ms Lam</p>
<p style="font-size: 15px; color: #888; margin: 0;">Party catering customer</p>
</div>

		</div>
	</div>
</div></div></div></div>



</div></div></div></div>
<div class="vc_row wpb_row vc_row-fluid">
    <div class="wpb_column vc_column_container vc_col-sm-12"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_single_image wpb_content_element vc_align_center wpb_content_element">
		
		<figure class="wpb_wrapper vc_figure">
			<div class="vc_single_image-wrapper   vc_box_border_grey"><img loading="lazy" decoding="async" width="300" height="129" src="https://aoaodelivery.com/wp-content/uploads/2024/09/1badge-1-300x129.png" class="vc_single_image-img attachment-medium" alt="" title="1badge" srcset="https://aoaodelivery.com/wp-content/uploads/2024/09/1badge-1-300x129.png 300w, https://aoaodelivery.com/wp-content/uploads/2024/09/1badge-1-1024x442.png 1024w, https://aoaodelivery.com/wp-content/uploads/2024/09/1badge-1-768x331.png 768w, https://aoaodelivery.com/wp-content/uploads/2024/09/1badge-1-1536x663.png 1536w, https://aoaodelivery.com/wp-content/uploads/2024/09/1badge-1-2048x883.png 2048w, https://aoaodelivery.com/wp-content/uploads/2024/09/1badge-1-18x8.png 18w, https://aoaodelivery.com/wp-content/uploads/2024/09/1badge-1-1440x621.png 1440w, https://aoaodelivery.com/wp-content/uploads/2024/09/1badge-1-100x43.png 100w, https://aoaodelivery.com/wp-content/uploads/2024/09/1badge-1-600x259.png 600w" sizes="auto, (max-width: 300px) 100vw, 300px"></div>
		</figure>
	</div>
</div></div></div></div>
<div class="vc_row wpb_row vc_row-fluid">
    <div class="wpb_column vc_column_container vc_col-sm-12"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_text_column wpb_content_element">
		<div class="wpb_wrapper">
			<div style="text-align: center; padding: 10px 0 24px;">
<h2 style="font-size: 38px; color: #1f1f1f; margin: 0 0 12px;">Frequently Asked Questions</h2>
<p style="font-size: 18px; color: #666; margin: 0;">Answers to the most common questions about ordering, delivery and menus.</p>
</div>

		</div>
	</div>

	<div class="wpb_raw_code wpb_raw_html wpb_content_element">
		<div class="wpb_wrapper">
			<div style="max-width:900px; margin:0 auto;">

  <details style="background:#ffffff; border-radius:8px; box-shadow:0 8px 24px rgba(0,0,0,0.06); margin-bottom:16px; padding:0 22px;">
    <summary style="font-size:20px; font-weight:700; color:#1f1f1f; cursor:pointer; padding:22px 0; outline:none;">
      How far in advance should I book?
    </summary>
    <div style="padding:0 0 22px; font-size:17px; color:#555; line-height:1.9;">
      Please book as early as possible, especially for weekends, festivals and large events, which fill up quickly. Order cut-off times depend on the menu, order size and delivery arrangements. WhatsApp us for details.
    </div>
  </details>

  <details style="background:#ffffff; border-radius:8px; box-shadow:0 8px 24px rgba(0,0,0,0.06); margin-bottom:16px; padding:0 22px;">
    <summary style="font-size:20px; font-weight:700; color:#1f1f1f; cursor:pointer; padding:22px 0; outline:none;">
      Is there a minimum order?
    </summary>
    <div style="padding:0 0 22px; font-size:17px; color:#555; line-height:1.9;">
      Requirements vary by set, à la carte category and delivery arrangement. Tell us your event date, headcount and delivery address and we will recommend the best option.
    </div>
  </details>

  <details style="background:#ffffff; border-radius:8px; box-shadow:0 8px 24px rgba(0,0,0,0.06); margin-bottom:16px; padding:0 22px;">
    <summary style="font-size:20px; font-weight:700; color:#1f1f1f; cursor:pointer; padding:22px 0; outline:none;">
      Which areas do you deliver to? Is there a delivery fee?
    </summary>
    <div style="padding:0 0 22px; font-size:17px; color:#555; line-height:1.9;">
      We deliver to most areas across Hong Kong Island, Kowloon and the New Territories. Fees depend on location, time slot and order details; remote areas or specific time slots may cost extra. Orders over HK$700 enjoy reduced delivery fees in selected areas, and orders over HK$1,450 enjoy free delivery across Hong Kong (excluding non-delivery areas). See <a href="https://aoaodelivery.com/en/delivery/">Delivery Information</a>.
    </div>
  </details>

  <details style="background:#ffffff; border-radius:8px; box-shadow:0 8px 24px rgba(0,0,0,0.06); margin-bottom:16px; padding:0 22px;">
    <summary style="font-size:20px; font-weight:700; color:#1f1f1f; cursor:pointer; padding:22px 0; outline:none;">
      Can you customise the menu for my event?
    </summary>
    <div style="padding:0 0 22px; font-size:17px; color:#555; line-height:1.9;">
      Yes. For birthday parties, corporate events, business lunches or boat parties, we can adjust the menu to your headcount, budget and dining style, and add à la carte dishes.
    </div>
  </details>

  <details style="background:#ffffff; border-radius:8px; box-shadow:0 8px 24px rgba(0,0,0,0.06); margin-bottom:16px; padding:0 22px;">
    <summary style="font-size:20px; font-weight:700; color:#1f1f1f; cursor:pointer; padding:22px 0; outline:none;">
      Do you provide cutlery, paper plates or party supplies?
    </summary>
    <div style="padding:0 0 22px; font-size:17px; color:#555; line-height:1.9;">
      Yes, you can add cutlery, drinks and selected party supplies to arrange everything in one place. Availability depends on the current menu and add-on options.
    </div>
  </details>

</div>

		</div>
	</div>

	<div class="wpb_text_column wpb_content_element">
		<div class="wpb_wrapper">
			<div style="text-align: center; padding-top: 18px;"><a style="display: inline-block; background: #8cc63f; color: #ffffff; padding: 15px 28px; text-decoration: none; border-radius: 6px; font-size: 18px; font-weight: bold; margin-right: 10px;" href="https://wa.me/85269011987" target="_blank" rel="noopener noreferrer"><br>
WhatsApp Us<br>
</a><br>
<a style="display: inline-block; background: #c9b18a; color: #ffffff; padding: 15px 28px; text-decoration: none; border-radius: 6px; font-size: 18px; font-weight: bold;" href="https://aoaodelivery.com/en/contacts/" target="_blank" rel="noopener noreferrer"><br>
Contact Us<br>
</a></div>

		</div>
	</div>
</div></div></div></div>
AOENB;
        $wrap = '<div class="ao-home" lang="en" data-no-translation>';
    } else {
        $a = <<<'AOZHA'
<div data-vc-full-width="true" data-vc-full-width-init="false" data-vc-stretch-content="true" class="vc_row wpb_row vc_row-fluid vc_custom_1776576454166 vc_row-has-fill vc_row-o-content-middle vc_row-flex lafka-align-center">
    <div class="wpb_column vc_column_container vc_col-sm-12"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_raw_code wpb_raw_html wpb_content_element">
		<div class="wpb_wrapper">
			<section class="ao-hero" style="padding:36px 20px;background:linear-gradient(180deg,#fbf8f3 0%,#f5efe7 100%);">
  <div class="ao-hero-grid" style="max-width:1240px;margin:0 auto;display:grid;grid-template-columns:1.05fr 0.95fr;gap:28px;align-items:center;">
    <div style="order:1;">
      <div style="display:inline-block;margin:0 0 12px;padding:6px 12px;border-radius:999px;background:#efe4d1;color:#7d5b27;font-size:12px;font-weight:800;letter-spacing:0.08em;line-height:1.2;">
        KITCHEN AO HONG KONG CATERING
      </div>
      <h1 style="margin:0 0 14px;color:#201814;font-size:42px;line-height:1.15;font-weight:800;">
        <span class="ao-nw">派對到會・</span><span class="ao-nw">公司活動餐飲</span><br>一站式安排
      </h1>
      <p style="margin:0 0 18px;max-width:620px;color:#5d534d;font-size:17px;line-height:1.9;">
        Kitchen AO 專注香港到會服務，適合生日派對、企業活動、家庭聚餐、船河聚會及品牌場合。由精緻擺盤、主打熱食到特色餐單，幫你把聚會做得更體面、更方便。
      </p>
      <div class="ao-hero-ctas">
        <a class="ao-hero-btn" href="https://aoaodelivery.com/product-category/party/" onclick="window.dataLayer=window.dataLayer||[];dataLayer.push({event:'cta_click',cta_label:'view_menu'});" style="display:inline-block;padding:14px 22px;border-radius:999px;background:#1f1714;color:#ffffff;text-decoration:none;font-size:15px;font-weight:800;line-height:1.2;">
          查看餐單
        </a>
        <a class="ao-hero-btn" href="https://wa.me/85269011987?text=你好，我想查詢 Kitchen AO 到會餐單及報價" target="_blank" rel="noopener noreferrer" onclick="window.dataLayer=window.dataLayer||[];dataLayer.push({event:'cta_click',cta_label:'whatsapp'});" style="display:inline-block;padding:14px 22px;border-radius:999px;background:#d9b06a;color:#241a12;text-decoration:none;font-size:15px;font-weight:800;line-height:1.2;">
          WhatsApp 查詢
        </a>
        <a class="ao-hero-btn" href="https://aoaodelivery.com/catering-quote-enquiry/" onclick="window.dataLayer=window.dataLayer||[];dataLayer.push({event:'cta_click',cta_label:'quote_form'});" style="display:inline-block;padding:12px 20px;border-radius:999px;background:#ffffff;color:#1f1714;text-decoration:none;font-size:15px;font-weight:800;line-height:1.2;border:2px solid #1f1714;">
          專人活動報價查詢
        </a>
        <a class="ao-hero-btn ao-hero-hw" href="https://aoaodelivery.com/product-category/halloween-set/?ao_ref=hw26_home_hero" onclick="window.dataLayer=window.dataLayer||[];dataLayer.push({event:'cta_click',cta_label:'halloween_menu'});">
          <span class="ao-hero-bats" aria-hidden="true"><i class="b1"><svg viewBox="0 0 100 44"><path d="M50 18 L53 9 L55.5 17 C62 12 78 6 97 10 C89 14 85 20 87 27 C81 22 75 22 71 29 C67 24 61 24 57.5 31 C55 29 52.5 33 50 38 C47.5 33 45 29 42.5 31 C39 24 33 24 29 29 C25 22 19 22 13 27 C15 20 11 14 3 10 C22 6 38 12 44.5 17 L47 9 Z" fill="#2a0d3d"></path><circle cx="47.6" cy="20" r="1.6" fill="#FFE14D"></circle><circle cx="52.4" cy="20" r="1.6" fill="#FFE14D"></circle></svg></i><i class="b2"><svg viewBox="0 0 100 44"><path d="M50 18 L53 9 L55.5 17 C62 12 78 6 97 10 C89 14 85 20 87 27 C81 22 75 22 71 29 C67 24 61 24 57.5 31 C55 29 52.5 33 50 38 C47.5 33 45 29 42.5 31 C39 24 33 24 29 29 C25 22 19 22 13 27 C15 20 11 14 3 10 C22 6 38 12 44.5 17 L47 9 Z" fill="#2a0d3d"></path><circle cx="47.6" cy="20" r="1.6" fill="#FFE14D"></circle><circle cx="52.4" cy="20" r="1.6" fill="#FFE14D"></circle></svg></i><i class="b3"><svg viewBox="0 0 100 44"><path d="M50 18 L53 9 L55.5 17 C62 12 78 6 97 10 C89 14 85 20 87 27 C81 22 75 22 71 29 C67 24 61 24 57.5 31 C55 29 52.5 33 50 38 C47.5 33 45 29 42.5 31 C39 24 33 24 29 29 C25 22 19 22 13 27 C15 20 11 14 3 10 C22 6 38 12 44.5 17 L47 9 Z" fill="#2a0d3d"></path><circle cx="47.6" cy="20" r="1.6" fill="#FFE14D"></circle><circle cx="52.4" cy="20" r="1.6" fill="#FFE14D"></circle></svg></i></span>
          <span class="ao-hero-hw-txt">🎃 Halloween 萬聖節狂嘩套餐 <small>10月23日–11月1日送貨</small></span>
        </a>
      </div>
      <div class="ao-hero-feats" style="display:flex;flex-wrap:wrap;gap:8px 18px;color:#6a5f58;font-size:14px;line-height:1.7;">
        <div style="white-space:nowrap;">適合生日派對</div>
        <div style="white-space:nowrap;">公司活動餐飲</div>
        <div style="white-space:nowrap;">精緻擺盤到會</div>
      </div>
    </div>
    <div style="order:2;">
      <div style="position:relative;background:#ffffff;border-radius:26px;padding:14px;box-shadow:0 20px 40px rgba(40,24,15,0.10);">
        <img class="ao-hero-img" src="https://aoaodelivery.com/wp-content/uploads/2026/07/catering-hongkong-corporate.jpg" alt="Kitchen AO 到會服務與精緻食物擺設" width="1200" height="1400" fetchpriority="high" decoding="async" style="display:block;width:100%;height:680px;object-fit:cover;object-position:center top;border-radius:18px;">
      </div>
    </div>
  </div>
</section>
<style>
.ao-hero-feats > div::before{content:"\2714\00A0";}
.ao-hero .ao-nw{white-space:nowrap;}

/* ===== CTA：3 個一行等闊，Halloween 掣喺下面同一闊度 ===== */
.ao-hero-ctas{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;max-width:620px;margin:0 0 18px;}
.ao-hero-ctas .ao-hero-btn{display:flex !important;align-items:center;justify-content:center;min-height:50px;box-sizing:border-box;text-align:center;white-space:nowrap;}

/* ===== Halloween CTA（同 Pop up 一樣：漸變 + 反光 + 搖動 + 蝙蝠）===== */
.ao-hero-ctas .ao-hero-hw{grid-column:1 / -1;position:relative;overflow:hidden;padding:12px 20px;border-radius:999px;background:linear-gradient(135deg,#FF8A1F 0%,#FF5A00 100%);color:#1c1426 !important;text-decoration:none !important;font-size:16px;font-weight:800;line-height:1.25;box-shadow:0 6px 18px rgba(255,90,0,.40);animation:aoHeroWiggle 3.2s ease-in-out infinite;}
.ao-hero-ctas .ao-hero-hw::after{content:"";position:absolute;top:0;left:-60%;width:40%;height:100%;background:linear-gradient(100deg,rgba(255,255,255,0),rgba(255,255,255,.65),rgba(255,255,255,0));transform:skewX(-20deg);animation:aoHeroShine 2.8s ease-in-out infinite;z-index:3;pointer-events:none;}
.ao-hero-hw-txt{position:relative;z-index:2;}
.ao-hero img.emoji,.ao-hero img.wp-smiley{display:inline !important;width:1em !important;height:1em !important;margin:0 .15em 0 0 !important;vertical-align:-0.12em !important;border:0 !important;box-shadow:none !important;}
.ao-hero-hw-txt small{display:inline-block;margin-left:8px;padding:2px 9px;border-radius:999px;background:rgba(28,20,38,.85);color:#FFB347;font-size:12px;font-weight:700;vertical-align:2px;}
.ao-hero-bats{position:absolute;inset:0;z-index:1;pointer-events:none;}
.ao-hero-bats i{position:absolute;top:50%;left:-12%;width:36px;margin-top:-7px;animation:aoHeroBat 5s linear infinite;}
.ao-hero-bats i.b2{width:26px;margin-top:-15px;animation-duration:6s;animation-delay:1.6s;}
.ao-hero-bats i.b3{width:30px;margin-top:1px;animation-duration:5.5s;animation-delay:3.2s;}
.ao-hero-bats svg{display:block;width:100%;height:auto;transform-origin:50% 40%;animation:aoHeroFlap .16s ease-in-out infinite alternate;}
@keyframes aoHeroShine{0%{left:-60%;}55%,100%{left:130%;}}
@keyframes aoHeroWiggle{0%,78%,100%{transform:rotate(0) scale(1);}82%{transform:rotate(-1.5deg) scale(1.03);}86%{transform:rotate(1.5deg) scale(1.03);}90%{transform:rotate(-1deg) scale(1.015);}94%{transform:rotate(.6deg) scale(1.005);}}
@keyframes aoHeroBat{0%{left:-12%;transform:translateY(4px);}25%{transform:translateY(-6px);}50%{transform:translateY(5px);}75%{transform:translateY(-5px);}100%{left:108%;transform:translateY(3px);}}
@keyframes aoHeroFlap{from{transform:scaleY(1);}to{transform:scaleY(.55) scaleX(.92);}}
@media (prefers-reduced-motion:reduce){.ao-hero-bats{display:none;}.ao-hero-ctas .ao-hero-hw,.ao-hero-ctas .ao-hero-hw::after{animation:none;}}

@media (max-width:960px){
  .ao-hero-grid{grid-template-columns:1fr !important;gap:22px !important;}
  .ao-hero h1{font-size:34px !important;}
  .ao-hero .ao-hero-img{height:520px !important;}
}
@media (max-width:640px){
  .ao-hero{padding:28px 16px !important;}
  .ao-hero h1{font-size:28px !important;line-height:1.2 !important;}
  .ao-hero p{font-size:15px !important;line-height:1.8 !important;}
  .ao-hero .ao-hero-img{height:420px !important;object-position:center top !important;}
  .ao-hero-ctas{grid-template-columns:1fr;gap:10px;max-width:none;}
  .ao-hero-ctas .ao-hero-btn{width:100%;}
  .ao-hero-ctas .ao-hero-hw{flex-direction:column;}
  .ao-hero-hw-txt small{display:block;width:max-content;margin:5px auto 0;vertical-align:0;}
  .ao-hero-feats{flex-direction:column;gap:6px;}
}
</style>

		</div>
	</div>
</div></div></div></div>
<section class="ao-promo"><div class="ao-mq" aria-label="會員優惠"><div class="ao-mq-track"><span>舊會員優惠：系統會根據你上一張訂單的金額，自動為今次訂單減價。上一張訂單滿 $2,000，今次減 $100；滿 $4,000 減 $200，如此類推。優惠可與「買送」優惠同時使用，但不可合併訂單計算，亦不適用於客服人手輸入的訂單。</span><span aria-hidden="true">舊會員優惠：系統會根據你上一張訂單的金額，自動為今次訂單減價。上一張訂單滿 $2,000，今次減 $100；滿 $4,000 減 $200，如此類推。優惠可與「買送」優惠同時使用，但不可合併訂單計算，亦不適用於客服人手輸入的訂單。</span></div></div><div class="ao-sl"><div class="ao-sl-track"><a class="ao-sl-item" href="https://aoaodelivery.com/product-category/halloween-set/"><img src="https://aoaodelivery.com/wp-content/uploads/2026/10/2025-Halloween-banner-1_banner_banner-scaled.jpg" srcset="https://aoaodelivery.com/wp-content/uploads/2026/10/2025-Halloween-banner-1_banner_banner-scaled.jpg 2560w, https://aoaodelivery.com/wp-content/uploads/2026/10/2025-Halloween-banner-1_banner_banner-300x140.jpg 300w, https://aoaodelivery.com/wp-content/uploads/2026/10/2025-Halloween-banner-1_banner_banner-1024x478.jpg 1024w, https://aoaodelivery.com/wp-content/uploads/2026/10/2025-Halloween-banner-1_banner_banner-768x358.jpg 768w, https://aoaodelivery.com/wp-content/uploads/2026/10/2025-Halloween-banner-1_banner_banner-1536x717.jpg 1536w, https://aoaodelivery.com/wp-content/uploads/2026/10/2025-Halloween-banner-1_banner_banner-2048x956.jpg 2048w, https://aoaodelivery.com/wp-content/uploads/2026/10/2025-Halloween-banner-1_banner_banner-18x8.jpg 18w, https://aoaodelivery.com/wp-content/uploads/2026/10/2025-Halloween-banner-1_banner_banner-1440x672.jpg 1440w, https://aoaodelivery.com/wp-content/uploads/2026/10/2025-Halloween-banner-1_banner_banner-100x47.jpg 100w, https://aoaodelivery.com/wp-content/uploads/2026/10/2025-Halloween-banner-1_banner_banner-600x280.jpg 600w" sizes="(max-width:1200px) 100vw, 1200px" width="2560" height="1195" alt="Halloween 萬聖節狂嘩套餐" loading="eager" fetchpriority="high" decoding="async"></a><a class="ao-sl-item" href="https://aoaodelivery.com/product-category/party/foot-party/"><img src="https://aoaodelivery.com/wp-content/uploads/2026/03/WhatsApp-Image-2026-03-18-at-15.55.47-scaled.jpeg" srcset="https://aoaodelivery.com/wp-content/uploads/2026/03/WhatsApp-Image-2026-03-18-at-15.55.47-scaled.jpeg 2560w, https://aoaodelivery.com/wp-content/uploads/2026/03/WhatsApp-Image-2026-03-18-at-15.55.47-300x140.jpeg 300w, https://aoaodelivery.com/wp-content/uploads/2026/03/WhatsApp-Image-2026-03-18-at-15.55.47-1024x478.jpeg 1024w, https://aoaodelivery.com/wp-content/uploads/2026/03/WhatsApp-Image-2026-03-18-at-15.55.47-768x358.jpeg 768w, https://aoaodelivery.com/wp-content/uploads/2026/03/WhatsApp-Image-2026-03-18-at-15.55.47-1536x717.jpeg 1536w, https://aoaodelivery.com/wp-content/uploads/2026/03/WhatsApp-Image-2026-03-18-at-15.55.47-2048x956.jpeg 2048w, https://aoaodelivery.com/wp-content/uploads/2026/03/WhatsApp-Image-2026-03-18-at-15.55.47-1440x672.jpeg 1440w, https://aoaodelivery.com/wp-content/uploads/2026/03/WhatsApp-Image-2026-03-18-at-15.55.47-100x47.jpeg 100w, https://aoaodelivery.com/wp-content/uploads/2026/03/WhatsApp-Image-2026-03-18-at-15.55.47-600x280.jpeg 600w" sizes="(max-width:1200px) 100vw, 1200px" width="2560" height="1195" alt="派對到會套餐" loading="lazy" decoding="async"></a><a class="ao-sl-item" href="https://aoaodelivery.com/product-category/party/foot-party/"><img src="https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠_工作區域-1-scaled.jpg" srcset="https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠_工作區域-1-scaled.jpg 2560w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠_工作區域-1-300x125.jpg 300w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠_工作區域-1-1024x426.jpg 1024w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠_工作區域-1-768x320.jpg 768w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠_工作區域-1-1536x639.jpg 1536w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠_工作區域-1-2048x852.jpg 2048w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠_工作區域-1-18x7.jpg 18w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠_工作區域-1-1440x599.jpg 1440w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠_工作區域-1-100x42.jpg 100w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠_工作區域-1-600x250.jpg 600w" sizes="(max-width:1200px) 100vw, 1200px" width="2560" height="1065" alt="香港到會會員優惠" loading="lazy" decoding="async"></a><a class="ao-sl-item" href="https://aoaodelivery.com/product-category/party/foot-party/"><img src="https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-02-scaled.jpg" srcset="https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-02-scaled.jpg 2560w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-02-300x125.jpg 300w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-02-1024x426.jpg 1024w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-02-768x320.jpg 768w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-02-1536x639.jpg 1536w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-02-2048x852.jpg 2048w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-02-18x7.jpg 18w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-02-1440x599.jpg 1440w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-02-100x42.jpg 100w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-02-600x250.jpg 600w" sizes="(max-width:1200px) 100vw, 1200px" width="2560" height="1065" alt="香港到會會員優惠" loading="lazy" decoding="async"></a><a class="ao-sl-item" href="https://aoaodelivery.com/product-category/party/foot-party/"><img src="https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-03-scaled.jpg" srcset="https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-03-scaled.jpg 2560w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-03-300x125.jpg 300w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-03-1024x426.jpg 1024w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-03-768x320.jpg 768w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-03-1536x639.jpg 1536w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-03-2048x852.jpg 2048w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-03-18x7.jpg 18w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-03-1440x599.jpg 1440w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-03-100x42.jpg 100w, https://aoaodelivery.com/wp-content/uploads/2024/10/會員優惠-03-600x250.jpg 600w" sizes="(max-width:1200px) 100vw, 1200px" width="2560" height="1065" alt="香港到會會員優惠" loading="lazy" decoding="async"></a></div><div class="ao-sl-dots"><button type="button" class="ao-sl-dot" aria-label="第 1 張"></button><button type="button" class="ao-sl-dot" aria-label="第 2 張"></button><button type="button" class="ao-sl-dot" aria-label="第 3 張"></button><button type="button" class="ao-sl-dot" aria-label="第 4 張"></button><button type="button" class="ao-sl-dot" aria-label="第 5 張"></button></div></div></section>
<div class="vc_row wpb_row vc_row-fluid vc_custom_1775899549282 vc_row-has-fill vc_column-gap-20 vc_row-o-equal-height vc_row-flex">
    <div class="wpb_column vc_column_container vc_col-sm-12"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_text_column wpb_content_element">
		<div class="wpb_wrapper">
			
<h2 class="h1title" style="text-align: center;">香港到會推介：派對、公司及船河到會套餐</h2>

		</div>
	</div>

	<div class="wpb_text_column wpb_content_element">
		<div class="wpb_wrapper">
			<div style="text-align: center; padding: 10px 0 20px;">
<h2 style="font-size: 38px; color: #1f1f1f; margin: 0 0 12px;">適合不同活動場合的到會服務</h2>
<p style="font-size: 18px; color: #666; margin: 0;">由派對聚會到公司活動，Kitchen AO 提供靈活而體面的餐飲安排。</p>
</div>

		</div>
	</div>
<div class="vc_row wpb_row vc_inner vc_row-fluid">
	<div class="wpb_column vc_column_container vc_col-sm-4"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_text_column wpb_content_element">
		<div class="wpb_wrapper">
			<div style="background: #ffffff; padding: 32px 26px; border-radius: 8px; box-shadow: 0 8px 24px rgba(0,0,0,0.06); text-align: center; height: 100%;">
<div style="font-size: 38px; line-height: 1; margin-bottom: 16px;">🎉</div>
<h3 style="font-size: 28px; color: #1f1f1f; margin: 0 0 12px;">派對到會</h3>
<p style="font-size: 17px; color: #555; line-height: 1.8; margin: 0 0 18px;">適合生日會、朋友聚會、家庭聚餐，套餐選擇靈活，方便分享。</p>
<p style="font-size: 15px; color: #888; line-height: 1.7; margin: 0;">小型聚會到大型派對都可安排</p>
</div>

		</div>
	</div>
</div></div></div><div class="wpb_column vc_column_container vc_col-sm-4"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_text_column wpb_content_element">
		<div class="wpb_wrapper">
			<div style="background: #ffffff; padding: 32px 26px; border-radius: 8px; box-shadow: 0 8px 24px rgba(0,0,0,0.06); text-align: center; height: 100%;">
<div style="font-size: 38px; line-height: 1; margin-bottom: 16px;">🏢</div>
<h3 style="font-size: 28px; color: #1f1f1f; margin: 0 0 12px;">公司活動餐飲</h3>
<p style="font-size: 17px; color: #555; line-height: 1.8; margin: 0 0 18px;">適合會議茶點、開幕酒會、員工聚餐，出餐穩定，送達準時。</p>
<p style="font-size: 15px; color: #888; line-height: 1.7; margin: 0;">商務場合更體面，安排更省心</p>
</div>

		</div>
	</div>
</div></div></div><div class="wpb_column vc_column_container vc_col-sm-4"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_text_column wpb_content_element">
		<div class="wpb_wrapper">
			<div style="background: #ffffff; padding: 32px 26px; border-radius: 8px; box-shadow: 0 8px 24px rgba(0,0,0,0.06); text-align: center; height: 100%;">
<div style="font-size: 38px; line-height: 1; margin-bottom: 16px;">🚤</div>
<h3 style="font-size: 28px; color: #1f1f1f; margin: 0 0 12px;">船河及商務午餐</h3>
<p style="font-size: 17px; color: #555; line-height: 1.8; margin: 0 0 18px;">適合外出活動、船河聚會及商務午餐，保溫穩定，方便分發。</p>
<p style="font-size: 15px; color: #888; line-height: 1.7; margin: 0;">方便攜帶，兼顧賣相與實用性</p>
</div>

		</div>
	</div>
</div></div></div></div>



<div class="vc_row wpb_row vc_inner vc_row-fluid vc_custom_1775900383223 vc_row-has-fill vc_column-gap-20 vc_row-o-equal-height vc_row-flex">
	<div class="wpb_column vc_column_container vc_col-sm-12"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_text_column wpb_content_element">
		<div class="wpb_wrapper">
			<div style="text-align: center; padding: 10px 0 20px;">
<h2 style="font-size: 38px; color: #1f1f1f; margin: 0 0 12px;">熱門到會套餐推薦</h2>
<p style="font-size: 18px; color: #666; margin: 0;">精選適合派對、公司聚會及輕食場合的人氣餐單，方便你快速開始預訂。</p>
</div>

		</div>
	</div>
</div></div></div></div>



<div class="vc_row wpb_row vc_inner vc_row-fluid">
	<div class="wpb_column vc_column_container vc_col-sm-4"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_text_column wpb_content_element">
		<div class="wpb_wrapper">
			<div style="background: #ffffff; padding: 32px 26px; border-radius: 8px; box-shadow: 0 8px 24px rgba(0,0,0,0.06); text-align: center; height: 100%;">
<div style="font-size: 16px; color: #b38b2d; font-weight: bold; letter-spacing: 1px; margin-bottom: 10px;">PARTY SET</div>
<h3 style="font-size: 28px; color: #1f1f1f; margin: 0 0 12px;">派對到會套餐</h3>
<p style="font-size: 17px; color: #555; line-height: 1.8; margin: 0 0 16px;">適合生日會、朋友聚餐及節日慶祝，菜式豐富，方便多人分享。</p>
<p style="font-size: 16px; color: #888; margin: 0 0 22px;">適合家庭聚會及派對場合</p>
<p><a style="display: inline-block; background: #c9b18a; color: #ffffff; padding: 14px 24px; text-decoration: none; border-radius: 4px;" href="https://aoaodelivery.com/product-category/party/">查看套餐</a></p>
</div>

		</div>
	</div>
</div></div></div><div class="wpb_column vc_column_container vc_col-sm-4"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_text_column wpb_content_element">
		<div class="wpb_wrapper">
			<div style="background: #ffffff; padding: 32px 26px; border-radius: 8px; box-shadow: 0 8px 24px rgba(0,0,0,0.06); text-align: center; height: 100%;">
<div style="font-size: 16px; color: #b38b2d; font-weight: bold; letter-spacing: 1px; margin-bottom: 10px;">REFRESHMENT</div>
<h3 style="font-size: 28px; color: #1f1f1f; margin: 0 0 12px;">輕食宴會套餐</h3>
<p style="font-size: 17px; color: #555; line-height: 1.8; margin: 0 0 16px;">適合會議茶點、開幕活動及下午茶聚會，款式精緻，取用方便。</p>
<p style="font-size: 16px; color: #888; margin: 0 0 22px;">適合公司活動及商務場合</p>
<p><a style="display: inline-block; background: #c9b18a; color: #ffffff; padding: 14px 24px; text-decoration: none; border-radius: 4px;" href="https://aoaodelivery.com/product-category/party/refreshment-set/">查看套餐</a></p>
</div>

		</div>
	</div>
</div></div></div><div class="wpb_column vc_column_container vc_col-sm-4"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_text_column wpb_content_element">
		<div class="wpb_wrapper">
			<div style="background: #ffffff; padding: 32px 26px; border-radius: 8px; box-shadow: 0 8px 24px rgba(0,0,0,0.06); text-align: center; height: 100%;">
<div style="font-size: 16px; color: #b38b2d; font-weight: bold; letter-spacing: 1px; margin-bottom: 10px;">À LA CARTE</div>
<h3 style="font-size: 28px; color: #1f1f1f; margin: 0 0 12px;">單點美食精選</h3>
<p style="font-size: 17px; color: #555; line-height: 1.8; margin: 0 0 16px;">自由配搭小食、主菜、甜品及飲品，適合想靈活安排餐單的客人。</p>
<p style="font-size: 16px; color: #888; margin: 0 0 22px;">方便加配或自組專屬餐單</p>
<p><a style="display: inline-block; background: #c9b18a; color: #ffffff; padding: 14px 24px; text-decoration: none; border-radius: 4px;" href="https://aoaodelivery.com/product-category/a-la-carte/">查看美食</a></p>
</div>

		</div>
	</div>
</div></div></div></div>



<div class="vc_row wpb_row vc_inner vc_row-fluid">
	<div class="wpb_column vc_column_container vc_col-sm-12"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_raw_code wpb_raw_html wpb_content_element">
		<div class="wpb_wrapper">
			<div style="margin:16px 0 22px;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'PingFang TC','Noto Sans TC','Microsoft JhengHei',sans-serif;">

  <a href="https://aoaodelivery.com/product-category/party/foot-party/" style="display:block;text-decoration:none;margin-bottom:10px;">
    <img decoding="async" src="https://aoaodelivery.com/wp-content/uploads/2026/07/左口魚煲仔飯-黑白叉燒-到會-catering-1000px.jpg" alt="Kitchen AO x 101wine group 黑白叉燒新產品 banner" style="display:block;width:100%;height:auto;border-radius:18px;box-shadow:0 10px 24px rgba(0,0,0,0.12);">
  </a>

  <div style="padding:14px 16px;border-radius:16px;background:linear-gradient(135deg,#251915 0%,#4a2c22 55%,#16110f 100%);border:1px solid rgba(214,180,104,0.24);box-shadow:0 10px 24px rgba(23,17,12,0.10);text-align:center;">
    
    <div style="margin:0 0 6px;color:#f8f1e7;font-size:16px;font-weight:800;line-height:1.5;">
      黑白叉燒新產品限定優惠
    </div>

    <div style="margin:0 0 12px;color:rgba(245,237,226,0.88);font-size:14px;line-height:1.7;">
      輸入優惠碼 <strong style="color:#f0d39a;">WIN95</strong>，全單享 95 折。
    </div>

    <a href="https://wa.me/85269011987?text=你好，我想查詢黑白叉燒新產品，同埋 WIN95 95折優惠" target="_blank" rel="noopener noreferrer" style="display:inline-block;padding:13px 22px;border-radius:999px;background:linear-gradient(135deg,#f0d39a 0%,#d2a44e 100%);color:#241a12 !important;text-decoration:none;font-size:15px;font-weight:800;line-height:1.2;box-shadow:0 8px 18px rgba(0,0,0,0.14);">
      用 WIN95 查詢優惠
    </a>

  </div>

</div>
		</div>
	</div>
</div></div></div></div>



</div></div></div></div>

AOZHA;
        $b = <<<'AOZHB'

<div class="vc_row wpb_row vc_row-fluid vc_custom_1775901384920 vc_row-has-fill vc_column-gap-20 vc_row-o-equal-height vc_row-flex">
    <div class="wpb_column vc_column_container vc_col-sm-12"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_text_column wpb_content_element">
		<div class="wpb_wrapper">
			<div style="text-align: center; padding: 10px 0 20px;">
<h2 style="font-size: 38px; color: #1f1f1f; margin: 0 0 12px;">為何選擇 Kitchen AO？</h2>
<p style="font-size: 18px; color: #666; margin: 0;">由食材、出品到配送安排，我們希望每一個重要場合都更安心、更體面。</p>
</div>

		</div>
	</div>
<div class="vc_row wpb_row vc_inner vc_row-fluid vc_custom_1775901425810 vc_row-has-fill vc_column-gap-20">
	<div class="wpb_column vc_column_container vc_col-sm-3"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_single_image wpb_content_element vc_align_center wpb_content_element">
		
		<figure class="wpb_wrapper vc_figure">
			<div class="vc_single_image-wrapper   vc_box_border_grey"><img loading="lazy" decoding="async" width="150" height="150" src="https://aoaodelivery.com/wp-content/uploads/2025/04/person_14933728-150x150.png" class="vc_single_image-img attachment-thumbnail" alt="" title="Kitchen AO 廚師團隊主理到會好食" srcset="https://aoaodelivery.com/wp-content/uploads/2025/04/person_14933728-150x150.png 150w, https://aoaodelivery.com/wp-content/uploads/2025/04/person_14933728-300x300.png 300w, https://aoaodelivery.com/wp-content/uploads/2025/04/person_14933728-12x12.png 12w, https://aoaodelivery.com/wp-content/uploads/2025/04/person_14933728-100x100.png 100w, https://aoaodelivery.com/wp-content/uploads/2025/04/person_14933728-60x60.png 60w, https://aoaodelivery.com/wp-content/uploads/2025/04/person_14933728.png 512w" sizes="auto, (max-width: 150px) 100vw, 150px"></div>
		</figure>
	</div>

	<div class="wpb_text_column wpb_content_element">
		<div class="wpb_wrapper">
			<div style="background: #ffffff; padding: 32px 26px; border-radius: 8px; box-shadow: 0 8px 24px rgba(0,0,0,0.06); text-align: center; height: 100%;">
<h3 style="font-size: 28px; color: #1f1f1f; margin: 0 0 12px;">酒店級廚師團隊</h3>
<p style="font-size: 17px; color: #555; line-height: 1.8; margin: 0 0 18px;">由經驗廚師團隊主理，重視食材、味道與賣相，令每份到會餐點更有水準。</p>
<p style="font-size: 15px; color: #888; line-height: 1.7; margin: 0;">適合重視質素與形象的聚會場合</p>
</div>

		</div>
	</div>
</div></div></div><div class="wpb_column vc_column_container vc_col-sm-3"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_single_image wpb_content_element vc_align_center wpb_content_element">
		
		<figure class="wpb_wrapper vc_figure">
			<div class="vc_single_image-wrapper   vc_box_border_grey"><img loading="lazy" decoding="async" width="150" height="150" src="https://aoaodelivery.com/wp-content/uploads/2025/04/salad_649363-150x150.png" class="vc_single_image-img attachment-thumbnail" alt="" title="Kitchen AO 多元化香港到會美食服務" srcset="https://aoaodelivery.com/wp-content/uploads/2025/04/salad_649363-150x150.png 150w, https://aoaodelivery.com/wp-content/uploads/2025/04/salad_649363-300x300.png 300w, https://aoaodelivery.com/wp-content/uploads/2025/04/salad_649363-12x12.png 12w, https://aoaodelivery.com/wp-content/uploads/2025/04/salad_649363-100x100.png 100w, https://aoaodelivery.com/wp-content/uploads/2025/04/salad_649363-60x60.png 60w, https://aoaodelivery.com/wp-content/uploads/2025/04/salad_649363.png 512w" sizes="auto, (max-width: 150px) 100vw, 150px"></div>
		</figure>
	</div>

	<div class="wpb_text_column wpb_content_element">
		<div class="wpb_wrapper">
			<div style="background: #ffffff; padding: 32px 26px; border-radius: 8px; box-shadow: 0 8px 24px rgba(0,0,0,0.06); text-align: center; height: 100%;">
<h3 style="font-size: 28px; color: #1f1f1f; margin: 0 0 12px;">靈活客製餐單</h3>
<p style="font-size: 17px; color: #555; line-height: 1.8; margin: 0 0 18px;">可選預設套餐，亦可按活動形式加入單點美食，自由組合更貼近實際需要。</p>
<p style="font-size: 15px; color: #888; line-height: 1.7; margin: 0;">更方便配合人數、預算與口味</p>
</div>

		</div>
	</div>
</div></div></div><div class="wpb_column vc_column_container vc_col-sm-3"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_single_image wpb_content_element vc_align_center wpb_content_element">
		
		<figure class="wpb_wrapper vc_figure">
			<div class="vc_single_image-wrapper   vc_box_border_grey"><img loading="lazy" decoding="async" width="150" height="150" src="https://aoaodelivery.com/wp-content/uploads/2025/04/technical-support_3222533-150x150.png" class="vc_single_image-img attachment-thumbnail" alt="" title="technical-support_3222533" srcset="https://aoaodelivery.com/wp-content/uploads/2025/04/technical-support_3222533-150x150.png 150w, https://aoaodelivery.com/wp-content/uploads/2025/04/technical-support_3222533-300x300.png 300w, https://aoaodelivery.com/wp-content/uploads/2025/04/technical-support_3222533-12x12.png 12w, https://aoaodelivery.com/wp-content/uploads/2025/04/technical-support_3222533-100x100.png 100w, https://aoaodelivery.com/wp-content/uploads/2025/04/technical-support_3222533-60x60.png 60w, https://aoaodelivery.com/wp-content/uploads/2025/04/technical-support_3222533.png 512w" sizes="auto, (max-width: 150px) 100vw, 150px"></div>
		</figure>
	</div>

	<div class="wpb_text_column wpb_content_element">
		<div class="wpb_wrapper">
			<div style="background: #ffffff; padding: 32px 26px; border-radius: 8px; box-shadow: 0 8px 24px rgba(0,0,0,0.06); text-align: center; height: 100%;">
<h3 style="font-size: 28px; color: #1f1f1f; margin: 0 0 12px;">專人準時送遞</h3>
<p style="font-size: 17px; color: #555; line-height: 1.8; margin: 0 0 18px;">由團隊安排送餐流程，重視時間管理，務求按預定時段將餐點送達。</p>
<p style="font-size: 15px; color: #888; line-height: 1.7; margin: 0;">重要場合更安心，減少臨場壓力</p>
</div>

		</div>
	</div>
</div></div></div><div class="wpb_column vc_column_container vc_col-sm-3"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_single_image wpb_content_element vc_align_center wpb_content_element">
		
		<figure class="wpb_wrapper vc_figure">
			<div class="vc_single_image-wrapper   vc_box_border_grey"><img loading="lazy" decoding="async" width="150" height="150" src="https://aoaodelivery.com/wp-content/uploads/2025/04/lunch-box_3101638-150x150.png" class="vc_single_image-img attachment-thumbnail" alt="" title="Kitchen AO 到會服務保溫技術" srcset="https://aoaodelivery.com/wp-content/uploads/2025/04/lunch-box_3101638-150x150.png 150w, https://aoaodelivery.com/wp-content/uploads/2025/04/lunch-box_3101638-300x300.png 300w, https://aoaodelivery.com/wp-content/uploads/2025/04/lunch-box_3101638-12x12.png 12w, https://aoaodelivery.com/wp-content/uploads/2025/04/lunch-box_3101638-100x100.png 100w, https://aoaodelivery.com/wp-content/uploads/2025/04/lunch-box_3101638-60x60.png 60w, https://aoaodelivery.com/wp-content/uploads/2025/04/lunch-box_3101638.png 512w" sizes="auto, (max-width: 150px) 100vw, 150px"></div>
		</figure>
	</div>

	<div class="wpb_text_column wpb_content_element">
		<div class="wpb_wrapper">
			<div style="background: #ffffff; padding: 32px 26px; border-radius: 8px; box-shadow: 0 8px 24px rgba(0,0,0,0.06); text-align: center; height: 100%;">
<h3 style="font-size: 28px; color: #1f1f1f; margin: 0 0 12px;">一站式派對配套</h3>
<p style="font-size: 17px; color: #555; line-height: 1.8; margin: 0 0 18px;">除了餐飲選擇，亦可配搭部分派對用品與加配項目，安排更完整方便。</p>
<p style="font-size: 15px; color: #888; line-height: 1.7; margin: 0;">適合想一次過處理活動細節的客人</p>
</div>

		</div>
	</div>
</div></div></div></div>



<div class="vc_row wpb_row vc_inner vc_row-fluid">
	<div class="wpb_column vc_column_container vc_col-sm-12"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_raw_code wpb_raw_html wpb_content_element">
		<div class="wpb_wrapper">
			<div style="max-width:980px; margin:0 auto; text-align:center;">
  <h2 style="font-size:38px; color:#1f1f1f; margin:0 0 12px;">甚麼是到會服務？</h2>
  <p style="font-size:18px; color:#666; line-height:1.9; margin:0 0 26px;">
    到會服務是按活動需要，將預先準備好的美食準時送到指定地點，適合派對、公司活動、會議及家庭聚會。
  </p>
</div>

<div style="display:flex; flex-wrap:wrap; gap:24px; justify-content:center;">
  <div style="flex:1 1 260px; max-width:300px; background:#fff; padding:28px 24px; border-radius:8px; box-shadow:0 8px 24px rgba(0,0,0,0.06); text-align:center;">
    <h3 style="font-size:24px; color:#1f1f1f; margin:0 0 10px;">豐富餐單</h3>
    <p style="font-size:16px; color:#555; line-height:1.8; margin:0;">由小食、主菜到甜品，配搭更靈活。</p>
  </div>

  <div style="flex:1 1 260px; max-width:300px; background:#fff; padding:28px 24px; border-radius:8px; box-shadow:0 8px 24px rgba(0,0,0,0.06); text-align:center;">
    <h3 style="font-size:24px; color:#1f1f1f; margin:0 0 10px;">準時送達</h3>
    <p style="font-size:16px; color:#555; line-height:1.8; margin:0;">按預訂時間送到活動場地，安排更安心。</p>
  </div>

  <div style="flex:1 1 260px; max-width:300px; background:#fff; padding:28px 24px; border-radius:8px; box-shadow:0 8px 24px rgba(0,0,0,0.06); text-align:center;">
    <h3 style="font-size:24px; color:#1f1f1f; margin:0 0 10px;">適合多種場合</h3>
    <p style="font-size:16px; color:#555; line-height:1.8; margin:0;">派對、商務午餐、會議茶點及節日聚會都適合。</p>
  </div>
</div>

		</div>
	</div>
</div></div></div></div>



</div></div></div></div>
<div class="vc_row wpb_row vc_row-fluid vc_custom_1775902198440 vc_row-has-fill vc_column-gap-20 vc_row-o-equal-height vc_row-flex">
    <div class="wpb_column vc_column_container vc_col-sm-12"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_text_column wpb_content_element">
		<div class="wpb_wrapper">
			<div style="text-align: center; padding: 10px 0 10px;">
<h2 style="font-size: 38px; color: #1f1f1f; margin: 0 0 12px;">客戶真實評價</h2>
<p style="font-size: 18px; color: #666; margin: 0;">來自派對聚會、公司活動及商務餐飲客戶的真實回饋，讓你更放心安排重要場合。</p>
</div>
<div style="text-align: center; padding: 10px 0 24px;">
<div style="display: inline-block; background: #ffffff; padding: 16px 26px; border-radius: 999px; box-shadow: 0 8px 24px rgba(0,0,0,0.06);"><span style="font-size: 22px; color: #d4a017; letter-spacing: 2px;">★★★★★</span><br>
<span style="font-size: 17px; color: #333; margin-left: 10px; font-weight: bold;">4.8 / 5</span><br>
<span style="font-size: 16px; color: #777; margin-left: 8px;">Google 商戶評價</span></div>
</div>
<div style="text-align: center; padding: 0 0 34px;"><a style="display: inline-block; background: #c9b18a; color: #ffffff; padding: 13px 26px; text-decoration: none; border-radius: 4px;" href="https://maps.app.goo.gl/YvZdM4HqFCP7Pw9p6?g_st=ic" target="_blank" rel="noopener"><br>
查看 Google 評論<br>
</a></div>

		</div>
	</div>
<div class="vc_row wpb_row vc_inner vc_row-fluid">
	<div class="wpb_column vc_column_container vc_col-sm-4"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_text_column wpb_content_element">
		<div class="wpb_wrapper">
			<div style="background: #ffffff; padding: 32px 28px; border-radius: 8px; box-shadow: 0 8px 24px rgba(0,0,0,0.06); height: 100%;">
<div style="font-size: 22px; color: #c9b18a; margin-bottom: 14px;">★★★★★</div>
<p style="font-size: 17px; color: #444; line-height: 1.9; margin: 0 0 20px;">Excellent service and food! Thank you KitchenAO。</p>
<p style="font-size: 18px; color: #1f1f1f; font-weight: bold; margin: 0 0 6px;">Sinyi Chu</p>
<p style="font-size: 15px; color: #888; margin: 0;">生日派對客戶</p>
</div>

		</div>
	</div>
</div></div></div><div class="wpb_column vc_column_container vc_col-sm-4"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_text_column wpb_content_element">
		<div class="wpb_wrapper">
			<div style="background: #ffffff; padding: 32px 28px; border-radius: 8px; box-shadow: 0 8px 24px rgba(0,0,0,0.06); height: 100%;">
<div style="font-size: 22px; color: #c9b18a; margin-bottom: 14px;">★★★★★</div>
<p style="font-size: 17px; color: #444; line-height: 1.9; margin: 0 0 20px;">公司活動當日準時送達，包裝整齊，方便同事自取，整體感覺專業又省心，之後都會再回購。</p>
<p style="font-size: 18px; color: #1f1f1f; font-weight: bold; margin: 0 0 6px;">黃先生</p>
<p style="font-size: 15px; color: #888; margin: 0;">公司活動餐飲客戶</p>
</div>

		</div>
	</div>
</div></div></div><div class="wpb_column vc_column_container vc_col-sm-4"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_text_column wpb_content_element">
		<div class="wpb_wrapper">
			<div style="background: #ffffff; padding: 32px 28px; border-radius: 8px; box-shadow: 0 8px 24px rgba(0,0,0,0.06); height: 100%;">
<div style="font-size: 22px; color: #c9b18a; margin-bottom: 14px;">★★★★★</div>
<p style="font-size: 17px; color: #444; line-height: 1.9; margin: 0 0 20px;">餐單配搭夠彈性，我哋按人數再加配單點小食就已經好夠，朋友都話方便又好食，整體體驗幾滿意。</p>
<p style="font-size: 18px; color: #1f1f1f; font-weight: bold; margin: 0 0 6px;">林小姐</p>
<p style="font-size: 15px; color: #888; margin: 0;">聚會到會客戶</p>
</div>

		</div>
	</div>
</div></div></div></div>



</div></div></div></div>
<div class="vc_row wpb_row vc_row-fluid">
    <div class="wpb_column vc_column_container vc_col-sm-12"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_single_image wpb_content_element vc_align_center wpb_content_element">
		
		<figure class="wpb_wrapper vc_figure">
			<div class="vc_single_image-wrapper   vc_box_border_grey"><img loading="lazy" decoding="async" width="300" height="129" src="https://aoaodelivery.com/wp-content/uploads/2024/09/1badge-1-300x129.png" class="vc_single_image-img attachment-medium" alt="" title="1badge" srcset="https://aoaodelivery.com/wp-content/uploads/2024/09/1badge-1-300x129.png 300w, https://aoaodelivery.com/wp-content/uploads/2024/09/1badge-1-1024x442.png 1024w, https://aoaodelivery.com/wp-content/uploads/2024/09/1badge-1-768x331.png 768w, https://aoaodelivery.com/wp-content/uploads/2024/09/1badge-1-1536x663.png 1536w, https://aoaodelivery.com/wp-content/uploads/2024/09/1badge-1-2048x883.png 2048w, https://aoaodelivery.com/wp-content/uploads/2024/09/1badge-1-18x8.png 18w, https://aoaodelivery.com/wp-content/uploads/2024/09/1badge-1-1440x621.png 1440w, https://aoaodelivery.com/wp-content/uploads/2024/09/1badge-1-100x43.png 100w, https://aoaodelivery.com/wp-content/uploads/2024/09/1badge-1-600x259.png 600w" sizes="auto, (max-width: 300px) 100vw, 300px"></div>
		</figure>
	</div>
</div></div></div></div>
<div class="vc_row wpb_row vc_row-fluid">
    <div class="wpb_column vc_column_container vc_col-sm-12"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_text_column wpb_content_element">
		<div class="wpb_wrapper">
			<div style="text-align: center; padding: 10px 0 24px;">
<h2 style="font-size: 38px; color: #1f1f1f; margin: 0 0 12px;">常見問題</h2>
<p style="font-size: 18px; color: #666; margin: 0;">以下整理了客人最常查詢的訂購、送貨及餐單安排問題，方便你快速了解。</p>
</div>

		</div>
	</div>

	<div class="wpb_raw_code wpb_raw_html wpb_content_element">
		<div class="wpb_wrapper">
			<div style="max-width:900px; margin:0 auto;">

  <details style="background:#ffffff; border-radius:8px; box-shadow:0 8px 24px rgba(0,0,0,0.06); margin-bottom:16px; padding:0 22px;">
    <summary style="font-size:20px; font-weight:700; color:#1f1f1f; cursor:pointer; padding:22px 0; outline:none;">
      需要幾日前預訂到會服務？
    </summary>
    <div style="padding:0 0 22px; font-size:17px; color:#555; line-height:1.9;">
      建議你盡早預訂，尤其是週末、節日或大型活動日子會較快額滿。實際截單時間按餐單種類、訂單規模及送貨安排而定，建議直接 WhatsApp 查詢。
    </div>
  </details>

  <details style="background:#ffffff; border-radius:8px; box-shadow:0 8px 24px rgba(0,0,0,0.06); margin-bottom:16px; padding:0 22px;">
    <summary style="font-size:20px; font-weight:700; color:#1f1f1f; cursor:pointer; padding:22px 0; outline:none;">
      有沒有最低消費或最低訂購要求？
    </summary>
    <div style="padding:0 0 22px; font-size:17px; color:#555; line-height:1.9;">
      不同套餐、單點類別及送貨安排可能設有不同要求。你可以先提供活動日期、人數及送貨地點，我們會按需要提供最合適的建議。
    </div>
  </details>

  <details style="background:#ffffff; border-radius:8px; box-shadow:0 8px 24px rgba(0,0,0,0.06); margin-bottom:16px; padding:0 22px;">
    <summary style="font-size:20px; font-weight:700; color:#1f1f1f; cursor:pointer; padding:22px 0; outline:none;">
      送貨覆蓋哪些地區？會收送貨費嗎？
    </summary>
    <div style="padding:0 0 22px; font-size:17px; color:#555; line-height:1.9;">
      一般可安排送貨至港九新界多個地區，實際收費會按地點、時段及訂單內容而定。偏遠地區或指定時段或會有額外運費，運費會根據送貨地區及訂單總金額計算。我們設有免運費門檻：單一訂單滿 HK$700 可享部分區域運費減免，滿 HK$1,450 可享全港免運費（不派送地區除外）。詳細收費請參考<a href="https://aoaodelivery.com/delivery/">送貨需知</a>。
    </div>
  </details>

  <details style="background:#ffffff; border-radius:8px; box-shadow:0 8px 24px rgba(0,0,0,0.06); margin-bottom:16px; padding:0 22px;">
    <summary style="font-size:20px; font-weight:700; color:#1f1f1f; cursor:pointer; padding:22px 0; outline:none;">
      可以按活動需要客製餐單嗎？
    </summary>
    <div style="padding:0 0 22px; font-size:17px; color:#555; line-height:1.9;">
      可以。無論是生日派對、公司活動、商務午餐或船河聚會，都可以按人數、預算及用餐形式調整餐單內容，亦可配搭單點美食。
    </div>
  </details>

  <details style="background:#ffffff; border-radius:8px; box-shadow:0 8px 24px rgba(0,0,0,0.06); margin-bottom:16px; padding:0 22px;">
    <summary style="font-size:20px; font-weight:700; color:#1f1f1f; cursor:pointer; padding:22px 0; outline:none;">
      會提供餐具、紙碟或派對用品嗎？
    </summary>
    <div style="padding:0 0 22px; font-size:17px; color:#555; line-height:1.9;">
      可按需要加配餐具、飲品及部分派對用品，方便你一站式安排整個活動。實際供應內容可按當時餐單及加購選項確認。
    </div>
  </details>

</div>

		</div>
	</div>

	<div class="wpb_text_column wpb_content_element">
		<div class="wpb_wrapper">
			<div style="text-align: center; padding-top: 18px;"><a style="display: inline-block; background: #8cc63f; color: #ffffff; padding: 15px 28px; text-decoration: none; border-radius: 6px; font-size: 18px; font-weight: bold; margin-right: 10px;" href="https://wa.me/85269011987" target="_blank" rel="noopener noreferrer"><br>
WhatsApp 查詢<br>
</a><br>
<a style="display: inline-block; background: #c9b18a; color: #ffffff; padding: 15px 28px; text-decoration: none; border-radius: 6px; font-size: 18px; font-weight: bold;" href="https://aoaodelivery.com/contacts/" target="_blank" rel="noopener noreferrer"><br>
聯絡我們<br>
</a></div>

		</div>
	</div>
</div></div></div></div>
AOZHB;
        $wrap = '<div class="ao-home">';
    }
    return '<style>' . $css . '</style>' . $wrap . $a . $form . $b . '</div><script>' . $js . '</script>';
} );
