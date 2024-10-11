# daftar_buku = {
# "Buku1" : "Harry Potter",
# "Buku2" : "Percy Jackson",
# "Buku3" : "Twillight"
# }
# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku["Buku3"])

# daftar_buku = {}

# daftar_buku["Novel 1"] = "senyum pertama di pagi hari Airin"
# daftar_buku[1] = "Matahari"
# print (daftar_buku)

# daftar_buku = dict(Buku1 = "Harry Potter", Buku2 = "Percy Jackson")
# print(daftar_buku)

# print(daftar_buku["Buku2"])
# print(daftar_buku.get("Buku2"))

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }

# # for i in Nilai:
# #     print(i)

# for i, j in Nilai.items():
#     print(f"nilai diri {i} itu valuenya adalah : {j}")

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }

# Nilai["Struktur Data"] = 99
# Nilai["Matematika"] = 69

# Nilai.update({"Struktur data" : 99})
# Nilai.update({"Matematika" : 69})
# print(Nilai)

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }

# print(Nilai+"\n\n")

# trashbin = Nilai.pop("Mstematika")

# print(Nilai+"\n\n")
# print(type(trashbin))

# print(f"JUmlah elemen dari variabel dict nilai adalah {len(Nilai)}")

# daftar_nilai = Nilai.copy()
# print(daftar_nilai)

# import os
# import datetime as dt

# os.system("cls")
# key = "motor", "mobil", "sepeda"
# value = 2
# daftar_kendaraan = dict.fromkey(key, value)

# print(daftar_kendaraan)

# Musik = {
# "The Chainsmoker" : ["All we Know", "The Paris"],
# "Alan Walker" : ["Alone", "Lily"],
# "Neffex" : ["Best of Me", "Memories"]
# }

# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
#     for song in j:
#         print(song)
#         print("")

mahasiswa = {
101 : {"Nama" : "Aldy", "Umur" : 19},
111 : {"Nama" : "Abdul", "Umur" : 18, "Hobi" : ["Membaca", "menulis", "ngoding"]}
}

for key, value in mahasiswa.items():
    print("ID Mahasiswa : ", key)
    # for key_a, value_a in value.items():
    #     print (key_a, " : ", value_a)
    #     print("")
print(mahasiswa[111]["Hobi"][2])