import requests

api_key = "cddaa9d249ebec7a6a4e2871202118e0"


def get_weather():
    location = str(input("\nInsert a municipality: "))
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric").json()

    print(response)
    weather, temp = response['weather'][0], response['main']
    print(f"\nLocation: {response['name']}, {response['sys']['country']}\n"
          f"Weather: {weather['main']}, {weather['description']}\n"
          f"Current temperature: {temp['temp']}ºC\n"
          f"Temperature range: {temp['temp_min']}ºC — {temp['temp_max']}ºC")


get_weather()
