N=int(input())
dx=[0,0,1,-1]
dy=[1,-1,0,0]
graph=[]
queue=[]
answer=[]
for i in range(N):
    a=input()
    graph.append(list(map(int,a)))
    
for k in range(N):
    for j in range(N):
        if graph[k][j]==1:
            queue.append([k,j])
            graph[k][j]=2
            count=1
            while queue:
                x,y=queue.pop(0)
                for i in range(4):
                    ax=x+dx[i]
                    ay=y+dy[i]
                    if ax>=0 and ax<N and ay>=0 and ay<N:
                        if graph[ax][ay]==1:
                            graph[ax][ay]=2
                            count+=1
                            queue.append([ax,ay])
            answer.append(count)
answer.sort()
print(len(answer))            
for i in answer:
    print(i)