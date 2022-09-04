# Проект 1. Угадай число

## Оглавление

1. [Описание проекта.](https://github.com/Stanislav-DS/sf_data_science/blob/main/project_1/README.md#Описание-проекта)

1. [Проектный кейс.](https://github.com/Stanislav-DS/sf_data_science/blob/main/project_1/README.md#Проектный-кейс)

1. [Результат.](https://github.com/Stanislav-DS/sf_data_science/blob/main/project_1/README.md#Результат)

1. [Выводы.](https://github.com/Stanislav-DS/sf_data_science/blob/main/project_1/README.md#Выводы)

### Описание проекта
Программа угадывает рандомное число не больше чем за 20 попыток.


⬆️[к оглавлению](https://github.com/Stanislav-DS/sf_data_science/blob/main/project_1/README.md#Оглавление)

### Проектный кейс

**Условие задачи**

*   Компьютер загадывает целое число от 1 до 100, и нам его нужно угадать. Под «угадать» подразумевается «написать программу, которая угадывает число».
*  Алгоритм учитывает информацию о том, больше или меньше случайное число нужного нам числа.

**Метрика качества**

Результаты оцениваются по среднему количеству попыток при 1000 повторений. Необходимо добиться минимального количества попыток.

Код должен быть воспроизводим, соответствовать PEP8, его необхомо выгрузить на надлежащим образом оформленный репозиторий GitHub. 

**Что практикуем**
*  Учимся писать хороший код на Python.
*  Учимся работать с IDE.
*  Учимся работать с GitHub.

**Эталонное решение**

*  Шаблон [baseline](https://colab.research.google.com/drive/1k2WZD8PWWOYFHrpAJoB2eZw06ID7KnFA) из скринкаста.
*  [Архив](https://lms.skillfactory.ru/assets/courseware/v1/f2a8fb0bf139c619f6b6d705f330e0ea/asset-v1:SkillFactory+DSPR-2.0+14JULY2021+type@asset+block/guess-number-task.zip) с базовым решением задачи.


⬆️[к оглавлению](https://github.com/Stanislav-DS/sf_data_science/blob/main/project_1/README.md#Оглавление)

### РЕЗУЛЬТАТ

Программа угадывает число в среднем за 6 попыток.

Код и описание алгоритма решения загружены на [GitHub](https://github.com/Stanislav-DS/sf_data_science/tree/main/project_1), обеспечена воспроизводимость кода:

*   [game_v3.py](https://github.com/Stanislav-DS/sf_data_science/blob/main/project_1/game_v3.py) - код (функции `guess_number` и `score_game`);
*   [game.ipynb](https://github.com/Stanislav-DS/sf_data_science/blob/main/project_1/game.ipynb) - описание алгоритма и демонстрация результатов работы программы;
*   [requirements.txt](https://github.com/Stanislav-DS/sf_data_science/blob/main/project_1/requirements.txt) - актульные версии библиотек на момент написания программы.

⬆️[к оглавлению](https://github.com/Stanislav-DS/sf_data_science/blob/main/project_1/README.md#Оглавление)

### ВЫВОДЫ

**Проблемные моменты**

Необходимо более детально разобраться в способах манипулирования ветвями Git, в т.ч. в алгоритме слияния двух ветвей удаленного и локального репозиториев с несвязанной историей.

**Полезный опыт**

Для проверки кода на соответствие PEP8 удобно использовать т.н. линтеры:
* [flake8](https://flake8.pycqa.org/en/latest/)
* [pylint](https://www.pylint.org/)


⬆️[к оглавлению](https://github.com/Stanislav-DS/sf_data_science/blob/main/project_1/README.md#Оглавление)