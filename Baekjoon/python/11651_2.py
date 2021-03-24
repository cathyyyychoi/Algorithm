n = int(input())

n_list = []

for i in range(n):
    n_list.append(list(map(int, input().split())))
n_list.sort(key = lambda x: (x[1], x[0]))
for i in n_list:
    print(i[0], i[1])

# same memory as sys.readline(), but take much more time
