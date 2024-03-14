from pyowm.owm import OWM
import pytz

owm = OWM('f90f9bec6513fedbcf4e335f4f5c8c5e')
weather_mgr = owm.weather_manager()
mgr = owm.weather_manager()
reg = owm.city_id_registry()


def get_tel_aviv_weather():
    observation = mgr.weather_at_place('Tel Aviv, IL')
    weather = observation.weather
    temperature = weather.temperature('celsius')['temp']
    sunrise_utc = weather.sunrise_time(timeformat='date')
    sunset_utc = weather.sunset_time(timeformat='date')
    tel_aviv_timezone = pytz.timezone('Asia/Jerusalem')
    sunrise_tel_aviv = sunrise_utc.astimezone(tel_aviv_timezone)
    sunset_tel_aviv = sunset_utc.astimezone(tel_aviv_timezone)
    wind_speed = weather.wind()['speed']

    print(f"It's currently {weather.detailed_status} and {int(round(temperature, 0))}°С in Tel-Aviv.")
    print(f"The wind is {wind_speed} m/s.")
    print(f"The sunrise today at {sunrise_tel_aviv.strftime("%I:%M %p")} ")
    print(f"The sunset today at {sunset_tel_aviv.strftime("%I:%M %p")} ")

get_tel_aviv_weather()