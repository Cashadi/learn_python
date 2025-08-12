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
tagihan = [50000, 75000, -150000, 125000, 300000, -50000, 200000]
i = 0
jumlah_tagihan = len(tagihan)
total_tagihan = 0
while i < jumlah_tagihan:
    # jika terdapat tagihan ke-i yang bernilai minus (di bawah nol),
    # pengulangan akan dihentikan
    if tagihan[i] < 0:
        total_tagihan = -1
        print("terdapat angka minus dalam tagihan, perhitungan dihentikan!")
        break
    total_tagihan += tagihan[i]
    i += 1
print(total_tagihan)