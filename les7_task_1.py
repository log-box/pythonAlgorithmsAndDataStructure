# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке
# [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком. Улучшенные версии
# сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

import random

array = []

while not array:
    array = [random.randint(-100, 101) for item in range(random.randint(-100, 101))]


def my_bubble(arr):
    _len = len(arr)
    print(f'Исходный массив имеет длину {_len}\nИсходный массив: {arr}')
    for i in range(0, _len - 1):
        for j in range(0, _len - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(f'Отсортированный массив: {arr}')

my_bubble(array)
