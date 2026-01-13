marks = int(input("Hi! Enter your marks \n")) #Taking user input for marks
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"
print("Your grade is:", grade) #Printing the grade based on the marks