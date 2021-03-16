# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

import sys
import random
import os
'''
Python 3.8.5 (default, Jan 27 2021, 15:41:15) 
[GCC 9.3.0] on linux
machine='x86_64'

'''
print(os.uname())

def count(obj):
    temp = 0
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                temp += count(key) + count(value)
            return temp + sys.getsizeof(obj)
        elif not isinstance(obj, str):
            for item in obj:
                temp += count(item)
            return temp + sys.getsizeof(obj)
    return sys.getsizeof(obj)


def max_my_func():
    arr = [random.randint(0, 10) for _ in range(1000)]
    dict_for_count = {}
    max_array_item = -sys.maxsize - 1
    for i in range(len(arr)):
        temp = str(arr[i])
        if str(arr[i]) in dict_for_count.keys():
            dict_for_count[str(arr[i])] += 1
        else:
            dict_for_count[str(arr[i])] = 1
        if dict_for_count[temp] >= max_array_item:
            max_array_item = dict_for_count[temp]
    result_dict = {key: value for key, value in dict_for_count.items() if value == max_array_item}
    _sum = count(arr) + count(dict_for_count) + count(result_dict) + count(max_array_item)
    print(f'Функция {max_my_func.__name__} заняла: {_sum} байт памяти')
    for number, value in result_dict.items():
        item = f'Число {number} встречается {value} раз(а)!'
        return item


def max_teacher_func():
    arr = [random.randint(0, 10) for _ in range(1000)]
    num = arr[0]
    frequency = 1
    for i in range(len(arr)):
        spam = 1
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                spam += 1
        if spam > frequency:
            frequency = spam
            num = arr[i]
    _sum = count(arr) + count(num) + count(frequency) + count(spam)
    print(f'Функция {max_teacher_func.__name__} заняла: {_sum} байт памяти')
    if frequency > 1:
        return f'Число {num} встречется {frequency} раз(а)'
    else:
        return 'Все элементы уникальны'


def max_built_in_func():
    arr = [random.randint(0, 10) for _ in range(1000)]
    max = 1
    for i in range(len(arr)):
        temp_number = arr[i]
        temp_count = arr.count(temp_number)
        if temp_count >= max:
            max = temp_count
            number = temp_number
    _sum = count(arr) + count(max) + count(temp_number) + count(temp_count) + count(number)
    print(f'Функция {max_built_in_func.__name__} заняла: {_sum} байт памяти')
    return f'Число: {number} встречается {max} раз'


print('Проверка работы функции')
print(count('1'))
print('*' * 35)
print(count(1))
print('*' * 35)
print(count({'1': 1, '2': 2, '3': 3}))
####################################

max_my_func()
max_teacher_func()
max_built_in_func()

# Проверка работы функции
# 50
# ***********************************
# 28
# ***********************************
# 466
# Функция max_my_func заняла: 38473 байт памяти
# Функция max_teacher_func заняла: 36712 байт памяти
# Функция max_built_in_func заняла: 36748 байт памяти
#
# Process finished with exit code 0
# оптимальная по потреблению памяти функция max_teacher_func()
