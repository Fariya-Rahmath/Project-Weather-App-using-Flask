from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    api_key = 'your api key'  # Replace with your own API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(url)
    weather_data = response.json()

    if weather_data['cod'] == '404':
        error_message = 'City not found'
        return render_template('G:\python\weather-flask\templates\index.html', error_message=error_message)
    else:
        temperature = round(weather_data['main']['temp'] - 273.15, 2)
        description = weather_data['weather'][0]['description']
        return render_template('G:\python\weather-flask\templates\weather.html', city=city, temperature=temperature, description=description)

if __name__ == '__main__':
    app.run(debug=True)
