document.getElementById('locationForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const location = document.getElementById('location').value;

    fetch('/api/weather', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `location=${location}`
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
            return;
        }

        const currentValues = data.current_values;
        document.getElementById('humidity').textContent = `Humidity: ${currentValues.relative_humidity}%`;
        document.getElementById('apparentTemperature').textContent = `Apparent Temperature: ${currentValues.apparent_temperature}°C`;
        document.getElementById('precipitationProbability').textContent = `Precipitation Probability: ${currentValues.precipitation_probability}%`;
        document.getElementById('precipitation').textContent = `Precipitation: ${currentValues.precipitation} mm`;
        document.getElementById('surfacePressure').textContent = `Surface Pressure: ${currentValues.surface_pressure} hPa`;
        document.getElementById('cloudCover').textContent = `Cloud Cover: ${currentValues.cloud_cover}%`;
        document.getElementById('visibility').textContent = `Visibility: ${currentValues.visibility} km`;
        document.getElementById('windSpeed').textContent = `Wind Speed: ${currentValues.wind_speed} m/s`;
        document.getElementById('windDirection').textContent = `Wind Direction: ${currentValues.wind_direction}°`;

        const temperatureByHours = data.temperature_by_hours;
        const labels = temperatureByHours.map(item => item.date);
        const temperatures = temperatureByHours.map(item => item.temperature);

        const ctx = document.getElementById('temperatureChart').getContext('2d');
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Temperature (°C)',
                    data: temperatures,
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1,
                    fill: false
                }]
            },
            options: {
                scales: {
                    x: {
                        type: 'time',
                        time: {
                            unit: 'hour',
                            displayFormats: {
                                hour: 'MMM D, hA'
                            }
                        }
                    },
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    });
});
