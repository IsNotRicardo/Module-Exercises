import random

code = list(range(7))

for i in code:
    if i < 3:
        code[i] = random.randint(0, 9)
    else:
        code[i] = random.randint(1, 6)

print("Your combinations of numbers are:", code)