# 2 Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите). 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет(или сколько вы зададите). 
# Тот, кто берет последнюю конфету - проиграл.
# Предусмотрите последний ход, ибо там конфет остается меньше.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


import os
import random
from secrets import choice 
os.system('cls')

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

if __name__ == '__main__':
    
    def choice_game(num):
        while num != 1 and num != 2:
            num = abs(get_number('Выберете режим игры: для того что бы сразиться с человеком введите 1, что бы играть против бота введите 2 -> '))
        if num == 1:
            game_pvp(candy_on_table, max_candy)
        if num == 2:
            print('Против вас будет играть -> Бот-Антон')
            game_pve(candy_on_table, max_candy)
    
    def check_candy_total(input_string):
        while input_string > 10000 or input_string < 10:
            print('Мы ценим ваше время и хотим что бы игра была интересной, поэтому введите число не больше 10 000 и не меньше 10')
            input_string = abs(get_number('Введите общее кол-во конфет: '))
        print(f'На столе {input_string} конфет')
        return input_string
                
    def check_candy_max(input_string, candy):
        while input_string > candy / 2 or input_string == 1:
            print(f'Вы ввели слишком большое число, введите число не больше {candy / 2}')
            input_string = abs(get_number('Введите общее кол-во конфет: '))
        return input_string
    
    def check_string_empty(name):
        while name == '' or name == ' ':
            print('Вы ничего не ввели')
            name = input('Введите имя Игрока: ')
        return name 
    
    
    print('Добро пожаловать в игру!')
    print()
    print('🍬 <КОНФЕТА> 🍬')
    print()
    print('Правила просты: Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.')
    print('Тот, кто берет последнюю конфету - проиграл!')
    
    candy_on_table = check_candy_total(abs(get_number('Введите общее кол-во конфет: ')))
    max_candy = check_candy_max(abs(get_number('Определите сколько можно взять конфет за один ход: ')), candy_on_table)
    
    
    def check_input_player(input_string, max_candy):
        while input_string > max_candy or input_string < 1:
            print(f'Error! Введите число от 1 до {max_candy}')
            input_string = abs(get_number('сколько 🍬 конфет хотите взять?'))
        return input_string
    
    def game_pvp(total_candy, max_candy):
        player_1 = check_string_empty(input('Введите имя первого игрока: '))
        player_2 = check_string_empty(input('Введите имя второго игрока: '))
        players = [player_1, player_2]
        lottery = choice(players)
        
        if lottery == player_1:
            print('Один момент... Подбрасываем монетку... ')
            print()
            print(f'Жребий опредил, что Ходит: {player_1} -> ')
            print()
        else:
            print('Один момент... Подбрасываем монетку... ')
            print()
            print(f'Жребий опредил, что Ходит: {player_2} -> ')
            print()

        while total_candy > 1:
            if lottery == player_1:
                move = check_input_player(abs(get_number(f'< {lottery} > сколько конфет хотите взять? ')), max_candy)
                total_candy -= move
                print(f'Осталось {total_candy} 🍬 ')
                lottery = player_2
            else:
                move = check_input_player(abs(get_number(f'< {lottery} > сколько конфет хотите взять? ')), max_candy)
                total_candy -= move
                print(f'Осталось {total_candy} 🍬 ')
                lottery = player_1

        if lottery == player_1:
            print(f'{player_1} вы проиграли')
            print(f'Выиграл {player_2}, поздравляем!')
        else:
            print(f'{player_2} вы проиграли')
            print(f'Выиграл {player_1}, поздравляем!')
            

def game_pve(total_candy, max_candy):
    player_1 = check_string_empty(input('Введите имя игрока: '))
    player_2 = 'Бот Антон'
    players = [player_1, player_2]
    lottery = choice(players)

    if lottery == player_1:
        print('Один момент... Подбрасываем монетку... ')
        print()
        print(f'Жребий опредил, что Ходит: Игрок {player_1} -> ')
        print()
    else:
        print('Один момент... Подбрасываем монетку... ')
        print()
        print(f'Жребий опредил, что Ходит: {player_2} -> ')
        print()
        
    while total_candy > 1:
                if lottery == player_1:
                    move = check_input_player(abs(get_number(f'< {lottery} > сколько конфет хотите взять? ')), max_candy)
                    print(f'{lottery} взял {move} конфет')
                    total_candy -= move
                    print(f'Осталось {total_candy} 🍬 ')
                    lottery = player_2
                else:
                    if total_candy <= max_candy:
                        move = total_candy - 1
                        print(f'{lottery} взял {move} конфет')
                        total_candy -= move
                        print(f'Осталось {total_candy} 🍬 ')
                        lottery = player_1  
                    else:
                        move = max_candy
                        print(f'{lottery} взял {move} конфет')
                        total_candy -= move
                        print(f'Осталось {total_candy} 🍬 ')
                        lottery = player_1  
                    
    if lottery == player_1:
        print(f'{player_1} вы проиграли')
        print(f'Выиграл {player_2}')
    else:
        print(f'{player_2} вы проиграли')
        print(f'Выиграл {player_1}, поздравляем!')
        
choice_game('')