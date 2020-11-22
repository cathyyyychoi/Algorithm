'''
실습노트 p7_greedy_MST.pptx에서
(1) 19쪽 [실습프로그램] Kruskal 알고리즘을 python으로 완성하라. 

실습노트 p9_greedy_Dijkstra_huffman.pptx에서
(2) 9쪽: [실습프로그램] Dijkstra 알고리즘을 python으로 완성하라.
최단경로에 포함되는 아크를 출력. 각 노드로 도달하는 최단거리를 save_length 리스트에 저장한 후, 출력한다.

실습자료에 주어진 자료구조 형식 또는 부분 프로그램을 사용하지 않고, 전혀 다른 구조로 구현하여도 됨.
'''

#krustal Algorithm
parent=dict()
rank=dict()
def make_singleton_set(v):
    parent[v]=v
    rank[v]=1
    
def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(r1,r2):
    if r1!=r2:
        if rank[r1]>rank[r2]:
            parent[r2]=r1
            rank[r1]+=rank[r2]
        else:
            parent[r1]=r2
            if rank[r1]==rank[r2]:
                rank[r2]+=rank[r1]

def krustal(graph):
    for i in graph['vertices']:
        make_singleton_set(i)
    mst=set()
    edge=list(graph['edges'])
    edge.sort()
    for j in edge:
        w, ver1, ver2 = j
        p=find(ver1)
        q=find(ver2)
        if p!=q:
            union(p,q)
            mst.add(j)
    return mst

graph={
    'vertices':['A','B','C','D','E'],
    'edges':set([
        (1,'A','B'),
        (3,'A','C'),
        (3,'B','C'),
        (6,'B','D'),
        (4,'C','D'),
        (2,'C','E'),
        (5,'D','E'),
        ])
    }
mst=krustal(graph)
print('krustal algorithm')
print(mst)

print()

#Dijkstra Algorithm
inf=1000
w=[[0,7,4,6,1],[inf,0,inf,inf,inf],
   [inf,2,0,5,inf],[inf,3,inf,0,inf],[inf,inf,inf,1,0]]
n=len(w)
f=set()
touch=n*[0]
length=n*[0]

for i in range(1,n):
    touch[i]=0
    length[i]=w[0][i]
    
for i in range(1, n):
    minimum=inf
    for j in range(1,n):
        if 0<=length[j]<=minimum:
            minumum=length[j]
            vnear=j
    f.add((touch[vnear], vnear))
    for k in range(1,n):
        if length[vnear]+w[vnear][k] <length[k]:
            length[k]=w[vnear][k]+length[vnear]
            touch[k]=vnear
    length[vnear]=-1

    
print('Dijkstra algorithm')
print(f)


