# Вычислить сумму бесконечного ряда
# Булгаков Арсений Сергеевич ИУ7-16Б

# Функция N-ого члена бесконечного ряда
def func(n) -> float:
    return 1 / ((2 ** n) - n)


# Вввод входных данных
EPS = float(input('Введите эпсилон: '))
step = int(input('Введите итерационный шаг: '))
end = int(input('Введите конечное количество итераций: '))
sum = 0  # Сумма
current = 1  # Текущая итерация

print('-' * 46 + '\n|    № Итерации    |     t     |     Sum     |\n|' + '-' * 44 + '|')  # Оглавления таблички
while current <= end:  # Пока текущая итерация меньше или рав конечной заданной
    new_x = func(current)  # Считаем член ряда
    sum += new_x  # Добавляем к сумме
    if (current - 1) % step == 0:  # Выводим на заданный шаг
        print(f'|{current:^18}|{new_x:>11.4g}|{sum:>13.4g}|')
    if abs(new_x) <= EPS:  # Сверяем точность
        print('-' * 46)
        print(f'Сумма бесконечного ряда - {sum:.5f}. Всего итераций: {current}')
        exit(-1)
    current += 1  # Добавляем 1 к итерации
print('-' * 46)
print(f'Не удалось достичь нужной точности. Всего итераций: {end}')
