#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
names = open("./Input/Names/invited_names.txt", mode='r')
temp_letter = open("./Input/Letters/starting_letter.docx", mode='r')

# list_of_names = names.readlines()
# temp_letter_list = temp_letter.readlines()
#
# for name in list_of_names:
#     new_list = []
#     new_list.append(temp_letter_list)
#     new_list[0] = new_list[0][0].replace("[name]", name.strip())
#     for _ in range(1,len(temp_letter_list)):
#         new_list.append(temp_letter_list[_])
#     with open(f"C:/Users/rafwz/Documents/PythonProjects/mail-merge-project-start/Output/ReadyToSend/letter_for_{name.strip()}.docx", mode="a") as new_letter:
#         for _ in range(0, len(new_list)):
#             new_letter.write(new_list[_])

list_of_names = names.readlines()
temp_l = temp_letter.read()

for name in list_of_names:
    new_letter = temp_l.replace("[name]", name.strip())
    with open(f"C:/Users/rafwz/Documents/PythonProjects/mail-merge-project-start/Output/letter_for_{name.strip()}.docx", mode="w") as letter:
            letter.write(new_letter)

names.close()
temp_letter.close()