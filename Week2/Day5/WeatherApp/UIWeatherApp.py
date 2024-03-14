from pyowm.owm import OWM
import pytz
import datetime
from timezonefinder import TimezoneFinder
import matplotlib.pyplot as plt

owm = OWM('f90f9bec6513fedbcf4e335f4f5c8c5e')
weather_mgr = owm.weather_manager()
mgr = owm.weather_manager()
reg = owm.city_id_registry()
tf = TimezoneFinder()


# Getting weather information
def get_weather(location):
    list_of_tuples = reg.ids_for(location, matching='like')
    city = list_of_tuples[0][0]
    city_coords = list_of_tuples[0][4], list_of_tuples[0][5]
    country = list_of_tuples[0][2]
    observation = mgr.weather_at_id(city)
    weather = observation.weather
    temperature = weather.temperature('celsius')['temp']
    sunrise_utc = weather.sunrise_time(timeformat='date')
    sunset_utc = weather.sunset_time(timeformat='date')
    timezone_name = tf.timezone_at(lat=city_coords[0], lng=city_coords[1])
    timezone = pytz.timezone(timezone_name)
    sunrise_in_the_city = sunrise_utc.astimezone(timezone)
    sunset_in_the_city = sunset_utc.astimezone(timezone)
    wind_speed = weather.wind()['speed']

    print(f"It's currently {weather.detailed_status} and {int(round(temperature, 0))}°С in {location + ", " + country}.")
    print(f"The wind is {wind_speed} m/s.")
    print(f"The sunrise today at {sunrise_in_the_city.strftime("%I:%M %p")} ")
    print(f"The sunset today at {sunset_in_the_city.strftime("%I:%M %p")} ")


# Creation of the chart
def init_plot(location):
    plt.figure(figsize=(10, 6))
    plt.xlabel('Date')
    plt.ylabel('Humidity (%)')
    plt.title(f'Three-Day Humidity Forecast in {location}')
    plt.grid(axis='y')


def plot_forecast_chart(location):
    # Getting 3-days humidity forecast for the chart
    list_of_tuples = reg.ids_for(location, matching='like')
    city = list_of_tuples[0][1]
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    forecaster = mgr.forecast_at_place(city, '3h')
    forecast = forecaster.forecast
    humidity_values = []
    dates = []
    for weather in forecast:
        if weather.reference_time('date').strftime('%Y-%m-%d') != today and len(dates) < 24:
            humidity_values.append(weather.humidity)
            dates.append(weather.reference_time('date').strftime('%Y-%m-%d'))

    # Creating the right forecast data
    part_size = len(humidity_values) // 3
    day1 = humidity_values[:part_size]
    day2 = humidity_values[part_size:2 * part_size]
    day3 = humidity_values[2 * part_size:]
    # Getting the average of each day
    avg_day1 = sum(day1) / len(day1)
    avg_day2 = sum(day2) / len(day2)
    avg_day3 = sum(day3) / len(day3)
    days_avg = [avg_day1, avg_day2, avg_day3]
    # Creating right amount of dates
    new_dates = []
    for date in dates:
        if date not in new_dates:
            new_dates.append(date)

    # Adding data to the chart
    plt.bar(new_dates, days_avg, color='skyblue')
    # Adding text to the chart
    for i, day in enumerate(days_avg):
        plt.text(i, day, f'{day}%', ha='center', va='bottom')
    plt.show()


# Main function
def main():
    print("Welcome to the weather forecast app!")
    while True:
        location = input("Enter the location: ").title()
        list_of_tuples = reg.ids_for(location, matching='like')
        if len(list_of_tuples) > 0:
            get_weather(location)
            init_plot(location)
            plot_forecast_chart(location)
            break
        else:
            print("Location not found! Try again")


main()
