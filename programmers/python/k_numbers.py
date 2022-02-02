def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        new_array = array[commands[i][0]-1:commands[i][1]]
        new_array.sort()
        answer.append(new_array[commands[i][2]-1
        # commands의 3번째 값을 new_array의 index로 추출!
                                
    return answer
