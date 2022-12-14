"""Использован шаблои из модуля1 и добавлена оптимизация поиска путем изменения диапозона
в зависимости от того, больше или мешье неверные варианты относительно загаданного числа"""

import numpy as np
def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0
    min_lim=1 #начальный нижний предел поиска
    max_lim=101 #начальный верхний предел поиска
    while True:
        count += 1 
        predict_number = np.random.randint(min_lim, max_lim) # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
        
        elif number < predict_number: #Для оптимищзации поиска добавляем два условия elif
            max_lim = predict_number+1 #уменьшаем верхний предел поиска
        elif number > predict_number:   
            min_lim = predict_number #увеличиваем нижний предел поиска
            
    return(count)

print(f'Количество попыток: {random_predict()}')

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

score_game(random_predict)