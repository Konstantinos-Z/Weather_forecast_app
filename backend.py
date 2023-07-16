import requests

API_KEY = "b3ba508d8c0eb0cb86d9881b30747e5d"


def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days    # 8 observations per day
    filtered_data = filtered_data[:nr_values]   # get data up to the user-designated day
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3))
