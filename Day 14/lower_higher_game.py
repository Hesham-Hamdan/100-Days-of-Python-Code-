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


def playing():
    continue_playing = True
    score = 0
    prev = {}
    while continue_playing:
        accounts = choosing_characters()

        if prev != {}:
            accounts["a"] = prev

        printing("Compare A", accounts["a"])
        printing("Against B", accounts["b"])

        account1_followers = accounts["a"]["follower_count"]
        account2_followers = accounts["b"]["follower_count"]

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        print("\n" * 10)
        is_correct = check_answer(
            accounts[guess], account1_followers, account2_followers
        )

        if is_correct:
            score += 1
            prev = accounts["b"]
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            continue_playing = False


playing()
