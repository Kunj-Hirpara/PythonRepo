# Pattern
nums = int(input("Enter the num :"))

for i in range(1, nums+1):
    for j in range(i):
        print ("*", end=" ")
    print()

# 2.
# nums = int(input("Enter Values :"))

for i in range(1, nums+1):
    for j in range(1, i+1):
        print (j, end=" ")
    print()

# 3.
# nums = int(input("Enter Values :"))

for i in range(nums, 0, -1):
    for j in range(1, i+1):
        print (j, end=" ")
    print()