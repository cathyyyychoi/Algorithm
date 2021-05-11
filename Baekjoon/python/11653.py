num = int(input())
result = []

while num != 1:
    for i in range(2, num + 1):
        if (num % i == 0):
            result.append(i)
            num = num // i
            break
        
for i in result:
    print(i)
