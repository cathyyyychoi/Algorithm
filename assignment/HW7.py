'''
실습노트 실습p11_sumOFsubsets_m_coloring.pptx에서

(1) 8쪽: [실습과제] 부분집합의 합 문제 해결 알고리즘을 python으로 완성하라.
모든 해를 출력하도록 작성할 것.

(2) 14쪽: [실습과제] m-coloring 문제 해결 알고리즘을 python으로 완성하라.
모든 해를 출력하도록 작성할 것.
'''

#부분집합의 합
def promising1(i, weight, total):
    return ((weight+total>=W) and (weight==W or weight+w[i+1]<=W))

def s_s(i, weight, total, include):
    if (promising1(i, weight, total)==True):
        if (W==weight):
            print("sol ", include)
        else:
            include[i+1]=1
            s_s(i+1, weight+w[i+1], total-w[i+1], include)
            include[i+1]=0
            s_s(i+1, weight, total-w[i+1], include)

n=4
w=[1,4,2,6]

W=6
print("items=",w,"W=",W)
include=n*[0]
total=0
for k in w:
    total+=k
s_s(-1,0,total,include)

print()
#m-coloring 문제
def color(i,vcolor):
    if (promising2(i,vcolor)==True):
        if (i==n1-1):
            print(vcolor)
        else:
            for j in range(1,m1+1):
                vcolor[i+1]=j
                color(i+1, vcolor)

def promising2(I, vcolor):
    switch=True
    index=0
    while (index<I and switch):
        if (W1[I][index] and vcolor[I]==vcolor[index]):
            switch=False
        index+=1
    return switch

n1=4
W1=[[0,1,1,1],[1,0,1,0],[1,1,0,1],[1,0,1,0]]
vcolor1=n*[0]
m1=3
color(-1,vcolor1)
