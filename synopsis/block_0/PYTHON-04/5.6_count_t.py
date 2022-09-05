str_list = ['text', 'morning', 'notepad', 'television', 'ornament']
symbol_to_check = 't'
words_dict = {}
for word in str_list:
    count_t = 0
    for symbol in word:
        if symbol == symbol_to_check:
            count_t += 1
    words_dict[word] = count_t


"""
Вывод программы
{'text': 2, 'morning': 0, 'notepad': 1, 'television': 1, 'ornament': 1}
"""