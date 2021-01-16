# with open("weather_data.csv") as csv:
#     data = csv.readlines()
#
# print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# avr_temp = sum(temp_list)/len(temp_list)
# print(avr_temp)
# avr_temp = data["temp"].mean()
# print(avr_temp)
# max_temp = data["temp"].max()
# print(max_temp)
#
# # Column
# print(data["condition"])
# print(data.condition)
#
# # Row
# print(data[data.day == "Monday"])
#
# print(data[data.temp == data["temp"].max()])
#
# monday = data[data.day == "Monday"]
# temp_f = int(monday.temp)*1.8 + 32
# print(temp_f)

