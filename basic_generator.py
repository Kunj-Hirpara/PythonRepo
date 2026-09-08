# Generators are related to iterators.
# A generator produces values one at a time instead of creating all values in memory.
# The main keyword is: yield

def numbers():

    yield 1
    yield 2
    yield 3


for number in numbers():
    print(number)