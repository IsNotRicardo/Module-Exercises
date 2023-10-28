cabinClass = str(input("Insert your cabin class: ")).upper()

if cabinClass == 'LUX':
    print("LUX: upper-deck cabin with a balcony.")
elif cabinClass == 'A':
    print("A: above the car deck, equipped with a window.")
elif cabinClass == 'B':
    print("B: windowless cabin above the car deck.")
elif cabinClass == 'C':
    print("C: windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")
