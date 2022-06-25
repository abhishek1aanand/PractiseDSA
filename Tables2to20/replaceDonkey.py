with open("content1.txt", "r") as f:
    content = f.read()

content = content.replace("Donkey", "##$@%##")

with open("content1.txt", "w") as f:
    f.write(content)



