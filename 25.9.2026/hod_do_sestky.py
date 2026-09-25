import random
hod = 0 
a=0
while hod<6:
    hod=random.randint(1,6)
    print(f"hod: {hod}")
    a=a+1

if hod==6:
    print(f"Šestka padla na {a} hod.")
