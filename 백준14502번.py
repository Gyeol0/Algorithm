import itertools
import copy
N,M=input().split()
N=int(N)
M=int(M)
dx=[0,0,1,-1]
dy=[1,-1,0,0]
graph=[]
vi=[]
wall=[]
queue=[]
min1=10000000
a1=0
a2=0
for i in range(N):
    
    a=list(input().split())
    a=list(map(int,a))
    graph.append(a)
for i in range(N):
    for j in range(M):
        if graph[i][j]==2:
            queue.append([i,j])
            a2+=1

        if graph[i][j]==0:
            wall.append([i,j])
        if graph[i][j]==1:
            a1+=1
www=list(itertools.combinations(wall,3))

for p in range(len(www)):
    b1=a1
    b2=a2
    queue1=copy.deepcopy(queue)
    graph1=copy.deepcopy(graph)
    
    for q in range(3):
        a=www[p][q][0]
        b=www[p][q][1]
        graph1[a][b]=1
    while queue1:
        x,y=queue1.pop(0)
    
        for i in range(4):
            ax=x+dx[i]
            ay=y+dy[i]
            if ax>=0 and ax<N and ay>=0 and ay<M:
                if graph1[ax][ay]==0:
                    graph1[ax][ay]=2
                    b2+=1
                    queue1.append([ax,ay])
     
                   
    if min1>b1+b2:
        min1=b1+b2

print(N*M-min1-3)