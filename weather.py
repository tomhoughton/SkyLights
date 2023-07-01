import json

class Weather:
    def __init__(self, condition, temp, uv) -> None:
        self.condition = condition
        self.temp = temp
        self.uv = uv

        # read the json file containing colors for weather:
        json_file = open('conditions.json')
        self.weather_color_m = json.load(json_file)
        
    def get_condition(self):
        return self.condition


    def get_temp(self):
        return self.temp


    def get_uv(self):
        return self.uv
    

    def get_condition_colors(self):

        # We need to convert things into tuples:
        colors = self.weather_color_m[self.get_condition()]['color']
        return [
            tuple(colors[0]),
            tuple(colors[1]),
            tuple(colors[2]),
            tuple(colors[3])
        ]