# 2 - Напишите программу, которая принимает на вход число N 
# и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def number():
    while True:
        try:
            num = abs(int(input('Введите число: ')))
            if num !=0:
             return num
        except(ValueError):
            print('Вы ввели не число')

number_n = number()
mult = 1
i = 1
factorial = []
while i <= number_n:
    mult *= i
    factorial.append(mult)
    i += 1
    
print('Факториал', number_n, ' = ', factorial)    
