ns = int(input())
numlist = []

for i in range(ns):
    nums = int(input())
    numlist.append(nums)
    
numlist.sort()

for i in numlist:
    print(i)
