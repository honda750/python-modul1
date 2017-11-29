"""
    Vær      henter data på openweather
"""
import pyowm

myOwm = pyowm.OWM("dbf6aaf008f3591e4eeb64257fd2d985")

location = 'Bergen, Norway'
#location = 'Oslo, Norway'
#location = 'Tromsø, Norway'
#location = 'Bønes, Norway'



myWeather = myOwm.weather_at_place(location)

print (myWeather.get_weather().get_wind())
print (myWeather.get_weather().get_temperature('celsius'))
print (myWeather.get_weather().get_humidity())