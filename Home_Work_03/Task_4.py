# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def number():
    while True:
        try:
            num = abs(int(input('Введите число: ')))
            if num !=0:
             return num
        except(ValueError):
            print('Вы ввели не число')
input_number = number()

def convert_to_bin(num: int) -> str:
    '''
    Преобразовывает десятичное число в двоичное
    '''
    result = ''
    while num > 0:
        result = str(num % 2) + result
        num = num // 2
    return result

print(f'Число {input_number} в двоичной системе будет выглядить так: {convert_to_bin(input_number)}')