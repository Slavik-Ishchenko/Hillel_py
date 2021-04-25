import csv
import argparse
import requests

#     data = []
with open('tz_opendata_z01012021_po01042021.csv', 'r+') as file:
    # csv_writer = csv.writer(file)
    # csv_writer.writerows(data)
    csv_reader = csv.reader(file)
    print(list(csv_reader))
    # for row in csv_reader:
    #     print(row)

