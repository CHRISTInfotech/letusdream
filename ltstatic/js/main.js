
$(window).on('scroll', function () {

    if ($(window).scrollTop()) {
        $('#navbar').addClass('black');
    }
    else {
        $('#navbar').removeClass('black');
    }
})

$(document).ready(function () {

    $('.counter').each(function () {
        $(this).prop('Counter', 0).animate({
            Counter: $(this).text()
        }, {
            duration: 4000,
            easing: 'swing',
            step: function (now) {
                $(this).text(Math.ceil(now));
            }
        });
    });

});




