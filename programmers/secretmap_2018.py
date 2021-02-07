def solution(n, arr1, arr2):
    answer = []
    for num1, num2 in zip(arr1, arr2):
        temp = str(bin(num1 | num2)[2:]) # 2진수로 변환
        temp = temp.rjust(n, "0") # bit연산결과가 n보다 작을때 오른쪽정렬 후 0으로 padding
        temp = temp.replace("1", "#")
        temp = temp.replace("0", " ")
        answer.append(temp)
    return answer

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n, arr1, arr2))
