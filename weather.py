class Weather:
    def __init__(self, condition, temp, uv) -> None:
        self.condition = condition
        self.temp = temp
        self.uv = uv


    def get_condition(self):
        return self.condition


    def get_temp(self):
        return self.temp


    def get_uv(self):
        return self.uv