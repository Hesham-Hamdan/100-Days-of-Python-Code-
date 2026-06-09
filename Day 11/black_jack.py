import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def generate_card():
    return cards[random.randint(0, len(cards) - 1)]
