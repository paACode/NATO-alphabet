import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_phonetic_alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_phonetic_alphabet_dict = {row.letter: row.code for (index, row) in nato_phonetic_alphabet_df.iterrows()}
print(nato_phonetic_alphabet_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Type your word: ").upper()
output_phonetic_code_list = [nato_phonetic_alphabet_dict[letter] for letter in user_input if
                             letter in nato_phonetic_alphabet_dict.keys()]
print(output_phonetic_code_list)
