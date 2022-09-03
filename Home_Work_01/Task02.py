# 2-Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. 
# Предикату можно заменить на понятие "бит".
# Должна получиться таблица истинности.

def truth_table():
    print('Таблица истинности для вырожения: ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
    print('| x | y | z | result|')
    print('---------------------')
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if not(x or y or z) == (not x and not y and not z):
                    print(f'| {x} | {y} | {z} | ', True,'|')
                else:
                    print(f'| {x} | {y} | {z} | ', False,'|')

truth_table()    