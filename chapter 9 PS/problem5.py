word = ["Donkey", "bad", "ganda"]

with open("chapter 9 PS/file.txt", "r") as f:
    content = f.read()

for word in word:
    content = content.replace(word, "#" * len(word))

with open("chapter 9 PS/file.txt", "w") as f:
    f.write(content)