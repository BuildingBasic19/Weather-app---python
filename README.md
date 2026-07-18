# Weather App 🌤️

A Python command-line app that fetches real-time weather data for any city using the OpenWeatherMap API.

---

## Features

- Fetches live weather data using the OpenWeatherMap API
- Displays current temperature in Celsius
- Displays current wind speed in m/s
- Clean error handling for failed requests
- Lightweight — no external UI libraries needed

---

## Project Structure

```
weather-app/
│
├── weather.py       # Main application file
└── README.md        # Project documentation
```

---

## Requirements

- Python 3.12+
- `requests` library

Install the required library using:

```bash
pip install requests
```

---

## Setup & Usage

### 1. Clone or download the project

```bash
git clone https://github.com/yourusername/weather-app.git
cd weather-app
```

### 2. Get your API key

- Go to [openweathermap.org](https://openweathermap.org)
- Create a free account
- Navigate to **API Keys** section
- Copy your key

### 3. Add your API key to the code

Open `weather.py` and replace the `api_key` value:

```python
api_key = "your_api_key_here"
```

> ⚠️ Never share your API key publicly or push it to GitHub.

### 4. Run the app

```bash
python weather.py
```

---

## How It Works

1. The app builds a request URL using the city name and your API key
2. It sends a GET request to the OpenWeatherMap API
3. The response comes back as JSON data
4. The app extracts temperature and wind speed from the nested JSON
5. Results are printed to the terminal

### API Endpoint Used

```
http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric
```

### Sample Output

```
Temperature of Delhi is 39.56°C and wind speed is 3.93 m/s
```

### Sample API Response Structure

```json
{
    "main": {
        "temp": 39.56,
        "feels_like": 41.88,
        "humidity": 29
    },
    "wind": {
        "speed": 3.93
    },
    "name": "Delhi"
}
```

---

## Future Plans

- [ ] Let the user input any city name instead of hardcoding Delhi
- [ ] Add humidity, feels like temperature, and weather description
- [ ] Add a 5-day forecast feature
- [ ] Build a GUI using CustomTkinter
- [ ] Store API key securely using environment variables
- [ ] Add support for multiple cities at once

---

## API Reference

- Provider: [OpenWeatherMap](https://openweathermap.org)
- Plan used: Free tier
- Docs: [Current Weather Data API](https://openweathermap.org/current)
- Rate limit on free plan: 60 calls/minute, 1,000,000 calls/month

---

## Author

**Anant**  
Aspiring Software Engineer | Python & Java  


---

## License

This project is open source and available under the [MIT License](LICENSE).
