def multiply_lst(lst):
    if not lst:
        return 1
    return lst[0] * multiply_lst(lst[1:])


my_lst = [10, 10, 10, 10, 10]
print(multiply_lst(my_lst))
