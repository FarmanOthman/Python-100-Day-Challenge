import random

print("Guess the word")
word_list = ["hello", "banana", "apple", "city", "good", "bad", "python"]
the_word = random.choice(word_list)
print("_" * len(the_word))  # Show the number of letters in the word

incorrect = 0
guessed_letters = []

while incorrect < 5:
  guess = input("Guess a letter?\n").lower()  # Make sure the guess is lowercase
  
  if guess in the_word:
    if guess not in guessed_letters:
      guessed_letters.append(guess)
      print("Correct!")
    else:
      print("You already guessed that letter!")
  else:
    print("Wrong!")
    incorrect += 1
  
  progress = ""
  for letter in the_word:
    if letter in guessed_letters:
      progress += letter
    else:
      progress += "_"
  print(progress)
  
  if "_" not in progress:
    print("Congratulations! You guessed the word!")
    break
else:
  print(f"Sorry, you didn't guess the word. The word was '{the_word}'.")
