def solution(lottos, win_nums):
    answer = [0, 0]
    rank = [6, 6, 5, 4, 3, 2, 1]
    
    cnt = 0
    cnt_zero = lottos.count(0)
    
    for i in lottos:
        if i in win_nums:
            cnt += 1
            
    answer[0] = rank[cnt + cnt_zero] # 최고 확률 => 0이 당첨 번호일 확률
    answer[1] = rank[cnt] # 최저 확률 => 0이 당첨 번호가 아닐 확률
    
    return answer
