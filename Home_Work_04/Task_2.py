# 2 - Задайте последовательность чисел. 
# Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности. 
# Не использовать множества.
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

import os
import random
os.system('cls')

import Task_1 

number_n = abs(Task_1.get_number('Введите число: '))

def get_list_random(num: int) -> list:
    '''
    Принимает число 'num' и содаёт список равный этому числу 'num', в диапозоне от '0' до 'num'
    '''
    list_element = []
    for i in range(num):
        list_element.append(random.randint(0, num))
    return list_element

my_list = get_list_random(number_n)
print(f'Исходный список ->  {my_list}')

def uniq_list(list_n: list) -> list:
    '''
    Создаёт список из неповторяющихся элементов исходного спсика
    '''
    result_list = [] # создаём пустой список, в который запишим изменения
    for i in list_n: # запускаем цикл по нашему исходному списку
        if i not in result_list: # добавляем условие: если такого значения нет во втором списке, то добовлем его
            result_list.append(i)
    return result_list # возвращаем список с уникальными значениями

result = uniq_list(my_list)
print(f'Cписок из неповторяющихся элементов исходной последовательности -> {result}')
            

# list1 = [2, 3, 3, 3, 6, 2, 8, 8] 
# list2 = [] 
# for i in list1: 
#     if i not in list2: 
#         list2.append(i) 
# print(list2)
