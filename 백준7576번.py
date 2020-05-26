from collections import deque
N,M=input().split()
N=int(N)
M=int(M)
dx=[0,0,1,-1]
dy=[1,-1,0,0]
graph=[]
queue=deque()
day=0
for i in range(M):
    a=list(map(int,input().split()))
    for j in range(N):
        if a[j]==1:
            queue.append([i,j])
    graph.append(a)
    
while queue:
    day+=1
    for j in range(len(queue)):
        x,y=queue.popleft()
        for i in range(4):
            ax=x+dx[i]
            ay=y+dy[i]
            if ax>=0 and ax<M and ay>=0 and ay<N:
                if graph[ax][ay]==0:
                    graph[ax][ay]=graph[x][y]+1
                    queue.append([ax,ay])
day=day-1 
for i in graph:
    if 0 in i:
        day=-1
print(day)