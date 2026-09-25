dni = int(input("Počet dní: "))

celkom=0

for i in range(1,dni+1):
    trzba=float(input(f"Tržba za deň {i}: "))
    celkom += trzba

print(f"{celkom}")
priemer = celkom/dni
print(f"{priemer}")