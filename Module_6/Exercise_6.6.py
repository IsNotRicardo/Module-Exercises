import math


def unit_price(length, cost):
    return cost / (math.pi * (length / 200) ** 2)


def main():
    diameter, price, value = list(range(2)), list(range(2)), list(range(2))

    for i in range(2):
        diameter[i] = float(input(f"\nInsert the diameter of pizza Nº{i + 1} (cm): "))
        price[i] = float(input(f"Insert the price of pizza Nº{i + 1} (€): "))
        value[i] = unit_price(diameter[i], price[i])

    print(f"\nThe pizza with the best value is: Nº{value.index(min(value)) + 1}, costing {min(value):.2f} €/m2\n"
          f"The other pizza is: Nº{value.index(max(value)) + 1}, costing {max(value):.2f} €/m2")


main()
