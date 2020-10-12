'''
각 합병정렬 알고리즘 수행에 필요한 추가적인 저장공간(합병정렬: ≒2n, 합병정렬2=n)을
계산할 수 있도록 기능을 추가하여 구현하라.
수행 종료 후 필요한 추가적인 저장공간의 개수 및 정렬된 데이터를 출력

사용한 공간을 반납하는 과정을 고려하여야 함.
프로그램이 수행되는 동안 추가공간은 재귀함수에 의해 증가 또는감소하게 됨.
추가적인 저장공간의 개수는 어느 순간에 갖고 있는 추가공간의 최대크기를 나타냅니다.

하나의 프로그램으로 작성
'''

import copy
import time

def mergeSort(n ,s):
    '''
    mergeSort1:
    Space complexity=2n
    Additional space is needed because of data replication,
    Data is duplicated to additional space u,v
    So space complexity is 2n
    '''
    h=n//2
    m=n-h
    u=[]
    v=[]
    if (n>1):
        u[0:h]=copy.copy(s[0:h])
        v[0:m+1]=copy.copy(s[h:n+1])
        mergeSort(h,u)
        mergeSort(m,v)
        merge(h,m,u,v,s)

def merge(h,m,u,v,s):
    i=j=k=0
    while ((i<h) and (j<m)):
        if u[i]<v[j]:
            s[k]=u[i]
            i+=1
        else:
            s[k]=v[j]
            j+=1
        k+=1
    if i>=h:
        s[k:h+m+1]=copy.copy(v[j:m+1])
    else:
        s[k:h+m+1]=copy.copy(u[i:h+1])
        


def mergeSort2(s, low, high):
    '''
    mergeSort2:
    Space complexity=n
    Additional space is needed for new list "u"
    n elements are appended to u, so space complexity is n
    '''
    if (low<high):
        mid=(low+high)//2
        mergeSort2(s, low, mid)
        mergeSort2(s, mid+1, high)
        merge2(s, low, mid, high)

def merge2(s, low, mid, high):
    uleft=s[low:mid+1]
    uright=s[mid+1:high+1]
    
    lindex=0
    rindex=0
    sorted_index=low

    while lindex<len(uleft) and rindex<len(uright):
        if uleft[lindex] <= uright[rindex]:
            s[sorted_index]=uleft[lindex]
            lindex=lindex+1
        else:
            s[sorted_index]=uright[rindex]
            rindex=rindex+1
        sorted_index=sorted_index+1
    while lindex<len(uleft):
        s[sorted_index]=uleft[lindex]
        lindex=lindex+1
        sorted_index=sorted_index+1
    while rindex<len(uright):
        s[sorted_index]=uright[rindex]
        rindex=rindex+1
        sorted_index=sorted_index+1
    

s=[3,5,2,9,10,14,4,8]

mergeSort(8,s)
print(s)

p=[3,5,2,9,10,14,4,8]

mergeSort2(p,0,7)
print(p)
