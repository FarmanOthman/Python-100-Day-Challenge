import random

print("Welcome to the Higher or Lower Game!")

the_option = [
  {"name": "Neymar", "followers": 250},
  {"name": "Messi", "followers": 317},
  {"name": "Ronaldo", "followers": 568},
  {"name": "Kane", "followers": 60}
]

def choose_players():
  player_1 = random.choice(the_option)
  player_2 = random.choice(the_option)
  while player_1 == player_2:
    player_2 = random.choice(the_option)
  return player_1, player_2

def higher_or_lower():
  score = 0
  while True:
    player_1, player_2 = choose_players()
    print("Who has more followers?")
    print(f"1: {player_1['name']} or 2: {player_2['name']}")

    while True:
      choice = input("Type 1 or 2: ")
      if choice in ["1", "2"]:
        break
      else:
        print("Invalid input. Please type 1 or 2.")

    if choice == "1" and player_1["followers"] > player_2["followers"]:
      print(f"Correct! {player_1['name']} has more followers.")
      score += 1
    elif choice == "2" and player_2["followers"] > player_1["followers"]:
      print(f"Correct! {player_2['name']} has more followers.")
      score += 1
    else:
      print("Wrong guess. Game over!")
      break

    print(f"Your current score: {score}\n")

higher_or_lower()
