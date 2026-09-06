import add, sub, mul, div

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition: ", add.add(a,b))
print("Subtraction: ", sub.sub(a,b))
print("Multiplication: ", mul.mul(a,b))
try:
    print("Division: ", div.div(a,b))
except ValueError:
    print("Error: Cannot divide by zero")