"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""
import math

import numpy as np
import math as mt

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """


    count = 0
    # выставляем дефолтные значение при сете выбора от 1 до 100
    h_bound = 100
    l_bound = 0
    while True:
        count += 1
        predict_number = (h_bound+l_bound)//2
        if predict_number > number:
            h_bound = predict_number
            predict_number = (h_bound+l_bound)//2
        elif predict_number < number:
            l_bound = predict_number
            predict_number = (h_bound+l_bound)//2
        elif number == predict_number:
            break  # выход из цикла если угадали
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
