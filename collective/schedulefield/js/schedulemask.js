jQuery(document).ready(function($) {
    $('.schedule-widget').each(function(){
        input = $(this);
        input.mask('99:99');
    });
});
