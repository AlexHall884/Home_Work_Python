# 1-Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

# *Пример:*

# - 6 -> да
# - 7 -> да
# - 1 -> нет

def check_the_day():
    day = int(input('Введите число от (1-7) обозначающую день недели: '))
    while day < 1 or day >= 8:
        day = int(input('Введите число от 1 до 7: '))
    if day > 5 and day < 7:
        return print('Этот день выходной')
    else:
        return print('Этот день рабочий')
        
check_the_day()        