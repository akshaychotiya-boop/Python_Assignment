#Write to a file
f = open('student_grades.txt', 'w') #Creating a file to store student grades
f.write("Akshay: 85\nBhavna: 92\nChirag: 78\nDivya: 90\n") #Writing initial grades to the file
f.write("Esha: 88\n") #Adding a new student and their grade
f.close() #Closing the file

#Read from the file
f = open('student_grades.txt', 'r') #Opening the file to read updated grades
data = f.read() #Reading the file content
print(data) #Printing the content of the file 
f.close() #Closing the file