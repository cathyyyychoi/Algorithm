M = int(input())
N = int(input())
num_list = []
    
def f_2581(M, N):
    for i in range(M, N + 1):
        count = 0
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    count += 1
                    break
            if count == 0:
                num_list.append(i)

            
    if len(num_list) != 0:
        print(sum(num_list))
        print(num_list[0])
    else:
        print(-1)

    return 0

f_2581(M, N)
