# 1 - Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

import os
os.system('cls')

def get_number(string_input: str) -> int:
    '''
    Проверяет ввёл ли пользователь целое число
    '''
    while True:
        try:
            num = int(input(string_input))
            if num !=0:
             return num
        except(ValueError):
            print('Вы ввели не число')

if __name__ == '__main__':
        
    number_n = abs(get_number('Введите целое число: '))

    def number_factorization(num: int) -> list:
        '''
        Раскладывает число но простые множетели (производит факторизацию)
        '''
        list_result = [] # создаём пустой список 
        simple = 2 # берём наменьшее просте число
        while num > 1: # запускаем цикл: пока 'num' будет больше единицы (минимальное простое число = 2)
            if num % simple == 0: # добовляем условие: если 'num' поделенное с остатком на 'simple' будет равно нулю
                list_result.append(simple)# добовляем 'simple' в конец списка
                num /= simple # 'num' делим на 'simple' и переходим к следующему множетелю
            else:
                simple += 1 # если деление с остатком даёт больше нуля, то увелиим 'simple' на 1 
        return list_result # возвращаем список

    result = number_factorization(number_n)

    print(f'Список простых множетелей {number_n} -> {result}')

