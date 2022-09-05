import random
my_list = []
for i in range(0, 10):
    my_list.append(random.randint(0, 10))
sum_ = 0
i = 0
while sum_ < 10:
    sum_ += my_list[i]
    i += 1

print(*my_list)
print(sum_)

"""
Вывод программы:
1 8 6 7 2 5 10 7 4 10
15
"""