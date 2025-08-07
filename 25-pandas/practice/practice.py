# with open("weather_data.csv") as file:
#     data = file.readlines()
#
#     print(data)


# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temp = int(row[1])
#             temperatures.append(temp)
#
#     print(temperatures)

import  pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type((data["temp"])))

#CONVERT DATAfRAM(TABLE) TO DICTIONARY
# data_dict = data.to_dict()
# print(data_dict)

#CONVERT DATAfRAM(TABLE) TO LIST
# data_list = data["temp"].to_list()

#OLD WAY OF AVG(MEAN)
# total = 0
# for temp in data_list:
#     total += temp
#
# avg = total / len(data_list)
# print(avg)

#GET MEAN OR AVG
# data_mean = data["temp"].mean()
# print(data_mean)

#GET MAX VALUE
# print(data["temp"].max())

# //GET ROW
# print(data[data.day == "Monday"])

#ROW WHERE TEMP. IS MAX
# print(data[data.temp == data.temp.max()])

# LOOKING INTO ROW
# monday = data[data.day == "Monday"]
# # print(monday.condition)
# temp_in_f = monday.temp[0] * 9/ 5 + 32
# print(temp_in_f)
# # print(monday.temp)

#CREATE A DATAFRAME
# students_dict = {
#     "students": ["a", "b", "c"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(students_dict)
# print(data)
#
# data.to_csv("new_data.csv")


squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

Fur_colors = squirrel_data["Primary Fur Color"].unique().tolist()
Fur_colors = Fur_colors[1:]
# print(Fur_colors)

squirrels = squirrel_data["Primary Fur Color"].to_list()
# print(squirrels.count("Gray"))


squirrel_dict = {}
squirrel_count = []

for color in Fur_colors:
    squirrel_count.append(squirrels.count(color))


squirrel_dict["Fur color"] = Fur_colors
squirrel_dict["Count"] = squirrel_count

data = pandas.DataFrame(squirrel_dict)

data.to_csv("Squirrel_count.csv")


