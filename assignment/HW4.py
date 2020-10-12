'''
(1) 실습노트 p5_dp_bin_floyd_chainMatrix.pptx 36쪽:
[실습프로그램] 연쇄행렬곱셈 프로그램
 
(2) 실습노트 p6_dp_OBStree_alignment.pptx 9쪽:
[실습프로그램] 최적이진검색트리 구축 알고리즘

데이터는 A, B, C, D, E 이고 p1=5/15, p2=4/15, p3=3/15, p4=2/15, p5=1/15 문제의 답

- 행렬 출력을 위해 포함되어 있는 utility를 사용하여도 되고, 별도로 필요한 프로그램을 작성하여도 됨.
단순히 출력형식을 지정하여 출력하여도 무방.

입력 데이터는 프로그램 내에 직접 넣어도 됨. 단, 입력 후 처리 프로그램은 그래프의 크기에 무관하게 작동하여야 함.
'''


import utility

#(1)
def order(p,i,j):
    if (i==j):
        print("A"+str(i), end="")
    else:
        k=p[i][j]
        print('(', end='')
        order(p,i,k)
        order(p,k+1,j)
        print(')', end='')
    return

d=[5,2,3,4,6,7,8]
n=len(d)-1
m=[[0 for j in range(1,n+2)] for i in range(1,n+2)]
p=[[0 for j in range(1,n+2)] for i in range(1,n+2)]

for i in range(1,n+1):
    m[i][i]=0
    
for diagonal in range(1,n):
    for i in range(1, n-diagonal+1):
        j=i+diagonal
        min=10000
        minpoint=0
        for k in range(i,j):
            if (m[i][k]+m[k+1][j]+d[i-1]*d[k]*d[j]<min):
                min=m[i][k]+m[k+1][j]+d[i-1]*d[k]*d[j]
                minpoint=k
            p[i][j]=minpoint
            m[i][j]=min
        

utility.printMatrix(m)
print()
utility.printMatrix(p)
order(p,1,6)


print()
print()


#(2)

class Node:
    def __init__(self, data):
        self.l_child=None
        self.r_chile=None
        self.data=data

def tree(key, r, i, j):
    k=r[i][j]
    if (k==0):
        return
    else:
        p=Node(key[k])
        p.l_child=tree(key, r, i, k-1)
        p.r_child=tree(key, r, k+1, j)
        return p

key=[" ","A","B","C","D"]
p=[0,0.375, 0.375, 0.125,0.125]
n=len(p)-1

a=[[0 for j in range(0,n+2)] for i in range(0,n+2)]
r=[[0 for j in range(0,n+2)] for i in range(0,n+2)]

for i in range (1,n+1):
    a[i][i-1]=0
    a[i][i]=p[i]
    r[i][i]=i
    r[i][i-1]=0
a[n+1][n]=0
r[n+1][n]=0

for diagonal in range(1,n):
    for i in range(1,n-diagonal+1):
        j=i+diagonal
        min=10000
        minpoint=0
        for k in range(i,j+1):
            psum=sum(p[i:j+1])
            if (a[i][k-1]+a[k+1][j]+psum < min):
                min=a[i][k-1]+a[k+1][j]+psum
                minpoint=k
        a[i][j]=min
        r[i][j]=minpoint                                            


utility.printMatrixF(a)
print()
utility.printMatrix(r)

root=tree(key,r,1,n)

utility.print_inOrder(root)
print()
utility.print_preOrder(root)
