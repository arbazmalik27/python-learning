def inch_to_cms(inch):
    return inch * 2.54

n = int(input("Enter the number of inches: "))
print(f"{n} inches is equal to {inch_to_cms(n)} centimeters.")