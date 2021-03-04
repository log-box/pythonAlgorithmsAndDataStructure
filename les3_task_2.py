# Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
# 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля), т.к. именно в
# этих позициях первого массива стоят четные числа.


import random

SIZE = 3
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

second_array = []

for i in range(len(array)):
    if array[i] % 2 == 0:
        second_array.append(i)

print('Индексты четных элементов следующие:', second_array)
