// autocomplete.js

document.addEventListener('DOMContentLoaded', function() {
    const input = document.getElementById('location');

    // Инициализация автозаполнения с Google Places API
    if (typeof google !== 'undefined') {
        const autocomplete = new google.maps.places.Autocomplete(input);

        autocomplete.addListener('place_changed', function() {
            const place = autocomplete.getPlace();
            if (place.geometry) {
                // Извлекаем географические координаты
                const lat = place.geometry.location.lat();
                const lng = place.geometry.location.lng();

                // Отправляем координаты на сервер для получения данных погоды
                fetchWeatherData(lat, lng);
            }
        });
    } else {
        console.error('Google Maps JavaScript API не загружен.');
    }

    function fetchWeatherData(lat, lng) {
        fetch('/api/weather', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `lat=${lat}&lng=${lng}`
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
                return;
            }

            // Обновляем данные погоды и график
            updateWeatherInfo(data.current_values);
            updateTemperatureChart(data.temperature_by_hours);
        });
    }
});
