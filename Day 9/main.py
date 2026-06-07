continue_bidding = "yes"
all_bids = {}

while continue_bidding == "yes":
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: $"))
    all_bids[name] = bid
    continue_bidding = input("Are there any other bidders? Type 'yes' or 'no' \n")
    print("\n" * 20)

bigger_bid = ["", 0]

for bidder in all_bids:
    if all_bids[bidder] > bigger_bid[1]:
        bigger_bid[1] = all_bids[bidder]
        bigger_bid[0] = bidder


print(f"The winner is {bigger_bid[0]} with a bid of {bigger_bid[1]}")
