# С помощью использования лямбд, filter, map, zip, enumerate, list comprehension, reduce**

# 1- Определить, присутствует ли в заданном списке строк, некоторое число
import Func

number = Func.get_number('Введите число, которое хотите найти в списке: ')
my_list = [n for x in 
           ['0.5 кг муки', '200 грамм масла', '100 грамм сахара', '2 щепотки соли', '3 яйца'] 
           for n in x if n == str(number)]
result = lambda my_list: f'Элемент <{number}> в спсике найден' if my_list else f'элемента <{number}> нет в списке'

print(result(my_list))

