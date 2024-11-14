
# with (open("weather_data.csv", "r") as file):
#     data_list = file.readlines()
#
#
# print(data_list)

# import csv
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
# print(temperatures)


# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# dict_data = data.to_dict()
# print(dict_data)
#
# temp_list = data['temp'].to_list()
# print(temp_list)
#
# avg2 = data["temp"].mean()
# print(avg2)
#
# max = data['temp'].max()
# print(max)




#Get data in colums
# print(data.day)

# get data in row
# print(data[data.day == 'Monday'])


# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# print(monday.condition)




# temp to C

# temps = data.temp
# for i in range(0, len(temps)):
#     temps[i] = temps[i]*1.8+32
#
# print(temps)



# CREATE DATAFRAME FROM SCRATCH
# data_dict = {
#     "students": ["Any", "James", "Angela"],
#     "scores" : [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)