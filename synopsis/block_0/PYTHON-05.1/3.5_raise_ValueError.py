def add_mark(name, mark, journal=None):
    # Добавьте здесь проверку аргумента mark
    if journal is None:
        journal = {}
    if mark not in [2, 3, 4, 5]:
        raise ValueError("Invalid Mark!")
    journal[name] = mark
    return journal


# попытка вызвать функцию с некорректными аргументами
try:
    print(add_mark('Ivanov', 6))
# должна завершиться с ошибкой ValueError, которую мы выведем в блоке except
except ValueError as e:
    print(e)