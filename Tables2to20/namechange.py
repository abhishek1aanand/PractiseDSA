import os
file = "toberenamed"

with open(file, 'r') as f:
    content = f.read()

with open("newnamed.txt", 'w') as f:
    f.write(content)

os.remove(file)