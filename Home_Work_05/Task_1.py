# 1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"
import os
os.system('cls')

# text = 'абвгдейка - это передача' # обычное решение
# text_list = text.split(' ')
# print(text_list)
# new_text = []
# for word in text_list:
#      if 'абв' not in word:
#          new_text.append(word)

# print(' '.join(new_text))


text = 'абвгдейка сезам - это абв передача'
new_text = ' '.join(list(filter(lambda x: not 'абв' in x, text.split(' ')))) # решение в одну строку
print(new_text)
