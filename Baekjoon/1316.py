num = int(input())

for i in range(num):
    input_str = input()
    for j in range(1, len(input_str)):
        if input_str.find(input_str[j-1]) > input_str.find(input_str[j]):
            num -= 1
            break

print(num)
