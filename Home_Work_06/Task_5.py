# С помощью использования лямбд, filter, map, zip, enumerate, list comprehension, reduce**

# 5- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.

# list_number = [2, 3, 4, 5, 6]

# def product_pairs_numbers_list(list_n: list) -> list:
#     '''
#     Находит произведение пар чисел списка
#     '''
#     list_result = []
#     for i in range((len(list_n) + 1) // 2):
#         list_result.append(list_n[i] * list_n[-i - 1])
#     return list_result
        
                
# print('Произведение пар чисел списка = ', product_pairs_numbers_list(list_number))

import Func 

number_n = abs(Func.get_number('Введите длинну списка: '))
list_number = Func.get_list_random(number_n)
print(list_number)

result = [list_number[i] * list_number[-i - 1] 
          for i in range((len(list_number) + 1) // 2)] 
print(result)