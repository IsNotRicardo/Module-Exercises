import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)

connection = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',
    database='flight_game',
    user='dbuser',
    password='1234',
)


def fetch_airport(code):
    cursor = connection.cursor(buffered=True)
    cursor.execute("SELECT name, municipality FROM airport WHERE ident='" + code + "'")

    for row in cursor.fetchall():
        return row[0], row[1]


@app.route('/airport/<path:icao>')
def check_airport(icao):
    result = fetch_airport(icao)
    if result:
        return jsonify({"ICAO": icao, "Name": result[0], "Location": result[1]})
    else:
        return "That ICAO is not in our system!"


if __name__ == '__main__':
    app.run(debug=True)
