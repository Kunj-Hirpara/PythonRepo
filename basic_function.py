# def add(a,b):
#     print("Addition = ",a+b)
# a = int(input("Enter Number 1 :"))
# b = int(input("Enter Number 2 :"))
# add(a,b)

# def op(a,b,opt):
#     if (opt == '+'):
#         print("Addition ",a, "+", b, " = ", a+b)
#     elif (opt == '-'):
#         print("Sub ",a, "-", b, " = ", a-b)
#     elif (opt == '*'):
#         print("Mul ",a, "*", b, " = ", a*b)
#     elif (opt == '/'):
#         print("Div ",a, "/", b, " = ", a/b)
#     else:
#         print("Invalid..")
# a = int(input("Enter Number 1 :"))
# b = int(input("Enter Number 2 :"))
# opt = input("Enter the sign (+,-,*,/) : ")
# op(a,b,opt)

# def op(a, b, opt):
#     match opt:
#         case '+':
#             print("Addition", a, "+", b, "=", a + b)
#         case '-':
#             print("Sub", a, "-", b, "=", a - b)
#         case '*':
#             print("Mul", a, "*", b, "=", a * b)
#         case '/':
#             if b != 0:
#                 print("Div", a, "/", b, "=", a / b)
#             else:
#                 print("Division by zero not allowed")
#         case _:
#             print("Invalid..")

# a = int(input("Enter Number 1 : "))
# b = int(input("Enter Number 2 : "))
# opt = input("Enter the sign (+,-,*,/) : ")
# op(a, b, opt)

# *args Function

# def s_d(name, rno, *marks):
#     print("Student Name: ", name)
#     print("Student RollNo: ", rno)
#     print("Marks: ", marks)

#     total = sum(marks)
#     print("Total: ", total)

#     per = (total/ (len(marks) * 100)) * 100
#     print("Percentage: ", per)

# name = input("Enter the name: ")
# rno = int(input("Enter the RollNo: "))
# marks = list(map(int, input("Enter the marks: ").split()))
# s_d(name,rno,*marks)


# use lambda function'
# In this function is use the only one line function

# add = lambda x,y : x+y
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# print("Addition: ", add(a,b))

list1 = list(map(int, input("Enter the list1: ").split()))
list2 = list(map(int, input("Enter the list2: ").split()))
print("List1: ", list1)
print("List2: ", list2)
fun = list(map(lambda x,y : x*y, list1, list2))
print(fun)


# Global Function

# n = 10
# def check():
#     global n
#     n += 10
#     print("Inside n = ", n)
# check()
# print("Outside n = ", n)