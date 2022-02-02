def solution(absolutes, signs):
    answer = 0
    
    for i in range(len(absolutes)):
        if signs[i]:
            answer += absolutes[i] # signs가 True: 원래 정수가 양수
            
        else:
            answer -= absolutes[i] # signs가 False: 원래 정수가 
            
    return answer
