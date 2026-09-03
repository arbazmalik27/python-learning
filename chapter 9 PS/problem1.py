f = open("chapter 9 PS/about.txt")
content = f.read()
if("Computer Science" in content):
    print("Yes, 'computer science' is present in the file.")

else:
    print("No, 'computer science' is not present in the file.")

f.close()