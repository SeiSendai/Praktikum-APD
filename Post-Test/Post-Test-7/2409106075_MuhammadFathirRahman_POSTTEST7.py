import os 

os.system('cls')

list_Patch = [{'Patch':'1.0','Char':'Trailblazer'},{'Patch':'1.0','Char':'Trailblazer(Fire)'},{'Patch':'1.0','Char':'Bailu'},{'Patch':'1.0','Char':'Yanqing'},{'Patch':'1.0','Char':'Clara'},
              {'Patch':'1.0','Char':'Gepard'},{'Patch':'1.0','Char':'Bronya'},{'Patch':'1.0','Char':'Welt'},{'Patch':'1.0','Char':'Himeko'},{'Patch':'1.0','Char':'Seele'},
              {'Patch':'1.0','Char':'Jing Yuan'},{'Patch':'1.1','Char':'Silver Wolf'},{'Patch':'1.1','Char':'Luocha'},{'Patch':'1.2','Char':'Blade'},{'Patch':'1.2','Char':'Kafka'},
              {'Patch':'1.3','Char':'Dan Heng:Imbibitor Lunae'},{'Patch':'1.3','Char':'Fuxuan'},{'Patch':'1.4','Char':'Jingliu'},{'Patch':'1.4','Char':'Topaz & Numby'},
              {'Patch':'1.5','Char':'Huohuo'},{'Patch':'1.5','Char':'Argenti'},{'Patch':'1.6','Char':'Ruan Mei'},{'Patch':'1.6','Char':'Dr.Ratio'},
              {'Patch':'2.0','Char':'Black Swan'},{'Patch':'2.0','Char':'Sparkle'},{'Patch':'2.1','Char':'Acheron'},{'Patch':'2.1','Char':'Aventurine'},{'Patch':'2.2','Char':'Trailblazer(Imaginary)'},{'Patch':'2.2','Char':'Robin'},
              {'Patch':'2.2','Char':'Boothill'},{'Patch':'2.3','Char':'Firefly'},{'Patch':'2.3','Char':'Jade'},{'Patch':'2.4','Char':'Yunli'},{'Patch':'2.4','Char':'Jiaoqiu'},
              {'Patch':'2.5','Char':'Feixiao'},{'Patch':'2.5','Char':'Lingsha'}]

patch_dict = {}
login_attempts = 0

def convert_list_to_dict():
    for item in list_Patch:
        patch = item['Patch']
        char = item['Char']
        if patch not in patch_dict:
            patch_dict[patch] = []
        patch_dict[patch].append(char)

def display_patch():
    os.system('cls')
    print("="*40)
    print("Daftar Patch".center(40))
    print("="*40)
    for patch, chars in patch_dict.items():
        print(f"{patch}: {', '.join(chars)}")
    input("\nSilahkan tekan enter Nameless")

def add_patch(patch_baru, char_baru):
    if patch_baru in patch_dict:
        patch_dict[patch_baru].append(char_baru)
    else:
        patch_dict[patch_baru] = [char_baru]
    print("\nPatch baru berhasil ditambahkan")
    input("\nSilahkan tekan enter Nameless")

def handle_login():
    global login_attempts
    user = "Fathir"
    password = "Astral"
    while login_attempts < 3:
        os.system('cls')
        print("="*40)
        print("Selamat datang di Astral Express".center(40))
        print("="*40)
        username = input("Masukkan username: ")
        pasword = input("Masukkan Password: ")
        if user == username and password == pasword:
            input(f"Selamat, anda berhasil masuk ke Astral Express, anda dikenali sebagai {user}. Silahkan tekan enter untuk lanjut")
            return True
        else:
            login_attempts += 1
            print(f"Gagal {login_attempts} kali")
    print(f"Kamu gagal login sebanyak {login_attempts} kali maka kamu tidak bisa login lagi")
    return False

def main():
    convert_list_to_dict()
    
    if not handle_login():
        return

    while True:
        os.system('cls')
        print("="*40)
        print("Selamat datang Nameless".center(40))
        print("="*40)
        print("1. Lihat Patch")
        print("2. Tambah Patch")
        print("3. Edit Patch")
        print("4. Hapus Patch")
        print("5. Log Out")
        menu = input("\nMasukkan pilihan: ")

        if menu == "1":
            display_patch()

        elif menu == "2":
            os.system('cls')
            print("="*40)
            print("Tambah Patch".center(40))
            print("="*40)
            patch_baru = input("Silahkan masukkan Patch baru: ")
            char_baru = input("Silahkan masukkan Char baru: ")
            add_patch(patch_baru, char_baru)

        elif menu == "3":
            os.system('cls')
            print("="*40)
            print("Perbarui Patch".center(40))
            print("="*40)
            for patch, chars in patch_dict.items():
                print(f"{patch}: {', '.join(chars)}")
            patch_to_edit = input("Silahkan masukkan Patch yang mau diubah Nameless: ")
            if patch_to_edit in patch_dict:
                char_baru = input("Char baru: ")
                patch_dict[patch_to_edit].append(char_baru)
                print("\nPatch berhasil diubah")
                input("\nSilahkan tekan enter Nameless")
            else:
                print("Patch tidak ada Nameless")
                input("\nSilahkan tekan enter Nameless")

        elif menu == "4":
            os.system('cls')
            print("="*40)
            print("Hapus Patch".center(40))
            print("="*40)
            for patch, chars in patch_dict.items():
                print(f"{patch}: {', '.join(chars)}")
            patch_to_delete = input("Silahkan masukkan Patch yang mau dihapus Nameless: ")
            if patch_to_delete in patch_dict:
                del patch_dict[patch_to_delete]
                print("\nPatch berhasil dihapus")
                input("\nSilahkan tekan enter Nameless")
            else:
                print("Patch tidak ada Nameless")
                input("\nSilahkan tekan enter Nameless")

        elif menu == "5":
            os.system('cls')
            print("Anda telah log out dari Astral Express")
            break
        
        else:
            os.system('cls')
            print("="*40)
            print("Anomali".center(40))
            print("="*40)
            print("Tidak ada menu ini Nameless, silahkan kembali")
            input("\nSilahkan tekan enter Nameless")

if __name__ == "__main__":
    main()
