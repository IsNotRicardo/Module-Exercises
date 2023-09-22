import math

integers = list(range(3))

for i in integers:
    integers[i] = int(input(f"Integer {i + 1}: "))

print("The sum of the numbers is:", sum(integers), '\n' +
      "The product of the numbers is:", math.prod(integers), '\n' +
      "The average of the numbers is:", round(sum(integers) / 3, 2))
