import requests
import json
import argparse
from datetime import timedelta, datetime
today = datetime.now()


def main():
    with open('symbols.json', 'r+') as f:
        v = json.load(f)
        v_symbol = v['symbols']
        if arg.currency_from in v_symbol and arg.currency_to in v_symbol:
            pars()


def pars():
    print('Date:                Currency_From:          Currency_To:          Amount:          Rate:          Result:')
    if arg.date != today:
        date = datetime.strptime(arg.date, "%Y-%m-%d")
        while date < today:
            site = requests.get('https://api.exchangerate.host/convert',
                                params={'amount': arg.amount, 'from': arg.currency_from, 'to': arg.currency_to,
                                        'date': date}).json()
            print(str(site['date']).ljust(21) + str(site['query']['from']).ljust(24) + str(site['query']['to']).ljust(
                22) + str(site['query']['amount']).ljust(17) + str(site['info']['rate']).ljust(15) + str(site['result']))
            date += timedelta(days=1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Converter App')
    parser.add_argument('currency_from', type=str, default='USD')
    parser.add_argument('currency_to', type=str, default='UAH')
    parser.add_argument('amount', type=float, default=100)
    parser.add_argument('date', type=str, default=today)
    arg = parser.parse_args()

pars()
