def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if (numbers[j] + numbers[i]) not in answer:
                answer.append(numbers[j] + numbers[i])
    return sorted(answer)

numbers = [2, 1, 3, 4, 1]
print(solution(numbers))
