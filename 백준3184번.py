from collections import deque
N,M=map(int,input().split())
graph=[]
for i in range(N): #입력
    a=list(input())
    graph.append(a)
dx=[0,0,1,-1]
dy=[1,-1,0,0]
V=0
O=0
for i in range(N): 
    for j in range(M):
        if graph[i][j]!='#' and graph[i][j]!='K': #울타리와 방문한 곳이 아닌 점
            queue=deque()
            countO=0
            countV=0
            if graph[i][j]=='v':
                countV+=1
            elif graph[i][j]=='o':
                countO+=1
            queue.append([i,j])
            graph[i][j]='K'
            while queue: #한 영역안의 o와 v수 Bfs
                x,y=queue.popleft()
                
                for k in range(4): #한 칸씩 이동
                    ax=x+dx[k]
                    ay=y+dy[k]
                    
                    if ax>=0 and ay>=0 and ax<N and ay<M:
                        if graph[ax][ay]!='#' and graph[ax][ay]!='K':
                            queue.append([ax,ay])
                            if graph[ax][ay]=='v':
                                countV+=1
                            elif graph[ax][ay]=='o':
                                countO+=1
                            graph[ax][ay]='K'
            if countO>countV:
                countV=0
            else:
                countO=0
            O+=countO
            V+=countV
print(O,V)