import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',
    database='flight_game',
    user='dbuser',
    password='1234',
)


def fetch_airport():
    code = str(input("Insert the ICAO code of the airport: ")).upper()
    cursor = connection.cursor(buffered=True)
    cursor.execute("SELECT name, municipality FROM airport where ident='" + code + "'")
    result = cursor.fetchall()

    if cursor.rowcount != 0:
        for row in result:
            print(code + ':', row[0] + ", located in", row[1])
    else:
        print("Airport code not in our system!")


def main():
    print("\n1. Fetch an airport;\n"
          "2. Quit the program.\n")

    match int(input("Select an option: ")):
        case 1:
            fetch_airport()
        case 2:
            quit()
        case _:
            print("Invalid option!")

    main()


main()
