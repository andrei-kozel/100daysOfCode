def get_names():
    with open("Input/Names/invited_names.txt", "r") as invited_names:
        return invited_names.read().split()


def get_letter_example():
    with open("Input/Letters/starting_letter.txt", "r") as starting_letter:
        return starting_letter.read()


names = get_names()
letter = get_letter_example()

for name in names:
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as ready_to_send:
        text = letter.replace("[name]", name, 1)
        ready_to_send.write(text)
