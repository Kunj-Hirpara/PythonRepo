# Unordered to order
s1 = {1,3,2}
print(s1)

print("Length: ", len(s1))
print("Type: ", type(s1))

# check 2 is exist or not
print(2 in s1)

# Using Not 
print(4 not in s1)

# Add key value
s1.add(4)
print(s1)

# Update
s2 = {"a","b","c"}
s1.update(s2)
print(s1)

# Add with tuple
t1 = ("d","e")
s1.update(t1)
print(s1)

# Remove
s1.remove("e")
print(s1)

# Discard
s1.discard("a")
print(s1)

# Pop Method remove any value
s1.pop()
print (s1)

# Clear 
s1.clear()
print (s1)

# Delete
del s1
# print (s1)



# Join Sets
s1 = {"a","b","c"}
s2 = {"b","d","e"}

# Union Method
# s3 = s1.union(s2)
# print(s3)

# Intersection Method
# s3 = s1.intersection(s2)
# print(s3)

# Intersection_Update Method
# s1.intersection_update(s2)
# print (s1)

# Difference Method
# s3 = s1.difference(s2)
# print (s3)

# Symmetric Diffrencce
# s3 = s1.symmetric_difference(s2)
# print (s3)

# Copy
# s2 = s1.copy()
# print (s2)

# isdisjoint
# s3 = s1.isdisjoint(s2)
# print (s3)

# issubset
# s3 = s1.issubset(s2)
# print (s3)