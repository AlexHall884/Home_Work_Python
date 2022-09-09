# 4 - Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime 
# (миллисекунды или наносекунды) - для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)

import datetime

def number(input_string):
    while True:
        try:
            num = int(input(input_string))
            return num 
        except(ValueError):
            print('Error: Попробуйте ещё раз')

def random_number(min, max):
    num = int(datetime.datetime.now().strftime('%f')) / 1000000
    num = int(num * (max - min) + min)
    return num

min_n = number('Введите нижнюю границу: ')
max_n = number('Введите верхнюю границу: ')
random_num = random_number(min_n, max_n)

print('Случайное число от ', min_n, ' до ', max_n, ' = ', random_num )