from stuff import *
from math import sqrt, ceil

file = open("amogus", 'r')
a = read_data(file)
file.close()
print(a)
print()

interval_count = ceil(sqrt(len(a)))
print("Кол-во интервалов -", interval_count)
interval_length = (max(a) - min(a)) / interval_count
print("Длина интервала -", format(interval_length, '.3f'))
print()

by_intervals = separate_into_intervals(a, interval_count, interval_length)
print(a[0])
x = avgs(a[0], interval_length, interval_count)
p = frequencies(by_intervals, len(a))
h = heights(p, interval_length)
print_info(by_intervals, x, p, h, interval_length)
print()

math_exp = math_exp(x, p)
print("Точечная оценка мат. ожидания:", format(math_exp, '.5f'))
dispersion = dispersion(x, p, math_exp)
print("Точечная оценка дисперсии:", format(dispersion, '.5f'))
print()

math_exp_borders = math_exp_borders(math_exp, dispersion, interval_count)
print("Доверительный интервал для мат. ожидания:",
      format(math_exp_borders[0], '.5f'), '< M <', format(math_exp_borders[1], '.5f'))

dispersion_borders = dispersion_borders(dispersion, interval_count)
print("Доверительный интервал для дисперсии:",
      format(dispersion_borders[0], '.5f'), '< D <', format(dispersion_borders[1], '.5f'))
