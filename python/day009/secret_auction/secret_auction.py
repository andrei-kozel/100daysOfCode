import utilities
import art

print(art.logo)
print("welcome to the secret auction program!")
should_continue = True
bids = {}


def find_winner():
    biggest_bid = 0
    winner = {}
    for bidder in bids:
        if int(bids[bidder]) > int(biggest_bid):
            biggest_bid = bids[bidder]
            winner = {"name": bidder, "bid": bids[bidder]}
    print(f"The winner is {winner['name']} with a bid of ${winner['bid']}.")


while should_continue:
    name = input("What is your name?: ")
    bid = input("What is your bid?: ")
    result = input("Are there any other bidders? Type 'yes' or 'no': ")
    bids[name] = bid
    if str.lower(result) == "no":
        should_continue = False
        find_winner()
    elif str.lower(result) == "yes":
        utilities.clear_console()
