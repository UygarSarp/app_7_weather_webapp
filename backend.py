import requests

API_KEY = "53a42dee4a590f51c59451f427ffbdf3"


def get_data(place, days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    filtered_data = filtered_data[:days*8]
    return filtered_data


if __name__ == "__main__":
    a = get_data("Tokyo", 3)
    print(get_data(place="Tokyo", days=3))
    print(a)
