num = int(input())
for i in range(num):
    n_list = list(map(int, input().split(' ')))
    avg = sum(n_list[1:]) / n_list[0]
    cnt = 0
    for j in n_list[1:]:
        if j > avg : 
            cnt += 1
            
    print(str("%.3f" % round((cnt / n_list[0]) * 100, 3)) + "%")
