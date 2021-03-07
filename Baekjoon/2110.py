n,c = map(int, input().split())
result = 0

house = []
for i in range(n):
    x = int(input())
    house.append(x)

house.sort()

low = house[1] - house[0]
high = house[-1] - house[0]

while (low <= high):
    mid = (low + high) // 2
    old = house[0]
    count = 1

    for i in range(1, len(house)):
        if house[i] >= old + mid:
            count += 1
            old = house[i]

    if count >= c:
        low = mid + 1
        result = mid
    else:
        high = mid - 1

print(result)
