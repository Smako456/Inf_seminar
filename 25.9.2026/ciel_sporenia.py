import math
ciel = float(input("Cieľová suma: "))
mesacne = int(input("Mesačne odložím: "))
a=0
mesiac=ciel/mesacne
zaokruhlene=math.ceil(mesiac)

for i in range(1,6):
    if a < ciel:
        a=i*mesacne
        print(f"Mesiac {i}: {a}")
    if a>= ciel:
        print(f"Cieľ dosiahnutý za {zaokruhlene} mesiacov.")
        