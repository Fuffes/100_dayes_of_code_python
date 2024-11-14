students_dict = {
    'student': ['A', 'B', 'C', 'D'],
    'scores' : [1, 32, 444, 43]
}

# looping through the dict
for (key, value) in students_dict.items():
    print(key)


import pandas

students_data_frame = pandas.DataFrame(students_dict)
print(students_data_frame)

# Looping through the DataFrame
# for (key, value) in students_data_frame.items():
#     print(key)

# Looping through the rows in DataFrame
for (index, row) in students_data_frame.iterrows():
    print(row.student)

