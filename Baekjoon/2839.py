input_num = int(input())

F = int(input_num / 5)
input_num %= 5

T = 0
while F >= 0:
    if input_num % 3 == 0:
        T = input_num // 3
        input_num = input_num % 3
        break
    F -= 1
    input_num += 5
    
print((input_num == 0) and (F + T) or -1)
