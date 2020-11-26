def my_func():
    sum_result = 0
    ex = False
    while ex == False:
        number = input('Введите строку числе или специальный символ q для выхода: ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_result = sum_result + res
        print(f'Текущая сумма такая: {sum_res}')
    print(f'Окончательный результат такой: {sum_res}')


my_func()