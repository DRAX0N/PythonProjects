# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
import pandas
alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter:row.code for (index, row) in alphabet.iterrows()}
# print(alphabet_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_letters():
    enter_word = input("Type word: ").upper()
    try:
        p_list = [alphabet_dict[letter] for letter in enter_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_letters()
    else:
        print(p_list)

# error = True
# while error:
#     enter_word = input("Type word: ").upper()
#     try:
#         p_list = [alphabet_dict[letter] for letter in enter_word]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#     else:
#         error = False
generate_letters()
# print(p_list)
# p_list = [alphabet_dict[enter_word[index]] for index in range(len(enter_word))]


