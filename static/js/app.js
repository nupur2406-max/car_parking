
$(document).ready(function(){
$('body').append('<div class="bg-backdrop"></div>');
  var header = $(".top_header");
  $(window).scroll(function() {
        var scroll = $(window).scrollTop();
        if (scroll >= 100) {
            header.removeClass("pt-4").addClass('bg-white shadow-sm');
            $('.navbar ').removeClass('shadow-sm');
        } else {
            header.addClass('pt-4').removeClass('bg-white shadow-sm');
             $('.navbar ').addClass('shadow-sm');
        }
    });


$('.btn_view').click(function(){
   $('.filter-box').addClass('show');
   $('.bg-backdrop').addClass('show');
   $('.wrapper').addClass('blur_fillter');
});

//All Close filter icon btn

  $('.close_btn').click(function(){
              $('.filter-box').removeClass('show');
              $('.bg-backdrop').removeClass('show');
              $('.wrapper').removeClass('blur_fillter');
              $('body').removeAttr('style');



});

});
