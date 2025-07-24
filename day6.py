# #menggunakan m sebagai module rename atau alias
# import math as m
#
# #m.pi merupakan sintak untuk memanggil fungsi
# print("Nilai pi adalah:", m.pi)


#import sebagian
# from math import pi
# print("Nilai pi adalah", pi)


#membaca CSV
# import requests
# from contextlib import closing
# import csv
#
# # tentukan lokasi file, nama file, dan inisialisasi csv
# url = 'https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv'
#
# # baca file csv secara streaming
# with closing(requests.get(url, stream=True)) as r:
#     f = (line.decode('utf-8') for line in r.iter_lines())
#
#     reader = csv.reader(f, delimiter=',')
#
#     # membaca baris per baris
#     for row in reader:
#         print(row)


# menggunakan pandas
# import pandas as pd
# pd.set_option("display.max_columns",50)
#
# table = pd.read_csv("https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv")
# table.head()
# print(table)