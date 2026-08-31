class student:
    def __init__(self,name,cou,sem):
        self.name = name
        self.cou = cou
        self.sem = sem
        self.marks = []

    def add_marks(self,marks):
        self.marks.append(marks)

    def cal_avg(self):
        if len(self.marks) == 0:
            return 0
        return (sum(self.marks) / (len(self.marks)))
    
    def disp(self):
        print("Student Name: ", self.name)
        print("Student course: ", self.cou)
        print("Student Sem: ", self.sem)
        print("Student Percentage: ", self.cal_avg())

print("Enter Student Details:")
a = input("Enter Student Name: ")
b = input("Enter Student Course: ")
c = int(input("Enter Student Sem: "))

stu = student(a,b,c)

count = int(input("Enter the sub. of student: "))
for i in range(count):
    mark = int(input("Enter the Student Marks: "))
    stu.add_marks(mark)

stu.disp()