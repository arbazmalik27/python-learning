f = open("chapter 9/file.txt")
print(f.read())
f.close()

#The same can be written using with statement which automatically closes the file after the nested block of code.

with open("chapter 9/file.txt") as f:
    print(f.read())