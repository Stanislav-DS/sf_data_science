def check_date(day, month, year):
    def is_leap(year):
        return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

    if (type(year) is not int or
            type(month) is not int or
            type(day) is not int):
        return False
    elif not (1900 <= year <= 2022):
        return False
    elif not (1 <= month <= 12):
        return False
    elif not (1 <= day <= 31):
        return False
    elif month in (4, 6, 9, 11) and day == 31:
        return False
    elif not is_leap(year) and month == 2 and day > 28:
        return False
    elif is_leap(year) and month == 2 and day > 29:
        return False
    return True