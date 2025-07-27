
with open("./Input/Letters/starting_letter.txt") as letter:
    letter_data = letter.read()
    # print(letter_data)


with open("./Input/Names/invited_names.txt") as names:
    names_list = names.readlines()
    for name in names_list:
        # print(new_names_list)
        new_letter_data = letter_data.replace("[name]", name.strip())
        with open(f"./Output/ReadyToSend/letter_for_{name.strip()}.txt", mode="w") as ready_letter:
            ready_letter.write(new_letter_data)




