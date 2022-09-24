# С помощью использования лямбд, filter, map, zip, enumerate, list comprehension, reduce**

# 2- Найти сумму чисел списка стоящих на нечетной позиции

# list_number = [2, 3, 5, 9, 3]

# def find_sum_odd_index(list_n: list) -> int:
#     '''
#     находит сумму элементов с нечётными индексами
#     '''
#     sum_odd_index = 0
#     for i in range(len(list_n)):
#         if i % 2 != 0:
#             sum_odd_index += list_n[i]
#         i += 1
#     return sum_odd_index

# print('Сумма  элементов списка, стоящих на нечётной позиции = ', find_sum_odd_index(list_number))

import Func 

number_n = abs(Func.get_number('Введите длинну списка: '))
list_number = Func.get_list_random(number_n)
print(list_number)

sum_odd_index = sum([item for index, item in enumerate(list_number) if index % 2 ])
print('Сумма  элементов списка, стоящих на нечётной позиции = ', sum_odd_index)