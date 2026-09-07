word = "Donkey"

with open("chapter 9 PS/file.txt", "r") as f:
    content = f.read()

content_new = content.replace(word, "######")

with open("chapter 9 PS/file.txt", "w") as f:
    f.write(content_new)