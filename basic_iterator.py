# What is an Iterator?
# An iterator is an object that allows you to access elements one at a time.

numbers = [10, 20, 30]
iterator = iter(numbers)
print(next(iterator))
print(next(iterator))
print(next(iterator))

names = ["abc", "xyz", "pqr"]
it = iter(names)
print(next(it))
print(next(it))
print(next(it))


num = [1, 2, 3]
it = iter(num)
for i in it:
    print(i)


name = "Kunj"
it = iter(name)
print(next(it))
print(next(it))
print(next(it))
print(next(it))


class Count:

    def __init__(self, max_value):
        self.max_value = max_value
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.current <= self.max_value:
            value = self.current
            self.current += 1
            return value

        raise StopIteration


numbers = Count(5)

for number in numbers:
    print(number)