import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def generate_card():
    return cards[random.randint(0, len(cards) - 1)]


def black_jack():
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        your_cards = [
            generate_card(),
            generate_card(),
        ]
        computer_cards = [generate_card()]

        # Check for immediate double Aces on the first draw
        if sum(your_cards) == 22:
            your_cards[your_cards.index(11)] = 1

        print(f"Your cards: {your_cards} , current score = {sum(your_cards)}")
        print(f"Computer's first card: {computer_cards}")

        def completing_computer_hand():
            while sum(computer_cards) < 17:
                computer_cards.append(generate_card())
                # Check for Ace immediately after computer draws
                if 11 in computer_cards and sum(computer_cards) > 21:
                    computer_cards[computer_cards.index(11)] = 1

            print(f"Your final hand: {your_cards} , final score = {sum(your_cards)}")
            print(
                f"Computer's final hand: {computer_cards}, final score = {sum(computer_cards)}"
            )

            if sum(computer_cards) > 21:
                print("You win, your opponent went over")
            elif sum(your_cards) < sum(computer_cards):
                print("You lose")
            elif sum(your_cards) > sum(computer_cards):
                print("You win")
            else:
                print("It's a draw")

        def shuffle():
            while sum(your_cards) < 21:
                another_card = input("Type 'y' to get another card, type 'n' to pass:")
                if another_card == "y":
                    your_cards.append(generate_card())

                    # FIX: Check for Ace immediately BEFORE printing
                    if 11 in your_cards and sum(your_cards) > 21:
                        your_cards.remove(11)
                        your_cards.append(1)

                    print(
                        f"Your cards: {your_cards} , current score = {sum(your_cards)}"
                    )
                    print(f"Computer's first card: {computer_cards}")
                else:
                    completing_computer_hand()
                    return  # Exit the shuffle function so it doesn't keep looping

        # Initial check for Blackjack (21 on first two cards)
        if sum(your_cards) == 21:
            print(f"Your final hand: {your_cards} , final score = 21")
            print(
                f"Computer's final hand: {computer_cards}, final score = {sum(computer_cards)}"
            )
            print("You won with a Blackjack")
        else:
            shuffle()

            # If shuffle ends and user is over 21, they busted
            if sum(your_cards) > 21:
                print(
                    f"Your final cards: {your_cards} , final score = {sum(your_cards)}"
                )
                print(
                    f"Computer's final cards: {computer_cards}, final score = {sum(computer_cards)}"
                )
                print("You went over. You lose.")


black_jack()
