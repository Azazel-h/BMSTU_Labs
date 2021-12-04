# Требуется написать программу для вычисления приближённого значения интеграла
# двумя разными методами (по варианту).
# Необходимо ввести: начало, конец отрезка, N1, N2 - количества участков разбиения
# для численного интегрирования.
# Срединных прямоугольников - парабол
# Далее построить таблицу
#
# На основе известной первообразной определить, какой метод является наиболее
# точным (указав абсолютную и относительную погрешности измерения), а для менее
# точного метода итерационно вычислить количество участков разбиения, для которого
# интеграл будет вычислен с заданной точностью:
# |𝐼(𝑁) − 𝐼(2𝑁)| < ε
# Интегрируемую функцию и первообразную необходимо описать в виде программных
# функций, чтобы их можно было легко заменить на произвольные и убедиться, что
# программа работает корректно.
# Булгаков Арсений Сергеевич ИУ7-16Б

from Functions import *

def f(x):
    return x ** 2

def F(x):
    return (x ** 3) / 3

def riemann_sum(N, start, end):
    S = 0
    step = (end - start) / N
    start_temp = start
    end_temp = start + step
    for i in range(N):
        S += f((start_temp + end_temp) / 2) * (end_temp - start_temp)
        start_temp = end_temp
        end_temp += step
    return S

def simpsons_rule(N, start, end):
    S = 0
    step = (end - start) / N
    start_temp = start
    end_temp = start + step
    for i in range(N):
        S += ((end_temp - start_temp) / 6) * (f(start_temp) + 4 * f((start_temp + end_temp) / 2) + f(end_temp))
        start_temp = end_temp
        end_temp += step
    return S

def better_N(var, N, EPS, start, end):
    flag = True
    while True:
        val = abs(riemann_sum(N, start, end) - riemann_sum(2 * N, start, end)) if var == 1 \
            else abs(simpsons_rule(N, start, end) - simpsons_rule(2 * N, start, end))
        if flag and N > 1000000:
            ans = input('Кол-во разбиений превысило 1e6! Нажмите Enter, чтобы продолжить и введите что-то, чтобы прерваться: ')
            if ans == '':
                flag = False
            else:
                break
        if val < EPS:
            flag = False
            break
        N *= 2
    if flag:
        print('Заданная точность не достигнута, выполнение программы прервано, т.к. было слишком долгим')
    else:
        print(f'Заданная точность для метода {"срединных перпендикуляров" if var == 1 else "парабол"} достигнута при N = {N}')
        print('Точность:', riemann_sum(N, start, end) if var == 1 else simpsons_rule(N, start, end))

start = validation(input('Введите начало отрезка: '), float)
end = validation(input('Введите конец отрезка: '), float)
while start > end:
    print('Ошибка: Конец отрезка не может быть меньше его начала')
    start = validation(input('Введите начало отрезка: '), float)
    end = validation(input('Введите конец отрезка: '), float)

N1 = validation(input('Введите количество участков разбиения N1: '), int)
while N1 == 0:
    print('Ошибка: Количество участков всегда > 0')
    N1 = validation(input('Введите количество участков разбиения N1: '), int)

N2 = validation(input('Введите количество участков разбиения N2: '), int)
while N2 == 0:
    print('Ошибка: Количество участков всегда > 0')
    N2 = validation(input('Введите количество участков разбиения N2: '), int)

real_integral = F(end) - F(start)
rs1 = riemann_sum(N1, start, end)
rs2 = riemann_sum(N2, start, end)
sr1 = simpsons_rule(N1, start, end)
sr2 = simpsons_rule(N2, start, end)

absolute_error_rs1 = abs(rs1 - real_integral)
absolute_error_rs2 = abs(rs2 - real_integral)
absolute_error_sr1 = abs(sr1 - real_integral)
absolute_error_sr2 = abs(sr2 - real_integral)

percent_error_rs1 = abs(absolute_error_rs1 / real_integral) * 100
percent_error_rs2 = abs(absolute_error_rs2 / real_integral) * 100
percent_error_sr1 = abs(absolute_error_sr1 / real_integral) * 100
percent_error_sr2 = abs(absolute_error_sr2 / real_integral) * 100

print('-' * 65)
print(f'|   {"":^32}|{"I(N1)":^13}|{"I(N2)":^13}|')
print(f'|  {"Метод срединных прямоугольников":^32} |  {rs1:^10.5f} |  {rs2:^10.5f} |')
print(f'|  {"Метод парабол":^32} | ', f'{sr1:^10.5f}' if N1 % 2 == 0 else f'{"-":^10}', '| ',
      f'{sr2:^10.5f}' if N2 % 2 == 0 else f'{"-":^10}', '|')
print('-' * 108)
print(f'|  {"":^32} |  {"Метод срединных прямоугольников":^32} | {"Метод парабол":^32} |')
print(f'|  {"Абсолютная погрешность для N1":^32} | {absolute_error_rs1:^32.5f}', ' |',
      f'{absolute_error_sr1:^32.5f}' if N1 % 2 == 0 else f'{"-":^32}', '|')
print(f'|  {"Абсолютная погрешность для N2":^32} | {absolute_error_rs2:^32.5f}', ' |',
      f'{absolute_error_sr2:^32.5f}' if N2 % 2 == 0 else f'{"-":^32}', '|')
print(f'|  {"Относительная погрешность для N1":^32} | {percent_error_rs1 :^32.5f}', ' |',
      f'{percent_error_sr1:^32.5f}' if N1 % 2 == 0 else f'{"-":^32}', '|')
print(f'|  {"Относительная погрешность для N2":^32} | {percent_error_rs2:^32.5f}', ' |',
      f'{percent_error_sr2:^32.5f}' if N2 % 2 == 0 else f'{"-":^32}', '|')
print('-' * 108)

EPS = validation(input('Введите EPS: '), float)
while not 0 < EPS < 1:
    print('Ошибка! - Введите корректный EPS (0 < EPS < 1)')
    EPS = validation(input('Введите EPS: '), float)

if N1 % 2 == 0:
    if percent_error_rs1 < percent_error_sr1:
        print('Метод срединных перпендикуляров точнее, улучшаем метод парабол')
        better_N(2, N1, EPS, start, end)
    else:
        print('Метод парабол точнее, улучшаем метод срединных перпендикуляров')
        better_N(1, N1, EPS, start, end)
elif N2 % 2 == 0:
    if percent_error_rs2 < percent_error_sr2:
        print('Метод срединных перпендикуляров точнее, улучшаем метод парабол')
        better_N(2, N2, EPS, start, end)
    else:
        print('Метод парабол точнее, улучшаем метод срединных перпендикуляров')
        better_N(1, N2, EPS, start, end)
else:
    print('Метод срединных перпендикуляров точнее, т.к данных по методу паробол недостаточно => Улучшаем его')
    better_N(1, N1, EPS, start, end)

print('Реальное значение интеграла, через первообразную:', real_integral)
