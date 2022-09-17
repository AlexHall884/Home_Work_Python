# 3 - В файле, содержащем фамилии студентов и их оценки, 
# изменить на прописные буквы фамилии тех студентов, 
# которые имеют средний балл более «4».
# Пример:
# Волков Андрей 5
# Наталья Тарасова 5
# Фредди Меркури 3
# Денис Байцуров 4

# Программа выдаст:
# ВОЛКОВ АНДРЕЙ 5
# НАТАЛЬЯ ТАРАСОВА 5
# Фредди Меркури 3
# Денис Байцуров 4

import os
os.system('cls')
import Task_1

def add_to_file(num: int): 
    '''
    Добавляет в файл информацию введённую пользователем
    '''
    for i in range(num):
        with open('file.txt', 'a', encoding ='utf-8') as file:
            file.write(input('Введите имя ученика и его оценку через пробел: ' + '\n'))
            file.write('\n')
             
def read_file(student_list: list) -> list:
    '''
    Считывает информацию из файла и записывает её в список
    '''
    with open('file.txt', 'r', encoding ='utf-8') as data:
        for line in data:
            if line != '\n':
                student_list.append(line)
    return student_list

def find_exellent_students(student_list: list) -> list:
    '''
    Меняет на прописные буквы Имена и Фамилии тех студентов у которых оценка 5
    '''
    for i in student_list:
        if '5' in i:
            student_list = [elem.replace(i, i.upper()) for elem in student_list]
    return student_list
        
def write_file(student_list: list):
    '''
    Записывает информацию из списка в файл
    '''    
    with open('file.txt', 'w', encoding ='utf-8') as file:
        for i in student_list:
            file.write(i)

number_n = abs(Task_1.get_number('Введите кол-во учеников, которых хотите записать: '))
add_to_file(number_n)  
list_journal = []
list_journal = read_file(list_journal)
list_journal = find_exellent_students(list_journal)       
write_file(list_journal)    
    

        
        

    

