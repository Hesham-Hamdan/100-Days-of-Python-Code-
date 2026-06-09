import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def generate_card():
    return cards[random.randint(0, len(cards) - 1)]


def completing_computer_hand(comp, yours, func):
    while sum(comp) < 17:
        comp.append(generate_card())
    print(f"Your final hand: {yours} , final score = {sum(yours)}")
    print(f"Computer's final hand: {comp},final score = {sum(comp)}")
    if sum(comp) > 21:
        if 11 in comp:
            comp[comp.index(11)] = 1
        else:
            print("You win, your opponent went over")
    elif sum(yours) < sum(comp):
        print("You lose")
    elif sum(yours) > sum(comp):
        print("You win")
    else:
        print("It's a draw")
    func()


def completing_user_hand(yours, comp):
    while sum(yours) < 21:
        another_card = input("Type 'y' to get another card, type 'n' to pass:")
        if another_card == "y":
            if 11 in yours and sum(yours) > 21:
                yours.remove(11)
                yours.append(1)
            yours.append(generate_card())
            print(f"Your cards: {yours} , current score = {sum(yours)}")
            print(f"Computer's first card: {comp}")
        else:
            completing_computer_hand(comp, yours, black_jack)
