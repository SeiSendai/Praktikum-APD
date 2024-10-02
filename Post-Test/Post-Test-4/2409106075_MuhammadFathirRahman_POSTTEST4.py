NamaUser = "Fathir"
Nim = "75"
salah = 0
maksimalsalah = 3

while salah <3:
    Username = input("Masukkan Username Anda: ")
    Password = input("Masukkan Password Anda: ")
    if Username == NamaUser and Password == Nim:
        print("Anda telah berhasil login")
        break
    else:
        salah+=1
        print(f"Login anda gagal, anda salah {salah}")