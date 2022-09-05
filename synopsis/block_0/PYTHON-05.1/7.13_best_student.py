def best_student(**kwargs):
    rating = []
    for name, i in kwargs.items():
        rating.append([i, name])
    rating.sort()
    return rating[0][1]


print(best_student(Tom=12, Jerry=1, Jane=2))