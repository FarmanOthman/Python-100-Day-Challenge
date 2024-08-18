import random
print(random.randint(1,3))
choose =int (input("What do you choose? \n1 for Rock \n2 for Paper\n3 for Scissors\n"))

random_num = random.randint(1,3)

if choose == 1:
  print("You pick rock")
  if random_num == 1:
    print("Computer peck rock\nTie")
  elif random_num == 2:
    print("Computer peck paper\nYou lose")
  else:print("Computer peck scissors\nYou win")
elif choose == 2:
  print("You pick paper")
  if random_num == 1:
    print("Computer peck rock\nYou win")
  elif random_num == 2:
    print("Computer peck paper\nTie")
  else:print("Computer peck scissors\nYou lose")
elif choose == 3:
  print("You pick scissors")
  if random_num == 1:
    print("Computer peck rock\nYou lose")
  elif random_num == 2:
    print("Computer peck paper\nYou win")
  else:print("Computer peck scissors\nTie")
else:
  print("choose some one please")
