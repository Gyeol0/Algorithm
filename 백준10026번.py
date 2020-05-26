from collections import deque
N=int(input())
graph=[]
for i in range(N):
    a=list(input())
    graph.append(a)
visit=[[0]*N for i in range(N)]
visit2=[[0]*N for i in range(N)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
count1=0
count2=0

queue=deque()
queue2=deque()
for i in range(N):
    for j in range(N):
        if visit[i][j]==0:
            count1+=1
            queue.append([i,j])
            visit[i][j]=count1
            a=graph[i][j]
            while queue:
                x,y=queue.popleft()
                
                for k in range(4):
                    ax=x+dx[k]
                    ay=y+dy[k]
                    
                    if ax>=0 and ax<N and ay>=0 and ay<N:
                        if graph[ax][ay]==a and visit[ax][ay]==0:
                            visit[ax][ay]=count1
                            queue.append([ax,ay])
        if visit2[i][j]==0:
            count2+=1
            queue2.append([i,j])
            visit2[i][j]=count2
            b=graph[i][j]
            while queue2:
                x1,y1=queue2.popleft()
                
                for p in range(4):
                    ax1=x1+dx[p]
                    ay1=y1+dy[p]
                
                    if ax1>=0 and ay1>=0 and ax1<N and ay1<N:
                        if b=='R' or b=='G':
                            if (graph[ax1][ay1]=='R' or graph[ax1][ay1]=='G') and visit2[ax1][ay1]==0:
                                visit2[ax1][ay1]=count2
                                queue2.append([ax1,ay1])
                        else:
                            if graph[ax1][ay1]==b and visit2[ax1][ay1]==0:
                                visit2[ax1][ay1]=count2
                                queue2.append([ax1,ay1])
print(count1)
print(count2)

            


                    