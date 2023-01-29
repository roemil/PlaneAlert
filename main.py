from WeatherStation import WeatherStation

if __name__ == "__main__":
    ws = WeatherStation()
    ws.updateWeatherData()
    print("Weather: " + ws.getWeather())
    print("Temperature: " + str(round(ws.getTemperature())) + " C")