from WeatherStation import WeatherStation
from FlightData import FlightData
import constants
import time

if __name__ == "__main__":
    ws = WeatherStation()

    fd = FlightData()
    fd.setZone(constants.HOME_ZONE)
    while(True):
        data = fd.run()
        if len(data) == 0:
            ws.updateWeatherData()
            print("Weather: " + ws.getWeather())
            print("Temperature: " + str(round(ws.getTemperature())) + " C")
        else:
            print(data)
        time.sleep(3)