a, b, c = list(map(int, input().split()))
point = 0

if (c <= b):
    point = -1

else:
    point = a // (c - b) + 1

print(point)
