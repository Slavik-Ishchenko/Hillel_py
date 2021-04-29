import requests
import json
import argparse
from datetime import timedelta, datetime
from pprint import pprint
today = datetime.now()
result = []
header = ['Date', 'Cur_From', 'Cur_To', 'Amount', 'Rate', 'Result']
result.append(header)


def inp_currency():
    with open('symbols.json', 'r+') as f:
        v = json.load(f)
        v_symbol = v['symbols']
        if arg.currency_from in v_symbol and arg.currency_to in v_symbol:
            currency_exchange()


def currency_exchange():
    if arg.date != today:
        date = datetime.strptime(arg.date, "%Y-%m-%d")
        while date < today:
            site = requests.get('https://api.exchangerate.host/convert',
                                params={'amount': arg.amount, 'from': arg.currency_from, 'to': arg.currency_to,
                                        'date': date}).json()
            values = [site['date'], site['query']['from'], site['query']['to'], site['query']['amount'],
                      site['info']['rate'], site['result']]
            date += timedelta(days=1)
            result.append(values)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Converter App')
    parser.add_argument('currency_from', type=str, default='USD')
    parser.add_argument('currency_to', type=str, default='UAH')
    parser.add_argument('amount', type=float, default=100)
    parser.add_argument('date', type=str, default=today)
    arg = parser.parse_args()

currency_exchange()
pprint(result)
