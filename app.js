const form = document.getElementById('weatherForm');
const townInput = document.getElementById('townInput');
const weatherInfo = document.getElementById('weatherInfo');

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const townName = townInput.value;
    try {
        const response = await fetch(`YOUR_WEATHER_API_URL?q=${townName}&appid=YOUR_API_KEY`);
        const data = await response.json();
        const { humidity, uvi, wind } = data.main;
        weatherInfo.innerHTML = `
            <p>Humidity: ${humidity}%</p>
            <p>UV Index: ${uvi}</p>
            <p>Wind Speed: ${wind.speed} m/s</p>
        `;
    } catch (error) {
        weatherInfo.innerHTML = '<p>Error fetching weather data. Please try again.</p>';
    }
});
