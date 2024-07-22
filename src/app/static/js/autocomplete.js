$(document).ready(function() {
    $("#location").autocomplete({
        source: function(request, response) {
            $.ajax({
                url: "/api/search_cities",
                dataType: "json",
                data: {
                    term: request.term
                },
                success: function(data) {
                    response(data);
                }
            });
        },
        minLength: 2,
        select: function(event, ui) {
            $("#location").val(ui.item.value);
        }
    });
});