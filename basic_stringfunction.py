a = input("Enter the string: ")
print("Your String: ", a)

print("Remove Whitespace from String.")
a1 = a.strip()
print(a1)

print("Converts the string to lowercase.")
a2 = a.lower()
print(a2)

print("Converts the string to uppercase.")
a3 = a.upper()
print(a3)

print("Replace the string1 with string2.")
b = input("Enter the second string for replace: ")
print("You enter: ", b)
a4 = a.replace(a, b)
print("Replaced String: ", a4)

print("Split the string with “*”.")
c = input("Enter the string '*' with : ")
a5 = c.split("*")
print("String: ", a5)

print("Capitalize the first character in the string.")
a6 = a.capitalize()
print(a6)

print("Count the 'imca' word in the string.")
d = input("Enter 'imca' multiple time: ")
print(d.count("imca"), "Time Imca word in string.")

print("Print the total number of 'e' character in the string.")
e = input("Enter 'e' multiple time: ")
print(e.count("e"), "Time e word in string.")

print("Print the index value of the 'n' character in the string.")
f = input("Enter 'n' multiple time: ")
for i in range(len(f)):
    if f[i] == 'n':
        print(i)

print("Check the string contains only alphabets or alphanumeric or digit.")
if a.isalpha():
    print("The String contains only Alphabets.")
elif a.isalnum():
    print("The String contains Alphanumeric.")
elif a.isnumeric():
    print("The string contains only numeric.")
else:
    print("The string has special characters or spaces.")
