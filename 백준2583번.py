from collections import deque
M,N,K=map(int,input().split())
graph=[[0]*N for i in range(M)]
for _ in range(K):
    x1,y1,x2,y2=map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            graph[i][j]=1
queue=deque()
count1=0
count2=[]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
for i in range(M):
    for j in range(N):
        if graph[i][j]==0:
            count1+=1
            count=1
            queue.append([j,i])
            graph[i][j]=1
            while queue:
                y,x=queue.popleft()
                for k in range(4):
                    ax=x+dx[k]
                    ay=y+dy[k]
                    if ax>=0 and ay>=0 and ax<M and ay<N:
                        if graph[ax][ay]==0:
                            count+=1
                            queue.append([ay,ax])
                            graph[ax][ay]=1
            count2.append(count)
count2.sort()
print(count1)
for i in count2:
    print(i,end=' ')