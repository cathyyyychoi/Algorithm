def solution(a, b):
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    day = day * 55
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    answer = day[sum(month[:a]) + b - 1]
    return answer

print(solution(5, 24))
