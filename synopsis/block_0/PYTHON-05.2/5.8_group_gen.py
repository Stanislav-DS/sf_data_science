def group_gen(n):
    while True:
        for i in range(1, n + 1):
             yield i


groups = group_gen(3)
for _ in range(10):
    print(next(groups))
# 1
# 2
# 3
# 1
# 2
# 3
# 1
# 2
# 3
# 1