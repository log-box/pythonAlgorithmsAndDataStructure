# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.


import sys
import random

SIZE = 3
MIN_ITEM = 0
MAX_ITEM = 100
#array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
array = [-796, -778, -755]
print(array)
min_array_item = sys.maxsize
max_array_item = -sys.maxsize - 1


for i in range(len(array)):
    if array[i] < min_array_item:
        min = i
        min_array_item = array[i]
    else:
        max = i
        max_array_item = array[i]


print(min_array_item, max_array_item)

#max = array.index(max_item)
#min = array.index(min_item)

array[max] = min_array_item
array[min] = max_array_item

print(array)


