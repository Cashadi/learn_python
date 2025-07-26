import pandas as pd
import matplotlib.pyplot as plt

# # Baca file
# table = pd.read_csv("C:/Users/Pongo/Documents/csv/electric_vehicles_spec_2025.csv.csv")

# # Bersihkan data yang hilang
# table = table.dropna(subset=['model', 'battery_capacity_kWh'])

# # Konversi model ke string
# x_label = table['model'].astype(str)
#
# # Plot
# plt.figure(figsize=(70, 10))
# plt.bar(x_label, table['battery_capacity_kWh'])
# plt.xticks(rotation=90)
# plt.xlabel("Model")
# plt.ylabel("Battery Capacity (kWh)")
# plt.title("Battery Capacity per EV Model")
# plt.tight_layout()
# plt.show()


#menampilkan 5 data yang paling besar
# # Baca file
# table = pd.read_csv("C:/Users/Pongo/Documents/csv/electric_vehicles_spec_2025.csv.csv")
#
# # Bersihkan data yang hilang
# table = table.dropna(subset=['model', 'battery_capacity_kWh'])
#
# # Ambil 5 data dengan kapasitas baterai terbesar
# top5 = table.nlargest(5, 'battery_capacity_kWh')
#
# # Konversi model ke string
# x_label = top5['model'].astype(str)
#
# # Plot
# plt.figure(figsize=(10, 6))
# plt.bar(x_label, top5['battery_capacity_kWh'])
# plt.xticks(rotation=45)
# plt.xlabel("Model")
# plt.ylabel("Battery Capacity (kWh)")
# plt.title("Top 5 EV Models by Battery Capacity")
# plt.tight_layout()
# plt.show()


#menampilkan 5 data yang paling kecil
# # Baca file
# table = pd.read_csv("C:/Users/Pongo/Documents/csv/electric_vehicles_spec_2025.csv.csv")
#
# # Bersihkan data yang hilang
# table = table.dropna(subset=['model', 'battery_capacity_kWh'])
#
# # Ambil 5 data dengan kapasitas baterai terkecil
# bottom5 = table.nsmallest(5, 'battery_capacity_kWh')
#
# # Konversi model ke string
# x_label = bottom5['model'].astype(str)
#
# # Plot
# plt.figure(figsize=(10, 6))
# plt.bar(x_label, bottom5['battery_capacity_kWh'])
# plt.xticks(rotation=45)
# plt.xlabel("Model")
# plt.ylabel("Battery Capacity (kWh)")
# plt.title("Bottom 5 EV Models by Battery Capacity")
# plt.tight_layout()
# plt.show()