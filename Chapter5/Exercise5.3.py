number = int(input("Insert a number: "))

for i in range(2, number):
    if number % i == 0:
        print("The number is not prime.")
        exit()

if number <= 0 or number == 1:
    print("The number is not prime.")
else:
    print("The number is prime.")