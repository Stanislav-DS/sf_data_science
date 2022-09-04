"""Игра угадывает число не больше чем за 20 попыток."""

import numpy as np


def guess_number(number:int=1) -> int:
    """Угадывает число не более чем за 20 попыток.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Количество попыток
    """
    
    # количество попыток
    count = 0
    # границы "диапазона угадывания"
    low_board = 1
    high_board = 101
    
    while True:
        count += 1
        if (answer := low_board + (high_board - low_board)//2) == number:
            return count
        low_board, high_board = ((answer, high_board) if answer < number else 
                                 (low_board, answer))
         
        count += 1
        if (answer := np.random.randint(low_board, high_board)) == number:
            return count
        low_board, high_board = ((answer, high_board) if answer < number else 
                                 (low_board, answer))
        
    
        
        


def score_game(random_predict) -> int:
    """Среднее количество попыток, за которое функция угадывает число от 1 до 100.
    Определяется за 1000 вызовов функции.

    Args:
        random_predict (function): функция, которая угадывает число.

    Returns:
        int: среднее количество попыток 
    """
    
    np.random.seed()
    random_array = np.random.randint(1, 101, size=1000)
    score = int(np.mean([random_predict(number) for number in random_array]))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


# RUN 
if __name__ == '__main__':
    score_game(guess_number)