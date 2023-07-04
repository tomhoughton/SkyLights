from weather import Weather
import json
import requests
import PIL.Image, PIL.ImageDraw
import time
import cv2
from simulator import Simulator
# So now we need to generate a video of frames: 

def get_data():
    res = requests.get('http://api.weatherapi.com/v1/current.json?key=e50ea9607d6740b08ac231014232906&q=SG189FX&aqi=no')
    return res.json()


def dbug_display_weather(weather_update):
    print('Current Weather statistics')
    print(weather_update.get_condition())
    print(weather_update.get_temp())
    print(weather_update.get_uv())

def main():

    SIM_MODE = True
    sim = None
    sim_frame_count = None

    if (SIM_MODE):
        sim = Simulator()
        sim_frame_count = 0

    api_update_timer = 1 # Controls how often we get new data.

    while(True):
        
        # Firstly create and get weather data:
        data = get_data()
        weather_update = Weather(
            data['current']['condition']['text'],
            data['current']['temp_c'],
            data['current']['uv'],
        )
        
        # Get the condition colors:
        condition_colors = weather_update.get_condition_colors()

        # dbugImage:
        if (SIM_MODE):
            sim.create_frame(
                condition_colors[0],
                condition_colors[1],
                condition_colors[2],
                condition_colors[3],
                sim_frame_count
            )
            sim_frame_count += 1

        # Api timer:
        time.sleep(api_update_timer)

        if (SIM_MODE):
            sim.display_frame_data()


main()

