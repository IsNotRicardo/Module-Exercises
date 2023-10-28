def conversion(gas):
    return gas * 3.78541


def main():
    gasoline = float(input("Insert the quantity of gasoline in American gallons: "))
    if gasoline < 0:
        exit()
    else:
        print(f"The quantity of gasoline is: {conversion(gasoline):.2f} liters.")
        main()


main()
