/**
  * isMobile
  * responsiveMenu
  * headerFixed
  * ajaxContactForm
  * alertBox
  * testimonialSlide
  * testimonialFlexSlide
  * testimonialFlexSlideStyle1
  * flatTestimonials
  * flexPortfolio
  * flexBlog
  * flatTeam
  * flatTeamstyle2
  * portfolioIsotope
  * detectViewport
  * counter
  * flatEventSlide
  * featuredPost
  * flatGallery
  * popupGallery
  * sectionVideo
  * togglesAccordion
  * responsiveVideo
  * flatAnimation
  * flatCountdown
  * swClick
  * goTop
  * retinaLogos
  * parallax
  * removePreloader
  * topSearch
*/

;(function($) {

   'use strict'

    var isMobile = {
        Android: function() {
            return navigator.userAgent.match(/Android/i);
        },
        BlackBerry: function() {
            return navigator.userAgent.match(/BlackBerry/i);
        },
        iOS: function() {
            return navigator.userAgent.match(/iPhone|iPad|iPod/i);
        },
        Opera: function() {
            return navigator.userAgent.match(/Opera Mini/i);
        },
        Windows: function() {
            return navigator.userAgent.match(/IEMobile/i);
        },
        any: function() {
            return (isMobile.Android() || isMobile.BlackBerry() || isMobile.iOS() || isMobile.Opera() || isMobile.Windows());
        }
    };

	var responsiveMenu = function() {
        var menuType = 'desktop';

        $(window).on('load resize', function() {
            var currMenuType = 'desktop';
            if ( matchMedia( 'only screen and (max-width: 991px)' ).matches ) {
                currMenuType = 'mobile';
            }

            if ( currMenuType !== menuType ) {
                menuType = currMenuType;

                if ( currMenuType === 'mobile' ) {
                    var $mobileMenu = $('#mainnav').attr('id', 'mainnav-mobi').hide();
                    var hasChildMenu = $('#mainnav-mobi').find('li:has(ul)');

                    $('#header').after($mobileMenu);
                    hasChildMenu.children('ul').hide();
                    hasChildMenu.children('a').after('<span class="btn-submenu"></span>');
                    $('.btn-menu').removeClass('active');
                } else {
                    var $desktopMenu = $('#mainnav-mobi').attr('id', 'mainnav').removeAttr('style');

                    $desktopMenu.find('.submenu').removeAttr('style');
                    $('#header').find('.nav-wrap').append($desktopMenu);
                    $('.btn-submenu').remove();
                }
            }
        });

        $('.btn-menu').on('click', function() {        	
            $('#mainnav-mobi').slideToggle(300);
            $(this).toggleClass('active');
        });

        $(document).on('click', '#mainnav-mobi li .btn-submenu', function(e) {
            $(this).toggleClass('active').next('ul').slideToggle(300);
            e.stopImmediatePropagation()
        });
    }

    var headerFixed = function() {
        if ( $('body').hasClass('header-sticky') ) {            
            $('#header').sticky();
        }
    }

    var ajaxContactForm = function() {  
        $('').each(function() {
            $(this).validate({
                submitHandler: function( form ) {
                    var $form = $(form),
                        str = $form.serialize(),
                        loading = $('<div />', { 'class': 'loading' });

                    $.ajax({
                        type: "POST",
                        url:  $form.attr('action'),
                        data: str,
                        beforeSend: function () {
                            $form.find('.submit-wrap').append(loading);
                        },
                        success: function( msg ) {
                            var result, cls;                            
                            if ( msg == 'Success' ) {                                
                                result = 'Message Sent Successfully To Email Administrator. ( You can change the email management a very easy way to get the message of customers in the user manual )';
                                cls = 'msg-success';
                            } else {
                                result = '';
                                cls = 'msg-error';
                            }

                            $form.prepend(
                                $('<div />', {
                                    'class': 'flat-alert ' + cls,
                                    'text' : result
                                }).append(
                                    $('<a class="close" href="#"><i class="fa fa-close"></i></a>')
                                )
                            );

                            $form.find(':input').not('.submit').val('');
                        },
                        complete: function (xhr, status, error_thrown) {
                            $form.find('.loading').remove();
                        }
                    });
                }
            });
        }); // each contactform
    };   

    var alertBox = function() {
        $(document).on('click', '.close', function(e) {
            $(this).closest('.flat-alert').remove();
            e.preventDefault();
        })     
    }  

    var twitterFeed = function () {
        if ( $().tweet ) {
            $('.list-tiwtter').each(function () {
                var $this = $(this);
                $this.tweet({
                    username: $this.data('username'),
                    join_text: "auto",
                    avatar_size: null,
                    count: $this.data('number'),
                    template: "{text}",
                    loading_text: "loading tweets...",
                    modpath: $this.data('modpath')      
                }); // tweet
            }); // lastest-tweets each
        };
    };
   
    var testimonialSlide = function() {
        $('.flat-testimonials-slider').each(function(){
            $(this).children('#flat-testimonials-carousel').flexslider({
                animation: "slide",
                controlNav: false,
                animationLoop: false,
                slideshow: true,
                itemWidth: 70,
                itemMargin: 30,
                asNavFor: $(this).children('#flat-testimonials-flexslider')
            });
            $(this).children('#flat-testimonials-flexslider').flexslider({
                animation: "slide",
                controlNav: false,
                animationLoop: true,
                slideshow: true,
                directionNav: false,                
                sync: $(this).children('#flat-testimonials-carousel'),
                prevText: '<i class="fa fa-angle-left"></i>',
                nextText: '<i class="fa fa-angle-right"></i>'
            });
        });
    };

    var testimonialFlexSlide = function() {
        if ( $().flexslider ) {
            $('.flat-row').each(function() {
                var $this = $(this)
                $this.find('.testimonials-flexslides').flexslider({
                    animation      :  "fade",
                    direction      :  "vertical", // vertical
                    pauseOnHover   :  false,
                    useCSS         :  false,
                    easing         :  "swing",
                    animationSpeed :  500,
                    slideshowSpeed :  5000,
                    controlNav     :  true,
                    directionNav   :  false,
                    slideshow      :  false,
                    smoothHeight   :  false
                }); // flexslider
            }); // flat-row
        }
    };

    var testimonialFlexSlideStyle1 = function() {
        if ( $().flexslider ) {
            $('.flat-row').each(function() {
                var $this = $(this)
                $this.find('.testimonials-flexslides1').flexslider({
                    animation      :  "fade",
                    pauseOnHover   :  false,
                    useCSS         :  false,
                    easing         :  "swing",
                    animationSpeed :  500,
                    slideshowSpeed :  5000,
                    controlNav     :  false,
                    directionNav   :  true,
                    slideshow      :  false,
                    smoothHeight   :  false
                }); // flexslider
            }); // flat-row
        }
    };

    var flatTestimonials = function() {
        $('.flat-row').each(function() {            
            if ( $().owlCarousel ) {
                $(this).find('.flat-testimonials').owlCarousel({
                    loop: true,
                    margin: 30,
                    nav: $('.flat-testimonials').data('nav'),
                    dots: $('.flat-testimonials').data('dots'),                     
                    autoplay: $('.flat-testimonials').data('auto'),                    
                    responsive:{
                        0:{
                            items: 1
                        },
                        480:{
                            items: 2
                        },
                        767:{
                            items: 2
                        },
                        991:{
                            items: 2
                        },
                        1200: {
                            items: $('.flat-testimonials').data('item')
                        }
                    }
                });
            }
        });
    };

    var flexPortfolio = function() {
        if ( $().flexslider ) {
            $('.flat-row').each(function() {
                var $this = $(this)
                $this.find('.portfolio-flexslides').flexslider({
                    animation      :  "slide",
                    pauseOnHover   :  false,
                    useCSS         :  false,
                    easing         :  "swing",
                    animationSpeed :  500,
                    slideshowSpeed :  5000,
                    controlNav     :  true,
                    directionNav   :  false,
                    slideshow      :  false,
                    smoothHeight   :  false
                }); // flexslider
            }); // flat-row
        }
    };  

    var flexBlog = function() {
        if ( $().flexslider ) {
            $('.flat-one-four.flat-flexslides-blog').each(function() {
                var $this = $(this)
                $this.find('.entry.flat-flexslides').flexslider({
                    animation      :  "slide",
                    pauseOnHover   :  false,
                    useCSS         :  false,
                    easing         :  "swing",
                    animationSpeed :  500,
                    slideshowSpeed :  5000,
                    directionNav   :  false,
                    slideshow      :  false,
                    smoothHeight   :  false
                }); // flexslider
            }); // flat-row
        }
    };      

    var flatTeam = function() {
        $('.flat-row').each(function() {               
            if ( $().owlCarousel ) {
                $(this).find('.flat-team-carosuel').owlCarousel({
                    loop: true,
                    margin: 0,
                    nav: $('.flat-team-carosuel').data('nav'),
                    dots: $('.flat-team-carosuel').data('dots'),                     
                    autoplay: $('.flat-team-carosuel').data('auto'),                    
                    responsive:{
                        0:{
                            items: 1
                        },
                        767:{
                            items: 1
                        },
                        991:{
                            items: 1
                        },
                        1200: {
                            items: $('.flat-team-carosuel').data('item')
                        }
                    }
                });
            }
        });
    };

    var flatTeamstyle2 = function() {
        $('.flat-row').each(function() {               
            if ( $().owlCarousel ) {
                $(this).find('.flat-team-carosuel-style2').owlCarousel({
                    loop: true,
                    margin: 0,
                    nav: $('.flat-team-carosuel-style2').data('nav'),
                    dots: $('.flat-team-carosuel-style2').data('dots'),                     
                    autoplay: $('.flat-team-carosuel-style2').data('auto'),                    
                    responsive:{
                        0:{
                            items: 1
                        },
                        767:{
                            items: 1
                        },
                        991:{
                            items: 1
                        },
                        1200: {
                            items: $('.flat-team-carosuel-style2').data('item')
                        }
                    }
                });
            }
        });
    };

    var portfolioIsotope = function() {         
        if ( $().isotope ) {           
            var $container = $('.portfolio-wrap');
            $container.imagesLoaded(function(){
                $container.isotope({
                    itemSelector: '.item',
                    transitionDuration: '1s'
                });
            });           
        };
    };  

    var detectViewport = function() {
        $('[data-waypoint-active="yes"]').waypoint(function() {
            $(this).trigger('on-appear');
        }, { offset: '90%', triggerOnce: true });

        $(window).on('load', function() {
            setTimeout(function() {
                $.waypoints('refresh');
            }, 100);
        });
    };

    var counter = function() {
        $('.flat-counter').on('on-appear', function() { 
            $(this).find('.numb-counter').each(function() { 
                var to = parseInt( ($(this).attr('data-to')),10 ), speed = parseInt( ($(this).attr('data-speed')),10 );
                if ( $().countTo ) {
                    $(this).countTo({
                        to: to,
                        speed: speed
                    });
                }
            });
       });
    };
       
    var flatEventSlide = function() {
        $('.flat-eventdate-slider').each(function(){
            $(this).children('#flat-eventdate-carousel').flexslider({
                animation: "slide",
                controlNav: false,
                animationLoop: false,
                directionNav: false,
                slideshow: true,
                itemWidth: 242,
                itemMargin: 1,
                asNavFor: $(this).children('#flat-eventcontent-flexslider'),
                prevText: '<i class="fa fa-angle-left"></i>',
                nextText: '<i class="fa fa-angle-right"></i>'
            });
            $(this).children('#flat-eventcontent-flexslider').flexslider({
                animation: "slide",
                controlNav: false,
                animationLoop: true,
                slideshow: true,
                directionNav: true,                
                sync: $(this).children('#flat-eventdate-carousel'),
                prevText: '<i class="fa fa-angle-left"></i>',
                nextText: '<i class="fa fa-angle-right"></i>'
            });
        });
    };

    var featuredPost = function() {
        $('.widget.widget-featured-post').each(function() {                
            if ( $().owlCarousel ) {
                $(this).find('.widg-featured-post').owlCarousel({
                    loop: true,
                    margin: 0,
                    nav: $('.widg-featured-post').data('nav'),
                    dots: $('.widg-featured-post').data('dots'),                     
                    autoplay: $('.widg-featured-post').data('auto'),                    
                    responsive:{
                        0:{
                            items: 1
                        },
                        767:{
                            items: 1
                        },
                        991:{
                            items: 1
                        },
                        1200: {
                            items: 1
                        }
                    }
                });
            }
        });
    }; 

    var flatGallery = function() {
        $('.flat-row').each(function() {               
            if ( $().owlCarousel ) {
                $(this).find('.flat-gallery-carousel').owlCarousel({
                    loop: true,
                    margin: 0,
                    nav: $('.flat-gallery-carousel').data('nav'),
                    dots: $('.flat-gallery-carousel').data('dots'),                     
                    autoplay: $('.flat-gallery-carousel').data('auto'),                    
                    responsive:{
                        0:{
                            items: 1
                        },
                        480:{
                            items: 2
                        },
                        767:{
                            items: 2
                        },
                        991:{
                            items: 3
                        },
                        1200: {
                            items: $('.flat-gallery-carousel').data('item')
                        }
                    }
                });
            }
        });
    };

    var popupGallery = function () {
        $('.flat-row').each(function() {
            if ( $('a').hasClass('popup-gallery') ) {                
                 $(".popup-gallery").magnificPopup({
                    type: "image",
                    tLoading: "Loading image #%curr%...",
                    removalDelay: 600,
                    mainClass: "my-mfp-slide-bottom",
                    gallery: {
                        enabled: true,
                        navigateByImgClick: true,
                        preload: [ 0, 1 ]
                    },
                    image: {
                        tError: '<a href="%url%">The image #%curr%</a> could not be loaded.'
                    }
                });
            }
        });       
    }

    var sectionVideo = function () {
        if($().YTPlayer) {           
            $(".video-section").YTPlayer( {
                showControls: false,
                autoPlay: false
            }); 
            var v = $('.video-section');
            $('#video-controls a')
            .each(function() {
                var t = $(this);
                t.on('click', (function(e) {
                    e.preventDefault();  
                    if (t.hasClass('fa-play')) {
                        t.removeClass('fa-play')
                            .addClass(
                                'fa-pause');
                        v.playYTP();
                        return false
                    }                  
                    if (t.hasClass('fa-pause')) {
                        t.removeClass(
                                'fa-pause')
                            .addClass('fa-play');
                        v.pauseYTP();
                        return false
                    }                    
                }));
            });
        }
    }     

    var togglesAccordion = function() {
        var args = {duration: 600};
        $('.flat-toggle .toggle-title.active').siblings('.toggle-content').show();

        $('.flat-toggle.enable .toggle-title').on('click', function() {
            $(this).closest('.flat-toggle').find('.toggle-content').slideToggle(args);
            $(this).toggleClass('active');
        }); // toggle 

        $('.flat-accordion .toggle-title').on('click', function () {
            if( !$(this).is('.active') ) {
                $(this).closest('.flat-accordion').find('.toggle-title.active').toggleClass('active').next().slideToggle(args);
                $(this).toggleClass('active');
                $(this).next().slideToggle(args);
            } else {
                $(this).toggleClass('active');
                $(this).next().slideToggle(args);
            }     
        }); // accordion
    };

    var responsiveVideo= function() {
        if ( $().fitVids ) {
            $('.container').fitVids();
        }
    };

    var flatAnimation = function() {
        if ( isMobile.any() == null ) {
            $('.flat-animation').each( function() {
                var flatElement = $(this),
                    flatAnimationClass = flatElement.data('animation'),
                    flatAnimationDelay = flatElement.data('animation-delay'),
                    flatAnimationOffset = flatElement.data('animation-offset');

                flatElement.css({
                    '-webkit-animation-delay':  flatAnimationDelay,
                    '-moz-animation-delay':     flatAnimationDelay,
                    'animation-delay':          flatAnimationDelay
                });

                flatElement.waypoint(function() {
                    flatElement.addClass('animated').addClass(flatAnimationClass);
                },{
                    triggerOnce: true,
                    offset: flatAnimationOffset
                });
            });
        }
    };

    var flatCountdown = function() {
        var aquarius_style = function(data) {
         $(this.el).html(
            "<div class='circle days'>" +                
                "<div class='numb'>" + this.leadingZeros(data.days, 2) + "</div>" +
                "<div class='text'>Days</div>" +
            "</div>" +
            "<div class='circle hours'>" +                
                "<div class='numb'>" + this.leadingZeros(data.hours, 2) + "</div>" +
                "<div class='text'>Hours</div>" +
            "</div>" +
            "<div class='circle mins'>" +                
                "<div class='numb'>" + this.leadingZeros(data.min, 2) + "</div>" +
                "<div class='text'>Minutes</div>" +
            "</div>" +
            "<div class='circle secs'>" +                
                "<div class='numb'>" + this.leadingZeros(data.sec, 2) + "</div>" +
                "<div class='text'>Seconds</div>" +
            "</div>");
        }

        $('.countdown').each(function() {
            $(this).countdown({
                date: $(this).attr('data-date'),
                render: aquarius_style
            });
        });
    };  

    var swClick = function () {
        function activeLayout () {
            $(".switcher-container" ).on( "click", "a.sw-light", function() {
                $(this).toggleClass( "active" );
                $('body').addClass('home-boxed');  
                $('body').css({'background': '#f6f6f6' });                
                $('.sw-pattern.pattern').css ({ "top": "100%", "opacity": 1, "z-index": "10"});
            }).on( "click", "a.sw-dark", function() {
                $('.sw-pattern.pattern').css ({ "top": "98%", "opacity": 0, "z-index": "-1"});
                $(this).removeClass('active').addClass('active');
                $('body').removeClass('home-boxed');
                $('body').css({'background': '#fff' });
                return false;
            })       
        }

        function activePattern () {
            $('.sw-pattern').on('click', function () {
                $('.sw-pattern.pattern a').removeClass('current');
                $(this).addClass('current');
                $('body').css({'background': 'url("' + $(this).data('image') + '")', 'background-size' : '30px 30px', 'background-repeat': 'repeat' });
                return false
            })
        }

        activeLayout(); 
        activePattern();
    }  
    
    var goTop = function() {
        $(window).scroll(function() {
            if ( $(this).scrollTop() > 800 ) {
                $('.go-top').addClass('show');
            } else {
                $('.go-top').removeClass('show');
            }
        }); 

        $('.go-top').on('click', function() {            
            $("html, body").animate({ scrollTop: 0 }, 1000 , 'easeInOutExpo');
            return false;
        });
    };

    var retinaLogos = function() {
      var retina = window.devicePixelRatio > 1 ? true : false;
        if( retina ) {
            $( '.header .logo' ).find('img').attr( {src:'./images/logo@2x.png',width:'156',height:'102'} );   
            $( '.title-section .icon' ).find('img').attr( {src:'./images/icon/line@2x.png',width:'282',height:'24'} );
        }
    };    
    
    var parallax = function() {
        if ( $().parallax && isMobile.any() == null ) {
            $('.parallax1').parallax("50%", 0.2);
            $('.parallax2').parallax("50%", 0.4);  
            $('.parallax3').parallax("50%", 0.5);            
        }
    };

    var removePreloader = function() {        
        $('.loader').fadeOut('slow',function () {
            $(this).remove();
        });
    };  
   
    var topSearch = function () {
        $('.show-search').on( 'click', function () {
            if( !$('.top-search' ).hasClass( "show" ))
                $('.top-search').addClass( 'show' );
            else
                $( '.top-search' ).removeClass( 'show' );
        });
    }

   	// Dom Ready
	$(function() { 
        if ( matchMedia( 'only screen and (min-width: 991px)' ).matches ) {
            headerFixed();
        } 
        flatGallery();
        portfolioIsotope();
        flexPortfolio();        
        featuredPost();        
        flexBlog();
        detectViewport();        
        counter();         
        responsiveMenu();
        flatTeam();
        flatTeamstyle2();
        testimonialSlide();
        testimonialFlexSlide();
        testimonialFlexSlideStyle1();
        flatTestimonials();
        sectionVideo();
        popupGallery();
        flatCountdown();
        flatEventSlide();
        togglesAccordion();    
        ajaxContactForm();
        alertBox();
        twitterFeed();           
        flatAnimation();
        topSearch();
        swClick();
        goTop();        
        responsiveVideo();
        retinaLogos(); 
        parallax();
        removePreloader();
   	});

})(jQuery);