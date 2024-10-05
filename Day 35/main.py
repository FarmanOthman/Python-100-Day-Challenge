import requests

paramts = {
  "lat": 36.00183730062074,
  "lon": 44.037324151492456,
  "appid": "....",
  "cnt": 4
}

import requests

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=paramts)


if response.status_code == 200:
  data = response.json()
  # Print the weather main description for the first time point in the forecast
  print(data["list"][0]["weather"][0]["main"])
else:
  print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")

