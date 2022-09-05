def split_date(in_str):
    day = int(in_str[0:2])
    month = int(in_str[2:4])
    year = int(in_str[4:])
    return day, month, year


print(split_date("31012019"))
