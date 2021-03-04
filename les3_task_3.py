# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.


import random

SIZE = 3
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_item = MAX_ITEM
max_item = MIN_ITEM

for i in range(len(array)):
    if array[i] < min_item:
        min_item = array[i]
        min = i
    if array[i] > max_item:
        max_item = array[i]
        max = i
print(min_item, max_item)

#max = array.index(max_item)
#min = array.index(min_item)

array[max] = min_item
array[min] = max_item

print(array)


