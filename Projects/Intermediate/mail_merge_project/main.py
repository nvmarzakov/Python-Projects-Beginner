PLACEHOLDER = "[name]"

# if you want to use "with"

# when we read text files and in case we forget to close them,
# if we use "with" python does this automatically for us

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_txt:
    letter_contents = letter_txt.read()
    for name in names:
        stripped_name = name.strip()
        personal_letter = letter_contents.replace(PLACEHOLDER, stripped_name)

        with open(f"./Output/ReadyToSend/invitation_for_{stripped_name}.txt", mode="w") as completed_invitation:
            completed_invitation.write(personal_letter)

# The second way with opening and closing the text files  

# names_file = open("./Input/Names/invited_names.txt")
# names = names_file.readlines()
#
# letter_file = open("./Input/Letters/starting_letter.txt")
# letter_contents = letter_file.read()
#
# for name in names:
#     stripped_name = name.strip()
#     new_letter = letter_contents.replace(PLACEHOLDER, name)
#     print(new_letter)
#
#     final_letter = open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w")
#     final_letter.write(new_letter)
#     final_letter.close()
#
# names_file.close()
# letter_file.close()


