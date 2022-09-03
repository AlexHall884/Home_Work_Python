# 4- Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

def find_range():
    number_quarter = int(input('Введите номер четверти (1-4): '))
    
    while number_quarter < 1 or number_quarter >= 5:
        number_quarter = int(input('Введите номер четверти (1-4): '))
    
    if number_quarter == 1:
        return print('по X все положительные, по Y все положительные')
    elif number_quarter == 2:
        return print('по X все отрицательные, по Y все положительные')
    elif number_quarter == 3:
        return print('по X все отрицательные, по Y все отрицательные')
    else:
        return print('по X все положительные, по Y все все отрицательные')


find_range()