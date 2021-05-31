import csv
import re


def number_inp():
    gos_number = str(input('Введите номер: ').upper())
    dict_trans = {'A': 'А', 'B': 'В', 'C': 'С', 'E': 'Е', 'H': 'Н', 'I': 'І', 'K': 'К', 'M': 'М', 'O': 'О', 'P': 'Р',
                  'T': 'Т', 'X': 'Х'}
    ukr = 'АВЕІКМНОРСТХ'
    indicator_of_number = re.findall(r'^[АВСЕНІКМОРТХABCEHIMOPTX]{2}\d{4}[АВСЕНІКМОРТХABCEHIMOPTX]{2}', gos_number)
    if not indicator_of_number:
        return False
    if indicator_of_number[0][0] and indicator_of_number[0][1] in ukr:
        work_string = indicator_of_number[0][0] + indicator_of_number[0][1]
        return work_string
    else:
        if len(indicator_of_number[0]) == 8:
            if indicator_of_number[0][0] or indicator_of_number[0][1] in dict_trans.keys():
                work_string = dict_trans[indicator_of_number[0][0]] + dict_trans[indicator_of_number[0][1]]
                return work_string


def find_region():
    working_string = [number_inp()]
    if not working_string[0]:
        return 'NUMBER NOT FOUND :('
    data = []
    with open('ua_auto.csv', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:
            if working_string[0] in row['Код 2004'] or working_string[0] in row['Код 2013']:
                data.append(row['Регіон'] + ': ' + row['Код 2004'] + ', ' + row['Код 2013'])
                ind = 0
                for letters in working_string:
                    while letters not in data[ind]:
                        ind += 1
                res = data[ind][:data[ind].index(':')]
                return res
        return 'NUMBER NOT FOUND :('


print(find_region())
