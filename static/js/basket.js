window.onload = function() {
    $('.basket_list').on('click','input[type="number"]', function() {
        var t_href = event.target;
        console.log(t_href.name);
        console.log(t_href.value);

        $.ajax({
            url: "/baskets/edit/" + t_href.name + "/" + t_href.value + "/",
            success: function (data) {
                $('.basket_list').html(data.result);
            }
        });
        event.preventDefault();
    });
}

window.onload = function() {
    $('.basket_list').on('click', 'button[type="button"]', function() {
        var t_href = event.target;

    // console.log(event.target);
//        console.log(t_href.href);

        $.ajax({
            url: "/baskets/remove/" + t_href.name + "/",
            success: function (data) {
                $('.basket_list').html(data.result);
            }
        });
        event.preventDefault();
    });
}
