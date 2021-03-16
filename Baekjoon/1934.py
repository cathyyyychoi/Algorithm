def gcd(a, b):
    return gcd(b % a, a) if b % a else a

def lcm(a, b):
    d = gcd(a, b)
    return d * (a // d) * ((b // d))


num = int(input())
for i in range(num):
    A, B = map(int, input().split())
    print(lcm(A, B))
