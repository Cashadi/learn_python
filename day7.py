#mapping type
# person = {'nama': 'John Doe', 'pekerjaan': 'Programmer'}
# print(person['nama'])
# print(person['pekerjaan'])

#praktek
# # Data yang dinyatakan ke dalam dictionary
# sepatu = {"nama": "Sepatu Niko", "harga": 150000, "diskon": 30000}
# baju = {"nama": "Baju Unikloh", "harga": 80000, "diskon": 8000}
# celana = {"nama": "Celana Lepis", "harga": 200000, "diskon": 60000}
# # Hitunglah harga masing-masing data setelah dikurangi diskon
# harga_sepatu = sepatu["harga"] - sepatu["diskon"]
# harga_baju = baju["harga"] - baju["diskon"]
# harga_celana = celana["harga"] - celana["diskon"]
# # Hitung harga total
# total_harga = harga_sepatu + harga_baju + harga_celana
# # Hitung harga kena pajak
# total_pajak = total_harga * 0.1
# # Cetak total_harga + total_pajak
# print(total_harga + total_pajak)


# #operator
# bil1 = 5
# bil2 = bil1 // 2
# hasil = bil1 <= bil2 or bil1 == 2
# print(hasil)

#tentang prioritas
# bilangan = (5 % 3 ** 2) + (3 + 2 * 2) * (4 - 2)
# print(bilangan)

#latiha
sepatu = { "nama" : "Sepatu Niko", "harga": 150000, "diskon": 30000 }
baju = { "nama" : "Baju Unikloh", "harga": 80000, "diskon": 8000 }
celana = { "nama" : "Celana Lepis", "harga": 200000, "diskon": 60000 }

harga_sepatu = sepatu["harga"] - sepatu["diskon"]
harga_baju = baju["harga"] - baju["diskon"]
harga_celana = celana["harga"] - celana["diskon"]

total_harga = (harga_sepatu + harga_baju + harga_celana) * 1.1

print(total_harga)
