import math
import numpy
import os

# Вывод мануала.
def print_man():
    os.system('cls')
    print('\033[92m{}\033[0m'.format('РУКОВОДСТВО ПО ИСПОЛЬЗОВАНИЮ\n\n') + 
        'Программа реализует метод анализа иерархий Томаса Саати для одного уровня.\n' +
        'Пользователь вводит целочисленные данные для заполнения единичной матрицы с \n' +
        'одной стороны от диагонали, другая сторона зеркалится в виде 1 / x.\n' +
        'x — число введенное пользователем.\n' +
        'На основании введенных данных выводятся весовые коэффициенты для каждого критерия.\n')

# Вывод результатов.
def print_results(coeffs):
    os.system('cls')
    print('\033[92m{}\033[0m'.format('ВЕСОВЫЕ КОЭФФИЦИЕНТЫ ДЛЯ КАЖДОГО КРИТЕРИЯ\n'))
    for i in range(len(coeffs)):
        print(f'Весовой коэффициент для {i + 1}-го критерия: {coeffs[i]}')

# Ввод числа с проверкой на корректность.
def input_num(msg, min=None):
    while True:
        try:
            num = int(input(msg + ': '))
        except:
            print('\033[31m{}\033[0m'.format('Invalid value. Try again...'))
            continue

        if min != None and num < min:
            print('\033[31m{}\033[0m'.format(f'Value must be greater than {min}! Try again...'))
            continue
        return num

print_man()
count = input_num('Введите количество критериев', min=2)

# Строим единичную матрицу.
matrix = numpy.eye(count)

# Выше диагонали пользователь заполняет критерии самостоятельно,
# ниже значения зеркалятся и записываются в виде 1 / x.
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        if matrix[i, j] == 1:
            break
        matrix[i, j] = input_num(f'Введите результат сравнения 2-х критериев по важности для ячейки [{i + 1}][{j + 1}]')
        matrix[j, i] = matrix[0, 0] / matrix[i, j]

mults = []
for vector in matrix:
    # Перемножение чисел в векторе.
    multiLine = vector.prod()
    # Нахождение корня произведений всех чисел строки.
    mults.append(math.pow(multiLine, 1 / count))

# Сумма всех перемножений.
sumAllMult = numpy.array(mults).sum()

# Рассчет весовых коэф-ов.
coeffs = [round(mults[i] / sumAllMult, 2) for i in range(len(mults))]

# Вывод результатов.
print_results(coeffs)

