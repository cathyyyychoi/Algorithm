import time
import random

'''
alg1: 매번 a[1]...,a[k]의 합을 계산한 후 avgk를 계산한다.
alg2: avgk 계산하는데 사용한 a[1]...,a[k]의 합 정보를 avgk+1 계산 시 활용한다.
'''

def alg1(A,n):
    startTime=time.time()
    for i in range(n):
        sum=0
        avgk=0
        for j in range(i+1):
            sum+=A[j]
        avgk=sum/(j+1)          
    endTime=time.time()
    timeSpend=endTime-startTime
    return avgk, timeSpend

def alg2(A,n):
    startTime=time.time()
    sum=0
    for i in range(n):
        sum+=A[i] 
    avgk=sum/n
    endTime=time.time()
    timeSpend=endTime-startTime
    return avgk, timeSpend

n=30000 #n 10,000 -> 20,000 -> 30,000
A=[random.randrange(1,10) for i in range(n)]

avgk1, timeSpend1=alg1(A,n)
avgk2, timeSpend2=alg2(A,n)

print("Average of alg1:",avgk1, "Time:",timeSpend1)
print("Average of alg2:",avgk2, "Time:",timeSpend2)
