!function(e) {
    if ($(this).hasClass("navbar-toggle")) {
      $(".collapse").slideToggle("500");
    } else if ($(this).hasClass("radio-btn")) {
      $('.radio-btn').removeClass('checked');
      var obj = $(this);
      var thisInput = obj.find('.radio-class');
      thisInput.prop("checked", true);
      obj.addClass("checked");
    } else if ($(this).is("#myTabs")) {
      e.preventDefault()
      $(this).tab('show')
    } else if ($(this).is("#but_prev")) {
      carousel.prev();
    } else if ($(this).hasClass("search-click")) {
      window.setTimeout(
        function() {
          $(".form-search input").focus();
          //$('body').addClass('stop-scrolling');
        }, 500);
    } else if ($(this).is("#but_pause")) {
      carousel.pause();
    } else if ($(this).is("#but_start")) {
      carousel.start();
    } else if ($(this).is("#but_next")) {
      carousel.next();
    } else if ($(this).is("#play-video-btn")) {
      var video = document.getElementById('bg-video');
      var $video = $('#bg-video');
      var $control = $('#play-video-btn');
      //alert("qwer");
      if (video.paused == true) {
  
        video.play();
        $('.video-bg').hide();
        $control.parents('.video-controls').fadeTo(500, 0).css({
          'z-index': 0
        }).addClass('hidden');
        $video.parents('.video-wrap').addClass('hide-bg-overlay');
      } else {
        video.pause();
        $control.parents('.video-controls').fadeTo(10, 1).css({
          'z-index': 1
        }).removeClass('hidden');
        $video.parents('.video-wrap').removeClass('hide-bg-overlay');
      }
      e.preventDefault();
    } else if ($(this).is("#bg-video")) {
      var $video = $('#bg-video');
      var $control = $('#play-btn');
      if (video.paused == false) {
        $control.parents('.video-controls').fadeTo(10, 1).css({
          'z-index': 1
        }).removeClass('hidden');
        video.pause();
        $video.parents('.video-wrap').removeClass('hide-bg-overlay');
      } else {
        $control.parents('.video-controls').fadeTo(500, 0).css({
          'z-index': 0
        }).addClass('hidden');
        video.play();
        $video.parents('.video-wrap').addClass('hide-bg-overlay');
      }
    } else if ($(this).hasClass("lightbox")) {
      e.preventDefault();
      $(this).ekkoLightbox({
        alwaysShowClose: false
      });
    } else if ($(this).is("#products-grid")) {
      product_list = 'grid';
      $(".products-list-type").removeClass("active");
      $(this).addClass("active");
      $('#product-content').data("list_style", product_list);
      loadFilteredProducts(true);
    } else if ($(this).is("#products-list")) {
      product_list = 'list';
      $(".products-list-type").removeClass("active");
      $(this).addClass("active");
      $('#product-content').data("list_style", product_list);
      loadFilteredProducts(true);
    } else if ($(this).hasClass("e_categories")) {
      product_category = $(this).data('category');
      $(".e_categories").find("span").removeClass("active");
      $(this).find("span").addClass("active");
      loadFilteredProducts(true);
    } else if ($(this).hasClass("e_tags")) {
      product_tag = $(this).data('tag');
      $(".e_tags").find("span").removeClass("active");
      $(this).find("span").addClass("active");
      loadFilteredProducts(true);
    } else if ($(this).hasClass("composite_add_to_cart_button")) {
      refreshCart();
    } else if ($(this).hasClass("wc-quick-view-button")) {
      compositeListener();
    } else if ($(this).hasClass("add_to_cart_button")) {
      refreshCart();
    } else if ($(this).hasClass("remove")) {
      refreshCart();
    } else if ($(this).hasClass("product_modal_ajax")) {
      modalListener(this);
      e.preventDefault();
    } else if ($(this).hasClass("banner-video")) {
      $("#madangModal").html($(".video-banner-cont").html()).modal('show');
    } else if ($(this).hasClass("menu-item")) {
  
      createCookie("product_category", "", 1);
      createCookie("ppp", "", 1);
      createCookie("offset", "", 1);
      createCookie("product_list", "", 1);
      createCookie("product_tag", "", 1);
      createCookie("product_calories_low", "", 1);
      createCookie("product_calories_high", "", 1);
      createCookie("product_pricing_low", "", 1);
      createCookie("product_pricing_high", "", 1);
      createCookie("product_columns", "", 1);
      createCookie("pagenum_link", "", 1);
      createCookie("pagenum_order", "", 1);
    } else if ($(this).hasClass("hvr-wobble-top")) {
  
      if ($(window).width() < 768) {
        // Scroll to a certain element
        document.querySelector('.tab-content-block').scrollIntoView({
          behavior: 'smooth'
        });
      }
    } else if ($(this).hasClass("ajax_cat")) {
  
      createCookie("product_category", $(this).data('cat'), 1);
      createCookie("product_category_single", $(this).data('cat'), 1);
      return true;
    }
  }