def sort_ignore_case(ls):
    ls.sort(key=lambda el: el.lower())
    return ls


print(sort_ignore_case(['Acc', 'abc']))
