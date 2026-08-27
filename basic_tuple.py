a = ("apple",) #comma is compalsary if 1 value

# convert tuple to list and list to tuple change value
fruit = ("banana", "apple", "cherry", "mango")
print("Before Change: ", fruit)
flist = list(fruit)
flist[0] = "kiwi"
fruit = tuple(flist)
print("After Change: ", fruit)

# add 4th value
a = ("a", "b", "c")
print(a)
b = list(a)
b.append("d")
a = tuple(b)
print(a)

# remove the value
a = ("a", "b", "c")
print(a)
b = list(a)
b.remove("c")
a = tuple(b)
print(a)

# delete tuple
a = ("a", "b", "c")
print(a)
b = list(a)
del b
# a = tuple(b)
# print(a)

# Join tuple
a = ("a", "b", "c")
b = ("d", "e", "f")
print(a)
print(b)
c = a+b
print(c)

# Multiple Tuple
a = ("a", "b", "c")
print(a)
b = a*2
print(b)