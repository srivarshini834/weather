from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Your verified API Key from image_a2a65f.png
API_KEY = "114eb81a1806873513578ec8bbfeb20d"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    city = request.form.get('city')
    units = request.form.get('units', 'metric') # Concept 7: Unit Conversion
    
    # Concept 1: API Integration
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={units}"
    
    response = requests.get(url)
    data = response.json()

    # Concept 5: Error Handling
    if data.get("cod") != 200:
        return f"Error: {data.get('message', 'City not found')}. Note: New keys take 30-60 mins to activate.", 400

    weather_info = {
        "city": data["name"],
        "temp": data["main"]["temp"],
        "desc": data["weather"][0]["description"].capitalize(),
        "icon": data["weather"][0]["icon"], # Concept 6: Visual Elements
        "humidity": data["main"]["humidity"],
        "wind": data["wind"]["speed"],
        "units": "°C" if units == "metric" else "°F"
    }

    return render_template('results.html', weather=weather_info)

if __name__ == '__main__':
    app.run(debug=True, port=5050)