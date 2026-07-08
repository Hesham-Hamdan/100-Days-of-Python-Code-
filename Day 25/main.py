# with open("Day 25\weather_data.csv") as file:
#     data = file.readlines()


# challenge 1

# import csv

# with open("Day 25\weather_data.csv") as file:
#     data = csv.reader(file)
#     temps = []
#     for row in data:
#         temp = row[1]
#         if temp != "temp":
#             temps.append(int(temp))

# print(temps)

# challenge 2

import pandas

data = pandas.read_csv("Day 25\weather_data.csv")
temps = data["temp"]

avg = sum(temps) / len(temps)
print(avg)

maximum = temps.max()
print(maximum)


print(data[data["temp"] == maximum])

monday_temp = data[data["day"] == "Monday"]["temp"][0]

feh = monday_temp * 9 / 5 + 32
print(feh)

# challenge 3

# data = pandas.read_csv("Day 25\Central-Park-Squirrel-Census-Squirrel-Data.csv")
# squirrels = {
#     "Fur Color": ["grey", "red", "black"],
#     "Count": [
#         len(data[data["Primary Fur Color"] == "Gray"]),
#         len(data[data["Primary Fur Color"] == "Cinnamon"]),
#         len(data[data["Primary Fur Color"] == "Black"]),
#     ],
# }

# data2 = pandas.DataFrame(squirrels)
# data2.to_csv("Day 25\squirrel_count.csv")
