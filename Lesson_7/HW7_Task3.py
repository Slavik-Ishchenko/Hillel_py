import urllib.request
from json import load
import datetime


def getting_parameters():
    city = str(input('Введите название города: ').lower())
    days = str(input('Введите количество дней: '))
    return city, days


def read_link(city, days):
    link = urllib.request.urlopen(f"http://api.openweathermap.org/data/2.5/forecast/daily?q={city}&cnt={days}&units=metric&appid=f9ada9efec6a3934dad5f30068fdcbb8")
    res = load(link)

    return res


def add_to_file(res):
    with open('19-09-2020-Odessa-5-days-weather-forecast.txt', 'w', encoding='utf-8') as file:
        file.write(str(f"""Погода для города {city.title()}:
Дата         Температура днем   Температура ночью   По ощущениям  """))
        for i in res['list']:
            file.write(datetime.datetime.fromtimestamp(i['dt']).strftime("\n%d-%m-%Y   "))
            file.write((str(i['temp']['day'])).ljust(19))
            file.write((str(i['temp']['night'])).ljust(20))
            file.write(str(i['feels_like']['day']))


city, days = getting_parameters()
res = read_link(city, days)
add_to_file(res)
