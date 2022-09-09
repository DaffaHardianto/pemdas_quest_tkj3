# Balok

print("\n1.volume balok")
panjang = int(input("masukan nilai panjang"))
lebar = int(input("masukan nilai lebar"))
tinggi = int(input("masukan nilai tinggi"))
volume_b = panjang * lebar * tinggi

print("volume balok adalah", volume_b)

# Kubus

print("\n2.volume kubus")
sisi = int(input("masukan nilai sisi"))
volume_k = sisi * sisi * sisi

print("volume kubus adalah", volume_k)

# Limas

print("\n3.volume limas")
sisi = int(input("masukan nilai sisi"))
tinggi = int(input("masukan nilai tinggi"))
volume_l= (1/3) * (sisi*sisi) * tinggi

print("volume limas adalah", volume_l)

# Tabung

print("\n4.volume tabung")
r = int(input("masukan nilai r"))
t = int(input("masukan nilai t"))
volume_t = 22/7 * r * r * t

print("volume tabung adalah", volume_t)

# Celcius ke Reamur

print("\n5.celcius ke reamur")
c = int(input("masukan nilai celcius"))
reamur = 4/5 * c

print("celcius ke reamur adalah", reamur)
