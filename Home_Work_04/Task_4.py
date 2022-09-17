# 4- Шифр Цезаря - это способ шифрования, 
# где каждая буква смещается на определенное количество 
# символов влево или вправо. При расшифровке происходит 
# обратная операция. К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. 
# "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, 
# а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.

import os
os.system('cls')
import Task_1

def chiper_Ceasar(input_string: str, key: int) -> str:
    '''
    Шифрует текст и записывает его в файл
    '''
    result = ''
    for i, symbol in enumerate(input_string):
        result += chr(ord(symbol) + key)
    with open('Ceasar.txt', 'w', encoding ='utf-8') as file:
            file.write(result)
    return result

def decoder(chiper_string: str, key: int) -> list:
    '''
    Считывает информацию из файла, декодирует её и записывает в строку
    '''
    with open('Ceasar.txt', 'r', encoding ='utf-8') as data:
        chiper_string = data.readline()
    result = []
    for i, symbol in enumerate(chiper_string):
        result += chr(ord(symbol) - key)           
    return result

print('Это программа позволит зашифровать текст с помощью шифра Цезаря')
print('Ключ - это сдивг в право или влево. Что бы сдвинуть в право введите положительное целое число, если в лево то отрицательное)')
chiper_key = Task_1.get_number('Введите ключ: ')
text = input('Введите текст: ')

ciphered_text = chiper_Ceasar(text, chiper_key)
print('Зашифрованный текст -> ', ciphered_text)
chiper_key = Task_1.get_number('Введите ключ: ')
deciphered_text = decoder(ciphered_text, chiper_key)
print('Расшифрованный текст -> ', ''.join(deciphered_text))