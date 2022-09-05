def inf_iter(lst):
    while True:
        for elem in lst:
            yield elem

lst = [101, 102, 103]
gen = inf_iter(lst)
for _ in range(10):
    print(next(gen))