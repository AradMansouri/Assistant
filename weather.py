import requests

def get_weather():
    city_name = input("Enter city's name: ").strip()

    url = f"https://wttr.in/{city_name}"
    response = requests.get(url)

    if response.status_code == 200:
        weather_info = response.text
        print(weather_info)
    else:
        print("Oh! Error!")

if __name__ == "__main__":
    get_weather()