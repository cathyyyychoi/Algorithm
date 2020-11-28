'''
실습노트 실습p12_BB.pptx에서

(1) 29,30쪽: [실습프로그램] 분기한정 가지치기 너비우선검색 방법으로
0-1 배낭문제를 해결하는 알고리즘을 python으로 완성하라.

(2) 36,37쪽: [실습프로그램] 분기한정 가지치기 최고우선검색 방법으로
0-1 배낭문제를 해결하는 알고리즘을 python으로 완성하라.

'''

import queue
print("branch and bound_BFS")
class Node:
    def __init__(self,level,weight,profit,bound,include):
        self.level = level
        self.weight = weight
        self.profit = profit
        self.include = include
    def __cmp__(self, other):
        return cmp(self.bound, other.bound)

def kp_BFS():
    global maxProfit
    global bestset
    temp = n*[0]
    v = Node(-1,0,0, 0.0 ,temp)

    v.bound = compBound1(v)
    q = queue.PriorityQueue()
    q.put((v.bound,v))
    while not q.empty():
        u=Node(0,0,0,0.0,temp)
        v.bound, v= q.get()
        u.level=v.level+1

        u.weight=v.weight+w[u.level]
        u.profit=v.profit+p[u.level]
        u.bound=compBound1(u)
        u.include=v.include[:]
        if u.weight<=W and u.profit>maxProfit:
            maxProfit=u.profit
            bestset=u.include[:]
            
        if u.bound>maxProfit:
            q.put((u.bound,u))
        u.weight=v.weight
        u.profit=v.profit
        u.include=v.include[:]
        if u.bound>maxProfit:
            q.put((u.bound,u))



def compBound1(u):
    if u.weight>=W:
        return 0
    else:
        result=u.profit
        j=u.level+1
        totweight=u.weight
        while (j<n-1 and totweight+w[j]<=W):
            totweight=totweight+w[j]
            result=result+p[j]
            j+=1
        k=j
        if k<=n-1:
            result=result+(W-totweight)*p[k]/w[k]
        return result
    


n=4
W=16
p=[40,30,50,10]
w=[2,5,10,5]
include=[0]*n
maxProfit =0
bestset=n*[0]
kp_BFS()
print(bestset)

print()

print("kp_Best_FS")



def kp_Best_FS():
    global maxProfit
    global bestset
    temp = n*[0]
    v = Node(-1,0,0, 0.0 ,temp)

    v.bound = compBound(v)
    q = queue.PriorityQueue()
    q.put((v.bound,v))
    while not q.empty():
        v.bound, v= q.get()
        if(v.bound < maxProfit):
            u = Node(0,0,0, 0.0, temp)
            u.level = v.level+1
            u.weight = v.weight + w[u.level]
            u.profit = v.profit + p[u.level]
            u.include = v.include[:]
            u.include[u.level]=1
            u.bound = compBound(u)
            if u.weight <= W and u.profit > maxProfit:
                maxProfit = -u.profit
                bestset = u.include[:]

            if u.bound < maxProfit:
                q.put((u.bound,u))
            u = Node(0,0,0, 0.0, temp)
            u.weight = v.weight
            u.profit = v.profit
            u.include = v.include[:]
            u.level = v.level+1
            u.bound = compBound(u)
            if u.bound < maxProfit:
                q.put((u.bound,u))
    print(u.include, u.bound)

    
def compBound(u):
    if u.weight>=W:
        return 0
    else:
        result=u.profit
        j=u.level+1
        totweight=u.weight
        while (j<n-1 and totweight+w[j] <=W):
            totweight=totweight+w[j]
            result=result+p[j]
            j+=1
        k=j
        if k<=n-1:
            result=result+(W-totweight)*p[k]/w[k]
        return -result
    


n=4
W=16
p=[40,30,50,10]
w=[2,5,10,5]
include=[0]*n
maxProfit=0
bestset=n*[0]
kp_Best_FS()
