# Решение квадратного уравнения
# Булгаков Арсений Сергеевич ИУ7-16Б

# # Вввод начальных значений
print('Введите коэффиценты - Ax^2 + Bx + C = 0')
a = float(input('Введите A: '))
b = float(input('Введите B: '))
c = float(input('Введите C: '))

# Обработка коэфицентов
if a == 0: # Если a = 0, тогда решаем линейное уравнение с одной переменной
    if b == 0: # Если и b = 0, тогда решение уравнения зависит от последнего коэффицента
        if c == 0:
            print('x - Любое число') # 0 = 0 при любом x
        else:
            print('Нет решений')  # c != 0 при любом x
    else: # Если b != 0, то продолжаем решать линейное уравнение
        x = -c / b
        print('Корень уравнения: {0:.5f}'.format(x))
else: # Если a != 0, тогда решаем квадратное уравнение через дескриминант
    D = b ** 2 - (4 * a * c) # Рассчет дискриминанта
    # В зависимости от количества корней решаем уравнение
    if D > 0: # Если два корня
        # Считаем корни по формуле
        x1 = (-b + D ** (1 / 2)) / (2 * a)
        x2 = (-b - D ** (1 / 2)) / (2 * a)
        print('Корни уравнения: {0:.5f} и {1:.5f}'.format(x1, x2))
    elif D == 0: # Если один корень
        x = (-b + D ** (1 / 2)) / 2
        print('Корнь уравнения: {0:.5f}'.format(x))

    else: # D < 0, следовательно корней нет
        print('Нет решений')