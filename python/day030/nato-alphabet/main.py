import pandas

nato_data = pandas.read_csv('nato_phonetic_alphabet.csv')


def generate_phonetic():
    word = input("Enter a word: ").upper()

    try:
        phonetic_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}
        result = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(result)


generate_phonetic()
