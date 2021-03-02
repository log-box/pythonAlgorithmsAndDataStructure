# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

new_chislo = 0

chislo = int(input('введите число:\n'))
while chislo !=0:
    new_chislo = (chislo % 10) + 10 * new_chislo
    chislo = chislo // 10

print(f'Перевернутое число: {new_chislo}')