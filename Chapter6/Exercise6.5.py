numList = []


def even_int(numbers):
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens


def main():
    value = int(input("Insert a number: "))
    if value > 0:
        numList.append(value)
        main()
    else:
        print("The list you inserted is:", numList, '\n' +
              f"The list without the uneven numbers is: {even_int(numList)}")
        quit()


main()
