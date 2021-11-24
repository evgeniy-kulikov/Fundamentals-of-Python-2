""" Homework for the Lesson_07 """
""" Task 01 """

# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):  # формируем матрицу из вложенных списков чисел
        row_matrix = ''
        for i in range(len(self.matrix)):
            row_matrix = row_matrix + '\t'.join(map(str, self.matrix[i])) + '\n'
        return row_matrix

    def __add__(self, other):  # сложение сформированных матриц
        if len(self.matrix) != len(other.matrix):  # проверка на одинаковую размерность матриц
            return f'Матрицы отличаются размерностью'
        res = self.matrix
        for i in range(len(self.matrix)):
            for k in range(len(self.matrix[i])):
                res[i][k] = self.matrix[i][k] + other.matrix[i][k]
        return Matrix(res)


l1 = [[1, 2, 4], [3, 4, 5], [5, 6, 6]]
l2 = [[11, 21, 41], [31, 41, 51], [51, 61, 61]]
mtr_1 = Matrix(l1)
mtr_2 = Matrix(l2)
print(f'{mtr_1}\t+')
print(mtr_2)
print('\t=\n')
result = mtr_1 + mtr_2
print(result)
