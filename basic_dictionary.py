s1 = {
    "name": "abc",
    "div": "A",
    "rno": 18
}
print("Dictionary of student: ", s1)
print("Div: ", s1["div"])

print("Dictionary Length: ", len(s1))
print("Dictionary Type: ", type(s1))
print("Name: ", s1.get("name"))
print("Keys: ", s1.keys())
print("Values: ", s1.values())

s1["marks"] = 85
print("All items: ", s1.items())

# Update the div from a to b
s1.update({"div": "B"})
print(s1)

# Remove item
s1.pop("name")
print(s1)

# Remove Latest Value
s1.popitem()
print(s1)

# Delete item
del s1["rno"]
print(s1)

# empty the dictionary
s1.clear()
print(s1)

# Copy()
s2 = s1.copy()
print(s2)

# Fromkeys()
x = ("m1","m2")
y = 50
z = dict.fromkeys(x,y)
print(z)

# Set Default
a = s1.setdefault("div", "A")
print(a)