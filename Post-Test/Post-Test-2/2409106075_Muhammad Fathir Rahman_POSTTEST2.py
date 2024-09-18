Nama = input("Beli Apa Bang: ")
Harga = float(input("Berapaan Harganya: RP."))
Jumlah = int(input("Beli Berapa: "))
Diskon = float(input("Diskon Berapa Persen Bang: "))

Total_Harga_Sebelum_Diskon = Jumlah * Harga
Total_Diskon =(Diskon/100) * Total_Harga_Sebelum_Diskon
Total_Yang_Harus_Dibayar = Total_Harga_Sebelum_Diskon - Total_Diskon
Sisa = int(Diskon) % 3

print(f"Kamu Telah Membeli {Jumlah} {Nama} Yang dimana harga satuannya adalah RP.{Harga}, Total Harga adalah RP.{Total_Harga_Sebelum_Diskon} yang dimana kamu mendapatkan potongan sebesar RP.{Total_Diskon}, Harga yang perlu kamu bayar adalah RP.{Total_Yang_Harus_Dibayar}.")
print(f"{Diskon} dibagi dengan 3 sisanya menjadi {Sisa}.")