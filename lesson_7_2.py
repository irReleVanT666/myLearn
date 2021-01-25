


class WeatherService:
    def __init__(self):
        self.__weathers = None
        self.__today = None
        self._init_weather_by_api()

    def _init_weather_by_api(self):
        self.__weathers = [-14, -13, -4, 10, 20, 25, 10]
        self.__today = 4

    def get_today_weather(self):
        return self.__weathers[self.__today]

    def get_avg_weather(self):
        return sum(self.__weathers) / len(self.__weathers)
    def __str__(self):
        return f"Weather Service on ({self.__today})"


if __name__ == '__main__':
    a = WeatherService()
    some_dict = {a:3}
    b = str(a)
    # print(a.get_today_weather())
    print (some_dict)
    print(b)