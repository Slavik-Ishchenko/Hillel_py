import urllib.request
import json
import datetime
from json import load
import datetime
# from_currency = str(input('Из валюты: '))
# to_currency = str(input('В валюту: '))
# amount = float(input('Сумма средств: '))
# start_date = str(input('Введите дату: '))
link = urllib.request.urlopen("https://api.exchangerate.host/convert")
with open('symbols.json', 'r+') as file:
    symbols_json = json.load(file)
    c = symbols_json['symbols']
print(c)

