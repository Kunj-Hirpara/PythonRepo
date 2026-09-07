# 1 to 20 numbers square using list comprehension

number = [num * num for num in range(1, 21)]
print("1 to 20 numbers square are: ", number)

# 1 to 50 even numbers using list comprehension

even_numbers = [num for num in range(1, 51) if num % 2 == 0]
print("1 to 50 even numbers are: ", even_numbers)

# above 50 numbers print in list comprehension

above_50_numbers = [num for num in range(1, 101) if num > 50]
print("Above 50 numbers are: ", above_50_numbers)

# Name are convert in uppercase using list comprehension

name_list = ["abc", "xyz", "pqr"]
uppercase_names = [name.upper() for name in name_list]
print("Uppercase names are: ", uppercase_names)

# numbers square using dictionary comprehension
square_dict = {num: num * num for num in range(1, 6)}
print("Numbers square using dictionary comprehension: ", square_dict)