# Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


from collections import deque


def hex_sum():

    reference_list = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
                      'C': 12, 'D': 13, 'E': 14, 'F': 15,
                      0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B',
                      12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    x = 1
    result = deque()
    one = 0

    while x == 1:
        x_number = deque(input('Введите первое число').upper())
        for item in x_number:
            if item not in reference_list:
                print('Вы ввели не шестнадцатиричное число')
                break
        else:
            x = 0
    while x == 0:
        y_number = deque(input('Введите второе число').upper())
        for item in y_number:
            if item not in reference_list:
                print('Вы ввели не шестнадцатиричное число')
                break
        else:
            x = 1

    if len(x_number) <= len(y_number):
        x_number, y_number = y_number, x_number
    while len(y_number) > 0:
        temp1 = reference_list[y_number.pop()]
        temp2 = reference_list[x_number.pop()]
        if temp1 + temp2 > 15:
            addition = abs((temp1+temp2) - 16) + one
            one = 1
        else:
            addition = temp1 + temp2 + one
            one = 0
        result.appendleft(reference_list[addition])
    while len(x_number) > 0:
        temp1 = reference_list[x_number.pop()]
        if temp1 + one > 15:
            addition = abs((temp1+one) - 16)
            one = 1
        else:
            addition = temp1+one
            one = 0
        result.appendleft(reference_list[addition])
    if one == 1:
        result.appendleft(str(one))
        print(f'Сумма чисел равна: {str(result)}')
    else:
        print(f'Сумма чисел равна: {str(result)}')

hex_sum()