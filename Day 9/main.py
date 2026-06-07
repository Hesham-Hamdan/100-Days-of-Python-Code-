continue_bidding = "yes"
all_bids = {}

while continue_bidding == "yes":
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: $"))
    all_bids[name] = bid
    continue_bidding = input("Are there any other bidders? Type 'yes' or 'no' \n")
    print("\n" * 20)
