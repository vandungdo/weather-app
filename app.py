from flask import Flask, redirect, render_template, url_for, request
from API_key import apiKey
import requests

app = Flask(__name__)

@app.route('/',methods =['GET','POST'])
def home():
    response = []
    weather = {}
    if request.method=='POST':
        city = request.form.get('city')
        response.append(requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+apiKey()).json())
        weather = {
            'City': response[0]['name'],
            'Location':response[0]['coord'],
            'Main_weather' : response[0]['weather'][0]['main'],
            'Description_weather' : response[0]['weather'][0]['description'],
            'Temperatur': round(response[0]['main']['temp']-273.15),
            'Feels_like': round(response[0]['main']['feels_like']-273.15),
            'Temp_min': round(response[0]['main']['temp_min']-273.15),
            'Temp_max': round(response[0]['main']['temp_max']-273.15),
            'Humidity': response[0]['main']['humidity']
        }
    return render_template('index.html',weather=weather)

# @app.route('/city',methods=['GET','POST'])
# def city():
#     city = request.form.get('city')
#     print(city)
#     # response = requests('api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+apiKey())
#     return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True,host='127.0.0.1',port=5001)