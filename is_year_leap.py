def is_year_leap(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    return False

print(is_year_leap(1240))
a = 10
A = 20