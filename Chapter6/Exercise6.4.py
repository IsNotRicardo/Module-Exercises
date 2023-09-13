numList = []


def sum_int(nums):
    return sum(nums)


def main():
    value = int(input("Insert a number: "))
    if value > 0:
        numList.append(value)
        main()
    else:
        print(f"The sum of the numbers is: {sum_int(numList)}")
        quit()


main()
