def get_length(elem):
    return len(elem)


new_list = ['bbb', 'ababa','aaa', 'aaaaa',  'cc']
new_list.sort(key=get_length)
print(new_list)
# Должно быть напечатано:
# ['cc', 'bbb', 'aaa', 'ababa', 'aaaaa']


'''
Вывод программы:
['cc', 'bbb', 'aaa', 'ababa', 'aaaaa']
'''