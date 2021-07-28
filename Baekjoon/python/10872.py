'''
def factorial(n):
    if n == 1:
        result = 1
    elif n >= 2:
        result = n * factorial(n - 1)
    return result

num = int(input())
print(factorial(num))
'''
num = int(input())
result = 1

if num == 1:
    result = 1
elif num >= 2:
    for i in range(1, num + 1):
        result = result * i
print(result)
