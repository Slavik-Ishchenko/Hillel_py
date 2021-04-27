import csv
import argparse
#o=tz_opendata_z01012021_po01042021.csv --brand "RENAULT" --color "ЧЕРВОНИЙ" --year 2012 --fuel "БЕНЗИН" --reg_num "АЕ6570ОР"  для теста
#o=tz_opendata_z01012021_po01042021.csv --brand "SKODA" --color "БЕЖЕВЫЙ" --year 2012 --fuel "БЕНЗИН" --reg_num "ВІ9541ЕХ"
data = []
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find car')
    parser.add_argument('file_name', type=str)
    parser.add_argument('--brand', type=str)
    parser.add_argument('--color', type=str)
    parser.add_argument('--year', type=str)
    parser.add_argument('--fuel', type=str)
    parser.add_argument('--reg_num', type=str)
    args = parser.parse_args()
    if 'brand' or 'color' or 'year' or 'fuel' not in args:   #сомневаюсь в правильности написания, но все работает
        exit(0)


def main():
    with open('tz_opendata_z01012021_po01042021.csv', encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            if row['N_REG_NEW'] == args.reg_num:
                data.append([row['D_REG'], row['BRAND'], row['MODEL'], row['COLOR'], row['MAKE_YEAR'], row['FUEL'],
                             row['N_REG_NEW']])
    head = [['D_REG'], ['BRAND'], ['MODEL'], ['COLOR'], ['MAKE_YEAR'], ['FUEL'], ['N_REG_NEW']]
    with open(f'brand-{str(args.brand).lower()}-year-{args.year}.csv', 'w+') as make_file:
        csv_writer = csv.writer(make_file, delimiter=';')
        csv_writer.writerow(head)
        for i in data:
            csv_writer.writerow(i)


main()
