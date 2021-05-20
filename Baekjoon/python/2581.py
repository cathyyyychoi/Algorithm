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
        return(sum(num_list), num_list[0])
    else:
        return("-1")
