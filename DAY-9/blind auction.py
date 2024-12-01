# # if you're using replit, then import replit
# from replt import clear

# from art import logo
# print(logo)

bids = {}
bidding_finish = True

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while bidding_finish:
    name = input("What is your name\n")
    price = int(input("What is your bid? $"))
    bids[name] = price
    print(bids)

    continue_bidding = input("Are there any other bidders? 'yes' or 'no'.\n").lower()
    if continue_bidding == "yes":
        should_go_again = True
        # clear()
    elif continue_bidding == "no":
        bidding_finish = False
        find_highest_bidder(bidding_record=bids)
