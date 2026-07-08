# challenge 1

import csv

with open("Day 25\weather_data.csv") as file:
    data = csv.reader(file)
    temps = []
    for row in data:
        temp = row[1]
        if temp != "temp":
            temps.append(int(temp))

print(temps)
