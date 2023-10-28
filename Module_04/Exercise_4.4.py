import random

compNumber = random.randint(1, 10)
number = int(input("Insert a number: "))

while number != compNumber:
    if number < compNumber:
        print("Too low")
    else:
        print("Too high")
    number = int(input("Insert a number: "))

print("Correct!")
