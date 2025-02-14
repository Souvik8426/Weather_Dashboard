from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Fetch the API key from environment variables
API_KEY = os.getenv('OPENWEATHER_API_KEY')

# Route for the main page
@app.route('/')
def serve_html():
    return send_from_directory('.', 'index.html')

@app.route('/get_weather')
def get_weather():
    if not API_KEY:
        return jsonify({'error': 'API key not found. Please check your .env file'}), 500
    
    # Get city from query parameters, default to London if not provided
    city = request.args.get('city', 'London')
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # Check if the API call was successful
        if response.status_code == 200:
            weather_info = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
                'feels_like': data['main']['feels_like'],
                'wind_speed': data['wind']['speed']
            }
            return jsonify(weather_info)
        else:
            return jsonify({'error': f'OpenWeather API error: {data.get("message", "Unknown error")}'}), response.status_code
            
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Request failed: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)