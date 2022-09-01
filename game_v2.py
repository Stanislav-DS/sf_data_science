"""Игра угадай число
Компьютер сам загаывает и сам угадывает."""

import numpy as np


def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Количество попыток
    """
    
    count = 0
    
    while True:
        count += 1
        if np.random.randint(1, 101) == number:
            return count


def score_game(random_predict) -> int:
    """Среднее количество попыток, за которое функция угадывает число от 1 до 100.
    Определяется за 1000 вызовов функции.

    Args:
        random_predict (function): функция, которая угадывает число.

    Returns:
        int: среднее количество попыток 
    """
    
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=1000)
    score = int(np.mean([random_predict(number) for number in random_array]))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


# RUN 
if __name__ == '__main__':
    score_game(random_predict)