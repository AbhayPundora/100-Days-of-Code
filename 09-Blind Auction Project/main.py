from art import logo

print(logo)

continue_bid = True
bids = {}

while continue_bid:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))

    bids[name] = price

    restart = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()

    if restart == "yes":
        print("\n" * 20)

    elif restart == "no":
        continue_bid = False

    else:
        print("Please type 'yes' or 'no' to continue..")

max_price = 0
winner = ""

for bidder in bids:
    if bids[bidder] > max_price:
        max_price = bids[bidder]
        winner = bidder

print(f"The winner is {winner} with a bid of ${max_price} ")


# bid_list = []
# for bid in bids:
#     bid_list.append(bids[bid])
#
# max_bid = max(bid_list)
#
# for bidder in bids:
#     if bids[bidder] == str(max_bid):
#         print(f"The winner is {bidder} with a bid of ${bids[bidder]} ")