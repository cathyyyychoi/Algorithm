input_str = input()
result = [0] * 26

for ch in input_str:
    result[ord(ch) - 97] += 1 # ord('a') = 97, ASCII code 변환 함수

print(result)
