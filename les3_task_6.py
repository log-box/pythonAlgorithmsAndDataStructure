# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random, sys

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = -1
#array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
array = [-796, -778, -755, -666]
min_array_item = sys.maxsize
max_array_item = -sys.maxsize - 1
sum = 0
min_index = 0  # без них Пичарм подсвечивает в коде - неудобно
max_index = 0  # ---

for i in range(len(array)):
    if array[i] > max_array_item:
        max_array_item = array[i]
        max_index = i
    if array[i] < min_array_item:
        min_array_item = array[i]
        min_index = i

if min_index < max_index:  # если минимальный стоит слева от максимального
    for i in range(min_index + 1, max_index):
        sum = sum + array[i]
for i in range(max_index + 1, min_index): # если максимальный стоит слева от минимального
    sum = sum + array[i]
print(f'Ваш массив: {array}')
print(f'Сумма между минимальным значением: {array[min_index]} и '
      f'максимальным значением: {array[max_index]} равна: {sum}')
