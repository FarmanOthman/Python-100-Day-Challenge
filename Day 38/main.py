import requests
import datetime as dt
import os
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Fetch environment variables
APP_API = os.getenv("APP_API")
API_KEY = os.getenv("API_KEY")
API_ENDPOINT = os.getenv("API_ENDPOINT")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SHEETY_AUTH = os.getenv("SHEETY_AUTH")

# Check if all necessary environment variables are set
if not all([APP_API, API_KEY, API_ENDPOINT, SHEETY_ENDPOINT, SHEETY_AUTH]):
  raise EnvironmentError("One or more required environment variables are missing. Please check your .env file or environment settings.")

# Headers
headers = {
  "x-app-id": APP_API,
  "x-app-key": API_KEY,
  "Content-Type": "application/json"
}
sheety_headers = {
  "Authorization": SHEETY_AUTH
}

# Function to call Nutritionix API
def fetch_exercise_data(query, gender="male", weight_kg=58, height_cm=180, age=20):
  params = {
    "query": query,
    "gender": gender,
    "weight_kg": weight_kg,
    "height_cm": height_cm,
    "age": age
  }
  
  try:
    response = requests.post(url=API_ENDPOINT, json=params, headers=headers)
    response.raise_for_status()  # Raises an error for bad responses (4xx or 5xx)
    return response.json()
  except requests.exceptions.RequestException as e:
    print(f"Error fetching exercise data: {e}")
    return None

# Function to log workout data to Sheety
def log_to_sheety(exercise_data):
  for exercise in exercise_data["exercises"]:
    workout_entry = {
      "workout": {
        "date": dt.datetime.now().strftime("%Y-%m-%d"),
        "time": dt.datetime.now().strftime("%H:%M:%S"),
        "exercise": exercise['name'].title(),
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"]
      }
    }
    
    try:
      sheety_response = requests.post(url=SHEETY_ENDPOINT, json=workout_entry, headers=sheety_headers)
      sheety_response.raise_for_status()
      print(f"Logged exercise: {exercise['name'].title()} to Sheety.")
    except requests.exceptions.RequestException as e:
      print(f"Error logging to Sheety: {e}")

# Main execution flow
def main():
  user_input = input("Tell me which exercises you did: ")
  
  # Fetch exercise data from Nutritionix API
  exercise_data = fetch_exercise_data(query=user_input)
  
  if exercise_data:
    print("Exercise data received:")
    log_to_sheety(exercise_data)
  else:
    print("No data to log. Something went wrong.")

if __name__ == "__main__":
  main()
