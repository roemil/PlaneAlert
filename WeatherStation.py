import requests
import json
import constants

class WeatherStation:
    def __init__(self):
        self.weather = ""
        self.temperature = -99
        url25 = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apiKey}&units=metric"
        self.formattedUrl = url25.format(lat=constants.LAT, lon=constants.LON, apiKey=constants.API_KEY)

    def toJson(self, RequestResuls):
        return json.loads(RequestResuls.text)

    def getWeather(self):
        return self.forecast['weather'][0]['main']

    def getTemperature(self):
        return self.forecast['main']['temp']

    def toJson(self, Data):
        return json.loads(Data)

    def updateForecast(self):
        self.forecast = self.toJson(requests.get(self.formattedUrl).text)

    def updateWeatherData(self):
        self.updateForecast()