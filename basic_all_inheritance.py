# Single Inheritance

# class parent:
#     print("Hello Parent.")

# class child(parent):
#     def __init__(self):
#         super().__init__() #Optional Line
#         print("Hello Child.")
# c1 = child()


# Multiple Inheritance

# class c1:
#     def getname(self,name):
#         self.name = name

# class c2:
#     def getmarks(self,marks):
#         self.marks = marks

# class c3(c1,c2):
#     def disp(self):
#         print("Student Name: ", self.name)
#         print("Student Marks: ", self.marks)

# name = input("Enter student name: ")
# marks = int(input("Enter student marks: "))
# obj = c3()
# obj.getname(name)
# obj.getmarks(marks)
# obj.disp()


# Multi-Level Inheritance

class c1:
    def getname(self, name):
        self.name = name

class c2(c1):
    def getmarks(self, marks):
        self.marks = marks

class c3(c2):
    def disp(self):
        print("Name :", self.name)
        print("Marks :", self.marks)

name = input("Enter the name :")
marks = int(input("Enter the marks :"))
obj = c3()
obj.getname(name)
obj.getmarks(marks)
obj.disp()