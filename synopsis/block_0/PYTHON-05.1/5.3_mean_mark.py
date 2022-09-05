marks = [4, 5, 5, 5, 5, 3, 4, 4, 5, 4, 5]


def mean_mark(name, *args):
    result = sum(args) / len(args)
    # Не возвращаем результат, а печатаем его
    print(name+':', result)


mean_mark('Kuznetsov', *marks)

'''
Вывод программы
Kuznetsov: 4.454545454545454
'''