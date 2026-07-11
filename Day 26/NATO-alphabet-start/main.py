import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

data = pandas.read_csv("Day 26/NATO-alphabet-start/nato_phonetic_alphabet.csv")

# step 1
letter_word = {row.letter: row.code for (_, row) in data.iterrows()}
print(letter_word)
# step 2
input_word = list(input("Enter a word: ").upper())
phonetis_words = [letter_word[letter] for letter in input_word]
print(phonetis_words)
