import requests
params = {
    "amount": 20,
    "type": "boolean"
}
data = requests.get("https://opentdb.com/api.php", params=params).json()

data = (data["results"])