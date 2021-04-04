PLACEHOLDER = "[name]"

names = []

with open("Input/Names/invited_names.txt") as in_file:
    name_data = in_file.readlines()
    for x in name_data:
        names.append(x.strip())

with open("Input/Letters/starting_letter.txt") as in_file:
    letter = in_file.readlines()

for name in names:
    new_letter = []
    for line in letter:
        new_letter.append(line.replace(PLACEHOLDER, name))

    with open(f"Output/ReadyToSend/{name}.txt", "w") as out_file:
        out_file.writelines(new_letter)
