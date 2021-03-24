n = int(input())
for i in range(n):
    a = input()
    l = list(a)
    sum = 0
    for i in l:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break

    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')
