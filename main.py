from weather import Weather
import json
import requests
import PIL.Image, PIL.ImageDraw
import time

# Imformation we need:
#condition.text
# uv
#temp_c
def get_data():
    res = requests.get('http://api.weatherapi.com/v1/current.json?key=e50ea9607d6740b08ac231014232906&q=SG189FX&aqi=no')
    return res.json()


def dbug_display_weather(weather_update):
    print('Current Weather statistics')
    print(weather_update.get_condition())
    print(weather_update.get_temp())
    print(weather_update.get_uv())


def dev_colour_view():
    height = 500
    width = 500 * 4
    image = PIL.Image.new('RGB', (height, width),  (255, 0, 0))
    
    for y in range(0, height):
        for x in range(0, width):
            image.putpixel((x, y), (255, 255, 1))
    
    image.show()

def main():

    api_update_timer = 1 # Controls how often we get new data.

    while(True):
        
        # Firstly create and get weather data:
        data = get_data()
        weather_update = Weather(
            data['current']['condition']['text'],
            data['current']['temp_c'],
            data['current']['uv'],
        )

        # dbug display:
        dbug_display_weather(weather_update)
        
        # dbugImage:
        dev_colour_view()

        # Api timer:
        time.sleep(api_update_timer)


main()

