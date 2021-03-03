# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.


import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_item = 0
max_item = 0

