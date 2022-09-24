# С помощью использования лямбд, filter, map, zip, enumerate, list comprehension, reduce**
# 6-Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

# for i in range(number_n):
#     print((-3) ** i, end=', ')      

import Func

number_n = abs(Func.get_number('Введите N: '))

result = [(-3) ** i for i in range(number_n)]

print(result)