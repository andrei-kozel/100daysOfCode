import pandas

nato_data = pandas.read_csv('nato_phonetic_alphabet.csv')
word = input("Enter a word: ").upper()

phonetic_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}
result = [phonetic_dict[letter] for letter in word]

print(result)
