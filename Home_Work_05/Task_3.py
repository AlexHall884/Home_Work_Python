# 3-Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, 
# состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: 
# если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, 
# то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. 
# Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком
# https://dzen.ru/media/simplichka/kak-tekst-hranitsia-v-kompiutere-chast-3-62d3d91515d67a522f78e1e6?&

languages = ['PHP', 'Python', 'Java', 'Swift', 'Go', 'Java-Script', 'C#', 'C++', 'Scratch']
print(languages)
numbers = [x for x in range(1, len(languages) +1 )]
print(numbers)

merge_lists = list(zip(numbers, [i.upper() for i in languages]))
print(merge_lists)

def filter_list(list_num_lang):
    result = []
    sum_ord = 0
    for num, lang in list_num_lang:
        for i in lang:
            sum_ord += ord(i)
        if sum_ord % num == 0:
            result.append((sum_ord, lang))
    return result

print(filter_list(merge_lists))