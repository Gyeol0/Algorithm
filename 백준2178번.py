N,M=input().split()
N=int(N)
M=int(M)
dx=[0,0,1,-1]
dy=[1,-1,0,0]
graph=[]
visit=[[0]*M for i in range(N)]
visit[0][0]=1
queue=[]
queue.append([0,0])
for i in range(N):
    a=input()
    a=list(map(int,a))
    graph.append(a)
while queue:
    x,y=queue.pop(0)
    if x==N-1 and y==M-1:
        print(visit[x][y])
        break
    for i in range(4):
        ax=x+dx[i]
        ay=y+dy[i]
        if ax>=0 and ax<N and ay>=0 and ay<M:
            if visit[ax][ay]==0 and graph[ax][ay]==1:
                visit[ax][ay]=visit[x][y]+1
                queue.append([ax,ay])

    
    