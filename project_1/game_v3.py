"""Игра. Угадывает число не больше чем за 20 попыток."""

from numpy import random, mean


def guess_number(number: int = 1) -> int:
    """Угадывает число не более чем за 20 попыток.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Количество попыток
    """

    # количество попыток
    count = 0
    # нижняя и верхняя границы "диапазона угадывания"
    # (lower bound and upper bound)
    l_bound, u_bound = 1, 101

    while True:
        count += 1
        if (answer := l_bound + (u_bound - l_bound)//2) == number:
            return count
        l_bound, u_bound = ((answer, u_bound) if answer < number else
                            (l_bound, answer))


def score_game(random_predict) -> int:
    """Среднее количество попыток, за которое функция
    угадывает число от 1 до 100. Определяется за 1000 вызовов функции.

    Args:
        random_predict (function): функция, которая угадывает число.

    Returns:
        int: среднее количество попыток
    """

    random.seed()
    random_array = random.randint(1, 101, size=1000)
    score = [random_predict(number) for number in random_array]
    score = mean(score)
    score = int(round(score, 0))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


# RUN
if __name__ == '__main__':
    score_game(guess_number)
