
with open("./Input/Names/invited_names.txt", mode="r") as names:
    for name in names:
        strip_name = name.strip()
        with open("./Input/Letters/starting_letter.txt", mode="r") as starting_letter:
            content = starting_letter.read().replace("[name]", strip_name)
        with open(f'./Output/ReadyToSend/letter_for_{strip_name}.txt', mode="w+") as letter:
            letter.write(content)








