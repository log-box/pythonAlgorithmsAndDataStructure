# Определить, какое число в массиве встречается чаще всего.
import random, sys, timeit, cProfile


SIZE = 1000
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


def max_my_func(arr):
    dict_for_count = {}
    max_array_item = -sys.maxsize - 1
    for i in range(len(array)): # перебираем массив, записываем цифры строкой, и увеличиваем счетчик на 1
        temp = str(array[i]) # временная переменная, хранит текущий ключ-строку
        if str(array[i]) in dict_for_count.keys():  #проверяем есть ли число в словаре, если есть, то его значение увеличиваем на 1
            dict_for_count[str(array[i])] += 1
        else:                               #если число не нашлось, то присваиваем его значению 1 - оно нашлось первый раз
            dict_for_count[str(array[i])] = 1
        if dict_for_count[temp] >= max_array_item:  # вычисляем максимальное значение
            max_array_item = dict_for_count[temp]

    result_dict = {key: value for key, value in dict_for_count.items() if value == max_array_item}  #генерируем новый словарь с макс. знач.

    for number, value in result_dict.items():
        item = f'Число {number} встречается {value} раз(а)!'
        yield item


def max_teacher_func(arr):
    num = array[0]
    frequency = 1
    for i in range(len(array)):
        spam = 1
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                spam += 1
        if spam > frequency:
            frequency = spam
            num = array[i]
    if frequency > 1:
        return f'Число {num} встречется {frequency} раз(а)'
    else:
        return 'Все элементы уникальны'


def max_built_in_func(arr):
    max = 1
    for i in range(len(array)):
        temp_number = array[i]
        temp_count = array.count(temp_number)
        if temp_count >= max:
            max = temp_count
            number = temp_number

    return f'Число: {number} встречается {max} раз'


print('# ================================= 1 ==============================')
for i in max_my_func(array):
    print(i)
print('# ================================= 2 ==============================')
print(max_teacher_func(array))
print('# ================================= 3 ==============================')
print(max_built_in_func(array))


print(timeit.timeit('max_my_func(array)', number=100, globals=globals()))
print(timeit.timeit('max_my_func(array)', number=100, globals=globals()))
print(timeit.timeit('max_my_func(array)', number=100, globals=globals()))
print(timeit.timeit('max_my_func(array)', number=100, globals=globals()))
print(timeit.timeit('max_my_func(array)', number=100, globals=globals()))