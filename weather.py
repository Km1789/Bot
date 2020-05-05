import pyowm


def wet(city):
    owm = pyowm.OWM('6756101e852df5f0f9792a64a6be1412',
                    language="RU")  # используется апи от openweathermap и указан язык отображения информации
    observation = owm.weather_at_place(city)
    itog = observation.get_weather()
    sp = [f"В городе {city} температура составляет {itog.get_temperature('celsius')['temp']} градусов Цельсия",
          f"Влажность равна {itog.get_humidity()}%", f"Облачность {itog.get_clouds()}%",
          f"В данный момент: {itog.get_detailed_status()}"]
    return sp
