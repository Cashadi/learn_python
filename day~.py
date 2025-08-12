# tagihan = [50000, 75000, 125000, 300000, 200000]
#
# # Tanpa menggunakan while loop
# total_tagihan = tagihan[0] + tagihan[1] + tagihan[2] + tagihan[3] + tagihan[4]
# print(total_tagihan)
#
# # Dengan menggunakan while loop
# i = 0
# jumlah_tagihan = len(tagihan)
# total_tagihan = 0
# while i < jumlah_tagihan:
#     total_tagihan += tagihan[i]
#     i += 1
# print(total_tagihan)

#python loops break
# tagihan = [50000, 75000, -150000, 125000, 300000, -50000, 200000]
# i = 0
# jumlah_tagihan = len(tagihan)
# total_tagihan = 0
# while i < jumlah_tagihan:
#     # jika terdapat tagihan ke-i yang bernilai minus (di bawah nol),
#     # pengulangan akan dihentikan
#     if tagihan[i] < 0:
#         total_tagihan = -1
#         print("terdapat angka minus dalam tagihan, perhitungan dihentikan!")
#         break
#     total_tagihan += tagihan[i]
#     i += 1
# print(total_tagihan)


#for loops part 1
# list_tagihan = [50000, 75000, -150000, 125000, 300000, -50000, 200000]
# total_tagihan = 0
# for tagihan in list_tagihan:
#     total_tagihan += tagihan
# print(total_tagihan)


#nested loops
# list_daerah = ['Malang', 'Palembang', 'Medan']
# list_buah = ['Apel', 'Duku', 'Jeruk']
# for nama_daerah in list_daerah:
#     for nama_buah in list_buah:
#         print(nama_buah+" "+nama_daerah)


#praktek
list_cash_flow = [
2500000, 5000000, -1000000, -2500000, 5000000, 10000000,
-5000000, 7500000, 10000000, -1500000, 25000000, -2500000
]
total_pengeluaran, total_pemasukan = 0, 0
for dana in list_cash_flow:
    if dana > 0:
        total_pemasukan += dana
    else:
        total_pengeluaran += dana
total_pengeluaran *= -1
print(total_pengeluaran)
print(total_pemasukan)