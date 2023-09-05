import random

dice = int(input("How many dice do you want to roll? "))
sumDice = 0

for i in range(1, dice + 1):
    sumDice += random.randint(1, 6)

print("The sum of the values in the dice is:", sumDice)