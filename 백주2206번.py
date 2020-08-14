from collections import deque
N,M=map(int,input().split())
graph=[]
for _ in range(N):
    graph.append(list(map(int,list(input()))))
queue=deque()
queue.append([0,0,1,1])
graph_1=[[0]*M for _ in range(N)]
graph[0][0]=2
dx=[1,-1,0,0]
dy=[0,0,1,-1]
while queue:
    x,y,d,count=queue.popleft()
    if x==N-1 and y==M-1:
        break
    for i in range(4):
        ax=x+dx[i]
        ay=y+dy[i]
        if ax>=0 and ay>=0 and ax<N and ay<M:
            if graph[ax][ay]==0:
                graph[ax][ay]=2
                graph_1[ax][ay]=d
                queue.append([ax,ay,d,count+1])
            elif graph[ax][ay]==1:
                if d>0:
                    graph_1[ax][ay]=d-1
                    queue.append([ax,ay,d-1,count+1])
            elif graph[ax][ay]==2:
                if graph_1[ax][ay]<d:
                    graph_1[ax][ay]=d
                    queue.append([ax,ay,d,count+1])
            
if graph[N-1][M-1]==0:
    print(-1)
else:
    print(count)