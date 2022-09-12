# 2-Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


list_number = [2, 3, 4, 5, 6]

def product_pairs_numbers_list(list_n: list) -> list:
    '''
    Находит произведение пар чисел списка
    '''
    list_result = []
    for i in range((len(list_n) + 1) // 2):
        list_result.append(list_n[i] * list_n[-i - 1])
    return list_result
        
                
print('Произведение пар чисел списка = ', product_pairs_numbers_list(list_number))
    