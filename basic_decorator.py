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
    return a + b

answer = add(10, 20)
print("Result:", answer)

