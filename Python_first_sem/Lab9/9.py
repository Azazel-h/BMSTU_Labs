# Ввести трёхмерный массив (массив матриц размера X*Y*Z), вывести из него i-й
# срез по второму индексу.
# Булгаков Арсений Сергеевич ИУ7-16Б

# Импортируем самописные функции проверки и создания матрицы по формуле
from Functions import *

print('Введите размерность трехмерного массива')

# Вводим размерность матрицы
y = validation(input('Y: '), int)
while not y: # Пока проверка не проходит
    print(f'Ошибка! - Введите значение типа {int}')
    y = validation(input('Y: '), int) # Повторно просим ввод

# Вводим размерность матрицы
x = validation(input('X: '), int)
while not x: # Пока проверка не проходит
    print(f'Ошибка! - Введите значение типа {int}')
    x = validation(input('X: '), int) # Повторно просим ввод

# Вводим размерность матрицы
z = validation(input('Z: '), int)
while not z: # Пока проверка не проходит
    print(f'Ошибка! - Введите значение типа {int}')
    z = validation(input('Z: '), int) # Повторно просим ввод

arr = [] # Создаем пустой массив для матрицы
for i in range(y): # Идем по строкам
    new_st = []
    for j in range(x): # Заполняем элементы в строках массивами длинной Z
        new_el = array_validation(input(f'Введите строку №{j + 1} через пробел: ').split(), int)  # Вводим и проверяем строку
        while not new_el:  # Пока проверка не проходит
            new_el = array_validation(input(f'Введите строку №{j + 1} через пробел: ').split(), int)  # Повторный ввод
        while len(new_el) != z:  # Если длинна строки не соответствует размерности
            new_el = []
            while not new_el:  # Проверяем строку
                print('Ошибка! - Указанное количество элементов не соответствует данному')
                new_el = array_validation(input(f'Введите строку №{j + 1} через пробел: ').split(), int)  # Вводим и проверяем строку
        new_st.append(new_el) # Добавляем в строку
    arr.append(new_st) # Добавляем строку в матрицу

# Выводим срез
i = int(input('Введите i для вывода среза по второму индексу: '))
while i > y:
    print('Ошибка! - i > y')
    i = int(input('Введите i для вывода среза: '))
for j in arr:
    print('Срез: ', *j[i:])