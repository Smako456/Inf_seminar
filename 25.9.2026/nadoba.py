import random
objem = int(input("Kapacita nádržev l: "))
stav=0
den=0
while stav<objem:
    a=random.randint(0,objem)
    den = den+1
    print(f"Deň {den}: pribudlo {a} litrov")
    stav= stav + a
    print(f"V nádrži: {stav} litrov")

if stav>=objem:
    print("Nádrž je plná.")
    print(f"Trvalo to {den} dní.")