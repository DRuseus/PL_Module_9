def is_prime(func):
    def wrapper(*args):
        result = 'Простое'

        func_result = func(*args)

        for i in range(func_result // 2, 1, -1):
            if func_result % i == 0 and i > 1:
                result = 'Составное'
                break
        print(result)
        return func_result

    return wrapper


@is_prime
def sum_three(first, second, three):
    return first + second + three


result = sum_three(2, 3, 6)
print(result)

result = sum_three(10, 4, 999)
print(result)

result = sum_three(10, 5, 999)
print(result)
