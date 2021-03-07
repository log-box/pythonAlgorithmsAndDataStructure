# Определить, какое число в массиве встречается чаще всего.
import random, sys

SIZE = 30
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

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
    print(f'Число {number} встречается {value} раз(а)!')