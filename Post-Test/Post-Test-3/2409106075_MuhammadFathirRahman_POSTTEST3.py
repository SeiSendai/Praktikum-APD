BeratBadan = float(input("Masukkan Berat Badan Anda (Jujur Ya Bang): "))
TinggiBadan = float(input("Masukkan Tinggi Badan Anda (Jujur loh ya): "))
TinggiBadan = TinggiBadan / 100
BodyMassIndex = BeratBadan / (TinggiBadan * TinggiBadan)

if BodyMassIndex < 18.5:
    print("Maaf Bang Berat Badanmu kurang (Underweight)")
elif BodyMassIndex < 24.9:
    print("Kamu Normal Bang, Tidak kelebihan atau kekurangan berat badan")
elif BodyMassIndex < 29.9:
    print("Berat Badanmu Berlebih (Overweight)")
else:
    print("Maaf kamu obesitas")