dic = { "zero" : 0, "one" : 1, "two" : 2, "three" : 3, "four" : 4,
        "five" : 5,  "six" : 6,  "seven" : 7, "eight" : 8, "nine" : 9}

def solution(s):
    answer = ""
    
    tmp = ""
    for item in s:
        tmp += item #문자나 숫자를 tmp에 계속 더해준다
        if tmp in dic: # item이 문자일 경우
            answer += str(dic[tmp]) # answer에 key값을 더해준다!
            tmp = ""
        elif item.isdigit(): # item이 숫자일 경우
            answer += item
            tmp = ""
    
    return int(answer)
