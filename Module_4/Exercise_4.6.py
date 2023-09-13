import random

number = int(input("Insert a large number of points: "))
squarePoints = list(range(2))
circlePoints = int()

for i in range(0, number):
    squarePoints = [random.uniform(-1, 1), random.uniform(-1, 1)]

    if (squarePoints[0] ** 2 + squarePoints[1] ** 2) < 1:
        circlePoints += 1

print("The approximate value of pi is:", 4 * circlePoints / number)