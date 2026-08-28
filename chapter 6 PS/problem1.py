a1 = int(input("Enter your number 1: " ))
a2 = int(input("Enter your number 2: " ))
a3 = int(input("Enter your number 3: " ))
a4 = int(input("Enter your number 4: " ))

if(a1>a2 and a1>a3 and a1>a4):
    print("The Greatest number is: ", a1)
elif(a2>a1 and a2>a3 and a2>a4):
    print("The Greatest number is: ", a2)
elif(a3>a1 and a3>a2 and a3>a4):
    print("The Greatest number is: ", a3)
else:
    print("The Greatest number is: ", a4)

