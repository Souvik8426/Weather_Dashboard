# Weather Dashboard

A simple weather dashboard built with Flask that fetches weather data from the OpenWeather API and displays it using a modern, sleek front-end design.

## Features

- Search for weather by entering a city name.
- Quick access to most of the cities(depends on openweather).
- Modern UI.
- Responsive design built using Bootstrap.

## Prerequisites

- Python 3.7+
- An OpenWeather API key (available at https://openweathermap.org/api)

## Installation

Clone the repository:
```bash
git clone https://github.com/your-username/weather-dashboard.git
cd weather-dashboard
```

Create a virtual environment(optional):
```bash
python -m venv venv
source venv/bin/activate   (or venv\Scripts\activate on Windows)
```

Install the dependencies:
```bash
pip install -r requirements.txt
```

Set up your environment variables by creating a .env file in the project root:
OPENWEATHER_API_KEY=your_openweather_api_key_here

## Usage

Run the Flask application:
python app.py

Then, open your browser and navigate to:
http://localhost:5000

## Project Structure

weather-dashboard/
  ├── app.py                # Main Flask application
  ├── index.html            # Front-end HTML file
  ├── requirements.txt      # Python dependencies
  ├── .env                  # Environment variables (not tracked in Git)
  └── README.md             # Project documentation

## API Endpoints

GET /  
Serves the main HTML page.

GET /get_weather  
Retrieves weather data for the specified city via the query parameter "city".
Example: http://localhost:5000/get_weather?city=Delhi

## License

This project is licensed under the MIT License.

## Acknowledgements

- OpenWeather for providing the weather API.
- Flask for the web framework.
- Bootstrap and Font Awesome for front-end styling.
