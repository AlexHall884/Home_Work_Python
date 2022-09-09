# 1 - Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр. 
# Учтите, что числа могут быть отрицательными
# Пример:
# 67.82 -> 23
# 0.56 -> 11

def number():
    while True:
        try:
            num = float(input('Введите число: '))
            return num
        except(ValueError):
            print('Вы ввели не число')

num = str(number()) 
suma = 0
for digit in num:
    if digit.isdigit():
        suma += int(digit)
       
print("Сумма цифр равно:", suma)
