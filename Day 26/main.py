# list assignments
# Assignment 1

# mbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squares = [mber**2 for mber in mbers]
# print(squares)

# Assignment 2

# list_of_strings = ["9", "0", "32", "8", "2", "8", "64", "29", "42", "99"]
# nums = [int(num) for num in list_of_strings]
# even_nums = [num for num in nums if num % 2 == 0]

# print(nums)
# print(even_nums)


# dict assignments

# Assignment 1
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# words = sentence.split(" ")
# result = {word: len(word) for word in words}
# print(result)

# Assignment 2

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: (temp * 9 / 5 + 32) for (day, temp) in weather_c.items()}
print(weather_f)
