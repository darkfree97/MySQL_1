$("#dialog").dialog({width:'345px', autoOpen : false});
$(".list-group div a").click(function(event){
    event.preventDefault();
    $("#dialog_image").attr('src',$(this).attr('href'));
    $("#dialog").dialog("open");
    return 0;
});
$('form').submit(function (event) {
    event.preventDefault();
    $.ajax({
        type: 'POST',
        url: '/strahova/search_dep/',
        data: {
            'region': $('#region').val(),
            'district': $('#district').val(),
            'city': $('#city').val(),
            'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
        },
        success: searchSuccess,
        dataType: 'html'
    })

});
function searchSuccess(data, textStatus, jqXHR) {
    $('.output_fields').html(data);
}