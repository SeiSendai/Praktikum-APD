import os 

os.system('cls')

# Convert the list of dictionaries to a dictionary
list_Patch = [{'Patch':'1.0','Char':'Trailblazer'},{'Patch':'1.0','Char':'Trailblazer(Fire)'},{'Patch':'1.0','Char':'Bailu'},{'Patch':'1.0','Char':'Yanqing'},{'Patch':'1.0','Char':'Clara'},
              {'Patch':'1.0','Char':'Gepard'},{'Patch':'1.0','Char':'Bronya'},{'Patch':'1.0','Char':'Welt'},{'Patch':'1.0','Char':'Himeko'},{'Patch':'1.0','Char':'Seele'},
              {'Patch':'1.0','Char':'Jing Yuan'},{'Patch':'1.1','Char':'Silver Wolf'},{'Patch':'1.1','Char':'Luocha'},{'Patch':'1.2','Char':'Blade'},{'Patch':'1.2','Char':'Kafka'},
              {'Patch':'1.3','Char':'Dan Heng:Imbibitor Lunae'},{'Patch':'1.3','Char':'Fuxuan'},{'Patch':'1.4','Char':'Jingliu'},{'Patch':'1.4','Char':'Topaz & Numby'},
              {'Patch':'1.5','Char':'Huohuo'},{'Patch':'1.5','Char':'Argenti'},{'Patch':'1.6','Char':'Ruan Mei'},{'Patch':'1.6','Char':'Dr.Ratio'},
              {'Patch':'2.0','Char':'Black Swan'},{'Patch':'2.0','Char':'Sparkle'},{'Patch':'2.1','Char':'Acheron'},{'Patch':'2.1','Char':'Aventurine'},{'Patch':'2.2','Char':'Trailblazer(Imaginary)'},{'Patch':'2.2','Char':'Robin'},
              {'Patch':'2.2','Char':'Boothill'},{'Patch':'2.3','Char':'Firefly'},{'Patch':'2.3','Char':'Jade'},{'Patch':'2.4','Char':'Yunli'},{'Patch':'2.4','Char':'Jiaoqiu'},
              {'Patch':'2.5','Char':'Feixiao'},{'Patch':'2.5','Char':'Lingsha'}]

patch_dict = {}
for item in list_Patch:
    patch = item['Patch']
    char = item['Char']
    if patch not in patch_dict:
        patch_dict[patch] = []
    patch_dict[patch].append(char)

print(patch_dict)

user = "Fathir"
Pass = "Astral"
salah = 0
while salah < 3:
    os.system('cls')
    print("="*40)
    print("selamat datang di Astral Express".center(40))
    print("="*40)
    username = input("Masukkan username: ")
    pasword = input("Masukkan Password: ")
    if user == username and Pass == pasword:
        input(f"selamat anda berhasil masuk ke Astral Express, anda dikenali sebagai {user} silahkan tekan enter untuk lanjut")
        break
    else:
        salah += 1
        print(f"Gagal {salah} kali")

if salah == 3:
    print(f"kamu gagal login sebanyak {salah} kali maka kamu tidak bisa login lagi")
else:   
    while True:
        os.system('cls')
        print("="*40)
        print("selamat datang Nameless".center(40))
        print("="*40)
        print("1 Lihat Patch")
        print("2 Tambah Patch")
        print("3 Edit Patch")
        print("4 Hapus Patch")
        print("5 log out")
        menu = input("\nMasukkan pilihan: ")

        if menu == "1":
            os.system('cls')
            print("="*40)
            print("Daftar Patch".center(40))
            print("="*40)
            for patch, chars in patch_dict.items():
                print(f"{patch}: {', '.join(chars)}")
            input("\n silahkan tekan enter Nameless")

        elif menu == "2":
            os.system('cls')
            print("="*40)
            print("Tambah Patch".center(40))
            print("="*40)
            patch_baru = input("silahkan masukkan Patch baru:")
            Char_baru = input("silahkan masukkan Char baru:")
            if patch_baru in patch_dict:
                patch_dict[patch_baru].append(Char_baru)
            else:
                patch_dict[patch_baru] = [Char_baru]
            print("\npatch baru berhasil di tambah")
            input("\nsilahkan tekan enter Nameless")

        elif menu == "3":
            os.system('cls')
            print("="*40)
            print("Perbarui Patch".center(40))
            print("="*40)
            for patch, Char in patch_dict.items():
                print(f"{patch}: {', '.join(Char)}")        
            patch_to_edit = input("silahkan masukkan Patch yang mau diubah Nameless: ")
            if patch_to_edit in patch_dict:
                Char = input("Char baru: ")
                patch_dict[patch_to_edit].append(Char)
                print("\nPatch berhasil di ubah")
                input("\nsilahkan tekan enter Nameless")
            else:
                print("patch tidak ada Nameless")
                input("\nsilahkan tekan enter Nameless")

        elif menu == "4":
            os.system('cls')
            print("="*40)
            print("Hapus Patch".center(40))
            print("="*40)

            for patch, chars in patch_dict.items():
                print(f"{patch}: {', '.join(chars)}")
            patch_to_delete = input("silahkan masukkan Patch yang mau dihapus Nameless: ")

            if patch_to_delete in patch_dict:
                del patch_dict[patch_to_delete]
                print("\nPatch berhasil dihapus")
                input("\nsilahkan tekan enter Nameless")
            else:
                print("patch tidak ada Nameless")
                input("\nsilahkan tekan enter Nameless")

        elif menu == "5":
            os.system('cls')
            print("anda telah log out dari Astral Express")
            break
        
        else:
            os.system('cls')
            print("="*40)
            print("anomali".center(40))
            print("="*40)
            print("tidak ada menu ini Nameless silahkan kembali")
            input("\nsilahkan tekan enter Nameless")
