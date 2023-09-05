numbers = []
value = input("Insert a number: ")

while value != ' ':
    try:
        value = int(value)
        numbers.append(value)
    except ValueError:
        print("Not a number.")
    value = input("Insert a number: ")

numbers.sort(reverse=True)
x = slice(5)
print("The five greatest numbers are:", numbers[x])