f = open("chapter 9/file.txt")

line = f.readlines()
while(line != ""):
    print(line)
    line = f.readline()

f.close()