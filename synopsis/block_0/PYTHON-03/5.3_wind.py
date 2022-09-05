# У вас есть заготовка функции — def get_wind_class(speed):
# Вам нужно вместо "???" написать цикл, который возвращает из функции класс ветра в зависимости от его характера:
# от 1 до 4 м/с - "weak [1]"
# от 5-10 м/c - "moderate [2]"
# от 11-18 м/c - "strong [3]"
# от 19 м/c - "hurricane [4]"
# В последней строке мы просим программу напечатать результат (в зависимости от цифры в скобках) —
def get_wind_class(speed):  # Объявление функции
    if 1 <= speed <= 4:
        return "weak [1]"
    elif 5 <= speed <= 10:
        return "moderate [2]"
    elif 11 <= speed <= 18:
        return "strong [3]"
    else:
        return "hurricane [4]"

print(get_wind_class(3))  # Печатаем результат выполнения