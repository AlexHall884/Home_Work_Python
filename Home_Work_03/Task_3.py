# 3-Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
#  - [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91

list_numbers = [1.1, 1.2, 3.1, 5.17, 10.02]

def get_list_fractional_part (list_n: list) -> list:
    '''
    Создаёт список только из дробной части переданного СПИСКА
    '''
    list_result = []
    for i in range(len(list_n)):
        list_result.append(round(list_n[i] % 1, 2))
    return list_result


print(f'Дробная часть чисел из списка {list_numbers} = { get_list_fractional_part(list_numbers)}')
print(f'Разница между максимальным и минимальным значением дробной части элементов = {round(max(get_list_fractional_part(list_numbers)) - min(get_list_fractional_part(list_numbers)), 2)}')