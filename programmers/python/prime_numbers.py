from itertools import combinations

def solution(numbers):
    answer = 0
    for num in combinations(numbers, 3):
        temp = sum(num)
        for j in range(2, temp):
            if temp % j == 0:
                 break
        else:
            answer += 1
    return answer

print(solution([1,2,3,4]))
