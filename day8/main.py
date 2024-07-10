def read_file():
    with open("Input/Names/invited_names.txt", "r") as file:
        names = file.readlines()
    return names

def read_blueprint():
    with open("Output/ReadyToSend/example.txt", "r") as f:
        blueprint = f.read()
    return blueprint

blueprint = str(read_blueprint())

type(blueprint)

names = [x.strip() for x in read_file()]

print(blueprint)

for name in names:
    text = blueprint.replace("[name]", name)
    with open(f"Output/ReadyToSend/letter_for_{name}", "w") as file:
        file.write(text)
