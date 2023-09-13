import math


def unit_price(length, cost):
    """Issue: The function is inverting the parameters"""
    """prints are for debugging"""
    print(length / 100)
    print(20 / (math.pi * (35 / 200) ** 2))
    print(cost / (math.pi * (length / 200) ** 2))
    return cost / (math.pi * (length / 200) ** 2)


def main():
    diameter = price = value = list(range(2))

    for i in range(2):
        diameter[i] = float(input(f"Insert the diameter of pizza Nº{i + 1} (cm): "))
        price[i] = float(input(f"Insert the price of pizza Nº{i + 1} (€): "))
        value[i] = unit_price(length=diameter[i], cost=price[i])

    print(f"The pizza with the best value is: Nº{value.index(min(value)) + 1}, costing {min(value):.2f} €/m2\n"
          f"The other pizza is: Nº{value.index(max(value)) + 1}, costing {max(value):.2f} €/m2")


main()
