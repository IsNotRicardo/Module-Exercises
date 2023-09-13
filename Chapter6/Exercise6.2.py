import random


def dice_roll():
    return random.randint(1, faces)


def main():
    num = dice_roll()
    print(f"The result is {num}.")
    if num == faces:
        exit()
    else:
        main()


faces = int(input("Insert the maximum amount of faces in the dice: "))
main()
