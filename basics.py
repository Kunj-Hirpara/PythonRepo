# 1
import math
import random

x = (random.randrange(1,50))
y = (random.randrange(1,50))

print("Square Root of number ", x, ":", math.sqrt(x))
print("Cosine of number ", x, ":", math.cos(x))
print("number pow ", x,"and",y, ":", math.pow(x,y))
print("Factorial of number ", x, ":", math.factorial(x))
print("------------------------------")

# 2
a = input("Enter a string: ")
print("You enter: ", a)

print("UperCase: ", a.upper())
print("LowerCase: ", a.lower())
print("Length of string: ", len(a))
print("Replace String: ")
b = input("Enter String: ")
print("Original String: ", a)
print("New String: ", a.replace(a,b))
print("------------------------------")

# 3
x = int(input("Enter num1: "))
y = int(input("Enter num2: "))

print("num1: ",x)
print("num2: ",y)

print("Add: ", x+y)
print("Sub: ", x-y)
print("Mul: ", x*y)
print("Div: ", x/y)
print("------------------------------")

# 4
a = int(input("Enter num1: "))
b = int(input("Enter num2: "))
c = int(input("Enter num3: "))

print("Min Max Function.")
print("Max num: ", max(a,b,c))
print("Min num: ", min(a,b,c))
print("------------------------------")

print("Nested If else condition for min.")
if a < b:
    if a < c:
        print("num1 is min.")
    else:
        print("num3 is min.")
elif b < a:
    if b < c:
        print("num2 is min.")
    else:
        print("num3 is min.")
else:
    print("Invalid.")
print("------------------------------")

print("If Else Condition for max.")
if a > b and a > c:
    print("num1 is max.")
elif b > a and b > c:
    print("num2 is max.")
else:
    print("num3 is max.")
    print("------------------------------")