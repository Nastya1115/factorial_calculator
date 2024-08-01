num = int(input('number:'))

def factorial(n):
    result = 1
    while n > 0:
        result = result * n
        n-=1
        print(result)
    return result

result = factorial(num)
print(f"Факторіал числа {num} дорівнює {result}")
