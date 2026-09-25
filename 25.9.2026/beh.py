dni=int(input("Počet tréningových dní: "))
spolu = 0

for i in range(1,dni+1):
    km=float(input(f"Kilometre v deň {i}:"))
    spolu+=km
    print(f"Doteraz spolu: {spolu}")

print(f"Celková vzdialenosť: {spolu}")