import random


def dice_roll():
    return random.randint(1, 6)


def main():
    num = dice_roll()
    print(f"The result is {num}.")
    if num == 6:
        exit()
    else:
        main()


main()
