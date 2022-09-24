# С помощью использования лямбд, filter, map, zip, enumerate, list comprehension, reduce**
# 4- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

my_list = ["qwe", "asd", "zxc", "qwe", "ertqwe", "asd"]
search_word = "2"

search_result = list([(i, c) for i, c in enumerate(my_list) if c == search_word])
if len(search_result) > 1:
    print(f'Второе вхождение строки "{search_word}" = {search_result[1][0]}')
else:
    print(f'Второго вхождения строки "{search_word}" нет')
