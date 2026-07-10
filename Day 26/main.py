# list assignments
# Assignment 1

# mbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squares = [mber**2 for mber in mbers]
# print(squares)

# Assignment 2

list_of_strings = ["9", "0", "32", "8", "2", "8", "64", "29", "42", "99"]
nums = [int(num) for num in list_of_strings]
even_nums = [num for num in nums if num % 2 == 0]

print(nums)
print(even_nums)
