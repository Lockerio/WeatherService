document.addEventListener('DOMContentLoaded', function() {
    let chartInstance;

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
            document.getElementById('humidity').textContent = `Влажность: ${currentValues.relative_humidity}%`;
            document.getElementById('currentTemperature').textContent = `Температура: ${currentValues.current_temperature}°C`;
            document.getElementById('apparentTemperature').textContent = `Ощущаемая температура: ${currentValues.apparent_temperature}°C`;
            document.getElementById('precipitationProbability').textContent = `Вероятность осадков: ${currentValues.precipitation_probability}%`;
            document.getElementById('precipitation').textContent = `Осадки: ${currentValues.precipitation} mm`;
            document.getElementById('surfacePressure').textContent = `Атмосферное давление: ${currentValues.surface_pressure} hPa`;
            document.getElementById('cloudCover').textContent = `Облачность: ${currentValues.cloud_cover}%`;
            document.getElementById('visibility').textContent = `Видимость: ${currentValues.visibility} km`;
            document.getElementById('windSpeed').textContent = `Скорость ветра: ${currentValues.wind_speed} m/s`;
            document.getElementById('windDirection').textContent = `Направление ветра: ${currentValues.wind_direction}°`;

            const temperatureByHours = data.temperature_by_hours;
            const labels = temperatureByHours.map(item => item.date);
            const temperatures = temperatureByHours.map(item => item.temperature);

            const ctx = document.getElementById('temperatureChart').getContext('2d');

            if (chartInstance) {
                chartInstance.destroy();
            }

            chartInstance = new Chart(ctx, {
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
                    plugins: {
                        legend: {
                            display: false
                        },
                        datalabels: {
                            align: 'end',
                            anchor: 'end',
                            formatter: function(value, context) {
                                return value + '°C';
                            }
                        }
                    },
                    layout: {
                        padding: {
                            top: 40,
                            bottom: 40
                        }
                    },
                    scales: {
                        x: {
                            type: 'time',
                            time: {
                                unit: 'hour',
                                displayFormats: {
                                    hour: 'dd.MM HH:mm'
                                }
                            },
                            ticks: {
                                maxRotation: 45,
                                minRotation: 30
                            }
                        },
                        y: {
                            beginAtZero: true
                        }
                    }
                },
                plugins: [ChartDataLabels]
            });
        });
    });
});
