import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241113.csv")

series = data["Primary Fur Color"]


# TODO get unique values of fure -> list1
fure = series.unique()
fure = fure[:-1]


#TODO get count of items with unique values -> list2
length = []
for i in fure:
    if i :
        length.append(len(data[series == i]))

#TODO make final dict where keys "Fur Color" and "Count", values list1 and list2

final_data = {
    "Fur Color" : fure,
    "Count" : length
}

# TODO export csv
new_csv = pandas.DataFrame(final_data)
new_csv.to_csv("squirrel_count.csv")