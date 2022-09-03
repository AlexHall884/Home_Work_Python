# 5-Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# *Пример:*
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


import math


def find_distance_between_points():
    print('Введите координаты первой точки: ')
    x1 = int(input('X:'))
    y1 = int(input('Y:'))
    
    print('Введите координаты второй точки: ')
    x2 = int(input('X:'))
    y2 = int(input('Y:'))
    result = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)
    print('Расстояние между точками = ', round(math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2)), 3))
    
find_distance_between_points()    