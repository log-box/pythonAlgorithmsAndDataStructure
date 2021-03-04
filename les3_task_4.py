# Определить, какое число в массиве встречается чаще всего.
import random

SIZE = 3
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

count = {}
max = 0

for i in range(len(array)): # перебираем массив, записываем цифры строкой, и увеличиваем счетчик на 1
    temp = str(array[i]) # временная переменная, хранит текущий ключ-строку
    if str(array[i]) in count.keys():  #проверяем есть ли число в словаре, если есть, то его значение увеличиваем на 1
        count[str(array[i])] += 1
    else:                               #если число не нашлось, то присваиваем его значению 1 - оно нашлось первый раз
        count[str(array[i])] = 1
    if count[temp] >= max:  # вычисляем максимальное значение
        max = count[temp]

result_dict = {key: value for key, value in count.items() if value == max}  #генерируем новый словарь с макс. знач.

for number, value in result_dict.items():
    print(f'Число {number} встречается {value} раз(а)!')

