# Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
#
# func("papa")
# 6
# func("sova")
# 9


import hashlib

string = input('Введите строку:\n')

sub_string_sum = set()  # нужен для проверки уникальности "слов"
len_ = len(string)  # для понимания работы range()


def my_hash_2(value):  # взял функцию с урока. В комментарии ниже использовал готовую функцию hashlib.sha1

    letter = 26
    hash_ = 0
    size = 10_000
    for index, char in enumerate(value):
        hash_ += (ord(char) - ord('a') + 1) * letter ** index
    return hash_ % size


def my_func_sub_string_count(_str):
    for i in range(len(string)):
        for j in range(len(string), i,
                       -1):  # пробегаем по срезам строки от начала до конца, сдвигая начало на 1 на прогоне
            hash_str = my_hash_2(_str[i:j])  # hashlib.sha1(string[i:j].encode('utf-8')).hexdigest()
            sub_string_sum.add(hash_str)  # добавятся только те хеши, которые уникальны

    print(f'Есть {len(sub_string_sum) - 1} уникальных подстрок в строке "{string}"')  # вычитаем хеш самой строки


my_func_sub_string_count(string)
