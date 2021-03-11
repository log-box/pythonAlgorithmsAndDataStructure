# Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


from collections import deque


def hex_summ():
    reference_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    x = 1
    result = deque()
    one = 0

    while x == 1:
        x_number = deque(input('Введите первое число').upper())
        for _ in x_number:
            if _ not in reference_list:
                print('Вы ввели не шестнадцатиричное число')
                break
        else:
            x = 0
    while x == 0:
        y_number = deque(input('Введите второе число').upper())
        for _ in y_number:
            if _ not in reference_list:
                print('Вы ввели не шестнадцатиричное число')
                break
        else:
            x = 1

    if len(x_number) <= len(y_number):
        x_number, y_number = y_number, x_number
    while len(y_number) > 0:
        temp1 = reference_list.index(y_number.pop())
        temp2 = reference_list.index(x_number.pop())
        if temp1 + temp2 > 15:
            addition = abs((temp1+temp2) - 16) + one
            one = 1
        else:
            addition = temp1 + temp2
        result.appendleft(reference_list[addition])
    while len(x_number) > 0:
        temp1 = reference_list.index(x_number.pop())
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

hex_summ()