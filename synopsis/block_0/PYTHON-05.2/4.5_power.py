def power(val, n):
    if n == 0:
        return 1
    if n == 1:
        return val
    return val * power(val, n - 1)
