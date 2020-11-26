def my_func(arg1, arg2, arg3):
    numbers = [arg1, arg2, arg3]
    result = []
    max1 = max(numbers)
    result.append(max1)
    numbers.remove(max1)
    max2 = max(numbers)
    result.append(max2)
    print(sum(result))

my_func(15, 8, 56)
