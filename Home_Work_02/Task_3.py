# 3 - Палиндромом называется слово, 
# которое в обе стороны читается одинаково: "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, 
# чтобы число в обе стороны читалось одинаково, но есть одно "но".
# Если перевернутое число не равно исходному, 
# то они складываются и проверяются на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, 
# которая найдет палиндром введенного пользователем числа.

def number():
    while True:
        try:
            num = int(input('Введите целое, положительное число: '))
            if num > 0:
             return num 
        except(ValueError):
            print('Error: Попробуйте ещё раз')

n = number()

def revers_digit(num):
    num_revers = 0
    while num != 0:
        digit = num % 10
        num = num // 10
        num_revers *=  10
        num_revers += digit
    return num_revers  

r = revers_digit(n)

def is_palindrom(num, rev):
    if num == rev:
        return num
    else:
        return revers_digit(num + rev)
            
print('Палиндром',n, ' = ', is_palindrom(n, r))