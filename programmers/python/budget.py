def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)

d = [2, 2, 3, 3]
budget = 10
print(solution(d, budget))
