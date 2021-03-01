# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых чисел
# и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.


int_count = int(input('Сколько чисел будете вводить?\n'))
digit = int(input('Какую цифру надо подсчитать?\n'))
count = 0


def recurs_func(sequence, dig, count=0):
    if sequence == 0:
        return count
    if sequence % 10 == dig:
        count += 1
    return recurs_func(sequence // 10, dig, count)


for i in range(1, int_count + 1):
    number = int(input('Число ' + str(i) + ': '))
    count = count + recurs_func(number, digit)
print(f'Искомая цифра встретилась {count} раз!')




