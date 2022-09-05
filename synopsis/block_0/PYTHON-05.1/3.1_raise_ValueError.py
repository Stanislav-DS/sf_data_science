def get_time(distance, speed):
    # Если расстояние или скорость отрицательные, то возвращаем ошибку
    if distance < 0 or speed < 0:
        # Оператор raise возвращает (raise — дословно англ. "поднимать")
        # объект-исключение. В данном случае ValueError (некорректное значение).
        # Дополнительно в скобках после слова ValueError пишем текст сообщения
        # об ошибке, чтобы сразу было понятно, чем вызвана ошибка.
        raise ValueError("Distance or speed cannot be below 0!")
    elif speed == 0:
        raise ValueError("Speed cannot be equal to 0!")
    result = distance / speed
    return result


try:
    print(get_time(100, 0))
except ValueError as e:
    print(e)
