import random
my_list = []
for i in range(0, 10):
    my_list.append(random.randint(0, 10))
print(*my_list)
for num in my_list:
    if my_list.count(num) > 1:
        print('Yes')
        break

        
"""
Вывод программы
7 2 5 9 6 8 5 10 0 3
Yes
"""