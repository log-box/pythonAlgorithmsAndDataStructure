# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.


import random

SIZE_N = 4
SIZE_M = 6
MIN_ITEM = 0
MAX_ITEM = 1_000
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_M)] for _ in range(SIZE_N)]
print(*matrix, sep='\n')