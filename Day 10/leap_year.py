def is_leap_year(year):
    year = int(year)
    if year % 400 == 0:
        return True
    elif year % 4 ==0 and not year % 100 == 0:
        return True
    else:
        return False

print(is_leap_year(input('Enter the year:\n')))