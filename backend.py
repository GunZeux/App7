import requests

API_KEY = "9ce1100d7269d9a4b8345ca9ec56835c"


def get_data(location, days=2, view="Temperature", mode=False):

    url = "https://api.openweathermap.org/data/2.5/" \
          f"forecast?q={location}&appid={API_KEY}"
    response = requests.get(url).json()
    # The data is present in the number of 3 hours hence 8 per day
    filtered_data = response["list"][:8*days]

    if view == "Temperature":
        final_data = [sub_val["main"]["temp"] for sub_val in filtered_data]
    else:
        final_data = [sub_val["weather"][0]["main"] for sub_val
                      in filtered_data]

    if mode:
        return final_data
    else:
        return filtered_data


if __name__ == "__main__":
    print(get_data("Tokyo", 2, "Sky"))