import copy
from collections import deque
N=int(input())
graph=[]
max1=[]
min1=[]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
queue=deque()
for i in range(N):
    a=list(map(int,input().split()))
    max1.append(max(a))
    min1.append(min(a))
    graph.append(a)
max2=max(max1)
min2=min(min1)
answer=[]
for i in range(min2-1,max2+1):
    graph1=copy.deepcopy(graph)
    count=0
    for j in range(N):
        for k in range(N):
            if graph1[j][k]>i:
                queue.append([j,k])
                
                while queue:
                    x,y=queue.popleft()
                    
                    for p in range(4):
                        ax=x+dx[p]
                        ay=y+dy[p]
                        if ax>=0 and ax<N and ay>=0 and ay<N:
                            if graph1[ax][ay]>i:
                                graph1[ax][ay]=0
                                queue.append([ax,ay])
                count+=1
    answer.append(count)
            
print(max(answer))