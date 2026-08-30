# class student:
#     def put(self,a):
#         print("The name is: ", a)

# stu = student()
# stu.put("abc")

# class student:
#     def put(self,a):
#         self.a = a

#     def put1(self):
#         print("The name is: ", self.a)

# stu = student()
# stu.put("abc")
# stu.put1()

class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def put(self):
        print("Name: ", self.name)
        print("Marks: ", self.marks)

a = input("Enter Name: ")
b = int(input("Enter Marks: "))
stu = student(a,b)
stu.put()
