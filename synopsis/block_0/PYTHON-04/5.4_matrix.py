str_list = ['Hello', 'my', 'name', 'is', 'Ezeikel', 'I', 'like', 'knitting']
cut_str_list = []
for i, elem in enumerate(str_list):
    cut_str_list.append([i, elem[:3]])

"""
Вывод программы:
[[0, 'Hel'], [1, 'my'], [2, 'nam'], [3, 'is'], [4, 'Eze'], [5, 'I'], [6, 'lik'], [7, 'kni']]
"""