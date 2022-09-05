my_dict = {'a': 15, 'b': 10.5, 'c': '15', 'd': 50, 'e': 15, 'f': '15'}
n_num = 0
for dict_id in my_dict:
    if type(my_dict[dict_id]) == str:
        continue
    n_num += 1
print(n_num)


# 4