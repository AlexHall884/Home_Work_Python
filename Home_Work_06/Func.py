import random

def get_number(string_input: str) -> int:
    '''
    Проверяет ввёл ли пользователь целое число
    '''
    while True:
        try:
            num = int(input(string_input))
            if num !=0:
             return num
        except(ValueError):
            print('Вы ввели не число')


            
def get_list_random(num: int) -> list:
    '''
    Принимает число 'num' и содаёт список равный этому числу 'num', в диапозоне от '0' до 'num'
    '''
    list_element = []
    for i in range(num):
        list_element.append(random.randint(0, num))
    return list_element