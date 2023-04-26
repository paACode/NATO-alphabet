import pandas


def translate_to_phonetic():
    try:
        user_input = input("Type your word: ").upper()
        output_phonetic_code_list = [nato_phonetic_alphabet_dict[letter] for letter in user_input]
    except KeyError:
        print("Only type letters please")
        translate_to_phonetic()
    else:
        print(output_phonetic_code_list)


# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_phonetic_alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_phonetic_alphabet_dict = {row.letter: row.code for (index, row) in nato_phonetic_alphabet_df.iterrows()}

translate_to_phonetic()
