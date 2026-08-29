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