import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',
    database='flight_game',
    user='dbuser',
    password='1234',
)


def get_airports():
    code = str(input("Insert the area code of a country: ")).upper()
    cursor = connection.cursor(buffered=True)
    cursor.execute("SELECT name, type FROM airport where iso_country='" + code + "' order by type desc")
    result = cursor.fetchall()

    if cursor.rowcount != 0:
        print("List of all airports in the country you selected: ")
        for row in result:
            print(row[0] + ", type:", row[1])
    else:
        print("Invalid area code!")


def main():
    print("\n1. Get airports in a country;\n"
          "2. Quit the program.\n")

    match int(input("Select an option: ")):
        case 1:
            get_airports()
        case 2:
            quit()
        case _:
            print("Invalid option!")

    main()


main()
