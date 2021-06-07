import csv
import argparse

"""Добавить ошибки, 38:40 -- 16 занятие"""


class AirportNotFoundError(BaseException):
    def __init__(self, msg):
        super().__init__(msg)


class CountryNotFoundError(BaseException):
    def __init__(self, msg):
        super().__init__(msg)


class MultipleOptionsError(BaseException):
    def __init__(self, msg):
        super().__init__(msg)


class NoOptionsFoundError(BaseException):
    def __init__(self, msg):
        super().__init__(msg)


class IATACodeError(BaseException):
    def __init__(self, msg):
        super().__init__(msg)


def open_csv_file():
    data = []
    with open('airport-codes_csv.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=',')
        for par in reader:
            data.append(par)
    return data


def params():
    """Проверяет наличие и определяет необходимый параметр для дальнейшей работы"""
    arg_parameters_dict = {'name': args.name, 'country': args.country, 'iata_code': args.iata_code}
    work_dict_args = {k: v for k, v in arg_parameters_dict.items() if v is not None}
    if len(work_dict_args) > 1:
        raise MultipleOptionsError('Введите только 1 параметр')
    if len(work_dict_args) == 0:
        raise NoOptionsFoundError('Параметры отсутвуют, введите 1 параметр ')
    if 'iata_code' in work_dict_args.keys() and len(work_dict_args['iata_code']) != 3:
        raise IATACodeError('Параметр "iata_code" должен нести в себе 3 символа')
    for k, v in work_dict_args.items():
        return k, v


def work_with_data():
    res = []
    country = []
    par_key, par_value = params()
    data = open_csv_file()
    for row in data:
        if par_key == 'name' and par_value in row['name']:
            res.append(row['name'])
        if par_key == 'country' and par_value.upper() in row['iso_country']:
            res.append(row)
            country.append(row['iso_country'])
        if par_key == 'iata_code' and par_value.upper() in row['iata_code']:
            res.append(row)
    if len(country) == 0:
        raise CountryNotFoundError('Страна не найдена')
    if len(res) == 0:
        raise AirportNotFoundError('Аэропорт не найден')
    return res


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Airport')
    parser.add_argument('--iata_code', type=str)
    parser.add_argument('--country', type=str)
    parser.add_argument('--name', type=str)
    args = parser.parse_args()

print(work_with_data())
