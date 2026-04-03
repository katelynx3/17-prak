def get_days(month):
    days = [31, 28, 31 ,30 , 31, 30, 31, 31, 30, 31, 30, 31]
    return days[month - 1]
print(get_days(1))
print(get_days(2))
print(get_days(9))
