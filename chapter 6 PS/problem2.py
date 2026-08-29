marks1 = int    (input("Enter your marks 1: " ))
marks2 = int(input("Enter your marks 2: " ))
marks3 = int(input("Enter your marks 3: " ))

total_percentage = ((100) * (marks1 + marks2 + marks3)) / 300

if(total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33):
    print("You have passed the exam with distinction")
else:
    print("You have failed the exam , better luck next time, total percentage is: ", total_percentage  )

