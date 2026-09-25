import random
b=["Jano", "Peto", "Stevo", "Juro"]

# float between 1 and 10
a=random.uniform(1,10)
print(f"{a}")

# one random element
c=random.choice(b)
print(f"{c}")

# k picks WITH replacement (repeats possible)
d=random.choices(b, k=2)
print(f"{d}")

# 2 picks WITHOUT replacement (no repeats)
e=random.sample(b, k=2)
print(f"{e}")

# shuffles the list in place, returns None
f=random.shuffle(b)
print(f"{b}")

# k picks WITH replacement (repeats possible)
g=random.choices(["win", "lose"], weights=[9,1], k=10)
print(f"{g}")