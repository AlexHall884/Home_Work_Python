# С помощью использования лямбд, filter, map, zip, enumerate, list comprehension, reduce**

# 3- Найти расстояние между двумя точками пространства(числа вводятся через пробел)

import math

def get_coordinate(input_string: str) -> list:
    '''
    Получает координаты двух точек и создаёт из них список чисел
    '''
    coordinate = [int(x) for x in input_string.split()]
    return coordinate
    # print('Расстояние между точками = ', round(math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2)), 3))
   
coordinat_point = get_coordinate(input('Введите координаты двух точек через пробел: '))
distance_between_points = lambda x1, y1, x2, y2: round(math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2)), 2)
print('Расстояние между точками = ', distance_between_points(coordinat_point[0], 
                                                             coordinat_point[1], coordinat_point[2], coordinat_point[3]))