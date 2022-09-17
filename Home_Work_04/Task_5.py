# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия 
# и восстановления данных. Входные и выходные данные 
# хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# сжатый текст.
import os
os.system('cls')

def write_file(input_string: str):
    '''
    Записывает информацию в файл
    '''
    with open('RLE_input_data.txt', 'w', encoding ='utf-8') as file:
                file.write(input_string)
            
def RLE_encoding(string: str) -> str:
    '''
    Кодирует данные и записывает их в файл
    '''
    i = 0
    compressed = ''
    while i < len(string):
        count = 1
        while i + 1 < len(string) and string[i] == string[i + 1]:
            count = count + 1
            i = i + 1
        if count == 1:    # это условие позволет избавиться от '1'
            compressed += string[i]
            i = i + 1
        else:
            compressed += str(count) + string[i]
            i = i + 1
    with open('RLE_output_data.txt', 'w', encoding ='utf-8') as file:
                file.write(compressed)
    return compressed

def data_decoding(encoding_data: str) -> str:
    '''
    Раскодирует данные и возвращает строку
    '''
    data = ''
    count = ''
    for char in encoding_data: 
            if char.isdigit(): 
                count += char 
            else:  
                if not count:
                    count = 1
                data += char * int(count) 
                count = '' 
    return data

input_data = input('Введите данные: ')
write_file(input_data)
compressed_data = RLE_encoding(input_data)
output_data = data_decoding(compressed_data)
print('Исходные данные ->', input_data)
print('Закодированные данные -> ', compressed_data)
print('Раскодировнные данные -> ', output_data)