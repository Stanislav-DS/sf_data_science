def mult(*args):
    res = 1
    for n in args:
        res *= n
    return res


print(mult(3, 5, 10))
