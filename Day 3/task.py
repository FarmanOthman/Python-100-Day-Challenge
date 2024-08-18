pizza_size = input("what size of pizza you want? S or M or L\n")
cash = 0
if pizza_size == "s":
  cash = 15
  pepparoni = input("do you want add pepparoin?Y or N\n")
  if pepparoni == "y":
    cash+=2
elif pizza_size == "m":
  cash = 20
  pepparoni = input("do you want add pepparoin?Y or N\n")
  if pepparoni == "y":
    cash+=2
else: 
  cash = 25 
  pepparoni = input("do you want add pepparoin?Y or N\n")
  if pepparoni == "y":
    cash+=3
cheese = input("do you want addtion chesse? Y or N\n")
if cheese == "y":
  cash +=1
print(f"total cash is {cash}")
  