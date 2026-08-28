a = int(input("Enter your age: "))

if a < 0:
    print("You are entering an invalid negative age.")

elif a == 0:
    print("You are entering an invalid age of zero.")

elif a >= 18:
    print("You are above the age of consent.")
    print("Good for you.")

else:
    print("You are below the age of consent.")

print("End of Program")