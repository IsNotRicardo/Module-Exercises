from flask import Flask, jsonify

app = Flask(__name__)


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False

    if n <= 0 or n == 1:
        return False
    else:
        return True


@app.route(f'/prime_number/<int:num>')
def check_num(num):
    return jsonify({"Number": num, "isPrime": is_prime(num)})


if __name__ == '__main__':
    app.run(debug=True)
