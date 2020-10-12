'''
(1) 7쪽: [실습프로그램] 빠른정렬 프로그램
(2) 21쪽: [실습프로그램] 쉬트라센 알고리즘
'''
import numpy as np

def quicksort(s, low, high):
    if (high>low):
        pivot=partition(s,low,high)
        quicksort(s,low,pivot-1)
        quicksort(s,pivot+1,high)
    return s

def partition(s, low, high):
    pivot=s[low]
    j=low
    for i in range(low+1, high+1):
        if s[i]<pivot:
            j+=1
            s[i],s[j]=s[j],s[i]
    pivotpoint=j
    s[low],s[pivotpoint]=s[pivotpoint],s[low]
    return pivotpoint
    
s=[3,5,2,9,10,14,4,8]
print("정렬 전: ")
print(s)
print("정렬 후: ")
quicksort(s,0,7)
print(s, '\n')




def strassen(n, A, B):
    A=np.array(A)
    B=np.array(B)
    def split(mat):
        row, col = mat.shape
        return mat[:row//2, :col//2], mat[:row//2, col//2:], mat[row//2:, :col//2], mat[row//2:, col//2:]

    threshold=2
#    C=np.array([A[rows][cols] for cols in range(int(n/2)) for rows in range(int(n/2))])
    if (n==1):
        return A*B
    
    elif (n<=threshold):
        return (np.matrix(A)*np.matrix(B).tolist())

    else:
        new_size = int(n/2)
        
        a11, a12, a21, a22 = split(A)
        b11, b12, b21, b22 = split(B)
        
        
        m1=strassen(new_size, a11+a22, b11+b22)
        m2=strassen(new_size, a21+a22, b11)
        m3=strassen(new_size, a11, b12-b22)
        m4=strassen(new_size, a22, b21-b11)
        m5=strassen(new_size, a11+a12, b22)
        m6=strassen(new_size, a21-a11, b11+b12)
        m7=strassen(new_size, a12-a22, b21+b22)

        c11=m1+m4-m5+m7
        c12=m3+m5
        c21=m2+m4
        c22=m1+m3-m2+m6

        C=np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))
    return C


n=4
A=[ [1,2,0,2], [3,1,0,0], [0,1,1,2], [2,0,2,0] ]
B=[ [0,3,0,2], [1,1,4,0], [1,1,0,2], [0,5,2,0] ]

C = (np.matrix(A)*np.matrix(B).tolist())

D = [[0 for cols in range(n)]for rows in range(n)]
print("일반 곱셈: \n", C)
print('\n')

D=strassen(n, A, B)
print("쉬트라센 곱셈: \n", D)

