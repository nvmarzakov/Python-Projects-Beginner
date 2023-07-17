PLACEHOLDER = "[name]"

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

# if you want to use "with"
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_txt:
    letter_contents = letter_txt.read()
    for name in names:
        stripped_name = name.strip()
        personal_letter = letter_contents.replace(PLACEHOLDER, stripped_name)

        with open(f"./Output/ReadyToSend/invitation_for_{stripped_name}.txt", mode="w") as completed_invitation:
            completed_invitation.write(personal_letter)
