# TODO Squaring Numbers
# You are going to write a List Comprehension to create a new list called squared_numbers. This new list should contain every number in the list numbers but each number should be squared.
# e.g.
# 4 * 4 = 16
# 4 squared equals 16.
# **DO NOT** modify the List numbers directly. Try to use List Comprehension instead of a Loop.
# Target Output
# [1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num*num for num in numbers]
print(squared_numbers)


# TODO Filtering Even Numbers
# In this list comprehension exercise you will practice using list comprehension to filter out the even numbers from a series of numbers.
# First, use list comprehension to convert the list_of_strings to a list of integers called numbers.
# Then use list comprehension again to create a new list called result.
# This new list should only contain the even numbers from the list numbers.
# Again, try to use Python's List Comprehension instead of a Loop.
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(num) for num in list_of_strings]
result = [i for i in numbers if i%2==0]
print(result)


# TODO Data Overlap
# 💪 This exercise is HARD 💪
# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
# You are going to create a list called result which contains the numbers that are common in both files.
# e.g. if file1.txt contained:
# 1
# 2
# 3
# and file2.txt contained:
# 2
# 3
# 4
# result = [2, 3]
# IMPORTANT:  The output should be a list of integers and not strings!
# Try to use List Comprehension instead of a Loop.
with open("file1.txt") as var:
    file1 = var.readlines()
with open("file2.txt") as var:
    file2 = var.readlines()

result = [int(f1) for f1 in file1 if f1 in file2]

print(result)
