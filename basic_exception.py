# try:
#     print(x)
# except:
#     print("An exception occurred.")
# finally:
#     print("In Finally code.")


# try:
#     print("Hello")
# except:
#     print("An exception occurred.")
# else:
#     print("Nothing went wrong.")
# finally:
#     print("In Finally code.")


# Built-in Exception

# try:
#     k = 5/0
#     print(k)
# except ZeroDivisionError:
#     print("can't divide by zero.")
# finally:
#     print("Finally is always executed.")


# a = [1,2,3]
# try:
#     print("Second Element: ", a[1])
#     print("Fourth Element: ", a[3])
# except IndexError:
#     print("An error occurred.")


# try:
#     print(x)
# except NameError:
#     print("An Exception Occurred.")
# finally:
#     print("In Finally code.")


# Raising Exception

# x = int(input("Enter an integer value: "))
# try:
#     if x < 0:
#         raise Exception("Sorry, no numbers below zero")
#     else:
#         print(x)
# except Exception:
#     print("Error Occurred.")


# user define exception

# class InvalidAgeException(Exception):
#     print("Raised when the input value is less than 18.")
#     pass
# try:
#     age = int(input("Enter your age: "))
#     if age < 18:
#         raise InvalidAgeException
#     else:
#         print("You are eligible to vote.")
# except InvalidAgeException:
#     print("Sorry, you are not eligible to vote.")


# Assert Keyword

# x = "Hello"
# assert x == "Hello"

# a = 4
# b = 2
# print("The Value of a/b is : ")
# assert b != 0
# print(a/b)

x = int(input("Enter an integer value: "))
assert x > 0
print(x)