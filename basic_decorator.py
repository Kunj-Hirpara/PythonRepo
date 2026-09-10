def decorator(func):
    def wrapper():
        print("Before the function call.")
        func()
        print("After the function call.")
    return wrapper

@decorator
def hello():
    print("Hello world!")
hello()
# Second way to call the decorator function
# decorator(hello)()

# Third way to call the decorator function
# hello = decorator(hello)
# hello()

# Decorator with arguments
def decorator(func):
    def wrapper(name):
        print("Before")
        func(name)
        print("After")
    return wrapper

@decorator
def hello(name):
    print("Hello ", name)
hello("world!")

# *args and **kwargs
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print("Function ended")
        return result
    return wrapper

@decorator
def add(a, b):
    print("Result:", a+b)
add(10, 20)

@decorator
def info(name, age):
    print("Name: ", name)
    print("Age: ", age)
info(name="ABC", age=25)

# Logging decorator
def log_function(function):
    def wrapper(*args, **kwargs):
        print("Calling:", function.__name__)
        result = function(*args, **kwargs)
        print("Finished:", function.__name__)
        return result
    return wrapper

@log_function
def add(a, b):
    print("Result:", a+b)
add(10, 20)

@log_function
def info(name, age):
    print("Name: ", name)
    print("Age: ", age)
info(name="ABC", age=25)

# Authentication decorator
def login_required(function):
    def wrapper(user):
        if user == "Kunj":
            return function(user)
        print("Access denied")
    return wrapper

@login_required
def dashboard(user):
    print("Welcome to dashboard", user)

dashboard("Kunj")
dashboard("Rahul")