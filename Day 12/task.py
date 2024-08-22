import random
print("Welcome to guess the number game")
level = input("Choose a difficulty. Type 1 for 'easy' or 2 for 'hard': ")

def random_number():
  return random.randint(1, 100)

def check_guess(guess , number):
  if guess > number:
    print("Too high")
  elif guess < number:
    print("Too low")
  else:
    print("Correct!")

def set_difficulty():
  if level == '1':
    return 10
  else:
    return 5

def game():
  print("I'm thinking of a number between 1 and 100.\nCan you guess what it is?")
  number = random_number()
  guess = 0
  turns = set_difficulty()

  while guess != number:
    print(f"You have {turns} attempts remaining to guess the number.")

    guess = int(input("Make a guess: "))
    turns -= 1
    check_guess(guess, number)

    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != number:
      print("Guess again.")

game()
