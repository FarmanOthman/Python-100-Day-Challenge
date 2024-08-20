print("Welcome to the Secure Auction Program!")
num_items = int(input("Enter the number of items you want to bid on: "))

auction_items = {}

for i in range(num_items):
    item_name = input(f"Enter the name of item {i + 1}: ")
    initial_bid = int(input(f"Enter your bid for {item_name}: "))
    auction_items[item_name] = [{"name": "Initial Bidder", "bid": initial_bid}]

print("The auction begins!")

for item_name, bids in auction_items.items():
    while True:
        print(f"\nItem: {item_name}\nCurrent highest bid: ${max(b['bid'] for b in bids)}")
        more_bidders = input("Is there another bidder? Type 'y' for yes or 'n' for no: ").lower()
        if more_bidders == 'y':
            bidder_name = input("Enter the new bidder's name: ")
            new_bid = int(input(f"Enter {bidder_name}'s bid for {item_name}: "))
            bids.append({"name": bidder_name, "bid": new_bid})
        else:
            highest_bid = max(bids, key=lambda x: x['bid'])
            print(f"The highest bid for {item_name} is ${highest_bid['bid']} by {highest_bid['name']}.")
            break
