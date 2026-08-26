sid = int(input("Enter Student id: "))
sname = input("Enter the student name: ")
mark1 = int(input("Enter Mark1: "))
mark2 = int(input("Enter Mark2: "))

print("------------------------------")

print("Student Id: ", sid)
print("Student Name: ", sname)
print("Mark1: ", mark1)
print("Mark2: ", mark2)

total = mark1+mark2
print("Total Marks: ", total)

per = (total/200)*100
print("Student Percentage: ", per)

if per > 90:
    print("Student Grade is A+.")
elif per > 80:
    print("Student Grade is B+.")
elif per > 70:
    print("Student Grade is c+.")
else:
    print("Student Fail.")