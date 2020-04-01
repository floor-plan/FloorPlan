(function($){"use strict";var $window=jQuery(window),body=jQuery('body'),sitewidth=$('.site').width(),maxwidth=$('.site-main').width(),windowheight=$window.height(),pageheight=$(document).height(),windowwidth=$window.width(),deviceAgent=navigator.userAgent.toLowerCase(),isMobile=deviceAgent.match(/(iphone|ipod|android|iemobile)/),isMobileAlt=deviceAgent.match(/(iphone|ipod|ipad|android|iemobile)/),isAppleDevice=deviceAgent.match(/(iphone|ipod|ipad)/);(function(){var nav=$('#site-navigation'),button,menu;if(!nav)
return;button=nav.find('.menu-toggle');if(!button)
return;menu=nav.find('.nav-menu');if(!menu||!menu.children().length){button.hide();return;}
$('.menu-toggle').on('click.ispirit',function(){nav.toggleClass('toggled-on');});})();$window.on('hashchange.ispirit',function(){var element=document.getElementById(location.hash.substring(1));if(element){if(!/^(?:a|select|input|button|textarea)$/i.test(element.tagName))
element.tabIndex=-1;element.focus();}});if($('body').hasClass('trans-header')&&$('.slider-container').length==0&&$('.titlebarrow').length==1)
{$('.page-heading').css('padding-top','86px');}else if($('body').hasClass('trans-header')&&$('.slider-container').length==0&&$('.titlebarrow').length==0){$('.page-heading').css('padding-top','86px');if($('.woo-outerwrap').length==1)
{$('.woo-outerwrap').css('padding-top','126px');}else if($('.content-area').length==1)
{$('.content-area').css('padding-top','126px');}}
$.fn.widify=function(){this.each(function(){var _this=$(this);var fwheight=$(this).children('div').outerHeight();var extrawidth=(sitewidth-maxwidth)/2;if(sitewidth>1200)
{_this.wrapInner("<div class='fullwidthinner'></div>");_this.css({"overflow":"visible"});_this.children('.fullwidthinner').css({"width":sitewidth+"px","position":"relative","margin-left":"-"+extrawidth+"px","right":"0px","overflow":"hidden"});}
$(window).resize(function(){maxwidth=$('.site-main').width();sitewidth=$('.site').width();extrawidth=(sitewidth-maxwidth)/2;if(sitewidth>1200){if(!_this.children('div').hasClass('fullwidthinner'))
{_this.wrapInner("<div style='position: relative; overflow: hidden;' class='fullwidthinner'></div>");console.log("added");}
_this.css({"overflow":"visible"});_this.children('.fullwidthinner').css({"width":sitewidth+"px","position":"relative","margin-left":"-"+extrawidth+"px","right":"0px"});}else
{if(_this.children('div').hasClass('fullwidthinner'))
{_this.children('.fullwidthinner').children().unwrap();}
_this.css({"height":"auto","overflow":"hidden"});}});});};$('.fullwidthrow').each(function(){if($('body.boxed').length<1&&$('.has-left-sidebar').length<1&&$('.has-right-sidebar').length<1)
{$(this).widify();}});$.fn.widifytbar=function(){this.each(function(){var _this=$(this);var fwheight=$(this).children('div').outerHeight();var extrawidth=(sitewidth-maxwidth)/2;extrawidth=extrawidth-32;_this.wrapInner("<div class='fullwidthinner'></div>");_this.css({"height":fwheight+"px","overflow":"visible"});_this.children('.fullwidthinner').css({"width":sitewidth+"px","position":"absolute","left":"-"+extrawidth+"px","overflow":"hidden"});$(window).resize(function(){maxwidth=$('.site-main').width();sitewidth=$('.site').width();extrawidth=(sitewidth-maxwidth)/2;extrawidth=extrawidth-32;if(!_this.children('div').hasClass('fullwidthinner'))
{_this.wrapInner("<div class='fullwidthinner'></div>");}
_this.css({"height":fwheight+"px","overflow":"visible"});_this.children('.fullwidthinner').css({"width":sitewidth+"px","left":"-"+extrawidth+"px"});});});};$('.titlebarrow').each(function(){$(this).widifytbar();});$.fn.vparallaxfy=function(){var _this=$(this);var vparallheight=_this.height();var davideo=_this.find('.video-wrap > video');var vdoheight=davideo.height();var vdowidth=davideo.width();var videoprop=vdowidth/vdoheight;var minvheight=(vparallheight*2)+(windowheight*.64);var minvwidth=minvheight*videoprop;var paraypos;davideo.trigger('play');davideo.css("min-width",minvwidth+'px');davideo.css("min-height",minvheight+'px');if(deviceAgent.indexOf("firefox")!=-1)
{davideo.css("min-height",minvheight+'px');}else
{if(windowwidth<minvwidth)
{davideo.attr("width",minvwidth);}else
{davideo.css("min-width",'100%');}}
_this.waypoint(function(direction)
{var scrll=$window.scrollTop();if(direction=="down")
{_this.addClass('parainview');paraypos=$window.scrollTop();}else
{_this.removeClass('parainview');}},{offset:'100%'});_this.waypoint(function(direction){var scrll=$window.scrollTop();if(direction=="down")
{_this.removeClass('parainview');}else
{_this.addClass('parainview');}},{offset:-vparallheight});$(window).scroll(function(){var newvalue=parseInt(($(this).scrollTop()-paraypos)*.64);_this.find('.video-wrap').css('margin-top','-'+newvalue+'px');});};$('.video-parallax').each(function(){$(this).vparallaxfy();});$.fn.iparallaxfy=function(){var _this=$(this);var iparallheight=_this.height();var daimage=_this.find('.image-wrap img');var miniheight=(iparallheight*2)+(windowheight*.50);var paraypos2;daimage.css("min-height",miniheight+'px');_this.waypoint(function(direction)
{var scrll=$window.scrollTop();if(direction=="down")
{_this.addClass('parainview');paraypos2=$window.scrollTop();}else
{_this.removeClass('parainview');}},{offset:'100%'});_this.waypoint(function(direction){var scrll=$window.scrollTop();if(direction=="down")
{_this.removeClass('parainview');}else
{_this.addClass('parainview');}},{offset:-iparallheight});$(window).scroll(function(){var newvalue=parseInt(($(this).scrollTop()-paraypos2)*0.50);_this.find('.image-wrap').css('margin-top','-'+newvalue+'px');});};$('.image-parallax').each(function(){$(this).iparallaxfy();});$(window).load(function(){var $container=$('.blog-masonry');var $container=$('.blog-masonry').isotope({itemSelector:'.post',layoutMode:'masonry'});var $container2=$('.loop-list .woo-isotope');var $container2=$('.loop-list .woo-isotope').isotope({itemSelector:'.product',layoutMode:'masonry'});var $container3=$('.bottom-widgets');var $container3=$('.bottom-widgets').isotope({itemSelector:'.widget',layoutMode:'masonry'});});if($('.loop-list .products').length>0&&$('.woo-infiscroll').length>0)
{var infinite_scroll={loading:{img:null,msgText:'<div class="infi-loader"><span class="infi-spinner"><i class="fa fa-spinner fa-spin" style="font-size:24px"></i><span><span class="infi-loadingtext">Loading..<span></div>',finishedMsg:'<div class="infi-loader">All Items loaded.</div>',finished:destryandload,},nextSelector:".page-numbers .next",navSelector:".page-numbers",itemSelector:"li.product",contentSelector:"ul.products",animate:true,dataType:'html',bufferPx:40,};$(infinite_scroll.contentSelector).infinitescroll(infinite_scroll);}
function destryandload()
{$('.woo-border-box').each(function(){if($(this).children('a:first-child').children('img').length>1&&!$(this).hasClass('nx-flipit'))
{$(this).addClass('nx-flipit');}});var $container2=$('.loop-list .woo-isotope');var $container2=$('.loop-list .woo-isotope').isotope('destroy');$('.loop-list .woo-isotope').imagesLoaded().done(function(instance){}).fail(function(){var $container2=$('.loop-list .woo-isotope').isotope({itemSelector:'.product',layoutMode:'masonry'});});}})(jQuery);jQuery(document).ready(function($){"use strict";$('.tooltip:not(.headerwrap .tooltip)').each(function(){$(this).tooltipster({animation:'grow',touchDevices:false});});$('.grid-image.tooltip2').each(function(){$(this).tooltipster({animation:'grow',touchDevices:false});});if($(window).width()>=1069)
{$(window).load(function(){$('.site-header .nav-container > ul').lavalamp({easing:'easeOutBack',activeObj:'current-menu-item, .current_page_item, .current-menu-parent, .current-menu-ancestor'});});}
if($('.go-top').length>0)
{jQuery(window).scroll(function(){if(jQuery(this).scrollTop()>200){jQuery('.go-top').fadeIn(200).addClass('bounce');}else{jQuery('.go-top').fadeOut("slow");}});jQuery('.go-top').click(function(event){event.preventDefault();jQuery('html, body').animate({scrollTop:0},1000);});}
if($('.nx-popup-link').length>0)
{$('.nx-popup-link').magnificPopup({type:'image'});}
if($('.sort-order-select').length>0)
{$('.sort-order-select').each(function(){$(this).chosen({disable_search_threshold:10});});}
$('.nx-owl-carousel').each(function(){$(this).owlCarousel({stopOnHover:true,navigation:true,paginationSpeed:1000,goToFirstSpeed:2000,singleItem:true,autoHeight:true,navigationText:["<i class=\"fa fa-angle-left\"></i>","<i class=\"fa fa-angle-right\"></i>"],theme:"nx-slider",transitionStyle:"fadeUp",addClassActive:true});});$('.nx-header-slider').each(function(){var slidespeed=$(this).data("slide-speed");console.log(slidespeed);$(this).owlCarousel({autoPlay:slidespeed,stopOnHover:true,navigation:true,paginationSpeed:1000,goToFirstSpeed:2000,slideSpeed:200,singleItem:true,autoHeight:true,navigationText:["<i class=\"fa fa-angle-left\"></i>","<i class=\"fa fa-angle-right\"></i>"],theme:"nx-slider",addClassActive:true});});$('.related.products ul.products').each(function(){var columns=$(this).data("column-count");$(this).owlCarousel({items:columns,navigation:true,autoHeight:true,itemsMobile:false,navigationText:["<i class=\"fa fa-angle-left\"></i>","<i class=\"fa fa-angle-right\"></i>"],theme:"nx-slider",addClassActive:true});});$('.nxprodscroll ul.products').each(function(){var columns=$(this).parent().parent().parent().data("column-count");$(this).owlCarousel({items:columns,navigation:true,autoHeight:true,itemsMobile:false,navigationText:["<i class=\"fa fa-angle-left\"></i>","<i class=\"fa fa-angle-right\"></i>"],theme:"nx-slider",addClassActive:true});});$('.mag-pop-img').each(function(){$(this).magnificPopup({type:'image'});});if($('.sidr-menu').length>0)
{$('body').append('<span class="alt-menu-toggle"><span class="genericon genericon-menu"></span></span>');if($('.woocombar').length>0)
{$('.menu-toggle').sidr({name:'sidr-left',speed:400,side:'left',source:'.woocombar,#navbar',onOpen:function(){$('.menu-toggle').delay(300).queue(function(){$(this).addClass('isoppen').dequeue();});},onClose:function(){$('.menu-toggle').removeClass('isoppen');}});}else{if($("#navbar").length>0)
{$('.menu-toggle').sidr({name:'sidr-left',speed:400,side:'left',source:'#navbar',onOpen:function(){$('.menu-toggle').delay(300).queue(function(){$(this).addClass('isoppen').dequeue();});},onClose:function(){$('.menu-toggle').removeClass('isoppen');}});}}}
if($('.sidr-menu').length>0)
{$(window).resize(function(){if(($('body').hasClass('sidr-open')&&$(window).width()>=1069)){$.sidr('close','sidr-left');}});$('.menu-toggle').hide();$('.alt-menu-toggle').click(function(){if($('body').hasClass('sidr-open')){$.sidr('close','sidr-left');$(this).animate({marginLeft:'0px'},200);}else
{$.sidr('open','sidr-left');$(this).animate({marginLeft:'260px'},200);}});}
if($('.classic-menu').length>0)
{var _this=$('.classic-menu');$('.menu-toggle').click(function(){if(_this.hasClass('classic-open')){_this.removeClass('classic-open');}else
{_this.addClass('classic-open');}});$('.nav-container > ul li a').click(function(){if($(this).parent('li').hasClass('class-menu-open')){$(this).parent('li').removeClass('class-menu-open');}else
{$(this).parent('li').addClass('class-menu-open');}});}
var nav_container=$('.headerboxwrap');var woo_bar_wrap=$('.woocombar-wrap');var stickystat=$('.headerboxwrap').data('sticky-header');var nav=$('.site-header');var top_spacing=30;var waypoint_offset=160;top_spacing=0;waypoint_offset=72;if($(window).width()<1069)
{stickystat=0;}
if(stickystat==1&&$(window).width()>=1069&&$(window).height()<($(document).height()-300))
{if($('.admin-bar').length>0)
{if($(window).width()<766)
{top_spacing=0;}else
{top_spacing=30;}}else
{top_spacing=0;}
nav_container.waypoint({handler:function(direction){if(direction=='down'){nav_container.css({'height':nav.outerHeight()});nav.stop().addClass("fixeddiv").css("top",-nav.outerHeight()).animate({"top":top_spacing});}else{nav_container.css({'height':'auto'});nav.stop().removeClass("fixeddiv").css("top",nav.outerHeight()).animate({"top":""});}},offset:function(){return-nav.outerHeight()-waypoint_offset;}});}
if($(".mega-menu").length>0)
{var imheader=$(".header-inwrap");var imoffset=imheader.offset();var imheader_left=imoffset.left;var imheader_width=imheader.width();var offset_mega=$(".mega-menu").offset();var mega_panel_left=offset_mega.left;var set_left=imheader_left-mega_panel_left+32;$('.mega-nx-wide-panel').each(function(){$(this).children(".mega-sub-menu").css("width",imheader_width);$(this).children(".mega-sub-menu").css("left",set_left);});$('.site').addClass('has-mega-menu');}
if(Modernizr.touch){$('body').addClass('nx-touch');}
$('.nx-heading-style-coloredline').bind('inview',function(event,isInView){if(isInView){$(this).addClass('headinview');}else{$(this).removeClass('headinview');}});if(($(".mega-menu").length<1)&&($(window).width()>=1069)&&($(".boxed").length>0)&&($(".default-header").length>0))
{$('.nav-menu li.menu-item.menu-item-has-children').each(function(){var nxnwidth=$('.nav-menu').outerWidth();var nxi=$(this);var nxipos=nxi.position();if((nxnwidth-nxipos.left)<240)
{$(this).addClass('nximoveleft');$(this).children('ul').children('.menu-item-has-children').addClass('nximoveleft');}});}
if($(".i-max-header").length>0)
{$(window).scroll(function(){setTimeout(function(){$('.site-header .nav-container > ul').lavalamp('update');},300);});$('.site-header .nav-container > ul > li ').hover(function(){$('.itemhovered').removeClass('itemhovered');$(this).addClass('itemhovered');$(this).parent('ul').addClass('menuhovered');;},function(){$('.itemhovered').removeClass('itemhovered');$('.menuhovered').removeClass('menuhovered');});}
$('.ispirit-slider').each(function(){var _this=$(this);var slider_delay=_this.data('delay');var slider_transition=_this.data('transition');if(slider_transition=='slide')
{$(this).owlCarousel({autoPlay:slider_delay,stopOnHover:true,navigation:true,paginationSpeed:1000,goToFirstSpeed:2000,singleItem:true,autoHeight:true,addClassActive:true,navigationText:["<i class=\"fa fa-angle-left\"></i>","<i class=\"fa fa-angle-right\"></i>"],theme:"nx-slider",pagination:true});}else
{$(this).owlCarousel({autoPlay:slider_delay,stopOnHover:true,navigation:true,paginationSpeed:1000,goToFirstSpeed:2000,singleItem:true,autoHeight:true,addClassActive:true,navigationText:["<i class=\"fa fa-angle-left\"></i>","<i class=\"fa fa-angle-right\"></i>"],theme:"nx-slider",transitionStyle:slider_transition,pagination:true});}});if($('.ispirit-slider').length>0)
{var slider_parallax=$('.ispirit-slider').data('parallax');if(slider_parallax==1)
{var slidetop=parseInt($('.ispirit-slider').offset().top);if($(window).width()>1069)
{$(window).scroll(function(){var newvalue2=parseInt($(this).scrollTop()*0.6);if(!($('.trans-header').length>0))
{newvalue2=newvalue2-56;}
if($(this).scrollTop()>slidetop)
{$('.ispirit-slider-img').css('margin-top',newvalue2+'px');$('.ispirit-slider .ispirit-slide-content-inner').css('margin-top','-'+(newvalue2/8)+'px');}
if($(this).scrollTop()<=slidetop)
{var slideheight2=$('.active .ispirit-slider-img').height();$('.ispirit-slider-img').css('margin-top',0+'px');$('.ispirit-slider .ispirit-slide-content-inner').css('margin-top',0+'px');}});}}
var header_height=$('.ispirit-slider').data('slider-height');var header_reduct=$('.ispirit-slider').data('slider-deduct');var winheight=$(window).height();var winwidth=$(window).width();if(header_height>100)
{if(winwidth>1200)
{$('.ispirit-slider .owl-wrapper-outer').css("height",header_height);$('.ispirit-slider-img').css("height",header_height);$('.ispirit-slider').css("maxHeight",header_height);}else
{$('.ispirit-slider .owl-wrapper-outer').css("height",winheight*.6);$('.ispirit-slider-img').css("height",winheight*.6);$('.ispirit-slider').css("maxHeight",winheight*.6);}}else
{if(winwidth>1200)
{$('.ispirit-slider .owl-wrapper-outer').css("height",((winheight-header_reduct)/100)*header_height);$('.ispirit-slider-img').css("height",((winheight-header_reduct)/100)*header_height);$('.ispirit-slider').css("maxHeight",((winheight-header_reduct)/100)*header_height);}else
{$('.ispirit-slider .owl-wrapper-outer').css("height",winheight*.6);$('.ispirit-slider-img').css("height",winheight*.6);$('.ispirit-slider').css("maxHeight",winheight*.6);}}}
if($('body').hasClass('trans-header'))
{if($('img.reverse').length>0)
{$('.site-header').addClass('reverse-logo');}
if(($('img.normal').length>0)||($('img.common').length>0))
{$('.site-header').addClass('normal-logo');}}
$('ul.products li.product .add_to_wishlist, ul.products li.product .yith-wcwl-wishlistaddedbrowse a, ul.products li.product .yith-wcwl-wishlistexistsbrowse a, ul.products li.product .add_to_cart_button + a.compare').each(function(){$(this).wrapInner("<div class='nx-rightfloat'></div>");});if($('body').hasClass('nx-preloader'))
{$('.nx-preloader .nx-ispload').css("display","none");}
if($('.elementor-editor-active').length>0){$('.nx-ispload').css("display","none");}});