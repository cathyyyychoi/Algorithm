import sys
import math

num = str(math.factorial(int(sys.stdin.readline())))
l = len(num)

for i in range(l):
    if num[-(i + 1)] != '0':
        print(i)
        break
