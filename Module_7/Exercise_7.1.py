seasons = ('spring', 'summer', 'autumn', 'winter')

month = int(input("Insert the number of a month: "))
match month:
    case 3 | 4 | 5:
        print("The season is:", seasons[0])
    case 6 | 7 | 8:
        print("The season is:", seasons[1])
    case 9 | 10 | 11:
        print("The season is:", seasons[2])
    case 12 | 1 | 2:
        print("The season is:", seasons[3])
    case _:
        print("Invalid month!")
