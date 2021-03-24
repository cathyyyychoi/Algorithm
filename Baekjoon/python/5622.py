dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
input_str = input()
cnt = 0

for i in range(len(input_str)):
    for j in dial:
        if input_str[i] in j:
            cnt += dial.index(j) + 3

print(cnt)
