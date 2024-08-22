print("Welcome to the coffee machine!")

coffee_resources = {
  "water": 500,
  "milk": 200,
  "coffee": 100,
  "money": 0
}

coffee_menu = {
  "espresso": {
    "water": 50,
    "coffee": 18,
    "price": 2.50  
  },
  "latte": {
    "water": 50,
    "milk": 150,
    "coffee": 18,
    "price": 3.00  
  },
  "cappuccino": {
    "water": 50,
    "milk": 100,
    "coffee": 18,
    "price": 3.50  
  }
}

def report():
  print(f"Water: {coffee_resources['water']}ml")
  print(f"Milk: {coffee_resources['milk']}ml")
  print(f"Coffee: {coffee_resources['coffee']}g")
  print(f"Money: ${coffee_resources['money']}0")

def check_resources(choice):
  ingredients = coffee_menu[choice]
  for item in ingredients:
    if item != "price" and coffee_resources[item] < ingredients[item]:
      print(f"Sorry, there is not enough {item}.")
      return False
  return True

def process_coins():
  """Calculates the total value of coins inserted by the user."""
  print("Please insert coins.")
  quarters = int(input("How many quarters? ($0.25 each): "))
  dimes = int(input("How many dimes? ($0.10 each): "))
  nickels = int(input("How many nickels? ($0.05 each): "))
  pennies = int(input("How many pennies? ($0.01 each): "))

  total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
  coffee_resources["money"] += total
  return total

def money_calculator(choice):
  """Handles payment and checks if the user has inserted enough money."""
  price = coffee_menu[choice]["price"]
  print(f"The price for {choice} is ${price:.2f}.")
  
  total_money_inserted = process_coins()

  if total_money_inserted < price:
    print(f"Sorry, that's not enough money. You inserted ${total_money_inserted:.2f}, but the price is ${price:.2f}.")
    return False
  else:
    change = total_money_inserted - price
    if change > 0:
      print(f"Here is your change: ${change:.2f}.")
      coffee_resources["money"] -= change
    return True  

def make_coffee(choice):
  for item in coffee_menu[choice]:
    if item != "price":  
      coffee_resources[item] -= coffee_menu[choice][item]
  print(f"Here is your {choice} ☕. Enjoy!")

def user_choice():
  valid_choices = ["espresso", "latte", "cappuccino", "off", "report"]
  while True:
    choice = input("What would you like? (espresso/latte/cappuccino): \n").lower()
    
    if choice in valid_choices:
      return choice
    else:
      print("Invalid choice. Please choose 'espresso', 'latte', or 'cappuccino'.")

def coffee_machine():
  while True:
    choice = user_choice()
    
    if choice == "off":
      print("Turning off the coffee machine. Goodbye!")
      break
    elif choice == "report":
      report()
    else:
      if check_resources(choice):
        if money_calculator(choice):  
          make_coffee(choice)


coffee_machine()
