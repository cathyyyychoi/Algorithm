import collections 

def solution(participant, completion): 
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0] 

# collections 라이브러리 잘 사용하기!
