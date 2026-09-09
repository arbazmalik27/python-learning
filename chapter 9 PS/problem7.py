with open("chapter 9 PS/log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if "Python" in line:
        print(f"yes python is present in line {lineno}")
        break
    lineno += 1

else: 
    print("No python is not present")