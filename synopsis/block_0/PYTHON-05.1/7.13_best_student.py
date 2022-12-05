# def best_student(**kwargs):
#     rating = []
#     for name, i in kwargs.items():
#         rating.append([i, name])
#     rating.sort()
#     return rating[0][1]


# def best_student(**kwargs):
#     return sorted(
#         [[place, name] for name, place in kwargs.items()]
#         )[0][1]


# def best_student(**kwargs):
#   return dict(
#       [(value, key) for key, value in kwargs.items()]
#       )[min(kwargs.values())]


# def best_student(**kwargs):
#   return {
#       value: key for key, value in kwargs.items()
#       }[min(kwargs.values())]


# def best_student(**kwargs):
#     return min(kwargs, key=kwargs.get)


best_student = lambda **k: min(k, key=k.get)

print(best_student(Tom=-20, Jerry=1, Jane=-10)) 




