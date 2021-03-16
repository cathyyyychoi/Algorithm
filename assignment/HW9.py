'''
실습노트 실습p13_sorting.pptx에서

(1) 31-33쪽: [실습과제] 방법2을 이용하여 makeHeap을 구현하고
힙정렬 알고리즘을 python으로 완성하라.
'''

import math
class Heap(object):
    n=0
    def __init__(self, data):
        self.data=data
        self.n=len(self.data)-1

    def addElt(self, elt):
        self.data.append(elt)
        self.n=len(self.data)-1
        self.siftUp(self.n)

    def siftUp(self, i):
        while(i>=2):
            if (self.data[i]>self.data[i//2]):
                temp=self.data[i//2]
                self.data[i//2]=self.data[i]
                self.data[i]=temp
            i=i//2


    def siftDown(self, i):
        siftkey = self.data[i]
        parent = i
        flag = False
        while(2*parent <= self.n and flag == False):
            if(2*parent < self.n and self.data[2*parent] < self.data[2*parent+1]):
                largerchild = 2*parent + 1
            else:
                largerchild = 2*parent
            if(siftkey < self.data[largerchild]):
                self.data[parent] = self.data[largerchild]
                parent = largerchild
            else:
                flag = True
        self.data[parent]=siftkey

    def makeHeap2(self):
        for i in range(len(self.data)//2,0,-1):
            self.siftDown(i)

    def root(self):
        keyout = self.data[1]
        self.data[1] = self.data[self.n]
        del self.data[self.n]
        self.n = self.n - 1
        if(self.n > 0):
            self.siftDown(1)
        return keyout
    
    def removeKeys(self):
        result=[]
        for i in range(self.n, 0, -1):
            a=self.root()
            result.append(a)
        return result

def heapSort(a):
    a_heap=Heap(a)
    a_heap.makeHeap2()
    return a_heap.removeKeys()

a=[0,11,14,2,7,6,3,9,5]
b=Heap(a)
b.makeHeap2()
print(b.data)
b.addElt(50)
print(b.data)
s=heapSort(a)
print(s)
