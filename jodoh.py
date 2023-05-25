import random

x = input("Nama Kamu ")
y = input("Nama Crush Kamu ")
Jodoh = ["Tidak Jodoh", "Jodoh"]
z = random.choice(Jodoh)
if z == "Tidak Jodoh":
    print("Maaf")
else:
    print("Selamat")
print(x + " dan " + y, z)