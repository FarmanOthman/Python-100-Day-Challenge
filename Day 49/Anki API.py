import requests

# AnkiConnect URL
ANKI_CONNECT_URL = "http://localhost:8765"

def check_anki_connect():
    """Check if AnkiConnect is running."""
    payload = {
        "action": "requestPermission",
        "version": 6
    }
    try:
        response = requests.post(ANKI_CONNECT_URL, json=payload)
        response.raise_for_status()
        if response.json().get("result") is not None:
            print("AnkiConnect is running.")
            return True
    except requests.exceptions.RequestException as e:
        print("Error: Unable to connect to AnkiConnect.", e)
    return False

def check_deck_exists(deck_name):
    """Check if a specific deck exists in Anki."""
    payload = {
        "action": "deckNames",
        "version": 6
    }
    try:
        response = requests.post(ANKI_CONNECT_URL, json=payload)
        response.raise_for_status()
        deck_names = response.json().get("result", [])
        return deck_name in deck_names
    except requests.exceptions.RequestException as e:
        print("Error checking deck existence:", e)
        return False

def check_model_exists(model_name):
    """Check if a specific model exists in Anki."""
    payload = {
        "action": "modelNames",
        "version": 6
    }
    try:
        response = requests.post(ANKI_CONNECT_URL, json=payload)
        response.raise_for_status()
        model_names = response.json().get("result", [])
        return model_name in model_names
    except requests.exceptions.RequestException as e:
        print("Error checking model existence:", e)
        return False

def add_notes(deck_name, model_name, notes):
    """Add multiple notes to Anki."""
    payload = {
        "action": "addNotes",
        "version": 6,
        "params": {
            "notes": [
                {
                    "deckName": deck_name,
                    "modelName": model_name,
                    "fields": note["fields"],
                    "tags": note.get("tags", [])
                }
                for note in notes
            ]
        }
    }
    try:
        response = requests.post(ANKI_CONNECT_URL, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error adding notes to Anki:", e)
        return None

flashcards = [
  {
    "front": "What is a frequency distribution?",
    "back": "A frequency distribution is a way to organize raw data in table form, using classes and their corresponding frequencies."
  },
  {
    "front": "What are the types of frequency distributions?",
    "back": "1. Categorical frequency distribution\n2. Ungrouped frequency distribution\n3. Grouped frequency distribution"
  },
  {
    "front": "What is a categorical frequency distribution?",
    "back": "A categorical frequency distribution is used for data that can be placed in specific categories (nominal or ordinal). Examples include political affiliation, religious affiliation, and blood type."
  },
  {
    "front": "How is relative frequency calculated?",
    "back": "Relative frequency (Rf) is calculated as:\nRf = f / n\nwhere f is the frequency of the class and n is the total number of observations."
  },
  {
    "front": "How is percentage frequency calculated?",
    "back": "Percentage frequency (P) is calculated as:\nP = (f / n) * 100\nwhere f is the class frequency and n is the total number of observations."
  },
  {
    "front": "What is an ungrouped frequency distribution?",
    "back": "An ungrouped frequency distribution is used when the range of data is small. Each individual value is treated as a class."
  },
  {
    "front": "What are class limits and class boundaries?",
    "back": "Class limits define the smallest and largest values in a class. Class boundaries are used to avoid gaps between classes.\nLower boundary = Lower limit - 0.5\nUpper boundary = Upper limit + 0.5"
  },
  {
    "front": "What is a grouped frequency distribution?",
    "back": "A grouped frequency distribution is used when the range of values is large. Data is divided into classes that are more than one unit in width."
  },
  {
    "front": "What is the procedure for constructing a grouped frequency distribution?",
    "back": "1. Determine the highest and lowest value.\n2. Find the range.\n3. Select the number of classes.\n4. Calculate class width (range / number of classes).\n5. Assign class limits.\n6. Find class boundaries.\n7. Tally the data.\n8. Compute frequencies."
  },
  {
    "front": "How do you determine the number of classes in a grouped frequency distribution?",
    "back": "You can use one of the following formulas:\n1. Yule method: Number of classes = 2.5 * (4th root of n)\n2. Sturges method: Number of classes = 1 + (3.332 * log(n))"
  },
  {
    "front": "What is class width and how can it be calculated?",
    "back": "Class width is the difference between consecutive class limits or boundaries.\nMethods to calculate class width:\n1. Upper class limit - Lower class limit + 1\n2. Upper boundary - Lower boundary\n3. Lower limit of 2nd class - Lower limit of 1st class\n4. Midpoint of 2nd class - Midpoint of 1st class"
  },
  {
    "front": "What is the class midpoint and how is it calculated?",
    "back": "The class midpoint (Xm) is the average of the lower and upper class limits.\nXm = (Lower Limit + Upper Limit) / 2"
  },
  {
    "front": "What is cumulative frequency and its types?",
    "back": "Cumulative frequency represents the running total of frequencies.\n1. Less than cumulative frequency - Sum of frequencies up to a given class.\n2. More than cumulative frequency - Total observations minus the cumulative count from previous classes."
  }
]


# Convert the Flashcards into notes
notes = [
    {
        "fields": {
            "Front": item["front"],
            "Back": item["back"]
        },
        "tags": ["mongodb", "flashcards"]
    }
    for item in flashcards
]

# Check if AnkiConnect is running and prerequisites are met
if check_anki_connect():
    deck_name = "Static"
    model_name = "Basic"

    if not check_deck_exists(deck_name):
        print(f"Error: Deck '{deck_name}' does not exist. Please create it in Anki.")
    elif not check_model_exists(model_name):
        print(f"Error: Model '{model_name}' does not exist. Please create it in Anki.")
    else:
        result = add_notes(deck_name, model_name, notes)
        print(result)
else:
    print("Please ensure Anki and AnkiConnect are running.")
