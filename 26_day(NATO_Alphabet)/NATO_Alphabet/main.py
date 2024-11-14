# {new_key:new_value for (index, row) in df.iterrows()}
import pandas

file = "nato_phonetic_alphabet.csv"

#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv(file)
parsed_data = {row.letter:row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

input = input("Enter the word ").upper()
result = [parsed_data[letter] for letter in input]
print(result)