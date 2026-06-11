import random
import game_data


def shuffle():
    return random.choice(game_data.data)


def printing(letter, character):
    print(
        f"{letter}: {character['name']}, a {character['description']}, from {character['country']}."
    )
