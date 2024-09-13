import requests

API_KEY = "855adad9fd6d65ac8b937a53bfedf4e7"


def get_data(place, days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if (int(data["cod"])) == 200:
        filtered_data = data["list"]
        nr_days = 8 * days
        filtered_data = filtered_data[:nr_days]
    else:
        filtered_data = data["message"]

    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Surat", days=3))
