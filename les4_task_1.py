# Определить, какое число в массиве встречается чаще всего.
import random
import sys
import timeit
import cProfile

SIZE1, SIZE2, SIZE3, SIZE4, SIZE5, SIZE6, SIZE7, SIZE8, SIZE9, = 10, 100, 1000, 5000, 7000, 200_000, 300_000,\
                                                                 500_000, 700_000
MIN_ITEM = 0
MAX_ITEM = 10
array1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE1)]
array2 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE2)]
array3 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE3)]
array4 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE4)]
array5 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE5)]
array6 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE6)]
array7 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE7)]
array8 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE8)]
array9 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE9)]
#print(array1)


def max_my_func(arr):
    dict_for_count = {}
    max_array_item = -sys.maxsize - 1
    for i in range(len(arr)): # перебираем массив, записываем цифры строкой, и увеличиваем счетчик на 1
        temp = str(arr[i]) # временная переменная, хранит текущий ключ-строку
        if str(arr[i]) in dict_for_count.keys():  #проверяем есть ли число в словаре, если есть, то его значение увеличиваем на 1
            dict_for_count[str(arr[i])] += 1
        else:                               #если число не нашлось, то присваиваем его значению 1 - оно нашлось первый раз
            dict_for_count[str(arr[i])] = 1
        if dict_for_count[temp] >= max_array_item:  # вычисляем максимальное значение
            max_array_item = dict_for_count[temp]

    result_dict = {key: value for key, value in dict_for_count.items() if value == max_array_item}  #генерируем новый словарь с макс. знач.

    for number, value in result_dict.items():
        item = f'Число {number} встречается {value} раз(а)!'
        yield item


def max_teacher_func(arr):
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
    if frequency > 1:
        return f'Число {num} встречется {frequency} раз(а)'
    else:
        return 'Все элементы уникальны'


def max_built_in_func(arr):
    max = 1
    for i in range(len(arr)):
        temp_number = arr[i]
        temp_count = arr.count(temp_number)
        if temp_count >= max:
            max = temp_count
            number = temp_number

    return f'Число: {number} встречается {max} раз'


# print('# ================================= 1 ==============================')
# for i in max_my_func(array1):
#     print(i)
# print('# ================================= 2 ==============================')
# print(max_teacher_func(array1))
# print('# ================================= 3 ==============================')
# print(max_built_in_func(array1))

print('=================My_CODE==================')
print(timeit.timeit('max_my_func(array1)', number=100, globals=globals()))          # 3.555603325366974e-05
print(timeit.timeit('max_my_func(array2)', number=100, globals=globals()))          # 3.350799670442939e-05
print(timeit.timeit('max_my_func(array3)', number=100, globals=globals()))          # 3.248604480177164e-05
print(timeit.timeit('max_my_func(array4)', number=100, globals=globals()))          # 3.33109637722373e-05
print(timeit.timeit('max_my_func(array5)', number=100, globals=globals()))          # 3.151199780404568e-05
print(timeit.timeit('max_my_func(array6)', number=100, globals=globals()))          # 3.4191005397588015e-05
print(timeit.timeit('max_my_func(array7)', number=100, globals=globals()))          # 3.310601459816098e-05
print(timeit.timeit('max_my_func(array8)', number=100, globals=globals()))          # 3.322400152683258e-05
print(timeit.timeit('max_my_func(array9)', number=100, globals=globals()))          # 3.338296664878726e-05
for i in max_my_func(array9):                                                       # Число 5 встречается 64010 раз(а)!
    print(i)
print('=================Teacher_CODE=============')
print(timeit.timeit('max_teacher_func(array1)', number=100, globals=globals()))    # 0.0005710749537684023
print(timeit.timeit('max_teacher_func(array2)', number=100, globals=globals()))    # 0.03304875799221918
print(timeit.timeit('max_teacher_func(array3)', number=100, globals=globals()))    # 2.9942595409811474
print(timeit.timeit('max_teacher_func(array4)', number=100, globals=globals()))    # 74.86369284597458
#print(timeit.timeit('max_teacher_func(array5)', number=100, globals=globals()))
#print(timeit.timeit('max_teacher_func(array6)', number=100, globals=globals()))
#print(timeit.timeit('max_teacher_func(array7)', number=100, globals=globals()))
#print(timeit.timeit('max_teacher_func(array8)', number=100, globals=globals()))
#print(timeit.timeit('max_teacher_func(array9)', number=100, globals=globals()))
print('=================Build_in_bad_CODE========')
print(timeit.timeit('max_built_in_func(array1)', number=100, globals=globals()))    # 0.0003827280015684664
print(timeit.timeit('max_built_in_func(array2)', number=100, globals=globals()))    # 0.01156340300804004
print(timeit.timeit('max_built_in_func(array3)', number=100, globals=globals()))    # 1.4136253620381467
print(timeit.timeit('max_built_in_func(array4)', number=100, globals=globals()))    # 35.69449894299032

cProfile.run('max_my_func(array5)')
cProfile.run('max_teacher_func(array5)')
cProfile.run('max_built_in_func(array5)')

#        4 function calls in 0.000 seconds
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#       1    0.000    0.000    0.000    0.000 les4_task_1.py:21(max_my_func)
#       1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#        7005 function calls in 1.464 seconds
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    1.464    1.464 <string>:1(<module>)
#        1    1.463    1.463    1.464    1.464 les4_task_1.py:40(max_teacher_func)
#        1    0.000    0.000    1.464    1.464 {built-in method builtins.exec}
#     7001    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#         7005 function calls in 0.691 seconds
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.691    0.691 <string>:1(<module>)
#        1    0.002    0.002    0.691    0.691 les4_task_1.py:57(max_built_in_func)
#        1    0.000    0.000    0.691    0.691 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     7000    0.690    0.000    0.690    0.000 {method 'count' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#
#Process finished with exit code 0

