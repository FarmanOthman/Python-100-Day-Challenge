import random

def calculate_score(hand):
  score = 0
  aces = 0
  for card in hand:
    if card in ["J", "Q", "K"]:
      score += 10
    elif card == "A":
      aces += 1
      score += 11
    else:
      score += int(card)

  while score > 21 and aces:
    score -= 10
    aces -= 1

  return score

def deal_card():
  cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
  return random.choice(cards)

def blackjack():
  print("Welcome to Blackjack!")
  
  player_hand = [deal_card(), deal_card()]
  dealer_hand = [deal_card(), deal_card()]

  while True:
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)
    
    print(f"Your cards: {player_hand}, Your score: {player_score}")
    print(f"Dealer's first card: {dealer_hand[0]}")

    if player_score == 21:
      print("Blackjack! You win!")
      return
    elif player_score > 21:
      print("You bust! Dealer wins.")
      return

    hit = input("Type 'y' to get another card, 'n' to pass: ").lower()
    if hit == "y":
      player_hand.append(deal_card())
    else:
      break

  while dealer_score < 17:
    dealer_hand.append(deal_card())
    dealer_score = calculate_score(dealer_hand)

  print(f"Your final hand: {player_hand}, final score: {player_score}")
  print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")

  if dealer_score > 21 or player_score > dealer_score:
    print("You win!")
  elif dealer_score > player_score:
    print("Dealer wins.")
  else:
    print("It's a draw!")

blackjack()
