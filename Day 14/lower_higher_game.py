import random
import game_data


def shuffle():
    return random.choice(game_data.data)


def printing(letter, character):
    print(
        f"{letter}: {character['name']}, a {character['description']}, from {character['country']}."
    )


def check_answer(guess, num1, num2):
    win = max(num1, num2)
    if guess["follower_count"] == win:
        return True
    else:
        return False


def choosing_characters():
    characters = {"a": shuffle(), "b": shuffle()}
    while characters["a"] == characters["b"]:
        characters["b"] = shuffle()
    return characters
