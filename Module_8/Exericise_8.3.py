import mysql.connector
from geopy.distance import geodesic

connection = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',
    database='flight_game',
    user='dbuser',
    password='1234',
)


def get_airport_distance():
    code, cursor = list(range(2)), list(range(2))
    coords = list([[] * 2] * 2)

    for i in range(2):
        code[i] = str(input(f"Insert the ICAO code of airport {i + 1}: ")).upper()
        cursor[i] = connection.cursor(buffered=True)
        cursor[i].execute("SELECT latitude_deg, longitude_deg FROM airport where ident='" + code[i] + "'")
        result = cursor[i].fetchall()

        if cursor[i].rowcount != 0:
            for row in result:
                coords[i] = row[0], row[1]
        else:
            print("Airport code not in our system!")
            break

    print(f"The distance between your airports is: {geodesic(coords[0], coords[1]).km:.2f} km.")


def main():
    print("\n1. Get distance between airports;\n"
          "2. Quit the program.\n")

    match int(input("Select an option: ")):
        case 1:
            get_airport_distance()
        case 2:
            quit()
        case _:
            print("Invalid option!")

    main()


main()
