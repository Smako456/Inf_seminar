eur = float(input("Koľko eur odložíš každý mesiac? "))
mesiac = int(input("Koľko mesiacov budeš sporiť? "))

for i in range(0,mesiac):
    print (f"Po {i+1} mesiaci: {eur*(i+1)}€")

print(f"Nasporené spolu: {eur*mesiac}€")