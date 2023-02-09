# Задание 1. Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150. 
# Посчитать (желательно без использования статистических методов наподобие std, var, mean) 
# среднее арифметическое, 
# среднее квадратичное отклонение, 
# смещенную и несмещенную оценки дисперсий для данной выборки.

import numpy as np

arr=np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])

def mean_value(array):
    return sum(array)/len(array)

print(f'Среднее арифметическое для данной выборки = {mean_value(arr):.2f}')


def mean_square_deviation(array):
    square_dev=(array-mean_value(array))**2
    return (sum(square_dev)/len(square_dev))**(1/2)

print(f'Среднее квадратичное отклонение для данной выборки = {mean_square_deviation(arr):.4f}')


def dispers(array, no_off=False):
    square_dev=(array-mean_value(array))**2
    return sum(square_dev)/(len(square_dev)-1) if no_off else sum(square_dev)/len(square_dev)

print(f'Смещенная оценка дисперсии для данной выборки D = {dispers(arr):.4f}\n'
      f'Несмещенная оценка дисперсии для данной выборки D = {dispers(arr, True):.4f}')