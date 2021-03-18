# 2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

array = []

while not array:
    array = [item*random.random() for item in range(random.randint(0, 51), random.randint(0, 51))]

print(f'Исходный массив:{array}')


def split_and_merge_list(arr):
    def merge_list(part_1, part_2):
        sorted_array = []
        part_1_length = len(part_1)
        part_2_length = len(part_2)

        i = 0
        j = 0
        while i < part_1_length and j < part_2_length:
            if part_1[i] <= part_2[j]:
                sorted_array.append(part_1[i])
                i += 1
            else:
                sorted_array.append(part_2[j])
                j += 1

        sorted_array += part_1[i:] + part_2[j:]
        return sorted_array
    splitter = len(arr) // 2
    arr_part_one = arr[:splitter]     # деление массива на два примерно равной длины
    arr_part_two = arr[splitter:]

    if len(arr_part_one) > 1:
        arr_part_one = split_and_merge_list(arr_part_one)
    if len(arr_part_two) > 1:
        arr_part_two = split_and_merge_list(arr_part_two)

    return merge_list(arr_part_one, arr_part_two)


test = split_and_merge_list(array)
print(f'Отсортированный массив:{test}')

