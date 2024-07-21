// autocomplete.js
document.addEventListener('DOMContentLoaded', function() {
    // Автозаполнение с использованием jQuery UI
    $("#location").autocomplete({
        source: function(request, response) {
            $.ajax({
                url: "/api/city_suggestions",
                type: "GET",
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
            // Действия при выборе города из списка автозаполнения
            $("#location").val(ui.item.label);
            return false;
        }
    });
});
