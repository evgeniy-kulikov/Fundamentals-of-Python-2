"""Homework for the Lesson_02"""

""" Task 4 """
#  4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
#  Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

user_str = input('Введите строку из нескольких слов, разделённых пробелами: ')
sep_word = []
for i in range(user_str.count(' ') + 1):
    sep_word = user_str.split()
for ind, el in enumerate(sep_word):
    print(ind, el[:10])
