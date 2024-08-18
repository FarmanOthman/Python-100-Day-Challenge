import random

print("Welcome to the password generator")

password_length = int(input("How many letters would you like in your password?\n"))
symbol_length = int(input("How many symbols would you like?\n"))
number_length = int(input("How many numbers would you like?\n"))

all_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
all_capital_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
all_characters = ["!", "#", "$", "%", "&", "(", ")", "*", "+", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"]
all_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

letters = ""
numbers = ""
symbols = ""

for _ in range(password_length):
    letters += random.choice(all_letters + all_capital_letters)

for _ in range(number_length):
    numbers += random.choice(all_numbers)

for _ in range(symbol_length):
    symbols += random.choice(all_characters)

password_list = list(letters + numbers + symbols)
random.shuffle(password_list)
password = ''.join(password_list)

print(f"Your generated password is: {password}")
