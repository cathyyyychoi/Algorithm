def solution(numbers):
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    answer = 0
    
    for i in num_list:
        if i not in numbers: # 숫자가 중복되지 않기 때문에 1~9까지의 list에 없으면 answer에 더해주기
            answer += i
            
    return answer
