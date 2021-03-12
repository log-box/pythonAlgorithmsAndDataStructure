# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.


from collections import defaultdict

profitable = []
not_profitable = []
equal = []
firms = defaultdict(int)
loan_sum = 0
firms_count = int(input('Введите колличество фирм: \n'))
for _ in range(firms_count):
    firm_name = input('Введите название ' + str(_+1) + ' фирмы\n')
    quarter_count = 1  # счетчик кварталов
    while quarter_count <= 4:
        loan = float(input(f'Введите доход за {quarter_count} квартал'))
        firms[firm_name] += loan
        loan_sum += loan
        quarter_count += 1
average_loan = (loan_sum/firms_count)
for i in firms:
    if firms[i] > average_loan:
        profitable.append(i)
    elif firms[i] < average_loan:
        not_profitable.append(i)
    else:
        equal.append(i)
print(f'Средняя прибыль всех фирм равна: {average_loan}')
if profitable:
    print('Фирмы с доходом выше среднего:')
    i=1
    for _ in profitable:
        print(f'{i}){_}')
        i += 1
else:
    print('НЕТ фирм с доходом выше среднего')
if not_profitable:
    print('Фирмы с доходом ниже среднего:')
    i = 1
    for _ in not_profitable:
        print(f'{i}){_}')
        i += 1
else:
    print('НЕТ фирм с доходом ниже среднего')

if equal:
    print('Фирмы с доходом равным среднему:')
    i = 1
    for _ in equal:
        print(f'{i}){_}')
        i += 1
else:
    print('НЕТ фирм с доходом равным среднему')
