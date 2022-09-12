# 5-Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# [Негафибоначчи](https://clck.ru/yWbkX.)


def number():
    while True:
        try:
            num = abs(int(input('Введите число: ')))
            if num !=0:
             return num
        except(ValueError):
            print('Вы ввели не число')

input_number = number()

def get_list_fibonaci(num: int) -> list:
    '''
    Создаёт список чисел Фибоначчи
    '''
    fib1, fib2 = 1, 1
    i = 0
    list_fibo = [fib1, fib2]
    while i < num - 2:
        list_fibo.append(list_fibo[i] + fib2)
        fib2 = fib1 + fib2
        fib1 = fib2 - fib1
        i += 1
    return list_fibo

fibonaci = get_list_fibonaci(input_number)

def get_list_negofibonaci(num: int) -> list:
    '''
    Создаёт список чисел негаФибоначчи
    '''
    fib1 = 0
    fib2 = 1
    i = 0
    list_nego_fibo = [fib1, fib2]
    while i < num -1:
        list_nego_fibo.append(list_nego_fibo[i] + ((-1)**(i + 1) * fib2))
        fib2 = fib1 + fib2
        fib1 = fib2 - fib1
        i += 1
    return list_nego_fibo

nego_fibo = get_list_negofibonaci(input_number)
nego_fibo.reverse()

list_result = nego_fibo + fibonaci
print(list_result)        