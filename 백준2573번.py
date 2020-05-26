from collections import deque
import copy
def melt(N,M,graph):
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    aaa=[]
    for i in range(N):
        for j in range(M):
            if graph[i][j]!=0:
                count=0
                for k in range(4):
                    x=i+dx[k]
                    y=j+dy[k]
                    if x>=0 and x<N and y>=0 and y<M:
                       if graph[x][y]==0:
                           count+=1
                aaa.append([i,j,count])
    for i in range(len(aaa)):
        x=aaa[i][0]
        y=aaa[i][1]
        count=aaa[i][2]
        if graph[x][y]>count:
            graph[x][y]=graph[x][y]-count
        else:
            graph[x][y]=0

def bfs(N,M,graph):
    queue=deque()
    count1=0
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    graph1=copy.deepcopy(graph)
    for i in range(N):
        for j in range(M):
            if graph1[i][j]>0:
                queue.append([i,j])
                graph1[i][j]=-1
                count1+=1
                while queue:
                    x,y=queue.popleft()
                    
                    for k in range(4):
                        ax=x+dx[k]
                        ay=y+dy[k]
                        if ax>=0 and ay>=0 and ax<N and ay<M:
                            if graph1[ax][ay]>0:
                                graph1[ax][ay]=-1
                                queue.append([ax,ay])
    return count1
                                
N,M=input().split()
N=int(N)
M=int(M)
graph=[]
for _ in range(N):
    graph.append(list(map(int,input().split())))

count=1
year=0
while count==1:
    melt(N,M,graph)
    count=bfs(N,M,graph)
    year+=1
if count==0:
    print(0)
else:
    print(year)
