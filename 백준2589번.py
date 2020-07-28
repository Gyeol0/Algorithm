from collections import deque
import copy
n,m=map(int,input().split())
graph=[]
for i in range(n):
    a=list(input())
    graph.append(a)

dx=[1,-1,0,0]
dy=[0,0,1,-1]
max_count=0
map_L=[]
for i in range(n): #모서리 부분 search
    for j in range(m):
        if graph[i][j]=='L':
            count_L=0
            for k in range(4):
                x=i+dx[k]
                y=j+dy[k]
                if x>=0 and x<n and y>=0 and y<m:
                    if graph[x][y]=='L':
                        count_L+=1
            if count_L<=2 and count_L>0:
                map_L.append([i,j])
                

for i in range(len(map_L)): #BFS
    a=map_L[i][0]
    b=map_L[i][1]
    queue=deque()
    queue.append([a,b,0])
    graph_1=copy.deepcopy(graph)
    graph_1[a][b]=0
    while queue:
        x,y,count=queue.popleft()
        if max_count<count:
            max_count=count
        for k in range(4):
            ax=x+dx[k]
            ay=y+dy[k]
            if ax>=0 and ay>=0 and ax<n and ay<m:
                if graph_1[ax][ay]=='L':
                    graph_1[ax][ay]=count+1
                    queue.append([ax,ay,count+1])
print(max_count)