# 3- Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
# *Пример:*
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def find_a_quarter():
    x_coordinates = int(input('Введите координаты X : '))
    y_coordinates = int(input('Введите координаты Y : '))
    
    while x_coordinates == 0 or y_coordinates == 0:
        print('X и Y не должны быть равны 0 ')
        x_coordinates = int(input('Введите координаты X : '))
        y_coordinates = int(input('Введите координаты Y : '))   
        
    if x_coordinates > 0 and y_coordinates > 0:
        return print('Это 1 четверть')
    elif x_coordinates < 0 and y_coordinates > 0:
        return print('Это 2 четверть')
    elif x_coordinates < 0 and y_coordinates < 0:
        return print('Это 3 четверть')
    else:
        return print('Это 4 четверть')
    
find_a_quarter()    
    