def get_less(args, num):
    for arg in args:
        if arg < num:
            return arg


l = [1, 5, 8, 10]
print(get_less(l, 0))
