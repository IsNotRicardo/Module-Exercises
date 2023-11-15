import requests

try:
    response = requests.get("https://api.chucknorris.io/jokes/random")
    print('\n' + response.json()['value'])

except requests.exceptions.RequestException:
    print("Request cannot be performed")
