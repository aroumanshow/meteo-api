from flask import Flask, request
import requests
import os

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")
DEFAULT_CITY = "Paris"
UNITS = "metric"

@app.route("/")
def meteo():
    ville = request.args.get("ville", DEFAULT_CITY)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ville}&appid={API_KEY}&units={UNITS}&lang=fr"

    response = requests.get(url)
    if response.status_code != 200:
        return f"❌ Ville inconnue : {ville}"

    data = response.json()
    temp = round(data["main"]["temp"])
    desc = data["weather"][0]["description"].capitalize()
    humidite = data["main"]["humidity"]

    return f"🌤️ Météo à {ville} : {temp}°C, {desc}, humidité {humidite}%"

if __name__ == "__main__":
    app.run()
