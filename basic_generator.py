# Generators are related to iterators.
# A generator produces values one at a time instead of creating all values in memory.
# The main keyword is: yield

# 1
def numbers():
    yield 1
    yield 2
    yield 3

for number in numbers():
    print(number)

# 2
def numbers(n):
    for i in range(1, n + 1):
        yield i

for number in numbers(5):
    print(number)

# 3
def squares(n):
    for i in range(1, n + 1):
        yield i * i

for square in squares(5):
    print(square)