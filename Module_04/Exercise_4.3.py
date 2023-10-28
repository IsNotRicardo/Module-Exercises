numbers = []
value = input("Insert a number: ")

while value != ' ':
    try:
        value = int(value)
        numbers.append(value)
    except ValueError:
        print("Not a number.")
    value = input("Insert a number: ")

print("The smallest number is:", min(numbers), '\n' +
      "The largest number is:", max(numbers))
