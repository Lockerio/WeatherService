$(document).ready(function() {
    function updateCitiesList() {
        $.get('/api/get_cities', function(data) {
            const cities = data.cities;
            const citiesList = $('#cities');
            citiesList.empty();
            cities.forEach(city => {
                citiesList.append(`<li><a href="#" class="city-link" data-city="${city}">${city}</a></li>`);
            });

            $('.city-link').on('click', function(event) {
                event.preventDefault();
                const city = $(this).data('city');
                $('#location').val(city);

                $('#locationForm').submit();
            });
        });
    }

    $('#locationForm').on('submit', function(event) {
        event.preventDefault();
        const city = $('#location').val();
        $.post('/api/add_city', { city: city }, function() {
            updateCitiesList();
        });
        updateWeather(city);
    });

    updateCitiesList();
});
