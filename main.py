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


def dev_colour_view(color01, color02, color03, color04):
    height = 250
    width = 250 * 4
    image = PIL.Image.new('RGB', (width, height),  (255, 0, 0))
    
    for y in range(0, height):
        for x in range(0, width):

            # Color each square:
            if (x > 0 and x < height * 1):
                image.putpixel((x, y), color01)
            elif (x > height * 1 and x < height * 2):
                image.putpixel((x, y), color02)
            elif (x > height * 2 and x < height * 3):
                image.putpixel((x, y), color03)
            elif (x > height * 3 and x < height * 4):
                image.putpixel((x, y), color04)
    
    image.show()
    image.close()

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
        
        print('condition colors')
        print(weather_update.get_condition_colors())
        condition_colors = weather_update.get_condition_colors()

        # dbugImage:
        dev_colour_view(
            condition_colors[0],
            condition_colors[1],
            condition_colors[2],
            condition_colors[3]
        )

        # Api timer:
        time.sleep(api_update_timer)


main()

