airports = {}


def new_airport():
    code = str(input("Insert the ICAO code of the airport: "))
    if len(code) != 4:
        print("The ICAO code must contain 4 letters!")
    elif not code.isalpha():
        print("The ICAO code can only contain letters!")
    else:
        name = str(input("Insert the name of the airport: "))
        airports[code] = name


def fetch_airport():
    code = str(input("Insert the ICAO code of the airport: "))
    if code in airports:
        print("The airport is:", airports[code])
    else:
        print("Airport ICAO code is not in the system!")


def main():
    print("\n1. Add new airport to the system;\n"
          "2. Fetch airport data from the system;\n"
          "3. Exit the program.\n")

    match int(input("Select your option: ")):
        case 1:
            new_airport()
        case 2:
            fetch_airport()
        case 3:
            quit()
        case _:
            print("Invalid option!")

    main()


main()
