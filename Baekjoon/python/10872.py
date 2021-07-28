def factorial(n):
    if n == 1:
        result = 1
    elif n >= 2:
        result = n * factorial(n - 1)
    return result

num = int(input())
print(factorial(num))
