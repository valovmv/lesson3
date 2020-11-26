def div(*args):

    try:
        arg1 = int(input('Введите первое число: '))
        arg2 = int(input('Введите второе число: '))
        result = arg1 // arg2
    except ValueError:
        return 'Ошибка'
    except ZeroDivisionError:
        return 'Ошибка: "Деление на ноль"'

    return result

print(f'Результат: {div()}')