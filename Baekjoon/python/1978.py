N = int(input())
num_list = list(map(int, input().split()))

def is_prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

count = 0

for i in num_list:
    if is_prime(i):
        count += 1
print(count)
